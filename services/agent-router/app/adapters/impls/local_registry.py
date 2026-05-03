"""
本地 Agent Registry 实现（基于 Redis + 文件存储）

适合 20-100 个 Agent 规模。

设计：
- 元数据：Redis Hash + Sorted Set 索引
- SKILL.md：本地文件系统
- 调用：通过 Invoker 路由
- 检索：BM25-like 关键词（生产可换 embedding）

数据模型：
  Redis Keys:
    agent:{name}                          → Hash {spec: json_str}
    agents:all                            → Set (所有 agent name)
    agents:by_framework:{framework}        → Set
    agents:by_team:{team}                 → Set
    agents:by_maturity:{maturity}         → Set
    stats:{name}:total                    → Counter
    stats:{name}:success                  → Counter
    stats:{name}:cost                     → Float counter
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import asdict
from pathlib import Path
from typing import AsyncIterator

import redis.asyncio as redis

from ..ports import AgentRegistryPort
from ..types import (
    AgentFramework,
    AgentInvokeRequest,
    AgentInvokeResponse,
    AgentMaturity,
    AgentSpec,
    Skill,
    StreamChunk,
)
from .invokers import FrameworkInvoker, InvokerError, build_default_invokers

logger = logging.getLogger(__name__)


class LocalAgentRegistry(AgentRegistryPort):
    """本地 Agent 注册中心"""

    def __init__(
        self,
        redis_url: str,
        skills_dir: Path | str,
        invokers: dict[AgentFramework, FrameworkInvoker] | None = None,
    ):
        self.redis: redis.Redis = redis.from_url(redis_url, decode_responses=True)
        self.skills_dir = Path(skills_dir)
        self.skills_dir.mkdir(parents=True, exist_ok=True)
        self.invokers = invokers or build_default_invokers()

    # ========================================================
    # 注册管理
    # ========================================================
    async def register(self, spec: AgentSpec) -> None:
        """注册 Agent"""
        spec.updated_at = time.time()
        if not spec.created_at:
            spec.created_at = spec.updated_at

        # 1. 写元数据
        key = f"agent:{spec.name}"
        await self.redis.hset(key, mapping={"spec": json.dumps(self._spec_to_dict(spec))})

        # 2. 索引
        pipe = self.redis.pipeline()
        pipe.sadd("agents:all", spec.name)
        pipe.sadd(f"agents:by_framework:{spec.framework.value}", spec.name)
        pipe.sadd(f"agents:by_maturity:{spec.maturity.value}", spec.name)
        if spec.owner_team:
            pipe.sadd(f"agents:by_team:{spec.owner_team}", spec.name)
        await pipe.execute()

        # 3. SKILL.md 写文件（标准 Anthropic 格式）
        skill_path = self.skills_dir / spec.name / "SKILL.md"
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(self._render_skill_md(spec), encoding="utf-8")

        logger.info(f"Registered agent: {spec.name} ({spec.framework.value})")

    async def update(self, name: str, spec: AgentSpec) -> None:
        """更新（先 deregister 再 register）"""
        old = await self.get(name)
        if old:
            await self.deregister(name)
            # 保留原创建时间
            spec.created_at = old.created_at
        spec.name = name
        await self.register(spec)

    async def deregister(self, name: str) -> None:
        """注销"""
        spec = await self.get(name)
        if not spec:
            return

        pipe = self.redis.pipeline()
        pipe.delete(f"agent:{name}")
        pipe.srem("agents:all", name)
        pipe.srem(f"agents:by_framework:{spec.framework.value}", name)
        pipe.srem(f"agents:by_maturity:{spec.maturity.value}", name)
        if spec.owner_team:
            pipe.srem(f"agents:by_team:{spec.owner_team}", name)
        await pipe.execute()

        logger.info(f"Deregistered agent: {name}")

    # ========================================================
    # 发现
    # ========================================================
    async def list_all(
        self,
        framework: AgentFramework | None = None,
        owner_team: str | None = None,
        maturity: AgentMaturity | None = None,
    ) -> list[AgentSpec]:
        """列表 + 过滤"""
        keys = ["agents:all"]
        if framework:
            keys.append(f"agents:by_framework:{framework.value}")
        if owner_team:
            keys.append(f"agents:by_team:{owner_team}")
        if maturity:
            keys.append(f"agents:by_maturity:{maturity.value}")

        if len(keys) == 1:
            names = await self.redis.smembers(keys[0])
        else:
            names = await self.redis.sinter(*keys)

        if not names:
            return []
        specs = await asyncio.gather(*[self.get(n) for n in names])
        return [s for s in specs if s is not None]

    async def get(self, name: str) -> AgentSpec | None:
        """精确查询"""
        data = await self.redis.hget(f"agent:{name}", "spec")
        if not data:
            return None
        try:
            return self._dict_to_spec(json.loads(data))
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to deserialize agent {name}: {e}")
            return None

    async def discover(
        self,
        query: str,
        top_k: int = 5,
        user_id: str | None = None,
    ) -> list[AgentSpec]:
        """语义检索（关键词匹配 + 触发词加权）"""
        all_agents = await self.list_all()

        # 权限过滤
        if user_id:
            all_agents = [
                a for a in all_agents
                if not a.allowed_users or user_id in a.allowed_users
            ]

        # 评分
        scored: list[tuple[float, AgentSpec]] = []
        query_lower = query.lower()

        for agent in all_agents:
            score = 0.0

            # 描述匹配
            if query_lower in agent.description.lower():
                score += 5
            if query_lower in agent.display_name.lower():
                score += 3

            # 触发词匹配（高权重）
            for trigger in agent.skill.triggers:
                if trigger.lower() in query_lower:
                    score += 10

            # 成熟度加分
            if agent.maturity == AgentMaturity.PRODUCTION:
                score += 3
            elif agent.maturity == AgentMaturity.BETA:
                score += 1
            elif agent.maturity == AgentMaturity.DEPRECATED:
                score -= 100  # 直接排除

            # 历史成功率加分
            score += agent.success_rate * 2

            if score > 0:
                scored.append((score, agent))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [a for _, a in scored[:top_k]]

    # ========================================================
    # 统一调用（核心）
    # ========================================================
    async def invoke(self, req: AgentInvokeRequest) -> AgentInvokeResponse:
        """根据 framework 路由到对应 invoker"""
        spec = await self.get(req.agent_name)
        if not spec:
            return AgentInvokeResponse(
                agent_name=req.agent_name,
                output="",
                error=f"Agent '{req.agent_name}' not found",
            )

        # 权限检查
        if not await self.check_permission(req.agent_name, req.user_id):
            return AgentInvokeResponse(
                agent_name=req.agent_name,
                output="",
                error="Permission denied",
            )

        # 路由到对应 invoker
        invoker = self.invokers.get(spec.framework)
        if not invoker:
            return AgentInvokeResponse(
                agent_name=req.agent_name,
                output="",
                error=f"Framework '{spec.framework.value}' not supported",
            )

        # 调用 + 计时 + 记录
        start = time.time()
        try:
            output = await invoker.invoke(spec, req)
            latency_ms = int((time.time() - start) * 1000)
            await self._record_invocation(spec, latency_ms, success=True)
            return AgentInvokeResponse(
                agent_name=req.agent_name,
                output=output,
                cost=spec.cost_per_call,
                latency_ms=latency_ms,
            )
        except InvokerError as e:
            latency_ms = int((time.time() - start) * 1000)
            await self._record_invocation(spec, latency_ms, success=False)
            logger.error(f"Invoke error for {spec.name}: {e}")
            return AgentInvokeResponse(
                agent_name=req.agent_name,
                output="",
                error=str(e),
                latency_ms=latency_ms,
            )
        except Exception as e:
            latency_ms = int((time.time() - start) * 1000)
            await self._record_invocation(spec, latency_ms, success=False)
            logger.exception(f"Unexpected error invoking {spec.name}")
            return AgentInvokeResponse(
                agent_name=req.agent_name,
                output="",
                error=f"Unexpected error: {e}",
                latency_ms=latency_ms,
            )

    async def stream_invoke(
        self, req: AgentInvokeRequest
    ) -> AsyncIterator[StreamChunk]:
        """流式调用"""
        spec = await self.get(req.agent_name)
        if not spec:
            yield StreamChunk(delta=f"Agent '{req.agent_name}' not found", is_last=True)
            return

        invoker = self.invokers.get(spec.framework)
        if not invoker:
            yield StreamChunk(
                delta=f"Framework '{spec.framework.value}' not supported",
                is_last=True,
            )
            return

        async for chunk in invoker.stream_invoke(spec, req):
            yield chunk

    # ========================================================
    # 治理
    # ========================================================
    async def check_permission(self, agent_name: str, user_id: str) -> bool:
        """权限检查"""
        spec = await self.get(agent_name)
        if not spec:
            return False
        # 没设置访问限制 = 允许所有人
        if not spec.allowed_users and not spec.allowed_teams:
            return True
        # 用户白名单
        if user_id in spec.allowed_users:
            return True
        # 团队白名单（需要外部用户→团队映射，这里留扩展点）
        # TODO: 接入飞书部门信息
        return False

    async def get_usage_stats(self, agent_name: str | None = None) -> dict:
        """从 Redis 读取统计"""
        if agent_name:
            total = await self.redis.get(f"stats:{agent_name}:total") or "0"
            success = await self.redis.get(f"stats:{agent_name}:success") or "0"
            cost = await self.redis.get(f"stats:{agent_name}:cost") or "0"
            return {
                "agent_name": agent_name,
                "total_calls": int(total),
                "success_calls": int(success),
                "total_cost": float(cost),
                "success_rate": int(success) / int(total) if int(total) > 0 else 0,
            }
        # 全局
        agents = await self.list_all()
        results = await asyncio.gather(*[self.get_usage_stats(a.name) for a in agents])
        return {a.name: r for a, r in zip(agents, results)}

    # ========================================================
    # 内部辅助
    # ========================================================
    async def _record_invocation(
        self, spec: AgentSpec, latency_ms: int, success: bool
    ) -> None:
        """记录调用统计"""
        pipe = self.redis.pipeline()
        pipe.incr(f"stats:{spec.name}:total")
        if success:
            pipe.incr(f"stats:{spec.name}:success")
        pipe.incrbyfloat(f"stats:{spec.name}:cost", spec.cost_per_call)
        await pipe.execute()

    def _spec_to_dict(self, spec: AgentSpec) -> dict:
        """dataclass → dict（处理枚举）"""
        d = asdict(spec)
        d["framework"] = spec.framework.value
        d["maturity"] = spec.maturity.value
        return d

    def _dict_to_spec(self, d: dict) -> AgentSpec:
        """dict → dataclass"""
        d = dict(d)  # copy
        d["framework"] = AgentFramework(d["framework"])
        d["maturity"] = AgentMaturity(d["maturity"])
        # skill 嵌套
        if isinstance(d.get("skill"), dict):
            d["skill"] = Skill(**d["skill"])
        return AgentSpec(**d)

    def _render_skill_md(self, spec: AgentSpec) -> str:
        """渲染标准 SKILL.md（Anthropic 标准）"""
        triggers_str = ", ".join(spec.skill.triggers) if spec.skill.triggers else ""
        return f"""---
name: {spec.name}
description: {spec.description}
triggers: [{triggers_str}]
framework: {spec.framework.value}
owner_team: {spec.owner_team}
maturity: {spec.maturity.value}
---

# {spec.display_name}

{spec.skill.instructions or spec.description}
"""

    async def close(self) -> None:
        """关闭 Redis 连接"""
        await self.redis.aclose()
