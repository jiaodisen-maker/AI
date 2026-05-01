"""GET /cases/{id} 全量返回 + GET /cases 列表."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(prefix="/cases", tags=["cases"])


@router.get("/{case_id}")
def get_case(case_id: str, db: Session = Depends(get_session)) -> dict:
    case = db.execute(
        text(
            """
            SELECT id, url, platform, brand, sku, category, duration_sec,
                   likes, comments, gmv_estimated,
                   data_lineage, poc_purge_at, ingested_at, workflow_id, raw_meta
            FROM cases WHERE id = :id
            """
        ),
        {"id": case_id},
    ).mappings().first()
    if case is None:
        raise HTTPException(404, "case not found")

    segments = [
        dict(r)
        for r in db.execute(
            text(
                """
                SELECT id, segment_type, start_sec, end_sec, asr_text, ocr_text, visual_desc, llm_analysis
                FROM case_segments WHERE case_id = :cid
                ORDER BY COALESCE(start_sec, 0)
                """
            ),
            {"cid": case_id},
        ).mappings().all()
    ]

    atoms = [
        dict(r)
        for r in db.execute(
            text(
                """
                SELECT id, atom_type, content, compliance_grade, feasibility_4d,
                       source_segment_id, created_by_agent
                FROM atoms WHERE source_case_id = :cid
                """
            ),
            {"cid": case_id},
        ).mappings().all()
    ]

    cross = [
        dict(r)
        for r in db.execute(
            text(
                """
                SELECT id, agent, verdict, confidence, raw_data, validated_at
                FROM cross_validations WHERE case_id = :cid
                ORDER BY validated_at
                """
            ),
            {"cid": case_id},
        ).mappings().all()
    ]

    return {"case": dict(case), "segments": segments, "atoms": atoms, "cross_validations": cross}


@router.get("")
def list_cases(limit: int = 50, db: Session = Depends(get_session)) -> list[dict]:
    rows = db.execute(
        text(
            """
            SELECT id, url, platform, brand, sku, category, data_lineage, ingested_at
            FROM cases ORDER BY ingested_at DESC LIMIT :limit
            """
        ),
        {"limit": limit},
    ).mappings().all()
    return [dict(r) for r in rows]
