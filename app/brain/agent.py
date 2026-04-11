"""AgentScope-based Brain layer: ReActAgent with tool calling.

Replaces the old manual intent recognition + routing pipeline with
AgentScope's ReActAgent that autonomously decides which tools to call.
"""

from __future__ import annotations

import logging
from typing import Any

import agentscope
from agentscope.agent import ReActAgent
from agentscope.message import Msg
from agentscope.tool import Toolkit

from app.config import settings

logger = logging.getLogger(__name__)

# System prompt for the AI middleware agent
SYSTEM_PROMPT = """\
你是一个保健品企业的 AI 助手，服务于公司内部员工。

你的职责：
1. 理解员工的请求，调用合适的工具完成任务
2. 如果需要多个步骤，自动规划并依次执行
3. 保持专业、简洁，用中文回答
4. 遵守保健品广告法合规要求

{experience_prompt}

可用工具已注册，请根据用户请求选择合适的工具调用。
如果没有匹配的工具，直接用你的知识回答。"""


class BrainAgent:
    """Central agent powered by AgentScope ReActAgent.

    Wraps AgentScope's ReActAgent with the AI middleware's skill system.
    Skills are registered as tool functions that the agent can call autonomously.
    """

    def __init__(self) -> None:
        self._initialized = False
        self._toolkit = Toolkit()
        self._agent: ReActAgent | None = None

    def initialize(self, model_config: dict[str, Any] | None = None) -> None:
        """Initialize AgentScope and create the ReActAgent.

        Args:
            model_config: AgentScope model configuration dict.
                         If None, uses settings to build a default config.
        """
        if self._initialized:
            return

        # Build model config from settings if not provided
        if model_config is None:
            model_config = self._build_model_config()

        # Initialize AgentScope
        agentscope.init(
            model_configs=[model_config],
            project="ai-zhongtai",
            save_log=settings.debug,
        )

        # Create the ReActAgent
        self._agent = ReActAgent(
            name="zhongtai-agent",
            sys_prompt=SYSTEM_PROMPT.format(experience_prompt=""),
            model=model_config["config_name"],
            toolkit=self._toolkit,
            max_iters=10,
        )

        self._initialized = True
        logger.info("BrainAgent initialized with AgentScope ReActAgent")

    def _build_model_config(self) -> dict[str, Any]:
        """Build AgentScope model config from app settings."""
        # Default to local model via OpenAI-compatible API (vLLM/LiteLLM)
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

    def register_tool(
        self,
        func: callable,
        name: str | None = None,
        description: str | None = None,
    ) -> None:
        """Register a callable as a tool the agent can use.

        Args:
            func: The function to register. Must have type hints and docstring.
            name: Override the function name.
            description: Override the function docstring.
        """
        self._toolkit.register_tool_function(func)
        display_name = name or func.__name__
        logger.info("Registered tool: %s", display_name)

    async def chat(
        self,
        message: str,
        user_id: str = "",
        session_id: str = "",
        experience_prompt: str = "",
    ) -> str:
        """Send a message to the agent and get a response.

        Args:
            message: User's message text.
            user_id: User identifier for context.
            session_id: Session identifier for multi-turn memory.
            experience_prompt: Injected experience patterns.

        Returns:
            Agent's response text.
        """
        if not self._initialized or self._agent is None:
            raise RuntimeError("BrainAgent not initialized. Call initialize() first.")

        # Update system prompt with experience if available
        if experience_prompt:
            self._agent.sys_prompt = SYSTEM_PROMPT.format(
                experience_prompt=experience_prompt,
            )

        # Create message and get response
        user_msg = Msg(name="user", content=message, role="user")

        try:
            response = self._agent(user_msg)
            return response.content if response else "抱歉，我暂时无法处理您的请求。"
        except Exception as e:
            logger.error("Agent execution failed: %s", e, exc_info=True)
            return f"处理请求时出错：{e}"

    @property
    def toolkit(self) -> Toolkit:
        """Access the toolkit for advanced registration."""
        return self._toolkit
