"""Experience management API: submit corrections, view/manage patterns."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.auth.middleware import require_auth

router = APIRouter(prefix="/experience", tags=["experience"])


class CorrectionRequest(BaseModel):
    """Submit a human correction for a skill output."""

    skill_id: str
    record_id: str = ""
    ai_output: str
    human_edited: str
    input_context: dict = {}


class PatternUpdateRequest(BaseModel):
    """Update a pattern's confidence or metadata."""

    action: str  # "confirm" or "reject"


@router.post("/corrections")
async def submit_correction(req: CorrectionRequest, user: dict = Depends(require_auth)):
    """Submit a human correction to trigger experience learning.

    This is the key endpoint for the experience engine:
    when a human edits AI output, we learn from the difference.
    """
    from app.main import get_app_state

    state = get_app_state()

    patterns = await state.experience_engine.learn_from_correction(
        record_id=req.record_id,
        skill_id=req.skill_id,
        ai_output=req.ai_output,
        human_edited=req.human_edited,
        input_context=req.input_context,
    )

    return {
        "learned_patterns": len(patterns),
        "patterns": [
            {
                "id": p.id,
                "pattern": p.pattern,
                "confidence": p.confidence,
            }
            for p in patterns
        ],
    }


@router.get("/patterns/{skill_id}")
async def list_patterns(skill_id: str):
    """List all active experience patterns for a skill."""
    from app.main import get_app_state

    state = get_app_state()
    patterns = state.experience_engine.store.get_all_patterns(skill_id)

    return {
        "skill_id": skill_id,
        "count": len(patterns),
        "patterns": [p.model_dump() for p in patterns],
    }


@router.post("/patterns/{pattern_id}")
async def update_pattern(
    pattern_id: str, req: PatternUpdateRequest, user: dict = Depends(require_auth)
):
    """Confirm or reject an experience pattern."""
    from app.main import get_app_state

    state = get_app_state()

    if req.action == "confirm":
        await state.experience_engine.store.confirm_pattern(pattern_id)
        return {"status": "confirmed"}
    elif req.action == "reject":
        await state.experience_engine.store.reject_pattern(pattern_id)
        return {"status": "rejected"}
    else:
        raise HTTPException(status_code=400, detail="action must be 'confirm' or 'reject'")
