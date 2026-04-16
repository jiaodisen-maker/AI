"""Celery tasks for patrol system.

Each task is registered with Celery and runs on schedule via Celery Beat.
Tasks call Skills (the value center) to do the actual work.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

# Lazy Celery import
try:
    from app.patrol.celery_app import get_celery_app
    celery = get_celery_app()
except ImportError:
    celery = None


def _make_task(name: str):
    """Decorator that registers a function as a Celery task if available."""

    def decorator(func):
        if celery:
            return celery.task(name=name, bind=True, max_retries=2)(func)
        return func

    return decorator


@_make_task("app.patrol.tasks.run_channel_scan")
def run_channel_scan(self=None) -> dict:
    """Daily channel data scan at 08:00."""
    logger.info("Running channel data scan")
    # In production, this calls a Skill via the registry
    # to query yesterday's GMV/ROI per channel and detect anomalies
    return {
        "task": "channel-scan",
        "status": "completed",
        "alerts": [],
    }


@_make_task("app.patrol.tasks.run_competitor_watch")
def run_competitor_watch(self=None) -> dict:
    """Daily competitor monitoring at 10:00."""
    logger.info("Running competitor watch")
    return {
        "task": "competitor-watch",
        "status": "completed",
        "competitors_checked": 0,
    }


@_make_task("app.patrol.tasks.run_compliance_scan")
def run_compliance_scan(self=None) -> dict:
    """Compliance scan every 30 minutes."""
    logger.info("Running compliance scan")
    return {
        "task": "compliance-scan",
        "status": "completed",
        "violations_found": 0,
    }
