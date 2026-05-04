---
source_url: https://docs.coze.cn/guides/deploy_vibe_workflow
title: '部署工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:26Z
---

# 部署工作流 - 文档 - 扣子

部署工作流

本文介绍如何将你在扣子 AI 编程开发的工作流，部署为 API 服务或 Web SDK。部署为 API 服务，让你可以通过标准的 OpenAPI 方式，将工作流的自动化处理能力灵活集成到你的后端服务或应用中。部署为 Web SDK，会自动为你生成一个可视化的操作界面。该界面包含工作流的输入表单和结果展示区，你可以将其作为一个即用型组件，轻松嵌入到任何网站页面中，方便用户直接通过图形界面来执行工作流。​

使用限制​

仅工作流的所有者有权限执行部署操作，且可创建的项目数量、部署次数等均存在配额限制。详情请参见​配额与限制。​

准备工作​

在开始部署之前，请确保你已通过扣子编程开发工作流，且试运行通过。具体可参考​开发工作流。​

部署操作​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的工作流，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27453%27%20height=%27312%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/56004474158f4637bd28f3bf25af37f7~tplv-goo7wpa0wc-quality:q75.image)​

​

2.

在 AI 编程开发界面的右上角，单击部署。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27347.8009259259259%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c2405ecf544549a08e4e23ac39698c60~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

填写部署配置。​

  * ​

配置​| 说明​  
---|---  
部署版本​| 选择要部署的开发版本。​  
数据库​| 仅在集成了数据库能力时需要配置。用于设置是否隔离生产环境和开发环境的数据。​首次部署时，你可以设置是否将开发环境的数据同步至生产环境。​
    * 关闭：仅同步开发环境中的数据表结构，不同步数据。​
    * 开启：将开发环境中的数据表结构和数据完全同步到生产环境。​
后续部署时，扣子编程仅同步开发环境的表结构变更，不同步具体数据。​  
生产环境变量​| 在生产环境中为项目配置特定的环境变量，例如 API Key、数据库连接字符串、飞书文档地址等敏感信息，以免将这些信息硬编码在代码中导致安全风险。​展开环境变量的下拉列表，你可以新建环境变量、查看本次部署新增和变更的环境变量。关于环境变量的具体说明请参考​管理环境变量。​说明部署时新建的变量，仅在生产环境生效，不会被添加至开发环境。​​  
更多配置​| 扣子编程自动为 AI 编程项目分配合理的服务器资源，如需查看资源配置、构建指令、端口等高级部署配置，你可以展开更多配置，查看配置详情。​这些配置不支持修改，只能查看。​  
  
​

4.

单击开始部署。​

  * 扣子编程将自动进行部署相关操作。你可以在部署页面查看部署的进展和部署日志。部署过程可能需要几分钟，请耐心等待。部署过程中，你可以随时取消部署。​

调用渠道​

通过 API 调用​

工作流部署成功后，系统为其自动启用 API 渠道。该渠道默认开启且无法关闭，确保工作流始终可以通过编程方式调用。具体调用方式，请参见​通过 API 调用工作流。​

通过 Web SDK 调用​

如果你希望将工作流作为一个即用型组件嵌入网站，让用户通过可视化的表单提交任务并查看结果，需要手动开启 Web SDK 渠道。该渠道支持按需随时关闭。​

1.

在部署页面，单击渠道。​

2.

在渠道页签，开启 Web SDK。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27586%27%20height=%27230%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg2IiBoZWlnaHQ9IjIzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

开启 Web SDK 后，你可以按需选择嵌入方式（如 JavaScript、React 组件或 Iframe），将工作流嵌入到你的网页中。详情请参见​Web SDK（AI 编程）。​

分享工作流​

  * 将工作流的 API 请求示例分享给其他用户​

  * 在工作流开发页面右上角单击分享按钮，然后在分享产物页签，单击 Curl 调用示例的复制按钮，即可获取工作流的 API 请求示例并分享给其他用户。你需要将创建的 API Token 提供给对方，对方调用时需将该 API Token 包含在请求头的Authorization参数中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27672%27%20height=%27266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcyIiBoZWlnaHQ9IjI2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 将工作流的 Web SDK 分享链接分享给其他用户​

  * 在工作流开发页面右上角单击分享按钮，然后在分享产物页签，单击设为公开可见，即可获取工作流的 Web SDK 分享链接并分享给其他用户，其他用户可通过该链接在 Web 页面可视化体验该工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27675%27%20height=%27218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc1IiBoZWlnaHQ9IjIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

  * ​能调用历史部署版本的智能体或工作流吗？​

  * ​重新部署后，之前的 API Token 还能继续使用吗？​

  * ​忘了 API Token 怎么办？​

  * ​部署失败时如何修复？​

  * ​首次部署和二次部署的数据库同步策略有什么不同？​

上一篇

部署智能体

下一篇

回滚部署版本