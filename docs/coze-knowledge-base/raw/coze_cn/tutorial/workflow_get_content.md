---
source_url: https://docs.coze.cn/tutorial/workflow_get_content
title: '联网搜索 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:35Z
---

# 联网搜索 - 文档 - 扣子

联网搜索

大模型的原理和训练模式决定了模型本身并不具备联网搜索能力，无法通过搜索引擎获取最新的知识和数据。你可以为大模型添加搜索插件，以便在低代码工作流中使用搜索引擎搜索知识，实现联网搜索。​

本文演示通过代码节点和插件节点构建一个用于处理搜索结果的低代码工作流。​

效果演示​

扣子编程的低代码智能体添加联网搜索工作流后，用户可以通过输入关键词，让低代码智能体调用工作流进行联网搜索，并获取搜索结果。除此之外，低代码智能体还会输出一条包含网页链接的消息。​

另外，搜索结果还可以展示为卡片效果，单击卡片即可跳转对应检索网页。​

消息效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27348%27%20height=%27407%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/dabc746b6fa54a3985ee375f00503efc~tplv-goo7wpa0wc-quality:q75.image)​

​

卡片效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27418%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1f07cba57169436aa28b46dd7627bc8c~tplv-goo7wpa0wc-quality:q75.image)​

​

​

低代码工作流设计​

本文构建的示例工作流节点概览如下图所示。在该工作流中：​

1.

使用头条搜索插件，搜索指定关键词。​

2.

大模型节点总结搜索结果。​

3.

文本处理节点提取搜索结果中的 URL 和标题，并通过输出节点展示出来。​

4.

结束节点展示大模型节点总结的搜索结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271893%27%20height=%27749.3125%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5MyIgaGVpZ2h0PSI3NDkuMzEyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

核心节点​

工作流各个核心节点的配置方式如下：​

​

节点​| 配置​| 示例​  
---|---|---  
开始节点​| 开始节点用于传入用户指定的搜索关键词。​这里我们定义一个输入变量 query，String 格式。​| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27777%27%20height=%27296.8314606741573%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzc3IiBoZWlnaHQ9IjI5Ni44MzE0NjA2NzQxNTczIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
插件节点​（头条搜索 search）​| 添加一个插件节点，插件工具选择头条搜索插件的 search 工具。通过插件节点运行头条搜索插件，获取搜索结果。​在插件节点中，设置 input_query 引用开始节点的 query 变量。​| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27724%27%20height=%27752.4719101123595%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzI0IiBoZWlnaHQ9Ijc1Mi40NzE5MTAxMTIzNTk1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
大模型节点​| 大模型节点读取插件节点的搜索结果，并归纳、分类、总结。节点设置如下：​

  * 输入：定义输入变量 doc_results，引用插件节点的输出变量 doc_results。​

  * 用户提示词：帮我总结一下联网搜索的结果{{doc_results}}。​

其他配置维持默认配置即可。​| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27740%27%20height=%27852.2471910112359%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQwIiBoZWlnaHQ9Ijg1Mi4yNDcxOTEwMTEyMzU5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
文本处理节点​| 除搜索结果的归纳总结之外，还可以另外输出一条消息，向用户展示搜索结果的相关网页链接。这一功能由文本处理节点和输出节点实现。​我们使用文本处理节点拼接一个网页链接的列表，每个链接为 Markdown 格式，url 和标题部分可以从插件节点搜索结果中的数组结构中提取。​

  * 选择应用：选择字符串拼接。​

  * 输入：默认变量 String1，变量值引用插件节点的输出结果 data.doc_results，它的格式为 Array<Object>。我们将从这个数组中提取 url 和 title 字段。​

  * 字符串拼接：设置为以下内容。​

​Markdown复制联网搜索结果如下：​1. [{{String1[0].title}}]({{String1[0].url}})​2. [{{String1[1].title}}]({{String1[1].url}})​3. [{{String1[2].title}}]({{String1[2].url}})​​| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27724%27%20height=%27488.08988764044943%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzI0IiBoZWlnaHQ9IjQ4OC4wODk4ODc2NDA0NDk0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
输出节点​| 输出节点用于在工作流运行过程中输出一段中间消息。我们希望运行这个联网搜索工作流时，除了结束节点输出的总结文本之外，另外输出一条消息展示搜索结果的网页 URL 列表。文本处理节点已经成功拼接了这个列表内容，现在我们需要使用输出节点将它作为一条消息展示出来。​消息节点的配置如下：​

  * 输出变量：定义变量 output，类型为 String，引用文本处理节点的输出变量 output。​

  * 输出内容：设置为 {{output}}。​

| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27741%27%20height=%27541.1797752808989%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQxIiBoZWlnaHQ9IjU0MS4xNzk3NzUyODA4OTg5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
结束​| 结束节点用于输出大模型节点总结的检索结果。设置方式如下：​

  * 模式：返回文本​

  * 输出变量：定义变量 output，引用大模型节点的输出变量 output。​

  * 回答内容：设置为 {{output}}。​

| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27353%27%20height=%27404.56179775280896%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUzIiBoZWlnaHQ9IjQwNC41NjE3OTc3NTI4MDg5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
  
​

卡片展示搜索结果​

如需实现​效果演示中展示的卡片效果，需要简单调整工作流的输出节点设计，并在智能体中设置卡片样式。​

工作流设计​

调整后，工作流整体编排如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271891%27%20height=%27420.2222222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5MSIgaGVpZ2h0PSI0MjAuMjIyMjIyMjIyMjIyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调整方式如下：​

​

节点​| 配置​| 示例​  
---|---|---  
删除文本处理节点​| 如果使用卡片展示搜索节点，无需使用文本处理节点拼接消息内容，所以我们需要将文本处理节点从工作流中删除，使大模型节点直接连接输出节点。​| /​  
修改输出节点变量​| 卡片结构需要引用输出节点中的数组格式变量，所以我们将输出变量 output 改为引用插件节点的输出结果 data.doc_results，它的格式为 Array<Object>。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27378%27%20height=%27369.50561797752806%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc4IiBoZWlnaHQ9IjM2OS41MDU2MTc5Nzc1MjgwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

简单调试之后，重新发布工作流。​

设置卡片样式​

在智能体中，为工作流的输出节点配置卡片样式。​

1.

在智能体编排页面的工作流区域找到工作流，单击卡片图标，并在输出区域单击绑定卡片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27518%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE4IiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选择卡片样式。​

  * 在官方卡片区域，找到最后一个卡片模板。我们的检索结果中没有返回图片信息，而此模板无需配置图片，符合需求。​

3.

为卡片绑定数据源。​

  * 在中间区域，设置卡片样式为竖向列表。竖向列表的卡片会展示多个列表项，每个列表项包含一个标题和一个内容。​

  * 设置最大长度，此示例中我们设置为 3，表示展示 3 个网页链接。​

  * 为卡片绑定数组。这里选择 output，它是我们在输出节点定义的变量，内容是插件节点返回的数组。​

  * 为卡片列表项绑定数据。这里我们分别选择 output 数组中的 title 和 summary。​

  * 启用卡片跳转。跳转链接设置为 output 数组中的 url。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27497%27%20height=%27318%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk3IiBoZWlnaHQ9IjMxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

设置完毕后单击确认。​

5.

调试智能体，查看卡片效果。​

  * 在智能体调试区域输入一个检索关键词，检查卡片的展示效果。可以看到智能体返回了一张卡片，其中包含多个网页链接。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27418%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUwIiBoZWlnaHQ9IjQxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

为智能体接入 DeepSeek 

下一篇

查找新闻