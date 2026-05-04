---
source_url: https://docs.coze.cn/guides/integrate_storage
title: '集成对象存储能力 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:01Z
---

# 集成对象存储能力 - 文档 - 扣子

集成对象存储能力

本文将帮助你快速上手扣子编程内置的对象存储服务，包括集成对象存储服务的基础介绍，以及在 AI 编程项目中接入对象存储服务、使用对象存储服务等指引。​

功能概述​

扣子编程内置的对象存储服务是专为 AI 编程项目设计的非结构化数据托管方案，支持图像、文档、音频、视频等各类文件的安全存储与高效管理。​

在开发 AI 编程项目过程中，你可以通过自然语言与扣子 AI 对话，让其为你开发的 AI 编程项目添加存储功能，也可以在可视化界面中手动配置，轻松实现文件上传与托管。​

功能特征如下：​

  * 持久化存储：采用高可靠性存储架构，确保文件长期稳定留存，供用户或 AI 编程项目访问。​

  * 多层环境隔离：​

  * 环境隔离：开发环境和生产环境物理独立，确保开发阶段的文件操作不影响线上环境。​

  * 项目隔离：不同 AI 编程项目的对象存储相互独立，文件访问权限隔离，保障数据安全。​

  * 无缝服务集成：将对象存储功能封装为标准化集成服务，可被扣子 AI 直接调用添加。​

开发与生产环境​

为项目接入对象存储能力后，你的 AI 编程项目将具备两个数据完全隔离的存储环境，即开发环境和生产环境。​

​

环境类型​| 开发环境​| 生产环境​  
---|---|---  
适用阶段​|  AI 编程项目开发/调试阶段​|  AI 编程项目部署上线后​  
说明​| 开发阶段仅创建开发环境存储桶。​在向量化写入数据到数据库时，系统将在对象存储中自动生成 coze_knowledge_origin、coze_knowledge_base 文件夹。更多信息，请参考​数据向量化写入与检索。​| 生产环境存储桶在首次部署项目时自动创建，部署前不支持手动开通生产环境存储桶。​首次部署时，系统会自动创建生产环境的存储桶。每次部署均会同步 coze_knowledge_base 文件夹及其文件到生产环境，不会同步其他文件。当你需要将开发环境中的文件同步到生产环境时，可以上传文件到 coze_knowledge_base 文件夹中。​  
  
​

权限说明​

只有 AI 编程项目的所有者，拥有其对应对象存储服务的操作权限。​

使用限制​

  * 每个项目均只提供一个开发环境存储桶和一个生产环境存储桶。​

  * 最大支持上传 200MB 大小的文件。​

  * 文件 URL 有效期为 0～30天。​

  * 不支持上传 PHP 文件。​

费用说明​

  * 在项目开发过程中，你与扣子 AI 的每轮对话均会产生扣子编程任务费用，更多信息，请参加​扣子编程任务费用。​

  * 目前免收存储、数据库、向量模型的内置集成费用，后续正式计费的时间计划与产品定价请关注平台公告。​

使用对象存储​

为项目接入对象存储能力​

你在开发 AI 编程项目时，可以与扣子 AI 对话为项目接入对象存储能力。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

3.

输入你的开发需求，然后进入 AI 编程环境。​

4.

等待项目初步开发完成后，通过自然语言与扣子 AI 对话，为项目接入对象存储服务。​

  * 例如输入：​

  * ​

Plain Text

复制

为我的工作流添加文件存储功能​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9IjI4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上传文件​

接入对象存储能力后，即可将各类文件上传至专属存储桶中。例如开发作品集应用时，可将作品上传至存储桶中，从而在应用内快速实现作品的展示与访问。​

1.

在 AI 编程环境的右上角，单击➕，然后在集成服务区域，单击对象存储。​

2.

在对象存储的文件管理页签中，单击上传文件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27472%27%20height=%27127%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcyIiBoZWlnaHQ9IjEyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择目标本地文件，完成上传。​

下载文件​

你可以在 AI 编程环境的对象存储页签中，将存储桶中的文件下载到本地。​

1.

在 AI 编程环境的右上角，单击➕，然后在集成服务区域，单击对象存储。​

2.

在对象存储的文件管理页签中，单击目标文件对应的··· > 下载。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27450%27%20height=%27143%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUwIiBoZWlnaHQ9IjE0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看文件​

你可以在 AI 编程环境的对象存储页签中，查看文件列表以及目标文件的大小、类型、创建时间及修改时间等信息。​

1.

在 AI 编程环境的右上角，单击➕，然后在集成服务区域，单击对象存储。​

2.

在对象存储的文件管理页签中，查看文件列表及相关信息。 ​

  * 单击目标文件，可以预览该文件。目前，图片、视频支持在线预览。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27470%27%20height=%27223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcwIiBoZWlnaHQ9IjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置 URL 有效期​

存储文件 URL 有效期为 0～30 天。在开发项目过程中，扣子 AI 会设置一个默认有效期，你也可以与扣子 AI 对话来调整。​

URL 是临时的访问凭证，每个文件还具备一个唯一且固定的标识符（URI）。如果你需要某文件长期有效访问，可以让扣子 AI 将文件 URI 存储到数据库中，再基于 URI 重新获取一个 URL。例如输入对话：​

​

Plain Text

复制

将存储在对象存储桶里的图片的URI存入数据库中，每次获取URL时，根据URI重新换取URL。​

​

管理对象存储​

在 AI 编程环境的对象存储页签中，你还可以进行如下相关操作。​

​

分类​| 操作​| 说明​| 图示​  
---|---|---|---  
管理文件夹​​| 创建文件夹​| 单击新建文件夹，创建文件夹，用于归类与管理文件。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271909%27%20height=%27322.2987012987013%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwOSIgaGVpZ2h0PSIzMjIuMjk4NzAxMjk4NzAxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
​| 重命名文件夹​| 在文件夹及文件列表中，单击目标文件夹对应的··· > 重命名，修改文件夹名称。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271265%27%20height=%27262.8571428571429%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI2NSIgaGVpZ2h0PSIyNjIuODU3MTQyODU3MTQyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
​| 删除文件夹​| 在文件夹及文件列表中，单击目标文件夹对应的··· > 删除，删除文件夹。​说明

  * 删除文件夹时，文件夹内的文件会被同步删除。在执行删除时添加的文件，也会被同步删除。​

  * 删除操作无法恢复，请谨慎操作。​

​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271261%27%20height=%27262.02597402597405%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI2MSIgaGVpZ2h0PSIyNjIuMDI1OTc0MDI1OTc0MDUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
​| 复制文件夹路径​| 在文件夹及文件列表中，单击目标文件夹对应的··· > 复制文件夹路径，复制文件夹的路径。在移动文件到文件夹时，你需要输入完整的文件夹路径。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271261%27%20height=%27245.64935064935065%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI2MSIgaGVpZ2h0PSIyNDUuNjQ5MzUwNjQ5MzUwNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
管理文件​| 移动文件到文件夹​| 在文件夹及文件列表中，选择一个或多个文件，单击对应的··· > 移动，将文件移动到目标文件夹中，进行管理。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271867%27%20height=%27703.1558441558442%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg2NyIgaGVpZ2h0PSI3MDMuMTU1ODQ0MTU1ODQ0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
​| 分享文件​​| 在文件夹及文件列表中，单击目标文件，然后单击获取URL，并选择有效期。​获取链接的用户，可以查看该文件。当文件链接超过有效期后，文件将不可访问。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271910%27%20height=%27992.2077922077921%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMCIgaGVpZ2h0PSI5OTIuMjA3NzkyMjA3NzkyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
​| 重命名文件​| 在文件夹及文件列表中，单击目标文件对应的··· > 重命名，修改文件名称。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271864%27%20height=%27653.6103896103896%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg2NCIgaGVpZ2h0PSI2NTMuNjEwMzg5NjEwMzg5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
​| 删除文件​| 在文件夹及文件列表中，单击目标文件对应的··· > 删除，删除文件。​说明删除操作无法恢复，请谨慎操作。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271867%27%20height=%27678.9090909090909%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg2NyIgaGVpZ2h0PSI2NzguOTA5MDkwOTA5MDkwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
管理对象存储服务​​| 查看存储容量​| 在对象存储的总览页面，查看开发环境、生产环境中已使用的存储容量。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271908%27%20height=%27346.90909090909093%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwOCIgaGVpZ2h0PSIzNDYuOTA5MDkwOTA5MDkwOTMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
​| 删除对象存储服务​| 在对象存储的设置页签下，单击删除桶，删除当前项目的对象存储服务。​在此处删除对象存储服务，不会触发代码更新，也不会影响项目的其他功能。你也可以通过与扣子 AI 对话，修改代码，删除代码中关于对象存储服务调用的相关逻辑。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271911%27%20height=%27421.9090909090909%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMSIgaGVpZ2h0PSI0MjEuOTA5MDkwOTA5MDkwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
通过 SDK 方式访问对象存储​| ​| 扣子编程官方提供的 Coze Storage Client Python SDK，采用同步实现方式，用于管理 Client 与 Coze S3 兼容存储的交互。通过该 SDK，你可以以编程方式上传、下载、删除文件，检查对象是否存在，以及通过 Coze S3 Proxy 生成签名下载 URL。更多信息，请参考​存储 Python SDK。​| 无​  
  
​

常见问题​

  * ​各个项目之间的存储桶是共享的吗？​

  * ​如何为项目接入对象存储能力？​

上一篇

数据向量化写入与检索

下一篇

存储 Python SDK