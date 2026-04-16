"""Tests for the MCP Server Manager."""

import pytest

from app.mcp.server import MCPServerManager


def test_register_and_list_tools():
    mcp = MCPServerManager()
    mcp.register_skill_tool(
        skill_id="test-skill",
        name="Test Tool",
        description="A test tool",
        handler=lambda: "result",
    )

    tools = mcp.list_tools()
    assert len(tools) == 1
    assert tools[0]["id"] == "test-skill"
    assert tools[0]["name"] == "Test Tool"


@pytest.mark.asyncio
async def test_call_tool():
    mcp = MCPServerManager()
    mcp.register_skill_tool(
        skill_id="echo",
        name="Echo",
        description="Echoes input",
        handler=lambda text="": f"Echo: {text}",
    )

    result = await mcp.call_tool("echo", {"text": "hello"})
    assert result == "Echo: hello"


@pytest.mark.asyncio
async def test_call_nonexistent_tool():
    mcp = MCPServerManager()
    result = await mcp.call_tool("nonexistent", {})
    assert "error" in result


def test_register_ontology_tools():
    mcp = MCPServerManager()

    class MockOntology:
        def query_product(self, name): return {"product": name}
        def query_metric(self, name): return {"metric": name}
        def query_role(self, name): return {"role": name}
        def query_compliance(self, name): return {"compliance": name}
        def query_workflow(self, name): return {"workflow": name}
        def query_capability(self, name): return {"capability": name}

    mcp.register_ontology_tools(MockOntology())
    tools = mcp.list_tools()
    assert len(tools) == 6
