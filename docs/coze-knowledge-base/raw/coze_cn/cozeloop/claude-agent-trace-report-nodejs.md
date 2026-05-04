---
source_url: https://docs.coze.cn/cozeloop/claude-agent-trace-report-nodejs
title: 'Claude Agent SDK (Node.js) - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:59Z
---

# Claude Agent SDK (Node.js) - 文档 - 扣子

Claude Agent SDK (Node.js)

本文介绍如何使用 OpenTelemetry 协议将 [Claude Agent SDK (Node.js)](<https://platform.claude.com/docs/en/agent-sdk/overview>) 的 Trace 数据自动上报到扣子罗盘。​

功能介绍​

Claude Agent SDK 使用 OpenTelemetry (OTel) 协议，将 Agent 运行过程中的 Trace 和 Span 数据上报到扣子罗盘，以用于性能分析与问题排查。通过结合 [OpenInference](<https://github.com/Arize-ai/openinference>) 提供的 openinference-instrumentation-claude-agent-sdk 库，你无需修改业务代码，即可自动采集并上报以下数据：​

  * 模型调用​

  * 工具调用​

  * 你自行添加的自定义业务节点​

这些数据最终会在扣子罗盘的 Trace 页面上，以完整的调用树形式呈现。​

💡

本文以 Node.js（ESM）示例为主，通过 OTel Exporter 把 trace 发送到 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。​

​

准备工作​

你需要先安装以下 Node.js 库：​

说明

Node.js 必须是 18.0 或更高版本。​

​

  * @anthropic-ai/claude-agent-sdk：Claude Agent SDK。​

  * @arizeai/openinference-instrumentation-claude-agent-sdk：用于 Claude Agent SDK 的自动埋点（instrumentation）。通过钩子注入，追踪 query() 和 ClaudeSDKClient 的 OpenInference AGENT span，包括提示输入、结果输出、会话/模型元数据、标记计数和工具子 span。​

  * @opentelemetry/api、@opentelemetry/sdk-node、@opentelemetry/sdk-trace-base、@opentelemetry/resources、@opentelemetry/exporter-trace-otlp-proto：OpenTelemetry SDK。​

​

Bash

复制

npm i @anthropic-ai/claude-agent-sdk \​

@arizeai/openinference-instrumentation-claude-agent-sdk \​

@opentelemetry/api @opentelemetry/sdk-node @opentelemetry/sdk-trace-base \​

@opentelemetry/resources @opentelemetry/exporter-trace-otlp-proto​

​

操作步骤​

步骤一：配置环境变量​

你需要配置以下环境变量（推荐使用 .env / CI 环境注入；不要把密钥写进代码仓库）。​

​

Bash

复制

# Anthropic​

export ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"​

​

# CozeLoop OTLP Trace 上报地址（固定值）​

export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="https://api.coze.cn/v1/loop/opentelemetry/v1/traces"​

​

# 逗号分隔多个 header（注意是英文逗号）​

export OTEL_EXPORTER_OTLP_HEADERS="cozeloop-workspace-id=YOUR_SPACE_ID,Authorization=Bearer YOUR_TOKEN"​

​

​

环境变量​| 说明​  
---|---  
ANTHROPIC_API_KEY​| Claude API 密钥，用于访问 Anthropic 的 Claude 模型服务。获取方法参考 [Claude Developer Platform](<https://console.anthropic.com/settings/keys>)。​  
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT​| OpenTelemetry SDK 的数据上报地址，固定为 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。​  
OTEL_EXPORTER_OTLP_HEADERS​| OpenTelemetry SDK 数据上报的认证头信息，包括以下参数：​

  * cozeloop-workspace-id：扣子罗盘的工作空间 ID。获取方法参考 ​获取扣子罗盘空间 ID。​

  * Authorization：扣子罗盘的个人访问令牌或服务访问令牌，获取方法参考 ​配置个人访问令牌 或 ​配置服务访问令牌。​

  
  
​

步骤二：上报 Trace​

初始化 OpenTelemetry SDK 并接入 OpenInference 的 openinference-instrumentation-claude-agent-sdk，即可让 Claude Agent SDK 的 query() 方法在执行时自动生成 AGENT 和 TOOL 类型的 span。​

说明

在 ESM 环境下，由于 import * as xxx 导入的模块是只读的，直接对其进行修补（patch）会失败。因此，你需要先创建一个可变副本（例如 const ClaudeAgentSDK = { ...ClaudeAgentSDKModule }），然后再对其调用 manuallyInstrument()。​

此外，你必须在进程退出前调用 await sdk.shutdown()，以确保 BatchSpanProcessor 能将所有缓存的 Span 数据成功上报至扣子罗盘，避免数据丢失。​

​

​

TypeScript

复制

import { createRequire } from "node:module";​

const require = createRequire(import.meta.url);​

​

const { NodeSDK } = require("@opentelemetry/sdk-node");​

const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");​

const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");​

const { resourceFromAttributes } = require("@opentelemetry/resources");​

​

const { ClaudeAgentSDKInstrumentation } = require(​

"@arizeai/openinference-instrumentation-claude-agent-sdk"​

);​

​

import * as ClaudeAgentSDKModule from "@anthropic-ai/claude-agent-sdk";​

​

// 1) exporter​

const exporter = new OTLPTraceExporter({ timeoutMillis: 10000 });​

​

// 2) ESM：复制一份可变对象，方便 instrumentation 覆写导出函数​

const ClaudeAgentSDK = { ...ClaudeAgentSDKModule };​

​

const instrumentation = new ClaudeAgentSDKInstrumentation({​

// 可选：隐藏输入输出，避免敏感信息上报​

// traceConfig: { hideInputs: true, hideOutputs: true },​

});​

​

instrumentation.manuallyInstrument(ClaudeAgentSDK);​

​

// 3) NodeSDK​

const sdk = new NodeSDK({​

resource: resourceFromAttributes({​

// 建议设置成可识别的服务名，便于在 Trace 页面筛选​

"service.name": "claude-agent-cozeloop-demo",​

}),​

spanProcessors: [new BatchSpanProcessor(exporter)],​

instrumentations: [instrumentation],​

});​

​

sdk.start();​

​

// 4) 使用被 patch 过的 query​

const { query } = ClaudeAgentSDK;​

​

for await (const message of query({​

prompt: "Hello, introduce yourself.",​

options: {​

model: "claude-sonnet-4-5-20250929",​

},​

})) {​

// ...你的业务处理​

}​

​

// 5) 关闭时确保 flush​

await sdk.shutdown();​

​

（可选）CommonJS 项目的自动埋点​

如果你的项目采用 CommonJS 规范（例如使用 require() 语句或 type 语句，而不是 module 语句 ），可以参考 ClaudeAgentSDKInstrumentation 的自动埋点用法：​

​

TypeScript

复制

const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");​

const {​

ClaudeAgentSDKInstrumentation,​

} = require("@arizeai/openinference-instrumentation-claude-agent-sdk");​

​

const provider = new NodeTracerProvider();​

provider.register();​

​

const instrumentation = new ClaudeAgentSDKInstrumentation();​

instrumentation.setTracerProvider(provider);​

​

上报自定义节点​

如果你希望在 Trace 调用树中添加自定义的业务节点（例如输入预处理、数据检索、外部依赖调用等），可以通过手动创建 Span 来实现。手动创建的 Span 将与自动上报的 AGENT 和 TOOL Span 串联，形成一棵完整的调用树。​

​

TypeScript

复制

const { trace } = require("@opentelemetry/api");​

​

const tracer = trace.getTracer("claude-agent-cozeloop-demo");​

​

await tracer.startActiveSpan("root_span", async (span) => {​

span.setAttribute("cozeloop.span_type", "custom");​

span.setAttribute("biz.scene", "weather_demo");​

​

try {​

// 这里调用 ClaudeAgentSDK.query(...)​

} finally {​

span.end();​

}​

});​

​

自定义 span 的 attribute/event 建议遵循扣子罗盘的字段映射规范 [OpenTelemetry 字段映射](<https://loop.coze.cn/open/docs/cozeloop/opentelemetry_field_mapping>)。​

步骤三：查看 Trace​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并单击目标 Span，查看上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272940%27%20height=%271332.295081967213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0MCIgaGVpZ2h0PSIxMzMyLjI5NTA4MTk2NzIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

更多示例​

关于上报 Claude Agent SDK（Node.js）Trace 数据的更多示例，参考 [claude_agent](<https://github.com/coze-dev/cozeloop-examples/tree/main/js/integration/framework/claude_agent>)。​

​

上一篇

Claude Agent SDK (Python)

下一篇

CrewAI