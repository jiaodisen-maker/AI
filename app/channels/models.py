"""Data models for the Channel layer."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class MessageSource(str, Enum):
    FEISHU = "feishu"
    WEB = "web"
    API = "api"


class IncomingMessage(BaseModel):
    """A message received from any channel."""

    message_id: str = ""
    source: MessageSource = MessageSource.API
    user_id: str = ""
    user_name: str = ""
    content: str = ""
    chat_id: str = ""  # group chat ID (feishu)
    session_id: str = ""
    timestamp: datetime = Field(default_factory=datetime.now)
    raw_event: dict[str, Any] = Field(default_factory=dict)


class OutgoingMessage(BaseModel):
    """A message to send back through a channel."""

    content: str = ""
    target_user_id: str = ""
    target_chat_id: str = ""
    source: MessageSource = MessageSource.API
    card: dict[str, Any] | None = None  # interactive card (feishu)
    metadata: dict[str, Any] = Field(default_factory=dict)
