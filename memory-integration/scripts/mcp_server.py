"""聚合 MCP Server：对 OpenClaw 暴露 3 个统一工具。

OpenClaw 通过 stdio 接入。背后委托给 router.MemoryRouter 和 auto_dream.consolidate。

启动:
  python mcp_server.py            # stdio 模式（OpenClaw 默认）
  python mcp_server.py --setup    # 仅做健康检查
"""
from __future__ import annotations

import argparse
import asyncio
from typing import Any

from mcp.server import Server          # @modelcontextprotocol/python-sdk
from mcp.types import Tool, TextContent

from .router import MemoryRouter
from .auto_dream import consolidate

router = MemoryRouter()
server = Server("memory-integration")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="memory_write",
            description="写入一条记忆。系统会自动决定存到 GBrain（语义/长期）还是 "
                        "Hindsight（情景/工作记忆），或两边都存。",
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {"type": "string"},
                    "hints":   {"type": "object"},
                },
                "required": ["content"],
            },
        ),
        Tool(
            name="memory_recall",
            description="跨 GBrain + Hindsight 检索，RRF 融合。返回结果带 [KB] / [MEM] "
                        "标签，下游 Agent 必须保留标签。",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "k":     {"type": "integer", "default": 5},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="memory_reflect",
            description="触发反思 + 凝固：稳定 belief 写入 GBrain；新文档反向索引 "
                        "进 Hindsight。冲突走 human_review，绝不自动覆盖。",
            inputSchema={
                "type": "object",
                "properties": {
                    "scope":   {"type": "string", "enum": ["recent", "all"],
                                "default": "recent"},
                    "dry_run": {"type": "boolean", "default": False},
                },
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, args: dict[str, Any]) -> list[TextContent]:
    if name == "memory_write":
        res = await router.write(args["content"], args.get("hints"))
        return [TextContent(type="text", text=str(res.__dict__))]

    if name == "memory_recall":
        hits = await router.recall(args["query"], args.get("k", 5))
        # 关键：保留 source 标签，前缀化文本
        lines = [f"[{h.source}] {h.ref}  ({h.ts})\n  {h.text}" for h in hits]
        return [TextContent(type="text", text="\n\n".join(lines))]

    if name == "memory_reflect":
        report = await consolidate(args.get("scope", "recent"),
                                   args.get("dry_run", False))
        return [TextContent(type="text", text=str(report))]

    raise ValueError(f"unknown tool: {name}")


async def health_check():
    res = await router.write("__healthcheck__", {"type": "test"})
    print("write:", res)
    hits = await router.recall("__healthcheck__", k=1)
    print("recall:", hits)
    print("OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--setup", action="store_true")
    args = ap.parse_args()

    if args.setup:
        asyncio.run(health_check())
        return

    from mcp.server.stdio import stdio_server
    asyncio.run(_run_stdio())


async def _run_stdio():
    from mcp.server.stdio import stdio_server
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    main()
