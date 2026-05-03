"""
Mock 实现 - 业务测试可以脱离任何框架。

让单元测试不需要起 Redis、不需要起 LLM、不需要起任何框架。
"""
from __future__ import annotations

import time
from collections import defaultdict
from typing import AsyncIterator

from ..ports import LLMPort, MemoryPort, SessionPort
from ..types import (
    GenerateRequest,
    GenerateResponse,
    Message,
    Role,
    SessionState,
    StreamChunk,
)


# ============================================================
# Mock LLM（按关键词返回固定回复）
# ============================================================
class MockLLMAdapter(LLMPort):
    """测试用 Mock LLM"""

    def __init__(self, canned_responses: dict[str, str] | None = None):
        self.canned = canned_responses or {}
        self.calls: list[GenerateRequest] = []

    async def generate(self, req: GenerateRequest) -> GenerateResponse:
        self.calls.append(req)

        last_user_msg = ""
        for msg in reversed(req.messages):
            if msg.role == Role.USER:
                last_user_msg = msg.content
                break

        for trigger, response in self.canned.items():
            if trigger in last_user_msg:
                return GenerateResponse(content=response)

        return GenerateResponse(content=f"[MOCK] received: {last_user_msg}")

    async def stream(self, req: GenerateRequest) -> AsyncIterator[StreamChunk]:
        response = await self.generate(req)
        # 字符级流式
        for char in response.content:
            yield StreamChunk(delta=char, is_last=False)
        yield StreamChunk(delta="", is_last=True)

    def get_supported_models(self) -> list[str]:
        return ["mock-model", "mock-fast"]


# ============================================================
# Mock Session（内存存储）
# ============================================================
class MockSessionAdapter(SessionPort):
    """测试用内存 Session"""

    def __init__(self):
        self._sessions: dict[str, SessionState] = {}

    async def get_or_create(self, session_id: str, user_id: str) -> SessionState:
        if session_id not in self._sessions:
            self._sessions[session_id] = SessionState(
                session_id=session_id,
                user_id=user_id,
            )
        return self._sessions[session_id]

    async def append_message(self, session_id: str, msg: Message) -> None:
        if session_id not in self._sessions:
            return
        self._sessions[session_id].messages.append(msg)
        self._sessions[session_id].updated_at = time.time()

    async def get_history(self, session_id: str, limit: int = 20) -> list[Message]:
        if session_id not in self._sessions:
            return []
        return self._sessions[session_id].messages[-limit:]

    async def save(self, session: SessionState) -> None:
        self._sessions[session.session_id] = session

    async def clear(self, session_id: str) -> None:
        self._sessions.pop(session_id, None)


# ============================================================
# Mock Memory（内存经验引擎）
# ============================================================
class MockMemoryAdapter(MemoryPort):
    """测试用内存经验引擎"""

    def __init__(self):
        self._patterns: dict[str, list[dict]] = defaultdict(list)
        self._knowledge: dict[str, list[dict]] = defaultdict(list)

    async def store_pattern(
        self,
        skill_name: str,
        input_text: str,
        output_text: str,
        feedback: dict | None = None,
    ) -> str:
        pattern_id = f"pattern_{skill_name}_{len(self._patterns[skill_name])}"
        self._patterns[skill_name].append({
            "id": pattern_id,
            "input": input_text,
            "output": output_text,
            "feedback": feedback or {},
            "timestamp": time.time(),
        })
        return pattern_id

    async def retrieve_patterns(
        self, skill_name: str, query: str, top_k: int = 3
    ) -> list[dict]:
        # 简单关键词匹配
        patterns = self._patterns.get(skill_name, [])
        scored = []
        for p in patterns:
            score = sum(1 for w in query.split() if w in p["input"])
            if score > 0:
                scored.append((score, p))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [p for _, p in scored[:top_k]]

    async def store_knowledge(
        self, namespace: str, content: str, metadata: dict
    ) -> str:
        kid = f"k_{namespace}_{len(self._knowledge[namespace])}"
        self._knowledge[namespace].append({
            "id": kid,
            "content": content,
            "metadata": metadata,
        })
        return kid

    async def retrieve_knowledge(
        self, namespace: str, query: str, top_k: int = 5
    ) -> list[dict]:
        items = self._knowledge.get(namespace, [])
        scored = []
        for item in items:
            score = sum(1 for w in query.split() if w in item["content"])
            if score > 0:
                scored.append((score, item))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [i for _, i in scored[:top_k]]
