from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl

router = APIRouter(prefix="/ingest", tags=["ingest"])


class IngestRequest(BaseModel):
    url: HttpUrl
    data_lineage: str = "manual"  # poc_crawled / oauth / public_api / manual


class IngestResponse(BaseModel):
    workflow_id: str
    case_id: str | None = None


@router.post("", response_model=IngestResponse, status_code=202)
async def ingest_case(req: IngestRequest) -> IngestResponse:
    """触发 AgenticInsight workflow（Temporal）。W1 实装。"""
    raise HTTPException(status_code=501, detail="Not implemented — W1 deliverable")
