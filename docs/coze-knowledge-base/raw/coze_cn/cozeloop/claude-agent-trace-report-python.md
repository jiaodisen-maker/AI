---
source_url: https://docs.coze.cn/cozeloop/claude-agent-trace-report-python
title: 'Claude Agent SDK (Python) - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:54Z
---

# Claude Agent SDK (Python) - 文档 - 扣子

Claude Agent SDK (Python)

本文介绍如何使用 OpenTelemetry 协议将 [Claude Agent SDK (Python)](<https://platform.claude.com/docs/en/agent-sdk/overview>) 的 Trace 数据自动上报到扣子罗盘。​

功能介绍​

Claude Agent SDK 是 Anthropic 官方提供的 Agent 开发工具包。结合 LangSmith SDK 和 OpenTelemetry SDK，你可以全面追踪基于 Claude Agent SDK 构建的 Agent 的运行状态，包括 Agent 执行、与 LLM 的交互及工具调用等。Trace 数据将以标准 OpenTelemetry Trace 格式上报至扣子罗盘平台，实现完整的可观测性监控。​

本文将指导你通过 LangSmith Python SDK 和 OpenTelemetry Python SDK 完成智能体 Trace 数据的集成配置。​

准备工作​

你需要先安装以下 Python 库：​

  * claude-agent-sdk：Claude Agent SDK。​

  * opentelemetry-sdk：OpenTelemetry Python SDK，用于向扣子罗盘上报符合 OpenTelemetry 标准的 Trace 数据。​

  * 说明

OpenTelemetry Python SDK 要求 Python 必须是 3.9.0 或更高版本。​

​

  * opentelemetry-exporter-otlp：OpenTelemetry Python SDK 的 OTLP 导出器，用于将 Trace 数据导出到支持 OTLP 协议的后端服务。​

  * langsmith[claude-agent-sdk]：LangSmith SDK 的 Claude Agent SDK 集成包，用于追踪由 Claude Agent SDK 构建的 Agent。​

  * 说明

仅 0.5.0 或更高版本的 LangSmith SDK 支持 Claude Agent SDK 监控插件。​

​

  * langsmith[otel]：LangSmith SDK 的 OpenTelemetry 集成包，用于将 LangSmith SDK 的 Trace 数据与 OpenTelemetry 生态系统集成。​

​

Python

复制

pip install claude-agent-sdk​

pip install opentelemetry-sdk​

pip install opentelemetry-exporter-otlp​

pip install "langsmith[claude-agent-sdk]" ​

pip install "langsmith[otel]"​

​

操作步骤​

步骤一：配置环境变量​

在上报 Trace 数据前，你需要正确配置环境变量，以确保 Trace 数据能够正确发送到指定的扣子罗盘空间中。环境变量配置格式及说明如下：​

​

Plain Text

复制

ANTHROPIC_API_KEY=***​

LANGSMITH_OTEL_ENABLED=true​

LANGSMITH_OTEL_ONLY=true​

LANGSMITH_TRACING=true​

OTEL_EXPORTER_OTLP_HEADERS=cozeloop-workspace-id={扣子罗盘工作空间ID},Authorization=Bearer {个人访问令牌或服务访问令牌}​

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.coze.cn/v1/loop/opentelemetry/v1/traces​

​

​

环境变量​| 说明​  
---|---  
ANTHROPIC_API_KEY​| Claude API 密钥，用于访问 Anthropic 的 Claude 模型服务。获取方法参考 [Claude Developer Platform](<https://console.anthropic.com/settings/keys>)。​  
OTEL_EXPORTER_OTLP_HEADERS​| OpenTelemetry SDK 数据上报的认证头信息，包括以下参数：​

  * cozeloop-workspace-id：扣子罗盘的工作空间 ID。获取方法参考 ​获取扣子罗盘空间 ID。​

  * Authorization：扣子罗盘的个人访问令牌或服务访问令牌，获取方法参考 ​配置个人访问令牌 或 ​配置服务访问令牌。​

  
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT​| OpenTelemetry SDK 的数据上报地址，固定为 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。​  
LANGSMITH_OTEL_ENABLED​| 固定为 true，启用 LangSmith SDK 的 OpenTelemetry 集成功能，使其能够生成符合 OpenTelemetry 标准的 Trace 数据。​  
LANGSMITH_OTEL_ONLY​| 固定为 true，配置 LangSmith SDK 为纯 OpenTelemetry 模式，不向 LangSmith 平台发送数据，仅输出 OpenTelemetry 标准格式的 Trace 数据。​  
LANGSMITH_TRACING​| 固定为 true，启用 LangSmith SDK 的自动追踪和监控功能。​  
  
​

步骤二：上报 Trace​

你可以结合使用 LangSmith SDK 与 OpenTelemetry Python SDK，将 Agent 的 Trace 数据上报至扣子罗盘。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27770%27%20height=%2774%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzcwIiBoZWlnaHQ9Ijc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

下方的示例代码演示如何通过 LangSmith SDK 追踪 Agent 的运行状态并生成符合 OpenTelemetry 标准的 Trace 数据，然后使用 OpenTelemetry Python SDK 将 Trace 数据上报到扣子罗盘。​

​

Python

复制

import os​

import asyncio​

from opentelemetry import trace​

from opentelemetry.sdk.trace import TracerProvider​

from opentelemetry.sdk.trace.export import (​

BatchSpanProcessor,​

)​

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter​

from claude_agent_sdk import (​

ClaudeAgentOptions,​

ClaudeSDKClient,​

tool,​

create_sdk_mcp_server,​

)​

from typing import Any​

​

# Your Anthropic API key​

os.environ["ANTHROPIC_API_KEY"] = "sk-ant-xxx"​

​

# OpenTelemetry env​

os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = "https://api.coze.cn/v1/loop/opentelemetry/v1/traces" # cozeloop endpoint​

os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = "cozeloop-workspace-id=xxx,Authorization=Bearer pat_xxx" # cozeloop space id, pat or sat token​

​

# Configure LangChain OpenTelemetry instrumentation for Claude Agent SDK​

os.environ["LANGSMITH_OTEL_ENABLED"] = "true"​

os.environ["LANGSMITH_OTEL_ONLY"] = "true"​

os.environ["LANGSMITH_TRACING"] = "true"​

​

​

otlp_exporter = OTLPSpanExporter(​

timeout=10,​

)​

trace.set_tracer_provider(TracerProvider())​

trace.get_tracer_provider().add_span_processor(​

BatchSpanProcessor(otlp_exporter)​

)​

tracer = trace.get_tracer(__name__)​

​

from langsmith.integrations.claude_agent_sdk import configure_claude_agent_sdk # require langsmith version >= 0.5.0​

​

# Configure Claude Agent SDK with OpenTelemetry tracing​

configure_claude_agent_sdk()​

​

​

@tool(​

"get_weather",​

"Gets the current weather for a given city",​

{​

"city": str,​

},​

)​

async def get_weather(args: dict[str, Any]) -> dict[str, Any]:​

"""Simulated weather lookup tool"""​

city = args["city"]​

​

# Simulated weather data​

weather_data = {​

"San Francisco": "Foggy, 62°F",​

"New York": "Sunny, 75°F",​

"London": "Rainy, 55°F",​

"Tokyo": "Clear, 68°F",​

}​

​

weather = weather_data.get(city, "Weather data not available")​

return {"content": [{"type": "text", "text": f"Weather in {city}: {weather}"}]}​

​

​

async def main():​

# Create SDK MCP server with the weather tool​

weather_server = create_sdk_mcp_server(​

name="weather",​

version="1.0.0",​

tools=[get_weather],​

)​

​

options = ClaudeAgentOptions(​

model="claude-sonnet-4-5-20250929",​

system_prompt="You are a friendly travel assistant who helps with weather information.",​

mcp_servers={"weather": weather_server},​

allowed_tools=["mcp__weather__get_weather"],​

)​

​

# Set custom span, name is root_span​

with tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

​

# Start Claude SDK client​

async with ClaudeSDKClient(options=options) as client:​

await client.query("What's the weather like in San Francisco and Tokyo?")​

​

async for message in client.receive_response():​

print(message)​

​

​

if __name__ == "__main__":​

asyncio.run(main())​

​

自定义 Span​

LangSmith SDK 会自动生成符合 [LangSmith 格式](<https://docs.langchain.com/langsmith/run-data-format>) 的 Span。同时，你也可以使用 OpenTelemetry Python SDK 自定义 Span。​

示例代码演示了如何使用 OpenTelemetry Python SDK 自定义一个 Span（即示例代码中的 root_span）。LangSmith SDK 自动生成的 Span 会与你自定义的 Span 自动关联，并显示在同一条 Trace 中。自定义 Span 时，其 attribute 和 event 需符合 ​OpenTelemetry 字段映射 中的规范。参考 ​步骤三：查看 Trace 查看示例代码所生成的 Trace 数据。​

​

Python

复制

# Set custom span, name is root_span​

with tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

​

# Start Claude SDK client​

async with ClaudeSDKClient(options=options) as client:​

await client.query("What's the weather like in San Francisco and Tokyo?")​

​

async for message in client.receive_response():​

print(message)​

​

步骤三：查看 Trace​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并查看 Agent 上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273024%27%20height=%271529.704918032787%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyNCIgaGVpZ2h0PSIxNTI5LjcwNDkxODAzMjc4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例地址​

要获取上报 Trace 数据的完整示例代码，参考 [claude_agent](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/integration/framework/claude_agent>)。​

​

​

上一篇

AutoGen

下一篇

Claude Agent SDK (Node.js)