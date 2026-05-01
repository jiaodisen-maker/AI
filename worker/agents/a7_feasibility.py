"""A7 Feasibility Agent — 多 LLM 互评 4 维机器友好度 + 不及格原子改写。

4 维（每维 1-10）：
- machine     LLM 能否稳定生成？需多少 few-shot？
- data        组装该原子需多少字段 / 数据栈是否支持？
- compliance  能否前置硬规则拦住？还是必须人审？
- orthogonal  与其它原子是否解耦？

互评家族（与 v6 §14.9 护栏一致：≥3 个不同家族）：Deepseek / Qwen / Claude
任何维 ≤4 → Deepseek 改写一次（生成新 atom，created_by_agent='a7-rewrite'，原 atom 标 deprecated 字段缺失，
留作后续 schema 演进；W2 阶段我们保留新旧两条 atom，旧的不删，由 A8/A9 决定取舍）。

写 cross_validations.agent='a7_feasibility' 汇总。
"""
from __future__ import annotations

import json
import logging
import statistics

from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..llm import call_claude, call_deepseek, call_qwen

log = logging.getLogger(__name__)

DIMS = ["machine", "data", "compliance", "orthogonal"]

RUBRIC_SYSTEM = """你是 LLM 应用工程评审专家。给定一条保健品脚本"原子"（hook/pain/trust/cta 之一），
按 4 维评分（每维 1-10 整数）：

- machine     LLM 能否稳定生成同质化输出？需要多少 few-shot 才能稳？
- data        生成该原子需要从多少字段拼装？数据依赖度越低越好。
- compliance  能否用规则 / 词库 / 元数据前置拦住违规？无法自动化则低分。
- orthogonal  与同类其它原子是否在概念上解耦？高度重叠或必须共现 → 低分。

输出严格 JSON：{"machine": 1-10, "data": 1-10, "compliance": 1-10, "orthogonal": 1-10, "reasoning": "..."}"""


REWRITE_SYSTEM = """你是保健品文案重构专家。下面给你一条原子（任一维度被评为 ≤4 分），请重写为
一条"机器友好 + 数据轻 + 合规可控 + 概念正交"的等价原子，保留意图但提升可机器化能力。
输出严格 JSON：{"content": "...", "reasoning": "..."}"""


def _score_one(content: str, atom_type: str) -> dict:
    user = f"原子类型：{atom_type}\n内容：{content}\n按 system 中的 4 维输出 JSON。"
    out_d = json.loads(call_deepseek(RUBRIC_SYSTEM, user, temperature=0.0, response_format_json=True))
    out_q = call_qwen(RUBRIC_SYSTEM, user, temperature=0.0)
    out_c = call_claude(RUBRIC_SYSTEM, user)

    def _try_parse(raw: str) -> dict:
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            start = raw.find("{")
            end = raw.rfind("}")
            if start >= 0 and end > start:
                try:
                    return json.loads(raw[start : end + 1])
                except json.JSONDecodeError:
                    pass
        return {}

    parsed = {"deepseek": out_d, "qwen": _try_parse(out_q), "claude": _try_parse(out_c)}

    avg: dict[str, float] = {}
    for d in DIMS:
        vals = []
        for src in parsed.values():
            v = src.get(d)
            if isinstance(v, int | float):
                vals.append(float(v))
        avg[d] = round(statistics.mean(vals), 2) if vals else 0.0

    return {"per_evaluator": parsed, "avg": avg, "min": min(avg.values()) if avg else 0.0}


def _maybe_rewrite(content: str, atom_type: str, weak_dim: str) -> dict | None:
    user = f"原子类型：{atom_type}\n原内容：{content}\n薄弱维度：{weak_dim}\n请重写。"
    try:
        out = call_deepseek(REWRITE_SYSTEM, user, temperature=0.5, response_format_json=True)
        return json.loads(out)
    except Exception as e:
        log.warning("A7 rewrite failed: %s", e)
        return None


@activity.defn
async def score_feasibility(case_id: str) -> dict:
    activity.logger.info("A7 Feasibility scoring case_id=%s", case_id)

    with session_scope() as s:
        atoms = s.execute(
            text(
                """
                SELECT id, atom_type, content, source_segment_id, compliance_grade
                FROM atoms
                WHERE source_case_id = :cid AND created_by_agent = 'a2'
                """
            ),
            {"cid": case_id},
        ).all()

        rewritten = 0
        all_avg: list[dict] = []

        for a in atoms:
            try:
                scoring = _score_one(a.content, a.atom_type)
            except Exception as e:
                log.warning("A7 scoring atom=%s failed: %s", a.id, e)
                continue

            avg = scoring["avg"]
            min_v = scoring["min"]
            all_avg.append({"atom_id": str(a.id), "avg": avg, "min": min_v})

            s.execute(
                text("UPDATE atoms SET feasibility_4d = CAST(:f AS JSONB) WHERE id = :id"),
                {"f": json.dumps(scoring, ensure_ascii=False), "id": a.id},
            )

            if min_v <= 4:
                weak_dim = min(avg, key=avg.get) if avg else "machine"
                rw = _maybe_rewrite(a.content, a.atom_type, weak_dim)
                if rw and rw.get("content"):
                    s.execute(
                        text(
                            """
                            INSERT INTO atoms (
                                atom_type, content,
                                source_case_id, source_segment_id,
                                compliance_grade, created_by_agent
                            )
                            VALUES (:t, :c, :cid, :sid, :grade, 'a7-rewrite')
                            """
                        ),
                        {
                            "t": a.atom_type,
                            "c": rw["content"],
                            "cid": case_id,
                            "sid": a.source_segment_id,
                            "grade": a.compliance_grade,
                        },
                    )
                    rewritten += 1

        if all_avg:
            overall = {
                d: round(statistics.mean([row["avg"].get(d, 0) for row in all_avg]), 2)
                for d in DIMS
            }
            verdict = "ok" if min(overall.values()) >= 6 else "rewrite_needed"
            confidence = 0.8
        else:
            overall = {d: 0.0 for d in DIMS}
            verdict = "no_atoms"
            confidence = 0.0

        s.execute(
            text(
                """
                INSERT INTO cross_validations (case_id, agent, verdict, confidence, raw_data)
                VALUES (:cid, 'a7_feasibility', :v, :c, CAST(:p AS JSONB))
                """
            ),
            {
                "cid": case_id,
                "v": verdict,
                "c": confidence,
                "p": json.dumps(
                    {
                        "atom_count": len(all_avg),
                        "rewritten": rewritten,
                        "overall_avg": overall,
                        "per_atom": all_avg,
                    },
                    ensure_ascii=False,
                ),
            },
        )

    activity.logger.info(
        "A7 Feasibility done case_id=%s atoms=%d rewritten=%d verdict=%s",
        case_id,
        len(all_avg),
        rewritten,
        verdict,
    )
    return {"verdict": verdict, "atom_count": len(all_avg), "rewritten": rewritten, "avg": overall}
