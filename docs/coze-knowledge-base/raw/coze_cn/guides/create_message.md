---
source_url: https://docs.coze.cn/guides/create_message
title: '创建消息节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:46Z
---

# 创建消息节点 - 文档 - 扣子

创建消息节点

低代码工作流中的创建消息节点用于在指定会话中手动插入消息。​

节点说明​

会话用于存储用户和模型的问答消息。对话流绑定会话之后，用户的输入和模型的输出默认会保存在该会话中，你也可以通过创建消息节点，手动向指定会话中插入消息，包括动态会话和静态会话。插入的消息会作为会话历史传递给模型，以便模型在后续对话中生成与上下文语义匹配的文本片段。​

每次执行创建消息节点时只能插入一条消息，且需要指定消息的来源，即用户（user）或模型（assistant）。建议交叉插入消息，即顺序为用户输入 -> 模型回复 -> 用户输入 -> 模型回复，其中用户和模型的一问一答为一轮对话。​

添加节点​

在工作流画布中，单击 \+ 添加节点，在消息区域选择创建消息节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27668%27%20height=%27358%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2d929c31579240998c1d8f8449be151d~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

创建消息节点的输入参数固定为：​

  * conversationName，必选，String 类型，表示待插入消息的会话名称。会话名称参数可以指定为一个固定值、引用上游节点的输出参数或者引用变量。​

  * role：必选，String 类型，表示消息的角色名。角色限制为 user 或者 assistant。user 代表该条消息内容是用户发出的；assistant 代表该条消息内容是返回给用户的。​

  * content：必选，String 类型，表示消息的内容。创建消息节点暂不支持创建多模态消息，即不支持创建图片、视频、音频等多媒体消息，但是你可以传入图片、视频等类型文件的 URL。​

输出​

创建消息节点的输出参数用于展示节点的执行结果和插入的消息详情。参数固定为：​

​

参数​| 说明​  
---|---  
isSuccess​| 创建消息节点是否执行成功。true 表示执行成功。​  
message​| 新消息的详细信息，仅在 isSuccess 为 true 时返回。​  
message.messageId​| 新消息的消息 ID。​  
message.role​| 新消息的角色名，即用户（user）或模型（assistant）。​  
message.contentType​| 新消息的内容类型。目前仅支持 text，表示文本消息。​  
message.content​| 新消息的完整内容。​  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27234%27%20height=%27324%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM0IiBoZWlnaHQ9IjMyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行节点​

对于资源库中的工作流或对话流，试运行创建消息节点时，需要关联智能体或应用，表示在智能体或应用的会话中创建消息。试运行工作流节点时，可以在动态会话或静态会话中创建消息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27539%27%20height=%27404%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM5IiBoZWlnaHQ9IjQwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行成功后，可以进入此应用的会话管理页面，可以在指定会话中看到已插入的消息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27566%27%20height=%27237%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY2IiBoZWlnaHQ9IjIzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

清空会话历史节点

下一篇

修改消息节点