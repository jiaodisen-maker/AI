---
source_url: https://docs.coze.cn/guides/environment_variables
title: '管理环境变量 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:06Z
---

# 管理环境变量 - 文档 - 扣子

管理环境变量

本文将帮助你快速上手扣子编程的环境变量功能，了解其在 AI 编程项目开发中的作用，及相关操作步骤。​

什么是环境变量​

扣子编程提供环境变量管理工具，用于将 AI 编程项目运行所需的信息以环境变量形式进行存储与管理，例如 API 密钥、数据库密码、鉴权 Token 等。通过将数据与代码分离，可有效避免硬编码风险，大幅提升 AI 编程项目的安全性、灵活性与合规性。支持以下两种类型的环境变量：​

  * 系统环境变量： 由平台内置并管理，以COZE_作为命名前缀。例如为 AI 编程项目接入数据库能力时，扣子 AI 会自动在代码中使用数据库相关的环境变量存储数据库的访问地址等信息。​

  * 自定义环境变量：由你根据项目需求自行创建。创建后，你需要与扣子 AI 对话，将环境变量写入项目代码中。​

核心特性如下：​

  * 应用级密钥管理：AI 编程项目维度独立管理环境变量。​

  * 生产与开发环境隔离：开发与生产环境完全隔离，避免开发调试阶段的配置变动影响线上运行。​

开发与生产环境​

扣子编程的环境变量区分开发环境和生产环境，数据完全隔离，避免开发阶段的配置变动影响线上业务运行。​

​

环境类型​| 适用阶段​| 说明​  
---|---|---  
开发环境​|  AI 编程项目开发/调试阶段​| 开发阶段仅创建开发环境的环境变量。​  
生产环境​|  AI 编程项目部署上线后​| 生产环境的环境变量在首次部署项目时进行配置，未部署前无法添加。​

  * 首次部署项目时，系统会自动同步开发环境的环境变量到部署页面，你可以调整环境变量，并发布到生产环境。​

  * 生产环境的环境变量只支持在发布管理页面进行配置，重新部署项目才能生效。​

  
  
​

权限说明​

仅 AI 编程项目的所有者具备对应环境变量的操作权限。​

使用环境变量​

你可以参考如下步骤创建并使用自定义环境变量。​

1.

创建自定义环境变量。​

a.

在[扣子编程](<https://code.coze.cn/home>)首页，按需输入你的开发需求，然后进入 AI 编程环境。​

b.

在 AI 编程环境的右上角，单击➕，然后在集成服务区域，单击环境变量。​

c.

在开发环境页签中，单击新建变量。​

d.

设置环境变量名称和值，单击确认。​

  * 说明

环境变量 Key 不允许以 COZE_ 开头，COZE_ 为系统环境变量专用前缀。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27573%27%20height=%27160%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTczIiBoZWlnaHQ9IjE2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

通过自然语言与扣子 AI 对话，将已创建的环境变量集成到项目代码中。​

  * 说明

创建自定义环境变量后，你需要通过对话，让扣子 AI 将其集成到业务代码中。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27560%27%20height=%27174%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYwIiBoZWlnaHQ9IjE3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例​

在开发识别发票并将识别结果发送到飞书多维表格的工作流时，工作流中会提供输入参数来配置飞书多维表格的 app_token 和 table_id。在该场景中，你可以：​

1.

创建环境变量 FEISHU_APP_TOKEN 和 FEISHU_TABLE_ID，并根据实际的app_token 和 table_id，配置环境变量值。​

2.

与扣子 AI 对话，更新代码，将这两个环境变量集成到业务代码中。​

运行工作流时，系统会自动读取环境变量中的配置值，你无需手动填写 app_token 和 table_id，即可将发票提取结果写入指定的飞书多维表格。如果你需要切换目标飞书多维表格，只需更新环境变量值。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271587%27%20height=%27889.1702127659574%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU4NyIgaGVpZ2h0PSI4ODkuMTcwMjEyNzY1OTU3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271379%27%20height=%27502.156862745098%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM3OSIgaGVpZ2h0PSI1MDIuMTU2ODYyNzQ1MDk4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

相关操作​

在 AI 编程环境的环境变量页签中，你还可以进行如下相关操作。​

​

操作​| 说明​| 图示​  
---|---|---  
修改环境变量​| 

  * 开发环境：在环境变量的开发环境页签中，找到目标环境变量，进行修改。​

  * 生产环境：在发布管理页面修改环境变量，并在修改后重新部署才能生效。​

说明

  * 修改环境变量 Key，系统不会自动更新代码，你需要让扣子 AI 调整相关配置或者自行调整相关代码，避免项目运行异常。​

  * 修改环境变量 Value 后，你可以重启 AI 编程项目，使变更生效。​

​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271906%27%20height=%27390.97435897435895%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwNiIgaGVpZ2h0PSIzOTAuOTc0MzU4OTc0MzU4OTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271356%27%20height=%27869.2307692307693%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM1NiIgaGVpZ2h0PSI4NjkuMjMwNzY5MjMwNzY5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​  
删除环境变量​| 

  * 开发环境：在环境变量的开发环境页签中，找到目标环境变量，选择更多 > 删除。​

  * 生产环境：在发布管理页面删除环境变量，并在删除后重新部署才能生效。​

说明删除环境变量并不会自动更新相关代码，你需要通过对话方式让扣子 AI 调整代码。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271361%27%20height=%27453.66666666666663%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM2MSIgaGVpZ2h0PSI0NTMuNjY2NjY2NjY2NjY2NjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
同步环境变量​| 在部署页面，如果你修改了环境变量名称或值，可以单击同步开发环境变量，一键同步开发环境变量。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271349%27%20height=%27864.7435897435898%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM0OSIgaGVpZ2h0PSI4NjQuNzQzNTg5NzQzNTg5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看环境变量​| 在环境变量页签中，查看开发环境或生产环境的环境变量。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271347%27%20height=%27483.53846153846155%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM0NyIgaGVpZ2h0PSI0ODMuNTM4NDYxNTM4NDYxNTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

常见问题​

  * ​各个项目之间的环境变量是共享的吗？​

上一篇

存储 Python SDK

下一篇

部署运维概述