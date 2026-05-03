"""
弹性工具：重试 / 超时 / 熔断

依赖：纯标准库 + asyncio
不依赖 tenacity 等第三方库（保持轻量）
"""
from __future__ import annotations

import asyncio
import logging
import random
import time
from dataclasses import dataclass, field
from typing import Awaitable, Callable, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


# ============================================================
# 重试（指数退避 + 抖动）
# ============================================================
async def retry_async(
    fn: Callable[[], Awaitable[T]],
    max_attempts: int = 3,
    initial_delay: float = 0.5,
    max_delay: float = 8.0,
    backoff_factor: float = 2.0,
    jitter: float = 0.1,
    retryable_exceptions: tuple[type[Exception], ...] = (Exception,),
    on_retry: Callable[[int, Exception], None] | None = None,
) -> T:
    """指数退避 + 抖动的异步重试"""
    last_exc: Exception | None = None
    delay = initial_delay

    for attempt in range(1, max_attempts + 1):
        try:
            return await fn()
        except retryable_exceptions as e:
            last_exc = e
            if attempt >= max_attempts:
                break
            sleep_for = min(delay, max_delay) * (1 + random.uniform(-jitter, jitter))
            if on_retry:
                on_retry(attempt, e)
            else:
                logger.warning(
                    f"Retry {attempt}/{max_attempts} after {sleep_for:.2f}s: {e}"
                )
            await asyncio.sleep(sleep_for)
            delay *= backoff_factor

    assert last_exc is not None
    raise last_exc


# ============================================================
# 超时
# ============================================================
async def with_timeout(
    coro: Awaitable[T],
    timeout: float,
    error_message: str = "operation timed out",
) -> T:
    """异步超时（替代 asyncio.wait_for 的语义糖）"""
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError as e:
        raise TimeoutError(error_message) from e


# ============================================================
# 熔断器
# ============================================================
class CircuitBreakerState:
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreakerError(Exception):
    """熔断打开时抛出"""


@dataclass
class CircuitBreaker:
    """简化版熔断器（per-key 独立计数）"""
    failure_threshold: int = 5
    recovery_timeout: float = 30.0
    half_open_test_calls: int = 1

    _state: dict[str, str] = field(default_factory=dict)
    _failures: dict[str, int] = field(default_factory=dict)
    _opened_at: dict[str, float] = field(default_factory=dict)

    def _state_for(self, key: str) -> str:
        state = self._state.get(key, CircuitBreakerState.CLOSED)
        if state == CircuitBreakerState.OPEN:
            opened_at = self._opened_at.get(key, 0)
            if time.time() - opened_at >= self.recovery_timeout:
                self._state[key] = CircuitBreakerState.HALF_OPEN
                return CircuitBreakerState.HALF_OPEN
        return state

    async def call(
        self,
        key: str,
        fn: Callable[[], Awaitable[T]],
    ) -> T:
        """通过熔断器调用 fn"""
        state = self._state_for(key)

        if state == CircuitBreakerState.OPEN:
            raise CircuitBreakerError(f"Circuit '{key}' is open")

        try:
            result = await fn()
        except Exception as e:
            self._on_failure(key)
            raise
        else:
            self._on_success(key)
            return result

    def _on_failure(self, key: str) -> None:
        self._failures[key] = self._failures.get(key, 0) + 1
        if self._failures[key] >= self.failure_threshold:
            self._state[key] = CircuitBreakerState.OPEN
            self._opened_at[key] = time.time()
            logger.warning(
                f"Circuit '{key}' OPENED after {self._failures[key]} failures"
            )

    def _on_success(self, key: str) -> None:
        if self._state.get(key) != CircuitBreakerState.CLOSED:
            logger.info(f"Circuit '{key}' CLOSED (recovered)")
        self._state[key] = CircuitBreakerState.CLOSED
        self._failures.pop(key, None)
        self._opened_at.pop(key, None)
