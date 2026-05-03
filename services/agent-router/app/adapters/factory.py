"""
Adapter 工厂 - 根据配置创建对应实现

业务代码用法：
    factory = AdapterFactory(config)
    registry = factory.create_agent_registry()

切换框架：改一行 yaml 即可，业务代码 0 改动。
"""
from __future__ import annotations

import os
from enum import Enum
from pathlib import Path

from .ports import (
    AgentRegistryPort,
    LLMPort,
    MemoryPort,
    SessionPort,
)


class FrameworkChoice(str, Enum):
    AGENTSCOPE_1X = "agentscope_1x"
    AGENTSCOPE_2X = "agentscope_2x"
    LANGGRAPH = "langgraph"
    CLAUDE_SDK = "claude_sdk"
    MOCK = "mock"


class AdapterFactory:
    """根据配置创建对应实现"""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.config = config
        # 默认 mock 方便本地启动
        self.framework = FrameworkChoice(
            config.get("framework", os.getenv("AGENT_FRAMEWORK", "mock"))
        )

    # ========================================================
    # Agent Registry（治理层核心）
    # ========================================================
    def create_agent_registry(self) -> AgentRegistryPort:
        """创建 Agent Registry"""
        registry_type = self.config.get(
            "registry_type", os.getenv("REGISTRY_TYPE", "local")
        )

        if registry_type == "local":
            from .impls.local_registry import LocalAgentRegistry
            return LocalAgentRegistry(
                redis_url=self.config.get(
                    "registry_redis_url",
                    os.getenv("REGISTRY_REDIS_URL", "redis://localhost:6379"),
                ),
                skills_dir=Path(self.config.get(
                    "skills_dir", os.getenv("SKILLS_DIR", "/data/skills")
                )),
            )
        else:
            raise NotImplementedError(f"Registry type {registry_type} not implemented")

    # ========================================================
    # LLM Port
    # ========================================================
    def create_llm(self) -> LLMPort:
        if self.framework == FrameworkChoice.MOCK:
            from .impls.mock_adapter import MockLLMAdapter
            return MockLLMAdapter()
        elif self.framework == FrameworkChoice.AGENTSCOPE_1X:
            # TODO: 实现
            raise NotImplementedError("AgentScope 1.x LLM adapter 待实现")
        elif self.framework == FrameworkChoice.LANGGRAPH:
            # TODO: 实现
            raise NotImplementedError("LangGraph LLM adapter 待实现")
        else:
            raise NotImplementedError(f"Framework {self.framework} not supported")

    # ========================================================
    # Session Port
    # ========================================================
    def create_session(self) -> SessionPort:
        session_type = self.config.get(
            "session_type", os.getenv("SESSION_TYPE", "mock")
        )
        if session_type == "mock":
            from .impls.mock_adapter import MockSessionAdapter
            return MockSessionAdapter()
        elif session_type == "redis":
            # TODO: 实现 Redis Session（生产用）
            raise NotImplementedError("Redis Session 待实现")
        else:
            raise NotImplementedError(f"Session type {session_type} not supported")

    # ========================================================
    # Memory Port
    # ========================================================
    def create_memory(self) -> MemoryPort:
        memory_type = self.config.get(
            "memory_type", os.getenv("MEMORY_TYPE", "mock")
        )
        if memory_type == "mock":
            from .impls.mock_adapter import MockMemoryAdapter
            return MockMemoryAdapter()
        else:
            raise NotImplementedError(f"Memory type {memory_type} not supported")
