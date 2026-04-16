"""Tests for the SOP Workflow Engine."""

import pytest

from app.brain.workflow import WorkflowEngine
from app.ontology.service import OntologyService
from app.skills.base import BaseSkill
from app.skills.models import SkillCategory, SkillMeta, SkillOutput
from app.skills.registry import SkillRegistry


class MockSkill(BaseSkill):
    def meta(self):
        return SkillMeta(
            id="compliant-copy",
            name="合规文案",
            description="test",
            category=SkillCategory.CONTENT,
        )

    async def execute(self, skill_input):
        return SkillOutput(success=True, content="生成的文案内容")


@pytest.fixture
def engine():
    reg = SkillRegistry()
    reg.register(MockSkill())
    ontology = OntologyService()
    return WorkflowEngine(skill_registry=reg, ontology_service=ontology)


@pytest.mark.asyncio
async def test_execute_known_workflow(engine):
    """Execute a workflow defined in ontology."""
    result = await engine.execute_workflow("新品上市文案流程")
    assert result["workflow"] == "新品上市文案流程"
    assert result["steps_total"] > 0
    assert result["steps_completed"] > 0


@pytest.mark.asyncio
async def test_execute_unknown_workflow(engine):
    result = await engine.execute_workflow("不存在的流程")
    assert "error" in result


@pytest.mark.asyncio
async def test_workflow_stops_at_human_approval(engine):
    """Workflow should block at human_approval steps."""
    result = await engine.execute_workflow("新品上市文案流程")
    # 新品上市流程第4步是 human_approval
    has_pending = any(
        r.get("status") == "pending_approval"
        for r in result.get("results", [])
    )
    assert has_pending or result["steps_completed"] < result["steps_total"]


@pytest.mark.asyncio
async def test_workflow_no_ontology():
    reg = SkillRegistry()
    engine = WorkflowEngine(skill_registry=reg)
    result = await engine.execute_workflow("anything")
    assert "error" in result
