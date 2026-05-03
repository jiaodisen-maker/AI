"""
Adapter 工厂 - 根据配置创建对应实现

业务代码用法：
    factory = AdapterFactory(config)
    registry = factory.create_agent_registry()
    session = factory.create_session()
    memory = factory.create_memory()
    skill = factory.create_skill_loader()
    llm = factory.create_llm()

切换框架：改一行 yaml/env 即可，业务代码 0 改动。
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
    SkillPort,
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
        self.config = config or {}
        self.framework = FrameworkChoice(
            self._cfg("framework", "AGENT_FRAMEWORK", "mock")
        )

    def _cfg(self, key: str, env: str, default):
        """取配置：优先 config，否则环境变量，最后默认"""
        if key in self.config:
            return self.config[key]
        return os.getenv(env, default)

    # ========================================================
    # Agent Registry（治理层核心）
    # ========================================================
    def create_agent_registry(self) -> AgentRegistryPort:
        registry_type = self._cfg("registry_type", "REGISTRY_TYPE", "local")

        if registry_type == "local":
            from .impls.local_registry import LocalAgentRegistry
            return LocalAgentRegistry(
                redis_url=self._cfg(
                    "registry_redis_url",
                    "REGISTRY_REDIS_URL",
                    "redis://localhost:6379",
                ),
                skills_dir=Path(
                    self._cfg("skills_dir", "SKILLS_DIR", "/data/skills")
                ),
            )
        raise NotImplementedError(f"Registry type '{registry_type}' not implemented")

    # ========================================================
    # LLM Port
    # ========================================================
    def create_llm(self) -> LLMPort:
        if self.framework == FrameworkChoice.MOCK:
            from .impls.mock_adapter import MockLLMAdapter
            return MockLLMAdapter()

        if self.framework == FrameworkChoice.AGENTSCOPE_1X:
            from .impls.agentscope_1x import AgentScope1xLLMAdapter
            model_config = self.config.get("model_config") or {
                "config_name": self._cfg("model_name", "DEFAULT_LLM_MODEL", "qwen-max"),
                "model_type": "dashscope_chat",
                "model_name": self._cfg("model_name", "DEFAULT_LLM_MODEL", "qwen-max"),
                "api_key": os.getenv("DASHSCOPE_API_KEY", ""),
            }
            return AgentScope1xLLMAdapter(model_config=model_config)

        if self.framework == FrameworkChoice.LANGGRAPH:
            from .impls.langgraph_adapter import LangGraphLLMAdapter
            return LangGraphLLMAdapter(
                model_name=self._cfg("model_name", "DEFAULT_LLM_MODEL", "qwen-max"),
                api_base=self._cfg("llm_api_base", "LLM_API_BASE", None),
                api_key=self._cfg("llm_api_key", "LLM_API_KEY", None),
            )

        raise NotImplementedError(f"Framework '{self.framework}' not supported")

    # ========================================================
    # Session Port
    # ========================================================
    def create_session(self) -> SessionPort:
        session_type = self._cfg("session_type", "SESSION_TYPE", "mock")

        if session_type == "mock":
            from .impls.mock_adapter import MockSessionAdapter
            return MockSessionAdapter()

        if session_type == "redis":
            from .impls.redis_session import RedisSessionAdapter
            return RedisSessionAdapter(
                redis_url=self._cfg(
                    "session_redis_url",
                    "SESSION_REDIS_URL",
                    "redis://localhost:6379",
                ),
                ttl_seconds=int(self._cfg("session_ttl", "SESSION_TTL", 7 * 24 * 3600)),
                max_messages=int(
                    self._cfg("session_max_messages", "SESSION_MAX_MESSAGES", 100)
                ),
            )

        raise NotImplementedError(f"Session type '{session_type}' not supported")

    # ========================================================
    # Memory Port
    # ========================================================
    def create_memory(self) -> MemoryPort:
        memory_type = self._cfg("memory_type", "MEMORY_TYPE", "mock")

        if memory_type == "mock":
            from .impls.mock_adapter import MockMemoryAdapter
            return MockMemoryAdapter()

        if memory_type == "redis":
            from .impls.redis_memory import RedisMemoryAdapter
            return RedisMemoryAdapter(
                redis_url=self._cfg(
                    "memory_redis_url",
                    "MEMORY_REDIS_URL",
                    "redis://localhost:6379",
                ),
            )

        raise NotImplementedError(f"Memory type '{memory_type}' not supported")

    # ========================================================
    # Skill Port
    # ========================================================
    def create_skill_loader(self) -> SkillPort:
        skill_type = self._cfg("skill_type", "SKILL_TYPE", "filesystem")

        if skill_type == "filesystem":
            from .impls.skill_loader import FilesystemSkillLoader
            skills_dir = Path(self._cfg("skills_dir", "SKILLS_DIR", "/data/skills"))
            return FilesystemSkillLoader(default_dirs=[skills_dir])

        raise NotImplementedError(f"Skill type '{skill_type}' not supported")
