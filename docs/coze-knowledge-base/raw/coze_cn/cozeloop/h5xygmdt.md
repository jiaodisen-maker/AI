---
source_url: https://docs.coze.cn/cozeloop/h5xygmdt
title: 'Semantic Kernel - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:25Z
---

# Semantic Kernel - 文档 - 扣子

Semantic Kernel

本文介绍如何使用 OpenTelemetry 协议将 [Semantic Kernel](<https://learn.microsoft.com/en-us/semantic-kernel/overview/>) 的 Trace 数据自动上报到扣子罗盘。​

功能介绍​

Semantic Kernel 是微软推出的一个用于构建 LLM 应用的 SDK。结合 OpenInference 和 OpenTelemetry SDK，你可以全面追踪 Semantic Kernel 应用的运行状态。Trace 数据将以标准 OpenTelemetry Trace 格式上报至扣子罗盘平台，实现完整的可观测性监控。​

准备工作​

你需要先安装以下 Python 库：​

  * semantic-kernel：Semantic Kernel 核心库。​

  * opentelemetry-sdk：OpenTelemetry Python SDK，用于向扣子罗盘上报符合 OpenTelemetry 标准的 Trace 数据。​

  * 说明

OpenTelemetry Python SDK 要求 Python 必须是 3.9.0 或更高版本。​

​

  * opentelemetry-exporter-otlp：OTLP 导出器。​

  * openinference-instrumentation-openai：针对 OpenAI SDK 的 OpenInference 自动埋点库。由于 Semantic Kernel 底层通过 OpenAI SDK 调用各类兼容 OpenAI 协议的模型，该库可实现对底层交互数据的自动追踪。​

​

Python

复制

pip install semantic-kernel​

pip install opentelemetry-sdk​

pip install opentelemetry-exporter-otlp​

pip install openinference-instrumentation-openai​

​

操作步骤​

步骤一：配置环境变量​

在上报 Trace 数据前，你需要正确配置环境变量，以确保数据能够正确发送到指定的扣子罗盘空间中。环境变量配置格式及说明如下：​

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

你可以结合使用 Semantic Kernel 与 OpenTelemetry Python SDK，将 Agent 的 Trace 数据上报至扣子罗盘。​

下方的示例代码演示如何通过 OpenInference Python SDK 追踪 Agent 的运行状态并生成符合 OpenTelemetry 标准的 Trace 数据，然后使用 OpenTelemetry Python SDK 将 Trace 数据上报到扣子罗盘。​

​

Python

复制

# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates​

# SPDX-License-Identifier: MIT​

​

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

# OTEL configuration​

otlp_exporter = OTLPSpanExporter(timeout=10)​

trace.set_tracer_provider(TracerProvider())​

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))​

tracer = trace.get_tracer(__name__)​

​

# OpenInference auto-detection for Semantic Kernel​

try:​

from openinference.instrumentation.openai import OpenAIInstrumentor​

OpenAIInstrumentor().instrument()​

print("✅ OpenInference Semantic Kernel instrumentation enabled")​

except ImportError as e:​

print(f"⚠️ OpenInference Semantic Kernel instrumentation import failed: {e}")​

print("Program will continue running, but without OTEL tracing functionality")​

​

from semantic_kernel import Kernel​

from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion​

​

async def main():​

# Initialize the kernel​

kernel = Kernel()​

​

# Add OpenAI Chat Completion service​

kernel.add_service(​

OpenAIChatCompletion(​

service_id="chat-gpt",​

ai_model_id=os.environ['OPENAI_MODEL_NAME'],​

)​

)​

​

# Define a simple prompt​

prompt = "Tell me a short joke about a programmer."​

​

# Invoke the prompt​

print(f"Invoking prompt: {prompt}")​

​

# Set custom span, name is root_span​

with tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

​

# Start invoke kernel​

result = await kernel.invoke_prompt(prompt)​

​

print("\nResult:")​

print(result)​

​

if __name__ == "__main__":​

asyncio.run(main())​

​

自定义 Span​

OpenInference Python SDK 会自动生成符合 [OpenInference 标准](<https://arize-ai.github.io/openinference/spec/>) 的 Span。同时，你也可以使用 OpenTelemetry Python SDK 自定义一个 Span。​

示例代码演示了如何使用 OpenTelemetry Python SDK 自定义一个 Span（即示例代码中的 root_span）。OpenInference Python SDK 自动生成的 Span 会与你自定义的 Span 自动关联，并显示在同一条 Trace 中。自定义 Span 时，其 attribute 和 event 需符合​OpenTelemetry 字段映射中的规范。​

​

Python

复制

# Set custom span, name is root_span​

with tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

​

# Start invoke kernel​

result = await kernel.invoke_prompt(prompt)​

​

步骤三：验证结果​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并查看 Agent 上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273020%27%20height=%271669.133489461358%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyMCIgaGVpZ2h0PSIxNjY5LjEzMzQ4OTQ2MTM1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例地址​

要获取上报 Trace 数据的完整示例代码，参考 [Semantic Kernel](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/integration/framework/semantic_kernel>)。​

​

上一篇

Spring AI

下一篇

VeADK