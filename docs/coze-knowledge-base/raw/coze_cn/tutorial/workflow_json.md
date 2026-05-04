---
source_url: https://docs.coze.cn/tutorial/workflow_json
title: 'JSON 序列化和反序列化 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:47Z
---

# JSON 序列化和反序列化 - 文档 - 扣子

JSON 序列化和反序列化

扣子编程的低代码工作流节点支持 Object、Array 等多种复杂类型的输出和输出格式，在数据传输和处理的过程中，往往需要转换数据类型以便下游节点处理。JSON 序列化和反序列化是常见的数据类型转换方式，例如将某个节点输出的 Object 对象保存在扣子编程的数据库中，需要先将 Object 对象转换为 JSON 字符串，再通过数据库节点保存到 String 类型的字段中。​

低代码工作流现已支持 JSON 序列化和反序列化节点，支持将 Object 对象等常见数据类型转换为 JSON 字符串，以及将 JSON 字符串还原为指定数据结构。相较于代码节点，JSON 序列化和反序列化节点无需编写代码，可视化程度高、操作更加便捷。关于节点的详细说明，可参考​JSON 序列化节点、​JSON 反序列化节点。​

本文档以发送 HTTP 请求为例，演示 JSON 序列化和反序列化的方式。​

低代码工作流设计​

设计一个调用扣子编程 OpenAPI ​创建消息的低代码工作流。​

1.

生成 OpenAPI 请求 Body：由大模型节点生成 Object 结构，即消息内容，再由 JSON 序列化节点将其序列化为 JSON 字符串。​

2.

发送 OpenAPI 请求：由 HTTP 请求节点发送请求，调用扣子编程 OpenAPI ​创建消息。​

3.

解析 OpenAPI 响应：由 JSON 反序列化节点解析 HTTP 请求节点的输出变量（body），将其转为 Object 结构，再解析出 code、msg 等响应参数。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272842%27%20height=%271256.5324074074074%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cee6caa3755e4801b4e58dcdd8961526~tplv-goo7wpa0wc-quality:q75.image)​

​

核心节点​

各个节点的配置详情如下：​

​

节点名称​| 说明​| 配置示例​  
---|---|---  
开始节点​| 在本教程中，开始节点用于传入调用 OpenAPI 的必选参数。我们设置一个输入参数 input，用于传入消息内容，例如“早上好”。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271388%27%20height=%27396.57142857142856%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM4OCIgaGVpZ2h0PSIzOTYuNTcxNDI4NTcxNDI4NTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
大模型节点​| 为开始节点传入的消息内容生成一个完整的消息结构，便于后续序列化为 JSON 字符串作为 OpenAPI 的请求体。​

  * 用户提示词：提示模型生成 role、content 和 content_type 三个字段，并描述三个字段的含义。其中 content 部分引用开始节点传入的 input，作为消息内容。​

  * 输出：输出变量设置为 output，Object 类型，其中包含 role、content 和 content_type 三个字段。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271378%27%20height=%271365.6964285714287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM3OCIgaGVpZ2h0PSIxMzY1LjY5NjQyODU3MTQyODciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
JSON 序列化节点​| 将大模型节点生成的 Object 类型数据转为 JSON 字符串，后续可直接作为 OpenAPI 的请求体。​

  * 输入：引用大模型节点输出的 ouput。​

  * 输出：固定为 JSON 字符串。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271312%27%20height=%27726.2857142857143%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMxMiIgaGVpZ2h0PSI3MjYuMjg1NzE0Mjg1NzE0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
HTTP 请求​| 发送一个扣子编程 OpenAPI 请求，对应的 API 为​创建消息。​

  * API：配置 OpenAPI 的请求方法、请求地址。​

  * 请求参数：引用 JSON 序列化节点输出参数。​

  * 请求头：配置 OpenAPI 的请求头。​

  * 请求体：配置为 JSON 格式，输入 { 并直接引用 JSON 序列化节点输出参数 ouput。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271358%27%20height=%271297.375%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM1OCIgaGVpZ2h0PSIxMjk3LjM3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
JSON 反序列化节点​| HTTP 请求节点的输出参数 body 中封装了 OpenAPI 响应的 Body 部分，其中包含 code、msg 等字段，通过 JSON 反序列化节点可以将其成功解析为输出变量，以便关注其中的重点字段内容。​

  * 输入：引用 HTTP 请求节点的输出参数 body，表示解析该字段。​

  * 输出：配置需要从 JSON 中解析的字段。可以复制一个 JSON 格式的 OpenAPI 响应 Body 示例，通过输出区域右上角 JSON 导入功能，直接生成节点的输出结构。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271338%27%20height=%271182.6964285714284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMzOCIgaGVpZ2h0PSIxMTgyLjY5NjQyODU3MTQyODQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
结束节点​| 输出需要返回的变量或文本。这里我们选择返回变量 code、msg。​调用工作流之后可以根据 code 判断接口的响应状态，如果 API 调用失败，可通过 code 和 msg 判断失败原因。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271344%27%20height=%27660%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM0NCIgaGVpZ2h0PSI2NjAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

​

上一篇

识别用户意图

下一篇

自媒体图文创作