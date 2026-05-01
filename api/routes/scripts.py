"""GET /scripts — 浏览 generated_scripts + 关联 critic_scores."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(prefix="/scripts", tags=["scripts"])


@router.get("")
def list_scripts(
    microtype_id: str | None = None,
    internal_only: bool | None = None,
    limit: int = 50,
    db: Session = Depends(get_session),
) -> list[dict]:
    where = ["1=1"]
    params: dict = {"limit": limit}
    if microtype_id:
        where.append("microtype_id = :m")
        params["m"] = microtype_id
    if internal_only is not None:
        where.append("for_internal_research_only = :i")
        params["i"] = internal_only

    rows = db.execute(
        text(
            f"""
            SELECT id, microtype_id, prompt_version, output, llm_model,
                   for_internal_research_only, generated_at
            FROM generated_scripts WHERE {" AND ".join(where)}
            ORDER BY generated_at DESC LIMIT :limit
            """
        ),
        params,
    ).mappings().all()
    return [dict(r) for r in rows]


@router.get("/{script_id}")
def get_script_with_critic(script_id: str, db: Session = Depends(get_session)) -> dict:
    s = db.execute(
        text(
            """
            SELECT id, microtype_id, atom_ids, prompt_version, output, llm_model,
                   for_internal_research_only, generated_at
            FROM generated_scripts WHERE id = :id
            """
        ),
        {"id": script_id},
    ).mappings().first()
    if s is None:
        raise HTTPException(404, "script not found")

    cs = db.execute(
        text(
            """
            SELECT id, evaluator_model, scores, reasoning, confidence, scored_at
            FROM critic_scores
            WHERE target_id = :tid AND target_type = 'generated_script'
            ORDER BY scored_at
            """
        ),
        {"tid": script_id},
    ).mappings().all()

    return {"script": dict(s), "critic_scores": [dict(r) for r in cs]}
