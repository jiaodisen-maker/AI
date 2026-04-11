"""Patrol system API: view tasks, trigger manual runs, check history."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/patrol", tags=["patrol"])


@router.get("/tasks")
async def list_patrol_tasks():
    """List all registered patrol tasks."""
    from app.main import get_app_state

    state = get_app_state()
    return {"tasks": state.patrol_scheduler.list_tasks()}


@router.post("/tasks/{task_id}/run")
async def run_patrol_task(task_id: str):
    """Manually trigger a patrol task."""
    from app.main import get_app_state

    state = get_app_state()
    result = await state.patrol_scheduler.run_now(task_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result
