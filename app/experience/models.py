"""Data models for the Experience Engine."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ExperienceRecord(BaseModel):
    """Record of a skill execution with optional human correction.

    This is the raw material for the experience engine to learn from.
    """

    id: str = ""
    skill_id: str
    input_context: dict[str, Any] = {}
    ai_output: str = ""
    human_edited_output: str | None = None
    diff_summary: str = ""
    extracted_patterns: list[str] = Field(default_factory=list)
    model_used: str = ""
    created_at: datetime = Field(default_factory=datetime.now)

    @property
    def was_edited(self) -> bool:
        return self.human_edited_output is not None and self.human_edited_output != self.ai_output


class ExperiencePattern(BaseModel):
    """A learned pattern extracted from human corrections.

    Confidence lifecycle:
        New pattern born       → confidence = 0.3
        Second confirmation    → confidence = 0.5
        5+ consistent uses     → confidence = 0.8 (auto-injected into prompts)
        User rejects once      → confidence -= 0.2
        confidence < 0.1       → auto-archived
    """

    id: str = ""
    skill_id: str
    pattern: str  # e.g. "抖音文案用口语化表达"
    description: str = ""  # longer explanation
    examples: list[dict[str, str]] = Field(default_factory=list)  # [{"before": ..., "after": ...}]
    confidence: float = 0.3
    usage_count: int = 0
    effectiveness: float = 0.0  # 0-1, how often this pattern leads to no further edits
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @property
    def is_reliable(self) -> bool:
        """Whether this pattern has enough confidence to be auto-injected."""
        return self.confidence >= 0.7

    @property
    def should_archive(self) -> bool:
        """Whether this pattern should be archived due to low confidence."""
        return self.confidence < 0.1
