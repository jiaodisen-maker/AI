"""MCP Server implementation using AgentScope's built-in MCP support.

Exposes AI middleware skills and ontology queries as MCP tools
that external agents can discover and call.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class MCPServerManager:
    """Manages MCP tool registration and server lifecycle.

    Skills and ontology queries are registered as MCP tools.
    External agents connect via stdio or HTTP+SSE transport.
    """

    def __init__(self) -> None:
        self._tools: dict[str, dict[str, Any]] = {}

    def register_skill_tool(
        self,
        skill_id: str,
        name: str,
        description: str,
        handler: callable,
        parameters: dict[str, Any] | None = None,
    ) -> None:
        """Register a skill as an MCP tool."""
        self._tools[skill_id] = {
            "name": name,
            "description": description,
            "handler": handler,
            "parameters": parameters or {},
        }
        logger.info("MCP tool registered: %s", name)

    def register_ontology_tools(self, ontology_service: Any) -> None:
        """Register ontology query methods as MCP tools."""
        if ontology_service is None:
            return

        tool_mappings = [
            ("query_product", "查询产品信息", "查询产品的成分、功效、合规要求"),
            ("query_metric", "查询指标定义", "查询指标的定义、公式、数据源"),
            ("query_role", "查询角色权限", "查询角色的权限、工具、数据范围"),
            ("query_compliance", "查询合规规则", "查询产品的合规要求和禁止宣称"),
            ("query_workflow", "查询业务流程", "查询SOP工作流的步骤和审批链"),
            ("query_capability", "查询能力信息", "查询能力的持有者和自动化状态"),
        ]

        for method_name, name, description in tool_mappings:
            method = getattr(ontology_service, method_name, None)
            if method:
                self._tools[method_name] = {
                    "name": name,
                    "description": description,
                    "handler": method,
                }

        logger.info("Registered %d ontology MCP tools", len(tool_mappings))

    def list_tools(self) -> list[dict[str, str]]:
        """List all registered MCP tools."""
        return [
            {"id": tid, "name": t["name"], "description": t["description"]}
            for tid, t in self._tools.items()
        ]

    async def call_tool(self, tool_id: str, arguments: dict[str, Any]) -> Any:
        """Call a registered MCP tool by ID."""
        tool = self._tools.get(tool_id)
        if not tool:
            return {"error": f"Tool not found: {tool_id}"}

        handler = tool["handler"]
        try:
            result = handler(**arguments)
            return result
        except Exception as e:
            logger.error("MCP tool %s failed: %s", tool_id, e)
            return {"error": str(e)}
