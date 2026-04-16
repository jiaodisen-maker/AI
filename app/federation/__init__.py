"""Federation: multi-tenant + cross-org collaboration."""

from app.federation.mcp_federation import MCPFederation
from app.federation.tenant import Tenant, TenantManager

__all__ = ["Tenant", "TenantManager", "MCPFederation"]
