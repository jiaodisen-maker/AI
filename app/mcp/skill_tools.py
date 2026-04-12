"""Register Skills as MCP tools for external agent discovery."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.mcp.server import MCPServerManager
    from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


def register_skills_as_mcp_tools(
    mcp: MCPServerManager,
    registry: SkillRegistry,
) -> None:
    """Register all Skills from the registry as MCP tools."""
    for meta in registry.list_all():
        skill = registry.get(meta.id)
        if skill is None:
            continue

        def make_handler(s):
            def handler(user_message: str = "") -> str:
                import asyncio

                from app.skills.models import SkillInput

                skill_input = SkillInput(user_message=user_message)
                record = asyncio.run(s.run(skill_input))
                if record.output.success:
                    return record.output.content
                return f"Error: {record.output.error}"

            return handler

        mcp.register_skill_tool(
            skill_id=meta.id,
            name=meta.name,
            description=meta.description,
            handler=make_handler(skill),
        )

    logger.info("Registered %d skills as MCP tools", registry.count)
