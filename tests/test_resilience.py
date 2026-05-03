"""弹性工具测试：retry / timeout / circuit breaker"""
import asyncio

import pytest

from app.adapters.resilience import (
    CircuitBreaker,
    CircuitBreakerError,
    retry_async,
    with_timeout,
)


@pytest.mark.asyncio
async def test_retry_succeeds_eventually():
    """重试在第 3 次成功"""
    counter = {"n": 0}

    async def flaky():
        counter["n"] += 1
        if counter["n"] < 3:
            raise ValueError("transient")
        return "ok"

    result = await retry_async(flaky, max_attempts=5, initial_delay=0.01)
    assert result == "ok"
    assert counter["n"] == 3


@pytest.mark.asyncio
async def test_retry_exhausts():
    """重试用尽后抛原异常"""
    async def always_fail():
        raise ValueError("perm")

    with pytest.raises(ValueError, match="perm"):
        await retry_async(always_fail, max_attempts=2, initial_delay=0.01)


@pytest.mark.asyncio
async def test_with_timeout_succeeds():
    async def quick():
        await asyncio.sleep(0.01)
        return "fast"

    result = await with_timeout(quick(), timeout=1.0)
    assert result == "fast"


@pytest.mark.asyncio
async def test_with_timeout_fails():
    async def slow():
        await asyncio.sleep(1)
        return "x"

    with pytest.raises(TimeoutError):
        await with_timeout(slow(), timeout=0.1)


@pytest.mark.asyncio
async def test_circuit_breaker_opens_on_failures():
    breaker = CircuitBreaker(failure_threshold=2, recovery_timeout=10)

    async def failing():
        raise ValueError("fail")

    # 前 2 次失败：抛原异常
    for _ in range(2):
        with pytest.raises(ValueError):
            await breaker.call("test", failing)

    # 第 3 次：熔断器打开，抛 CircuitBreakerError
    with pytest.raises(CircuitBreakerError):
        await breaker.call("test", failing)


@pytest.mark.asyncio
async def test_circuit_breaker_recovery():
    breaker = CircuitBreaker(failure_threshold=1, recovery_timeout=0.1)

    async def failing():
        raise ValueError()

    async def succeeding():
        return "ok"

    # 触发熔断
    with pytest.raises(ValueError):
        await breaker.call("test", failing)
    with pytest.raises(CircuitBreakerError):
        await breaker.call("test", failing)

    # 等待恢复
    await asyncio.sleep(0.15)

    # 半开状态：成功后回到 closed
    result = await breaker.call("test", succeeding)
    assert result == "ok"

    # 之后调用正常
    result = await breaker.call("test", succeeding)
    assert result == "ok"


@pytest.mark.asyncio
async def test_circuit_breaker_per_key():
    """不同 key 独立计数"""
    breaker = CircuitBreaker(failure_threshold=2, recovery_timeout=10)

    async def fail_a():
        raise ValueError()

    async def succeed_b():
        return "b"

    # A 失败 2 次 → 熔断
    for _ in range(2):
        with pytest.raises(ValueError):
            await breaker.call("agent_a", fail_a)
    with pytest.raises(CircuitBreakerError):
        await breaker.call("agent_a", fail_a)

    # B 不受影响
    result = await breaker.call("agent_b", succeed_b)
    assert result == "b"
