---
source_url: https://docs.coze.cn/guides/input_node
title: '输入节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:57Z
---

# 输入节点 - 文档 - 扣子

输入节点

低代码工作流中的输入节点用于在工作流运行期间收集用户输入。​

节点说明​

在比较复杂的工作流场景中，某些节点的执行往往需要额外的用户输入。如果上游节点中没有获取到这些信息，你可以添加一个输入节点来主动收集信息。工作流执行到输入节点时会暂时中断，直到此节点收集到必要的用户输入。​

说明

  * 仅扣子商店、OpenAPI 渠道支持使用输入节点。​

  * 如果需要通过输入节点上传文件，可以通过如下方式：​

  * 试运行工作流时，在弹出的卡片中通过上传文件按钮上传本地文件。​

  * 将文件上传到第三方存储工具，获取一个公开可访问的 URL 地址，将此 URL 传入输入节点。​

  * 通过​上传文件 API 获取文件 ID，将文件 ID 以序列化的形式传入输入节点，例如：{"imgs":"[{\"file_id\":\"756918943296***\"}]","img":"{\"file_id\":\"75692127211375***\"}"}。​

  * 单 Agent 对话流模式和多 Agents 模式，暂不支持通过工作流的输入节点上传文件。​

​

配置输入节点​

输入节点中，只需设置输入参数即可。​

​

配置​| 说明​  
---|---  
变量名​| 输入参数的名称。​  
变量类型​| 输入参数的数据类型，支持 String 等多种数据类型。​  
描述​| 参数的描述信息。​  
是否必选​| 参数是否必选。工作流在执行此节点时，收集到所有必选参数之后才会继续执行后续节点。​  
  
​

你也可以直接导入 JSON 格式的数据结构，示例如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272814%27%20height=%271110.6180555555557%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgxNCIgaGVpZ2h0PSIxMTEwLjYxODA1NTU1NTU1NTciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

示例​

通过输入节点获取城市名称，并调用模型节点查询该地区的热门景点。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272272%27%20height=%27328.32369942196533%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI3MiIgaGVpZ2h0PSIzMjguMzIzNjk5NDIxOTY1MzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

核心节点说明如下：​

​

节点类型​| 配置说明​| 示例​  
---|---|---  
输入节点​| 添加一个必选的输入参数，名为 city，即用户想去的城市。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27235.51401869158877%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIzNS41MTQwMTg2OTE1ODg3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
大模型节点​| 设置以下参数：​

  * 输入：添加一个输入参数 city，引用输入节点的参数 city。​

  * 系统提示词：智能体的人设，按需设置。​

  * 用户提示词：需要模型回答的问题，此处引用输入节点的参数 city。​

  * 输出：维持默认设置即可。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27671%27%20height=%271051.753488372093%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcxIiBoZWlnaHQ9IjEwNTEuNzUzNDg4MzcyMDkzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

执行工作流时，系统会直接执行输入节点，引导用户输入想去的城市，并根据用户提供的城市名称，由大模型生成景点导览。实际运行效果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27440%27%20height=%27358%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQwIiBoZWlnaHQ9IjM1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

异步任务节点

下一篇

输出节点