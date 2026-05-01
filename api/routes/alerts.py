from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("")
def list_alerts(
    status: str = Query(default="open", pattern="^(open|resolved)$"),
    alert_type: str | None = None,
    limit: int = 100,
    db: Session = Depends(get_session),
) -> list[dict]:
    where = ["status = :s"]
    params: dict = {"s": status, "limit": limit}
    if alert_type:
        where.append("alert_type = :t")
        params["t"] = alert_type

    rows = db.execute(
        text(
            f"""
            SELECT id, alert_type, payload, status, resolved_by, resolved_at, created_at
            FROM hitl_alerts WHERE {" AND ".join(where)}
            ORDER BY created_at DESC LIMIT :limit
            """
        ),
        params,
    ).mappings().all()
    return [dict(r) for r in rows]


@router.post("/{alert_id}/resolve")
def resolve_alert(
    alert_id: str, resolved_by: str = Query(...), db: Session = Depends(get_session)
) -> dict:
    row = db.execute(
        text(
            """
            UPDATE hitl_alerts
            SET status = 'resolved', resolved_by = :rb, resolved_at = now()
            WHERE id = :id
            RETURNING id
            """
        ),
        {"id": alert_id, "rb": resolved_by},
    ).first()
    db.commit()
    return {"id": str(row.id) if row else None, "status": "resolved"}
