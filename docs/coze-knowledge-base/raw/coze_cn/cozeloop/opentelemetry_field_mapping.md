---
source_url: https://docs.coze.cn/cozeloop/opentelemetry_field_mapping
title: 'OpenTelemetry 字段映射 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:49Z
---

# OpenTelemetry 字段映射 - 文档 - 扣子

OpenTelemetry 字段映射

在使用 OpenTelemetry 向扣子罗盘发送 Trace 数据时，以下属性将映射为扣子罗盘字段。这些映射关系确保了数据的一致性和可读性，同时也遵循了 OpenTelemetry 的语义规范。​

OpenTelemetry 协议的语义规范，请参考[Semantic conventions for generative client AI spans](<https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/>)。​

字段优先级​

字段的优先级按照以下原则：​

  * 细粒度优先级高于粗粒度，例如 gen_ai.prompt.{n}.role 优先于 gen_ai.prompt。​

  * 事件（Event）的优先级高于属性（Attribute），例如 Message 事件优先级高于 gen_ai.prompt 属性，Choice 事件优先级高于 gen_ai.completion 属性。​

通用字段​

通用字段涵盖了 Span 的标识、时间、基本信息等核心字段。​

属性（Attribute）​

说明

  * 不支持用户设置时，对应的字段值将依赖 OpenTelemetry 自动生成。​

  * cozeloop.span_type 字段不一定被使用，优先使用具体类型的 Span 节点中的 span_type 属性，如 Model Span 的属性 gen_ai.operation.name。​

​

​

OpenTelemetry ​Span 主字段​| OpenTelemetry ​Span Attributes 子字段​| 字段类型​| 扣子罗盘字段​| 是否必填​| 是否支持设置​​| 说明​  
---|---|---|---|---|---|---  
SpanId​| -​| []byte​| Span ID​| 是​| 否​| Span ID。​  
TraceId​| -​| []byte​| Trace ID​| 是​| 否​| Trace ID。​  
ParentSpanId​| -​| []byte​| Parent Span ID​| 否​| 否​| 父级 Span ID。​  
StartTimeUnixNano​| -​| int​| Start Time​| 是​| 否​| Span 开始时间，单位：微秒。​  
StartTimeUnixNano​EndTimeUnixNano​| -​​| int​int​| Duration​| 是​| 否​| Span 持续时间，单位：微秒。​  
Name​| -​| string​| Span Name​| 是​| 是​| Span 节点名称。​  
Attributes​| cozeloop.workspace_id​​| string​| WorkSpace ID​| 否​​| 是​| 扣子罗盘工作空间 ID，用于鉴权。​只有在同一个服务需要上报多个空间的 Trace 时，才需要填写，优先级高于 Header 中的cozeloop-workspace-id。​  
Attributes​​| cozeloop.span_type​​| string​| Span Type​​| 是​| 是​| Span 节点类型，可选值：​

  * model：大模型节点​

  * prompt：Prompt节点​

  * retriever：RAG 召回节点​

  * tool：Tool Call 节点​

  
Attributes​| cozeloop.input​| string​| Input​| 否​| 是​| 输入内容，可以为任意内容。​  
Attributes​| cozeloop.output​| string​| Output​| 否​| 是​| 输出内容，可以为任意内容。​  
Attributes​| session.id​​| string​| Tags.thread_id​| 否​| 是​| 会话（会话、线程）的唯一标识符，用于存储和关联此会话中的消息。​  
Attributes​| user.id​| string​| Tags.user_id​| 否​| 是​| 用户 ID。​  
Attributes​| messaging.message.id​| string​| Tags.message_id​| 否​| 是​| 消息 ID。​  
Attributes​| error.type​| string​| Tags.error​| 否​| 是​| 错误信息。​未设置 status_code 时，将默认为 -1。​  
  
​

事件（Event）​

Event 用于记录在 Span 执行过程中发生的特定事件，例如异常或用户交互。​

Exception 事件​

Exception（异常）事件的字段映射如下：​

​

event Attributes 字段​| 字段类型​| 罗盘字段​| 说明​  
---|---|---|---  
exception.message​| string​| 

  * status_code​

  * 未设置 status_code 时，将默认为 -1。​

  * error message​

| error 获取优先级：​exception 事件的优先级高于 error.message。​  
exception.stacktrace​​| string​| 

  * status_code​

  * 未设置 status_code 时，将默认为 -1。​

  * error message​

  * 补充添加到error message之后​

| error 获取优先级：​exception 事件的优先级高于 error.message。​  
  
​

Model 节点​

Model 节点用于记录与 AI 模型调用相关的详细信息，包括输入、输出和调用参数。​

属性（Attribute）​

标准字段​

​

OpenTelemetry attribute字段​| 字段类型​| 扣子罗盘字段​| 说明​  
---|---|---|---  
gen_ai.system​| string​| Tags.model_provider​| 模型提供方，例如 openai、anthropic。​  
gen_ai.operation.name​gen_ai.request.type（traceLoop使用该字段）​| string​| span_type​​| Span 节点类型。映射转换关系：​

  * chat：转换为 model​

  * create_agent：不转换​

  * embeddings：不转换​

  * execute_tool：转换为 tool​

  * generate_content：转换为 model​

  * invoke_agent：不转换​

  * text_completion：转换为 model​

  
gen_ai.prompt​​| string​| Input​| 大模型输入，优先级比 Event 低。​(opentelemetry 已废弃，不推荐使用)​  
gen_ai.completion​| string​| Output​| 大模型输出，优先级比 Event 低。​(opentelemetry 已废弃，不推荐使用)​  
gen_ai.prompt.{n}.role​| string​| Input.messages[n].role​| 输入消息的Role，优先级比 event 低。​  
gen_ai.prompt.{n}.content​| string​| Input.messages[n].content​| 输入消息的内容，优先级比 event 低。​  
gen_ai.completion.{n}.role​| string​| Output.messages[n].role​| 输出消息的 Role，优先级比 event 低。​  
gen_ai.completion.{n}.content​| string​| Output.messages[n].content​| 输出消息的内容，优先级比 event 低。​  
cozeloop.time_to_first_token​​| int​​| Tags.latency_first_resp​| 流式调用模型时，首包返回的时间戳, 单位：微秒。会自动计算出从 Span 开始到首包返回的耗时。​  
cozeloop.stream​| boolean​| Tags.stream​| 是否流式输出。​  
  
​

Request 参数​

Request 参数用于记录调用 AI 模型时的请求参数，例如模型名称、token 数量等。​

​

OpenTelemetry 字段​| 字段类型​| 扣子罗盘字段​| 说明​  
---|---|---|---  
gen_ai.request.model​| string​| Tags.model_name​| 模型名字，不区分 request 和 response。​  
gen_ai.response.model​| string​| Tags.model_name​| 模型名字，不区分 request 和 response。​  
gen_ai.request.temperature​| double​| Tags.call_options.temperature​| Temperature 配置。​  
gen_ai.request.top_p​| double​| Tags.call_options.top_p​| top_p 采样配置。​  
gen_ai.request.top_k​| double​| Tags.call_options.top_k​| top_k 采样配置。​  
gen_ai.request.max_tokens​| int​| Tags.call_options.max_tokens​| 控制生成文本的最大 tokens。​  
gen_ai.request.frequency_penalty​| double​| Tags.call_options.frequency_penalty​| Frequency penalty 配置。​  
gen_ai.request.presence_penalty​| double​| Tags.call_options.presence_penalty​| Presence penalty 配置。​  
gen_ai.request.stop_sequences​| string[]​| Tags.call_options.stop​| 指定生成文本时的停止序列。​  
  
​

Usage参数​

Usage 参数用于记录 AI 模型调用的使用情况，例如输入和输出的令牌数。​

​

OpenTelemetry Attribute​| 字段类型​| 扣子罗盘字段​| 说明​  
---|---|---|---  
gen_ai.usage.input_tokens​| int​| Tags.input_tokens​| 输入的 tokens，会和 output tokens 取和自动计算出 tokens。​  
gen_ai.usage.output_tokens​| int​| Tags.output_tokens​| 输出的 tokens，会和 input tokens 取和自动计算出 tokens。​  
gen_ai.usage.prompt_tokens​​| int​| Tags.input_tokens​​| Opentelemetry 已废弃，不推荐使用。​  
gen_ai.usage.completion_tokens​​| int​| Tags.output_tokens​| Opentelemetry 已废弃，不推荐使用。​  
  
​

事件（Event）​

OpenTelemetry Model 节点相关的 Event 说明，请参考 [Event](<https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/#event-gen_aiassistantmessage>)。​

Message 事件​

罗列了消息相关的事件字段，事件名称为 gen_ai.system.message、gen_ai.user.message、gen_ai.assistant.message、gen_ai.tool.message。​

​

事件名称​| Event Attributes 字段​| 字段类型​| 扣子罗盘字段​  
---|---|---|---  
gen_ai.system.message​gen_ai.user.message​| content​| string​| Input.messages[n].content​  
​| role​| string​| Input.messages[n].role​  
gen_ai.assistant.message​​| content​| string​| Input.messages[n].content​  
​| role​| string​| Input.messages[n].role​  
​| tool_calls​| map[]​| Input.messages[n].tool_calls​  
​| tool_calls.{n}.id​| string​| Input.messages[n].tool_calls.id​  
​| tool_calls.{n}.type​| string​| Input.messages[n].tool_calls.type​  
​| tool_calls.{n}.function​| map​| Input.messages[n].tool_calls.function​  
​| tool_calls.{n}.function.name​| string​| Input.messages[n].tool_calls.function.name​  
​| tool_calls.{n}.function.arguments​| undefined​| Input.messages[n].tool_calls.function.arguments​  
gen_ai.tool.message​| content​| string​| Input.messages[n].content​  
​| id​| string​| Input.messages[n].name​  
​| role​| string​| Input.messages[n].role​  
  
​

Choice 事件​

罗列了决策相关的事件字段，事件名称为 gen_ai.choice。​

​

事件名称​| Event 字段​| 字段类型​| 扣子罗盘字段​  
---|---|---|---  
gen_ai.choice​| finish_reason​| string​| Output.choices[0].finish_reason​  
​| index​| int​| Output.choices[0].index​  
​| message​| map​| Output.choices[0].message​  
​| message.content​| string​| Output.choices[0].message.content​  
​| message.role​| string​| Output.choices[0].message.role​  
​| message.tool_calls​| map[]​| Output.choices[0].message.tool_calls​  
​| message.tool_calls.{n}.id​| string​| Output.choices[0].message.tool_calls.id​  
​| message.tool_calls.{n}.type​| string​| Output.choices[0].message.tool_calls.type​  
​| message.tool_calls.{n}.function​| map​| Output.choices[0].message.tool_calls.function​  
​| message.tool_calls.{n}.function.name​| string​| Output.choices[0].message.tool_calls.function.name​  
​| message.tool_calls.{n}.function.arguments​| undefined​| Output.choices[0].message.tool_calls.function.arguments​  
  
​

Prompt节点​

Prompt 节点用于记录与 AI 模型调用相关的提示信息，包括唯一标识符、版本和提供方信息。Attribute 的标准字段如下：​

​

OpenTelemetry attribute​| 字段类型​| 扣子罗盘字段​| 说明​  
---|---|---|---  
cozeloop.prompt_key​| string​| Tags.prompt_key​| Prompt key。​  
cozeloop.prompt_version​| string​| Tags.prompt_version​| Prompt 版本。​  
cozeloop.prompt_provider​| string​| Tags.prompt_provider​| Prompt 提供方。​  
  
​

其他字段​

  * 其他未提及的用户自定义属性字段，默认存放在 Tags 字段，前端页面展示在 Metadata 中。​

  * 其他未提及的事件，不保留，直接丢弃。​

上一篇

通过 OpenTelemetry SDK 上报 Trace

下一篇

AutoGen