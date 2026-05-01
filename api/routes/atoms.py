from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/atoms", tags=["atoms"])


@router.get("")
async def search_atoms(q: str | None = None, atom_type: str | None = None) -> list[dict]:
    raise HTTPException(status_code=501, detail="Not implemented — W2 deliverable")
