"""Chat endpoint: the main conversation interface."""

from __future__ import annotations

import uuid

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.channels.models import IncomingMessage, MessageSource

router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    user_id: str = ""
    session_id: str = Field(default_factory=lambda: uuid.uuid4().hex)


class ChatResponse(BaseModel):
    content: str
    skill_id: str | None = None
    execution_time_ms: int | None = None


@router.post("/chat")
async def chat(req: ChatRequest) -> ChatResponse:
    """Main chat endpoint: send a message, get AI response.

    The message goes through:
    1. Intent recognition
    2. Skill routing
    3. Skill execution (with experience injection)
    4. Response formatting
    """
    from app.main import get_app_state

    state = get_app_state()

    incoming = IncomingMessage(
        message_id=uuid.uuid4().hex,
        source=MessageSource.API,
        user_id=req.user_id,
        content=req.message,
        session_id=req.session_id,
    )

    outgoing = await state.message_router.handle(incoming)

    return ChatResponse(
        content=outgoing.content,
        skill_id=outgoing.metadata.get("skill_id"),
        execution_time_ms=outgoing.metadata.get("execution_time_ms"),
    )
