"""Multi-tenant support: data isolation between organizations.

Each tenant has:
  - Isolated experience patterns
  - Isolated session memory
  - Isolated ontology overrides (extend base ontology)
  - Separate budget and rate limits

Tenants share the base ontology, Skills, and Agent infrastructure.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class Tenant:
    """A tenant (typically a customer organization)."""

    id: str
    name: str
    config: dict[str, Any] = field(default_factory=dict)
    ontology_overrides: dict[str, Any] = field(default_factory=dict)
    enabled_skills: list[str] = field(default_factory=list)  # empty = all
    daily_token_limit: int = 1000000
    feishu_app_id: str = ""
    created_at: str = ""


class TenantManager:
    """Manages multi-tenant configuration and isolation."""

    def __init__(self) -> None:
        self._tenants: dict[str, Tenant] = {}
        self._init_default_tenant()

    def _init_default_tenant(self) -> None:
        """Single-tenant mode: create a default tenant."""
        self.create_tenant(
            tenant_id="default",
            name="默认租户",
            config={"mode": "single_tenant"},
        )

    def create_tenant(
        self,
        tenant_id: str,
        name: str,
        config: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Tenant:
        """Create a new tenant."""
        from datetime import datetime
        tenant = Tenant(
            id=tenant_id,
            name=name,
            config=config or {},
            created_at=datetime.now().isoformat(),
            **kwargs,
        )
        self._tenants[tenant_id] = tenant
        logger.info("Tenant created: %s (%s)", tenant_id, name)
        return tenant

    def get_tenant(self, tenant_id: str) -> Tenant | None:
        return self._tenants.get(tenant_id)

    def list_tenants(self) -> list[Tenant]:
        return list(self._tenants.values())

    def is_skill_enabled(self, tenant_id: str, skill_id: str) -> bool:
        """Check if a skill is enabled for a tenant."""
        tenant = self.get_tenant(tenant_id)
        if not tenant:
            return False
        if not tenant.enabled_skills:  # empty = all enabled
            return True
        return skill_id in tenant.enabled_skills

    def get_namespaced_key(self, tenant_id: str, key: str) -> str:
        """Get a Redis/DB key namespaced by tenant."""
        return f"tenant:{tenant_id}:{key}"

    def merge_ontology(
        self, tenant_id: str, base_ontology: dict[str, Any]
    ) -> dict[str, Any]:
        """Merge tenant overrides into base ontology."""
        tenant = self.get_tenant(tenant_id)
        if not tenant or not tenant.ontology_overrides:
            return base_ontology

        merged = dict(base_ontology)
        for key, value in tenant.ontology_overrides.items():
            if key in merged and isinstance(merged[key], dict):
                merged[key] = {**merged[key], **value}
            else:
                merged[key] = value
        return merged
