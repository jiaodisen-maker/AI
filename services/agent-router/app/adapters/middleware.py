"""
中间件链 - 洋葱模型（Koa.js 风格）

设计目标：
- 框架无关（不依赖 AgentScope/LangGraph）
- 可拦截（短路返回）
- 可链式
- 异步友好

使用：
    chain = MiddlewareChain()
    chain.use(audit_middleware)
    chain.use(pii_middleware)
    chain.use(rate_limit_middleware)

    response = await chain.execute(ctx, base_handler)
"""
from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from typing import Awaitable, Callable

from .types import AgentInvokeRequest, AgentInvokeResponse

logger = logging.getLogger(__name__)


# ============================================================
# 上下文 + 类型
# ============================================================
@dataclass
class InvokeContext:
    """中间件传递的上下文"""
    request: AgentInvokeRequest
    metadata: dict = field(default_factory=dict)
    started_at: float = field(default_factory=time.time)


# 中间件签名: async (ctx, next) -> response
NextHandler = Callable[[InvokeContext], Awaitable[AgentInvokeResponse]]
Middleware = Callable[[InvokeContext, NextHandler], Awaitable[AgentInvokeResponse]]


# ============================================================
# 中间件链
# ============================================================
class MiddlewareChain:
    """洋葱中间件链"""

    def __init__(self):
        self.middlewares: list[Middleware] = []

    def use(self, mw: Middleware) -> "MiddlewareChain":
        """注册中间件（链式调用）"""
        self.middlewares.append(mw)
        return self

    async def execute(
        self,
        ctx: InvokeContext,
        base_handler: NextHandler,
    ) -> AgentInvokeResponse:
        """执行整个中间件链 + 最终 handler"""
        # 反向构建调用链
        handler = base_handler
        for mw in reversed(self.middlewares):
            current_mw = mw
            current_handler = handler

            async def wrapped(c: InvokeContext, _mw=current_mw, _next=current_handler):
                return await _mw(c, _next)

            handler = wrapped

        return await handler(ctx)


# ============================================================
# 内置中间件 1：审计日志
# ============================================================
async def audit_middleware(
    ctx: InvokeContext, next_handler: NextHandler
) -> AgentInvokeResponse:
    """记录每次调用（用户/agent/输入/输出/耗时）"""
    req = ctx.request
    logger.info(
        f"[AUDIT] user={req.user_id} agent={req.agent_name} "
        f"input_len={len(req.input)}"
    )

    response = await next_handler(ctx)

    logger.info(
        f"[AUDIT] user={req.user_id} agent={req.agent_name} "
        f"output_len={len(response.output)} "
        f"latency={response.latency_ms}ms "
        f"error={response.error or 'none'}"
    )
    return response


# ============================================================
# 内置中间件 2：PII 脱敏
# ============================================================
# 简单 PII 模式（生产建议用专业 NER）
PII_PATTERNS = [
    # 中国大陆手机号
    (r"\b1[3-9]\d{9}\b", "[手机号]"),
    # 邮箱
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[邮箱]"),
    # 中国身份证（18 位）
    (r"\b[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dxX]\b", "[身份证]"),
    # 银行卡号（16-19 位连续数字，宽松匹配）
    (r"\b\d{16,19}\b", "[银行卡]"),
]


def _scrub_pii(text: str) -> tuple[str, list[str]]:
    """脱敏文本，返回 (脱敏后文本, 触发的类型列表)"""
    triggered = []
    for pattern, label in PII_PATTERNS:
        if re.search(pattern, text):
            text = re.sub(pattern, label, text)
            triggered.append(label)
    return text, triggered


async def pii_middleware(
    ctx: InvokeContext, next_handler: NextHandler
) -> AgentInvokeResponse:
    """对输入做 PII 脱敏（避免敏感信息进 LLM）"""
    scrubbed_input, triggered = _scrub_pii(ctx.request.input)
    if triggered:
        logger.warning(
            f"[PII] user={ctx.request.user_id} scrubbed: {triggered}"
        )
        ctx.metadata["pii_triggered"] = triggered
        # 替换 input
        ctx.request.input = scrubbed_input

    response = await next_handler(ctx)

    # 输出也脱敏
    if response.output:
        scrubbed_output, out_triggered = _scrub_pii(response.output)
        if out_triggered:
            logger.warning(
                f"[PII] user={ctx.request.user_id} output scrubbed: {out_triggered}"
            )
            response.output = scrubbed_output

    return response


# ============================================================
# 内置中间件 3：合规禁词
# ============================================================
# 保健品行业常见禁词（这是 demo，生产应该从配置/数据库加载）
DEFAULT_FORBIDDEN_WORDS = [
    "治疗", "治愈", "根治", "特效",
    "100%有效", "立竿见影", "包治百病",
    "替代药物", "胜过药品",
]


def make_compliance_middleware(
    forbidden_words: list[str] | None = None,
    block_input: bool = False,
    sanitize_output: bool = True,
) -> Middleware:
    """生成合规中间件（可配置禁词列表）"""
    words = forbidden_words or DEFAULT_FORBIDDEN_WORDS

    async def compliance_middleware(
        ctx: InvokeContext, next_handler: NextHandler
    ) -> AgentInvokeResponse:
        # 输入禁词（可选拦截）
        if block_input:
            for word in words:
                if word in ctx.request.input:
                    logger.warning(
                        f"[COMPLIANCE] user={ctx.request.user_id} "
                        f"blocked input with word: {word}"
                    )
                    return AgentInvokeResponse(
                        agent_name=ctx.request.agent_name,
                        output=f"[合规拦截] 输入包含违禁词：{word}",
                        error="compliance_block",
                    )

        response = await next_handler(ctx)

        # 输出禁词（默认替换为***）
        if sanitize_output and response.output:
            triggered = []
            for word in words:
                if word in response.output:
                    response.output = response.output.replace(word, "*" * len(word))
                    triggered.append(word)
            if triggered:
                logger.warning(
                    f"[COMPLIANCE] user={ctx.request.user_id} "
                    f"sanitized output: {triggered}"
                )
                ctx.metadata["compliance_sanitized"] = triggered

        return response

    return compliance_middleware


# ============================================================
# 内置中间件 4：限流
# ============================================================
def make_rate_limit_middleware(
    redis_client,  # redis.asyncio.Redis
    max_per_minute: int = 60,
    max_per_day: int = 1000,
) -> Middleware:
    """生成限流中间件（基于 Redis 计数）"""

    async def rate_limit_middleware(
        ctx: InvokeContext, next_handler: NextHandler
    ) -> AgentInvokeResponse:
        user_id = ctx.request.user_id
        now = int(time.time())
        minute_bucket = now // 60
        day_bucket = now // 86400

        minute_key = f"rl:user:{user_id}:m:{minute_bucket}"
        day_key = f"rl:user:{user_id}:d:{day_bucket}"

        pipe = redis_client.pipeline()
        pipe.incr(minute_key)
        pipe.expire(minute_key, 70)
        pipe.incr(day_key)
        pipe.expire(day_key, 86400 + 60)
        results = await pipe.execute()

        minute_count = int(results[0])
        day_count = int(results[2])

        if minute_count > max_per_minute:
            logger.warning(f"[RATE_LIMIT] user={user_id} exceeds {max_per_minute}/min")
            return AgentInvokeResponse(
                agent_name=ctx.request.agent_name,
                output=f"[限流] 调用过于频繁，请稍后再试（{max_per_minute}次/分钟）",
                error="rate_limited",
            )
        if day_count > max_per_day:
            logger.warning(f"[RATE_LIMIT] user={user_id} exceeds {max_per_day}/day")
            return AgentInvokeResponse(
                agent_name=ctx.request.agent_name,
                output=f"[限流] 今日调用次数已达上限（{max_per_day}次/天）",
                error="rate_limited_daily",
            )

        return await next_handler(ctx)

    return rate_limit_middleware


# ============================================================
# 内置中间件 5：经验注入
# ============================================================
def make_experience_middleware(memory_port) -> Middleware:
    """生成经验注入中间件 - 调用前查相似 pattern"""

    async def experience_middleware(
        ctx: InvokeContext, next_handler: NextHandler
    ) -> AgentInvokeResponse:
        # 查询历史相似 pattern
        try:
            patterns = await memory_port.retrieve_patterns(
                skill_name=ctx.request.agent_name,
                query=ctx.request.input,
                top_k=2,
            )
            if patterns:
                logger.info(
                    f"[EXPERIENCE] injected {len(patterns)} patterns "
                    f"for {ctx.request.agent_name}"
                )
                ctx.metadata["injected_patterns"] = len(patterns)
                # 把经验放到 metadata 里，让下游 invoker 能用
                ctx.request.metadata["experience_patterns"] = [
                    {"input": p["input"], "output": p["output"]}
                    for p in patterns
                ]
        except Exception as e:
            logger.warning(f"[EXPERIENCE] retrieve failed: {e}")

        response = await next_handler(ctx)

        # 记录这次调用为新 pattern（如果成功）
        if not response.error and response.output:
            try:
                await memory_port.store_pattern(
                    skill_name=ctx.request.agent_name,
                    input_text=ctx.request.input,
                    output_text=response.output,
                )
            except Exception as e:
                logger.warning(f"[EXPERIENCE] store failed: {e}")

        return response

    return experience_middleware
