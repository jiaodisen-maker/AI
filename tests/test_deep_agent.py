"""Tests for the Deep Agent module (LangChain/LangGraph)."""


from app.skills.base import BaseSkill
from app.skills.models import SkillCategory, SkillMeta, SkillOutput
from app.skills.registry import SkillRegistry


def test_langchain_imports():
    """LangChain + LangGraph dependencies are installed."""
    from langchain_core.messages import HumanMessage
    from langchain_core.tools import StructuredTool
    from langgraph.prebuilt import create_react_agent

    assert HumanMessage is not None
    assert StructuredTool is not None
    assert create_react_agent is not None


def test_deep_agent_skill_wrapper():
    """Deep Agent can wrap Skills as LangChain tools."""
    from app.brain.deep import _build_tools_from_skills

    class TestSkill(BaseSkill):
        def meta(self):
            return SkillMeta(
                id="test-skill",
                name="Test",
                description="A test skill",
                category=SkillCategory.DATA,
            )

        async def execute(self, skill_input):
            return SkillOutput(success=True, content="test result")

    registry = SkillRegistry()
    registry.register(TestSkill())

    tools = _build_tools_from_skills(registry)
    assert len(tools) == 1
    assert tools[0].name == "test_skill"
    assert "Test" in tools[0].description


def test_deep_agent_import():
    """run_deep_agent function is importable."""
    from app.brain.deep import run_deep_agent

    assert callable(run_deep_agent)
