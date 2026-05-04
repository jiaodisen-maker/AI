---
source_url: https://docs.coze.cn/guides/delete_message
title: '删除消息节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:51Z
---

# 删除消息节点 - 文档 - 扣子

删除消息节点

低代码工作流中的删除消息节点用于删除指定会话中的某一条消息内容。​

节点说明​

增删改查是消息类节点的常见操作，你可以通过删除消息节点来删除指定会话中的某一条消息内容。从会话中删除存储的消息之后，模型可见的消息历史中也会同时删除此条消息记录。​

每次执行删除消息节点时只能删除一条消息，且需要指定消息的 ID，开发者可以通过​查询消息列表节点来查看指定会话中的消息列表，获得消息 ID。​

添加节点​

在工作流画布中，单击 \+ 添加节点，在消息区域选择删除消息节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27690%27%20height=%27365%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/669f818cbdfb49e99448bfb17952fcb5~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

删除消息节点的输入参数固定为：​

  * conversationName，必选，String 类型，表示待删除消息的会话名称。​

  * messageId：必选，String 类型，表示待删除的消息 ID。​

输出​

删除消息节点的输出参数用于展示节点的执行结果。参数固定为 isSuccess，Boolean 类型，表示删除消息节点是否执行成功。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27265%27%20height=%27232%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY1IiBoZWlnaHQ9IjIzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行节点​

对于资源库中的工作流或对话流，试运行删除消息节点时，需要关联智能体或应用，表示在指定智能体或应用的会话中删除消息。试运行工作流节点时，可以删除动态会话或静态会话中的消息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27513%27%20height=%27491%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEzIiBoZWlnaHQ9IjQ5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

修改消息节点

下一篇

查询消息列表节点