---
source_url: https://docs.coze.cn/guides/ltm_node
title: '长期记忆节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:28Z
---

# 长期记忆节点 - 文档 - 扣子

长期记忆节点

低代码工作流中的长期记忆节点用于在工作流中召回长期记忆中储存的用户的个性化信息。​

节点说明​

在用户喜好推荐等个性化的场景中，通常需要基于用户画像、关键记忆点等个人数据进行推荐、筛选，让智能体效果更加贴合用户需求、提高用户体验。通常情况下，我们可以通过多轮会话的上下文来收集这些信息，但是基于上下文轮数限制，个性化信息无法长期记忆和保存，此时可以开启长期记忆功能，记录并调用用户的个性化信息。在工作流中，也可以通过长期记忆节点调用智能体的长期记忆，查询智能体已记录的用户喜好、用户画像等信息，让工作流的效果更加个性化。​

说明

  * 长期记忆节点需要召回智能体存储的长期记忆数据，所以试运行长期记忆节点或包含长期记忆节点的低代码工作流时，需要指定一个已开启长期记忆功能的智能体。​

  * 在低代码项目中，如果智能体绑定了包含长期记忆节点的工作流，则智能体需要开启长期记忆功能，否则工作流执行会报错 720712021 Bot 没有开启 LTM。同时建议关闭支持在Prompt中调用，否则在对话中容易同时触发长期记忆召回和工作流执行，影响对话效果。​

​

配置长期记忆节点​

长期记忆节点的配置说明如下：​

​

配置​| 说明​  
---|---  
输入参数​| 输入参数固定为 Query，表示需要从长期记忆中匹配的关键信息，例如查询用户的喜好、生日、男友名字等信息。以新闻搜索的工作流为例，Query 可以固定为“喜欢什么类型的新闻”，基于用户喜好检索并推荐新闻。​Query 可指定为引用或输入：​

  * 引用：引用上游节点的输出参数。​

  * 输入：指定为某个字符串。​

  
输出参数​| 输出参数固定为 outputList，格式为 Array<Object>，智能体会列举和 Query 相关的长期记忆。如果下游节点引用了这个参数，智能体会总结长期记忆中的内容，并将总结内容作为下游节点的输入。​  
  
​

长期记忆节点配置示例：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27356%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU2IiBoZWlnaHQ9IjI1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

下游节点引用长期记忆节点的输出参数：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27324%27%20height=%27422%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI0IiBoZWlnaHQ9IjQyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例​

例如对于查看热点新闻的工作流，可以召回用户的长期记忆，根据用户喜好来筛选出其可能感兴趣的内容。​

工作流主要设计如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271791%27%20height=%27183.69230769230768%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc5MSIgaGVpZ2h0PSIxODMuNjkyMzA3NjkyMzA3NjgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

各节点说明如下：​

​

节点​| 说明​| 配置示例​  
---|---|---  
开始节点​| 维持默认参数设置即可，无需任何必选的输入参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27232%27%20height=%27115%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMyIiBoZWlnaHQ9IjExNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
长期记忆节点​| 长期记忆节点的输入参数设置为输入，Query 固定为“喜欢什么类型的新闻”。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27223%27%20height=%27156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzIiBoZWlnaHQ9IjE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
插件节点​| 插件节点中使用头条新闻插件 getToutiaoNews，输入参数中引用长期记忆节点的输出参数，基于用户喜好检索并推荐新闻。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27178%27%20height=%27231%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc4IiBoZWlnaHQ9IjIzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 结束节点引用插件节点的输出参数，返回变量由智能体生成回答。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27461%27%20height=%27265.96153846153845%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYxIiBoZWlnaHQ9IjI2NS45NjE1Mzg0NjE1Mzg0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

​

智能体对话效果如下，你也可以将工作流绑定卡片，定制个性化的展示效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27571%27%20height=%27478%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcxIiBoZWlnaHQ9IjQ3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

知识库删除节点

下一篇

变量节点