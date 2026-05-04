---
source_url: https://docs.coze.cn/guides/edit_message
title: '修改消息节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:51Z
---

# 修改消息节点 - 文档 - 扣子

修改消息节点

低代码工作流中的修改消息节点用于修改指定会话中的某一条消息内容。​

节点说明​

增删改查是消息类节点的常见操作，你可以通过修改消息节点来修改指定会话中的某一条消息内容。修改消息之后，会话中存储的消息内容及模型可见的消息历史都会同步更新。​

每次执行修改消息节点时只能修改一条消息，且需要指定消息的 ID，开发者可以通过​查询消息列表节点来查看指定会话中的消息列表，获得消息 ID。​

添加节点​

在工作流画布中，单击 \+ 添加节点，在消息区域选择修改消息节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27717%27%20height=%27387%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6aeb630c02d24a239146eba3b57dc03c~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

修改消息节点的输入参数固定为：​

  * conversationName，必选，String 类型，表示待修改消息的会话名称。​

  * messageId：必选，String 类型，表示待修改的消息 ID。​

  * newContent：必选，String 类型，表示新的消息的内容，暂不支持多模态消息。​

输出​

修改消息节点的输出参数用于展示节点的执行结果。参数固定为 isSuccess，Boolean 类型，表示修改消息节点是否执行成功。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27572%27%20height=%27362%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcyIiBoZWlnaHQ9IjM2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行节点​

对于资源库中的工作流或对话流，试运行修改消息节点时，需要关联智能体或应用，表示在智能体或应用的会话中修改消息。试运行工作流节点时，可以修改动态会话或静态会话中的消息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27483%27%20height=%27424%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgzIiBoZWlnaHQ9IjQyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

创建消息节点

下一篇

删除消息节点