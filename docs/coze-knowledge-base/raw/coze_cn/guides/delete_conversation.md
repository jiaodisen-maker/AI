---
source_url: https://docs.coze.cn/guides/delete_conversation
title: '删除会话节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:35Z
---

# 删除会话节点 - 文档 - 扣子

删除会话节点

低代码工作流中的删除会话节点用于删除通过创建会话节点创建的会话。​

节点说明​

增删改查是会话管理类节点的常见操作，每个用户的会话上限为 200 个。超过 200 个后，建议先通过删除会话节点删除历史会话，否则直接创建会话会报错。​

删除会话节点每次执行时，删除一个指定名称的会话，同时删除会话中的所有消息。会话及消息删除后不可恢复。​

说明

会话类节点只能在应用中使用。低代码智能体暂不支持会话管理类节点，即创建会话、修改会话、删除会话、查询会话列表节点。​

​

添加节点​

在工作流画布中，单击 \+ 添加节点，在会话管理区域选择删除会话节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27636%27%20height=%27335%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/724d6d56aaf94664bd1aa3f69768f5e4~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

删除会话节点的输入参数固定为 conversationName，必选，String 类型，表示待删除的会话名称。会话名称参数可以指定为一个固定值、引用上游节点的输出参数或者引用变量。​

输出​

删除会话节点的输出参数用于展示节点的执行结果。参数固定为 isSuccess，Boolean 类型，表示删除会话节点是否执行成功。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27324%27%20height=%27269%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI0IiBoZWlnaHQ9IjI2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行节点​

对于资源库中的工作流或对话流，试运行删除会话节点时，需要关联应用，表示在指定的应用中删除会话。试运行工作流节点时，操作的是草稿态的数据，也就是应用中存储的临时会话。线上执行工作流时，操作的是线上数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27356%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行成功后，可以在节点卡片中单击查看数据，在应用的会话管理页面中可见指定的临时会话已被成功删除。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27662%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYyIiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

修改会话节点

下一篇

查看会话列表节点