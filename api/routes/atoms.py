from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(prefix="/atoms", tags=["atoms"])


@router.get("")
def search_atoms(
    q: str | None = Query(default=None, description="文本子串搜索"),
    atom_type: str | None = Query(default=None, pattern="^(hook|pain|trust|cta)$"),
    grade: str | None = Query(default=None, pattern="^[GYR]$"),
    microtype_id: str | None = None,
    limit: int = 50,
    db: Session = Depends(get_session),
) -> list[dict]:
    where = ["1=1"]
    params: dict = {"limit": limit}
    if q:
        where.append("content ILIKE :q")
        params["q"] = f"%{q}%"
    if atom_type:
        where.append("atom_type = :t")
        params["t"] = atom_type
    if grade:
        where.append("compliance_grade = :g")
        params["g"] = grade
    if microtype_id:
        where.append("microtype_ids @> ARRAY[CAST(:m AS UUID)]")
        params["m"] = microtype_id

    rows = db.execute(
        text(
            f"""
            SELECT id, atom_type, content, compliance_grade, feasibility_4d,
                   microtype_ids, source_case_id, created_by_agent
            FROM atoms WHERE {" AND ".join(where)}
            ORDER BY id DESC
            LIMIT :limit
            """
        ),
        params,
    ).mappings().all()
    return [dict(r) for r in rows]
