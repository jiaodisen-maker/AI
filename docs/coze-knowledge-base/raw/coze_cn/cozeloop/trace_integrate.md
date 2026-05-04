---
source_url: https://docs.coze.cn/cozeloop/trace_integrate
title: '数据上报概述 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:44Z
---

# 数据上报概述 - 文档 - 扣子

数据上报概述

扣子罗盘观测支持自动上报平台上创建的 Prompt、 扣子智能体、扣子工作流和扣子 AI 应用的 Trace 数据。开发者可在扣子罗盘 Trace 中实时查看上报的数据。同时，支持与主流框架 (Eino、Langchain等) 集成，实现 Trace 数据一键上报，也支持灵活的自定义数据上报。​

平台自动上报​

扣子罗盘会自动对平台上创建的 Prompt、扣子智能体、扣子工作流和扣子 AI 应用的用户请求自动上报。同时，支持在调试阶段就通过 Trace 能力查看各环节的执行情况，以便在调试阶段就能够发现问题进行调优。​

如下图所示，在 扣子罗盘观测 > Trace 页面，能够快速筛选出平台 Prompt 开发、同一扣子账号与空间的扣子智能体和扣子 AI 应用的用户请求上报数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27616%27%20height=%27197%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9eb4f5dad3b64a6c8cf59d1266894e8a~tplv-goo7wpa0wc-quality:q75.image)​

​

AI 框架集成上报​

扣子罗盘支持与主流的 AI 框架集成，上报 Trace 数据到扣子罗盘。主要的集成方式及支持的 AI 框架如下：​

说明

对于暂未支持的 AI 框架，可通过 OpenTelemetry SDK 或罗盘 SDK 实现 Trace 数据上报，具体操作，请参考​通过 OpenTelemetry SDK 上报 Trace。​

​

  * 基于 OpenTelemetry 协议集成 AI 框架​

  * ​Spring AI​

  * ​CrewAI​

  * ​Google ADK​

  * ​OpenAI Agent​

  * ​LlamaIndex​

  * ​LiteLLM SDK​

  * ​VeADK​

  * ​Claude Agent SDK (Python)​

  * ​AutoGen​

  * ​Pydantic AI​

  * ​Semantic Kernel​

  * 基于扣子罗盘 SDK 上报​

  * ​LangChain & LangGraph & DeepAgents​

  * ​Eino​

  * ​Instructor​

  * ​扣子工作流​

  * ​扣子智能体​

网关集成上报​

扣子罗盘支持与 API 网关连接，实现 Trace 数据上报。例如通过扣子罗盘 SDK 提供的 OpenAI Client Wrapper 对接 [LiteLLM Proxy](<https://docs.litellm.ai/docs/proxy/quick_start#quick-start---litellm-proxy--configyaml>) 来调用 OpenAI 模型，并上报 Trace 数据。详情请参考 ​LiteLLM Proxy。​

模型提供商直接上报​

扣子罗盘支持与 AI 模型提供商直接集成，上报 Trace 数据。例如通过扣子罗盘 SDK 提供的 OpenAI Client Wrapper 将 OpenAI 模型调用过程的 Trace 数据自动上报到扣子罗盘。详情请参考​OpenAI Chat & Responses。​

SDK 上报​

扣子罗盘支持与 Eino、Langchain 主流框架集成，提供了不同语言的 SDK，可追踪文本和图像数据。此外，扣子罗盘 SDK 支持 Low-Level API，自定义上报 Trace 数据。​

你可以参考以下 SDK 使用说明，进行数据上报：​

​

开发语言​| 参考文档​| 配置示例​  
---|---|---  
Go SDK​| ​快速开始​| 

  * ​Eino ​

  * ​Low-Level API​

  
Python SDK​| ​快速开始​| 

  * ​Langchain ​

  * ​Low-Level API​

  
Node.js SDK​| ​快速开始​| ​Trace 上报​  
  
​

基于 OpenTelemetry 协议上报​

[OpenTelemetry](<https://opentelemetry.io/>)（OTel）是一个开源的、具备厂商中立性的可观测性框架。它提供了一组规范、API 和库，基于特定结构化数据建模，以输出应用程序的分布式追踪（Trace）、指标（Metrics）和日志（Log）数据。​

扣子罗盘支持接收来自 OpenTelemetry 客户端上报的 Trace 数据并可视化展示，从而实现对应用程序的深度监控和分析。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271888%27%20height=%27275.33333333333337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg4OCIgaGVpZ2h0PSIyNzUuMzMzMzMzMzMzMzMzMzciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

目前，支持如下两种上报方式：​

  * 通过 OpenTelemetry SDK 将 Trace 数据上报到扣子罗盘。具体操作，请参考​通过 OpenTelemetry SDK 上报 Trace。​

  * 通过适配 OpenTelemetry 协议的 AI 框架自动上报 Trace。例如通过 Spring AI 与 OpenTelemetry 的集成，将 Trace 数据上报到扣子罗盘。​

上一篇

什么是观测？

下一篇

OpenTelemetry Trace