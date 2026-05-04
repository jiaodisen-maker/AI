---
source_url: https://docs.coze.cn/guides/deploy_agent_as_api_service
title: '部署智能体 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:22Z
---

# 部署智能体 - 文档 - 扣子

部署智能体

本文介绍如何将你在扣子 AI 编程开发的智能体，部署为 API 服务或 Web SDK。部署为 API 服务，让你可以通过 OpenAPI 方式将智能体的 AI 功能灵活集成到应用中。部署为 Web SDK，将提供网页嵌入式聊天窗口，用户可直接在网页中与智能体进行对话。​

使用限制​

仅智能体的所有者有权限执行部署操作，且可创建的项目数量、部署次数等均存在配额限制。详情请参见​配额与限制。​

准备工作​

在开始部署之前，请确保你已通过扣子编程开发智能体，且试运行通过。具体可参考​开发智能体。​

部署操作​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的智能体，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27383%27%20height=%27443%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/50f8143c629b422a8ce756b54c5540ca~tplv-goo7wpa0wc-quality:q75.image)​

​

2.

在 AI 编程开发界面的右上角，单击部署。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27487%27%20height=%27410%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg3IiBoZWlnaHQ9IjQxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

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

  * 部署 > 总览页面可查看每个部署版本的状态。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27765%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzY1IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调用渠道​

通过 API 调用​

智能体部署成功后，系统为其自动启用 API 渠道。该渠道默认开启且无法关闭，确保智能体始终可以通过编程方式调用。具体调用方式，请参见​通过 API 调用智能体。​

通过 Web SDK 调用​

如果你希望在网页中直接与智能体进行交互，需要手动开启 Web SDK 渠道。该渠道支持按需随时关闭。​

1.

在部署页面，单击渠道。​

2.

在渠道页签，开启 Web SDK。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9IjIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

开启 Web SDK 后，你可以按需选择嵌入方式（如 JavaScript、React 组件或 Iframe），将智能体嵌入到你的网页中。详情请参见​Web SDK（AI 编程）。​

分享智能体​

  * 将智能体的 API 请求示例分享给其他用户​

  * 在智能体开发页面右上角单击分享按钮，即可获取智能体的 API 请求示例并分享给其他用户。你需要将创建的 API Token 提供给对方，对方调用时需将该 API Token 包含在请求头的Authorization参数中。更多信息，请参见​创建 API Token。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27559%27%20height=%27206%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU5IiBoZWlnaHQ9IjIwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 将智能体的 Web SDK 分享链接分享给其他用户​

  * 在智能体开发页面右上角单击分享按钮，然后在分享产物页签，单击设为公开可见，即可获取智能体的 Web SDK 分享链接并分享给其他用户，其他用户可通过该链接在 Web 页面可视化体验该智能体。​

  * :::​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27567%27%20height=%27174%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY3IiBoZWlnaHQ9IjE3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

  * ​能调用历史部署版本的智能体或工作流吗？​

  * ​重新部署后，之前的 API Token 还能继续使用吗？​

  * ​忘了 API Token 怎么办？​

  * ​部署失败时如何修复？​

  * ​首次部署和二次部署的数据库同步策略有什么不同？​

​

上一篇

部署小程序

下一篇

部署工作流