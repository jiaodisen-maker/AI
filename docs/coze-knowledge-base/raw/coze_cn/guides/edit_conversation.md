---
source_url: https://docs.coze.cn/guides/edit_conversation
title: '修改会话节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:35Z
---

# 修改会话节点 - 文档 - 扣子

修改会话节点

低代码工作流中的修改会话节点通常用于修改已创建的会话名称。​

节点说明​

会话用于存储用户和模型的对话消息。每个对话流都需要绑定一个会话作为开始节点的默认会话，执行对话流时产生的消息都会自动写入到这个会话中。通过​创建会话节点创建会话之后，可以通过修改会话节点来修改会话的名称，但不会修改会话 ID 和会话中的消息。​

说明

  * 会话类节点只能在应用中使用。低代码智能体暂不支持会话管理类节点，即创建会话、修改会话、删除会话、查询会话列表节点。​

  * 只支持修改通过​创建会话节点创建的会话。​

​

添加节点​

在工作流画布中，单击 \+ 添加节点，在会话管理区域选择修改会话节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27571%27%20height=%27304%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e2ad9f3630f54d4b9a5ea8311a5a8f61~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

修改会话节点的输入参数固定为 conversationName 和 newConversationName，均为必选、String 类型，表示待修改的会话和新会话的名称。同一个应用中会话名称必须唯一。会话名称参数可以指定为一个固定值、引用上游节点的输出参数或者引用变量。​

输出​

修改会话节点的输出参数用于展示修改会话节点的执行结果。参数固定为：​

  * isSuccess：Boolean 类型，表示修改会话节点是否执行成功。​

  * isExisted：Boolean 类型，表示应用中是否已存在此名称的会话。​

  * conversationId：会话的 ID，修改会话名称不会变更会话 ID。​

输出示例如下：​

  * 应用中没有同名的会话，修改会话成功，返回会话 ID：​

  * ​

Markdown

复制

isSuccess : true​

isExisted : false​

conversationId : 7444890359211262037​

​

  * 应用中已有同名的节点，所以未修改会话，此时返回原会话的 ID：​

  * ​

Markdown

复制

isSuccess : false​

isExisted : true​

conversationId : 7444890359211262004​

​

试运行节点​

对于资源库中的工作流或对话流，试运行修改会话节点时，需要关联应用，表示修改指定应用中的会话。试运行工作流节点时，操作的是草稿态的数据，也就是应用中存储的临时会话。线上执行工作流时，操作的是线上数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27371%27%20height=%27313%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzcxIiBoZWlnaHQ9IjMxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行成功后，可以在节点卡片中单击查看数据，在应用的会话管理页面中查看修改名称后的会话。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27670%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcwIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

创建会话节点

下一篇

删除会话节点