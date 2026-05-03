"""Invoker 单元测试 - 验证 Mock Invoker 行为"""
import pytest

from app.adapters.impls.invokers import MockInvoker
from app.adapters.types import (
    AgentFramework,
    AgentInvokeRequest,
    AgentSpec,
    Skill,
)


@pytest.mark.asyncio
async def test_mock_invoker_canned():
    """Mock Invoker 按关键词返回"""
    invoker = MockInvoker(canned_responses={"文案": "返回了文案"})

    spec = AgentSpec(
        name="test",
        display_name="test",
        description="d",
        framework=AgentFramework.MOCK,
        endpoint="x",
        skill=Skill(name="s", description="d"),
    )
    req = AgentInvokeRequest(
        agent_name="test",
        input="帮我写文案",
        session_id="s1",
        user_id="u1",
    )
    out = await invoker.invoke(spec, req)
    assert out == "返回了文案"


@pytest.mark.asyncio
async def test_mock_invoker_records_calls():
    """Mock Invoker 记录调用便于断言"""
    invoker = MockInvoker()
    spec = AgentSpec(
        name="test",
        display_name="test",
        description="d",
        framework=AgentFramework.MOCK,
        endpoint="x",
        skill=Skill(name="s", description="d"),
    )
    await invoker.invoke(spec, AgentInvokeRequest(
        agent_name="test",
        input="hi",
        session_id="s",
        user_id="u",
    ))
    assert len(invoker.calls) == 1
    assert invoker.calls[0][1].input == "hi"
