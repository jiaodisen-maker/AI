"""从 critic_scores 拉训练集供 DSPy 优化。

策略：
- 取 critic_scores 表里 7 维分数 avg ≥ THRESHOLD 的 generated_scripts 作为正样本
- input = (microtype, atoms) input；output = script
- 拆 train/holdout（80/20）
"""
from __future__ import annotations

import json
import statistics

from sqlalchemy import text

from worker.db import session_scope

DIMS = ["hook", "pain", "trust", "cta", "compliance", "creativity", "exec"]
HIGH_THRESHOLD = 7.0


def _avg_for_target(scores_rows: list[dict]) -> float:
    """把同一 target_id 多个 evaluator 的 7 维分数压成一个总均值。"""
    all_vals: list[float] = []
    for sc in scores_rows:
        d = sc.get("scores") or {}
        if isinstance(d, str):
            try:
                d = json.loads(d)
            except json.JSONDecodeError:
                continue
        for k in DIMS:
            v = d.get(k)
            if isinstance(v, int | float):
                all_vals.append(float(v))
    return round(statistics.mean(all_vals), 2) if all_vals else 0.0


def build_a8_trainset(limit: int = 50) -> list[dict]:
    """每条 example: {microtype, atoms, target_script, avg_score}。"""
    out: list[dict] = []
    with session_scope() as s:
        scripts = s.execute(
            text(
                """
                SELECT gs.id, gs.microtype_id, gs.atom_ids, gs.output, gs.for_internal_research_only
                FROM generated_scripts gs
                ORDER BY gs.generated_at DESC
                LIMIT :n
                """
            ),
            {"n": limit * 4},
        ).mappings().all()

        for gs in scripts:
            cs_rows = s.execute(
                text(
                    """
                    SELECT scores FROM critic_scores
                    WHERE target_id = :tid AND target_type = 'generated_script'
                    """
                ),
                {"tid": gs["id"]},
            ).mappings().all()
            avg = _avg_for_target([dict(r) for r in cs_rows])
            if avg < HIGH_THRESHOLD:
                continue

            mt = s.execute(
                text(
                    """
                    SELECT scene, audience, ingredient, emotion, restriction
                    FROM microtypes WHERE id = :id
                    """
                ),
                {"id": gs["microtype_id"]},
            ).mappings().first()
            if mt is None:
                continue

            atom_rows = []
            if gs["atom_ids"]:
                atom_rows = (
                    s.execute(
                        text(
                            """
                            SELECT id, atom_type, content, compliance_grade
                            FROM atoms WHERE id = ANY(CAST(:ids AS UUID[]))
                            """
                        ),
                        {"ids": "{" + ",".join(str(x) for x in gs["atom_ids"]) + "}"},
                    )
                    .mappings()
                    .all()
                )

            out.append(
                {
                    "microtype": dict(mt),
                    "atoms": [dict(a) for a in atom_rows],
                    "target_script": gs["output"],
                    "avg_score": avg,
                    "internal_only": gs["for_internal_research_only"],
                }
            )
            if len(out) >= limit:
                break
    return out
