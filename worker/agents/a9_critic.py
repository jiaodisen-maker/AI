"""A9 Critic Agent — 核心闭环：≥3 家 LLM 互评 + DSPy prompt 自优化触发。

7 维 rubric：hook / pain / trust / cta / compliance / creativity / exec — 各 1-10
互评家族：Deepseek-V3 / Qwen-Max / Claude-Haiku-4.5 (claude-haiku-4-5-20251001)

confidence = 1 - normalized_variance（三家分歧越小，confidence 越高）
confidence < 0.6 → hitl_alert(low_confidence)

DSPy 触发：每完成 K=5 个 case 的 critique 后调用 dspy.optimizer.maybe_optimize('a8')，
新 prompt 在 holdout 上若不优于旧 prompt 则不写 prompt_versions（回滚机制）。
"""
from __future__ import annotations

import json
import logging
import statistics
from typing import Any

from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..llm import call_claude, call_deepseek, call_qwen

log = logging.getLogger(__name__)

DIMS = ["hook", "pain", "trust", "cta", "compliance", "creativity", "exec"]

CRITIC_SYSTEM = """你是保健品抖音脚本评审专家。给定一条新生成的脚本 + 它对标的原 case 9 段拆解，
按 7 维评分（每维 1-10 整数），并解释打分理由。

7 维:
- hook        开场 3 秒抓注意力的强度 / 创意度
- pain        痛点呈现是否精准 / 共鸣感
- trust       信任建立元素的可信度（无患者证言、无虚构权威）
- cta         CTA 引导力
- compliance  合规风险（10=完全合规, 1=高危违规）
- creativity  原创度（1=与原 case 雷同，10=结构相同但创意全新）
- exec        可执行度（拍摄难度 / 真人友好度 / 数字人不友好则降分）

输出严格 JSON（不要 markdown）：
{"scores": {"hook":1-10,"pain":1-10,"trust":1-10,"cta":1-10,"compliance":1-10,"creativity":1-10,"exec":1-10},
 "reasoning": "..."}"""


CRITIC_TRIGGER_K = 5  # 累计 K 个 case critique 后触发 DSPy


def _try_parse_json(raw: str) -> dict:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(raw[start : end + 1])
            except json.JSONDecodeError:
                return {}
        return {}


def _evaluate_one(script_text: str, case_summary: str) -> dict:
    user = f"""原 case 9 段拆解概览:
{case_summary}

新生成脚本:
{script_text}

按 system 中的 7 维输出 JSON。"""

    out_d = call_deepseek(CRITIC_SYSTEM, user, temperature=0.0, response_format_json=True)
    out_q = call_qwen(CRITIC_SYSTEM, user, temperature=0.0)
    out_c = call_claude(CRITIC_SYSTEM, user)

    return {
        "deepseek-chat": _try_parse_json(out_d),
        "qwen-max-latest": _try_parse_json(out_q),
        "claude-haiku-4-5": _try_parse_json(out_c),
    }


def _agg_scores(per_evaluator: dict) -> tuple[dict, float]:
    """Return (avg_per_dim, confidence ∈ [0,1])."""
    avg: dict[str, float] = {}
    variances: list[float] = []
    for d in DIMS:
        vals = []
        for src in per_evaluator.values():
            v = (src.get("scores") or {}).get(d) if isinstance(src.get("scores"), dict) else None
            if isinstance(v, int | float):
                vals.append(float(v))
        if vals:
            avg[d] = round(statistics.mean(vals), 2)
            if len(vals) >= 2:
                variances.append(statistics.pvariance(vals))
        else:
            avg[d] = 0.0

    if not variances:
        confidence = 0.0
    else:
        # max possible variance for 1-10 range w/ 3 evaluators ≈ 18
        mean_var = statistics.mean(variances)
        confidence = max(0.0, min(1.0, 1.0 - mean_var / 18.0))
    return avg, round(confidence, 2)


def _build_case_summary(s, case_id: str) -> str:
    rows = s.execute(
        text(
            """
            SELECT segment_type, asr_text
            FROM case_segments WHERE case_id = :cid
            ORDER BY COALESCE(start_sec, 0)
            """
        ),
        {"cid": case_id},
    ).all()
    return "\n".join(f"[{r.segment_type}] {(r.asr_text or '')[:200]}" for r in rows)


def _maybe_trigger_dspy(s) -> bool:
    """判断是否应触发 DSPy 优化（每 K 个 critique 触发一次）。"""
    last_trigger = s.execute(
        text(
            """
            SELECT MAX(created_at) AS ts FROM prompt_versions WHERE agent = 'a8'
            """
        )
    ).scalar()
    cnt = s.execute(
        text(
            """
            SELECT COUNT(*) FROM critic_scores
            WHERE target_type = 'generated_script'
              AND scored_at > COALESCE(:since, '1970-01-01'::timestamptz)
            """
        ),
        {"since": last_trigger},
    ).scalar_one()
    return cnt >= CRITIC_TRIGGER_K


@activity.defn
async def critique(payload: dict[str, Any]) -> dict[str, Any]:
    case_id: str = payload["case_id"]
    script_ids: list[str] = payload.get("script_ids") or []
    activity.logger.info("A9 Critic case_id=%s scripts=%d", case_id, len(script_ids))

    if not script_ids:
        return {"avg_score": None, "confidence": None, "dspy_triggered": False, "reason": "no_scripts"}

    all_avg: list[dict] = []
    all_conf: list[float] = []
    low_conf_count = 0

    with session_scope() as s:
        case_summary = _build_case_summary(s, case_id)

        for sid in script_ids:
            row = s.execute(
                text("SELECT output FROM generated_scripts WHERE id = :id"), {"id": sid}
            ).first()
            if row is None:
                continue
            try:
                per_eval = _evaluate_one(row.output, case_summary)
            except Exception as e:
                log.warning("A9 evaluator failure script_id=%s: %s", sid, e)
                continue

            avg, conf = _agg_scores(per_eval)
            all_avg.append(avg)
            all_conf.append(conf)
            if conf < 0.6:
                low_conf_count += 1

            for evaluator, scoring in per_eval.items():
                s.execute(
                    text(
                        """
                        INSERT INTO critic_scores (
                            target_id, target_type, evaluator_model,
                            scores, reasoning, confidence
                        )
                        VALUES (
                            :tid, 'generated_script', :model,
                            CAST(:sc AS JSONB), :rs, :cf
                        )
                        """
                    ),
                    {
                        "tid": sid,
                        "model": evaluator,
                        "sc": json.dumps(scoring.get("scores") or {}, ensure_ascii=False),
                        "rs": scoring.get("reasoning"),
                        "cf": conf,
                    },
                )

            if conf < 0.6:
                s.execute(
                    text(
                        """
                        INSERT INTO hitl_alerts (alert_type, payload)
                        VALUES ('low_confidence', CAST(:p AS JSONB))
                        """
                    ),
                    {
                        "p": json.dumps(
                            {
                                "agent": "a9_critic",
                                "case_id": case_id,
                                "script_id": sid,
                                "avg": avg,
                                "confidence": conf,
                                "evaluators": list(per_eval.keys()),
                            },
                            ensure_ascii=False,
                        )
                    },
                )

        # 触发 DSPy（在事务外做副作用 — 但 commit 之后再调）
        should_trigger = _maybe_trigger_dspy(s)

    dspy_triggered = False
    dspy_outcome: dict | None = None
    if should_trigger:
        try:
            from dspy_opt.optimizer import maybe_optimize

            dspy_outcome = maybe_optimize("a8")
            dspy_triggered = bool(dspy_outcome and dspy_outcome.get("inserted"))
        except Exception as e:
            log.warning("A9 DSPy optimize failed (non-fatal): %s", e)
            dspy_outcome = {"error": str(e)}

    if all_avg:
        overall = {d: round(statistics.mean([a.get(d, 0) for a in all_avg]), 2) for d in DIMS}
        avg_conf = round(statistics.mean(all_conf), 2)
    else:
        overall = {d: 0.0 for d in DIMS}
        avg_conf = 0.0

    activity.logger.info(
        "A9 Critic done case_id=%s avg=%s conf=%.2f low_conf=%d dspy=%s",
        case_id,
        overall,
        avg_conf,
        low_conf_count,
        dspy_triggered,
    )
    return {
        "avg_score": overall,
        "confidence": avg_conf,
        "low_confidence_count": low_conf_count,
        "dspy_triggered": dspy_triggered,
        "dspy_outcome": dspy_outcome,
    }
