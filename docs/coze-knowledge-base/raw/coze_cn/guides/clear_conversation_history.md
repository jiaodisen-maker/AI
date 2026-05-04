---
source_url: https://docs.coze.cn/guides/clear_conversation_history
title: '清空会话历史节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:46Z
---

# 清空会话历史节点 - 文档 - 扣子

清空会话历史节点

低代码工作流中的清空会话历史节点用于清除指定会话中存储的上下文消息。​

节点说明​

会话中的历史消息也被称为上下文，对大模型的性能和文本生成效果有重要影响。较长的上下文可以为模型提供更多的信息参考，生成与上下文语义匹配的文本片段，使模型生成更为连贯、逻辑性更强的内容。​

多轮对话中启动新话题时，过时的上下文也会同样影响模型的生成效果，例如模型可能召回一些过时的知识或记忆。此时可以使用清空会话历史节点，清除会话中已存储的上下文，成功清除后，对话流中的大模型节点会读到的对话历史为空，之后的对话不会收到之前历史消息的影响。​

例如以下对话中，清空会话历史后模型的回复会更加准确：​

  * 用户：最近看了几个恐怖电影。​

  * 模型：真是非常刺激和紧张的观影体验！你看了哪些恐怖电影？​

  * 用户：你有什么别的好电影推荐吗？​

  * 模型：当然！恐怖电影《闪灵》你感兴趣吗？​

  * 【清空会话历史】​

  * 用户：你有什么别的好电影推荐吗？​

  * 模型：根据最新的搜索结果，这里有一些 2025 年备受期待和推荐的电影。​

说明

  * 试运行清空会话历史节点时，只能清除应用中测试数据的上下文，无法清除线上数据。​

  * 清空会话历史只会清除模型可见的上下文，不会真正删除会话中存储的历史消息。所以清空会话历史之后，仍旧可以通过​查询消息列表节点查看完整的消息内容。​

  * 发布豆包渠道不支持清空会话历史节点。​

​

配置清空会话历史节点​

输入​

清空会话历史节点的输入参数固定为 conversationName，必选，String 类型，表示待清空会话历史的会话名称。会话名称参数可以指定为一个固定值，或引用上游节点的输出参数。​

输出​

清空会话历史节点的输出参数用于展示清空会话历史节点的执行结果。参数固定为 isSuccess，Boolean 类型，表示此节点是否执行成功。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27219.1907514450867%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjIxOS4xOTA3NTE0NDUwODY3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

试运行清空会话历史节点​

对于资源库中的工作流或对话流，试运行清空会话历史节点时，需要关联智能体或应用，表示清除指定智能体或应用中的上下文。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27489%27%20height=%27412%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg5IiBoZWlnaHQ9IjQxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行成功后，可以进入此应用的会话管理页面，可以在指定会话的对话框中看到页面提示“清空上下文”。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27524%27%20height=%27350%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI0IiBoZWlnaHQ9IjM1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

查询会话历史节点

下一篇

创建消息节点