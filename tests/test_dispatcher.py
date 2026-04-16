"""Tests for the SkillDispatcher — 1+1+Deep+Workflow+Discuss routing."""

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
    result = await dispatcher.dispatch("echo hello world")
    assert result["skill_id"] == "echo"
    assert result["mode"] == "fast"
    assert "Echo: echo hello world" in result["content"]


@pytest.mark.asyncio
async def test_fast_track_chinese_trigger(dispatcher):
    result = await dispatcher.dispatch("重复这句话")
    assert result["skill_id"] == "echo"
    assert result["mode"] == "fast"


@pytest.mark.asyncio
async def test_no_match_no_agent(dispatcher):
    result = await dispatcher.dispatch("unrelated query")
    assert result["skill_id"] is None
    assert result["mode"] == "no_match"


@pytest.mark.asyncio
async def test_deep_command_no_deps(dispatcher):
    result = await dispatcher.dispatch("/deep 分析竞品")
    assert result["content"]
    assert result["mode"] in ("deep", "deep_error", "no_match", "error")


@pytest.mark.asyncio
async def test_workflow_command_no_engine(dispatcher):
    result = await dispatcher.dispatch("/workflow 新品上市文案流程")
    assert "未初始化" in result["content"]
    assert result["mode"] == "workflow_error"


@pytest.mark.asyncio
async def test_discuss_command_no_brain(dispatcher):
    result = await dispatcher.dispatch("/discuss 竞品策略")
    assert "未初始化" in result["content"]
    assert result["mode"] == "discuss_error"


@pytest.mark.asyncio
async def test_lifecycle():
    log = []

    class LifecycleSkill(BaseSkill):
        def meta(self):
            return SkillMeta(
                id="lc", name="LC", description="test",
                category=SkillCategory.DATA, triggers=["lifecycle"],
            )

        def validate(self, si):
            log.append("validate")
            return None

        async def execute(self, si):
            log.append("execute")
            return SkillOutput(success=True, content="done")

        async def post_execute(self, si, o):
            log.append("post_execute")
            return o

    reg = SkillRegistry()
    reg.register(LifecycleSkill())
    d = SkillDispatcher(registry=reg)

    result = await d.dispatch("lifecycle test")
    assert result["skill_id"] == "lc"
    assert "validate" in log
    assert "execute" in log
    assert "post_execute" in log


@pytest.mark.asyncio
async def test_session_memory():
    from app.memory.session import SessionMemory

    mem = SessionMemory()
    reg = SkillRegistry()
    reg.register(EchoSkill())
    d = SkillDispatcher(registry=reg, session_memory=mem)

    await d.dispatch("echo hi", session_id="s1")
    history = await mem.get_history("s1")
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[1]["role"] == "assistant"
