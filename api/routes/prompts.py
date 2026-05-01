"""GET /prompt-versions — DSPy 自优化历史浏览。"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(prefix="/prompt-versions", tags=["prompts"])


@router.get("")
def list_prompt_versions(
    agent: str | None = Query(default=None, pattern="^(a2|a8)$"),
    limit: int = 50,
    db: Session = Depends(get_session),
) -> list[dict]:
    where = ["1=1"]
    params: dict = {"limit": limit}
    if agent:
        where.append("agent = :ag")
        params["ag"] = agent

    rows = db.execute(
        text(
            f"""
            SELECT id, agent, version, metric, created_at, trigger_critic_id
            FROM prompt_versions WHERE {" AND ".join(where)}
            ORDER BY created_at DESC LIMIT :limit
            """
        ),
        params,
    ).mappings().all()
    return [dict(r) for r in rows]


@router.get("/{prompt_id}")
def get_prompt_version(prompt_id: str, db: Session = Depends(get_session)) -> dict:
    row = db.execute(
        text(
            """
            SELECT id, agent, version, prompt_text, metric, created_at, trigger_critic_id
            FROM prompt_versions WHERE id = :id
            """
        ),
        {"id": prompt_id},
    ).mappings().first()
    if not row:
        from fastapi import HTTPException
        raise HTTPException(404, "prompt version not found")
    return dict(row)
