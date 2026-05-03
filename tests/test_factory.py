"""工厂模式测试 - 验证可以根据配置切换实现"""
import pytest

from app.adapters.factory import AdapterFactory, FrameworkChoice
from app.adapters.impls.mock_adapter import (
    MockLLMAdapter,
    MockMemoryAdapter,
    MockSessionAdapter,
)
from app.adapters.ports import (
    AgentRegistryPort,
    LLMPort,
    MemoryPort,
    SessionPort,
    SkillPort,
)


def test_default_framework_is_mock():
    factory = AdapterFactory()
    assert factory.framework == FrameworkChoice.MOCK


def test_factory_creates_mock_llm():
    factory = AdapterFactory({"framework": "mock"})
    llm = factory.create_llm()
    assert isinstance(llm, MockLLMAdapter)
    assert isinstance(llm, LLMPort)


def test_factory_creates_mock_session():
    factory = AdapterFactory({"session_type": "mock"})
    session = factory.create_session()
    assert isinstance(session, MockSessionAdapter)
    assert isinstance(session, SessionPort)


def test_factory_creates_mock_memory():
    factory = AdapterFactory({"memory_type": "mock"})
    memory = factory.create_memory()
    assert isinstance(memory, MockMemoryAdapter)
    assert isinstance(memory, MemoryPort)


def test_factory_creates_filesystem_skill_loader(tmp_path):
    factory = AdapterFactory({
        "skill_type": "filesystem",
        "skills_dir": str(tmp_path),
    })
    loader = factory.create_skill_loader()
    assert isinstance(loader, SkillPort)


def test_unsupported_framework_raises():
    factory = AdapterFactory({"framework": "claude_sdk"})  # 暂未实现
    with pytest.raises(NotImplementedError):
        factory.create_llm()
