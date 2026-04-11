"""Base class for all skills."""

from __future__ import annotations

import time
import uuid
from abc import ABC, abstractmethod

from app.skills.models import SkillExecutionRecord, SkillInput, SkillMeta, SkillOutput


class BaseSkill(ABC):
    """Abstract base class that every skill must implement.

    Lifecycle: validate → pre_execute → execute → post_execute → record
    """

    @abstractmethod
    def meta(self) -> SkillMeta:
        """Return skill metadata for registration and routing."""

    def validate(self, skill_input: SkillInput) -> str | None:
        """Validate input before execution. Return error message or None."""
        return None

    @abstractmethod
    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        """Core execution logic. Must be implemented by every skill."""

    async def pre_execute(self, skill_input: SkillInput) -> SkillInput:
        """Hook: transform input before execution (e.g. inject experience)."""
        return skill_input

    async def post_execute(self, skill_input: SkillInput, output: SkillOutput) -> SkillOutput:
        """Hook: transform output after execution (e.g. compliance check)."""
        return output

    async def run(self, skill_input: SkillInput) -> SkillExecutionRecord:
        """Full execution pipeline with timing and recording."""
        start = time.monotonic()

        # Validate
        error = self.validate(skill_input)
        if error:
            output = SkillOutput(success=False, error=error)
            return SkillExecutionRecord(
                id=uuid.uuid4().hex,
                skill_id=self.meta().id,
                input=skill_input,
                output=output,
            )

        # Pre-execute hook
        skill_input = await self.pre_execute(skill_input)

        # Execute
        output = await self.execute(skill_input)

        # Post-execute hook
        output = await self.post_execute(skill_input, output)

        elapsed_ms = int((time.monotonic() - start) * 1000)

        return SkillExecutionRecord(
            id=uuid.uuid4().hex,
            skill_id=self.meta().id,
            input=skill_input,
            output=output,
            execution_time_ms=elapsed_ms,
        )
