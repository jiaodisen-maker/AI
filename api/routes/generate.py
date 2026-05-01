"""POST /generate — 用户在 UI 选 microtype + atoms 触发生成（非 case-driven 路径）。

case-driven 路径由 workflow 的 A8 自动跑；这个 endpoint 主要给 UI 手工探索。
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..config import get_settings
from ..db import get_session

router = APIRouter(prefix="/generate", tags=["generate"])


class GenerateRequest(BaseModel):
    microtype_id: str
    atom_ids: list[str]
    n: int = 3


class GenerateResponse(BaseModel):
    script_ids: list[str]


@router.post("", response_model=GenerateResponse)
def generate_scripts(
    req: GenerateRequest, db: Session = Depends(get_session)
) -> GenerateResponse:
    settings = get_settings()
    _ = settings  # placeholder for future feature flag

    mt = db.execute(
        text(
            """
            SELECT id, scene, audience, ingredient, emotion, restriction
            FROM microtypes WHERE id = :id
            """
        ),
        {"id": req.microtype_id},
    ).mappings().first()
    if mt is None:
        raise HTTPException(404, "microtype not found")

    if not req.atom_ids:
        raise HTTPException(400, "atom_ids required")

    atoms = db.execute(
        text(
            """
            SELECT id, atom_type, content, compliance_grade
            FROM atoms WHERE id = ANY(CAST(:ids AS UUID[]))
            """
        ),
        {"ids": "{" + ",".join(req.atom_ids) + "}"},
    ).mappings().all()
    if not atoms:
        raise HTTPException(400, "no atoms resolved")

    # 防止 PoC 数据泄漏：检查 atoms 来源 case 的 data_lineage
    lineages = db.execute(
        text(
            """
            SELECT DISTINCT c.data_lineage
            FROM atoms a JOIN cases c ON a.source_case_id = c.id
            WHERE a.id = ANY(CAST(:ids AS UUID[]))
            """
        ),
        {"ids": "{" + ",".join(req.atom_ids) + "}"},
    ).scalars().all()

    has_poc = "poc_crawled" in lineages
    if has_poc:
        # PoC 数据触发的生成必须 internal-only（trigger 也会兜底）
        for_internal = True
    else:
        for_internal = False

    # 这里不重复实现 LLM 调用 — 复用 worker 的 a8 路径
    # 但避免在 API 进程加载 worker 模块（worker 依赖 Temporal context），
    # 所以这里走一个简化的同步生成路径
    import json
    import logging

    from worker.agents.a8_prompts import GENERATION_SYSTEM_DEFAULT, build_generation_user
    from worker.llm import call_deepseek
    log = logging.getLogger(__name__)

    script_ids: list[str] = []
    mt_dict = dict(mt)
    atoms_list = [dict(a) for a in atoms]
    for _ in range(req.n):
        try:
            raw = call_deepseek(
                GENERATION_SYSTEM_DEFAULT,
                build_generation_user(mt_dict, atoms_list),
                temperature=0.7,
                response_format_json=True,
            )
            out = json.loads(raw)
        except Exception as e:
            log.warning("/generate LLM failure: %s", e)
            continue

        script_text = out.get("script", "")
        used = out.get("used_atom_ids") or []
        if not script_text:
            continue

        try:
            row = db.execute(
                text(
                    """
                    INSERT INTO generated_scripts (
                        microtype_id, atom_ids, prompt_version, output, llm_model,
                        for_internal_research_only
                    )
                    VALUES (
                        :mt, CAST(:aids AS UUID[]), 'default', :out, 'deepseek-chat', :internal
                    )
                    RETURNING id
                    """
                ),
                {
                    "mt": req.microtype_id,
                    "aids": "{" + ",".join(used) + "}" if used else "{}",
                    "out": script_text,
                    "internal": for_internal,
                },
            ).first()
            script_ids.append(str(row.id))
        except Exception as e:
            log.warning("/generate persist failed (PoC trigger?): %s", e)

    db.commit()
    return GenerateResponse(script_ids=script_ids)
