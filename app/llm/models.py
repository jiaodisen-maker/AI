"""Data models for LLM interactions."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class ChatMessage(BaseModel):
    role: Role
    content: str


class ChatRequest(BaseModel):
    """Unified request to the LLM routing layer."""

    messages: list[ChatMessage]
    model_preference: str = "auto"  # local / overseas / specialized / auto
    temperature: float = 0.7
    max_tokens: int = 4096
    skill_id: str = ""  # for routing decisions & logging
    metadata: dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    """Unified response from the LLM routing layer."""

    content: str
    model_used: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: int = 0
    cost_usd: float = 0.0
