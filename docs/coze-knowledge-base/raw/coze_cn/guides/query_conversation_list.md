---
source_url: https://docs.coze.cn/guides/query_conversation_list
title: '查看会话列表节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:40Z
---

# 查看会话列表节点 - 文档 - 扣子

查看会话列表节点

低代码工作流中的查看会话列表节点用于查看当前用户的会话列表。​

节点说明​

增删改查是会话管理类节点的常见操作，创建会话之后可以通过查看会话列表节点查看当前终端用户的所有会话，包括静态会话和动态会话。通过此节点可查看会话的名称及 ID。​

会话类、消息类节点往往需要指定会话名称，你也可以通过查看会话节点快速筛选出要操作的会话名称。​

说明

会话类节点只能在应用中使用。低代码智能体暂不支持会话管理类节点，即创建会话、修改会话、删除会话、查询会话列表节点。​

​

添加节点​

在工作流画布中，单击 \+ 添加节点，在会话管理区域选择查看会话列表节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27701%27%20height=%27366%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8f6ada6a145d454b8a88448fddd3e040~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

查看会话列表节点无需指定任何输入参数，默认查看当前用户的所有会话，包括动态会话和静态会话。​

输出​

查看会话列表节点的输出参数固定为 conversationList，即会话列表，其中包含：​

  * conversationName：会话的名称。​

  * conversationId：会话的 ID。​

试运行节点​

对于资源库中的工作流或对话流，试运行查看会话列表节点时，需要关联应用，表示查看指定应用的会话。试运行工作流节点时，操作的是草稿态的数据，也就是应用中存储的临时会话。线上执行工作流时，操作的是线上数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27384%27%20height=%27327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg0IiBoZWlnaHQ9IjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行成功后，可以在节点卡片中单击查看数据，在应用的会话管理页面中可见会话列表和试运行的结果完全一致。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27662%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYyIiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

删除会话节点

下一篇

查询会话历史节点