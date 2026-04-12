"""A2A (Agent-to-Agent) Protocol implementation.

Implements the A2A protocol so external agents can discover and call
this AI middleware as if it were a peer agent.

A2A specification:
  - Agent Card at /.well-known/agent-card.json
  - Task lifecycle: submitted → working → completed
  - JSON-RPC 2.0 over HTTP
"""

from __future__ import annotations

import logging
import uuid
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

logger = logging.getLogger(__name__)

router = APIRouter(tags=["a2a"])


# ============================================================
# Agent Card
# ============================================================


@router.get("/.well-known/agent-card.json")
async def agent_card() -> dict[str, Any]:
    """Return the A2A agent card describing this agent's capabilities."""
    from app.main import get_app_state

    state = get_app_state()
    skills = []
    if state.skill_registry:
        for meta in state.skill_registry.list_all():
            skills.append({
                "id": meta.id,
                "name": meta.name,
                "description": meta.description,
                "input": {"type": "string"},
                "output": {"type": "string"},
            })

    return {
        "name": "ai-zhongtai",
        "description": "保健品行业自进化 AI 中台 — Skills 中心架构",
        "version": "0.1.0",
        "url": "/api/a2a",
        "capabilities": {
            "streaming": False,
            "push_notifications": False,
        },
        "skills": skills,
        "authentication": {
            "schemes": ["bearer"],
        },
    }


# ============================================================
# Task lifecycle
# ============================================================

_tasks: dict[str, dict[str, Any]] = {}


class TaskRequest(BaseModel):
    skill_id: str
    input: dict[str, Any] = {}


class TaskResponse(BaseModel):
    task_id: str
    status: str
    output: Any = None
    error: str | None = None


@router.post("/api/a2a/tasks")
async def create_task(req: TaskRequest) -> TaskResponse:
    """A2A: Create a task to execute a skill."""
    from app.main import get_app_state
    from app.skills.models import SkillInput

    task_id = uuid.uuid4().hex
    state = get_app_state()
    skill = state.skill_registry.get(req.skill_id) if state.skill_registry else None

    if not skill:
        _tasks[task_id] = {
            "status": "failed",
            "error": f"Skill '{req.skill_id}' not found",
        }
        return TaskResponse(
            task_id=task_id, status="failed", error=f"Skill '{req.skill_id}' not found"
        )

    _tasks[task_id] = {"status": "working"}

    # Run skill (simplified: synchronous, real A2A would be async with polling)
    skill_input = SkillInput(
        user_message=req.input.get("message", ""),
        parameters=req.input,
    )

    try:
        record = await skill.run(skill_input)
        if record.output.success:
            _tasks[task_id] = {
                "status": "completed",
                "output": record.output.content,
            }
            return TaskResponse(
                task_id=task_id, status="completed", output=record.output.content
            )
        else:
            _tasks[task_id] = {"status": "failed", "error": record.output.error}
            return TaskResponse(
                task_id=task_id, status="failed", error=record.output.error
            )
    except Exception as e:
        _tasks[task_id] = {"status": "failed", "error": str(e)}
        return TaskResponse(task_id=task_id, status="failed", error=str(e))


@router.get("/api/a2a/tasks/{task_id}")
async def get_task(task_id: str) -> TaskResponse:
    """A2A: Get task status (polling)."""
    task = _tasks.get(task_id)
    if not task:
        return TaskResponse(task_id=task_id, status="not_found")
    return TaskResponse(task_id=task_id, **task)
