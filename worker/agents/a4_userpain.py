"""A4 UserPain Agent — 客服库 RAG + 痛点真伪判定。

流程：
1) 取本 case 的 pain 段落（segment_type='pain' 或所有 segments 的 ASR 拼接 fallback）
2) 文本嵌入（DashScope text-embedding-v3，1024 dim）
3) 在 userpain_clusters.embedding 上 cosine 相似召回 top-5
4) Deepseek-V3 判定：真痛点 / 伪痛点 / 营销造痛点
5) 写 cross_validations.agent='a4_userpain'

边界：userpain_clusters 为空时（W0 客服库尚未导入），verdict='no_userpain_data', confidence=0
"""
from __future__ import annotations

import json
import logging

from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..embeddings import embed_text
from ..llm import call_deepseek

log = logging.getLogger(__name__)

JUDGE_SYSTEM = """你是用户研究专家。给定一段保健品脚本的痛点叙述，以及来自客服 / 私域系统的 5 个真实
用户痛点 cluster（每个含 cluster 标签 + 代表性 quotes），判断脚本中描述的痛点属于哪一类：

- real_pain      — 与真实用户 cluster 高度匹配，是真痛点
- fake_pain      — 与真实 cluster 不匹配或无对应，疑似脚本编造
- marketing_pain — 真实用户提及但被脚本放大或扭曲（情绪化营销）
- uncertain      — 信息不足

输出严格 JSON：{"verdict": "real_pain|fake_pain|marketing_pain|uncertain",
                 "confidence": 0.0-1.0,
                 "reasoning": "...",
                 "matched_cluster_label": "..." | null}"""


def _collect_pain_text(s, case_id: str) -> str:
    rows = s.execute(
        text(
            """
            SELECT segment_type, asr_text, ocr_text, llm_analysis
            FROM case_segments
            WHERE case_id = :cid
              AND (segment_type = 'pain' OR asr_text IS NOT NULL)
            ORDER BY COALESCE(start_sec, 0)
            """
        ),
        {"cid": case_id},
    ).all()

    pain_only = [r for r in rows if r.segment_type == "pain"]
    target = pain_only or rows

    parts: list[str] = []
    for r in target:
        if r.asr_text:
            parts.append(r.asr_text)
        if r.llm_analysis:
            try:
                la = r.llm_analysis if isinstance(r.llm_analysis, dict) else json.loads(r.llm_analysis)
                if la.get("summary"):
                    parts.append(la["summary"])
            except (json.JSONDecodeError, TypeError):
                pass
    return "\n".join(p for p in parts if p)


def _topk_clusters(s, vec: list[float], k: int = 5) -> list[dict]:
    rows = s.execute(
        text(
            """
            SELECT id, cluster_label, representative_quotes, source_count,
                   1 - (embedding <=> CAST(:v AS vector)) AS similarity
            FROM userpain_clusters
            WHERE embedding IS NOT NULL
            ORDER BY embedding <=> CAST(:v AS vector)
            LIMIT :k
            """
        ),
        {"v": str(vec), "k": k},
    ).mappings().all()
    return [dict(r) for r in rows]


@activity.defn
async def match_userpain(case_id: str) -> dict:
    activity.logger.info("A4 UserPain matching case_id=%s", case_id)

    with session_scope() as s:
        pain_text = _collect_pain_text(s, case_id)
        if not pain_text.strip():
            s.execute(
                text(
                    """
                    INSERT INTO cross_validations (case_id, agent, verdict, confidence, raw_data)
                    VALUES (:cid, 'a4_userpain', 'no_pain_text', 0.0, CAST(:p AS JSONB))
                    """
                ),
                {"cid": case_id, "p": json.dumps({"reason": "no pain segments"})},
            )
            return {"verdict": "no_pain_text"}

        cluster_count = s.execute(
            text("SELECT COUNT(*) FROM userpain_clusters WHERE embedding IS NOT NULL")
        ).scalar_one()
        if cluster_count == 0:
            s.execute(
                text(
                    """
                    INSERT INTO cross_validations (case_id, agent, verdict, confidence, raw_data)
                    VALUES (:cid, 'a4_userpain', 'no_userpain_data', 0.0, CAST(:p AS JSONB))
                    """
                ),
                {
                    "cid": case_id,
                    "p": json.dumps({"reason": "userpain_clusters empty — import customer log first"}),
                },
            )
            return {"verdict": "no_userpain_data"}

        vec = embed_text(pain_text)
        top = _topk_clusters(s, vec, k=5)

        user_msg = f"""脚本痛点叙述：
{pain_text}

候选真实痛点 cluster（按相似度降序）：
{json.dumps(top, ensure_ascii=False, indent=2, default=str)}

按 system 中的格式输出 JSON。"""

        try:
            raw = call_deepseek(JUDGE_SYSTEM, user_msg, temperature=0.1, response_format_json=True)
            judgment = json.loads(raw)
        except Exception as e:
            log.warning("A4 LLM judgment failed: %s", e)
            judgment = {"verdict": "uncertain", "confidence": 0.0, "reasoning": str(e)}

        verdict = judgment.get("verdict", "uncertain")
        confidence = float(judgment.get("confidence", 0.0))

        s.execute(
            text(
                """
                INSERT INTO cross_validations (case_id, agent, verdict, confidence, raw_data)
                VALUES (:cid, 'a4_userpain', :v, :c, CAST(:p AS JSONB))
                """
            ),
            {
                "cid": case_id,
                "v": verdict,
                "c": confidence,
                "p": json.dumps(
                    {"top_clusters": top, "judgment": judgment, "pain_text": pain_text[:1000]},
                    ensure_ascii=False,
                    default=str,
                ),
            },
        )

        if confidence < 0.6:
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
                            "agent": "a4_userpain",
                            "case_id": case_id,
                            "verdict": verdict,
                            "confidence": confidence,
                            "reasoning": judgment.get("reasoning"),
                        },
                        ensure_ascii=False,
                    )
                },
            )

    activity.logger.info("A4 UserPain done case_id=%s verdict=%s conf=%.2f", case_id, verdict, confidence)
    return {"verdict": verdict, "confidence": confidence}
