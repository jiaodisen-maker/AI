---
source_url: https://docs.coze.cn/tutorial/intra-enterprise_agents_apps_channels
title: '为企业内 AI 应用选择发布渠道 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:31Z
---

# 为企业内 AI 应用选择发布渠道 - 文档 - 扣子

为企业内 AI 应用选择发布渠道

本文介绍如何为企业内部的扣子智能体或应用选择合适的发布渠道，以便企业内部用户安全、便捷地使用 AI 智能服务。​

渠道选择建议​

​

发布渠道​| 官方渠道​| 企业商店​| Web SDK​| API​| Chat SDK​  
---|---|---|---|---|---  
适用场景​| 非敏感、通用性强的工具。​| 涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的工具。​| 需要将应用界面嵌入到内部系统或第三方平台等场景。​| 核心业务流程自动化。​| 智能客服、知识问答等对话场景。​  
核心优势​| 零配置、易推广。​| 零配置、易推广。​| 

  * 完整应用界面无缝嵌入。​

  * 快速集成。​

| 

  * AI 能力与企业后端服务深度整合。​

  * 灵活定制前端。​

| 

  * 悬浮窗交互。​

  * 轻量化集成。​

  
开发成本​| 无额外开发成本。​| 无额外开发成本。​| 低。​| 高。​| 低。​  
支持对象​| 智能体、扣子应用​| 智能体、扣子应用、自定义插件​| 扣子应用​| 智能体、扣子应用​| 智能体、扣子应用​  
  
​

方式一：发布至扣子官方渠道​

对于不涉及企业核心业务或敏感数据的通用型应用，例如会议纪要整理、文档翻译等，开发者可以将智能体或扣子应用发布至扣子商店、豆包等公开渠道。具体请参见​将智能体上架到作品社区、​发布到豆包。​

企业内部用户可直接通过[扣子商店](<https://www.coze.cn/store/agent?cate_type=recommend>)等渠道搜索，便捷使用对应智能体或扣子应用。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27332.2543352601156%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/42bea05dc94e47b8a3851b754a96f1c3~tplv-goo7wpa0wc-quality:q75.image)​

​

方式二：发布至企业商店​

扣子企业旗舰版支持将智能体、扣子应用、自定义插件发布至企业商店。​

  * 企业项目：​

  * 对于涉及核心业务逻辑、数据敏感信息或仅限内部使用的企业内部智能体和应用，开发者可以将其发布至企业项目。企业项目是面向企业旗舰版用户的专属商店入口与发布渠道，企业项目中的智能体和应用仅本企业的员工和访客可见、可访问，非本企业成员无法浏览或使用，可有效防止内部资源外泄，保护企业数据隐私与知识产权。具体请参见​发布到企业商店、​发布到企业商店。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27221.96531791907512%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIyMS45NjUzMTc5MTkwNzUxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27237.5722543352601%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIzNy41NzIyNTQzMzUyNjAxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

  * 企业插件商店：​

  * 对于企业自主开发的自定义插件，可直接通过企业插件商店进行内部分发。既能避免内部资源外泄，保护企业知识产权与数据隐私，又能让企业成员便捷使用内部服务，提升协作效率。具体请参见​管理企业插件。​

方式三：发布为 Web SDK​

如果需要将扣子应用的用户界面作为完整功能模块、无缝嵌入到企业现有内部系统（如 OA、ERP）或第三方平台时，开发者可以将应用发布为 Web SDK，并将 Web SDK 的 JavaScript 代码集成到目标系统的 Web 页面，应用中的用户界面和工作流将作为一个完整的组件，嵌入到目标业务系统中。​

企业内部用户在业务系统内即可直接使用 AI 应用，降低学习成本。​

具体请参见​发布为 Web SDK、​Web SDK（低代码）。​

说明

仅扣子应用支持该方式，智能体不支持发布为 Web SDK。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27385.66473988439304%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM4NS42NjQ3Mzk4ODQzOTMwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

方式四：发布为 API​

如果需要将 AI 能力与企业后端服务深度整合，实现业务流程自动化的场景，开发者可以将智能体或扣子应用发布为 API。​

开发者需要自定义前端交互，企业后端服务调用扣子的 Open API ，将智能体或扣子应用集成到业务系统中，实现 AI 能力无痕融入现有业务逻辑。​

方式五：发布为 Chat SDK​

对于智能客服、知识问答等以对话为核心交互形式的场景，开发者可以将智能体或扣子应用发布为 Chat SDK，并将 Chat SDK 的代码集成到目标系统中，具体请参见​安装并使用 Chat SDK。​

内部用户单击右下角的悬浮图标，即可与 AI 智能体或应用对话。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27439.8843930635838%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQzOS44ODQzOTMwNjM1ODM4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

上一篇

入驻公共渠道

下一篇

如何在飞书使用扣子