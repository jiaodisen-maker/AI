"""Mock Adapter 测试 - 验证业务能不依赖任何框架做单元测试"""
import pytest

from app.adapters.impls.mock_adapter import (
    MockLLMAdapter,
    MockMemoryAdapter,
    MockSessionAdapter,
)
from app.adapters.types import (
    GenerateRequest,
    Message,
    Role,
)


@pytest.mark.asyncio
async def test_mock_llm_canned_response():
    """Mock LLM 应该按关键词返回预设回复"""
    llm = MockLLMAdapter(canned_responses={
        "文案": "这是一段合规文案",
        "禁词": "拦截了违禁词",
    })

    response = await llm.generate(GenerateRequest(
        messages=[Message(role=Role.USER, content="帮我写文案")]
    ))
    assert response.content == "这是一段合规文案"


@pytest.mark.asyncio
async def test_mock_llm_records_calls():
    """Mock LLM 应该记录所有调用，方便测试断言"""
    llm = MockLLMAdapter()
    await llm.generate(GenerateRequest(
        messages=[Message(role=Role.USER, content="hi")]
    ))
    await llm.generate(GenerateRequest(
        messages=[Message(role=Role.USER, content="hello")]
    ))
    assert len(llm.calls) == 2


@pytest.mark.asyncio
async def test_mock_llm_streaming():
    """Mock LLM 流式应该按字符返回"""
    llm = MockLLMAdapter(canned_responses={"hi": "abc"})

    chunks = []
    async for chunk in llm.stream(GenerateRequest(
        messages=[Message(role=Role.USER, content="hi")]
    )):
        chunks.append(chunk)

    # "abc" 3 字 + 1 个 is_last
    assert len(chunks) == 4
    assert chunks[-1].is_last is True


@pytest.mark.asyncio
async def test_mock_session_user_isolation():
    """关键测试：两个用户的会话互相不可见（解决 HiClaw 多用户共享问题）"""
    session = MockSessionAdapter()

    s1 = await session.get_or_create("alice", "alice")
    s2 = await session.get_or_create("bob", "bob")

    await session.append_message(
        "alice", Message(role=Role.USER, content="alice 的机密")
    )

    history_alice = await session.get_history("alice")
    history_bob = await session.get_history("bob")

    assert len(history_alice) == 1
    assert "机密" in history_alice[0].content
    # bob 看不到 alice 的内容
    assert len(history_bob) == 0


@pytest.mark.asyncio
async def test_mock_memory_pattern_storage():
    """经验引擎 Mock - 存取 pattern"""
    memory = MockMemoryAdapter()

    pid = await memory.store_pattern(
        skill_name="compliant-copy",
        input_text="阿胶糕文案",
        output_text="经过合规审核的文案",
    )
    assert pid.startswith("pattern_")

    patterns = await memory.retrieve_patterns(
        skill_name="compliant-copy",
        query="阿胶糕",
    )
    assert len(patterns) == 1
    assert patterns[0]["input"] == "阿胶糕文案"
