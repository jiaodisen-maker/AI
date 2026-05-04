---
source_url: https://docs.coze.cn/cozeloop/openai_chat_trace_report
title: 'OpenAI Chat & Responses - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:35Z
---

# OpenAI Chat & Responses - 文档 - 扣子

OpenAI Chat & Responses

本文介绍如何通过扣子罗盘 SDK 提供的 Client Wrapper 将 OpenAI 模型调用过程的 Trace 数据自动上报到扣子罗盘。 ​

说明

本集成方案与 Low-Level 上报、注解上报完全兼容，能够无缝集成在同一 Trace 调用树中。​

​

功能介绍​

扣子罗盘 SDK 提供了针对 OpenAI Chat & Responses 接口的客户端封装器（Client Wrapper）。开发者只需简单集成，即可将模型调用的 Trace 数据自动采集与上报到扣子罗盘，完成可视化分析。​

配置环境变量 ​

在上报 Trace 数据前，你需要正确配置环境变量，以确保 OpenAI Chat 应用能够正常调用 OpenAI 模型，并能正确发送 Trace 数据到指定的扣子罗盘空间中。环境变量配置格式及说明如下： ​

​

环境变量​| 说明​  
---|---  
COZELOOP_API_TOKEN ​| 设置上报数据时所需的扣子罗盘认证信息，即配置为扣子罗盘的个人访问令牌或服务访问令牌。获取步骤，请参考​配置个人访问令牌、​配置服务访问令牌。​  
COZELOOP_WORKSPACE_ID ​| 配置为扣子罗盘工作空间 ID。获取步骤，请参考​获取扣子罗盘工作空间 ID。​  
OPENAI_BASE_URL​| 配置 OpenAI 模型的服务地址。​

  * 推荐使用方舟模型，其 BASE_URL 固定为 https://ark.cn-beijing.volces.com/api/v3。​

  * 使用其他 OpenAI 模型时，配置为其对应的 BASE_URL 即可。​

  
OPENAI_API_KEY​| 配置 OpenAI 模型的 API Key。​

  * 推荐使用方舟模型，其 API Key 获取步骤，请参考 [API Key 管理](<https://www.volcengine.com/docs/82379/1361424>)。​

  * 使用其他 OpenAI 模型时，配置为其对应的 API Key 即可。​

  
OPENAI_MODEL_NAME​| 配置 OpenAI 模型名称。​  
  
​

上报 Trace​

完成上述配置后，你可以调用 OpenAI 模型开展 AI 对话，并通过扣子罗盘 SDK 上报 Trace 数据到扣子罗盘。​

本示例构建了一个基于 RAG 技术的问答程序。该程序通过检索函数获取与问题相关的上下文信息，并在 OpenAI Chat 模式中调用 AI 模型生成回答。同时，通过扣子罗盘 SDK，自动采集并上报执行过程中的 Trace 数据到扣子罗盘，从而实现对 AI 模型调用过程的全面监控和分析。​

说明

本示例以 OpenAI Chat 功能为例，如果需要使用 responses 接口，只需改为 responses.create 方法，详情请参考​支持的具体方法。​

​

​

Python

复制

import os​

​

from openai import OpenAI​

​

from cozeloop import new_client​

from cozeloop.decorator import observe​

from cozeloop.integration.wrapper import openai_wrapper​

​

​

base_url = os.environ.get('OPENAI_BASE_URL')​

api_key = os.environ.get('OPENAI_API_KEY')​

model_name = os.environ.get('OPENAI_MODEL_NAME')​

​

​

openai_client = openai_wrapper(OpenAI(​

base_url=base_url, # use ark model, refer: https://www.volcengine.com/docs/82379/1361424​

api_key=api_key,​

))​

​

def retriever():​

results = ["John worked at Beijing"]​

return results​

​

# 使用注解上报​

@observe​

def rag(question):​

docs = retriever()​

system_message = """Answer the question using only the provided information below:​

​

{docs}""".format(docs="\n".join(docs))​

​

# not stream​

# res = openai_client.chat.completions.create( # chat completion​

# messages=[​

# {"role": "system", "content": system_message},​

# {"role": "user", "content": question},​

# ],​

# model=model_name,​

# )​

# print(res)​

​

# stream​

res = openai_client.chat.completions.create( # chat completion​

messages=[​

{"role": "system", "content": system_message},​

{"role": "user", "content": question},​

],​

model=model_name,​

stream=True,​

extra_body={​

"stream_options": {​

"include_usage": True # ark model, return token usage by this param​

}​

}​

)​

for chunk in res:​

print(chunk)​

​

​

if __name__ == '__main__':​

# Set the following environment variables first (Assuming you are using a PAT token.).​

# os.environ["COZELOOP_WORKSPACE_ID"] = "your workspace id"​

# os.environ["COZELOOP_API_TOKEN"] = "your token"​

​

client = new_client()​

rag("Where is John worked?")​

client.flush()​

​

查看 Trace​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并单击目标 Span，查看上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27730%27%20height=%27387%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzMwIiBoZWlnaHQ9IjM4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

支持的具体方法​

​

client 类别​| 方法​| 非流式​| 流式​  
---|---|---|---  
OpenAI​| chat.completions.create​| 支持​| 支持​  
AsyncOpenAI​| async chat.completions.create​| 支持​| 支持​  
AzureOpenAI​| chat.completions.create​| 支持​| 支持​  
AsyncAzureOpenAI​| async chat.completions.create​| 支持​| 支持​  
OpenAI​| responses.create​| 支持​| 支持​  
AsyncOpenAI​| async responses.create​| 支持​| 支持​  
AzureOpenAI​| responses.create​| 支持​| 支持​  
AsyncAzureOpenAI​| async responses.create​| 支持​| 支持​  
  
​

更多示例​

关于上报 OpenAI Trace 数据的更多示例，请参考 [OpenAI](<https://github.com/coze-dev/cozeloop-python/tree/main/examples/trace/wrapper_openai>)。​

​

上一篇

扣子智能体

下一篇

LiteLLM Proxy