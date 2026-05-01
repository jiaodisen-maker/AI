from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("")
async def list_alerts(status: str = "open") -> list[dict]:
    raise HTTPException(status_code=501, detail="Not implemented — W2 deliverable")


@router.post("/{alert_id}/resolve")
async def resolve_alert(alert_id: str, resolved_by: str) -> dict:
    raise HTTPException(status_code=501, detail="Not implemented — W2 deliverable")
