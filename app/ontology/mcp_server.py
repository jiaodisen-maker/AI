"""Ontology MCP exposure — lets external agents query the enterprise ontology.

This module bridges OntologyService to the MCP Server,
so Claude Code, Gemini CLI, Feishu Aily can query:
  - Products (ingredients, claims, compliance)
  - Metrics (definitions, formulas)
  - Roles (permissions, tools, scope)
  - Workflows (SOP steps)
  - Capabilities (automation status)
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.mcp.server import MCPServerManager
    from app.ontology.service import OntologyService

logger = logging.getLogger(__name__)


def expose_ontology_via_mcp(
    mcp: MCPServerManager,
    ontology: OntologyService,
) -> None:
    """Register all ontology query methods as MCP tools."""
    mcp.register_ontology_tools(ontology)
    logger.info("Ontology exposed via MCP: 6 tools registered")
