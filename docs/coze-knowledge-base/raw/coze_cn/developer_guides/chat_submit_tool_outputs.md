---
source_url: https://docs.coze.cn/developer_guides/chat_submit_tool_outputs
title: '提交工具执行结果 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:21:06Z
---

# 提交工具执行结果 - 文档 - 扣子

提交工具执行结果

调用此接口提交工具执行的结果。​

接口说明​

你可以将需要客户端执行的操作定义为插件，对话中如果触发这个插件，流式 event 响应信息会提示“conversation.chat.requires_action”，此时需要执行客户端的操作后，通过此接口提交插件执行后的结果。​

说明

  * 调用[发起对话](<https://docs.coze.cn/developer_guides/chat_v3>) API 时，auto_save_history 参数需要设置为 true，否则调用本 API 提交工具执行结果时会提示 5000 错误。​

  * 仅触发了端插件的对话需要调用此接口提交执行结果。端插件是非扣子服务端执行的插件，需要开发者自行执行任务后提交结果，通常用于 IoT 等设备控制场景。详细说明可参考[通过 API 使用端插件](<https://docs.coze.cn/guides/use_local_plugin>)。​

​

基础信息​

​

请求方式​| POST​  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v3/chat/submit_tool_outputs​​  
权限​| submitToolChat​确保调用该接口使用的访问令牌开通了 submitToolChat 权限，详细信息参考[准备工作](<https://www.coze.com/docs/developer_guides/preparation>)。​  
接口说明​| 调用接口提交工具执行结果。​  
  
​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考[鉴权方式](<https://docs.coze.cn/developer_guides/authentication>)。​  
Content-Type​| application/json​| 解释请求正文的方式。​  
  
​

Query​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
conversation_id​| String​| 必选​| 748348012449138***​| Conversation ID，即会话的唯一标识。可以在[发起对话](<https://docs.coze.cn/developer_guides/chat_v3>)接口 Response 中查看 conversation_id 字段。​  
chat_id​| String​| 必选​| 738137187639794***​| Chat ID，即对话的唯一标识。可以在[发起对话](<https://docs.coze.cn/developer_guides/chat_v3>)接口 Response 中查看 id 字段，如果是流式响应，则在 Response 的 chat 事件中查看 id 字段。​  
  
​

Body​

​

ToolOutput​

​

​

返回参数​

非流式响应​

在非流式响应中，无论服务端是否处理完毕，立即发送响应消息。其中包括本次对话的 chat_id、状态等元数据信息，但不包括模型处理的最终结果。​

非流式响应不需要维持长连接，在场景实现上更简单，但通常需要客户端主动查询对话状态和消息详情才能得到完整的数据。你可以通过接口​查看对话详情确认本次对话处理结束后，再调用​查看对话消息详情接口查看模型回复等完整响应内容。流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27282%27%20height=%27340%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgyIiBoZWlnaHQ9IjM0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

非流式响应的结构如下：​

​

ChatV3ChatDetail​

​

LastError​

​

RequiredAction​

​

SubmitToolOutputs​

​

InterruptPlugin​

​

InterruptFunction​

​

Usage​

​

ResponseDetail​

​

流式响应​

在流式响应中，服务端不会一次性发送所有数据，而是以数据流的形式逐条发送数据给客户端，数据流中包含对话过程中触发的各种事件（event），直至处理完毕或处理中断。处理结束后，服务端会通过 conversation.message.completed 事件返回拼接后完整的模型回复信息。各个事件的说明可参考流式响应事件。​

流式响应允许客户端在接收到完整的数据流之前就开始处理数据，例如在对话界面实时展示智能体的回复内容，减少客户端等待模型完整回复的时间。​

流式响应的整体流程如下：​

​

​

​

ChatV3MessageDetail​

​

示例​

请求示例​

​

返回示例​

​

错误码​

如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考[错误码](<https://docs.coze.cn/developer_guides/coze_error_codes>)文档查看对应的解决方法。​

​

上一篇

查看对话消息详情

下一篇

取消进行中的对话