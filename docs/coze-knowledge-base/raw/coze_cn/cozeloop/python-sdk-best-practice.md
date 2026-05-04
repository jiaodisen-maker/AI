---
source_url: https://docs.coze.cn/cozeloop/python-sdk-best-practice
title: '最佳实践 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:16Z
---

# 最佳实践 - 文档 - 扣子

最佳实践

本教程以一个旅游助手为例，介绍如何使用 Python 集成扣子罗盘 SDK 实现对旅游助手的全链路追踪，从用户输入到模型响应的全过程。 在本教程中，你需要先在扣子罗盘控制台中编写 Prompt，并通过扣子罗盘 SDK 拉取 Prompt 并调用模型，然后就能在控制台中查看 SDK 上报的 Trace 数据。​

步骤一：编写 Prompt ​

为了方便演示，本教程以 CozeLoop Demo 空间中的[旅行专家](<https://loop.coze.cn/console/enterprise/personal/space/7487806534651887643/pe/prompts/7490479658761207820>)为例。​

以下是旅行助手的 Prompt 示例。你也可以根据实际需求，开发一个 Prompt 并提交版本，详情请参考​开发提示词。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272794%27%20height=%271290.795321637427%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0caf1641ecdc4232adf70a8647f0d1d6~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：上报数据​

以下代码展示了如何使用扣子罗盘实现完整的链路追踪，从用户输入到模型响应的全过程。​

1.

主流程（main）：​

  * 初始化 CozeLoop 客户端，启用 Prompt 追踪​

  * 创建 root span 追踪整个请求链路​

  * 获取并格式化旅行专家 Prompt​

  * 调用大模型获取响应​

  * 记录输出结果并完成追踪​

2.

模型调用（callLLM）：​

  * 创建专门的 Model Span​

  * 配置火山引擎（VolcEngine）的模型调用参数​

  * 记录完整的调用上下文：​

  * 输入信息（提示词）​

  * 模型配置（提供商、模型名称、参数）​

  * Prompt 信息​

  * 追踪模型响应和性能指标（Token 使用量）​

​

Python

复制

import os​

​

import cozeloop​

from cozeloop.spec import tracespec​

from openai import OpenAI​

from openai.types.chat import ChatCompletionSystemMessageParam​

​

def main():​

# 初始化cozeloop client​

client = cozeloop.new_client(prompt_trace=True)​

​

# 准备用户输入​

input = {"people_num": "2", "destination": "上海", "days_num": "5", "travel_theme": "自由行"}​

​

# 创建root span​

root = cozeloop.start_span("旅行专家", "chain")​

root.set_input(input)​

​

try:​

# 拉取Prompt​

prompt = client.get_prompt(prompt_key="CozeLoop_Travel_Master")​

cozeloop_messages = client.prompt_format(prompt, input)​

messages = [​

ChatCompletionSystemMessageParam(​

role="system",​

content=cozeloop_messages[0].content​

)​

]​

​

# 调用大模型​

response = call_llm(​

messages=messages,​

prompt=prompt,​

)​

​

# 处理最终结果​

final_output = response.choices[0].message.content​

root.set_output(final_output)​

​

finally:​

# root span 上报​

root.finish()​

​

# 服务退出前调用Close方法，否则可能造成trace数据丢失​

client.close()​

​

def call_llm(messages, prompt):​

# 创建model span​

model_span = cozeloop.start_span("CallLLM", "model")​

​

ark_client = OpenAI(​

base_url="https://ark.cn-beijing.volces.com/api/v3",​

api_key=os.environ.get("OPENAI_API_KEY")​

)​

temperature = 0.7​

max_tokens = 1000​

​

try:​

# 设置模型参数​

model_span.set_input({"messages": messages})​

model_span.set_model_provider("volcengine")​

model_span.set_model_name("doubao-1-5-vision-pro-32k-250115")​

model_span.set_model_call_options(tracespec.ModelCallOption(​

temperature=temperature,​

max_tokens=max_tokens​

))​

model_span.set_prompt(prompt=prompt)​

​

# 执行模型调用​

response = ark_client.chat.completions.create(​

model="doubao-1-5-vision-pro-32k-250115",​

messages=messages,​

temperature=temperature,​

max_tokens=max_tokens​

)​

​

model_span.set_output(response)​

model_span.set_input_tokens(response.usage.prompt_tokens)​

model_span.set_output_tokens(response.usage.completion_tokens)​

​

return response​

except Exception as e:​

model_span.set_error(e)​

raise​

finally:​

model_span.finish()​

​

if __name__ == '__main__':​

main()​

​

步骤三：查看 Trace 数据​

在完成数据上报后，就可以在扣子罗盘的观测页面查看 SDK 上报的 Trace 数据了。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271280%27%20height=%27793.4502923976607%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4MCIgaGVpZ2h0PSI3OTMuNDUwMjkyMzk3NjYwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

快速开始

下一篇

通过版本标识拉取 Prompt 版本