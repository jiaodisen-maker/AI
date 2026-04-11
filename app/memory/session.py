"""Redis-backed session memory for multi-turn conversations.

Stores conversation history per session_id, enabling the agent
to remember what was said earlier in the same conversation.
"""

from __future__ import annotations

import json
import logging
from typing import Any

logger = logging.getLogger(__name__)

# Max messages to keep per session
MAX_HISTORY_LENGTH = 50
# Session TTL in seconds (2 hours)
SESSION_TTL = 7200


class SessionMemory:
    """Multi-turn conversation memory backed by Redis.

    Each session_id maps to a list of message dicts:
    [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
    """

    def __init__(self, redis_client: Any = None) -> None:
        self._redis = redis_client
        self._local: dict[str, list[dict]] = {}  # Fallback in-memory

    def _key(self, session_id: str) -> str:
        return f"session:{session_id}:history"

    async def add_message(
        self, session_id: str, role: str, content: str
    ) -> None:
        """Add a message to session history."""
        msg = {"role": role, "content": content}

        if self._redis:
            key = self._key(session_id)
            await self._redis.rpush(key, json.dumps(msg, ensure_ascii=False))
            await self._redis.ltrim(key, -MAX_HISTORY_LENGTH, -1)
            await self._redis.expire(key, SESSION_TTL)
        else:
            if session_id not in self._local:
                self._local[session_id] = []
            self._local[session_id].append(msg)
            self._local[session_id] = self._local[session_id][
                -MAX_HISTORY_LENGTH:
            ]

    async def get_history(self, session_id: str) -> list[dict[str, str]]:
        """Get conversation history for a session."""
        if self._redis:
            key = self._key(session_id)
            raw = await self._redis.lrange(key, 0, -1)
            return [json.loads(m) for m in raw]
        else:
            return list(self._local.get(session_id, []))

    async def clear_session(self, session_id: str) -> None:
        """Clear a session's history."""
        if self._redis:
            await self._redis.delete(self._key(session_id))
        else:
            self._local.pop(session_id, None)
