"""
生产级 Redis Session Adapter

设计：
- 用户级会话隔离（session_id 通常 = user_id）
- 消息追加用 Redis List（O(1) 追加，O(n) 范围查询）
- 元数据用 Redis Hash
- 自动 TTL（默认 7 天）
- 历史长度限制（防止无限增长）

Redis Keys:
  session:meta:{session_id}      → Hash {user_id, created_at, updated_at, metadata_json}
  session:msgs:{session_id}      → List [json_msg, json_msg, ...]
"""
from __future__ import annotations

import json
import logging
import time
from dataclasses import asdict

import redis.asyncio as redis

from ..ports import SessionPort
from ..types import Message, Role, SessionState

logger = logging.getLogger(__name__)


# 默认配置
DEFAULT_TTL_SECONDS = 7 * 24 * 3600   # 7 天
DEFAULT_MAX_MESSAGES = 100             # 单 session 最多保留 100 条消息


class RedisSessionAdapter(SessionPort):
    """生产级 Redis 实现 - 用户级会话隔离"""

    def __init__(
        self,
        redis_url: str,
        ttl_seconds: int = DEFAULT_TTL_SECONDS,
        max_messages: int = DEFAULT_MAX_MESSAGES,
        key_prefix: str = "session",
    ):
        self.redis: redis.Redis = redis.from_url(redis_url, decode_responses=True)
        self.ttl = ttl_seconds
        self.max_messages = max_messages
        self.prefix = key_prefix

    # ========================================================
    # Key 命名约定
    # ========================================================
    def _meta_key(self, session_id: str) -> str:
        return f"{self.prefix}:meta:{session_id}"

    def _msgs_key(self, session_id: str) -> str:
        return f"{self.prefix}:msgs:{session_id}"

    # ========================================================
    # Session 生命周期
    # ========================================================
    async def get_or_create(self, session_id: str, user_id: str) -> SessionState:
        """获取或创建会话"""
        meta_key = self._meta_key(session_id)
        meta = await self.redis.hgetall(meta_key)

        now = time.time()
        if not meta:
            # 创建新会话
            meta = {
                "user_id": user_id,
                "created_at": str(now),
                "updated_at": str(now),
                "metadata": "{}",
            }
            pipe = self.redis.pipeline()
            pipe.hset(meta_key, mapping=meta)
            pipe.expire(meta_key, self.ttl)
            await pipe.execute()
            logger.debug(f"Created new session: {session_id}")

        # 拉历史消息
        messages = await self.get_history(session_id, limit=self.max_messages)

        # 解析元数据
        try:
            metadata = json.loads(meta.get("metadata", "{}"))
        except json.JSONDecodeError:
            metadata = {}

        return SessionState(
            session_id=session_id,
            user_id=meta.get("user_id", user_id),
            messages=messages,
            metadata=metadata,
            created_at=float(meta.get("created_at", now)),
            updated_at=float(meta.get("updated_at", now)),
        )

    async def append_message(self, session_id: str, msg: Message) -> None:
        """追加消息（自动滚动 + 续期）"""
        msgs_key = self._msgs_key(session_id)
        meta_key = self._meta_key(session_id)

        # 序列化
        msg_json = self._msg_to_json(msg)

        pipe = self.redis.pipeline()
        # 追加
        pipe.rpush(msgs_key, msg_json)
        # 截断（保留最近 max_messages 条）
        pipe.ltrim(msgs_key, -self.max_messages, -1)
        # 续期 TTL
        pipe.expire(msgs_key, self.ttl)
        # 更新最后活跃时间
        pipe.hset(meta_key, "updated_at", str(time.time()))
        pipe.expire(meta_key, self.ttl)
        await pipe.execute()

    async def get_history(self, session_id: str, limit: int = 20) -> list[Message]:
        """获取历史（最近 limit 条）"""
        msgs_key = self._msgs_key(session_id)
        # LRANGE -limit -1 拿最后 limit 条
        raw_msgs = await self.redis.lrange(msgs_key, -limit, -1)

        messages = []
        for raw in raw_msgs:
            try:
                msg = self._msg_from_json(raw)
                messages.append(msg)
            except Exception as e:
                logger.warning(f"Skip bad message in {session_id}: {e}")
        return messages

    async def save(self, session: SessionState) -> None:
        """整体保存（重建 session）"""
        meta_key = self._meta_key(session.session_id)
        msgs_key = self._msgs_key(session.session_id)

        pipe = self.redis.pipeline()
        # 元数据
        pipe.hset(meta_key, mapping={
            "user_id": session.user_id,
            "created_at": str(session.created_at),
            "updated_at": str(time.time()),
            "metadata": json.dumps(session.metadata),
        })
        pipe.expire(meta_key, self.ttl)

        # 消息（先清空再追加）
        pipe.delete(msgs_key)
        if session.messages:
            for msg in session.messages[-self.max_messages:]:
                pipe.rpush(msgs_key, self._msg_to_json(msg))
            pipe.expire(msgs_key, self.ttl)

        await pipe.execute()

    async def clear(self, session_id: str) -> None:
        """清空 session（用户主动清除）"""
        pipe = self.redis.pipeline()
        pipe.delete(self._meta_key(session_id))
        pipe.delete(self._msgs_key(session_id))
        await pipe.execute()
        logger.info(f"Cleared session: {session_id}")

    # ========================================================
    # 关闭
    # ========================================================
    async def close(self) -> None:
        await self.redis.aclose()

    # ========================================================
    # 序列化辅助
    # ========================================================
    def _msg_to_json(self, msg: Message) -> str:
        d = asdict(msg)
        d["role"] = msg.role.value  # 枚举 → string
        # tool_calls 字段是 dataclass list，asdict 会自动转成 dict list
        return json.dumps(d, ensure_ascii=False)

    def _msg_from_json(self, raw: str) -> Message:
        d = json.loads(raw)
        d["role"] = Role(d["role"])
        # tool_calls 暂时简化处理（生产可以反序列化为 ToolCall）
        d.pop("tool_calls", None)
        return Message(
            role=d["role"],
            content=d["content"],
            metadata=d.get("metadata", {}),
        )
