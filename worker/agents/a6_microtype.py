"""A6 Microtype Agent — 5 维归类 + candidate 提案。

流程：
1) LLM 从 case + atoms 抽取 5 维标签（严格落 microtype_schema.yaml 允许值集合）
2) SELECT microtypes WHERE (scene, audience, ingredient, emotion, restriction) 匹配 + status='active'
3) 命中：UPDATE atoms.microtype_ids = array_append(...) WHERE source_case_id = :cid
4) 未命中：INSERT microtypes(...) VALUES (..., status='candidate', proposed_by_agent=true)
   并写 hitl_alert(new_microtype) 通知人审定
"""
from __future__ import annotations

import json
import logging
from functools import lru_cache
from pathlib import Path

import yaml
from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..llm import call_deepseek

log = logging.getLogger(__name__)

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "rules" / "microtype_schema.yaml"


@lru_cache(maxsize=1)
def _load_schema() -> dict:
    raw = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    return {
        "scenes": [d["id"] for d in raw["scenes"]],
        "audiences": [d["id"] for d in raw["audiences"]],
        "ingredients": [d["id"] for d in raw["ingredients"]],
        "emotions": [d["id"] for d in raw["emotions"]],
        "restrictions": [d["id"] for d in raw["restrictions"]],
    }


def _build_extraction_system() -> str:
    sch = _load_schema()
    return f"""你是保健品内容微类型分类器。给定 case 信息，从下列 5 个维度的允许值集合中各选 1 个。
不要输出集合外的值，不要输出空值（必须 5 维齐备）。

scenes (场景)         允许值: {sch["scenes"]}
audiences (人群)      允许值: {sch["audiences"]}
ingredients (成分)    允许值: {sch["ingredients"]}
emotions (情绪)       允许值: {sch["emotions"]}
restrictions (限制)   允许值: {sch["restrictions"]}

输出严格 JSON：
{{"scene":"...","audience":"...","ingredient":"...","emotion":"...","restriction":"...","reasoning":"简要说明"}}"""


def _validate_tags(tags: dict) -> tuple[bool, str]:
    sch = _load_schema()
    pairs = [
        ("scene", "scenes"),
        ("audience", "audiences"),
        ("ingredient", "ingredients"),
        ("emotion", "emotions"),
        ("restriction", "restrictions"),
    ]
    for k, sk in pairs:
        v = tags.get(k)
        if not v:
            return False, f"missing {k}"
        if v not in sch[sk]:
            return False, f"{k}={v!r} not in allowed set"
    return True, ""


@activity.defn
async def classify_microtype(case_id: str) -> dict:
    activity.logger.info("A6 Microtype classifying case_id=%s", case_id)

    with session_scope() as s:
        case_row = s.execute(
            text("SELECT brand, sku, category, raw_meta FROM cases WHERE id = :id"),
            {"id": case_id},
        ).first()

        seg_rows = s.execute(
            text(
                """
                SELECT segment_type, asr_text, llm_analysis
                FROM case_segments WHERE case_id = :cid
                ORDER BY COALESCE(start_sec, 0)
                """
            ),
            {"cid": case_id},
        ).all()

        atom_rows = s.execute(
            text("SELECT atom_type, content FROM atoms WHERE source_case_id = :cid"),
            {"cid": case_id},
        ).all()

        case_summary = {
            "brand": case_row.brand if case_row else None,
            "sku": case_row.sku if case_row else None,
            "category": case_row.category if case_row else None,
            "segments": [
                {"type": r.segment_type, "text": (r.asr_text or "")[:200]} for r in seg_rows
            ],
            "atoms": [{"type": r.atom_type, "content": r.content[:160]} for r in atom_rows],
        }

        try:
            raw = call_deepseek(
                _build_extraction_system(),
                json.dumps(case_summary, ensure_ascii=False, indent=2),
                temperature=0.0,
                response_format_json=True,
            )
            tags = json.loads(raw)
        except Exception as e:
            log.warning("A6 LLM extraction failed: %s", e)
            tags = {}

        ok, err = _validate_tags(tags)
        if not ok:
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
                            "agent": "a6_microtype",
                            "case_id": case_id,
                            "reason": "extraction_failed",
                            "error": err,
                            "raw_tags": tags,
                        },
                        ensure_ascii=False,
                    )
                },
            )
            activity.logger.warning("A6 extraction invalid: %s", err)
            return {"matched": False, "reason": "extraction_failed", "error": err}

        existing = s.execute(
            text(
                """
                SELECT id, status FROM microtypes
                WHERE scene = :s AND audience = :a AND ingredient = :i
                  AND emotion = :e AND restriction = :r
                """
            ),
            {
                "s": tags["scene"],
                "a": tags["audience"],
                "i": tags["ingredient"],
                "e": tags["emotion"],
                "r": tags["restriction"],
            },
        ).first()

        if existing and existing.status == "active":
            mt_id = str(existing.id)
            matched = True
            s.execute(
                text(
                    """
                    UPDATE atoms
                    SET microtype_ids = (
                      CASE
                        WHEN microtype_ids IS NULL
                          THEN ARRAY[CAST(:m AS UUID)]
                        WHEN NOT (microtype_ids @> ARRAY[CAST(:m AS UUID)])
                          THEN microtype_ids || CAST(:m AS UUID)
                        ELSE microtype_ids
                      END
                    )
                    WHERE source_case_id = :cid
                    """
                ),
                {"m": mt_id, "cid": case_id},
            )
        else:
            if existing is None:
                mt_id = str(
                    s.execute(
                        text(
                            """
                            INSERT INTO microtypes (
                                scene, audience, ingredient, emotion, restriction,
                                status, proposed_by_agent
                            )
                            VALUES (:s, :a, :i, :e, :r, 'candidate', TRUE)
                            RETURNING id
                            """
                        ),
                        {
                            "s": tags["scene"],
                            "a": tags["audience"],
                            "i": tags["ingredient"],
                            "e": tags["emotion"],
                            "r": tags["restriction"],
                        },
                    ).scalar_one()
                )
            else:
                mt_id = str(existing.id)
            matched = False
            s.execute(
                text(
                    """
                    INSERT INTO hitl_alerts (alert_type, payload)
                    VALUES ('new_microtype', CAST(:p AS JSONB))
                    """
                ),
                {
                    "p": json.dumps(
                        {
                            "case_id": case_id,
                            "microtype_id": mt_id,
                            "tags": tags,
                            "reasoning": tags.get("reasoning"),
                        },
                        ensure_ascii=False,
                    )
                },
            )

    activity.logger.info(
        "A6 Microtype done case_id=%s mt_id=%s matched=%s", case_id, mt_id, matched
    )
    return {"matched": matched, "microtype_id": mt_id, "tags": tags}
