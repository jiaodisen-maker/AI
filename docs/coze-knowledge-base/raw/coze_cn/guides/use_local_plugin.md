---
source_url: https://docs.coze.cn/guides/use_local_plugin
title: '通过 API 使用端插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:07Z
---

# 通过 API 使用端插件 - 文档 - 扣子

通过 API 使用端插件

本文介绍如何通过调用 API 与扣子编程对话并调用端插件。​

准备工作​

  * 已创建绑定了端插件的低代码智能体，并且智能体已经发布为 API 服务。​

  * 已申请 Access Token，且 Access Token 已授权操作会话和消息的权限。具体请参见​鉴权方式概述。​

示例项目源码​

扣子编程提供端插件使用的示例项目源码， 通过扣子编程 Python SDK 实现与智能体对话并调用端插件，具体请参见 [agent_chat.py](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/local_plugin/agent_chat.py>)。​

使用流式响应​

API 调用流程​

通过 OpenAPI 使用端插件需要关注以下几个请求：​

​

API​| 是否必须​| API 路径​  
---|---|---  
​创建会话​| 可选（可以复用以前的会话）​| [https://api.coze.cn/v1/conversation/create](<https://api.coze.cn/v1/conversation/create>) ​  
​发起对话​| 必选​| [https://api.coze.cn/v3/chat](<https://api.coze.cn/v3/chat>)​  
​提交工具执行结果​| 必选​| [https://api.coze.cn/v3/chat/submit_tool_outputs](<https://api.coze.cn/v3/chat/submit_tool_outputs>) ​  
  
​

1 创建会话​

调用​创建会话 API。请求和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v1/conversation/create'\​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \​

\--header 'Content-Type: application/json' \​

​

​

2 发起对话​

调用​发起对话 API。返回结果中， status 为 requires_action，表示已经召回了端插件。​

conversation_id ：创建会话返回的 ID，例如上文中的 737917310581999****。​

请求和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v3/chat?conversation_id=748535563872637****' \​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"bot_id": "75049216555930***",​

"user_id": "123456789",​

"stream": true,​

"auto_save_history":true,​

"additional_messages":[​

{​

"role":"user",​

"content":"河南的降水概率",​

"content_type":"text"​

}​

]​

}'​

​

​

3 提交执行结果​

调用​提交工具执行结果 API。关键参数说明如下：​

  * conversation_id ：创建会话 API 返回的 ID，例如上文中的 737917310581999****。​

  * chat_id ：发起对话 API 返回的 ID，例如上文中的 743436994609809****。​

  * tool_call_id ：发起对话 API 返回的 tool_calls.id，例如上文中的 BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=。​

请求和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl --location 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=737917310581999****&chat_id=743436994609809****' \​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \​

\--header 'Content-Type: application/json' \​

\--data '{​

"stream": true,​

"auto_save_history": true,​

"tool_outputs": [​

{​

"tool_call_id": "BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=",​

"output": "{\"probability\":0.5}"​

}​

]​

}'​

​

​

使用非流式响应​

API 调用流程​

通过 OpenAPI 使用端插件需要关注以下几个 API 请求。​

​

API​| 是否必须​| API 路径​  
---|---|---  
​创建会话​| 可选（可以复用以前的会话）​| [https://api.coze.cn/v1/conversation/create](<https://api.coze.cn/v1/conversation/create>) ​  
​发起对话​| 必选​| [https://api.coze.cn/v3/chat](<https://api.coze.cn/v3/chat>)​  
​提交工具执行结果​| 必选​|  [https://api.coze.cn/v3/chat/submit_tool_outputs](<https://api.coze.cn/v3/chat/submit_tool_outputs>) ​  
​查看对话详情​| 必选​| [https://api.coze.cn/v3/chat/retrieve](<https://api.coze.cn/v3/chat/retrieve>) ​  
​查看对话消息详情​| 必选​| [https://api.coze.cn/v3/chat/message/list](<https://api.coze.cn/v3/chat/message/list>) ​  
  
​

1 创建会话​

调用 API ​创建会话。请求和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v1/conversation/create'\​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \​

\--header 'Content-Type: application/json' \​

​

​

2 发起对话​

调用​发起对话 API。​

conversation_id 为创建会话返回的 ID，例如上文中的 737917310581999****。​

请求和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v3/chat?conversation_id=737917310581999****' \​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"bot_id": "7504921655593****",​

"user_id": "123456789",​

"stream": false,​

"auto_save_history":true,​

"additional_messages":[​

{​

"role":"user",​

"content":"河南的降水概率",​

"content_type":"text"​

}​

]​

}'​

​

​

3 查看对话详情​

调用​查看对话详情 API。返回结果中， status 为 requires_action，表示已经召回了端插件。​

请求示例

返回示例

​

Shell

复制

curl --location 'https://api.coze.cn/v3/chat/retrieve?conversation_id=737917310581999****&chat_id=743436994609809****' \​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****'​

\--header 'Content-Type: application/json' \​

​

​

4 提交执行结果​

调用​提交工具执行结果 API。关键参数说明如下：​

  * conversation_id ：创建会话 API 返回的 ID，例如上文中的 737917310581999****。​

  * chat_id ：发起对话 API 返回的 ID，例如上文中的 743436994609809****。​

  * tool_call_id ：查看对话详情 API 返回的 tool_calls.id，例如上文中的 BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=。​

请求和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl --location 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=737917310581999****&chat_id=743436994609809****' \​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \​

\--header 'Content-Type: application/json' \​

\--data '{​

"stream": false,​

"auto_save_history": true,​

"tool_outputs": [​

{​

"tool_call_id": "BUJJERJDFxISEEFeS0pEQF5HFUZBXkpASkdeQEVAEhFGEkASFRdFSUI=",​

"output": "{\"probability\":0.5}"​

}​

]​

}'​

​

​

5 查看对话消息详情​

调用​查看对话消息详情 API。关键参数说明如下：​

  * conversation_id ：创建会话 API 返回的 ID，例如上文中的 737917310581999****。​

  * chat_id ：发起对话 API 返回的 ID，例如上文中的 743436994609809****。​

请求示例

返回示例

​

Shell

复制

curl --location 'https://api.coze.cn/v3/chat/message/list?conversation_id=737917310581999****&chat_id=743436994609809****' \​

\--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****'​

\--header 'Content-Type: application/json' \​

​

​

处理本地文件​

默认情况下，通过​上传文件 API 上传本地文件仅返回文件 ID，在触发了端插件的对话中，提交端插件工具执行结果时，也仅支持将该文件 ID 返回给大模型，而大模型并无法直接理解文件 ID。为了使 ​提交工具执行结果 API 能够返回大模型可理解的文件 URL， 你可参考本步骤完成相关配置。​

步骤一：定义端插件​

在端插件编辑工具页面的配置输入参数区域，添加 file 类型的输入参数，支持上传 File（通用文件）、Image（图片）、Doc（文档） 和 Code（代码文件）等文件，详细类型请参考​支持的文件格式。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27300.35087719298247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjMwMC4zNTA4NzcxOTI5ODI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：上传文件​

通过​上传文件 API 上传文件到扣子编程，并在返回结果中获取文件 ID（id）。​

请求示例

返回示例

​

Shell

复制

curl -X POST 'https://api.coze.cn/v1/files/upload' \​

-H "Authorization: Bearer pat_iQhcxIIxJiKxU0OaM8sLFH7MSNZKgNW6qLoAhC9XP1oOqjIuqREhzRoMjDP2****" \​

-H "Content-Type: multipart/form-data"​

\--form 'file=@"1120.png"'​

​

​

步骤三：提交执行结果​

当你通过 ​发起对话 API 与绑定了端插件的智能体对话时，如果对话触发了端插件请求本地文件，那么你可以在​提交工具执行结果API 中定义output 为文件 ID， ​提交工具执行结果 API 会将此文件 ID 转换为可访问的文件 URL，并返回给大模型。​

​提交工具执行结果 API 请求示例和返回示例如下，其中示例中的 output 为你在​步骤二：上传文件中上传的文件 ID。​

请求示例

返回示例

​

Shell

复制

curl -X POST 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=747295135519236****&chat_id=747303250529034****' \​

-H "Authorization: Bearer pat_iQhcxIIxJiKxU0OaM8sLFH7MSNZKgNW6qLoAhC9XP1oOqjIuqREhzRoMjDP2****" \​

-H "Content-Type: application/json" \​

-d '{​

"stream": false,​

"tool_outputs": [​

{​

"output": "{\"image\": \"736949598110202****\"}",​

"tool_call_id": "BUJJREUSERBBRUVeRBcXSl5HRhUVXkpFERdeFUBCRBUSEERGFhJ****"​

}​

]​

}'​

​

​

处理云端文件​

在触发了端插件的对话中，如果涉及请求云端文件，你可参考本步骤完成相关配置。​

步骤一：定义端插件​

在端插件编辑工具页面的配置输入参数区域，添加一个 File 类型或 String 类型的输入参数。两种类型均支持直接使用文件 URL。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27300.35087719298247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjMwMC4zNTA4NzcxOTI5ODI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：提交执行结果​

当你通过 ​发起对话 API 与绑定了端插件的智能体对话时，如果对话触发了端插件请求云端文件，那么你可以在​提交工具执行结果API 中定义output 为文件 URL， ​提交工具执行结果 API 会将此文件 URL 返回给大模型。​

​提交工具执行结果 API 请求示例和返回示例如下：​

请求示例

返回示例

​

Shell

复制

curl -X POST 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=747295135519236****&chat_id=747303250529034****' \​

-H "Authorization: Bearer pat_iQhcxIIxJiKxU0OaM8sLFH7MSNZKgNW6qLoAhC9XP1oOqjIuqREhzRoMjDP2****" \​

-H "Content-Type: application/json" \​

-d '{​

"stream": false,​

"tool_outputs": [​

{​

"output": "{\"image\": \"https://****.png\"}",​

"tool_call_id": "BUJJREUSERBBRUVeRBcXSl5HRhUVXkpFERdeFUBCRBUSEERGFhJ****"​

}​

]​

}'​

​

​

​

上一篇

创建端插件

下一篇

基于 MCP 服务创建插件