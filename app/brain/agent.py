"""AgentScope Brain layer — deep integration.

Three agent types:
  1. MainAgent (coordinator): understands intent, delegates to role agents
  2. RoleAgent: created from ontology, has specific permissions/tools/scope
  3. Skills are tools that any agent can call through the full lifecycle

Uses AgentScope's full stack:
  - ReActAgent for autonomous reasoning + tool calling
  - MsgHub for multi-agent communication
  - SequentialPipeline / FanoutPipeline for orchestration
  - RedisMemory / InMemoryMemory for conversation persistence
  - Toolkit for skill-as-tool registration
"""

from __future__ import annotations

import logging
from typing import Any

import agentscope
from agentscope.agent import ReActAgent
from agentscope.memory import InMemoryMemory, RedisMemory
from agentscope.message import Msg
from agentscope.pipeline import FanoutPipeline, MsgHub, SequentialPipeline
from agentscope.tool import Toolkit

from app.config import settings

logger = logging.getLogger(__name__)

# ============================================================
# System prompts
# ============================================================

COORDINATOR_PROMPT = """\
你是保健品企业 AI 中台的总调度 Agent。

你的职责：
1. 理解用户意图
2. 如果你有合适的工具，直接调用工具完成任务
3. 如果需要多步骤，规划步骤并依次调用工具
4. 遵守保健品广告法合规要求
5. 保持专业、简洁，用中文回答

{experience_prompt}

重要：调用工具时传入完整的用户原始请求作为 user_message 参数。"""

ROLE_PROMPT_TEMPLATE = """\
你是{role_name}。

职责：{responsibilities}
可用工具权限：{tools}
数据范围：{data_scope}

遵守公司规范，用中文回答。只使用你权限范围内的工具。"""


# ============================================================
# Agent Factory — creates agents from ontology
# ============================================================


class AgentFactory:
    """Creates AgentScope agents from ontology role definitions.

    organization.yaml defines roles → AgentFactory creates matching agents
    with correct permissions, tools, and system prompts.
    """

    def __init__(self) -> None:
        self._model_config: dict[str, Any] | None = None
        self._initialized = False

    def initialize(self, model_config: dict[str, Any] | None = None) -> None:
        """Initialize AgentScope runtime."""
        if self._initialized:
            return

        self._model_config = model_config or self._build_model_config()

        agentscope.init(
            model_configs=[self._model_config],
            project="ai-zhongtai",
            save_log=settings.debug,
        )
        self._initialized = True
        logger.info("AgentScope initialized")

    def _build_model_config(self) -> dict[str, Any]:
        return {
            "config_name": "default",
            "model_type": "litellm_chat",
            "model_name": settings.local_model_name,
            "api_key": settings.local_model_api_key,
            "client_args": {
                "api_base": settings.local_model_base_url,
            },
            "generate_args": {
                "temperature": 0.7,
                "max_tokens": 4096,
            },
        }

    def create_coordinator(
        self,
        toolkit: Toolkit,
        experience_prompt: str = "",
    ) -> ReActAgent:
        """Create the main coordinator agent."""
        prompt = COORDINATOR_PROMPT.format(
            experience_prompt=experience_prompt,
        )

        memory = self._create_memory()

        return ReActAgent(
            name="coordinator",
            sys_prompt=prompt,
            model=self._model_config["config_name"],
            toolkit=toolkit,
            memory=memory,
            max_iters=10,
        )

    def create_role_agent(
        self,
        role_name: str,
        role_def: dict[str, Any],
        toolkit: Toolkit,
    ) -> ReActAgent:
        """Create a role-specific agent from ontology definition.

        Args:
            role_name: Role name from organization.yaml
            role_def: Role definition dict with permissions, tools, data_scope
            toolkit: Toolkit with allowed tools for this role
        """
        prompt = ROLE_PROMPT_TEMPLATE.format(
            role_name=role_name,
            responsibilities=", ".join(role_def.get("permissions", [])),
            tools=", ".join(role_def.get("tools", [])),
            data_scope=", ".join(role_def.get("data_scope", [])),
        )

        memory = self._create_memory()

        return ReActAgent(
            name=role_name.replace(" ", "_"),
            sys_prompt=prompt,
            model=self._model_config["config_name"],
            toolkit=toolkit,
            memory=memory,
            max_iters=5,
        )

    def _create_memory(self):
        """Create memory backend (Redis if available, else in-memory)."""
        try:
            return RedisMemory(
                session_id="zhongtai",
                host=settings.redis_url.split("://")[1].split(":")[0]
                if "://" in settings.redis_url
                else "localhost",
            )
        except Exception:
            return InMemoryMemory()

    # ============================================================
    # Multi-Agent orchestration patterns
    # ============================================================

    def create_sequential_pipeline(
        self, agents: list[ReActAgent]
    ) -> SequentialPipeline:
        """Create a sequential pipeline: Agent1 → Agent2 → Agent3."""
        return SequentialPipeline(agents=agents)

    def create_parallel_pipeline(
        self, agents: list[ReActAgent]
    ) -> FanoutPipeline:
        """Create a parallel pipeline: all agents run concurrently."""
        return FanoutPipeline(agents=agents)

    def create_msg_hub(
        self,
        agents: list[ReActAgent],
        announcement: str = "",
    ) -> MsgHub:
        """Create a MsgHub for multi-agent group discussion."""
        return MsgHub(
            participants=agents,
            announcement=Msg(
                name="system",
                content=announcement or "协作讨论开始",
                role="system",
            ),
        )


# ============================================================
# BrainAgent — high-level interface used by SkillDispatcher
# ============================================================


class BrainAgent:
    """High-level brain interface for the AI middleware.

    Manages the AgentFactory and provides a simple chat() API
    that SkillDispatcher calls.
    """

    def __init__(self) -> None:
        self.factory = AgentFactory()
        self._coordinator: ReActAgent | None = None
        self._toolkit = Toolkit()
        self._role_agents: dict[str, ReActAgent] = {}

    def initialize(
        self, model_config: dict[str, Any] | None = None
    ) -> None:
        """Initialize AgentScope and create the coordinator."""
        self.factory.initialize(model_config)
        self._coordinator = self.factory.create_coordinator(
            toolkit=self._toolkit,
        )
        logger.info("BrainAgent: coordinator created")

    def register_tool(self, func: callable) -> None:
        """Register a tool function for the coordinator."""
        self._toolkit.register_tool_function(func)
        logger.info("Tool registered: %s", func.__name__)

    def create_role_agent(
        self,
        role_name: str,
        role_def: dict[str, Any],
    ) -> ReActAgent:
        """Create and cache a role agent from ontology."""
        # Role agents share the same toolkit as coordinator
        # In Phase 3, each role gets a filtered toolkit
        agent = self.factory.create_role_agent(
            role_name=role_name,
            role_def=role_def,
            toolkit=self._toolkit,
        )
        self._role_agents[role_name] = agent
        logger.info("Role agent created: %s", role_name)
        return agent

    def get_role_agent(self, role_name: str) -> ReActAgent | None:
        """Get a cached role agent."""
        return self._role_agents.get(role_name)

    async def chat(
        self,
        message: str,
        user_id: str = "",
        session_id: str = "",
        experience_prompt: str = "",
    ) -> str:
        """Send a message to the coordinator agent."""
        if not self._coordinator:
            raise RuntimeError("BrainAgent not initialized")

        # Update experience prompt if provided
        if experience_prompt:
            self._coordinator.sys_prompt = COORDINATOR_PROMPT.format(
                experience_prompt=experience_prompt,
            )

        user_msg = Msg(name="user", content=message, role="user")

        try:
            response = self._coordinator(user_msg)
            return response.content if response else "无法处理请求"
        except Exception as e:
            logger.error("Coordinator failed: %s", e, exc_info=True)
            return f"处理请求时出错：{e}"

    async def multi_agent_discuss(
        self,
        topic: str,
        role_names: list[str],
        rounds: int = 3,
    ) -> str:
        """Multi-agent group discussion via MsgHub.

        Multiple role agents discuss a topic and produce a conclusion.
        """
        agents = [
            self._role_agents[name]
            for name in role_names
            if name in self._role_agents
        ]

        if not agents:
            return "没有可用的角色 Agent 参与讨论"

        hub = self.factory.create_msg_hub(
            agents=agents,
            announcement=f"讨论主题：{topic}",
        )

        # Run discussion rounds
        with hub:
            topic_msg = Msg(name="主持人", content=topic, role="user")
            for agent in agents:
                agent(topic_msg)

            for _ in range(rounds - 1):
                for agent in agents:
                    agent()

        # Collect last messages as conclusion
        conclusions = []
        for agent in agents:
            if hasattr(agent, "memory") and agent.memory:
                recent = agent.memory.get_memory(recent_n=1)
                if recent:
                    conclusions.append(
                        f"[{agent.name}]: {recent[-1].content}"
                    )

        return "\n\n".join(conclusions) if conclusions else "讨论未产出结论"

    async def sequential_workflow(
        self,
        task: str,
        role_names: list[str],
    ) -> str:
        """Sequential workflow: Agent1 output → Agent2 input → Agent3 input.

        Models a SOP where each step's output feeds the next.
        """
        agents = [
            self._role_agents[name]
            for name in role_names
            if name in self._role_agents
        ]

        if not agents:
            return "没有可用的角色 Agent 执行流程"

        pipeline = self.factory.create_sequential_pipeline(agents)
        initial_msg = Msg(name="system", content=task, role="user")

        try:
            result = pipeline(initial_msg)
            return result.content if result else "流程执行完毕但无输出"
        except Exception as e:
            logger.error("Sequential workflow failed: %s", e)
            return f"流程执行出错：{e}"

    @property
    def toolkit(self) -> Toolkit:
        return self._toolkit

    @property
    def role_agent_names(self) -> list[str]:
        return list(self._role_agents.keys())
