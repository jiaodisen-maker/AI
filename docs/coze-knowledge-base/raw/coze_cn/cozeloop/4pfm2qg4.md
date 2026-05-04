---
source_url: https://docs.coze.cn/cozeloop/4pfm2qg4
title: 'Instructor - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:10Z
---

# Instructor - 文档 - 扣子

Instructor

本文介绍如何使用 Coze Loop SDK 将 [Instructor](<https://python.useinstructor.com/>) 的 Trace 数据自动上报到扣子罗盘。​

功能介绍​

Instructor 是一个基于 Pydantic 的库，旨在简化 LLM 的结构化数据提取。结合 Coze Loop SDK，你可以全面追踪 Instructor 的数据提取过程。Trace 数据将被上报至扣子罗盘，实现完整的可观测性监控。​

准备工作​

你需要先安装以下 Python 库：​

  * instructor：Instructor 核心库。​

  * openai：OpenAI Python SDK，用于调用所有符合 OpenAI API 标准协议的 LLM。​

  * pydantic：Pydantic 数据验证库。通过 Pydantic，你可以使用 Python 类型提示进行数据验证。​

  * cozeloop：Coze Loop SDK，用于把 Trace 数据上报到扣子罗盘。​

​

Python

复制

pip install instructor​

pip install openai​

pip install pydantic​

pip install cozeloop​

​

操作步骤​

步骤一：配置环境变量​

在上报 Trace 数据前，你需要正确配置环境变量，以确保 Trace 数据能够正确发送到指定的扣子罗盘空间中。环境变量配置格式及说明如下：​

​

Python

复制

COZELOOP_API_TOKEN=***​

COZELOOP_WORKSPACE_ID=***​

OPENAI_BASE_URL=***​

OPENAI_API_KEY=***​

OPENAI_MODEL_NAME=***​

​

​

环境变量​| 说明​  
---|---  
COZELOOP_API_TOKEN​| 用于设置上报数据时所需的扣子罗盘认证信息，配置为扣子罗盘的个人访问令牌或服务访问令牌，获取方法参考​配置个人访问令牌或​配置服务访问令牌。​  
COZELOOP_WORKSPACE_ID​| 配置为扣子罗盘工作空间 ID。获取方法参考​获取扣子罗盘空间 ID。​  
OPENAI_BASE_URL​| 配置 OpenAI 模型服务的 Base URL。推荐使用火山方舟模型服务：https://ark.cn-beijing.volces.com/api/v3。​  
OPENAI_API_KEY​| 配置 OpenAI 模型服务的 API Key。如果使用火山方舟模型，请参考 [获取 API Key](<https://www.volcengine.com/docs/82379/1361424>)。​  
OPENAI_MODEL_NAME​| 模型名称，例如 openai/doubao-1-5-pro-256k-250115。使用模型提供方作为前缀，例如 openai/。​  
  
​

步骤二：上报 Trace​

你可以使用 Coze Loop SDK 将 Trace 数据上报至扣子罗盘。​

下方的示例代码演示如何通过 Coze Loop SDK 追踪 Instructor 的运行状态并将 Trace 数据上报到扣子罗盘。openai_wrapper 是 Coze Loop SDK 提供的封装库，用于简化与 OpenAI API 的交互。你可以通过 openai_wrapper 来调用符合 OpenAI API 标准协议的 LLM，并上报 LLM 调用过程的 Trace 数据到扣子罗盘。​

​

Python

复制

import os​

from pydantic import BaseModel​

from openai import OpenAI​

import instructor​

from cozeloop import new_client​

from cozeloop.decorator import observe​

from cozeloop.integration.wrapper import openai_wrapper​

​

# OpenAI env​

os.environ['OPENAI_BASE_URL'] = 'https://ark.cn-beijing.volces.com/api/v3' # use ark model url by default, from https://www.volcengine.com/docs/82379/1361424​

os.environ['OPENAI_API_KEY'] = '***' # your api key​

os.environ['OPENAI_MODEL_NAME'] = '***' # your model name, like doubao-1-5-vision-pro-32k-250115​

​

# cozeloop client init​

# Set the following environment variables first:​

# os.environ["COZELOOP_WORKSPACE_ID"] = "your workspace id"​

# os.environ["COZELOOP_API_TOKEN"] = "your pat or sat token"​

cozeloop_client = new_client()​

​

# Wrap OpenAI client with cozeloop's openai_wrapper to enable tracing.​

# This ensures that LLM calls are captured by cozeloop.​

# Then patch the wrapped client with instructor for structured data extraction.​

patched_openai_client = openai_wrapper(OpenAI(​

api_key=os.environ.get('OPENAI_API_KEY'),​

base_url=os.environ.get('OPENAI_BASE_URL'),​

))​

client = instructor.patch(patched_openai_client)​

​

class UserDetail(BaseModel):​

name: str​

age: int​

​

@observe(span_type="workflow") # Customizing the span type​

def extract_user_info(text: str):​

"""​

This function is decorated with @observe, which creates a span in cozeloop.​

The nested LLM call via 'client.chat.completions.create' will be captured ​

by the 'openai_wrapper' and associated with this span.​

"""​

user = client.chat.completions.create(​

model=os.environ.get('OPENAI_MODEL_NAME'),​

response_model=UserDetail,​

messages=[​

{"role": "user", "content": text},​

],​

)​

return user​

​

def main():​

# Example of a manual root span for even more control over the trace hierarchy.​

with cozeloop_client.start_span("Instructor_Root_Process", "root") as root_span:​

input_text = "Jason is 25 years old"​

root_span.set_input(input_text)​

​

print(f"Extracting info from: {input_text}")​

user_info = extract_user_info(input_text)​

​

print(f"Extracted info: {user_info}")​

root_span.set_output(user_info.model_dump_json())​

​

# Ensure all spans are sent to cozeloop​

cozeloop_client.flush()​

​

if __name__ == "__main__":​

main()​

​

自定义 Span​

Coze Loop SDK 的 openai_wrapper 会自动生成 Span。同时，你也可以使用 Coze Loop SDK 自定义 Span。​

示例代码演示了如何使用 Coze Loop SDK 自定义 Span。Coze Loop SDK 自动生成的 Span 会与你自定义的 Span 自动关联，并显示在同一条 Trace 中。示例代码中使用了以下方式自定义 Span：​

  * 使用@observe注解自定义了类型为 workflow 的 Span。@observe注解所对应的方法中包含的 LLM 调用会与这个自定义 Span 关联。​

  * 调用 cozeloop_client.start_span() 手动创建一个自定义 Span 作为 Root Span。​

​

Python

复制

@observe(span_type="workflow") # Customizing the span type​

def extract_user_info(text: str):​

"""​

This function is decorated with @observe, which creates a span in cozeloop.​

The nested LLM call via 'client.chat.completions.create' will be captured ​

by the 'openai_wrapper' and associated with this span.​

"""​

user = client.chat.completions.create(​

model=os.environ.get('OPENAI_MODEL_NAME'),​

response_model=UserDetail,​

messages=[​

{"role": "user", "content": text},​

],​

)​

return user​

​

def main():​

# Example of a manual root span for even more control over the trace hierarchy.​

with cozeloop_client.start_span("Instructor_Root_Process", "root") as root_span:​

input_text = "Jason is 25 years old"​

root_span.set_input(input_text)​

​

print(f"Extracting info from: {input_text}")​

user_info = extract_user_info(input_text)​

​

print(f"Extracted info: {user_info}")​

root_span.set_output(user_info.model_dump_json())​

​

# Ensure all spans are sent to cozeloop​

cozeloop_client.flush()​

​

步骤三：验证结果​

上报 Trace 数据后，你可以在[扣子罗盘](<https://loop.coze.cn/>)的 Trace 页面，找到并查看 Instructor 上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272946%27%20height=%271441.953161592506%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0NiIgaGVpZ2h0PSIxNDQxLjk1MzE2MTU5MjUwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例地址​

要获取上报 Trace 数据的完整示例代码，参考 [instructor](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/integration/framework/instructor>)。​

​

​

上一篇

Google ADK

下一篇

LangChain & LangGraph & DeepAgents