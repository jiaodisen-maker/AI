---
source_url: https://docs.coze.cn/cozeloop/litellm_sdk_trace_report
title: 'LiteLLM SDK - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:15Z
---

# LiteLLM SDK - 文档 - 扣子

LiteLLM SDK

本文介绍如何将 [LiteLLM SDK](<https://docs.litellm.ai/docs/#litellm-python-sdk>) 运行过程的 Trace 数据自动上报到扣子罗盘。​

本文适用于 LiteLLM SDK，如果你需要上报 LiteLLM Proxy 的 Trace 数据，请参考 ​LiteLLM Proxy。​

功能介绍​

[LiteLLM](<https://docs.litellm.ai/docs/>) 是一款开源的 Proxy 和 SDK。它提供了统一的 API 接口，能够兼容 OpenAI 的 Endpoint，实现对数百家大语言模型提供商及旗下模型的统一调用与管理。​

LiteLLM SDK 能够与 OpenTelemetry 集成，自动捕获 LiteLLM SDK 运行过程中的关键操作和性能指标，并将这些数据作为 Trace 数据上报到扣子罗盘，完成可视化分析。本集成方案适用于监控 LiteLLM SDK 调用 AI 模型过程、排查调用问题的场景。​

本文以 Python SDK 为例，介绍如何通过 OpenTelemetry SDK 将 Trace 数据上报至扣子罗盘平台，从而实现对应用程序性能和行为的高效监控与分析。​

准备工作 ​

使用 OpenTelemetry Python SDK 前，需要先安装 Python SDK 以及相关的依赖库。 ​

1.

安装 Python SDK。 ​

  * Opentelemetry Python SDK 要求 Python 3.9 或以上版本。你可以通过如下方法查看 Python 版本。 ​

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

pip install opentelemetry-exporter-otlp​

pip install openinference-instrumentation-litellm​

pip install litellm​

​

配置环境变量 ​

在上报 Trace 数据前，你需要正确配置 OpenTelemetry 的环境变量，以确保 LiteLLM SDK 能够正常调用 OpenAI 模型，并能正确发送 Trace 数据到指定的扣子罗盘空间中。环境变量配置格式及说明如下： ​

​

Python

复制

OTEL_EXPORTER_OTLP_HEADERS=cozeloop-workspace-id={CozeLoop空间ID},Authorization=Bearer {个人访问令牌或服务访问令牌}​

OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.coze.cn/v1/loop/opentelemetry/v1/traces​

OPENAI_BASE_URL=***​

OPENAI_API_KEY=***​

OPENAI_MODEL_NAME=***​

​

​

环境变量​| 说明​  
---|---  
OTEL_EXPORTER_OTLP_HEADERS ​| 设置上报数据时所需的扣子罗盘认证信息和工作空间标识。包括如下参数： ​

  * cozeloop-workspace-id：配置为扣子罗盘工作空间 ID。获取步骤，请参考​获取扣子罗盘工作空间 ID。​

  * Authorization：配置为扣子罗盘的个人访问令牌或服务访问令牌。获取步骤，请参考​配置个人访问令牌、​配置服务访问令牌。​

  
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT ​| 指定 OpenTelemetry 数据的上报地址，固定为 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。 ​  
OPENAI_BASE_URL​| 配置 OpenAI 模型的服务地址。​

  * 推荐使用方舟模型，其 BASE_URL 固定为 https://ark.cn-beijing.volces.com/api/v3。​

  * 使用其他 OpenAI 模型时，配置为其对应的 BASE_URL 即可。​

  
OPENAI_API_KEY​| 配置 OpenAI 模型的 API Key。​

  * 推荐使用方舟模型，其 API Key 获取步骤，请参考 [API Key 管理](<https://www.volcengine.com/docs/82379/1361424>)。​

  * 使用其他 OpenAI 模型时，配置为其对应的 API Key 即可。​

  
OPENAI_MODEL_NAME​| 配置 OpenAI 模型名称，需使用模型提供方作为前缀。例如 openai/doubao-1-5-pro-256k-250115。​  
  
​

上报 Trace​

完成上述配置后，你可以调用 OpenAI 模型开展 AI 对话，并通过 OpenTelemetry Python SDK 上报 Trace 数据到扣子罗盘。以下示例将分别展示自动上报 Trace 数据与上报自定义 Span 节点数据的具体实现方式。​

自动上报​

在本示例中，使用 LiteLLM 框架调用火山方舟 doubao-1-5-pro-256k-250115 模型完成天气查询功能，并通过 OpenTelemetry SDK 自动收集和上报 OpenAI 模型执行过程中的 Trace 数据到扣子罗盘，包括 LLM 调用、工具执行、请求处理流程等数据，从而实现对 AI 模型调用过程的全面监控和分析。​

​

Python

复制

from time import sleep​

import os​

import json​

from typing import Any, Dict, List, Optional​

​

import litellm​

from opentelemetry import trace​

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter​

from opentelemetry.sdk.trace import TracerProvider # noqa: E402​

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, BatchSpanProcessor​

from openinference.instrumentation.litellm import LiteLLMInstrumentor​

​

# OpenAI env​

os.environ['OPENAI_BASE_URL'] = 'https://ark.cn-beijing.volces.com/api/v3' # use ark model url​

os.environ['OPENAI_API_KEY'] = '***' # your ark api key, from https://www.volcengine.com/docs/82379/1361424​

os.environ['OPENAI_MODEL_NAME'] = 'openai/doubao-1-5-pro-256k-250115' # your model name, use model provider as prefix, like openai/​

​

# OTEL env​

os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = "https://api.coze.cn/v1/loop/opentelemetry/v1/traces" # cozeloop otel endpoint​

os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = "cozeloop-workspace-id=***,Authorization=Bearer ***" # set your 'spaceID' and 'pat or sat token'​

​

# Set up OpenTelemetry tracing​

otlp_exporter = OTLPSpanExporter(​

timeout=10,​

)​

trace.set_tracer_provider(TracerProvider())​

trace.get_tracer_provider().add_span_processor(​

BatchSpanProcessor(otlp_exporter)​

)​

tracer = trace.get_tracer(__name__)​

​

LiteLLMInstrumentor().instrument()​

​

​

def get_current_weather(location: str, unit: str = "fahrenheit") -> str:​

with tracer.start_as_current_span("get_current_weather") as span:​

span.set_attribute("cozeloop.span_type", "tool")​

span.set_attribute("cozeloop.input", json.dumps({"location": location, "unit": unit}))​

​

res = ""​

if "tokyo" in location.lower():​

res = json.dumps({"location": "Tokyo", "temperature": "10", "unit": "celsius"})​

elif "san francisco" in location.lower():​

res = json.dumps({"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"})​

elif "paris" in location.lower():​

res = json.dumps({"location": "Paris", "temperature": "22", "unit": "celsius"})​

else:​

res = json.dumps({"location": location, "temperature": "unknown"})​

span.set_attribute("cozeloop.output", res)​

​

return res​

​

​

def to_dict_message(msg: Any) -> Dict[str, Any]:​

return {​

"role": str(getattr(msg, "role", "")),​

"content": str(getattr(msg, "content", "")),​

}​

​

​

def parallel_function_call() -> None:​

try:​

messages: List[Dict[str, Any]] = [​

{​

"role": "user",​

"content": "What's the weather like in San Francisco, Tokyo, and Paris?",​

}​

]​

tools = [​

{​

"type": "function",​

"function": {​

"name": "get_current_weather",​

"description": "Get the current weather in a given location",​

"parameters": {​

"type": "object",​

"properties": {​

"location": {​

"type": "string",​

"description": "The city and state, e.g. San Francisco, CA",​

},​

"unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},​

},​

"required": ["location"],​

},​

},​

}​

]​

response: Any = litellm.completion(​

base_url=os.environ["OPENAI_BASE_URL"],​

api_key=os.environ["OPENAI_API_KEY"],​

model=os.environ["OPENAI_MODEL_NAME"],​

messages=messages,​

tools=tools,​

tool_choice="auto",​

)​

print("\nFirst LLM Response:\n", response)​

response_message: Any = response.choices[0].message​

tool_calls: Optional[Any] = getattr(response_message, "tool_calls", None)​

​

print("\nLength of tool calls", len(list(tool_calls or [])))​

​

if tool_calls:​

available_functions = {​

"get_current_weather": get_current_weather,​

}​

messages.append(response_message)​

for tool_call in list(tool_calls):​

function_name = getattr(getattr(tool_call, "function", None), "name", None)​

if function_name is None:​

continue​

function_to_call = available_functions[function_name]​

function_args = json.loads(​

getattr(getattr(tool_call, "function", None), "arguments", "{}")​

)​

function_response = function_to_call(​

location=function_args.get("location"),​

unit=function_args.get("unit"),​

)​

messages.append(​

{​

"tool_call_id": getattr(tool_call, "id", ""),​

"role": "tool",​

"name": function_name,​

"content": function_response,​

}​

)​

second_response: Any = litellm.completion(​

base_url=os.environ["OPENAI_BASE_URL"],​

api_key=os.environ["OPENAI_API_KEY"],​

model=os.environ["OPENAI_MODEL_NAME"],​

messages=messages,​

)​

print("\nSecond LLM response:\n", second_response)​

except Exception as e:​

print(f"Error occurred: {e}")​

​

​

if __name__ == "__main__":​

# set custom span, name is root_span​

with tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

​

# start call​

parallel_function_call()​

​

上报自定义节点​

如果你需要上报自定义 Span 节点，可以使用 OpenTelemetry SDK 手动创建 Span 并上报。OpenTelemetry SDK 手动上报的节点数据支持和自动上报的节点数据串联，形成完整的 Trace 调用树。​

自定义的 OpenTelemetry Span，attribute 和 event 规范需遵循 [OpenTelemetry 字段映射](<https://loop.coze.cn/open/docs/cozeloop/opentelemetry_field_mapping>)。​

​

Python

复制

# 设置自定义Span节点 root_span​

with tracer.start_as_current_span("root_span") as span:​

span.set_attribute("cozeloop.span_type", "custom")​

​

# 启动LiteLLM调用​

parallel_function_call()​

​

查看 Trace 数据​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并单击目标 Span，查看上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27684%27%20height=%27339%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg0IiBoZWlnaHQ9IjMzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

更多示例​

关于上报 LiteLLM SDK Trace 数据的更多示例，请参考 [LiteLLM SDK](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/integration/framework/litellm_sdk>)。​

​

上一篇

LlamaIndex

下一篇

OpenAI Agent