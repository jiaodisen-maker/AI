---
source_url: https://docs.coze.cn/guides/maintain_knowledge
title: '维护知识库 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:42:46Z
---

# 维护知识库 - 文档 - 扣子

维护知识库

本文主要介绍了扣子知识库的维护操作，包括编辑、停用、启用、删除扣子知识库，以及添加内容、删除知识库文件等操作。​

编辑知识库​

知识库的所有者可以编辑自己创建的知识库，包括编辑知识库的名称、描述信息和图标。​

参考以下操作，编辑知识库：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在知识库页签下，单击目标知识库。​

4.

单击知识库名称右侧的编辑图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27416%27%20height=%27170%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6b990dd14c734948aab5e64159ef9f2b~tplv-goo7wpa0wc-quality:q75.image)​

​

5.

在编辑知识库页面，根据实际需要修改名称、描述和图标，然后单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27419%27%20height=%27375%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b816fe5c8ed743958637ae4912cc20ba~tplv-goo7wpa0wc-quality:q75.image)​

​

停用知识库​

创建完知识库后，知识库默认为启用状态。如果你不希望使用某个知识库，你可以执行停用操作。如果低代码智能体或工作流已经使用了某个知识库，停用该知识库后，该知识库的内容也不会被召回。​

在资源库的知识库页签下，找到目标知识库，然后在操作列中，关闭启用开关。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27580%27%20height=%27109%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgwIiBoZWlnaHQ9IjEwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

关闭知识库后，知识库的状态变更为已停用。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27437%27%20height=%27178%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM3IiBoZWlnaHQ9IjE3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

启用知识库​

如果你希望低代码智能体或工作流使用某个知识库，你可以执行启用操作。启用后，知识库的内容才能被召回。​

在资源库的知识库页签下，找到目标知识库，然后在操作列中，打开启用开关。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27640%27%20height=%27119%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQwIiBoZWlnaHQ9IjExOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

开启知识库后，系统会取消已停用标签。​

为知识库添加内容​

创建完知识库后，你可以向知识库中添加新内容，以不断丰富知识库。​

1.

在资源库的知识库页签下，单击目标知识库。​

2.

单击页面右上角的添加内容，然后选择一种导入方式。​

3.

在添加内容页面，根据指引添加内容。​

添加内容同创建知识库时上传文件到知识库的操作一致，详情请参考​创建文本知识库。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27448%27%20height=%27140%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ4IiBoZWlnaHQ9IjE0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

删除知识库文件​

在知识库中，每个在线网页、各类格式文件或图片都是一个个独立的知识文件。你可以在扣子编程中查看每个知识库文件的内容分段，也可以通过 API 的方式管理和维护知识库，例如查看知识库文件列表、删除知识库文件等。​

注意

  * 删除某个知识库文件后，引用了对应知识库的低代码智能体或工作流将无法召回该内容。​

  * 删除操作不可撤回，请谨慎操作。​

​

参考以下操作，删除知识库文件：​

1.

在资源库的知识库页签下，选择目标知识库。​

2.

展开全部内容，然后选择要删除的知识库文件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27452%27%20height=%27242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUyIiBoZWlnaHQ9IjI0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

单击右上角的删除图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27453%27%20height=%27205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUzIiBoZWlnaHQ9IjIwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在弹出的对话框中，单击删除。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27140%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI2IiBoZWlnaHQ9IjE0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

删除知识库​

知识库的所有者支持删除自己创建的知识库。​

注意

删除某个知识库后，引用了该知识库的低代码智能体或工作流也将自动取消引用，且此操作不可撤回，请谨慎操作。​

​

1.

在资源库的知识库页签下，找到目标知识库，然后在操作列中，选择 ··· > 删除。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27630%27%20height=%27121%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMwIiBoZWlnaHQ9IjEyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在弹出的对话框中，单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27453%27%20height=%27150%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUzIiBoZWlnaHQ9IjE1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

使用知识库

下一篇

管理数据源权限