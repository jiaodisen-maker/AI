"""
框架调用器（Invoker）。
每个第三方 Agent 框架（Coze/Dify/LangGraph 等）一个实现。

设计原则：
- 输入：AgentSpec + AgentInvokeRequest
- 输出：str（Agent 的响应文本）
- 屏蔽各框架 API 差异
- 错误抛 InvokerError
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import AsyncIterator

import httpx

from ..types import (
    AgentInvokeRequest,
    AgentSpec,
    StreamChunk,
)


class InvokerError(Exception):
    """调用器错误（所有 Invoker 异常都抛这个）"""


# ============================================================
# 基类
# ============================================================
class FrameworkInvoker(ABC):
    """各框架 Invoker 的抽象基类"""

    @abstractmethod
    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        """同步调用，返回完整文本"""
        raise NotImplementedError

    async def stream_invoke(
        self, spec: AgentSpec, req: AgentInvokeRequest
    ) -> AsyncIterator[StreamChunk]:
        """流式调用，默认 fallback 到 invoke + 单 chunk"""
        text = await self.invoke(spec, req)
        yield StreamChunk(delta=text, is_last=True)


# ============================================================
# Coze（扣子）Invoker
# ============================================================
class CozeInvoker(FrameworkInvoker):
    """Coze / 扣子 Bot 调用"""

    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        bot_id = spec.metadata.get("bot_id")
        if not bot_id:
            raise InvokerError("Coze Agent 缺少 metadata.bot_id")

        token = spec.auth_config.get("token") or spec.auth_config.get("api_key")
        if not token:
            raise InvokerError("Coze Agent 缺少 auth_config.token")

        async with httpx.AsyncClient(timeout=spec.timeout_seconds) as client:
            try:
                response = await client.post(
                    spec.endpoint,
                    json={
                        "bot_id": bot_id,
                        "user_id": req.user_id,
                        "query": req.input,
                        "stream": False,
                        "conversation_id": req.session_id,
                    },
                    headers={
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/json",
                    },
                )
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPError as e:
                raise InvokerError(f"Coze HTTP error: {e}") from e

        # Coze 响应格式：messages 数组，最后一条 type=answer
        messages = data.get("messages", [])
        for msg in reversed(messages):
            if msg.get("type") == "answer":
                return msg.get("content", "")
        # fallback
        return messages[-1].get("content", "") if messages else ""


# ============================================================
# Dify Invoker
# ============================================================
class DifyInvoker(FrameworkInvoker):
    """Dify 应用调用"""

    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        api_key = spec.auth_config.get("api_key")
        if not api_key:
            raise InvokerError("Dify Agent 缺少 auth_config.api_key")

        endpoint = spec.endpoint.rstrip("/") + "/chat-messages"

        async with httpx.AsyncClient(timeout=spec.timeout_seconds) as client:
            try:
                response = await client.post(
                    endpoint,
                    json={
                        "inputs": req.metadata.get("inputs", {}),
                        "query": req.input,
                        "user": req.user_id,
                        "conversation_id": req.metadata.get("conversation_id", ""),
                        "response_mode": "blocking",
                    },
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                )
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPError as e:
                raise InvokerError(f"Dify HTTP error: {e}") from e

        return data.get("answer", "")


# ============================================================
# LangGraph Invoker（HTTP 模式）
# ============================================================
class LangGraphInvoker(FrameworkInvoker):
    """LangGraph 通过 LangServe HTTP 接口调用"""

    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        endpoint = spec.endpoint.rstrip("/") + "/invoke"

        async with httpx.AsyncClient(timeout=spec.timeout_seconds) as client:
            try:
                response = await client.post(
                    endpoint,
                    json={
                        "input": {
                            "messages": [{"role": "user", "content": req.input}],
                        },
                        "config": {
                            "configurable": {"thread_id": req.session_id},
                        },
                    },
                )
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPError as e:
                raise InvokerError(f"LangGraph HTTP error: {e}") from e

        # LangGraph 响应：output.messages 最后一条
        output = data.get("output", {})
        if isinstance(output, dict):
            messages = output.get("messages", [])
            if messages:
                return messages[-1].get("content", "")
        return str(output)


# ============================================================
# AgentScope 1.x Invoker（通过 agentscope-runtime HTTP）
# ============================================================
class AgentScope1xInvoker(FrameworkInvoker):
    """AgentScope 1.x 通过 agentscope-runtime HTTP 接口调用"""

    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        async with httpx.AsyncClient(timeout=spec.timeout_seconds) as client:
            try:
                response = await client.post(
                    spec.endpoint,
                    json={
                        "message": req.input,
                        "session_id": req.session_id,
                        "user_id": req.user_id,
                    },
                )
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPError as e:
                raise InvokerError(f"AgentScope HTTP error: {e}") from e

        return data.get("content", "") or data.get("output", "")


# ============================================================
# Custom HTTP Invoker（你自建 Agent 的标准接口）
# ============================================================
class CustomHTTPInvoker(FrameworkInvoker):
    """
    自建 Agent 标准 HTTP 接口

    约定的 Agent HTTP 接口：
    POST {endpoint}
    Body: {
        "input": str,
        "user_id": str,
        "session_id": str,
        "metadata": {}
    }
    Response: {
        "output": str,
        "metadata": {}
    }
    """

    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        headers = {"Content-Type": "application/json"}
        if spec.auth_type == "bearer":
            token = spec.auth_config.get("token")
            if token:
                headers["Authorization"] = f"Bearer {token}"
        elif spec.auth_type == "api_key":
            api_key = spec.auth_config.get("api_key")
            header_name = spec.auth_config.get("header_name", "X-API-Key")
            if api_key:
                headers[header_name] = api_key

        async with httpx.AsyncClient(timeout=spec.timeout_seconds) as client:
            try:
                response = await client.post(
                    spec.endpoint,
                    json={
                        "input": req.input,
                        "user_id": req.user_id,
                        "session_id": req.session_id,
                        "metadata": req.metadata,
                    },
                    headers=headers,
                )
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPError as e:
                raise InvokerError(f"Custom HTTP error: {e}") from e

        return data.get("output", "")


# ============================================================
# Mock Invoker（测试用）
# ============================================================
class MockInvoker(FrameworkInvoker):
    """测试用 Mock - 永远返回固定回复"""

    def __init__(self, canned_responses: dict[str, str] | None = None):
        self.canned = canned_responses or {}
        self.calls: list[tuple[AgentSpec, AgentInvokeRequest]] = []

    async def invoke(self, spec: AgentSpec, req: AgentInvokeRequest) -> str:
        self.calls.append((spec, req))
        # 关键词匹配
        for trigger, response in self.canned.items():
            if trigger in req.input:
                return response
        return f"[MOCK:{spec.name}] 收到消息：{req.input}"


# ============================================================
# 工厂：根据 framework 选 Invoker
# ============================================================
def build_default_invokers() -> dict:
    """构建默认的 Invoker 映射"""
    from ..types import AgentFramework

    return {
        AgentFramework.COZE: CozeInvoker(),
        AgentFramework.DIFY: DifyInvoker(),
        AgentFramework.LANGGRAPH: LangGraphInvoker(),
        AgentFramework.AGENTSCOPE_1X: AgentScope1xInvoker(),
        AgentFramework.CUSTOM_HTTP: CustomHTTPInvoker(),
        AgentFramework.MOCK: MockInvoker(),
    }
