"""Tests for the Skill system."""

import pytest

from app.skills.base import BaseSkill
from app.skills.models import SkillCategory, SkillInput, SkillMeta, SkillOutput
from app.skills.registry import SkillRegistry


class DummySkill(BaseSkill):
    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="dummy",
            name="Dummy Skill",
            description="A test skill",
            category=SkillCategory.CONTENT,
            triggers=["test", "dummy"],
        )

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        return SkillOutput(success=True, content=f"Echo: {skill_input.user_message}")


class FailingSkill(BaseSkill):
    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="failing",
            name="Failing Skill",
            description="Always fails validation",
            category=SkillCategory.DATA,
        )

    def validate(self, skill_input: SkillInput) -> str | None:
        return "Input is invalid"

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        return SkillOutput(success=True, content="Should not reach here")


def test_registry_register_and_get():
    registry = SkillRegistry()
    skill = DummySkill()
    registry.register(skill)

    assert registry.count == 1
    assert registry.get("dummy") is skill
    assert registry.get("nonexistent") is None


def test_registry_find_by_trigger():
    registry = SkillRegistry()
    registry.register(DummySkill())

    found = registry.find_by_trigger("please test this")
    assert found is not None
    assert found.meta().id == "dummy"

    not_found = registry.find_by_trigger("no match here")
    assert not_found is None


def test_registry_list_all():
    registry = SkillRegistry()
    registry.register(DummySkill())
    metas = registry.list_all()
    assert len(metas) == 1
    assert metas[0].id == "dummy"


@pytest.mark.asyncio
async def test_skill_run_success():
    skill = DummySkill()
    skill_input = SkillInput(user_message="hello")
    record = await skill.run(skill_input)

    assert record.output.success is True
    assert "Echo: hello" in record.output.content
    assert record.execution_time_ms >= 0


@pytest.mark.asyncio
async def test_skill_run_validation_failure():
    skill = FailingSkill()
    skill_input = SkillInput(user_message="anything")
    record = await skill.run(skill_input)

    assert record.output.success is False
    assert record.output.error == "Input is invalid"
