"""POST /discovery/run — admin 触发批量发现 + 起 workflow。

权限：W3 阶段无认证；生产部署应加 internal-only 网络隔离 + 简单 token 校验。
"""
import uuid
from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..config import get_settings
from ..temporal_client import get_temporal_client

router = APIRouter(prefix="/discovery", tags=["discovery"])


class DiscoveryRequest(BaseModel):
    channel: Literal["poc", "prod"]
    query: str
    n: int = 5


class DiscoveryResponse(BaseModel):
    discovered: int
    started_workflows: list[dict]


@router.post("/run", response_model=DiscoveryResponse, status_code=202)
async def run_discovery(req: DiscoveryRequest) -> DiscoveryResponse:
    settings = get_settings()

    if req.channel == "poc" and not settings.poc_crawled_enabled:
        raise HTTPException(
            403,
            "POC_CRAWLED_ENABLED is false; PoC discovery channel disabled in this env.",
        )

    from worker.discovery import discover

    try:
        cases = discover(req.channel, req.query, req.n)
    except PermissionError as e:
        raise HTTPException(403, str(e)) from e
    except ValueError as e:
        raise HTTPException(400, str(e)) from e

    if not cases:
        return DiscoveryResponse(discovered=0, started_workflows=[])

    client = await get_temporal_client()
    started: list[dict] = []
    for c in cases:
        wf_id = f"agentic-insight-{uuid.uuid4()}"
        payload = dict(c)
        payload["trigger"] = "auto"
        await client.start_workflow(
            "AgenticInsightWorkflow",
            payload,
            id=wf_id,
            task_queue=settings.temporal_task_queue,
        )
        started.append({"workflow_id": wf_id, "url": c["url"]})

    return DiscoveryResponse(discovered=len(cases), started_workflows=started)
