---
source_url: https://docs.coze.cn/cozeloop/trace-data
title: '查看 Trace 数据 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:45Z
---

# 查看 Trace 数据 - 文档 - 扣子

查看 Trace 数据

扣子罗盘提供了可视化的 Trace 数据记录，你可以直观地查看不同处理环节的详细信息例如延迟、token 消耗等。​

操作步骤​

在扣子罗盘 观测 > Trace 页面，可查看指定应用在特定时间范围内上报的 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273822%27%20height=%271915.6159420289855%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a60459bdaad44ca090ee74c1a057c5f5~tplv-goo7wpa0wc-quality:q75.image)​

​

在 Trace 列表，选择目标记录后，可查看 Trace 详情。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273396%27%20height=%271560.4305555555557%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/43b1975d2df9468bb2dde7aff1dc5ffd~tplv-goo7wpa0wc-quality:q75.image)​

​

你可以选择每个 Span 查看其 Run、Metadata 和 Feedback 信息：​

  * Run：默认以易于阅读的格式展示所选 Span 的输入和输出数据。你可一键展开/折叠长内容，并在美化视图与原始 JSON 格式之间切换。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27814%27%20height=%27391%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODE0IiBoZWlnaHQ9IjM5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * Metadata：以 JSON 格式展示所选 Span 的所有元数据（包括 tags 和 runtime 信息），并支持一键复制。元数据是以键值对形式存储的补充信息，例如应用程序版本、运行环境和调用的模型等。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273058%27%20height=%271210.4583333333333%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA1OCIgaGVpZ2h0PSIxMjEwLjQ1ODMzMzMzMzMzMzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * Feedback：展示所选 Span 关联的人工标注或自动评测结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273050%27%20height=%271041.3773148148148%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA1MCIgaGVpZ2h0PSIxMDQxLjM3NzMxNDgxNDgxNDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

你还可以单击 仅展示轨迹节点 按钮查看轨迹（Trajectory）数据。如果要查看指定节点的详细信息，你可以选择该节点。每个节点代表一个 Span。​

说明

Agent 的 Trace 数据被上报到扣子罗盘后，扣子罗盘可以自动提取出轨迹数据。关于轨迹，详情参阅 ​轨迹评测介绍。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272740%27%20height=%271572.962962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc0MCIgaGVpZ2h0PSIxNTcyLjk2Mjk2Mjk2Mjk2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

你还可以单击 仅展示轨迹节点 按钮旁的下拉箭头，单击 设置轨迹展示规则，在 轨迹节点规则配置 窗口创建筛选条件，对需要显示的轨迹节点进行筛选。筛选条件对空间内所有 Trace 生效。​

说明

你可以通过设置轨迹展示规则展示原本不属于轨迹的节点，例如 invoke_agent 节点。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27740%27%20height=%271563.2900432900433%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQwIiBoZWlnaHQ9IjE1NjMuMjkwMDQzMjkwMDQzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273796%27%20height=%271906.4858420268256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5NiIgaGVpZ2h0PSIxOTA2LjQ4NTg0MjAyNjgyNTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

Trace 信息说明​

Trace 列表包含以下信息。​

​

Trace 信息​| 说明​| 示例​  
---|---|---  
Trace ID​| 唯一标识请求完整链路的 ID，用于关联所有相关数据。​| 118f0c30f303292305f7bb7ee003f9****​  
Input​| 请求的原始输入内容。例如，文本信息或 API 调用参数等。​| ​Markdown复制我在北京，给我推荐一些菜，需要有口味辣一点的菜，至少推荐有2家餐厅​​  
Output​| 请求的最终输出结果。例如模型生成的回答或 API 返回数据。​| ​Markdown复制为您推荐以下两家位于北京的餐厅及其菜品： - **云边小馆**：推荐菜品有红烧肉、清泉牛肉，其中清泉牛肉口味辣。 - **聚福轩食府**：推荐菜品有红烧排骨、大刀回锅肉（经典的回锅肉，肉很大，价格40元，评分8分）、火辣辣的吻，其中大刀回锅肉和火辣辣的吻都是辣口的菜品。​​  
Tokens​| 本次请求的输入和输出总 token 数量。​| 1405​  
Input Tokens​| 输入信息的 token 数量。​| 1116​  
Output Tokens​| 输出信息的 token 数量。​| 289​  
Latency​| 请求从开始到结束的总耗时。​| 1200ms​  
LatencyFirstResp​| 流式响应中首次返回数据的时间。​| 300ms​  
Start Time​| 请求开始处理的时间戳。​| 2025-04-03 15:21:41​  
SpanID​| 子请求的唯一标识。​| 1b4c709f137cb1af​  
SpanType​| 子请求的类型，例如数据库查询、API调用、模型推理。​| Agent​  
SpanName​| 子操作的名称，自定义或系统预设。​| ReActAgent​  
PromptKey​| 触发模型响应的提示词标识。​| travel.bot​  
火山应用​| 火山应用的名称。​| travel_agent​  
火山智能体​| 火山智能体的名称。​| travel_agent.v2​  
Coze 智能体​| Coze 平台特定智能体实例的名称。​| 周末趣享助手​  
Coze 应用​| Coze 平台特定关联应用的名称。​| 长文写作助手​  
数据到期时间​| 请求数据在系统中的保留截止时间。​| 2025-04-06 15:21:41​  
  
​

使用过滤器​

在调试过程中，为了方便开发者快速查看所需的 Trace 数据，扣子罗盘提供筛选器和应用视图功能，支持快速筛选。​

Trace 数据的筛选维度​

下表列举了观测功能支持的 Trace 数据的筛选维度。​

​

筛选维度​| 说明​  
---|---  
上报时间​| 支持选择要查看的 Trace 数据的时间范围。​

  * 对于首次进入 Trace 列表页的用户，默认展示最近 3 天的 Trace 数据。​

  * 对于非首次进入 Trace 列表页的用户，系统展示的时间维度与一次筛选 Trace 列表的时间维度保持一致。​

  
查看方式​| 支持筛选 Root Span、All Span、Model Span 三种可选类型的 Trace。​

  * Root Span：查看所有请求的完整请求链路信息。​

  * All Span：查看所有子请求、子任务的链路信息。​

  * Model Span：查看所有模型请求的链路信息。​

  
数据来源​| 支持筛选以下类型的 Trace 数据：​

  * SDK 上报：通过集成扣子罗盘 SDK 后上报的 Trace 数据。若尚未上报数据，请参考 ​SDK 概述完成接入。​

  * Prompt 开发：在扣子罗盘创建并调试 Prompt 后上报的 Trace 数据。​

  * Coze 智能体：使用 Coze 智能体后上报的 Trace 数据。​

  * Coze 应用：使用 Coze 应用后上报的 Trace 数据。​

  * Coze 工作流：使用 Coze 工作流后上报的 Trace 数据。​

  * 火山智能体(veFaaS)：部署在 [火山引擎函数服务](<https://www.volcengine.com/docs/6662/97169?lang=zh>) 的火山智能体所上报的 Trace 数据。​

  * 火山智能体(AgentKit)：部署在 [火山引擎 AgentKit](<https://www.volcengine.com/docs/86681/1844823?lang=zh>) 的火山智能体所上报的 Trace 数据。​

  * 方舟应用：在 [方舟应用实验室](<https://www.volcengine.com/docs/82379/1262002?lang=zh>) 中创建的应用所上报的 Trace 数据。​

  
Input​| 支持筛选 Input 包含特定信息、为空、不为空三种类型的 Trace。​  
Output​| 支持筛选 Output 包含特定信息、为空、不为空三种类型的 Trace。​  
Latency​| 支持筛选指定延迟时长的 Trace。​  
LatencyFirstResp​| 支持筛选指定首次返回延迟时长的 Trace。​  
MessageID​| 支持筛选指定 Message ID 的 Trace。​  
SpanType​| 支持筛选指定 SpanType 的 Trace。​  
Status​| 支持筛选成功或失败状态的 Trace。​  
TraceID​| 支持筛选指定 TraceID 的 Trace。​  
UserID​| 支持筛选指定 UserID 的 Trace。​  
SpanName​| 支持筛选指定 SpanName 的 Trace。​  
  
​

轨迹数据的筛选维度​

下表列举了观测功能支持的轨迹节点的筛选维度。​

​

筛选维度​| 说明​  
---|---  
SpanType​| 支持根据 SpanType 筛选 Span 作为轨迹节点。​  
SpanName​| 支持根据 SpanName 筛选 Span 作为轨迹节点。​  
Metadata​| 支持根据 Metadata 中特定字段的值筛选 Span 作为轨迹节点。例如，你可以筛选出 Metadata 中 gen_ai.tool.name 字段的值包含 web_search 的 Span 作为轨迹节点。​  
Feedback-自动评测​| 在自动评测场景下，支持筛选 Feedback 中指定评估器返回的值符合指定条件的 Span 作为轨迹节点。​  
Feedback-人工标注​| 在人工标注场景下，支持筛选 Feedback 中指定标签的值符合指定条件的 Span 作为轨迹节点。​  
  
​

应用视图​

Trace 列表页提供两种系统视图：​

  * 所有异常：查看属于 Root Span，数据来源属于 SDK 上报，Status 为失败的 Trace。​

  * 性能差：查看属于 Root Span，数据来源属于 SDK 上报，Latency 大于 10s 的 Trace。​

此外，Trace 列表页支持创建个人偏好视图，可在过滤器中选定个人偏好后，单击保存视图并输入视图名称。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272384%27%20height=%271109.2222222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM4NCIgaGVpZ2h0PSIxMTA5LjIyMjIyMjIyMjIyMjIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

视图保存完成后，点击视图即可快速筛选符合个人偏好的 Trace，再次点击视图即可退出个人视图。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272390%27%20height=%27621.9590643274854%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM5MCIgaGVpZ2h0PSI2MjEuOTU5MDY0MzI3NDg1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

获取扣子罗盘空间 ID

下一篇

查看统计数据