"""
AgentScope 1.x LLM Adapter

唯一允许 import agentscope 的文件之一。
当 AgentScope 2.0 GA 时，新建 agentscope_2x.py 平行存在。

注意：
- agentscope 是可选依赖（pip install agentscope）
- 如果未安装，import 时报错，但 Mock/HTTP 路径仍可用
"""
from __future__ import annotations

import logging
from typing import AsyncIterator

from ..ports import LLMPort
from ..types import (
    GenerateRequest,
    GenerateResponse,
    Message,
    Role,
    StreamChunk,
    ToolCall,
)

logger = logging.getLogger(__name__)


class AgentScope1xLLMAdapter(LLMPort):
    """LLM Port 的 AgentScope 1.x 实现"""

    def __init__(self, model_config: dict, project: str = "ai-platform"):
        # 延迟 import，避免无 agentscope 环境也能起服务
        try:
            import agentscope
            from agentscope.agents import ReActAgent
        except ImportError as e:
            raise ImportError(
                "AgentScope 1.x adapter 需要安装 agentscope: pip install agentscope"
            ) from e

        agentscope.init(model_configs=[model_config], project=project)
        self._react_agent_cls = ReActAgent
        self.default_model = model_config.get("config_name", "default")

    async def generate(self, req: GenerateRequest) -> GenerateResponse:
        """同步生成"""
        from agentscope.message import Msg

        # 系统 prompt 提取
        system_prompt = ""
        for m in req.messages:
            if m.role == Role.SYSTEM:
                system_prompt = m.content
                break

        # 找最后一条用户消息
        last_user = None
        for m in reversed(req.messages):
            if m.role == Role.USER:
                last_user = m
                break

        if not last_user:
            return GenerateResponse(content="(empty)", is_complete=True)

        # 创建临时 agent（无状态调用）
        # 生产场景应该缓存 agent 实例
        agent = self._react_agent_cls(
            name="oneshot",
            model_config_name=req.model or self.default_model,
            sys_prompt=system_prompt or "你是一个有帮助的 AI 助手",
        )

        as_msg = Msg(name="user", content=last_user.content, role="user")

        try:
            # AgentScope 1.x 的 agent 是 sync callable
            import asyncio
            response = await asyncio.to_thread(agent, as_msg)
        except Exception as e:
            logger.exception(f"AgentScope generate failed: {e}")
            return GenerateResponse(content="", is_complete=True, usage={"error": str(e)})

        return GenerateResponse(
            content=str(response.content) if response and response.content else "",
            tool_calls=self._extract_tool_calls(response),
            is_complete=True,
        )

    async def stream(self, req: GenerateRequest) -> AsyncIterator[StreamChunk]:
        """1.x 流式能力有限 — fallback 到 generate + 单 chunk"""
        response = await self.generate(req)
        yield StreamChunk(delta=response.content, is_last=True, usage=response.usage)

    def get_supported_models(self) -> list[str]:
        # 实际可用模型由 model_configs 决定
        return ["qwen-max", "qwen-plus", "qwen-turbo", "claude-sonnet-4-6", "gpt-4o"]

    @staticmethod
    def _extract_tool_calls(response) -> list[ToolCall]:
        """从 AgentScope response 提取 tool calls"""
        if not response:
            return []
        tool_calls = []
        # AgentScope 1.x 的 tool call 在 response.tool_use 或 metadata 里
        tool_use = getattr(response, "tool_use", None) or []
        for i, tu in enumerate(tool_use):
            if isinstance(tu, dict):
                tool_calls.append(
                    ToolCall(
                        id=tu.get("id", f"call_{i}"),
                        name=tu.get("name", ""),
                        arguments=tu.get("input", {}),
                    )
                )
        return tool_calls
