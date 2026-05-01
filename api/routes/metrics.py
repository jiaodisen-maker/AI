"""GET /metrics — Prometheus exposition format。

Gauges:
- agentic_open_alerts (by alert_type)
- agentic_cases_total (by data_lineage)
- agentic_poc_pending_purge
- agentic_atoms_total (by atom_type, by compliance_grade)
- agentic_microtypes_total (by status)
- agentic_dspy_prompt_versions (by agent)
"""
from fastapi import APIRouter, Depends, Response
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..db import get_session

router = APIRouter(tags=["metrics"])


def _fmt(name: str, help_text: str, samples: list[tuple[dict, float]]) -> str:
    lines = [f"# HELP {name} {help_text}", f"# TYPE {name} gauge"]
    for labels, value in samples:
        if labels:
            label_str = ",".join(f'{k}="{v}"' for k, v in labels.items())
            lines.append(f"{name}{{{label_str}}} {value}")
        else:
            lines.append(f"{name} {value}")
    return "\n".join(lines)


@router.get("/metrics")
def metrics(db: Session = Depends(get_session)) -> Response:
    blocks: list[str] = []

    # open alerts by type
    rows = db.execute(
        text(
            """
            SELECT alert_type, COUNT(*) AS n
            FROM hitl_alerts WHERE status = 'open'
            GROUP BY alert_type
            """
        )
    ).all()
    blocks.append(
        _fmt(
            "agentic_open_alerts",
            "Open HITL alerts by type",
            [({"alert_type": r.alert_type}, r.n) for r in rows],
        )
    )

    # cases by lineage
    rows = db.execute(
        text(
            """
            SELECT data_lineage, COUNT(*) AS n
            FROM cases GROUP BY data_lineage
            """
        )
    ).all()
    blocks.append(
        _fmt(
            "agentic_cases_total",
            "Cases by data_lineage",
            [({"data_lineage": r.data_lineage}, r.n) for r in rows],
        )
    )

    # poc pending purge
    n = db.execute(
        text(
            """
            SELECT COUNT(*) FROM cases
            WHERE data_lineage = 'poc_crawled' AND poc_purge_at IS NOT NULL AND poc_purge_at < now()
            """
        )
    ).scalar_one()
    blocks.append(_fmt("agentic_poc_pending_purge", "PoC cases past TTL pending purge", [({}, n)]))

    # atoms
    rows = db.execute(
        text(
            """
            SELECT atom_type, COALESCE(compliance_grade, '?') AS grade, COUNT(*) AS n
            FROM atoms GROUP BY atom_type, compliance_grade
            """
        )
    ).all()
    blocks.append(
        _fmt(
            "agentic_atoms_total",
            "Atoms by atom_type and compliance_grade",
            [({"atom_type": r.atom_type, "grade": r.grade}, r.n) for r in rows],
        )
    )

    # microtypes
    rows = db.execute(
        text("SELECT status, COUNT(*) AS n FROM microtypes GROUP BY status")
    ).all()
    blocks.append(
        _fmt(
            "agentic_microtypes_total",
            "Microtypes by status",
            [({"status": r.status}, r.n) for r in rows],
        )
    )

    # prompt versions
    rows = db.execute(
        text("SELECT agent, COUNT(*) AS n FROM prompt_versions GROUP BY agent")
    ).all()
    blocks.append(
        _fmt(
            "agentic_dspy_prompt_versions",
            "DSPy prompt versions by agent",
            [({"agent": r.agent}, r.n) for r in rows],
        )
    )

    body = "\n\n".join(blocks) + "\n"
    return Response(content=body, media_type="text/plain; version=0.0.4")
