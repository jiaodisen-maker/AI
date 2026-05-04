---
source_url: https://docs.coze.cn/cozeloop/prompt_version
title: '管理提示词版本 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:05Z
---

# 管理提示词版本 - 文档 - 扣子

管理提示词版本

扣子罗盘会自动记录提示词的历史版本，你可以查看版本记录、调试指定的历史版本，或者还原提示词到指定版本。每个提示词版本可添加版本标识，你也可以根据版本标识实现版本控制。​

提交新版本​

参考以下步骤，提交 Prompt：​

1.

在 Prompt 开发页面，单击提交新版本。​

2.

确认版本差异。​

  * 对于已有历史版本的提示词，提交一个新版本时需要确认版本差异。页面会展示最新历史版本和当前草稿版本的差异，包括模板内容、变量设置、模板引擎等所有差异。确认完毕后单击继续。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27429%27%20height=%27258%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/069a62004d30441f835e543194e8de64~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

确认版本信息。​

  * 在弹出的对话框中，确认版本号，按需设置版本标识，并提供版本说明，然后单击提交。关于版本标识的详细说明可参考​使用版本标识。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27397%27%20height=%27228%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/51238ad9816240c68e151cd0a3896bf0~tplv-goo7wpa0wc-quality:q75.image)​

​

查看版本记录​

在 Prompt 开发页面，单击版本记录，查看不同版本的提交信息。​

  * 每个版本条目下都会显示其“源版本”，即它最初基于哪个版本创建。​

  * 在版本记录中选择指定的历史版本，还可以查看指定版本的详细内容。​

查看版本记录：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27944%27%20height=%27587%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTQ0IiBoZWlnaHQ9IjU4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

版本详细信息：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272928%27%20height=%271694%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyOCIgaGVpZ2h0PSIxNjk0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

对比版本差异​

进入 Prompt 的编辑页面，点击页面右上角的 Diff 编辑 按钮，将进入DIff编辑模式，你可以将当前草稿和任意一个历史版本进行对比，并在对比模式下实时编辑草稿。​

进入 Diff 编辑模式：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272396%27%20height=%271306.1527777777776%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM5NiIgaGVpZ2h0PSIxMzA2LjE1Mjc3Nzc3Nzc3NzYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

实时对比与编辑：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272460%27%20height=%271317.4407582938388%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ2MCIgaGVpZ2h0PSIxMzE3LjQ0MDc1ODI5MzgzODgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

还原或创建副本​

在历史版本记录中，选中一个历史版本，然后单击创建副本复制一个与目标历史记录版本配置相同的 Prompt 副本；或单击还原为此版本回退至目标历史版本的 Prompt 配置。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27586%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg2IiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用版本标识​

扣子罗盘支持用户给 Prompt 不同版本添加标识，用于标记版本特性，开发者可以在不同环境（生产/测试）中拉取特定 Prompt 版本，以满足运行时版本控制的目的。扣子罗盘预置 3 个系统标识（production、beta、test），你也可以手动添加自定义标识。​

说明

  * 已创建的自定义标识无法删除或修改名称，创建时请谨慎操作。​

  * 自定义版本标识在工作空间内有效，空间内的所有 Prompt 均可使用。​

  * 每个 Prompt 版本最多可设置 20 个标识，但每个标识只能用于一个版本，以确保可通过指定标识定位到 Prompt 版本。例如 0.0.1 版本已设置 beta 标识，如果提交 0.0.2 版本时仍旧选择了 beta 标识，页面会提示冲突，并以最后一次添加该标识为准。​

  * 设置版本标识后，使用 SDK 拉取指定指定标识的 Prompt，可参考​通过版本标识拉取 Prompt 版本。​

​

为 Prompt 添加版本标识​

你可以在提交 Prompt 新版本时设置版本标识。如果预置的系统标识不符合需求，可以根据页面提示创建自定义标识。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27505%27%20height=%27285%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA1IiBoZWlnaHQ9IjI4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

修改版本标识​

对于已提交的历史版本 Prompt，你也可以在版本记录中设置或者修改版本标识。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27511%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTExIiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

智能优化提示词

下一篇

管理扣子提示词