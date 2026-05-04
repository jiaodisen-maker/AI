---
source_url: https://docs.coze.cn/guides/import_from_github
title: '导入项目 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:19Z
---

# 导入项目 - 文档 - 扣子

导入项目

除了从零开发以外，你还可以导入现有的代码文件，在扣子编程继续你的开发工作，或者通过扣子编程将其部署为线上服务。​

功能介绍​

通过导入项目功能，你可以将已有的代码工程快速迁移到扣子编程环境中，进行后续开发、调试和部署。扣子编程支持两种导入方式：​

  * 从 GitHub 导入：支持导入你的公开或私有 GitHub 仓库。项目导入后会自动与原仓库绑定，方便你进行代码的双向同步和版本控制。​

  * 从本地导入：支持通过上传 .zip 等格式的压缩包来导入项目。此方式不仅适用于迁移本地项目，也常用于项目在不同工作空间或企业间的备份与迁移。​

这项功能主要适用于以下场景：​

  * 迁移现有项目：将你在其他平台或本地开发的项目迁移至扣子编程，以利用其 AI 编程和云端开发环境。​

  * 快速部署服务：将已有的成熟项目导入，并直接使用扣子编程的部署能力，将其快速发布为在线应用或服务。​

  * 团队协同开发：团队成员可将同一个 GitHub 仓库导入进行协作开发，同时保持与标准 Git 工作流的一致性。​

  * 项目备份与迁移：通过“导出再导入”的方式，可以实现项目在不同扣子空间、甚至不同企业组织之间的安全迁移。​

准备工作​

从 GitHub 导入​

从 GitHub 导入项目时，自动导入仓库中所有文件，包括源码、静态资源和文档等。​

说明

暂不支持导入超过 500MB 的 GitHub 代码仓库。​

​

步骤一：GitHub 账号授权​

导入项目之前，需要先为工作空间配置 GitHub 账号授权。​

说明

  * 权限要求：空间所有者或管理员。​

  * 授权范围：指定工作空间。授权后，此工作空间下所有的 AI 编程项目都可以绑定这个账号下的代码仓库。​

​

操作方式如下：​

1.

登录[扣子编程](<https://code.coze.cn/>)。​

2.

找到要授权的工作空间。​

  * 免费版只有一个默认的个人空间，无需切换，可以直接跳过此步骤。​

  * 个人版

企业版

在页面左下角头像处切换工作空间。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27148%27%20height=%27208%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ4IiBoZWlnaHQ9IjIwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

3.

在左侧导航栏中，单击集成管理。​

4.

在 Git 服务页签中找到 GitHub，并单击配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27467%27%20height=%27187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY3IiBoZWlnaHQ9IjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

根据页面提示登录 GitHub 账号，并完成授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27127%27%20height=%27175%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI3IiBoZWlnaHQ9IjE3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * GitHub 服务一栏中，如果提示已配置，表示已完成账号授权和绑定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27503%27%20height=%27132%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAzIiBoZWlnaHQ9IjEzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：从 GitHub 导入​

1.

登录[扣子编程](<https://code.coze.cn/>)。​

2.

在左侧导航栏中，单击导入 > GitHub 导入。​

3.

选择需要导入的项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27259%27%20height=%27324%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU5IiBoZWlnaHQ9IjMyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

扣子编程自动执行初始化配置。​

  * 编程 AI 会自动从 GitHub 仓库中拉取项目代码，克隆到扣子编程项目中。这期间，还会自动查看并理解源码，补齐 AGENTS.md 等必要的内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27206%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjIwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

完成导入。​

  * 扣子编程完成项目初始化配置之后，会自动构建项目，你可以在页面右侧查看并调试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27452%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUyIiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

从本地导入​

除了从 GitHub 仓库导入，扣子编程也支持你上传本地项目压缩包来创建新项目。​

导入要求​

  * 文件格式：必须是压缩文件，格式为 .zip、.tar 或 .tar.gz。​

  * 文件结构：解压后必须是单个文件夹。​

  * 体积限制：文件夹内每个文件不超过 500 MB。​

操作步骤​

1.

登录[扣子编程](<https://code.coze.cn/>)。​

2.

在左侧导航栏中，单击导入 > 本地上传。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27468%27%20height=%27234%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY4IiBoZWlnaHQ9IjIzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择要上传的 Zip 文件，并单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27372%27%20height=%27278%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzcyIiBoZWlnaHQ9IjI3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

扣子编程自动执行初始化配置。​

  * 编程 AI 会自动解压你上传的文件，并将其作为项目源码。这期间，它还会自动查看并理解源码，补齐 AGENTS.md 等必要的项目内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27416%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE2IiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

完成导入。​

  * 扣子编程完成项目初始化配置之后，会自动构建项目，你可以在页面右侧打开新标签页，并单击预览来在线调试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27430%27%20height=%27240%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDMwIiBoZWlnaHQ9IjI0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

继续开发​

导入项目之后，如果你的项目还需要修改和优化、调试和修复，可以参考以下文档，与编程 AI 一起继续开发与调试。​

  * ​开发网页应用​

  * ​开发移动应用​

  * ​开发小程序​

  * ​开发智能体​

  * ​开发工作流​

后续操作​

1.

部署应用。​

  * 完成应用的开发与测试之后，你可以在页面右上角单击部署，将扣子编程搭建的应用部署成为一个公开可访问的在线项目，将你的创意和原型，转化为服务于真实用户的产品。详细操作步骤可参考​部署网页应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27465%27%20height=%27199%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY1IiBoZWlnaHQ9IjE5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

分享项目。​

  * 在项目搭建页面右上角单击分享按钮，可以将部署成功的项目分享给他人。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271420%27%20height=%27359.93055555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQyMCIgaGVpZ2h0PSIzNTkuOTMwNTU1NTU1NTU1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看线上日志​

查看已发布的应用、智能体和工作流的前后端运行日志，以便在出现问题时进行故障排查和分析。详细说明可参考​查看日志和 Trace。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27462%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYyIiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上一篇

开发工作流

下一篇

技能概述