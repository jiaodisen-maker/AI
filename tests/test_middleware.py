"""中间件链单元测试"""
import pytest

from app.adapters.middleware import (
    InvokeContext,
    MiddlewareChain,
    audit_middleware,
    make_compliance_middleware,
    pii_middleware,
)
from app.adapters.types import AgentInvokeRequest, AgentInvokeResponse


def _make_ctx(input_text: str = "hello") -> InvokeContext:
    return InvokeContext(
        request=AgentInvokeRequest(
            agent_name="test",
            input=input_text,
            session_id="s1",
            user_id="u1",
        )
    )


@pytest.mark.asyncio
async def test_empty_chain():
    chain = MiddlewareChain()

    async def handler(ctx):
        return AgentInvokeResponse(agent_name="test", output="ok")

    response = await chain.execute(_make_ctx(), handler)
    assert response.output == "ok"


@pytest.mark.asyncio
async def test_audit_middleware_passes_through():
    chain = MiddlewareChain().use(audit_middleware)

    async def handler(ctx):
        return AgentInvokeResponse(agent_name="test", output="ok")

    response = await chain.execute(_make_ctx(), handler)
    assert response.output == "ok"


@pytest.mark.asyncio
async def test_pii_middleware_scrubs_phone():
    """PII 中间件应该脱敏手机号"""
    chain = MiddlewareChain().use(pii_middleware)

    captured_input = []

    async def handler(ctx):
        captured_input.append(ctx.request.input)
        return AgentInvokeResponse(agent_name="test", output="ok")

    ctx = _make_ctx("我的手机号 13812345678 请联系")
    response = await chain.execute(ctx, handler)

    # 输入到 handler 时应该已脱敏
    assert "13812345678" not in captured_input[0]
    assert "[手机号]" in captured_input[0]
    assert "pii_triggered" in ctx.metadata


@pytest.mark.asyncio
async def test_pii_middleware_scrubs_output():
    """PII 中间件也应该脱敏输出"""
    chain = MiddlewareChain().use(pii_middleware)

    async def handler(ctx):
        return AgentInvokeResponse(
            agent_name="test",
            output="客户邮箱是 alice@example.com",
        )

    response = await chain.execute(_make_ctx("hi"), handler)
    assert "alice@example.com" not in response.output
    assert "[邮箱]" in response.output


@pytest.mark.asyncio
async def test_compliance_middleware_blocks_input():
    """合规中间件 block_input=True 时应拦截违禁词输入"""
    chain = MiddlewareChain().use(
        make_compliance_middleware(
            forbidden_words=["治疗"], block_input=True
        )
    )

    handler_called = []

    async def handler(ctx):
        handler_called.append(True)
        return AgentInvokeResponse(agent_name="test", output="ok")

    response = await chain.execute(
        _make_ctx("这能治疗糖尿病吗"), handler
    )
    assert response.error == "compliance_block"
    assert handler_called == []  # handler 没被调用


@pytest.mark.asyncio
async def test_compliance_middleware_sanitizes_output():
    """合规中间件应该脱敏输出禁词"""
    chain = MiddlewareChain().use(
        make_compliance_middleware(forbidden_words=["治疗"])
    )

    async def handler(ctx):
        return AgentInvokeResponse(
            agent_name="test",
            output="可以治疗糖尿病",
        )

    response = await chain.execute(_make_ctx("hi"), handler)
    assert "治疗" not in response.output
    assert "**" in response.output


@pytest.mark.asyncio
async def test_chain_execution_order():
    """中间件应该按 use() 顺序执行（洋葱模型）"""
    order = []

    async def mw_a(ctx, next_h):
        order.append("a_pre")
        r = await next_h(ctx)
        order.append("a_post")
        return r

    async def mw_b(ctx, next_h):
        order.append("b_pre")
        r = await next_h(ctx)
        order.append("b_post")
        return r

    async def handler(ctx):
        order.append("handler")
        return AgentInvokeResponse(agent_name="test", output="ok")

    chain = MiddlewareChain().use(mw_a).use(mw_b)
    await chain.execute(_make_ctx(), handler)

    assert order == ["a_pre", "b_pre", "handler", "b_post", "a_post"]
