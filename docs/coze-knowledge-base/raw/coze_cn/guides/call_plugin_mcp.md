---
source_url: https://docs.coze.cn/guides/call_plugin_mcp
title: '通过 MCP 方式调用付费插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:12Z
---

# 通过 MCP 方式调用付费插件 - 文档 - 扣子

通过 MCP 方式调用付费插件

扣子编程支持将扣子编程官方付费插件和三方付费插件封装为 MCP（Model Context Protocol）工具，便于开发者在支持 MCP Server 的平台（如 Trae、Cursor、Claude 等）轻松调用扣子编程插件。​

说明

目前仅支持将扣子编程官方付费插件和三方付费插件封装为 MCP 工具，不支持免费插件和资源库中的插件。​

​

功能简介​

扣子编程拥有海量的优质插件资源，涵盖图像处理、音视频生成、网页搜索、实用工具等多元领域，并支持通过 MCP 协议访问。开发者在支持 MCP Server 的平台中将插件部署为 MCP 工具后，即可直接调用这些插件。MCP 方式调用插件的功能特点如下：​

  * 提供简单易用的命令行配置方式，实现快速部署与启动。​

  * 与主流 AI 工具（如 Trae、Cursor、Claude）无缝集成。​

  * 支持设置临时凭证和长期凭证，遵循权限最小化原则，确保插件调用安全可控。​

例如，你可以在扣子编程获取新闻插件的 MCP 配置（包括调用地址和访问凭证），然后在 Trae 上将其配置为 MCP 工具，以实现在 Trae 中调用扣子编程的新闻插件查询新闻。​

说明

扣子编程还支持通过 API 方式调用付费插件。更多信息，请参考​调用插件工具。​

​

费用说明​

通过 MCP 方式调用付费插件的计费逻辑与在扣子编程调用付费插件一致，均根据插件调用量（次数、时长等）计费。各个付费插件的计费项及单价，请参考​插件费用。​

调用额度与 QPS​

本表格罗列了 MCP 方式和 API 方式的总月累计调用次数及 QPS 限制。​

说明

  * 套餐限制：扣子付费套餐​

  * 在工作流及智能体中调用插件的次数，不计入本调用额度。​

  * 当调用次数超过月累计调用次数上限时，系统将报错，你可以升级套餐获取更多的调用次数。​

  * 扣子编程会在月累计调用次数达到总次数的 50%、70%、80%、90% 和 100% 时，分别发送一次站内信和短信提醒。​

​

​

订阅套餐​| 个人免费版​| 个人进阶版​| 个人高阶版​| 个人旗舰版​| 企业标准版​| 企业旗舰版​  
---|---|---|---|---|---|---  
月累计调用次数上限​| 不支持调用​| 1000 次​| 1000 次​| 1000 次​| 5 万次​| 无限制​  
QPS​| 0​| 5​| 5​| 5​| 20​| 100，支持扩容至 200​具体操作，请参考​购买扩容服务。​  
  
​

步骤 1：获取插件的 MCP 配置​

在外部平台配置扣子编程插件的 MCP 服务前，你需要先在扣子编程获取该插件的 MCP 配置。插件的 MCP 配置支持设置临时凭证和长期凭证，你可以先使用临时凭证进行测试，确认能正常调用插件后，再替换为长期凭证。​

注意

请妥善保管你的调用凭证，请勿泄露，避免他人冒用你的身份调用插件，造成不必要的资金损失。​

​

临时凭证​

系统将基于 callTool、getPlugin 接口权限生成临时凭证，有效期为 1 天，过期后需要重新生成。​

1.

在[扣子插件商店](<https://www.coze.cn/store/plugin?cate_type=recommend&cate_value=recommend>)，单击目标付费插件。​

2.

在插件详情页面的右上角，单击 MCP 调用。​

3.

在 MCP 调用对话框中，单击生成临时凭证。​

4.

单击复制图标，复制 MCP 配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27240%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjI0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

长期凭证​

如果你需要使用长期凭证，需创建扣子编程的访问令牌，支持个人访问令牌、服务访问令牌和 OAuth 访问令牌。​

1.

创建访问令牌。具体操作，请参考​获取访问令牌。​

  * 权限：至少包含插件管理中 callTool、getPlugin 权限。​

  * 有期限：根据业务需求选择对应的有效期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27289%27%20height=%27230%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg5IiBoZWlnaHQ9IjIzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

复制访问令牌。​

3.

在[扣子插件商店](<https://www.coze.cn/store/plugin?cate_type=recommend&cate_value=recommend>)，单击目标付费插件。​

4.

在插件详情页面的右上角，单击 MCP 调用。​

5.

在 MCP 配置的 Authorization 中，手动替换为你所创建的访问令牌。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27378%27%20height=%27351%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc4IiBoZWlnaHQ9IjM1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤 2：配置 MCP 服务​

获取到插件的 MCP 配置后，你可以在支持 MCP Server 的平台上配置 MCP 服务。本文以 Trae 为例，演示在 Trae 平台配置 MCP 服务的步骤。​

1.

在 Trae 客户端，单击设置图标，然后在 MCP 页签下，单击手动添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271128%27%20height=%27638.8436018957347%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEyOCIgaGVpZ2h0PSI2MzguODQzNjAxODk1NzM0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27227%27%20height=%27311%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI3IiBoZWlnaHQ9IjMxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

输入你已复制的 MCP 配置信息，单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27354%27%20height=%27308%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU0IiBoZWlnaHQ9IjMwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27412%27%20height=%27107%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEyIiBoZWlnaHQ9IjEwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤3：调用插件​

在外部 AI 开发客户端（如 Trae）中配置好插件的 MCP 服务后，输入自然语言即可调用插件功能。​

你可以在提示词中指定插件名称及任务内容，例如调用 getToutiaoNews 插件搜索今天新闻，也可以直接输入任务内容，系统会自动分析任务并调用对应的插件，例如搜索今天新闻。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27423%27%20height=%27452%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIzIiBoZWlnaHQ9IjQ1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

基于 MCP 服务创建插件

下一篇

提示词优化插件