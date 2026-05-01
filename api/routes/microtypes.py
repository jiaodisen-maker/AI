from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(prefix="/microtypes", tags=["microtypes"])


@router.get("")
def list_microtypes(
    status: str | None = Query(default=None, pattern="^(active|candidate|deprecated)$"),
    db: Session = Depends(get_session),
) -> list[dict]:
    where = ["1=1"]
    params: dict = {}
    if status:
        where.append("status = :s")
        params["s"] = status

    rows = db.execute(
        text(
            f"""
            SELECT id, scene, audience, ingredient, emotion, restriction,
                   status, proposed_by_agent
            FROM microtypes WHERE {" AND ".join(where)}
            ORDER BY (status = 'active') DESC, scene, audience
            """
        ),
        params,
    ).mappings().all()
    return [dict(r) for r in rows]


@router.post("/{microtype_id}/activate")
def activate_microtype(microtype_id: str, db: Session = Depends(get_session)) -> dict:
    """人审通过 candidate microtype。"""
    row = db.execute(
        text("UPDATE microtypes SET status = 'active' WHERE id = :id RETURNING id"),
        {"id": microtype_id},
    ).first()
    db.commit()
    return {"id": str(row.id) if row else None, "status": "active"}
