"""Tests for the SkillDispatcher — 1+1+Deep routing."""

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
        return SkillOutput(
            success=True, content=f"Echo: {skill_input.user_message}"
        )


@pytest.fixture
def registry():
    reg = SkillRegistry()
    reg.register(EchoSkill())
    return reg


@pytest.fixture
def dispatcher(registry):
    return SkillDispatcher(registry=registry)


@pytest.mark.asyncio
async def test_fast_track_trigger_match(dispatcher):
    """Fast track: trigger word match, no LLM needed."""
    result = await dispatcher.dispatch("echo hello world")
    assert result["skill_id"] == "echo"
    assert result["mode"] == "fast"
    assert "Echo: echo hello world" in result["content"]


@pytest.mark.asyncio
async def test_fast_track_chinese_trigger(dispatcher):
    """Fast track: Chinese trigger word."""
    result = await dispatcher.dispatch("重复这句话")
    assert result["skill_id"] == "echo"
    assert result["mode"] == "fast"


@pytest.mark.asyncio
async def test_no_match_no_agent_returns_fallback(dispatcher):
    """No matching skill, no agent → fallback message."""
    result = await dispatcher.dispatch("completely unrelated query")
    assert result["skill_id"] is None
    assert result["mode"] == "no_match"
    assert "抱歉" in result["content"]


@pytest.mark.asyncio
async def test_deep_command_no_deps(dispatcher):
    """/deep command without LangChain deps → falls back gracefully."""
    result = await dispatcher.dispatch("/deep 分析竞品机会")
    # Should not crash, either runs deep agent or falls back
    assert result["content"]  # Has some response
    assert result["mode"] in ("deep", "deep_error", "no_match", "error")


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


@pytest.mark.asyncio
async def test_session_memory_integration():
    """Session memory stores conversation history."""
    from app.memory.session import SessionMemory

    memory = SessionMemory()
    registry = SkillRegistry()
    registry.register(EchoSkill())
    dispatcher = SkillDispatcher(registry=registry, session_memory=memory)

    await dispatcher.dispatch("echo hello", session_id="s1")

    history = await memory.get_history("s1")
    assert len(history) == 2  # user + assistant
    assert history[0]["role"] == "user"
    assert history[1]["role"] == "assistant"
