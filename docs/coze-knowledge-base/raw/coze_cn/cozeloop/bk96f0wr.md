---
source_url: https://docs.coze.cn/cozeloop/bk96f0wr
title: 'Pydantic AI - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:19Z
---

# Pydantic AI - 文档 - 扣子

Pydantic AI

本文介绍如何使用 OpenTelemetry 协议将 [Pydantic AI](<https://ai.pydantic.dev/>) 的 Trace 数据自动上报到扣子罗盘。​

功能介绍​

Pydantic AI 是一个用于构建生产级 AI 应用的 Python Agent 框架。结合 OpenInference 和 OpenTelemetry SDK，你可以全面追踪 Pydantic AI Agent 的运行状态。Trace 数据将以标准 OpenTelemetry Trace 格式上报至扣子罗盘平台，实现完整的可观测性监控。​

准备工作​

你需要先安装以下 Python 库：​

  * pydantic-ai：Pydantic AI 核心库。​

  * opentelemetry-sdk：OpenTelemetry Python SDK，用于向扣子罗盘上报符合 OpenTelemetry 标准的 Trace 数据。​

  * 说明

OpenTelemetry Python SDK 要求 Python 必须是 3.9.0 或更高版本。​

​

  * opentelemetry-exporter-otlp：OTLP 导出器。​

  * openinference-instrumentation-pydantic-ai：针对 Pydantic AI 的 OpenInference SDK，用于追踪 Pydantic AI 。​

​

Python

复制

pip install pydantic-ai​

pip install opentelemetry-sdk​

pip install opentelemetry-exporter-otlp​

pip install openinference-instrumentation-pydantic-ai​

​

操作步骤​

步骤一：配置环境变量​

在上报 Trace 数据前，你需要正确配置环境变量，以确保 Trace 数据能够正确发送到指定的扣子罗盘空间中。环境变量配置格式及说明如下：​

​

Python

复制

OTEL_EXPORTER_OTLP_HEADERS=cozeloop-workspace-id={扣子罗盘工作空间ID},Authorization=Bearer {个人访问令牌或服务访问令牌}​

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.coze.cn/v1/loop/opentelemetry/v1/traces​

OPENAI_BASE_URL=***​

OPENAI_API_KEY=***​

OPENAI_MODEL_NAME=***​

​

​

环境变量​| 说明​  
---|---  
OTEL_EXPORTER_OTLP_HEADERS​| OpenTelemetry SDK 数据上报的认证头信息，包括以下参数：​

  * cozeloop-workspace-id：扣子罗盘的工作空间 ID。获取方法参考​获取扣子罗盘空间 ID。​

  * Authorization：扣子罗盘的个人访问令牌或服务访问令牌，获取方法参考​配置个人访问令牌 或 ​配置服务访问令牌。​

  
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT​| OpenTelemetry SDK 的数据上报地址，固定为 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。​  
OPENAI_BASE_URL​| 配置 OpenAI 模型服务的 Base URL。推荐使用火山方舟模型服务：https://ark.cn-beijing.volces.com/api/v3。​  
OPENAI_API_KEY​| 配置 OpenAI 模型服务的 API Key。如果使用火山方舟模型，请参考 [获取 API Key](<https://www.volcengine.com/docs/82379/1361424>)。​  
OPENAI_MODEL_NAME​| 模型名称，例如 openai/doubao-1-5-pro-256k-250115。使用模型提供方作为前缀，例如 openai/。​  
  
​

步骤二：上报 Trace​

你可以结合使用 OpenInference Python SDK 与 OpenTelemetry Python SDK，将 Agent 的 Trace 数据上报至扣子罗盘。​

下方的示例代码演示如何通过 OpenInference Python SDK 追踪 Agent 的运行状态并生成符合 OpenTelemetry 标准的 Trace 数据，然后使用 OpenTelemetry Python SDK 将 Trace 数据上报到扣子罗盘。​

​

Python

复制

import os​

import asyncio​

from opentelemetry import trace​

from opentelemetry.sdk.trace import TracerProvider​

from opentelemetry.sdk.trace.export import BatchSpanProcessor​

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter​

​

# OpenAI env​

os.environ['OPENAI_BASE_URL'] = 'https://ark.cn-beijing.volces.com/api/v3' # use ark model url by default, from https://www.volcengine.com/docs/82379/1361424​

os.environ['OPENAI_API_KEY'] = 'xxx' # your api key​

os.environ['OPENAI_MODEL_NAME'] = 'xxx' # your model name, like doubao-1-5-vision-pro-32k-250115​

​

# OTEL env​

os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = "https://api.coze.cn/v1/loop/opentelemetry/v1/traces" # cozeloop otel endpoint​

os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = "cozeloop-workspace-id=xxx,Authorization=Bearer pat_xxx" # set your 'spaceID' and 'pat or sat token'​

​

# OpenInference auto-detection for pydantic_ai​

try:​

from openinference.instrumentation.pydantic_ai import OpenInferenceSpanProcessor​

print("✅ OpenInference pydantic_ai instrumentation enabled")​

except ImportError as e:​

print(f"⚠️ OpenInference pydantic_ai instrumentation import failed: {e}")​

print("Program will continue running, but without OTEL tracing functionality")​

​

# OTEL configuration​

otlp_exporter = OTLPSpanExporter(timeout=10)​

trace.set_tracer_provider(TracerProvider())​

trace.get_tracer_provider().add_span_processor(OpenInferenceSpanProcessor())​

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))​

tracer = trace.get_tracer(__name__)​

​

​

from pydantic_ai import Agent​

​

async def main():​

# Initialize Pydantic AI Agent​

model = 'openai:' \+ os.environ['OPENAI_MODEL_NAME']​

agent = Agent(​

model=model,​

system_prompt='Be concise.',​

instrument=True, # Enable instrumentation​

)​

​

# Set custom span as the root span​

with tracer.start_as_current_span("pydantic_ai_root_span") as span:​

# Set cozeloop specific attribute for custom root span​

span.set_attribute("cozeloop.span_type", "custom")​

​

print("Running Pydantic AI agent...")​

result = await agent.run('What is the capital of France?')​

print(f"Result: {result.output}")​

​

if __name__ == "__main__":​

asyncio.run(main())​

​

自定义 Span​

OpenInference Python SDK 会自动生成符合 [OpenInference 标准](<https://arize-ai.github.io/openinference/spec/>) 的 Span。同时，你也可以使用 OpenTelemetry Python SDK 自定义一个 Span。​

示例代码演示了如何使用 OpenTelemetry Python SDK 自定义一个 Span（即示例代码中的 pydantic_ai_root_span）。OpenInference Python SDK 自动生成的 Span 会与你自定义的 Span 自动关联，并显示在同一条 Trace 中。自定义 Span 时，其 attribute 和 event 需符合 ​OpenTelemetry 字段映射 中的规范。参考 ​步骤三：验证结果 查看示例代码所生成的 Trace 数据。​

​

Python

复制

# Set custom span as the root span​

with tracer.start_as_current_span("pydantic_ai_root_span") as span:​

# Set cozeloop specific attribute for custom root span​

span.set_attribute("cozeloop.span_type", "custom")​

​

print("Running Pydantic AI agent...")​

result = await agent.run('What is the capital of France?')​

print(f"Result: {result.output}")​

​

步骤三：验证结果​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并查看 Agent 上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273010%27%20height=%271614.2622950819673%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAxMCIgaGVpZ2h0PSIxNjE0LjI2MjI5NTA4MTk2NzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

示例地址​

要获取上报 Trace 数据的完整示例代码，参考 [Pydantic AI](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/integration/framework/pydantic_ai>)。​

​

上一篇

OpenAI Agent

下一篇

Spring AI