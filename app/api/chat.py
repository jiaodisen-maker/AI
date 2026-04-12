"""Chat endpoint: the main conversation interface."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.auth.middleware import require_auth

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
async def chat(req: ChatRequest, user: dict = Depends(require_auth)) -> ChatResponse:
    """Main chat endpoint — goes through SkillDispatcher.

    Fast track: trigger word → Skill (0 tokens)
    Main path:  Agent loop → model decides (AgentScope)
    /deep:      Deep Agent for open-ended research (LangChain)
    """
    from app.main import get_app_state

    state = get_app_state()

    result = await state.dispatcher.dispatch(
        message=req.message,
        user_id=req.user_id or user.get("sub", ""),
        session_id=req.session_id,
        source="api",
    )

    return ChatResponse(
        content=result["content"],
        skill_id=result.get("skill_id"),
        tier=None,  # deprecated, use mode
        execution_time_ms=result.get("metadata", {}).get("execution_time_ms"),
    )
