from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/generate", tags=["generate"])


class GenerateRequest(BaseModel):
    microtype_id: str
    atom_ids: list[str]
    n: int = 5


@router.post("")
async def generate_scripts(req: GenerateRequest) -> dict:
    raise HTTPException(status_code=501, detail="Not implemented — W3 deliverable")
