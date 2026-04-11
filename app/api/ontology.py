"""Ontology management API: view, query, and edit ontology definitions.

Provides the backend for the ontology management frontend.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/ontology", tags=["ontology"])


class OntologyUpdateRequest(BaseModel):
    """Request to update an ontology entry."""

    path: str  # e.g. "product_categories.胶原蛋白.approved_claims"
    value: Any


@router.get("/dimensions")
async def list_dimensions():
    """List all loaded ontology dimensions."""
    from app.main import get_app_state

    state = get_app_state()
    if not hasattr(state, "ontology_service") or state.ontology_service is None:
        return {"dimensions": []}
    return {"dimensions": state.ontology_service.list_dimensions()}


@router.get("/dimension/{name}")
async def get_dimension(name: str):
    """Get full content of a specific ontology dimension."""
    from app.main import get_app_state

    state = get_app_state()
    if not hasattr(state, "ontology_service") or state.ontology_service is None:
        raise HTTPException(status_code=503, detail="Ontology service not initialized")
    data = state.ontology_service.loader.get(name)
    if not data:
        raise HTTPException(status_code=404, detail=f"Dimension '{name}' not found")
    return {"dimension": name, "data": data}


@router.get("/product/{name}")
async def query_product(name: str):
    """Query product info from domain ontology."""
    from app.main import get_app_state

    state = get_app_state()
    return state.ontology_service.query_product(name)


@router.get("/metric/{name}")
async def query_metric(name: str):
    """Query metric definition."""
    from app.main import get_app_state

    state = get_app_state()
    return state.ontology_service.query_metric(name)


@router.get("/role/{name}")
async def query_role(name: str):
    """Query role permissions and scope."""
    from app.main import get_app_state

    state = get_app_state()
    return state.ontology_service.query_role(name)


@router.get("/compliance/{product_name}")
async def query_compliance(product_name: str):
    """Query compliance rules for a product."""
    from app.main import get_app_state

    state = get_app_state()
    return state.ontology_service.query_compliance(product_name)


@router.get("/workflow/{name}")
async def query_workflow(name: str):
    """Query a business workflow/SOP."""
    from app.main import get_app_state

    state = get_app_state()
    return state.ontology_service.query_workflow(name)


@router.get("/capability/{name}")
async def query_capability(name: str):
    """Query capability info and automation status."""
    from app.main import get_app_state

    state = get_app_state()
    return state.ontology_service.query_capability(name)


@router.post("/reload")
async def reload_ontology():
    """Hot-reload all ontology YAML files."""
    from app.main import get_app_state

    state = get_app_state()
    data = state.ontology_service.loader.reload()
    return {"status": "reloaded", "dimensions": list(data.keys())}
