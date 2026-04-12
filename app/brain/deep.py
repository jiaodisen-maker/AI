"""Deep Agent: LangChain Deep Agents for open-ended research.

Triggered by user via /deep command. Handles tasks that need:
- Autonomous multi-step reasoning
- File system backend for large results
- Context compression for long chains
- Planning and self-correction

Skills are registered as tools the Deep Agent can call.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


async def run_deep_agent(
    query: str,
    skill_registry: SkillRegistry,
    user_id: str = "",
    session_id: str = "",
) -> str:
    """Run a deep research task using LangChain Deep Agents.

    This function is designed to be called from SkillDispatcher
    when the user triggers /deep.

    If LangChain/LangGraph dependencies are not installed,
    ImportError propagates and the dispatcher falls back to
    the AgentScope main path.
    """
    from langchain_core.messages import HumanMessage, SystemMessage
    from langgraph.prebuilt import create_react_agent

    # Build tools from skill registry
    tools = _build_tools_from_skills(skill_registry)

    system_prompt = (
        "你是一个深度分析助手。用户要求你进行深入的研究和分析。\n"
        "你可以使用可用工具查询数据、生成文案、检查合规等。\n"
        "请一步步思考，必要时多次调用工具获取信息。\n"
        "最后给出结构化的分析结论和建议。"
    )

    # Create LangGraph ReAct agent
    # Model config uses LiteLLM for provider-agnostic routing
    from langchain_openai import ChatOpenAI

    from app.config import settings

    llm = ChatOpenAI(
        model=settings.local_model_name,
        openai_api_key=settings.local_model_api_key,
        openai_api_base=settings.local_model_base_url,
        temperature=0.3,
        max_tokens=4096,
    )

    agent = create_react_agent(llm, tools)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query),
    ]

    try:
        result = await agent.ainvoke({"messages": messages})
        # Extract final response
        final_message = result["messages"][-1]
        return final_message.content
    except Exception as e:
        logger.error("Deep Agent execution failed: %s", e, exc_info=True)
        raise


def _build_tools_from_skills(skill_registry: SkillRegistry) -> list:
    """Convert registered Skills into LangChain tools."""
    from langchain_core.tools import StructuredTool

    tools = []
    for meta in skill_registry.list_all():
        skill = skill_registry.get(meta.id)
        if skill is None:
            continue

        tool = StructuredTool.from_function(
            func=_make_sync_skill_wrapper(skill),
            name=meta.id.replace("-", "_"),
            description=f"{meta.name}: {meta.description}",
        )
        tools.append(tool)

    return tools


def _make_sync_skill_wrapper(skill) -> callable:
    """Wrap an async Skill as a sync function for LangChain tools."""
    import asyncio

    from app.skills.models import SkillInput

    def wrapper(user_message: str = "") -> str:
        """Execute a skill with the given message."""
        skill_input = SkillInput(user_message=user_message)

        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                record = pool.submit(asyncio.run, skill.run(skill_input)).result()
        else:
            record = asyncio.run(skill.run(skill_input))

        if record.output.success:
            return record.output.content
        return f"Error: {record.output.error}"

    wrapper.__name__ = skill.meta().id.replace("-", "_")
    wrapper.__doc__ = f"{skill.meta().name}: {skill.meta().description}"
    return wrapper
