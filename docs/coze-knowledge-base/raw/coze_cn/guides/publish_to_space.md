---
source_url: https://docs.coze.cn/guides/publish_to_space
title: '发布为 MCP 工具 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:45:11Z
---

# 发布为 MCP 工具 - 文档 - 扣子

发布为 MCP 工具

MCP 工具是基于模型上下文协议（Model Context Protocol，MCP）的一种工具实现，它允许服务器向客户端暴露可执行的功能。通过 MCP 工具，大语言模型（LLM）可以按需自动执行计算、操作外部系统，甚至与真实世界交互。扣子应用现已支持发布为 MCP 工具，可作为扣子空间的扩展能力，帮助用户在扣子空间内实现更丰富的功能，为扣子空间增加垂直领域的私有知识、数据、工具等等。​

什么是 MCP​

MCP 是一种开放协议，它规范了应用程序向大语言模型提供上下文的方式。你可以将 MCP 理解为扣子空间的插件系统，它允许你通过标准化的接口，将扣子空间的 AI Agent 与各种外部工具、数据源相连接。通过 MCP 扩展，大语言模型（LLM）可以按需自动执行计算、操作外部系统，甚至与真实世界交互。关于 MCP 的更多信息，请参考 [MCP 官方文档](<https://modelcontextprotocol.io/introduction>)。​

MCP 可以帮助你在大语言模型的基础上构建智能体和复杂的工作流。大语言模型常常需要与数据和工具进行集成，而 MCP 提供了：​

  * 一系列不断增加的预构建集成，让大模型可以直接接入这些集成。​

  * 能够在不同的大语言模型提供商和供应商之间灵活切换。​

  * 在你的基础设施内保障数据安全的最佳实践方法。​

MCP 扩展库​

扣子提供了一系列官方 MCP 扩展供你使用，常见的官方 MCP 扩展详细说明可参考​官方 MCP 扩展。​

如果你的任务还需要添加私有知识、数据，或者集成一系列定义好的流程节点，你也可以在扣子编程中搭建扣子应用，并将其发布为 MCP 扩展，为扣子空间增加垂直领域的私有知识、数据、工具等等。扣子编程为你提供了简单易用但能力上限极高的 AI 应用开发脚手架，在这里你可以快速开发、调试各种流程工具，并快速发布到包括扣子空间扩展库在内的丰富渠道。​

说明

扣子空间调用扣子应用对应的自定义 MCP 扩展完成任务时，会产生模型 Token 等资源用量，扣子编程会根据每次调用的实际 Token 数量从扣子账号中扣减对应的积分。你可以在积分的消费历史中查看明细。​

​

官方 MCP 扩展​

说明

在使用过程中，可能需要你进行环境变量配置、授权等操作。​

​

扣子空间集成了丰富的 MCP 扩展，为你提供了全面的功能支持。对于通用的 MCP 扩展，扣子空间已直接将其内置到主 Agent 中，在 Agent 执行任务过程中，会自动选择并调用合适的 MCP 扩展，无需你额外配置。此外，扣子空间还提供了一系列个性化的 MCP 扩展，这些扩展已上传至扩展库。​

扩展库中常用的 MCP 扩展如下所示。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27372%27%20height=%27417%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzcyIiBoZWlnaHQ9IjQxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

MCP 扩展​| 说明​  
---|---  
高德地图​| 高德地图官方 MCP 扩展，支持查询地点、搜索周边、规划不同交通工具的路线、经纬度与位置的转换等功能。​  
飞书云文档​| 支持在你的飞书文档空间中进行检索、创建、编辑飞书文档等操作。​  
飞书多维表格​| 支持在你的飞书文档空间中进行检索、创建、编辑飞书多维表格等操作。​  
飞书电子表格​| 支持在你的飞书文档空间中进行检索、创建、编辑飞书电子表格等操作。​  
水滴信用​| 支持全国企业信用信息查询，包括企业工商数据、股权结构、司法行政风险等信息。​  
飞常准​| 支持查询全球航班状态、航班号、预计出发/降落时间等信息。​  
音乐生成​| 支持生成不同风格的高质量歌曲，支持男/女声等不同音色。​  
墨迹天气​| 天气查询工具，可提供省、市、区县的未来 40 天的天气情况，包括温度、湿度、日夜风向等信息。​  
图像工具​| 支持生成高质量图片以及编辑已有图像。​  
语音合成​| 支持将文本转化成不同音色的人声音频。​  
Notion​| 支持 Notion 文档和数据表的创建、读取、编辑、更新、搜索、查询等操作。​  
Github​| 支持搜索 Github 仓库、文件、代码、用户，并支持查询 issue。申请 Personal Access Token，请参考 [modelcontextprotocol/servers](<https://github.com/modelcontextprotocol/servers/tree/main/src/github>)。​  
MySQL​| 支持连接并执行 MySQL 查询请求。​  
Clickhouse​| 支持对 ClickHouse 数据库的列取、数据表操作和只读 Query 执行功能，详情请参考[mcp-clickhouse](<https://github.com/ClickHouse/mcp-clickhouse>)。​  
  
​

自定义 MCP 扩展​

为什么需要自定义 MCP 扩展​

  * 对于某些要求严格根据流程执行的任务，Agent 不一定每次都按照固定的流程执行，而自定义的 MCP 扩展可以约束 Agent 按照固定的步骤稳定执行任务。例如，在数据分析场景，通用 Agent 通常会通过写 Python 代码来处理数据，每次执行的代码可能都不同，但如果你开发了一个数据分析的扣子应用，则可以稳定地使用你预设的逻辑和分析方法处理数据。​

  * 通用 Agent 常常缺少解决任务必须的私有数据和知识，此时你可以通过自定义扩展为 Agent 提供这些内容。例如通过自定义扩展让 Agent 通过你已搭建的达人数据库帮你筛选最合适的推品达人。​

  * 自定义扩展也可以为扣子空间通用 Agent 赋予一些垂直领域的能力，比如根据房型设计装修图、搭建 3D 模型、发送消息等等。​

发布应用为 MCP 工具​

注意事项​

将应用发布为 MCP 工具，应注意：​

​

限制​| 说明​  
---|---  
工作流​| 

  * 输出节点不生效，发布后只会返回结束节点的最终输出​

  * 暂不支持以下工作流发布为 MCP 工具：​

  * 对话流​

  * 包含创建会话等会话管理类节点的工作流​

  * 包含端插件节点、问答节点、输入节点等中断节点的工作流​

  
权限​| 扣子应用的发布者必须是应用的所有者。发布后仅应用所有者本人可在扣子空间中使用​  
费用​| 如果扣子空间在执行任务时，自动调用了此 MCP 工具，扣子编程会根据实际产生的模型 Token 等资源用量，自动扣减对应的扣子积分。扣子编程的收费标准可参考​计费概述。​  
名称与图标​| MCP 工具名称和图标默认为扣子应用的名称和图标。​  
  
​

操作步骤​

以下是发布到商店的详细步骤：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择你要发布的低代码应用，进入应用的编排页面。​

4.

在页面右上角，单击发布，进入发布页面。​

5.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。​

  * 版本描述：可选，说明该版本更新的内容。​

6.

填写扩展配置。​

a.

在选择发布平台 > MCP 服务选项，找到扣子空间扩展库，并单击配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27193.5185185185185%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE5My41MTg1MTg1MTg1MTg1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

b.

选择要发布为 MCP 工具的工作流，并单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27349%27%20height=%27208%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ5IiBoZWlnaHQ9IjIwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

确认已选择扣子空间扩展库，并单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27216.66666666666666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIxNi42NjY2NjY2NjY2NjY2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

确认发布成功。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27297%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk3IiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在扣子空间使用 MCP 工具​

将应用中的指定工作流发布为 MCP 工具之后，你就可以在扣子空间中开启 MCP 工具扩展，并创建任务。MCP 工具默认是模型控制，即大模型会按需自动调用 MCP 工具完成任务，例如进行简单的计算、复杂的 API 交互，或查看私有知识与数据。​

添加 MCP 工具​

在扣子空间中创建任务之前，单击扩展并添加你的自定义 MCP 工具即可。​

点击扩展：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27425%27%20height=%27155%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI1IiBoZWlnaHQ9IjE1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

添加扩展：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273144%27%20height=%271677.439024390244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE0NCIgaGVpZ2h0PSIxNjc3LjQzOTAyNDM5MDI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

调用 MCP 工具​

任务执行过程中，扣子空间会自动调用工具完成任务，你可以通过 Agent 的思考过程来判断是否已调用工具。例如 MCP 工具的功能为解析抖音视频，其中工作流名为 douyin_video_parse，当创建一个需要解析抖音视频的任务时，可以看到 Agent 调用了 douyin_video_parse 来解析视频。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27603%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAzIiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看 MCP 工具的调用记录​

将扣子应用发布为 MCP 工具之后，你可以在发布管理页面查看此 MCP 工具在扣子空间中的调用记录。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27601%27%20height=%27301%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAxIiBoZWlnaHQ9IjMwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

扣子空间调用扣子应用对应的 MCP 工具完成任务时，会产生模型 Token 等资源用量，扣子编程会根据每次调用的实际 Token 数量从扣子账号中扣减对应的积分。你可以在积分的消费历史中查看明细。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27587%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg3IiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

下架应用​

如果不再需要在扣子空间中展示该 MCP 工具，你可以选择将其下架。下架的操作步骤请参见​下架应用。​

​

上一篇

发布为模板

下一篇

发布为 Web SDK