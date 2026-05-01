from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/microtypes", tags=["microtypes"])


@router.get("")
async def list_microtypes(status: str | None = None) -> list[dict]:
    raise HTTPException(status_code=501, detail="Not implemented — W2 deliverable")
