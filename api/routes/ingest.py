"""POST /ingest — 触发 AgenticInsight workflow."""
import uuid
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl

from ..config import get_settings
from ..temporal_client import get_temporal_client

router = APIRouter(prefix="/ingest", tags=["ingest"])

DataLineage = Literal["poc_crawled", "oauth", "public_api", "manual"]


class ManualPayload(BaseModel):
    """旁路媒体管道：调用方直接传预提取好的多模态文本。"""

    asr_text: str | None = None
    ocr_text: str | None = None
    visual_desc: str | None = None
    duration_sec: float | None = None


class IngestRequest(BaseModel):
    url: HttpUrl
    data_lineage: DataLineage = "manual"
    platform: str | None = None
    brand: str | None = None
    sku: str | None = None
    category: str | None = None
    manual_payload: ManualPayload | None = None


class IngestResponse(BaseModel):
    workflow_id: str


@router.post("", response_model=IngestResponse, status_code=202)
async def ingest_case(req: IngestRequest) -> IngestResponse:
    settings = get_settings()
    if req.data_lineage == "poc_crawled" and not settings.poc_crawled_enabled:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=403,
            detail="POC_CRAWLED_ENABLED is false (production mode); poc_crawled lineage rejected.",
        )

    client = await get_temporal_client()
    workflow_id = f"agentic-insight-{uuid.uuid4()}"

    payload = req.model_dump(mode="json")
    payload["url"] = str(req.url)
    payload["trigger"] = "manual"

    await client.start_workflow(
        "AgenticInsightWorkflow",
        payload,
        id=workflow_id,
        task_queue=settings.temporal_task_queue,
    )

    return IngestResponse(workflow_id=workflow_id)
