"""Celery app for distributed patrol task scheduling.

Replaces in-process APScheduler with Celery + Redis broker.
Benefits:
  - Scheduled tasks survive process restart
  - Distributed across multiple workers
  - Built-in retry and dead letter queue
  - Beat scheduler for cron-style triggers

Usage:
  Worker:    celery -A app.patrol.celery_app worker --loglevel=info
  Beat:      celery -A app.patrol.celery_app beat --loglevel=info
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

# Lazy import to avoid hard dependency on celery
_celery_app = None


def get_celery_app():
    """Get or create the Celery app instance."""
    global _celery_app
    if _celery_app is not None:
        return _celery_app

    try:
        from celery import Celery
        from celery.schedules import crontab

        from app.config import settings

        app = Celery(
            "ai_zhongtai",
            broker=settings.redis_url,
            backend=settings.redis_url,
        )

        app.conf.update(
            timezone=settings.patrol_timezone,
            enable_utc=False,
            task_serializer="json",
            accept_content=["json"],
            result_serializer="json",
            task_track_started=True,
            task_acks_late=True,
            worker_prefetch_multiplier=4,
            task_default_retry_delay=60,
            task_max_retries=3,
        )

        # Register patrol tasks via Beat schedule
        app.conf.beat_schedule = {
            "channel-data-scan": {
                "task": "app.patrol.tasks.run_channel_scan",
                "schedule": crontab(hour=8, minute=0),
            },
            "competitor-watch": {
                "task": "app.patrol.tasks.run_competitor_watch",
                "schedule": crontab(hour=10, minute=0),
            },
            "compliance-scan": {
                "task": "app.patrol.tasks.run_compliance_scan",
                "schedule": crontab(minute="*/30"),
            },
        }

        _celery_app = app
        logger.info("Celery app initialized with Redis broker")
        return app
    except ImportError:
        logger.info("Celery not installed, using APScheduler")
        return None
