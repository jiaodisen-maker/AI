"""Register Ontology queries as MCP tools for external agent discovery."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.mcp.server import MCPServerManager
    from app.ontology.service import OntologyService

logger = logging.getLogger(__name__)


def register_ontology_as_mcp_tools(
    mcp: MCPServerManager,
    ontology: OntologyService,
) -> None:
    """Register ontology query methods as MCP tools."""
    mcp.register_ontology_tools(ontology)
    logger.info("Ontology MCP tools registered")
