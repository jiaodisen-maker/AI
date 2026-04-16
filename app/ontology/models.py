"""Pydantic data models for the Enterprise Ontology."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class RoleDefinition(BaseModel):
    """A role in the organization ontology."""

    name: str = ""
    permissions: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    data_scope: list[str] = Field(default_factory=list)
    reports_to: str = ""
    collaborates_with: list[str] = Field(default_factory=list)


class CapabilityDefinition(BaseModel):
    """A capability in the capabilities ontology."""

    id: str = ""
    name: str = ""
    holders: dict[str, list[str]] = Field(default_factory=dict)
    automation_status: str = "none"  # none / partial / full
    automation_coverage: int = 0
    gaps: list[str] = Field(default_factory=list)
    priority: str = ""


class WorkflowStep(BaseModel):
    """A step in a workflow/SOP."""

    id: int = 0
    role: str = ""
    action: str = ""
    skill: str = ""
    type: str = "deterministic"  # deterministic / probabilistic / human_approval
    condition: str = ""
    gate: str = ""
    timeout: str = ""


class MetricDefinition(BaseModel):
    """A business metric definition."""

    chinese_name: str = ""
    definition: str = ""
    formula: str = ""
    data_source: str = ""
    dimensions: list[str] = Field(default_factory=list)
    warning: str = ""


class ProductInfo(BaseModel):
    """A product from the domain ontology."""

    category: str = ""
    subcategories: list[str] = Field(default_factory=list)
    key_ingredients: list[dict[str, Any]] = Field(default_factory=list)
    approved_claims: list[str] = Field(default_factory=list)
    prohibited_claims: list[str] = Field(default_factory=list)
    required_disclaimers: list[str] = Field(default_factory=list)
    competitors: list[dict[str, Any]] = Field(default_factory=list)


class BusinessEvent(BaseModel):
    """A business event from the events ontology."""

    trigger_condition: str = ""
    severity: str = "P2"
    response_workflow: str = ""
    auto_actions: list[str] = Field(default_factory=list)
    sla: str = ""
    escalation: str = ""
