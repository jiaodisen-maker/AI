from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/cases", tags=["cases"])


@router.get("/{case_id}")
async def get_case(case_id: str) -> dict:
    raise HTTPException(status_code=501, detail="Not implemented — W1 deliverable")


@router.get("")
async def list_cases() -> list[dict]:
    raise HTTPException(status_code=501, detail="Not implemented — W1 deliverable")
