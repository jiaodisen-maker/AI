---
source_url: https://docs.coze.cn/cozeloop/opentelemetry_sdk_trace_report
title: '通过 OpenTelemetry SDK 上报 Trace - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:49Z
---

# 通过 OpenTelemetry SDK 上报 Trace - 文档 - 扣子

通过 OpenTelemetry SDK 上报 Trace

本文介绍如何通过 [OpenTelemetry Python SDK](<https://opentelemetry.io/docs/languages/python/>) 上报 Trace 数据到扣子罗盘。​

功能介绍​

你可以使用各种语言的 OpenTelemetry SDK 将 Trace 数据上报到扣子罗盘。通过OpenTelemetry SDK 上报时，开发者需要直接在代码中引入 OpenTelemetry SDK 来创建和管理 Trace 数据（例如创建 Span、设置 Attribute、记录 Event 等）。​

本文以 Python SDK 为例，介绍如何通过 OpenTelemetry  SDK将应用程序的 Trace 数据上报至扣子罗盘平台，从而实现对应用程序性能和行为的高效监控与分析。​

准备工作​

使用 OpenTelemetry Python SDK 前，需要先安装 Python SDK 以及相关的依赖库。​

1.

安装 Python SDK。​

  * Opentelemetry Python SDK 要求 Python 3.9 或以上版本。你可以通过如下方法查看 Python 版本 。​

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

安装依赖库。​

  * 安装 Python 依赖库，分别用于调用 AI 模型、对调用过程进行可观测性管理以及将 Trace 数据导出到后端系统。​

  * ​

Python

复制

pip install openai​

pip install opentelemetry-sdk​

pip install opentelemetry-exporter-otlp​

​

配置环境变量​

在上报 Trace 数据前，你需要正确配置 OpenTelemetry 的环境变量 OTEL_EXPORTER_OTLP_HEADERS 和 OTEL_EXPORTER_OTLP_TRACES_ENDPOINT，用于指定上报数据时所需的扣子罗盘空间 ID，访问令牌和上报地址，以确保数据能够正确发送到指定的扣子罗盘空间中。环境变量配置格式及说明如下：​

​

Python

复制

OTEL_EXPORTER_OTLP_HEADERS=cozeloop-workspace-id={CozeLoop空间ID},Authorization=Bearer {个人访问令牌或服务访问令牌}​

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.coze.cn/v1/loop/opentelemetry/v1/traces​

​

​

环境变量​| 说明​  
---|---  
OTEL_EXPORTER_OTLP_HEADERS​| 用于设置上报数据时所需的扣子罗盘认证信息和工作空间标识。包括如下参数：​

  * cozeloop-workspace-id：配置为扣子罗盘工作空间 ID。获取空间 ID 的步骤，请参考​获取扣子罗盘工作空间 ID。​

  * Authorization：配置为扣子罗盘的个人访问令牌或服务访问令牌，获取访问令牌的步骤，请参考​配置个人访问令牌、​配置服务访问令牌。​

  
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT​| 用于指定 OpenTelemetry 数据的上报地址，固定为 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。​  
  
​

上报 Trace​

完成上述配置后，你可以使用 OpenAI SDK 调用 AI 模型进行对话，并通过 OpenTelemetry Python SDK 上报 Trace 数据到扣子罗盘。本文以调用火山方舟的 doubao-1-5-vision-pro-32k-250115 模型为例，展示如何通过 OpenTelemetry 记录并上报调用 AI 模型过程中的各种信息，包括输入参数、输出结果、调用耗时等，从而实现对 AI 模型调用过程的全面监控和分析。​

示例代码及重要字段说明如下：​

  * api_key：火山方舟模型的 API Key。获取步骤，请参考[API Key 管理](<https://www.volcengine.com/docs/82379/1361424>)。​

  * model：火山方舟模型的 ID。获取步骤，请参考[获取 Model ID](<https://www.volcengine.com/docs/82379/1399008#_2-获取-model-id>)。在调用火山方舟模型前，你需要先开通对应的模型。​

  * call_model：Span 名称，请根据实际情况修改。​

​

Python

复制

client = OpenAI(api_key={填写你的API_KEY}, base_url="https://ark.cn-beijing.volces.com/api/v3")​

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

def call_model():​

model = "doubao-1-5-vision-pro-32k-250115"​

with tracer.start_as_current_span("call_model") as span:​

span.set_attribute("cozeloop.span_type", "model")​

span.set_attribute("session.id", "thread-1")​

span.set_attribute("user.id", "user-1")​

span.set_attribute("messaging.message.id", "message-1")​

span.set_attribute("error.message", "mock error")​

​

span.set_attribute("gen_ai.system", "ark")​

span.set_attribute("gen_ai.operation.name", "chat")​

span.set_attribute("gen_ai.request.model", model)​

span.set_attribute("llm.request.type", "chat")​

span.set_attribute("gen_ai.request.temperature", 0.6)​

​

messages = [​

{"role": "system", "content": "你是一个专业的沟通师，擅长解答科普知识，回答不要超过100个字."},​

{​

"role": "user",​

"content": "月球离地球有多远."​

}​

]​

​

for i, message in enumerate(messages):​

span.set_attribute(f"gen_ai.prompt.{i}.content", str(message["content"]))​

span.set_attribute(f"gen_ai.prompt.{i}.role", str(message["role"]))​

​

completion = client.chat.completions.create(​

model=model,​

messages=messages​

)​

​

span.set_attribute("gen_ai.completion.0.content", str(completion.choices[0].message.content))​

span.set_attribute("gen_ai.completion.0.role", "assistant")​

span.set_attribute("gen_ai.usage.input_tokens", completion.usage.prompt_tokens)​

span.set_attribute("gen_ai.usage.output_tokens", completion.usage.completion_tokens)​

​

# little_span是span的子节点​

with tracer.start_as_current_span("after_call_model") as little_span:​

time.sleep(1) # 模拟一些操作​

little_span.set_attribute("process_result", "bad")​

little_span.add_event("exception", {​

"exception.message": "mock error message",​

"exception.stacktrace": "mock error stacktrace"​

})​

​

return completion​

​

if __name__ == "__main__":​

call_model()​

​

验证结果​

OpenTelemetry Python SDK 上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并单击目标 Span，查看上报的 Trace 数据。例如下图的 Trace 数据展示了模型交互全流程与详情：系统设定了一个专业沟通师、擅长科普的角色，当用户向大模型提问月球离地球有多远时 ，由ark 提供的doubao-1-5-vision-pro-32k-250115模型成功响应，涉及 279 个 Token，输出了详细科普内容。整个调用流程含 call_model（7.85 秒 ）及后续 after_call_model（1.00 秒 ）环节。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27377%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjM3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

OpenTelemetry Trace

下一篇

OpenTelemetry 字段映射