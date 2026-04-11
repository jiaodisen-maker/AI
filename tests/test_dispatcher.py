"""Tests for the SkillDispatcher — Skill-centered routing."""

import pytest

from app.skills.base import BaseSkill
from app.skills.dispatcher import SkillDispatcher
from app.skills.models import SkillCategory, SkillInput, SkillMeta, SkillOutput
from app.skills.registry import SkillRegistry


class EchoSkill(BaseSkill):
    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="echo",
            name="Echo",
            description="Echoes input",
            category=SkillCategory.CONTENT,
            triggers=["echo", "重复"],
        )

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        return SkillOutput(success=True, content=f"Echo: {skill_input.user_message}")


@pytest.fixture
def registry():
    reg = SkillRegistry()
    reg.register(EchoSkill())
    return reg


@pytest.fixture
def dispatcher(registry):
    return SkillDispatcher(registry=registry)


@pytest.mark.asyncio
async def test_tier1_trigger_match(dispatcher):
    """Tier 1: trigger word match, no LLM needed."""
    result = await dispatcher.dispatch("echo hello world")
    assert result["skill_id"] == "echo"
    assert result["tier"] == 1
    assert "Echo: echo hello world" in result["content"]


@pytest.mark.asyncio
async def test_tier1_chinese_trigger(dispatcher):
    """Tier 1: Chinese trigger word."""
    result = await dispatcher.dispatch("重复这句话")
    assert result["skill_id"] == "echo"
    assert result["tier"] == 1


@pytest.mark.asyncio
async def test_no_match_returns_fallback(dispatcher):
    """No matching skill → fallback message."""
    result = await dispatcher.dispatch("completely unrelated query")
    assert result["skill_id"] is None
    assert result["tier"] == 0
    assert "抱歉" in result["content"]


@pytest.mark.asyncio
async def test_skill_goes_through_full_lifecycle():
    """Verify the full BaseSkill lifecycle runs."""
    lifecycle_log = []

    class LifecycleSkill(BaseSkill):
        def meta(self):
            return SkillMeta(
                id="lifecycle",
                name="Lifecycle Test",
                description="Tests lifecycle",
                category=SkillCategory.DATA,
                triggers=["lifecycle"],
            )

        def validate(self, skill_input):
            lifecycle_log.append("validate")
            return None

        async def execute(self, skill_input):
            lifecycle_log.append("execute")
            return SkillOutput(success=True, content="done")

        async def post_execute(self, skill_input, output):
            lifecycle_log.append("post_execute")
            return output

    registry = SkillRegistry()
    registry.register(LifecycleSkill())
    dispatcher = SkillDispatcher(registry=registry)

    result = await dispatcher.dispatch("lifecycle test")
    assert result["skill_id"] == "lifecycle"
    assert "validate" in lifecycle_log
    assert "execute" in lifecycle_log
    assert "post_execute" in lifecycle_log
