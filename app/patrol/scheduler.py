"""Patrol scheduler: manages periodic execution of patrol tasks."""

from __future__ import annotations

import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.config import settings
from app.patrol.base import BasePatrolTask
from app.patrol.notifier import PatrolNotifier

logger = logging.getLogger(__name__)


class PatrolScheduler:
    """Manages registration and scheduled execution of patrol tasks.

    Uses APScheduler with cron triggers for flexible scheduling.
    """

    def __init__(self, notifier: PatrolNotifier) -> None:
        self.notifier = notifier
        self._tasks: dict[str, BasePatrolTask] = {}
        self._scheduler = AsyncIOScheduler(timezone=settings.patrol_timezone)

    def register(self, task: BasePatrolTask) -> None:
        """Register a patrol task with its configured schedule."""
        config = task.config()
        self._tasks[config.task_id] = task

        if config.enabled and settings.patrol_enabled:
            self._scheduler.add_job(
                self._run_task,
                trigger=CronTrigger.from_crontab(config.cron),
                args=[config.task_id],
                id=config.task_id,
                name=config.name,
                replace_existing=True,
            )
            logger.info("Patrol task registered: %s (cron: %s)", config.name, config.cron)
        else:
            logger.info("Patrol task registered (disabled): %s", config.name)

    async def _run_task(self, task_id: str) -> None:
        """Execute a patrol task and handle notification."""
        task = self._tasks.get(task_id)
        if not task:
            logger.error("Patrol task %s not found", task_id)
            return

        config = task.config()
        logger.info("Running patrol task: %s", config.name)

        try:
            result = await task.execute()
            logger.info(
                "Patrol task %s completed: %s — %s",
                config.name,
                result.alert_level,
                result.title,
            )
            await self.notifier.notify(result)
        except Exception as e:
            logger.error("Patrol task %s failed: %s", config.name, e, exc_info=True)

    def start(self) -> None:
        """Start the patrol scheduler."""
        if settings.patrol_enabled:
            self._scheduler.start()
            logger.info("Patrol scheduler started with %d tasks", len(self._tasks))
        else:
            logger.info("Patrol scheduler disabled by config")

    def stop(self) -> None:
        """Stop the patrol scheduler."""
        if self._scheduler.running:
            self._scheduler.shutdown(wait=False)
            logger.info("Patrol scheduler stopped")

    async def run_now(self, task_id: str) -> dict:
        """Manually trigger a patrol task (for testing / ad-hoc runs)."""
        task = self._tasks.get(task_id)
        if not task:
            return {"error": f"Task {task_id} not found"}

        result = await task.execute()
        await self.notifier.notify(result)
        return result.model_dump()

    def list_tasks(self) -> list[dict]:
        """List all registered patrol tasks."""
        return [
            {
                "task_id": tid,
                "name": task.config().name,
                "cron": task.config().cron,
                "enabled": task.config().enabled,
            }
            for tid, task in self._tasks.items()
        ]
