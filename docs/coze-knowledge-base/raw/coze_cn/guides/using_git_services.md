---
source_url: https://docs.coze.cn/guides/using_git_services
title: '使用 Git 服务 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:38Z
---

# 使用 Git 服务 - 文档 - 扣子

使用 Git 服务

为了便于多人协作开发和远程备份，你可以将项目绑定到 GitHub 仓库，使用 Git 服务进行代码同步。​

功能介绍​

扣子编程的 Git 服务允许你将 AI 编程项目与 GitHub 仓库进行绑定和同步。​

  * 绑定仓库：将项目绑定到 GitHub 仓库，便于团队协作开发。​

  * Push 和 Pull：拉取和推送代码到 GitHub 仓库，实现代码的同步和备份。​

  * 解决冲突：可视化展示冲突的代码文件，帮助你解决冲突。​

  * 终端操作：对于习惯使用命令行的开发者，也可以在 AI 编程环境的终端中直接使用 Git 命令进行操作。​

注意事项​

  * 服务范围：Git 服务目前仅支持 GitHub。​

  * 同步范围：目前仅同步 main 分支，暂不支持创建或切换分支。​

准备工作​

在你的 AI 编程项目中使用 Git 服务之前，需要先为工作空间配置 GitHub 账号授权。​

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

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27659%27%20height=%27264%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU5IiBoZWlnaHQ9IjI2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

根据页面提示登录 GitHub 账号，并完成授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27194%27%20height=%27267%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk0IiBoZWlnaHQ9IjI2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * GitHub 服务一栏中，如果提示已配置，表示已完成账号授权和绑定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27668%27%20height=%27175%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjY4IiBoZWlnaHQ9IjE3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用方法​

在你已创建的 AI 编程项目中，通过以下方式使用 Git 服务。​

绑定仓库​

通过 Git 服务为 AI 编程项目设置并连接 GitHub 仓库，以便通过 GitHub 进行备份和多人协作。支持绑定新仓库或已有仓库。绑定步骤如下：​

1.

登录[扣子编程](<https://code.coze.cn/>)。​

2.

在左侧导航栏中，单击项目管理。​

3.

找到你的 AI 编程项目，并打开项目。​

4.

在右侧新建标签页，并选择版本控制。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27521%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIxIiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击绑定仓库。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27522%27%20height=%27255%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIyIiBoZWlnaHQ9IjI1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

新建仓库或选择一个已有仓库。​

  * 你可以在这里看到此账号下的所有仓库，如果仓库数量比较多，你还可以通过检索框来查找仓库。注意需要输入正确的仓库名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27201%27%20height=%27251%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAxIiBoZWlnaHQ9IjI1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

成功绑定仓库后，你就可以看到 Push 和 Pull 操作的按钮、版本检查的提醒。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27563%27%20height=%27248%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYzIiBoZWlnaHQ9IjI0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

Push 操作​

Push 操作可将 AI 编程项目的代码推送到远程仓库。​

  * 首次绑定仓库后，页面会提示你“有未推送的更改”，说明 GitHub 仓库版本落后于扣子编程项目，你可以选择 Push 操作，将扣子编程项目代码推送到 GitHub 仓库。​

  * AI 编程项目的每次改动，也都可以通过 Push 操作同步到 GitHub。​

操作步骤如下：​

1.

在 AI 编程项目的版本控制页面中，单击 Push。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27589%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg5IiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

确认要同步的 Commit 列表，并单击 Push。​

  * 如果暂时不想同步这些 Commit，可以单击忽略，表示取消这次操作。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27426%27%20height=%27385%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI2IiBoZWlnaHQ9IjM4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

Push 完成后，页面会提示已同步，表示推送成功。​

  * 项目的版本列表中也会添加一个新版本，并注明这个版本来自 agent，即扣子编程 AI。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27531%27%20height=%27251%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMxIiBoZWlnaHQ9IjI1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

Pull 操作​

Pull 操作可以从远程拉取更新，例如协作者提交到 GitHub 上的更新。当远程有新的提交时，扣子编程会提示你“远程有更新”， 你可以选择 Pull 操作，把远程更新同步到你的 AI 编程项目中。​

操作步骤如下：​

1.

在 AI 编程项目的版本控制页面中，单击 Pull。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27626%27%20height=%27276%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI2IiBoZWlnaHQ9IjI3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

Pull 完成后，页面会提示已同步，表示拉取成功。​

  * 项目的版本列表中也会添加一个新版本，并注明这个版本来自 GitHub。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27630%27%20height=%27218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMwIiBoZWlnaHQ9IjIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

冲突处理​

Push 或 Pull 时，不同来源的代码可能会发生冲突，扣子编程会识别冲突的文件内容，并可视化展示冲突代码的两个版本，供你选择保留哪一个版本，解决之后再帮你合并冲突。​

例如拉取 GitHub 上的更新时，扣子编程提示冲突，你需要选择处理机制：​

  * 全部保留我的版本：放弃远程的所有修改，仅保留扣子编程项目的内容。​

  * 全部使用远程版本：用远程仓库的文件覆盖你扣子编程项目的所有冲突文件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27407%27%20height=%27331%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA3IiBoZWlnaHQ9IjMzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用 Git 命令​

如果你习惯使用终端来执行 Git 操作，也可以在 AI 编程环境的终端区域直接输出 Git 命令行。目前支持 Pull 和 Push 相关的常见 Git 命令，例如：​

  * 拉取远程变更：git push​

  * 推送变更到远程：git pull​

  * 查看文件修改状态：git status​

  * 查看提交历史：git log​

  * 提交变更：git commit -m"feat: 新增xxx"​

常见问题​

如何更换授权的 GitHub 账号？​

你可以取消授权，再登录其他 GitHub 账号来完成授权。取消授权后，此工作空间下所有已绑定的 GitHub 仓库会自动解绑，若有需要，你可以自行绑定其他仓库。​

1.

在集成管理 > Git 服务页面中，单击取消配置，并根据页面提示取消授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27483%27%20height=%27239%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgzIiBoZWlnaHQ9IjIzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

使用其他账号登录 [GitHub](<https://github.com/>)。​

  * 换绑之前必须登录你想授权的另一个 GitHub 账号，否则扣子编程会使用你当前登录账号直接完成授权。​

3.

在集成管理 > Git 服务页面中，单击配置，完成授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27659%27%20height=%27264%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU5IiBoZWlnaHQ9IjI2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

如何更换绑定的 GitHub 仓库？​

为 AI 编程项目解除仓库绑定，并重新绑定一个仓库即可。​

1.

在 AI 编程项目的版本控制页面，单击解绑图标。​

2.

单击解绑仓库。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27653%27%20height=%27340%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjUzIiBoZWlnaHQ9IjM0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

单击绑定仓库，根据页面提示重新绑定仓库即可。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27637%27%20height=%27341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM3IiBoZWlnaHQ9IjM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用 Git 服务时可以指定分支吗？​

暂不支持，目前固定使用 main 分支。​

编程项目可以绑定已有的 Git 仓库吗？​

可以但不推荐。如果你的 Git 仓库中已有代码文件，Pull 或 Push 时可能会和 AI 编程项目中的代码文件产生冲突，不便于项目管理协作。建议你绑定时根据页面提示创建一个新的仓库。​

上一篇

版本控制

下一篇

分享编程项目