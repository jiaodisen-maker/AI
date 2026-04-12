"""Skill management API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.auth.middleware import require_auth
from app.skills.models import SkillInput

router = APIRouter(prefix="/skills", tags=["skills"])


class SkillExecuteRequest(BaseModel):
    message: str
    parameters: dict = {}
    user_id: str = ""


@router.get("/")
async def list_skills():
    """List all registered skills."""
    from app.main import get_app_state

    state = get_app_state()
    skills = state.skill_registry.list_all()
    return {
        "count": len(skills),
        "skills": [s.model_dump() for s in skills],
    }


@router.get("/{skill_id}")
async def get_skill(skill_id: str):
    """Get details of a specific skill."""
    from app.main import get_app_state

    state = get_app_state()
    skill = state.skill_registry.get(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail=f"Skill '{skill_id}' not found")
    return skill.meta().model_dump()


@router.post("/{skill_id}/execute")
async def execute_skill(
    skill_id: str, req: SkillExecuteRequest, user: dict = Depends(require_auth)
):
    """Execute a specific skill directly."""
    from app.main import get_app_state

    state = get_app_state()
    skill = state.skill_registry.get(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail=f"Skill '{skill_id}' not found")

    skill_input = SkillInput(
        user_message=req.message,
        parameters=req.parameters,
        user_id=req.user_id,
        context={
            "experience_prompt": state.experience_engine.get_experience_prompt(skill_id),
        },
    )

    record = await skill.run(skill_input)

    # Record execution for experience engine
    await state.experience_engine.record_execution(
        skill_id=skill_id,
        input_context={"user_message": req.message, **req.parameters},
        ai_output=record.output.content,
        model_used=record.model_used,
    )

    return {
        "success": record.output.success,
        "content": record.output.content,
        "error": record.output.error,
        "metadata": record.output.metadata,
        "execution_time_ms": record.execution_time_ms,
    }


@router.get("/{skill_id}/experience")
async def get_skill_experience(skill_id: str):
    """Get experience statistics and patterns for a skill."""
    from app.main import get_app_state

    state = get_app_state()
    stats = state.experience_engine.get_stats(skill_id)
    patterns = state.experience_engine.store.get_all_patterns(skill_id)

    return {
        "stats": stats,
        "patterns": [p.model_dump() for p in patterns],
    }
