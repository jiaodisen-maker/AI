"""Ontology query service — used by agents via tools/MCP."""

from __future__ import annotations

import logging
from typing import Any

from app.ontology.loader import OntologyLoader

logger = logging.getLogger(__name__)


class OntologyService:
    """Query interface for the enterprise ontology.

    Agents call these methods (via tool functions) to look up
    products, metrics, roles, workflows, compliance rules, etc.
    """

    def __init__(self, loader: OntologyLoader | None = None) -> None:
        self.loader = loader or OntologyLoader()
        self.loader.load_all()

    def query_product(self, product_name: str) -> dict[str, Any]:
        """Query product info: ingredients, claims, prohibited claims."""
        domain = self.loader.get("health_supplements")
        categories = domain.get("product_categories", {})

        for cat_name, cat_data in categories.items():
            if product_name in cat_name or cat_name in product_name:
                return {"category": cat_name, **cat_data}

        return {"error": f"未找到产品: {product_name}"}

    def query_metric(self, metric_name: str) -> dict[str, Any]:
        """Query metric definition: formula, data source, dimensions."""
        data_defs = self.loader.get("data_definitions")
        metrics = data_defs.get("metrics", {})

        if metric_name in metrics:
            return {"metric": metric_name, **metrics[metric_name]}

        # Fuzzy match
        for name, info in metrics.items():
            if metric_name in name or metric_name in info.get("chinese_name", ""):
                return {"metric": name, **info}

        return {"error": f"未找到指标: {metric_name}"}

    def query_role(self, role_name: str) -> dict[str, Any]:
        """Query role: permissions, tools, data scope, reports_to."""
        org = self.loader.get("organization")
        roles = org.get("roles", {})

        if role_name in roles:
            return {"role": role_name, **roles[role_name]}

        return {"error": f"未找到角色: {role_name}"}

    def query_compliance(self, product_name: str) -> dict[str, Any]:
        """Query compliance rules for a product category."""
        product = self.query_product(product_name)
        if "error" in product:
            return product

        return {
            "product": product.get("category", product_name),
            "approved_claims": product.get("approved_claims", []),
            "prohibited_claims": product.get("prohibited_claims", []),
            "required_disclaimers": product.get("required_disclaimers", []),
        }

    def query_workflow(self, workflow_name: str) -> dict[str, Any]:
        """Query a business workflow/SOP."""
        workflows = self.loader.get("workflows")
        wf_list = workflows.get("workflows", {})

        if workflow_name in wf_list:
            return {"workflow": workflow_name, **wf_list[workflow_name]}

        return {"error": f"未找到流程: {workflow_name}"}

    def query_capability(self, capability_name: str) -> dict[str, Any]:
        """Query a capability: who has it, automation status."""
        caps = self.loader.get("capabilities")
        for domain_data in caps.get("capability_domains", {}).values():
            for cap in domain_data.get("capabilities", []):
                if capability_name in cap.get("name", "") or capability_name in cap.get("id", ""):
                    return cap

        return {"error": f"未找到能力: {capability_name}"}

    def list_dimensions(self) -> list[str]:
        """List all loaded ontology dimensions."""
        return self.loader.dimensions
