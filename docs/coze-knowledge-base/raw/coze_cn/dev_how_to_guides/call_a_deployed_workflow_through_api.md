---
source_url: https://docs.coze.cn/dev_how_to_guides/call_a_deployed_workflow_through_api
title: '通过 API 调用工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:07Z
---

# 通过 API 调用工作流 - 文档 - 扣子

通过 API 调用工作流

将 AI 编程生成的工作流部署为 API 服务后，你可以在你的应用程序或网页中通过 HTTP 请求来调用工作流的 API，以便在你的应用程序或网页中集成工作流的 AI 能力。​

前提条件​

已将 AI 编程生成的工作流部署为 API 服务。详情请参见​部署工作流。​

支持的 API 接口​

​

API 接口​| API请求地址​| 说明​  
---|---|---  
执行工作流​|  https://<your_domain>/run​| 采用同步执行方式并以非流式返回响应，适用于执行时间短、且只需一次性获取最终结果的工作流。​调用该 API 时，工作流的执行时间控制在 5 分钟（300 秒）以内。如果服务器在 300 秒内未返回响应，连接将因超时而中断。对于生图渲染等执行耗时较长的工作流，为避免连接断开，需每 300 秒至少发送一次心跳信号，确保服务器与调用端的连接持续活跃。实现方法可参考​在生图等场景中出现连接超时怎么办？​  
执行工作流（流式）​| https://<your_domain>/run/stream​| 采用流式执行方式并以流式返回响应，适用于执行时间长、且需要多次获取中间结果的工作流。​调用该 API 时，建议将工作流的执行时间控制在 15 分钟（900 秒）内。为避免执行超时导致连接中断，服务端会自动发送心跳包来维持连接。​  
查询工作流信息​| https://<your_domain>/graph_parameter​| 用于查询执行工作流的状态与结果。​  
  
​

获取访问信息​

部署成功后，扣子编程会自动生成 API 服务，你可以在部署总览页面获取访问 API 的相关信息。​

查看 API 访问信息​

获取该服务的 API 访问地址、请求Header、请求参数等详细信息。​

1.

在工作流开发页面，在右侧单击➕打开新的标签页，在弹出的标签页中选择部署。​

2.

在部署的总览页面，单击某条部署记录右侧的更多按钮，选择查看。​

3.

在API 请求示例及接口说明页面，查看该服务的 API 访问信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27433.52601156069363%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQzMy41MjYwMTE1NjA2OTM2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

创建 API Token​

你需要创建 API Token，以便集成调用该服务。​

1.

在工作流开发页面，在右侧单击➕打开新的标签页，在弹出的标签页中选择部署。​

2.

在部署的总览页面，单击某条部署记录右侧的更多按钮，选择查看。​

3.

在API 请求示例及接口说明页面，单击查看 API Token，单击管理 API Token 生成新的 API Token。复制并妥善保存 API Token。 ​

  * 说明

    * 生成的令牌仅在此时展示一次，请即刻复制并妥善保存。​

    * 请妥善保存该 API Token，不要在浏览器或其他客户端代码中暴露 API Token。​

    * 每个项目最多能创建 10 个 API Token，API Token 的有效期为永久有效。​

    * 暂时不支持在部署详情页面直接调用和调试 API。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27541.6184971098265%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjU0MS42MTg0OTcxMDk4MjY1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

（可选）你也可以在 API Token 页面查看已创建的 API Token 列表，删除不再使用的 API Token。​

API 接口调用流程​

以上三个 API 接口调用流程类似。以调用执行工作流接口为例，其调用流程如下：​

1.

在工作流的部署页面，复制扣子编程提供的 Curl 请求命令。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272900%27%20height=%27989.0173410404624%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwMCIgaGVpZ2h0PSI5ODkuMDE3MzQxMDQwNDYyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

将 header 中的 <YOUR_TOKEN> 替换为你在​创建 API Token中获取的 API Token。​

3.

通过 Curl、Python 或 Node.js 的方式调用 API。​

  * 以下示例展示了如何使用 Curl 调用工作流 API。你也可以在部署页面复制 Python 和 Node.js 的调用示例。API 的请求参数和返回参数由 AI 编程自动生成。​

  * ​

TypeScript

复制

curl --location 'https://t6h***.coze.site/run' \​

\--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFkNDYwNWY5LWRjM2MtNGE0Ni04YmFhLWRiNTg3MGNmMTI4ZSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbImVNYk1rMVRmVEdDQ1IybmQ1WlVjYUNwUmk5U25HQUdmIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzY2NDYwODg0LCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93******' \​

\--header 'Content-Type: application/json' \​

\--data '{"number1":0,"number2":0}'​

​

API接口返回示例​

调用执行工作流接口返回示例​

返回工作流的最终输出，其数据结构与工作流中定义的输出参数保持一致。​

​

TypeScript

复制

{"result":0.0,"run_id":"858996f9-ba21-45aa-ae5f-5c8771c9****"}​

​

返回结果说明如下：​

​

字段​| 类型​| 描述​  
---|---|---  
result​| /​| 工作流的最终输出结果，其数据结构和内容与工作流中定义的输出参数一致。​  
run_id​| string​| 整个工作流实例的唯一标识。​  
  
​

调用执行工作流（流式）接口返回示例​

返回一个 Server-Sent Events (SSE) 格式的数据流。为了追踪工作流的实时进度，你需要逐条解析这些事件。数据流中的每个事件都分别代表一个节点的开始、输出或结束。​

​

TypeScript

复制

id: 0​

event: message​

data: {"type": "node_start", "timestamp": 1768877934224, "log_id": "", "run_id": "1878882f-f2c5-4572-9138-9a0f7b8c****", "node_name": "calculator", "input": {"a": 1.0, "b": 2.0}}​

​

id: 1​

event: message​

data: {"type": "node_end", "timestamp": 1768877935232, "log_id": "", "run_id": "1878882f-f2c5-4572-9138-9a0f7b8c****", "node_name": "calculator", "output": {"result": 3.0}, "time_cost_ms": 1008}​

​

id: 2​

event: message​

data: {"type": "node_start", "timestamp": 1768877935233, "log_id": "", "run_id": "1878882f-f2c5-4572-9138-9a0f7b8c****", "node_name": "calculator1", "input": {"a": 1.0, "b": 2.0}}​

​

id: 3​

event: message​

data: {"type": "node_end", "timestamp": 1768877936246, "log_id": "", "run_id": "1878882f-f2c5-4572-9138-9a0f7b8c****", "node_name": "calculator1", "output": {"result": 3.0}, "time_cost_ms": 1013}​

​

id: 4​

event: message​

data: {"type": "done", "timestamp": 1768877936246, "log_id": "", "run_id": "1878882f-f2c5-4572-9138-9a0f7b8c****", "output": {"result": 3.0}, "time_cost_ms": 2024}​

​

返回结果各字段说明如下：​

​

字段​| 类型​| 出现事件​| 含义​  
---|---|---|---  
id​| int​| 所有事件​| 事件在响应流中的序号，从 0 开始递增​  
event​| string​| 所有事件​| 固定为 message，表示是流式推送的消息​  
data.type​| string​| 所有事件​| 事件子类型，如 node_start、node_end、done。​  
data.timestamp​| int​| 所有事件​| 事件发生的时间戳（毫秒）​  
data.log_id​| string​| 所有事件​| 日志 ID，可为空​  
data.run_id​| string​| 所有事件​| 整个工作流实例的唯一标识，同一工作流内所有事件的 run_id 相同​  
data.node_name​| string​| node_start / node_end​| 当前执行的节点名称​  
data.input​| object​| node_start​| 节点执行时的输入参数​  
data.output​| object​| node_end / done​| 节点或工作流的输出结果​  
data.time_cost_ms​| int​| node_end / done​| 节点运行耗时或整个工作流总耗时（毫秒）​  
  
​

调用查询工作流信息接口返回示例​

返回工作流的最终输出，其数据结构与工作流中定义的输出参数保持一致。​

​

TypeScript

复制

{​

"code": 0,​

"msg": "",​

"input_schema": {​

"description": "工作流的输入",​

"properties": {​

"number1": {​

"description": "第一个加数",​

"title": "Number1",​

"type": "number"​

},​

"number2": {​

"description": "第二个加数",​

"title": "Number2",​

"type": "number"​

}​

},​

"required": ["number1", "number2"],​

"title": "GraphInput",​

"type": "object"​

},​

"output_schema": {​

"description": "工作流的输出",​

"properties": {​

"result": {​

"description": "加法计算结果",​

"title": "Result",​

"type": "number"​

}​

},​

"required": ["result"],​

"title": "GraphOutput",​

"type": "object"​

}​

}​

​

返回示例各字段说明如下：​

​

字段​| 类型​| 描述​  
---|---|---  
code​| int​| 调用状态码，0 表示成功，其他值表示失败。​  
msg​| string​| 状态信息，失败时返回详细错误信息。​  
input_schema​| object​| 工作流的输入参数规范，包含每个参数的名称、描述、类型和是否必填。​  
output_schema​| object​| 工作流的输出结果规范，包含每个参数的名称、描述、类型和是否必填。​  
  
​

故障排查​

如果 API 调用失败，请参考以下内容进行排查。​

  * 确认 Authorization Header 中的 API Token 是否正确。​

  * 确认请求体中的参数名和数据类型是否与工作流定义一致。​

  * 将错误码和返回的 msg 字段中的详细错误信息，提供给 AI 编程帮忙定位并修复问题。​

上一篇

消息评价

下一篇

通过 API 调用智能体