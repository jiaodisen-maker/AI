---
source_url: https://docs.coze.cn/guides/version_management
title: '版本控制 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:36Z
---

# 版本控制 - 文档 - 扣子

版本控制

通过扣子编程开发应用、智能体和工作流的过程中，扣子编程为代码和产物变更提供类似 Git 的版本控制能力，适用于开发过程中需要追溯代码变更、回滚错误版本等场景。你可以清晰地追溯每一次代码变更，对比不同版本间的差异，并在需要时恢复到任意历史版本。本文介绍扣子编程中版本控制的相关操作。​

版本控制概述​

你在扣子编程开发应用、智能体或工作流过程中，扣子编程会自动生成一个版本，并自动将这些版本的代码存档并生成版本记录，从而实现精细化的版本控制与回退。​

主要功能​

扣子编程的版本控制功能主要包括：​

  * 自动存档：在日常开发过程中，代码变更时会生成新的版本，扣子编程会自动将当前的代码存档，形成一个新的版本记录。​

  * 查看版本历史：清晰地列出每一次提交的版本历史，包括详细的 Commit 信息，方便你追溯每一次变更。​

  * 搜索版本：支持通过版本标题或 Commit 信息中的关键词进行搜索，帮助你快速定位到特定的版本。​

  * 变更对比（Diff）：你可以查看任意一次提交所涉及的所有文件变更，并进行文件级的差异对比（Diff），直观地了解代码的新增、修改和删除。​

  * 回滚版本：当需要恢复到某个历史版本时，可以一键执行回滚操作。​

版本类型​

版本列表中的版本分为以下几种类型：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27325.7229832572298%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/19bbfa54edeb4d48844d1bc015de5a5b~tplv-goo7wpa0wc-quality:q75.image)​

​

​

版本类型​| 图中序号​| 说明​  
---|---|---  
Initial commit 版本​| ①​| 项目初始化时自动生成的初始版本。版本列表中关键词为 Initial commit的版本。​  
feat 版本​| ②​| 代码变更时，扣子编程自动将当前代码存档并生成的版本。版本列表中关键词为 feat 的版本。​  
Restored 版本​| ③​| 执行版本回滚操作后自动创建的新版本。版本列表中关键词为 Restored 的版本。​  
Auto commit 版本​| ④​| 若你手动修改文件后未提交，直接执行回滚或部署操作时，扣子编程会自动创建一个 Auto commit 版本，以确保手动修改的文件变更不会丢失。版本列表中关键词为 auto commit的版本。​  
  
​

使用限制​

  * 权限限制：仅项目所有者有权限执行版本控制操作。​

  * 回滚版本限制：不支持回滚以下类型的版本：​

  * 最新版本。​

  * Auto commit 版本。​

  * Restored 版本。​

使用方式​

自动存档​

在日常开发过程中，编程 AI 修改代码后会生成新的版本，扣子编程会自动将当前的代码存档，形成一个新的版本记录。​

1.

进入 AI 编程开发页面，在左侧对话框中描述需要修改的功能，触发代码变更，例如：列表页的默认条数修改为每页显示 20 条，并在底部增加‘加载更多’按钮。​

2.

扣子编程修改代码后，会自动提交一个版本，并根据变更内容自动生成摘要（Commit Message）。​

3.

你可以在对话框上方的版本卡片中单击查看修改记录，在版本控制页面查看该版本变更的详细信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27304.97685185185185%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwNC45NzY4NTE4NTE4NTE4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

手动提交​

如果你手动修改了代码文件，则必须手动提交版本，并填写摘要。操作步骤如下：​

1.

在文件区域单击图标，打开源代码管理页面。​

2.

单击文件名称，查看文件的详细变更对比。​

3.

确认无误后，填写版本摘要，并单击提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27503%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAzIiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

手动编辑场景下，除了基础的手动提交功能以外，你还可以：​

  * 放弃更改：放弃本次变更，将文件内容回退到上一个版本。​

  * 暂存变更：暂存当前的变更，以便在后续提交时合并到其他版本中。​

  * 添加到 .gitignore：将文件添加到 .gitignore 文件中，以便在后续提交时忽略该文件。​

在想要操作的文件上单击右键，即可执行以上操作。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27451%27%20height=%27266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUxIiBoZWlnaHQ9IjI2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看版本差异​

你可以随时查看任一历史版本的具体代码变更。​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的项目，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27212.96296296296296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIxMi45NjI5NjI5NjI5NjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在 AI 编程开发页面，你可以通过如下两种方式进入版本控制页面，看目标版本变更的文件，包括新增、修改、删除的文件列表。​

  * 对话区版本历史图标

右侧的新标签页

单击对话区顶部的版本历史图标，在目标版本右侧单击查看修改记录图标。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27267.2955974842767%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI2Ny4yOTU1OTc0ODQyNzY3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

3.

单击对应的文件，即可查看该文件的详细变更差异。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27537.5%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjUzNy41IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

回滚开发版本​

当你需要将项目恢复到某个特定的历史版本时，可以使用版本回滚功能，回滚后会撤销该版本之后的所有更改。此操作通常用于撤销错误的修改或恢复到某个稳定的功能节点。​

版本回滚后，在版本记录中会新增一条版本记录。回滚并不会删除历史记录，而是会创建一个新的版本，其内容与你选择回滚到的目标版本完全一致。​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的项目，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27212.96296296296296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIxMi45NjI5NjI5NjI5NjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在 AI 编程开发页面，你可以通过如下方式进行版本回滚。​

  * 对话区版本历史图标

右侧的新标签页

单击对话区顶部的版本历史图标，在目标版本右侧单击回滚图标。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27234.22897196261684%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIzNC4yMjg5NzE5NjI2MTY4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

3.

在回滚确认对话框中，如果项目集成了数据库，根据需要选择是否回滚数据库。如果勾选同时回滚数据库，系统将把开发环境数据库还原至对应版本状态，该版本之后添加的数据将丢失，包括 Schema 以及数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27247.0308788598575%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI0Ny4wMzA4Nzg4NTk4NTc1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

单击回滚。​

相关文档​

如果要回滚已部署的历史版本，请参考​回滚部署版本。​

​

上一篇

AI 编程环境

下一篇

使用 Git 服务