---
source_url: https://docs.coze.cn/guides/preview_debug
title: '预览与调试 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:06Z
---

# 预览与调试 - 文档 - 扣子

预览与调试

在搭建低代码智能体后，你可以在预览与调试界面与低代码智能体进行对话，并根据低代码智能体执行过程及响应信息对智能体配置进行优化与调整。在实际使用低代码智能体时，如果智能体响应不符合预期、速度过慢甚至不响应时，也可以通过调试台查看智能体的执行细节，排查问题。​

调试台介绍​

扣子编程的调试台功能提供全链路调试，你可以在调试台查看每一条用户请求从输入到响应的全流程，包括模型调用、配置的工作流或知识库等详细信息，方便你精准并快速定位问题，调整智能体配置。​

调试台适用于以下场景的问题分析：​

  * 开发调试：搭建智能体时，发现智能体输出不符合预期，例如回答与问题不符，需要修改智能体流程。​

  * 线上排障：收到智能体用户反馈，例如智能体不响应、返回错误信息，需要诊断定位问题。​

打开调试台​

你可以通过智能体的编排页面进入调试台，操作步骤如下：​

1.

在智能体编排页面右侧的预览与调试区域，发送一条消息内容开始与智能体对话。​

2.

在收到智能体响应后，点击消息卡片下方的调试按钮，或点击右上角的调试选项进入调试台页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272816%27%20height=%271642%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/32b7555710264e978a16cee7a92e7dc6~tplv-goo7wpa0wc-quality:q75.image)​

​

  * 进入调试台页面后，默认展示当前消息的响应过程，你可以筛选或选择查看之前某次对话的响应过程。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27269%27%20height=%27374%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY5IiBoZWlnaHQ9IjM3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调试信息说明​

调试台中展示每轮对话运行的全链路，包括会话的 Logid 等基础信息、调用流程、每个节点的状态和耗时等节点详情、节点的输入和输出等信息。​

基础信息​

页面默认展示当前会话的信息，你也可以通过会话时间和会话状态筛选会话，例如查看上周日所有运行异常的会话。会话详情区域用于了解会话的概览数据，例如会话整体耗时、消耗的 token 数量是否超出预期等等。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27364%27%20height=%27226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY0IiBoZWlnaHQ9IjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

参数​| 说明​  
---|---  
耗时​| 响应返回的整体耗时，即从用户发起会话到智能体运行结束的时长，单位为毫秒。​  
token 数量​| 该会话消耗的 token 总数量，包括用户输入、运行链路、模型输出、智能体推荐词等配置消耗的 token 数量。​  
任务状态​| 响应返回的状态，成功或失败。​  
Logid​| 当前响应的Log ID。如果无法自行排查问题，可以将 Logid 提供给扣子平台，协助处理。​  
首次响应耗时​​| 第一个字符出现的时长，单位毫秒。​  
  
​

调用树​

在排查和定位问题时，往往需要查看请求的完整调用链路，扣子编程通过可视化的方式展示了整个请求响应的完整链路和各节点的执行情况包括输入、输出、耗时等，帮助你快速定位问题和故障​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27430%27%20height=%27451%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDMwIiBoZWlnaHQ9IjQ1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 查看请求响应链路​

  * 首先，你可以通过树形图查看本次请求的完整响应流程。以上图中的天气查询请求为例，本次请求共涉及了4个节点。​

  * 查看请求节点的详细信息​

  * 你可以点击任一节点查看该节点的详细信息包括耗时和 token 消耗等。​

  * 查看请求节点的输入和输出​

  * 当点击任一节点后，输入和输入区域会展示所选节点的输入数据和输出数据。下图是插件节点的输入和输出示例。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27534%27%20height=%27261%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM0IiBoZWlnaHQ9IjI2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

火焰图​

调试台的火焰图可以帮助你清晰地了解各节点的耗时，有针对性的进行性能调优。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27509%27%20height=%27193%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA5IiBoZWlnaHQ9IjE5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见调试场景​

​

场景​| 调试方法​  
---|---  
工作流​| 当智能体使用了工作流时，你可以通过调试台查看每次请求响应的工作流节点的输入和输出，以及调用出错的节点，方便你快速定位工作流中有问题的节点。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27514%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjUxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
插件​| 与工作流类型，你也可以通过调试台查看每次请求响应中调用的插件的运行情况，以及运行出错的插件节点。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27311%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzExIiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
知识库​| 知识库作为智能体配置中重要的信息存储和知识来源，知识库的召回速度和准确性会直接影响回复的准确性。​在调试台中你可以查看知识库节点的运行情况。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27333%27%20height=%27436%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzIiBoZWlnaHQ9IjQzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​此外，你可以在请求响应运行完毕后，在调试与预览页面中，点击运行完毕选项，然后展开知识库节点，查看召回的内容片段是否正确。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27375%27%20height=%27416%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc1IiBoZWlnaHQ9IjQxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

常见问题​

调试与预览窗口中的运行结果与调试台的有何区别？​

  * 调试与预览窗口中的运行结果会实时展示请求的响应过程，当运行完毕后会展示最后一个节点的执行信息。​

  * 调试台中会展示指定请求的完整响应节点和每个节点的执行信息。​

为什么选择语音通话模式后，调试页面没有电话图标且无法使用语音通话功能？​

如果调试页面没有显示电话图标且无法使用语音通话功能，请检查智能体编排页面的以下配置：​

  * 确认已配置音色。​

  * 确认用户输入方式是否设置为语音通话。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27141.04046242774567%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE0MS4wNDA0NjI0Mjc3NDU2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

音视频通话

下一篇

低代码工作流介绍