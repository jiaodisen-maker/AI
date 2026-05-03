"""
Redis 经验引擎 v1（基于 Redis）

设计：
- Pattern：每个 Skill 一个 List，存最近 N 条 (input, output) 对
- Knowledge：每个 namespace 一个 List，存知识条目
- 检索：简单关键词 + 倒序最近优先（生产可换 embedding + 向量检索）

Redis Keys:
  exp:patterns:{skill}     → List [json_pattern, ...]
  exp:knowledge:{ns}       → List [json_knowledge, ...]
"""
from __future__ import annotations

import json
import logging
import time
import uuid

import redis.asyncio as redis

from ..ports import MemoryPort

logger = logging.getLogger(__name__)

DEFAULT_MAX_PATTERNS = 1000  # 每 skill 最多保留 1000 条 pattern
DEFAULT_MAX_KNOWLEDGE = 5000


class RedisMemoryAdapter(MemoryPort):
    """生产级经验引擎"""

    def __init__(
        self,
        redis_url: str,
        max_patterns: int = DEFAULT_MAX_PATTERNS,
        max_knowledge: int = DEFAULT_MAX_KNOWLEDGE,
    ):
        self.redis: redis.Redis = redis.from_url(redis_url, decode_responses=True)
        self.max_patterns = max_patterns
        self.max_knowledge = max_knowledge

    # ========================================================
    # Pattern（执行经验）
    # ========================================================
    async def store_pattern(
        self,
        skill_name: str,
        input_text: str,
        output_text: str,
        feedback: dict | None = None,
    ) -> str:
        pattern_id = f"pat_{uuid.uuid4().hex[:12]}"
        record = {
            "id": pattern_id,
            "skill_name": skill_name,
            "input": input_text,
            "output": output_text,
            "feedback": feedback or {},
            "timestamp": time.time(),
        }
        key = f"exp:patterns:{skill_name}"
        pipe = self.redis.pipeline()
        pipe.rpush(key, json.dumps(record, ensure_ascii=False))
        pipe.ltrim(key, -self.max_patterns, -1)
        await pipe.execute()
        return pattern_id

    async def retrieve_patterns(
        self, skill_name: str, query: str, top_k: int = 3
    ) -> list[dict]:
        """简单关键词匹配（生产可换向量检索）"""
        key = f"exp:patterns:{skill_name}"
        # 拉最近 N 条候选
        candidates_raw = await self.redis.lrange(key, -200, -1)

        query_words = set(self._tokenize(query))
        if not query_words:
            return []

        scored: list[tuple[float, dict]] = []
        for raw in candidates_raw:
            try:
                p = json.loads(raw)
            except json.JSONDecodeError:
                continue

            input_words = set(self._tokenize(p.get("input", "")))
            if not input_words:
                continue

            # Jaccard 相似度
            overlap = len(query_words & input_words)
            union = len(query_words | input_words)
            score = overlap / union if union else 0

            # 加分：人工反馈正向
            feedback = p.get("feedback") or {}
            if feedback.get("rating", 0) >= 4:
                score += 0.2

            if score > 0.1:  # 最低阈值
                scored.append((score, p))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [p for _, p in scored[:top_k]]

    # ========================================================
    # Knowledge（行业本体）
    # ========================================================
    async def store_knowledge(
        self, namespace: str, content: str, metadata: dict
    ) -> str:
        kid = f"kn_{uuid.uuid4().hex[:12]}"
        record = {
            "id": kid,
            "namespace": namespace,
            "content": content,
            "metadata": metadata or {},
            "timestamp": time.time(),
        }
        key = f"exp:knowledge:{namespace}"
        pipe = self.redis.pipeline()
        pipe.rpush(key, json.dumps(record, ensure_ascii=False))
        pipe.ltrim(key, -self.max_knowledge, -1)
        await pipe.execute()
        return kid

    async def retrieve_knowledge(
        self, namespace: str, query: str, top_k: int = 5
    ) -> list[dict]:
        key = f"exp:knowledge:{namespace}"
        candidates_raw = await self.redis.lrange(key, -500, -1)

        query_words = set(self._tokenize(query))
        if not query_words:
            return []

        scored: list[tuple[float, dict]] = []
        for raw in candidates_raw:
            try:
                k = json.loads(raw)
            except json.JSONDecodeError:
                continue

            content_words = set(self._tokenize(k.get("content", "")))
            if not content_words:
                continue

            overlap = len(query_words & content_words)
            if overlap > 0:
                scored.append((overlap, k))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [k for _, k in scored[:top_k]]

    # ========================================================
    # 关闭
    # ========================================================
    async def close(self) -> None:
        await self.redis.aclose()

    # ========================================================
    # 内部
    # ========================================================
    @staticmethod
    def _tokenize(text: str) -> list[str]:
        """简单分词（中英文）。生产可用 jieba。"""
        if not text:
            return []
        # 中文按字 + 英文按词
        tokens = []
        en_buf = ""
        for ch in text.lower():
            if ch.isascii() and (ch.isalnum() or ch in "_"):
                en_buf += ch
            else:
                if en_buf:
                    tokens.append(en_buf)
                    en_buf = ""
                if not ch.isspace() and not ch.isascii():
                    tokens.append(ch)  # 中文字
        if en_buf:
            tokens.append(en_buf)
        return tokens
