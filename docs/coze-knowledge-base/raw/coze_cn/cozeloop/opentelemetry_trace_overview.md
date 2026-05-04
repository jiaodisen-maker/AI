---
source_url: https://docs.coze.cn/cozeloop/opentelemetry_trace_overview
title: 'OpenTelemetry Trace - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:44Z
---

# OpenTelemetry Trace - 文档 - 扣子

OpenTelemetry Trace

[OpenTelemetry](<https://opentelemetry.io/>)（OTel）是一个开源的、具备厂商中立性的可观测性框架。它提供了一组规范、API 和库，基于特定结构化数据建模，以输出应用程序的分布式追踪（Trace）、指标（Metrics）和日志（Log）数据。​

扣子罗盘支持接收来自 OpenTelemetry 客户端上报的 Trace 数据并可视化展示，从而实现对应用程序的深度监控和分析。​

基于 OpenTelemetry 客户端上报的流程图如下所示：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27745%27%20height=%27109%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e77d412392a94493af6b499312daa15f~tplv-goo7wpa0wc-quality:q75.image)​

​

OpenTelemetry Trace 集成方式​

通过 OpenTelemetry SDK 上报 Trace​

你可以使用各种语言的 OpenTelemetry SDK 将 Trace 数据上报到扣子罗盘。通过OpenTelemetry SDK 上报时，开发者需要直接在代码中引入 OpenTelemetry SDK 来创建和管理 Trace 数据（例如创建 Span、设置 Attribute、记录 Event 等）。这种方式需要开发者对 OpenTelemetry 的 SDK 有一定的了解，并在代码中明确实现埋点逻辑。具体示例，请参考​通过 OpenTelemetry SDK 上报 Trace。​

通过适配 OpenTelemetry 协议的 AI 框架自动上报 Trace​

与 OpenTelemetry 协议适配的 AI 框架，可集成 OpenTelemetry 能力，实现 Trace 数据向扣子罗盘的自动上报。​

  * ​Spring AI​

  * ​CrewAI​

  * ​Google ADK​

  * ​OpenAI Agent​

  * ​LlamaIndex​

  * ​LiteLLM SDK​

  * ​VeADK​

字段映射​

扣子罗盘完全适配 [OpenTelemetry ](<https://opentelemetry.io/docs/specs/semconv/gen-ai/>)[GenAI 协议](<https://opentelemetry.io/docs/specs/semconv/gen-ai/>)，定义了罗盘标准字段对应的 OpenTelemetry Attribute 和 Event。具体的映射关系，请参考​OpenTelemetry 字段映射。​

常见问题​

如何排查常见报错？​

如果你收到报错，请根据具体使用的框架提示的错误进行排查。一些常见的错误，请参考[错误码](<https://loop.coze.cn/open/docs/cozeloop/error-codes>)。​

扣子罗盘支持什么协议？​

扣子罗盘不支持 GRPC 协议的 OpenTelemetry Endpoint，需使用 http/protobuf 协议。​

如果使用原生的 OpenTelemetry SDK，那么全局环境变量 OTEL_EXPORTER_OTLP_PROTOCOL 或者OTEL_EXPORTER_OTLP_TRACES_PROTOCOL 需配置为"http/protobuf"，或者按照以下配置方式，将当前的SpanExporter 修改为 http/protobuf 协议，以 Python 为例，配置示例如下：​

​

Python

复制

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (​

OTLPSpanExporter as HTTPOTLPSpanExporter,​

)​

headers = {​

"cozeloop-workspace-id": "xxx",​

"authorization": "Bearer xxx",​

}​

exporter = HTTPOTLPSpanExporter(​

endpoint="https://api.coze.cn/v1/loop/opentelemetry/v1/traces",​

headers=headers,​

timeout=10,​

)​

processor = BatchSpanProcessor(exporter)​

provider.add_span_processor(processor)​

​

​

上一篇

数据上报概述

下一篇

通过 OpenTelemetry SDK 上报 Trace