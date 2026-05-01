"""A8 Generation Agent — 反向生成 N=5 候选脚本。

流程：
1) 读 case → 找 A6 写入的 microtype（通过 atoms.microtype_ids 反查）
2) 拉同 microtype 下高质量 atoms（compliance_grade in {G,Y}, feasibility_4d.min ≥ 6 if available）
3) 读当前 active 的 a8 prompt_version（DSPy 自优化产物，否则用 DEFAULT）
4) 调用 Deepseek N=5 次（temperature=0.7 确保多样性）
5) 落库 generated_scripts，for_internal_research_only 由 case.data_lineage 决定
   （PoC 隔离 trigger 会兜底校验）

返回 script_ids: list[str]
"""
from __future__ import annotations

import json
import logging

from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..llm import call_deepseek
from .a8_prompts import GENERATION_SYSTEM_DEFAULT, build_generation_user

log = logging.getLogger(__name__)

DEFAULT_N = 5


def _resolve_microtype_for_case(s, case_id: str) -> dict | None:
    row = s.execute(
        text(
            """
            SELECT m.id, m.scene, m.audience, m.ingredient, m.emotion, m.restriction, m.status
            FROM microtypes m
            JOIN atoms a ON a.microtype_ids @> ARRAY[m.id]
            WHERE a.source_case_id = :cid
            ORDER BY (m.status = 'active') DESC, m.id
            LIMIT 1
            """
        ),
        {"cid": case_id},
    ).mappings().first()
    return dict(row) if row else None


def _fetch_quality_atoms(s, microtype_id: str, limit: int = 40) -> list[dict]:
    rows = s.execute(
        text(
            """
            SELECT id, atom_type, content, compliance_grade, feasibility_4d
            FROM atoms
            WHERE microtype_ids @> ARRAY[CAST(:m AS UUID)]
              AND COALESCE(compliance_grade, 'G') <> 'R'
            ORDER BY
              (compliance_grade = 'G') DESC,
              created_by_agent
            LIMIT :lim
            """
        ),
        {"m": microtype_id, "lim": limit},
    ).mappings().all()
    return [dict(r) for r in rows]


def _resolve_active_prompt(s, agent: str) -> tuple[str, str]:
    row = s.execute(
        text(
            """
            SELECT version, prompt_text FROM prompt_versions
            WHERE agent = :ag
            ORDER BY created_at DESC LIMIT 1
            """
        ),
        {"ag": agent},
    ).first()
    if row:
        return row.version, row.prompt_text
    return "default", GENERATION_SYSTEM_DEFAULT


def _generate_one(system_prompt: str, microtype: dict, atoms: list[dict]) -> dict:
    raw = call_deepseek(
        system_prompt,
        build_generation_user(microtype, atoms),
        temperature=0.7,
        response_format_json=True,
    )
    return json.loads(raw)


@activity.defn
async def generate_scripts(case_id: str, n: int = DEFAULT_N) -> list[str]:
    activity.logger.info("A8 Generation case_id=%s n=%d", case_id, n)

    with session_scope() as s:
        case_row = s.execute(
            text("SELECT data_lineage FROM cases WHERE id = :id"), {"id": case_id}
        ).first()
        if case_row is None:
            return []
        for_internal = case_row.data_lineage == "poc_crawled"

        mt = _resolve_microtype_for_case(s, case_id)
        if mt is None:
            activity.logger.warning("A8 no microtype found for case_id=%s — skip", case_id)
            return []

        atoms = _fetch_quality_atoms(s, mt["id"])
        if not atoms:
            activity.logger.warning("A8 no quality atoms for microtype=%s", mt["id"])
            return []

        version, system_prompt = _resolve_active_prompt(s, "a8")

        script_ids: list[str] = []
        for i in range(n):
            try:
                out = _generate_one(system_prompt, mt, atoms)
            except Exception as e:
                log.warning("A8 gen i=%d failed: %s", i, e)
                continue

            script_text = out.get("script", "")
            used = out.get("used_atom_ids") or []
            if not script_text:
                continue

            try:
                row = s.execute(
                    text(
                        """
                        INSERT INTO generated_scripts (
                            microtype_id, atom_ids, prompt_version, output, llm_model,
                            for_internal_research_only
                        )
                        VALUES (
                            :mt, CAST(:aids AS UUID[]), :pv, :out, 'deepseek-chat', :internal
                        )
                        RETURNING id
                        """
                    ),
                    {
                        "mt": mt["id"],
                        "aids": "{" + ",".join(used) + "}" if used else "{}",
                        "pv": version,
                        "out": script_text,
                        "internal": for_internal,
                    },
                ).first()
                script_ids.append(str(row.id))
            except Exception as e:
                log.warning("A8 persist failed (likely PoC trigger): %s", e)

    activity.logger.info("A8 Generation done case_id=%s scripts=%d", case_id, len(script_ids))
    return script_ids
