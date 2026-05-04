---
source_url: https://docs.coze.cn/guides/queries
title: '消息日志 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:45:42Z
---

# 消息日志 - 文档 - 扣子

消息日志

在智能体、应用或工作流中，每条消息回复都会生成一条消息日志，这个消息日志详细记录了其回复问题的编排步骤和详细过程。消息日志帮助你了解低代码智能体、应用或工作流的推理过程，以便你进行针对性的分析和优化。​

功能说明​

日志页面主要展示低代码智能体、应用和工作流的消息日志，单击日志可查看全流程处理链路。​

消息日志功能通常用于以下场景：​

  * 日志分析：查看的详细消息日志。​

  * 故障排查：在扣子编程中，一个对话请求通常会经由多个环节处理，例如调用 LLM 节点回复问题。消息日志功能提供智能体调用技能的输入、查询的知识库等信息，你可以识别智能体出现异常或不符合预期行为的步骤。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27491.0982658959537%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ebdf4c9d0e7e4f68b232be720682686f~tplv-goo7wpa0wc-quality:q75.image)​

​

使用限制​

不同扣子套餐支持的消息日志相关权益如下表。​

​

功能​| 个人免费版​| 个人进阶版​| 企业标准版​| 企业旗舰版​  
---|---|---|---|---  
消息日志存储天数​| 3天​| 7天​| 90天​| 180天​  
上报的消息数量​| 5 万条/月​| 10 万条/月​| 10 万条/月​| 200 万条/月​  
消息导出​| 不支持​| 每个智能体单次最多可导出 5000 条消息记录。​| ​| ​  
  
​

消息日志的使用限制如下表所示。​

​

限制类​| 限制说明​  
---|---  
权限​| 

  * 空间成员仅能查看你作为所有者或协作者的应用、智能体和工作流的消息日志。添加智能体协作者的操作可参考​协同管理低代码智能体。​

  * 空间所有者和管理员支持查看所有应用、智能体和工作流的消息日志。​

  
记录范围​| 

  * 渠道：暂不支持豆包 的智能体消息日志。​

  * 内容：消息日志页面暂不支持展示多模态用户输入，例如语音、图片、文件等类型的消息。​

  
延时​| 消息在各个渠道中的延时不同，部分渠道可能长达数分钟，对话后建议间隔一段时间再查看消息。​  
数据准确性​| 日志页面显示的用户输入 Token、模型输出 Token仅用于参考。企业标准版、企业旗舰版和[旧版付费套餐用户](<https://docs.coze.cn/guides/20260119_coze_premium_upgraded>)实际使用的 Token 数量可查看[火山引擎账单](<https://console.volcengine.com/finance/bill/detail/>)。​  
  
​

查看消息日志​

借助分析看板，你能够全面跟踪和分析已发布的低代码智能体、应用和工作流的运行状况，包括 Token 消耗、积分消耗、用户数、对话数等基础运营数据、用户参与度、性能评估以及渠道运营洞察等，帮助你优化用户体验、提升运营效率、解决技术问题。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左下角单击个人头像，选择企业，然后单击对应组织的设置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27311%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzExIiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在组织管理页面的顶部选择空间管理，然后单击目标工作空间对应的设置。​

​

3.

在顶部选择发布管理页签。​

4.

单击对应的低代码智能体、应用或工作流，在日志页面，在顶部选择时间段，查看对话记录。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273422%27%20height=%27727.9167630057804%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQyMiIgaGVpZ2h0PSI3MjcuOTE2NzYzMDA1NzgwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看消息列表​

页面默认展示过去 3 天内的消息列表。列表标题行各字段说明如下：​

说明

对于 API 渠道，会话、消息和用户 ID 均由 API 的调用方自定义设置，对话状态也取决于​发起对话 API 的执行状态。​

​

​

字段​| 说明​| 筛选示例​  
---|---|---  
状态​| 本次对话的状态。如果智能体由于系统限流或其他技术因素未能提供有效回复，或者对话中触发的工作流中任意节点运行异常，则视为对话状态异常。​| 支持根据对话状态筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2774.78260869565217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9Ijc0Ljc4MjYwODY5NTY1MjE3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
消息 ID​| 用户向智能体发送的消息的 ID。​​| 支持根据对话 ID 筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27118.26086956521739%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjExOC4yNjA4Njk1NjUyMTczOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
会话 ID​| 会话 ID 即 Conversation ID，是会话的唯一标识。会话是用户和智能体之间围绕某个主题的一段问答交互。一个会话包含一条或多条消息。​| 支持根据会话 ID 筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27125.21739130434784%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEyNS4yMTczOTEzMDQzNDc4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
用户 ID​| 和智能体对话的用户 ID。用户 ID 的类型取决于对话发生的渠道。​

  * 智能体商店&调试区：扣子用户的 UID。查看 UID 的方式可参考​查看 UID。​

  * API&SDK：调用​发起对话 API 时设置的 user_id 参数。​

  * 飞书等第三方渠道：展示第三方渠道中的用户 ID。详细说明可参考​消息列表中的用户 IDUser ID是什么？​

| 支持根据用户 ID 筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27120%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
用户输入​| 对话中用户输入的消息内容。​| 支持根据关键词筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27116.52173913043478%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjExNi41MjE3MzkxMzA0MzQ3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
输出​| 智能体或工作流的输出内容。​| 支持根据关键词筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27128.69565217391303%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEyOC42OTU2NTIxNzM5MTMwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
模型输入 Token​| 用户输入内容的 Token 长度，估算值，仅用于参考。​| 不支持筛选​​  
模型输出 Token​| 模型输出内容的 Token 长度，估算值，仅用于参考。​| ​不支持筛选​  
请求发起时间​| 请求的发起时间。​| 不支持筛选。​  
整体耗时​| 对话的总时长，单位为毫秒（ms）。从用户发起请求开始计算，到智能体最终回复完成为止。​| 支持根据整体耗时筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27139.1304347826087%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEzOS4xMzA0MzQ3ODI2MDg3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
首次响应耗时​| 智能体首次响应的处理耗时，单位为毫秒（ms）。从用户发起请求开始计算，到智能体或工作流返回第一个 Token 为止。​如果希望工作流尽早返回首个 Token，可配置输出节点。​| 支持根据首次响应耗时筛选消息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27116.52173913043478%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjExNi41MjE3MzkxMzA0MzQ3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
渠道​| 用户和智能体的对话发生的渠道。​在日志页面不支持查看豆包渠道的智能体消息日志。​| 支持筛选指定渠道的消息列表。只能筛选并查看智能体发布过的渠道。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27184.34782608695653%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE4NC4zNDc4MjYwODY5NTY1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

在消息列表中，你可以执行以下操作：​

​

操作​| 说明​  
---|---  
隐藏或显示指定列​| 列表中默认展示请求状态、名称、输入等部分信息，你也可以在页面右上角自定义设置展示哪些列。​  
刷新​| 单击刷新图标，即可刷新当前页签。​  
根据时间段筛选​| 支持根据以下方式指定时间：​

  * 指定时区：选择时区进行筛选，例如选择 UTC-12:00。​

  * 指定相对时间：例如过去 1 天、过去 3 天、过去 7 天等。​

  * 自定义时间范围：单击 Custom，设置开始时间与结束时间。​

  
下载​| 在日志页面右上角单击下载图标，即可将筛选后的消息导出到 .csv 文件中，并保存到本地。​  
  
​

查看数据统计​

页面右侧的统计区域展示筛选范围内消息日志的相关统计数据，包括：​

​

字段​| 说明​  
---|---  
消息数​| 筛选范围内的消息总数。​  
错误率​| 筛选范围内，错误消息数量在所有消息中的占比。​  
整体耗时​| 筛选范围内所有消息的平均整体耗时。​  
首次响应耗时​| 筛选范围内所有消息平均首次响应耗时。​  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27521%27%20height=%27385%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIxIiBoZWlnaHQ9IjM4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看消息请求全链路​

在日志页面的消息列表中单击指定消息，即可查看此消息的详细请求链路。调用树下选择具体节点，可查看：​

  * 节点详情：指定节点的详细信息，包括节点类型、状态、整体耗时等信息。​

  * 输入和输出：指定节点的输入和输出信息，JSON 格式展示扣子编程在此节点发起请求时的完整输入信息、完整输出信息。​

  * 链路拓扑：扣子编程在此节点的请求拓扑，对于工作流等节点，拓扑中会展示本次工作流的完整执行链路，你可以在此查看执行的节点名称与顺序。在左侧调用树中也可以单击工作流子节点名称右侧的图标，跳转到工作流试运行页面，查看本次请求的工作流运行过程与结果。​

关于消息请求的全链路信息详细说明，可参考​预览与调试。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27491.0982658959537%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ5MS4wOTgyNjU4OTU5NTM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

常见问题​

扣子的消息最多保存多久？​

仅智能体的所有者和协作者才能访问消息页面，不同扣子套餐支持的消息日志存储天数不一样，具体如下表所示。​

​

功能​| 个人免费版​| 个人进阶版​| 企业标准版​| 企业旗舰版​  
---|---|---|---|---  
消息日志存储天数​| 3天​| 7天​| 90天​| 180天​  
上报的消息数量​| 5 万条/月​| 10 万条/月​| 10 万条/月​| 200 万条/月​  
消息导出​| 不支持​| 每个智能体单次最多可导出 5000 条消息记录。​| ​| ​  
  
​

升级套餐后，消息保存天数如何生效？​

升级套餐后，新的消息保存天数规则将从升级当天开始计算，不会追溯之前的消息保存天数。例如，你当前是个人免费版，消息仅能保存 3 天。如果 5 月 1 日订阅了个人进阶版，此时你仍然只能查看 4 月 28 日~ 4 月30 日 这三天的消息。但从 5 月 1 日开始，消息保存天数变更为 7 天，到了 5 月 7 日，你就能看到 5 月 1 日~5 月 7 日的消息。​

可以导出消息吗？​

扣子付费套餐支持导出消息，个人免费版不支持导出消息。在日志页面右上角单击下载图标，即可将筛选后的消息导出到 .csv 格式的 Excel 文件中，并保存到本地。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27145.25462962962962%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjE0NS4yNTQ2Mjk2Mjk2Mjk2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

消息列表中的用户 ID是什么？​

消息列表中的用户 ID是和智能体对话的用户 ID。用户 ID 的类型取决于对话发生的渠道。详细说明如下：​

​

渠道​| 用户 ID 示例​| 说明​  
---|---|---  
智能体商店&调试区​| 737618761376343****​| 扣子用户的 UID。查看 UID 的方式可参考​查看 UID。​  
API&SDK​| 12345****​| 调用​发起对话 API 时设置的 user_id 参数。​  
飞书​| 736588c9260f****#93f8****​| 飞书的租户 Key 及 OpenID，格式为 TenantKey#open_id。​  
抖音​| _000qxLv3hSueysm05WV925wziQRlFfx****​| 用户在 Coze 应用上的 open_id。​抖音渠道包括抖音小程序、抖音企业号。​  
微信服务号、微信订阅号​| gh_63a996234fa3_o0A3K6cqH****-2-cC_0jZrS****​| 微信 origin_id 和 user_id的拼接，格式为 {{originalID}}_{{userID}}。​微信渠道包括微信客服、微信小程序、微信服务号、微信订阅号。​  
微信客服​| wmpyqxdwaacyi1zouwwpjrppgrcr****​| external_userid​  
微信小程序​| ouao3618yko28my12carsrho****​| 微信小程序用户的 openid。​  
  
​

如何查看用户与智能体的对话记录？​

智能体的开发者可通过消息日志功能查看对话记录，具体请参见​查看消息日志。但需注意目前豆包侧的消息记录暂不支持展示。​

​

​

上一篇

数据分析

下一篇

管理发布产物