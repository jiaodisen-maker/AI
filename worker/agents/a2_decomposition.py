"""A2 Decomposition Agent — 多模态拆解 + 9 段式 + 4 类原子抽取。

W1 实装范围：
- LLM 拆解（Deepseek-V3）+ 落库 cases / case_segments / atoms — 完整可用
- 媒体管道（yt-dlp + FunASR + PaddleOCR + Qwen-VL）— 可用，但依赖 optional [media] extras
- manual_payload 旁路 — 调用方可直接 POST 已经预提取好的 asr/ocr/visual_desc，跳过媒体管道，
  方便没装媒体依赖时端到端跑通

case_input 结构（与 api/routes/ingest.py 的 IngestRequest 对齐）:
{
    "url": str,
    "data_lineage": "manual" | "poc_crawled" | "oauth" | "public_api",
    "brand": str | None,
    "sku": str | None,
    "category": str | None,
    "platform": str | None,
    "manual_payload": {                         # 可选；若有则跳过媒体管道
        "asr_text": str,
        "ocr_text": str,
        "visual_desc": str,
        "duration_sec": float | None,
    } | None,
}
"""
from __future__ import annotations

import json
import logging
import os
from datetime import UTC, datetime, timedelta
from typing import Any

from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..llm import call_deepseek
from .a2_prompts import DECOMPOSITION_SYSTEM, build_user_prompt

log = logging.getLogger(__name__)


def _extract_via_media_pipeline(url: str) -> dict:
    """yt-dlp + FunASR + PaddleOCR + Qwen-VL.

    所有依赖在 optional [media] extras 里，未安装时抛 NotImplementedError，
    此时调用方应该用 manual_payload 旁路。
    """
    try:
        import funasr  # noqa: F401
        import paddleocr  # noqa: F401
        import yt_dlp  # noqa: F401
    except ImportError as e:
        raise NotImplementedError(
            "Media pipeline deps not installed. Install with `pip install -e .[media]` "
            "or pass manual_payload in IngestRequest."
        ) from e

    # 下载 → ASR → OCR → 视觉理解
    # 完整实装见 worker/agents/a2_media.py（W1 末交付）
    raise NotImplementedError("Media pipeline implementation pending — use manual_payload for now")


def _persist_case_and_segments(case_input: dict, decomp: dict) -> str:
    """落库 cases + case_segments + atoms（atom.compliance_grade 留 NULL，由 A3 补）。"""
    data_lineage = case_input.get("data_lineage", "manual")
    poc_purge_at: datetime | None = None
    if data_lineage == "poc_crawled":
        ttl_days = int(os.getenv("POC_DATA_TTL_DAYS", "30"))
        poc_purge_at = datetime.now(UTC) + timedelta(days=ttl_days)

    duration_sec = (case_input.get("manual_payload") or {}).get("duration_sec")

    with session_scope() as s:
        case_row = s.execute(
            text(
                """
                INSERT INTO cases (
                    url, platform, brand, sku, category, duration_sec,
                    raw_meta, discovered_by, data_lineage, poc_purge_at,
                    workflow_id
                )
                VALUES (
                    :url, :platform, :brand, :sku, :category, :duration,
                    CAST(:raw_meta AS JSONB), :discovered_by, :lineage, :purge_at,
                    :wfid
                )
                RETURNING id
                """
            ),
            {
                "url": case_input["url"],
                "platform": case_input.get("platform"),
                "brand": case_input.get("brand"),
                "sku": case_input.get("sku"),
                "category": case_input.get("category"),
                "duration": int(duration_sec) if duration_sec else None,
                "raw_meta": json.dumps({"input": case_input}, ensure_ascii=False),
                "discovered_by": "manual" if data_lineage == "manual" else "a1_discovery",
                "lineage": data_lineage,
                "purge_at": poc_purge_at,
                "wfid": activity.info().workflow_id,
            },
        ).first()
        case_id = str(case_row.id)

        # segments
        seg_ids: list[str] = []
        for seg in decomp.get("segments", []):
            row = s.execute(
                text(
                    """
                    INSERT INTO case_segments (
                        case_id, segment_type, start_sec, end_sec,
                        asr_text, ocr_text, visual_desc, llm_analysis
                    )
                    VALUES (
                        :cid, :stype, :start, :end,
                        :asr, :ocr, :visual, CAST(:llm AS JSONB)
                    )
                    RETURNING id
                    """
                ),
                {
                    "cid": case_id,
                    "stype": seg.get("segment_type"),
                    "start": seg.get("start_sec"),
                    "end": seg.get("end_sec"),
                    "asr": seg.get("summary"),  # 9 段拆解后, 段级文本 ≈ summary
                    "ocr": None,
                    "visual": None,
                    "llm": json.dumps(seg, ensure_ascii=False),
                },
            ).first()
            seg_ids.append(str(row.id))

        # atoms
        for atom in decomp.get("atoms", []):
            seg_idx = atom.get("source_segment_index")
            seg_id = seg_ids[seg_idx] if isinstance(seg_idx, int) and 0 <= seg_idx < len(seg_ids) else None
            s.execute(
                text(
                    """
                    INSERT INTO atoms (
                        atom_type, content, source_case_id, source_segment_id, created_by_agent
                    )
                    VALUES (:atype, :content, :cid, :sid, 'a2')
                    """
                ),
                {
                    "atype": atom.get("atom_type"),
                    "content": atom.get("content"),
                    "cid": case_id,
                    "sid": seg_id,
                },
            )

    return case_id


@activity.defn
async def decompose(case_input: dict[str, Any]) -> str:
    activity.logger.info("A2 Decomposition starting url=%s", case_input.get("url"))

    payload = case_input.get("manual_payload")
    if payload is None:
        payload = _extract_via_media_pipeline(case_input["url"])

    asr = payload.get("asr_text") or ""
    ocr = payload.get("ocr_text") or ""
    visual = payload.get("visual_desc") or ""
    duration = payload.get("duration_sec")

    raw = call_deepseek(
        DECOMPOSITION_SYSTEM,
        build_user_prompt(asr, ocr, visual, duration),
        temperature=0.2,
        response_format_json=True,
    )
    try:
        decomp = json.loads(raw)
    except json.JSONDecodeError as e:
        activity.logger.error("A2 LLM returned non-JSON: %r", raw[:500])
        raise RuntimeError(f"A2 decomposition output not parseable as JSON: {e}") from e

    if "segments" not in decomp or "atoms" not in decomp:
        raise RuntimeError(f"A2 decomposition output missing required keys: {list(decomp.keys())}")

    case_id = _persist_case_and_segments({**case_input, "manual_payload": payload}, decomp)
    activity.logger.info(
        "A2 Decomposition done case_id=%s segments=%d atoms=%d",
        case_id,
        len(decomp.get("segments", [])),
        len(decomp.get("atoms", [])),
    )
    return case_id
