---
source_url: https://docs.coze.cn/cozeloop/veadk_trace_report
title: 'VeADK - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:29Z
---

# VeADK - 文档 - 扣子

VeADK

本文介绍如何将 VeADK （Volcengine Agent Development Kit）运行过程的 Trace 数据上报到扣子罗盘。​

功能介绍​

VeADK 是由[火山引擎](<https://www.volcengine.com/>)推出的一套面向智能体（Agent）开发的全流程框架，旨在为开发者提供一套面向智能体构建、云端部署、评测与优化的全流程开发框架。关于火山智能体的详细说明可参考[ VeADK 帮助文档](<https://volcengine.github.io/veadk-python/introduction/overview>)。​

VeADK 支持与 OpenTelemetry 集成，自动捕获 Agent 执行过程中的关键路径和中间状态，并将这些信息作为 Trace 数据上报到扣子罗盘，进行可视化分析。本文以 Python SDK 为例，介绍如何通过 OpenTelemetry  SDK 将 VeADK Trace 数据上报至扣子罗盘平台。​

准备工作 ​

使用 OpenTelemetry Python SDK 前，需要先安装 Python SDK 以及相关的依赖库。 ​

1.

安装 Python SDK。 ​

  * OpenTelemetry Python SDK 要求 Python 3.9 或以上版本。你可以通过如下方法查看 Python 版本 。 ​

  * ​

Python

复制

# 查看 Python 版本 ​

python --version ​

​

# 回显信息显示已安装 3.9.2 版本 ​

Python 3.9.2​

​

2.

安装依赖库。 ​

  * 安装 Python 依赖库，分别用于调用 AI 模型、对调用过程进行可观测性管理以及将 Trace 数据导出到后端系统。 ​

  * ​

Python

复制

pip install opentelemetry-sdk​

pip install veadk-python​

​

步骤一：配置环境变量 ​

在上报 Trace 数据前，你需要配置全局环境变量，以确保 VeADK Agent 能够正常调用火山方舟模型，并能正确发送 Trace 数据到指定的扣子罗盘空间中。环境变量配置格式及说明如下： ​

​

环境变量​| 说明​  
---|---  
MODEL_AGENT_API_KEY​| 配置方舟模型的 API Key。获取步骤，请参考 [API Key 管理](<https://www.volcengine.com/docs/82379/1361424>)。​  
OBSERVABILITY_OPENTELEMETRY_COZELOOP_API_KEY ​| 用于设置上报数据时所需的扣子罗盘认证信息，配置为扣子罗盘的个人访问令牌或服务访问令牌，获取访问令牌的步骤，请参考​配置个人访问令牌、​配置服务访问令牌。​  
OBSERVABILITY_OPENTELEMETRY_COZELOOP_SERVICE_NAME ​| 配置为扣子罗盘工作空间 ID。获取空间 ID 的步骤，请参考​获取扣子罗盘工作空间 ID。​  
  
​

步骤二：上报 Trace​

完成上述配置后，你可以通过 VeADK 框架调用火山方舟模型开展 AI 对话，并通过 OpenTelemetry Python SDK 上报 Trace 数据到扣子罗盘。以下示例将分别展示自动上报 Trace 数据与上报自定义 Span 节点数据的具体实现方式。​

自动上报​

在自动上报场景中，先构建一个 VeADK Agent，具体操作请参考 [VeADK 快速开始](<https://volcengine.github.io/veadk-python/introduction/quickstart>)。然后，设置云端上报器 CozeloopExporter，将 Trace 数据上报到扣子罗盘。​

本示例构建了一个聊天智能体，指定火山方舟 doubao-1-5-pro-32k-250115 模型回复用户问题（例如对用户询问北京天气及调用的天气查询工具进行回复）。同时，配置了 CozeloopExporter 上报 Agent 交互过程中的 Trace 数据到扣子罗盘。​

​

Python

复制

import os​

import asyncio​

​

os.environ["MODEL_AGENT_API_KEY"] = "***"​

os.environ["OBSERVABILITY_OPENTELEMETRY_COZELOOP_SERVICE_NAME"] = "***"​

os.environ["OBSERVABILITY_OPENTELEMETRY_COZELOOP_API_KEY"] = "***"​

​

from veadk import Agent, Runner​

from veadk.memory.short_term_memory import ShortTermMemory​

from veadk.tools.demo_tools import get_city_weather​

from veadk.tracing.telemetry.exporters.cozeloop_exporter import CozeloopExporter, CozeloopExporterConfig​

from veadk.tracing.telemetry.opentelemetry_tracer import OpentelemetryTracer​

from opentelemetry import trace​

​

​

exporters = [CozeloopExporter()]​

tracer = OpentelemetryTracer(exporters=exporters) # init veadk opentelemetry tracer​

otel_raw_tracer = trace.get_tracer_provider().get_tracer(__name__) # get global opentelemetry tracer for custom span​

​

agent = Agent(​

name="chat_robot",​

description="A robot talk with user.",​

instruction="Talk with user friendly.",​

tools=[get_city_weather],​

tracers=[tracer],​

model_name="doubao-1-5-pro-32k-250115" # use your model name, like doubao-1-5-pro-32k-250115​

)​

​

session_id = "session_id"​

​

runner = Runner(​

agent=agent,​

short_term_memory=ShortTermMemory()​

)​

​

prompt = "How is the weather like in Beijing? Besides, tell me which tool you invoked."​

​

# set custom span​

with otel_raw_tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

# start veadk runner​

asyncio.run(runner.run(messages=prompt, session_id=session_id))​

​

上报自定义节点​

如果你需要上报自定义 Span 节点，可以使用 OpenTelemetry SDK 手动创建 Span 并上报。OpenTelemetry SDK 手动上报的节点数据支持和自动上报的节点数据串联，形成完整的 Trace 调用树。​

自定义的 OpenTelemetry Span，attribute 和 event 规范需遵循 [OpenTelemetry 字段映射](<https://loop.coze.cn/open/docs/cozeloop/opentelemetry_field_mapping>)。​

​

Python

复制

# 设置自定义Span节点 root_span​

with otel_raw_tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

# start veadk runner​

asyncio.run(runner.run(messages=prompt, session_id=session_id))​

​

步骤三：查看 Trace​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，筛选火山智能体，然后单击目标 Span，查看上报的 VeADK Trace 数据。例如下图的 Trace 数据展示了 Agent 交互全流程与详情：系统设定了一个聊天机器人的角色，当用户询问北京天气及调用的天气查询工具时，由 doubao-1-5-pro-32k-250115 模型生成回复。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271804%27%20height=%27388.0945626477542%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgwNCIgaGVpZ2h0PSIzODguMDk0NTYyNjQ3NzU0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271654%27%20height=%271044.0141843971633%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY1NCIgaGVpZ2h0PSIxMDQ0LjAxNDE4NDM5NzE2MzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

示例地址​

关于上报 VeADK Trace 数据的更多示例代码，请参考 [VeADK](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/integration/framework/veadk>)。​

上一篇

Semantic Kernel

下一篇

扣子工作流