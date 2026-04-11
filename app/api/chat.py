"""Chat endpoint: the main conversation interface."""

from __future__ import annotations

import uuid

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    user_id: str = ""
    session_id: str = Field(default_factory=lambda: uuid.uuid4().hex)


class ChatResponse(BaseModel):
    content: str
    skill_id: str | None = None
    tier: int | None = None
    execution_time_ms: int | None = None


@router.post("/chat")
async def chat(req: ChatRequest) -> ChatResponse:
    """Main chat endpoint — goes directly through SkillDispatcher.

    Three-tier routing:
    1. Trigger word match (fast, no LLM)
    2. LLM intent classification
    3. Agent multi-step orchestration
    """
    from app.main import get_app_state

    state = get_app_state()

    result = await state.dispatcher.dispatch(
        message=req.message,
        user_id=req.user_id,
        session_id=req.session_id,
        source="api",
    )

    return ChatResponse(
        content=result["content"],
        skill_id=result.get("skill_id"),
        tier=result.get("tier"),
        execution_time_ms=result.get("metadata", {}).get("execution_time_ms"),
    )
