---
source_url: https://docs.coze.cn/tutorial/split_msg
title: '拆分输出消息 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:54Z
---

# 拆分输出消息 - 文档 - 扣子

拆分输出消息

以好书解析场景为例，演示如何将长文本消息拆分为多条消息，减少用户等待回复的时间。​

场景说明​

在内容生成和内容处理场景中，工作流最终输出的内容较长，即使开启了结束节点的流式输出，用户也需要等待一段时间才能获得完整的输出文本，在一定程度上会影响用户体验。​

扣子编程的低代码工作流提供了输出节点，可以在工作流执行过程中阶段性输出文本消息。我们可以使用文本处理节点将消息拆分为两部分，一部分通过输出节点输出，一部分通过结束节点输出，同时开启流式输出。此方案适用于文章生成、剧本写作、文档优化等最终输出大量文本的场景，减少用户等待时间，提升用户体验。​

效果演示​

以好书解析场景为例，智能体将一条长文本消息拆分为了两条消息输出：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27302%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/99c79661e5cc4723a2069ddfbd9aec51~tplv-goo7wpa0wc-quality:q75.image)​

​

低代码工作流设计​

大模型节点生成书籍的介绍，并指定输出为两个段落，通过文本处理节点将两个段落拆开，一段通过输出节点输出，一段通过结束节点输出。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272840%27%20height=%271159.526627218935%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg0MCIgaGVpZ2h0PSIxMTU5LjUyNjYyNzIxODkzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

核心节点配置​

工作流核心节点的配置详情如下：​

​

节点类型​| 配置说明​| 示例​  
---|---|---  
大模型节点​| 引用开始节点的变量，获取用户需要查询的书籍名称。​用户提示词中需要指定输出格式，例如指定输出为两个段落。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27668.3544303797469%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjY2OC4zNTQ0MzAzNzk3NDY5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
文本处理节点​| 使用字符串分隔模式，通过换行符将大模型节点的输出内容转为数组格式，每个段落是数组的一个元素。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27456.73758865248226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ1Ni43Mzc1ODg2NTI0ODIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
输出节点​| 引用文本处理节点的输出，注意这里只引用数组的第一个元素，也就是书籍简介的第一个段落。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27397.63313609467457%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM5Ny42MzMxMzYwOTQ2NzQ1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 引用文本处理节点的输出，这里只引用第二个段落即可。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27444.9704142011834%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ0NC45NzA0MTQyMDExODM0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

​

上一篇

通过循环生成长文本

下一篇

动态设置大模型工具入参