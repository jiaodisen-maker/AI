"""Experience store: persistence layer for experience records and patterns."""

from __future__ import annotations

import logging
import uuid
from datetime import datetime

from app.experience.models import ExperiencePattern, ExperienceRecord

logger = logging.getLogger(__name__)


class ExperienceStore:
    """In-memory experience store with optional Redis persistence.

    Stores:
    - ExperienceRecords: raw execution history with human corrections
    - ExperiencePatterns: extracted, evolving patterns with confidence scores
    """

    def __init__(self) -> None:
        self._records: list[ExperienceRecord] = []
        self._patterns: dict[str, ExperiencePattern] = {}  # id → pattern
        self._redis = None

    async def init_redis(self, redis_url: str) -> None:
        """Initialize Redis connection for persistence."""
        try:
            import redis.asyncio as aioredis

            self._redis = aioredis.from_url(redis_url, decode_responses=True)
            await self._load_from_redis()
            logger.info("Experience store connected to Redis")
        except Exception as e:
            logger.warning("Redis not available, using in-memory store only: %s", e)
            self._redis = None

    # --- Records ---

    async def add_record(self, record: ExperienceRecord) -> str:
        """Store an execution record (memory + Redis + DB)."""
        if not record.id:
            record.id = uuid.uuid4().hex

        # In-memory (capped to prevent leak)
        self._records.append(record)
        if len(self._records) > 10000:
            self._records = self._records[-5000:]

        # Redis
        if self._redis:
            await self._redis.lpush(
                f"exp:records:{record.skill_id}",
                record.model_dump_json(),
            )
            # Cap Redis list too
            await self._redis.ltrim(f"exp:records:{record.skill_id}", 0, 9999)

        # DB persistence (best effort)
        try:
            await self._persist_record_to_db(record)
        except Exception as e:
            logger.warning("DB persist failed (non-fatal): %s", e)

        return record.id

    async def _persist_record_to_db(self, record: ExperienceRecord) -> None:
        """Persist record to SQLAlchemy database."""
        try:
            from app.data.database import DatabaseManager
            from app.data.models import SkillExecutionLog

            db = DatabaseManager()
            async with db.session() as session:
                log = SkillExecutionLog(
                    id=record.id,
                    skill_id=record.skill_id,
                    input_message=record.input_context.get("user_message", ""),
                    input_parameters=record.input_context,
                    output_content=record.ai_output,
                    human_edited_output=record.human_edited_output,
                    model_used=record.model_used,
                )
                session.add(log)
        except ImportError:
            pass  # DB module not available

    def get_records(self, skill_id: str, limit: int = 50) -> list[ExperienceRecord]:
        """Get recent execution records for a skill."""
        records = [r for r in self._records if r.skill_id == skill_id]
        return sorted(records, key=lambda r: r.created_at, reverse=True)[:limit]

    def get_edited_records(self, skill_id: str, limit: int = 50) -> list[ExperienceRecord]:
        """Get records where human made corrections."""
        records = [r for r in self._records if r.skill_id == skill_id and r.was_edited]
        return sorted(records, key=lambda r: r.created_at, reverse=True)[:limit]

    # --- Patterns ---

    async def add_pattern(self, pattern: ExperiencePattern) -> str:
        """Store a new learned pattern."""
        if not pattern.id:
            pattern.id = uuid.uuid4().hex
        self._patterns[pattern.id] = pattern

        if self._redis:
            await self._redis.hset(
                f"exp:patterns:{pattern.skill_id}",
                pattern.id,
                pattern.model_dump_json(),
            )

        logger.info(
            "New pattern for %s: %s (confidence=%.2f)",
            pattern.skill_id,
            pattern.pattern[:50],
            pattern.confidence,
        )
        return pattern.id

    async def update_pattern(self, pattern: ExperiencePattern) -> None:
        """Update an existing pattern (confidence, usage count, etc.)."""
        pattern.updated_at = datetime.now()
        self._patterns[pattern.id] = pattern

        if self._redis:
            await self._redis.hset(
                f"exp:patterns:{pattern.skill_id}",
                pattern.id,
                pattern.model_dump_json(),
            )

    def get_reliable_patterns(self, skill_id: str) -> list[ExperiencePattern]:
        """Get patterns with confidence >= 0.7 for auto-injection."""
        return [
            p
            for p in self._patterns.values()
            if p.skill_id == skill_id and p.is_reliable
        ]

    def get_all_patterns(self, skill_id: str) -> list[ExperiencePattern]:
        """Get all active patterns for a skill."""
        return [
            p
            for p in self._patterns.values()
            if p.skill_id == skill_id and not p.should_archive
        ]

    async def confirm_pattern(self, pattern_id: str) -> None:
        """Confirm a pattern was useful — increase confidence."""
        pattern = self._patterns.get(pattern_id)
        if pattern:
            pattern.usage_count += 1
            pattern.confidence = min(1.0, pattern.confidence + 0.1)
            await self.update_pattern(pattern)

    async def reject_pattern(self, pattern_id: str) -> None:
        """Reject a pattern — decrease confidence."""
        pattern = self._patterns.get(pattern_id)
        if pattern:
            pattern.confidence = max(0.0, pattern.confidence - 0.2)
            await self.update_pattern(pattern)
            if pattern.should_archive:
                logger.info("Pattern %s archived (confidence too low)", pattern_id)

    # --- Persistence ---

    async def _load_from_redis(self) -> None:
        """Load patterns from Redis on startup."""
        if not self._redis:
            return

        cursor = "0"
        while True:
            cursor, keys = await self._redis.scan(cursor=cursor, match="exp:patterns:*", count=100)
            for key in keys:
                entries = await self._redis.hgetall(key)
                for pattern_json in entries.values():
                    try:
                        pattern = ExperiencePattern.model_validate_json(pattern_json)
                        self._patterns[pattern.id] = pattern
                    except Exception as e:
                        logger.warning("Failed to load pattern: %s", e)
            if cursor == "0":
                break

        logger.info("Loaded %d experience patterns from Redis", len(self._patterns))
