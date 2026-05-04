---
source_url: https://docs.coze.cn/tutorial/workflow_read_link
title: '解析文件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:38Z
---

# 解析文件 - 文档 - 扣子

解析文件

本文档演示如何搭建一个解析 PDF 文件的低代码工作流。​

场景描述​

大模型本身并不具备文件读取和解析的能力，无法直接处理文件字节流。对于支持工具调用（Function calling）的模型，扣子编程提供插件功能来帮助大模型调用外部工具 API，拓展大模型的能力边界。插件商店提供海量官方插件和第三方插件，例如链接读取插件可以将链接对应的文件内容解析为纯文本传递给大模型。​

本文介绍如何使用链接读取插件节点搭建一个用于解析 PDF 文件的低代码工作流。​

说明

可解析的文件类型取决于插件能力，你可以在[链接读取插件的详情页](<https://www.coze.cn/store/plugin/7329410795979161663>)中查看插件最新的支持文件类型列表。目前插件可解析包括 PDF、Word、Excel 等常见格式的文件，也可以解析在线网页地址。​

​

效果示例​

搭建一个解析 PDF 的工作流，并将其绑定智能体之后，在调试区域发送一个 PDF 文件，并发送你的问题，智能体会自动调用工作流，并根据解析后的文件内容回答你的问题。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27265%27%20height=%27315%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/eaa8e94108124959944e4756ef26090c~tplv-goo7wpa0wc-quality:q75.image)​

​

工作流设计​

本文构建的示例工作流节点概览如下图所示。在该工作流中：​

1.

开始节点接收用户指定的文件和对应的问题（query）。​

2.

插件节点调用[链接读取插件](<https://www.coze.cn/store/plugin/7329410795979161663>)[ LinkReaderPlugin](<https://www.coze.cn/store/plugin/7329410795979161663>)[ ](<https://www.coze.cn/store/plugin/7329410795979161663>)[工具](<https://www.coze.cn/store/plugin/7329410795979161663>)，将文件内容解析为纯文本。​

3.

大模型节点根据解析后的文本，回答用户的问题。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271817%27%20height=%27433.2199074074074%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgxNyIgaGVpZ2h0PSI0MzMuMjE5OTA3NDA3NDA3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

核心节点​

工作流各个核心节点的配置方式如下：​

​

节点名称​| 说明​| 示例​  
---|---|---  
开始节点​| 开始节点用于接收用户设置的变量，并将变量传递给后续节点。​在开始节点定义以下变量，并为变量设置描述：​

  * pdf：待解析的 PDF 文件，File<Default> 格式。​

  * query：用户的问题，String 格式。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27364%27%20height=%27239.55555555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY0IiBoZWlnaHQ9IjIzOS41NTU1NTU1NTU1NTU1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
插件节点​| 添加一个插件节点，插件工具选择链接读取插件的 LinkReaderPlugin 工具。通过插件节点运行链接读取插件，获取搜索结果。​

  * 定义输入变量 url，在参数值区域引用开始节点的 pdf 变量，表示解析 pdf 变量传入的文件。​

  * 注意，节点会标红提示你 pdf 的变量格式和 url 变量的格式要求不一致，此处可忽略，扣子编程会将用户在开始节点上传的文件自动转为 String 格式的链接，并传递给 LinkReaderPlugin，所以实际传入的变量格式是符合要求的。​

  * 文件解析的结果会作为输出变量 pdf_content，便于后续节点使用。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27806%27%20height=%27733.6666666666666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODA2IiBoZWlnaHQ9IjczMy42NjY2NjY2NjY2NjY2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
大模型节点​| 通过用户提示词将问题和文件解析结果输入给大模型，大模型会自动总结文件信息，并生成对应的回复。​节点设置如下：​

  * 输入：定义以下输入变量。​

  * pdf_content：文件解析结果，引用插件节点的输出变量 pdf_content。​

  * query：用户的问题，引用开始节点的变量 query。​

  * 用户提示词：{{pdf_content}} {{query}}。​

其他配置维持默认配置即可。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27357%27%20height=%27709.4230769230769%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU3IiBoZWlnaHQ9IjcwOS40MjMwNzY5MjMwNzY5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
结束节点​| 结束节点用于输出大模型节点针对文件解析结果生成的回复。设置方式如下：​

  * 模式：返回文本​

  * 输出变量：定义变量 output，引用大模型节点的输出变量 output。​

  * 回答内容：设置为 {{output}}。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27353%27%20height=%27404.29059829059827%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUzIiBoZWlnaHQ9IjQwNC4yOTA1OTgyOTA1OTgyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

​

上一篇

查找新闻

下一篇

生成随机数