"""Base class for all skills — the center of the architecture.

Everything serves Skills. The BaseSkill lifecycle is the mandatory
pipeline that ALL requests pass through, no exceptions.

Lifecycle:
  1. validate        — input validation
  2. guardrail_input — safety check (injection, PII)
  3. inject_ontology — auto-inject domain knowledge from ontology
  4. inject_experience — auto-inject learned patterns
  5. execute         — core skill logic
  6. guardrail_output — output safety check
  7. post_execute    — skill-specific post-processing (e.g. compliance)
  8. record          — log execution for experience engine
"""

from __future__ import annotations

import logging
import time
import uuid
from abc import ABC, abstractmethod
from typing import Any

from app.skills.models import SkillExecutionRecord, SkillInput, SkillMeta, SkillOutput

logger = logging.getLogger(__name__)

# These are injected at app startup, not imported directly
# to avoid circular imports. See SkillRuntime.
_guardrail = None
_ontology_service = None
_experience_engine = None


def configure_skill_runtime(
    guardrail: Any = None,
    ontology_service: Any = None,
    experience_engine: Any = None,
) -> None:
    """Configure the global skill runtime services.

    Called once at app startup to inject shared services
    into the BaseSkill lifecycle.
    """
    global _guardrail, _ontology_service, _experience_engine
    _guardrail = guardrail
    _ontology_service = ontology_service
    _experience_engine = experience_engine


class BaseSkill(ABC):
    """Abstract base class that every skill must implement.

    The run() method enforces the full lifecycle pipeline.
    Subclasses only need to implement meta() and execute().
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

    async def post_execute(
        self, skill_input: SkillInput, output: SkillOutput
    ) -> SkillOutput:
        """Hook: skill-specific post-processing (e.g. compliance check)."""
        return output

    def ontology_needs(self) -> list[str]:
        """Declare which ontology dimensions this skill needs.

        Override to auto-inject ontology context. Example:
            return ["health_supplements", "data_definitions"]
        """
        return []

    async def run(self, skill_input: SkillInput) -> SkillExecutionRecord:
        """Full execution pipeline — the mandatory path for ALL requests.

        Every request passes through this pipeline, no matter how it
        was triggered (chat, API, CLI, MCP, patrol, scheduled).
        """
        start = time.monotonic()
        meta = self.meta()

        # Step 1: Validate
        error = self.validate(skill_input)
        if error:
            return self._make_record(meta.id, skill_input, SkillOutput(
                success=False, error=error
            ), start)

        # Step 2: Input guardrail
        if _guardrail:
            guard_result = _guardrail.check_input(skill_input.user_message)
            if not guard_result.passed:
                logger.warning(
                    "Skill %s: input blocked by guardrail: %s",
                    meta.id, guard_result.issues,
                )
                return self._make_record(meta.id, skill_input, SkillOutput(
                    success=False,
                    error="请求被安全系统拦截",
                    metadata={"guardrail_issues": guard_result.issues},
                ), start)

        # Step 3: Inject ontology context
        if _ontology_service and self.ontology_needs():
            ontology_context = {}
            for dimension in self.ontology_needs():
                ontology_context[dimension] = _ontology_service.loader.get(
                    dimension
                )
            skill_input.context["ontology"] = ontology_context

        # Step 4: Inject experience patterns
        if _experience_engine:
            exp_prompt = _experience_engine.get_experience_prompt(meta.id)
            if exp_prompt:
                skill_input.context["experience_prompt"] = exp_prompt

        # Step 5: Execute
        output = await self.execute(skill_input)

        # Step 6: Output guardrail
        if _guardrail and output.success:
            guard_result = _guardrail.check_output(output.content)
            if guard_result.issues:
                output.metadata["guardrail_warnings"] = guard_result.issues

        # Step 7: Skill-specific post-processing
        output = await self.post_execute(skill_input, output)

        # Step 8: Record for experience engine
        if _experience_engine and output.success:
            await _experience_engine.record_execution(
                skill_id=meta.id,
                input_context={
                    "user_message": skill_input.user_message,
                    **skill_input.parameters,
                },
                ai_output=output.content,
            )

        return self._make_record(meta.id, skill_input, output, start)

    @staticmethod
    def _make_record(
        skill_id: str,
        skill_input: SkillInput,
        output: SkillOutput,
        start: float,
    ) -> SkillExecutionRecord:
        return SkillExecutionRecord(
            id=uuid.uuid4().hex,
            skill_id=skill_id,
            input=skill_input,
            output=output,
            execution_time_ms=int((time.monotonic() - start) * 1000),
        )
