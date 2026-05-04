---
source_url: https://docs.coze.cn/cozeloop/python-sdk
title: '快速开始 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:14Z
---

# 快速开始 - 文档 - 扣子

快速开始

本文指导你如何安装并使用扣子罗盘 SDK 进行数据上报。​

说明

扣子罗盘提供多种语言的开发工具包。本教程专注于 Python 语言开发，其他语言的使用说明请参考：​

  * Go：​快速开始​

  * Node.js：​快速开始​

​

准备工作​

环境准备​

扣子罗盘 Python SDK 适用于 Python 3.8 及以上版本。​

安装 Python SDK 之前，执行以下命令确认你已安装 3.8 及以上版本的 Python。 ​

​

Python

复制

# 查看 Python 版本 ​

python --version ​

​

# 回显信息显示已安装 3.8.2 版本 ​

Python 3.8.2​

​

SDK 鉴权​

在使用扣子罗盘 Python SDK 前，确保你已经完成了授权。详情请参考​SDK 鉴权。​

安装扣子罗盘 SDK​

执行以下命令安装扣子罗盘 SDK。​

​

Python

复制

pip install cozeloop​

​

默认直接安装最新版本的 SDK。如果你想使用历史版本，单击[此处](<https://github.com/coze-dev/cozeloop-go/blob/main/CHANGLOG.md>)查看历史版本记录和 README。​

初始化扣子罗盘 SDK​

初始化扣子罗盘 Client 之后，才可以访问 SDK 提供的 API。​

初始化时推荐通过环境变量动态获取访问密钥，以免硬编码引发数据安全风险。 设置完成环境变量后，你可以直接访问 SDK API 实现相应功能。​

以下示例代码展示了如何使用扣子罗盘 SDK创建并上报一个 Span。​

说明

该示例中使用了 PAT 授权方式，在生产环境中推荐使用安全性更高的 OAuth 授权方式，详情参考​配置 OAuth JWT 授权。​

​

​

Python

复制

import os​

import cozeloop​

​

if __name__ == "__main__":​

# 设置相关环境变量​

os.environ["COZELOOP_WORKSPACE_ID"] = "your workspace id"​

os.environ["COZELOOP_API_TOKEN"] = "your token"​

​

# 直接调用api​

span = cozeloop.start_span("first_span", "custom")​

span.finish()​

​

# 程序退出前，需要调用Close方法，否则可能造成trace数据上报丢失。Close后无法再执行任何操作。​

cozeloop.close()​

​

你也可以通过创建 client 进行更多定制化配置。​

说明

client 是协程安全的，一般一个进程中仅需要创建一个 client 即可。​

​

​

Python

复制

import os​

import cozeloop​

​

if __name__ == "__main__":​

# 设置相关环境变量​

os.environ["COZELOOP_WORKSPACE_ID"] = "your workspace id"​

os.environ["COZELOOP_API_TOKEN"] = "your token"​

​

# 创建client​

client = cozeloop.new_client()​

​

# 通过client调用api​

span = client.start_span("first_span", "custom")​

span.finish()​

​

# 程序退出前，需要调用Close方法，否则可能造成trace数据上报丢失。Close后无法再执行任何操作。​

client.close() ​

​

示例代码​

Langchain ​

扣子罗盘基于 Langchain 的 callback 机制，提供了一键集成能力，能够自动完成 Trace 数据的上报。​

以下示例展示了如何在 LangChain 的 LCEL 模式中无缝集成扣子罗盘的 Trace 功能，实现对 AI 模型调用的监控和分析。​

​

Python

复制

import os​

​

import cozeloop​

from langchain_core.runnables import RunnableConfig​

from langchain_openai import ChatOpenAI​

from langchain_core.output_parsers import StrOutputParser​

​

from cozeloop.integration.langchain.trace_callback import LoopTracer​

​

​

def do_lcel_demo():​

# 配置CozeLoop环境变量​

os.environ['COZELOOP_API_TOKEN'] = '{your_token}'​

os.environ['COZELOOP_WORKSPACE_ID'] = '{your_workspace_id}'​

​

# 创建cozeloop client​

client = cozeloop.new_client()​

# 注册callback​

trace_callback_handler = LoopTracer.get_callback_handler(client)​

​

llm_model = ChatOpenAI()​

lcel_sequence = llm_model | StrOutputParser()​

output = lcel_sequence.invoke(​

input='用你所学的技巧，帮我生成几个有意思的问题',​

config=RunnableConfig(callbacks=[trace_callback_handler])​

)​

print(output)​

​

# 程序退出前，需要调用Close方法，否则可能造成trace数据上报丢失。Close后无法再执行任何操作。​

client.close()​

​

​

if __name__ == "__main__":​

do_lcel_demo()​

​

Decorator​

使用方法注解，可以快速实现对特定方法的监控。​

​

Python

复制

import logging​

import os​

import time​

​

from cozeloop import new_client, flush, get_span_from_context​

from cozeloop.decorator import observe​

from cozeloop.logger import set_log_level​

​

logger = logging.getLogger(__name__)​

​

ERR_CODE_LLM_CALL = 600789111​

​

class LLMRunner:​

def __init__(self):​

pass​

​

@observe(​

name="llmCall",​

span_type="model",​

tags={"model_provider":'openai', "input_tokens": 232, "output_tokens": 1211, "model_name": "gpt-4-1106-preview"},​

)​

def llm_call(self, input_data):​

"""​

Simulate an LLM call and set relevant span tags.​

"""​

# span = self.client.start_span("llmCall", "model")​

try:​

# Assuming llm is processing​

# output = ChatOpenAI().invoke(input=input_data)​

​

# mock resp​

time.sleep(1)​

output = "I'm a robot. I don't have a specific name. You can give me one."​

return output​

except Exception as e:​

raise e​

finally:​

pass​

​

@observe(​

# client=new_client(api_token="**"), # Unless you need a new client, no configuration is required,​

# the default client will be used automatically.​

name="root_span", # The name of the Span. Defaults to the function name.​

span_type="main_span", # The span_type of the Span. Defaults to 'custom'.​

tags={"mode": 'simple', "node_id": 6076665}, # Set static custom tag. The Priority is higher than the default tags.​

baggage={"product_id": "123456654321"}, # Set static custom baggage. baggage can cover tag of sample key, and will pass to child span automatically.​

)​

def do_simple_demo():​

# Dynamic set tag or baggage in runtime​

get_span_from_context().set_baggage({"thread_id": "my-thread-id"})​

get_span_from_context().set_tags({"sale_id": "my-sale-id"})​

​

# 0. new client​

set_log_level(logging.INFO)​

llm_runner = LLMRunner()​

​

# assuming call llm​

try:​

# assuming call llm​

llm_runner.llm_call("What's your name?")​

except Exception as e:​

pass​

​

​

if __name__ == "__main__":​

# Set the following environment variables first (Assuming you are using a PAT token.).​

# os.environ["COZELOOP_WORKSPACE_ID"] = "your workspace id"​

# os.environ["COZELOOP_API_TOKEN"] = "your token"​

​

do_simple_demo()​

​

# flush all trace data before server exit.​

flush()​

​

Trace效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273006%27%20height=%271622%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwNiIgaGVpZ2h0PSIxNjIyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

更多示例可以参考：[https://github.com/coze-dev/cozeloop-python/tree/main/examples/trace/annotation](<https://github.com/coze-dev/cozeloop-python/tree/main/examples/trace/annotation>)​

Low-Level API​

你也可以通过扣子罗盘 SDK提供的 low-level API，手动完成 Prompt 拉取和 Trace 数据的上报。​

说明

Low-level API 是更底层的编程接口，提供基础功能的直接访问，需要开发者手动处理更多细节，但能实现更灵活的控制和定制化需求。​

​

Root Span 上报​

在处理用户请求时，建议为每个请求创建一个完整的 Trace 链路：从服务入口处创建 root span，记录用户输入、系统响应和关键业务标识（如请求ID、用户ID等），便于后续进行链路追踪和性能分析。当请求处理完成时，调用 Finish 方法结束追踪。​

以下示例代码展示了如何使用扣子罗盘 SDK创建一个完整的请求追踪链路（Trace）。​

​

Python

复制

import cozeloop​

​

def handler(input: str) -> str:​

# 开启root span​

span = cozeloop.start_span("{your_span_name}", "{your_span_type}")​

​

# 设置用户输入​

span.set_input(input)​

# 设置相关业务id，可以使用Baggage能力将这些id全链路透传，减少重复代码，便于在平台上自由检索​

span.set_user_id_baggage("{user_id}")​

span.set_message_id_baggage("{message_id}")​

try:​

# 执行业务逻辑​

output = do_something(input)​

# 设置服务输出​

span.set_output(output)​

# 如果使用流式返回，记录首Token返回的微秒时间戳，SDK会自动计算首Token耗时​

span.set_start_time_first_resp({start_time_first_resp})​

except Exception as e:​

# 设置错误信息​

span.set_status_code(your_error_code)​

span.set_error(e)​

finally:​

# span 上报​

span.finish()​

​

return output​

​

Prompt 拉取​

在使用 SDK 拉取 Prompt 前，需要在扣子罗盘的 Prompt 开发页面获取 Prompt Key 和版本号。​

说明

只支持获取已提交的 Prompt 配置。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272826%27%20height=%27669.3157894736842%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgyNiIgaGVpZ2h0PSI2NjkuMzE1Nzg5NDczNjg0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

扣子罗盘 SDK 提供接口来拉取在扣子罗盘中创建并提交的 Prompt。通过 GetPrompt 方法可以获取指定 Key 的 Prompt（支持指定版本），然后使用 PromptFormat 方法完成变量替换。启用 PromptTrace 功能后，SDK 会自动记录 Prompt 的获取和渲染过程，便于后续分析和优化。​

以下是 Prompt 上报的示例代码。​

​

Python

复制

from typing import Dict, Any, List​

​

import cozeloop​

from cozeloop import entities​

​

# 初始化client，打开prompt trace上报开关​

client = cozeloop.new_client(prompt_trace=True)​

​

def get_prompt(params: Dict[str, Any]) -> List[entities.Message]:​

# 当version不为空时，将拉取特定版本的prompt​

# 当version为空时，将拉取最新版本的prompt​

prompt = client.get_prompt(​

prompt_key="{promptKey}", ​

version="{version}"​

)​

​

# 执行模板变量替换​

return client.prompt_format(​

prompt=prompt,​

variables=params​

)​

​

Model Span 上报​

模型调用往往是最关键的节点，在模型调用前后，上报 Model Span。span_type应该使用model，建议使用 spec 公共包中的 ModelInput 和 ModelOutput 记录input和output，以便在平台获得更好的体验。​

在进行模型调用时，建议创建专门的 Model Span 来追踪这个关键环节。以下示例代码展示了如何使用扣子罗盘 SDK创建一个完整的模型调用追踪：​

1.

创建 Model Span 时使用tracespec.VModelSpanType作为类型标识。​

2.

记录模型调用的完整上下文：​

  * 输入信息：使用 tracespec.ModelInput记录系统提示词和用户输入。​

  * 模型信息：记录模型提供商、模型名称和调用参数。​

  * Prompt 信息：关联使用的 Prompt Key 和版本。​

3.

调用完成后记录：​

  * 输出内容：使用tracespec.ModelOutput记录模型响应。​

  * 性能指标：记录输入输出的 Token 数量。​

  * 对于流式响应：记录首 Token 时间戳以计算响应延迟。​

以下是完整的 Model Span 上报示例代码。​

​

Python

复制

import cozeloop​

from cozeloop import entities​

from cozeloop.spec import tracespec​

​

def call_llm(prompt: entities.Prompt) -> None:​

# SpanType使用model​

span = cozeloop.start_span("{your_span_name}", tracespec.V_MODEL_SPAN_TYPE)​

​

# 设置模型输入​

span.set_input(tracespec.ModelInput(​

message=[​

tracespec.ModelMessage(​

role=tracespec.V_ROLE_SYSTEM,​

content="{system_prompt}",​

),​

tracespec.ModelMessage(​

role=tracespec.V_ROLE_USER,​

content="{user_prompt}",​

)​

]​

))​

​

# 设置模型提供商和模型名称​

span.set_model_provider("{model_provider}")​

span.set_model_name("{model_name}")​

# 关联PromptKey和Version​

span.set_prompt(prompt)​

# 设置Temperature, MaxTokens等其他参数​

span.set_model_call_options(tracespec.ModelCallOption())​

​

try:​

# 使用任意方式调用大模型​

# ...​

​

# 设置模型输出​

span.set_output(tracespec.ModelOutput(​

choices=[​

tracespec.ModelChoice(​

message=tracespec.ModelMessage(​

role=tracespec.V_ROLE_ASSISTANT,​

content="{model_response}",​

)​

)​

]​

))​

​

# 设置InputTokens和OutputTokens，SDK会自动计算TotalTokens​

span.set_input_tokens({input_tokens})​

span.set_output_tokens({output_tokens})​

​

# 如果使用流式返回，记录首Token返回的微秒时间戳，SDK会自动计算首Token耗时​

span.set_start_time_first_resp({start_time_first_resp})​

​

except Exception as e:​

span.set_error(e)​

span.set_status_code({status_code})​

raise​

finally:​

span.finish()​

​

自定义 Span 上报​

你可以在任何重要的业务节点创建自定义 span，通过设置以下信息进行全面追踪：​

  * 基础信息：自定义 span 名称和类型​

  * 业务数据：记录输入输出内容​

  * 自定义标签：通过 SetTags 添加需要追踪的特定信息​

  * 执行状态：记录状态码和错误信息​

这种灵活的追踪方式让您能够根据业务需求，精确监控和分析任何关键流程。​

以下示例代码展示了如何创建自定义 Span。​

​

Python

复制

import cozeloop​

​

def custom_func() -> None:​

span = cozeloop.start_span("{your_span_name}", "{your_span_type}")​

​

span.set_input("{your_input}")​

# 设置自定义tags​

span.set_tags({"key": "value"})​

​

try:​

# 执行业务逻辑​

output = do_something()​

​

span.set_status_code(0)​

span.set_output(output)​

except Exception as e:​

span.set_error(e)​

span.set_status_code({your_error_code})​

raise​

finally:​

span.finish()​

​

更多示例​

CozeLoop Python SDK 提供多种授权方式、常见使用方式的示例代码，便于开发者直接参考使用。 更多示例，访问 [Github](<https://github.com/coze-dev/cozeloop-python/tree/main/examples>)。​

​

模块​| 示例文件​| 说明​  
---|---|---  
授权 ​| [pat.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/init/pat.py>)​| 通过个人访问密钥实现授权。 ​  
​| [oauth_jwt.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/init/oauth_jwt.py>)​| 通过 OAuth JWT 方式实现授权。 ​  
Prompt​| [prompt_hub.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/prompt/prompt_hub.py>)[ ](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/prompt/prompt_hub.py>)​| 拉取扣子罗盘空间内的 Prompt，并进行变量替换。​  
​| [prompt_hub_with_jinja.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/prompt/advance/prompt_hub_with_jinja.py>)​| 拉取扣子罗盘空间内的使用 Jinja2 模版的 Prompt，并进行变量替换。​  
​| [prompt_hub_with_multipart.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/prompt/prompt_hub/prompt_hub_with_multipart.py>)​| 拉取扣子罗盘空间内的 Prompt，并注入多模态变量。​  
Trace​​| [simple.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/simple.py>)​| 实现最基本的 Trace 数据上报。​  
​| [parent_child.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/parent_child.py>)​| 正确设置 span 的父子关系。​  
​| [large_text.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/large_text.py>)​| 实现超大文本上报。​  
​| [multi_modality.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/multi_modality.py>)[ ](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/multi_modality.py>)​| 实现多模态数据上报。​  
​| [with_as.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/with_as.py>)​| 使用 Context Manager 进行上报。​  
​| [annotation](<https://github.com/coze-dev/cozeloop-python/tree/main/examples/trace/annotation>)​| 使用注解自动上报。​  
​| [wrapper_openai](<https://github.com/coze-dev/cozeloop-python/tree/main/examples/trace/wrapper_openai>)​| 集成 OpenAI 模型，并上报 Trace。​  
​| [transfer_between_services.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/transfer_between_services.py>)[ ](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/trace/transfer_between_services.py>)​| 实现跨进程 Trace 数据串联。​  
框架集成​| [lcel.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/lcel/lcel.py>)​| Trace callback 集成到 Langchain 框架，非流式场景。​  
​| [lcel_stream.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/lcel/lcel_stream.py>)[ ](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/lcel/lcel_stream.py>)​| Trace callback 集成到 Langchain 框架，流式场景。​  
异常处理 ​| [error.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/init/error.py>)[ ](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/init/error.py>)​| 处理 SDK 异常。 ​  
获取日志 ​| [log.py](<https://github.com/coze-dev/cozeloop-python/blob/main/examples/init/log.py>)​| 修改 SDK 内部打印日志的级别。​  
  
​

​

上一篇

调用 Prompt

下一篇

最佳实践