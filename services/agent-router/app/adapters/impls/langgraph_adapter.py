"""
LangGraph LLM Adapter

证明 6 Port 抽象的可移植性 - 同一份业务代码可以切换到 LangGraph。

依赖（可选）:
  pip install langchain-core langchain-openai

如果未安装，import 时报错，但 Mock/AgentScope 路径仍可用。
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


class LangGraphLLMAdapter(LLMPort):
    """LLM Port 的 LangGraph/LangChain 实现"""

    def __init__(
        self,
        model_name: str = "qwen-max",
        api_base: str | None = None,
        api_key: str | None = None,
        model_kwargs: dict | None = None,
    ):
        try:
            from langchain_openai import ChatOpenAI
        except ImportError as e:
            raise ImportError(
                "LangGraph adapter 需要安装 langchain-openai: "
                "pip install langchain-openai langchain-core"
            ) from e

        kwargs = {"model": model_name}
        if api_base:
            kwargs["base_url"] = api_base
        if api_key:
            kwargs["api_key"] = api_key
        if model_kwargs:
            kwargs.update(model_kwargs)

        self.model_name = model_name
        self.llm = ChatOpenAI(**kwargs)

    async def generate(self, req: GenerateRequest) -> GenerateResponse:
        from langchain_core.messages import (
            AIMessage,
            HumanMessage,
            SystemMessage,
            ToolMessage,
        )

        lc_messages = []
        for m in req.messages:
            if m.role == Role.USER:
                lc_messages.append(HumanMessage(content=m.content))
            elif m.role == Role.ASSISTANT:
                lc_messages.append(AIMessage(content=m.content))
            elif m.role == Role.SYSTEM:
                lc_messages.append(SystemMessage(content=m.content))
            elif m.role == Role.TOOL:
                lc_messages.append(
                    ToolMessage(
                        content=m.content,
                        tool_call_id=m.metadata.get("tool_call_id", ""),
                    )
                )

        try:
            llm = self.llm
            if req.tools:
                llm = self.llm.bind_tools([self._tool_to_lc(t) for t in req.tools])
            response = await llm.ainvoke(lc_messages)
        except Exception as e:
            logger.exception(f"LangGraph generate failed: {e}")
            return GenerateResponse(content="", usage={"error": str(e)})

        tool_calls = []
        for tc in getattr(response, "tool_calls", None) or []:
            tool_calls.append(
                ToolCall(
                    id=tc.get("id", ""),
                    name=tc.get("name", ""),
                    arguments=tc.get("args", {}),
                )
            )

        return GenerateResponse(
            content=str(response.content) if response.content else "",
            tool_calls=tool_calls,
            is_complete=True,
            usage=getattr(response, "usage_metadata", {}) or {},
        )

    async def stream(self, req: GenerateRequest) -> AsyncIterator[StreamChunk]:
        from langchain_core.messages import HumanMessage, SystemMessage

        lc_messages = []
        for m in req.messages:
            if m.role == Role.USER:
                lc_messages.append(HumanMessage(content=m.content))
            elif m.role == Role.SYSTEM:
                lc_messages.append(SystemMessage(content=m.content))

        try:
            async for chunk in self.llm.astream(lc_messages):
                content = chunk.content if isinstance(chunk.content, str) else ""
                yield StreamChunk(delta=content, is_last=False)
            yield StreamChunk(delta="", is_last=True)
        except Exception as e:
            logger.exception(f"LangGraph stream failed: {e}")
            yield StreamChunk(delta="", is_last=True, usage={"error": str(e)})

    def get_supported_models(self) -> list[str]:
        # 通过 LiteLLM/OpenAI 兼容协议支持的模型
        return [
            "qwen-max", "qwen-plus", "qwen-turbo",
            "claude-sonnet-4-6", "claude-opus-4-7",
            "gpt-4o", "gpt-4o-mini",
            "deepseek-chat",
        ]

    @staticmethod
    def _tool_to_lc(schema):
        """ToolSchema → LangChain tool def（OpenAI 函数 schema 风格）"""
        return {
            "type": "function",
            "function": {
                "name": schema.name,
                "description": schema.description,
                "parameters": schema.parameters,
            },
        }
