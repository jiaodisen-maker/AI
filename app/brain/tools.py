"""Bridge: convert AI middleware Skills into AgentScope tool functions.

Each BaseSkill is wrapped as a plain function with type hints and docstring,
then registered with the AgentScope Toolkit so the ReActAgent can call it.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any

from app.brain.agent import BrainAgent
from app.skills.base import BaseSkill
from app.skills.models import SkillInput
from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


def register_skills_as_tools(
    brain: BrainAgent,
    registry: SkillRegistry,
    experience_engine: Any = None,
) -> None:
    """Register all skills from the registry as AgentScope tool functions.

    Each skill becomes a callable tool that the ReActAgent can invoke
    autonomously via tool calling.
    """
    for meta in registry.list_all():
        skill = registry.get(meta.id)
        if skill is None:
            continue

        # Create a tool function for this skill
        tool_func = _make_tool_function(skill, experience_engine)
        brain.register_tool(tool_func)

    logger.info(
        "Registered %d skills as AgentScope tools",
        registry.count,
    )


def _make_tool_function(
    skill: BaseSkill,
    experience_engine: Any = None,
) -> callable:
    """Create a tool function wrapping a BaseSkill.

    The generated function has proper name, docstring, and type hints
    so AgentScope can generate the correct tool schema.
    """
    meta = skill.meta()

    def tool_func(user_message: str, platform: str = "", product_name: str = "") -> str:
        """Placeholder docstring, replaced below."""
        # Build skill input
        experience_prompt = ""
        if experience_engine:
            experience_prompt = experience_engine.get_experience_prompt(meta.id)

        skill_input = SkillInput(
            user_message=user_message,
            parameters={
                k: v for k, v in {"platform": platform, "product_name": product_name}.items() if v
            },
            context={"experience_prompt": experience_prompt},
        )

        # Run async skill in sync context (AgentScope tools are synchronous)
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                record = pool.submit(
                    asyncio.run, skill.run(skill_input)
                ).result()
        else:
            record = asyncio.run(skill.run(skill_input))

        if record.output.success:
            result = record.output.content
            # Append compliance warnings if any
            warnings = record.output.metadata.get("compliance_warning", "")
            if warnings:
                result += f"\n\n[合规提示] {warnings}"
            return result
        else:
            return f"执行失败：{record.output.error}"

    # Set function metadata for AgentScope schema generation
    tool_func.__name__ = meta.id.replace("-", "_")
    tool_func.__doc__ = f"{meta.name}: {meta.description}"

    return tool_func
