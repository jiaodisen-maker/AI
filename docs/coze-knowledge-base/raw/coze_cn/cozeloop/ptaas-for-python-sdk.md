---
source_url: https://docs.coze.cn/cozeloop/ptaas-for-python-sdk
title: '调用 Prompt - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:21Z
---

# 调用 Prompt - 文档 - 扣子

调用 Prompt

扣子罗盘 SDK 支持调用预定义的 Prompt 来与 AI 模型交互，文档介绍如何通过 Python SDK 实现这一功能。​

场景介绍​

通过扣子罗盘 Python SDK 调用预定义的 Prompt 模板时，可以选择以下两种调用方式：​

  * 非流式调用（nonStream）：一次性获取完整的 AI 响应结果。​

  * 流式调用（stream）：逐段获取 AI 的响应内容，类似实时对话的打字效果。​

准备工作​

  * 已集成 0.1.13 及以上版本的扣子罗盘 Python SDK。​

  * 已创建 Prompt 模板并提交版本。操作步骤可参考​开发提示词。​

  * 获取以下配置信息：​

  * COZELOOP_WORKSPACE_ID：扣子罗盘 Prompt 所在工作空间的 ID。你可以在 Prompt 详情页 URL 的 space 关键词之后获取工作空间 ID，例如 https://loop.coze.cn/console/enterprise/personal/space/73917415734092****/pe/prompts/75115667262537**** 中，73917415734092****为工作空间 ID。​

  * COZELOOP_API_TOKEN：扣子罗盘访问密钥，应具备 executePrompt 权限。获取密钥及授权方式可参考​SDK 鉴权。​

示例代码​

以下示例代码演示如何通过扣子罗盘 Python SDK 调用一个预定义的 Prompt 模板。调用模板时传入具体参数，然后获取 AI 模型对 "解释机器学习" 这个问题的简短回答，同时演示了同步获取完整结果和异步流式获取结果两种方式。​

关于调用 Prompt 的更多使用示例，例如指定版本标识执行 Prompt、多模态 Prompt、传递 Prompt 变量、超时设置等，可参考 [Github](<https://github.com/coze-dev/cozeloop-python/tree/main/examples/prompt/ptaas>)。 ​

​

Python

复制

import asyncio​

import os​

​

from cozeloop import new_client, Client​

from cozeloop.entities.prompt import Message, Role, ExecuteResult​

​

​

def setup_client() -> Client:​

"""​

Unified client setup function​

​

Environment variables:​

\- COZELOOP_WORKSPACE_ID: workspace ID​

\- COZELOOP_API_TOKEN: API token​

"""​

# Set the following environment variables first.​

# COZELOOP_WORKSPACE_ID=your workspace id​

# COZELOOP_API_TOKEN=your token​

client = new_client(​

workspace_id=os.getenv("COZELOOP_WORKSPACE_ID"),​

api_token=os.getenv("COZELOOP_API_TOKEN"),​

)​

return client​

​

​

def print_execute_result(result: ExecuteResult) -> None:​

"""Unified result printing function, consistent with Go version format"""​

if result.message:​

print(f"Message: {result.message}")​

if result.finish_reason:​

print(f"FinishReason: {result.finish_reason}")​

if result.usage:​

print(f"Usage: {result.usage}")​

​

​

def sync_non_stream_example(client: Client) -> None:​

"""Sync non-stream call example"""​

print("=== Sync Non-Stream Example ===")​

​

# 1. Create a prompt on the platform​

# Create a Prompt on the platform's Prompt development page (set Prompt Key to 'ptaas_demo'),​

# add the following messages to the template, submit a version.​

# System: You are a helpful assistant for {{topic}}.​

# User: Please help me with {{user_request}}​

​

result = client.execute_prompt(​

prompt_key="ptaas_demo",​

version="0.0.1",​

variable_vals={​

"topic": "artificial intelligence",​

"user_request": "explain what is machine learning"​

},​

# You can also append messages to the prompt.​

messages=[​

Message(role=Role.USER, content="Keep the answer brief.")​

],​

stream=False​

)​

print_execute_result(result)​

​

​

def sync_stream_example(client: Client) -> None:​

"""Sync stream call example"""​

print("=== Sync Stream Example ===")​

​

stream_reader = client.execute_prompt(​

prompt_key="ptaas_demo",​

version="0.0.1",​

variable_vals={​

"topic": "artificial intelligence",​

"user_request": "explain what is machine learning"​

},​

messages=[​

Message(role=Role.USER, content="Keep the answer brief.")​

],​

stream=True​

)​

​

for result in stream_reader:​

print_execute_result(result)​

​

print("\nStream finished.")​

​

​

async def async_non_stream_example(client: Client) -> None:​

"""Async non-stream call example"""​

print("=== Async Non-Stream Example ===")​

​

result = await client.aexecute_prompt(​

prompt_key="ptaas_demo",​

version="0.0.1",​

variable_vals={​

"topic": "artificial intelligence",​

"user_request": "explain what is machine learning"​

},​

messages=[​

Message(role=Role.USER, content="Keep the answer brief.")​

],​

stream=False​

)​

print_execute_result(result)​

​

​

async def async_stream_example(client: Client) -> None:​

"""Async stream call example"""​

print("=== Async Stream Example ===")​

​

stream_reader = await client.aexecute_prompt(​

prompt_key="ptaas_demo",​

version="0.0.1",​

variable_vals={​

"topic": "artificial intelligence",​

"user_request": "explain what is machine learning"​

},​

messages=[​

Message(role=Role.USER, content="Keep the answer brief.")​

],​

stream=True​

)​

​

async for result in stream_reader:​

print_execute_result(result)​

​

print("\nStream finished.")​

​

​

async def main():​

"""Main function"""​

client = setup_client()​

​

try:​

# Sync non-stream call​

sync_non_stream_example(client)​

​

# Sync stream call​

sync_stream_example(client)​

​

# Async non-stream call​

await async_non_stream_example(client)​

​

# Async stream call​

await async_stream_example(client)​

​

finally:​

# Close client​

if hasattr(client, 'close'):​

client.close()​

​

​

if __name__ == "__main__":​

asyncio.run(main())​

​

上一篇

通过版本标识拉取 Prompt 版本

下一篇

快速开始