---
source_url: https://docs.coze.cn/guides/model_management_FAQ
title: '模型常见问题 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:43:59Z
---

# 模型常见问题 - 文档 - 扣子

模型常见问题

豆包模型性能指标，为什么数据为空？​

豆包模型的性能指标，是根据空间所有者的模型实际使用情况统计的，如果模型在一个统计周期内未被使用，则性能指标数据为空。​

为什么不同用户查看同一豆包模型的性能指标存在差异？​

豆包模型的性能指标是根据空间所有成员的综合使用情况而统计。因此，即使是查看同一豆包模型，不同用户查看的性能指标数据也可能存在差异。​

是否支持接入自定义模型？​

扣子企业旗舰版支持接入自定义模型。除了扣子编程提供的官方模型及方舟接入点接入的火山方舟模型，企业旗舰版用户还可将自行部署的模型或第三方在线模型集成至平台，进一步拓展可用模型范围，具体请参见​接入自定义模型。​

是否支持对模型微调？​

暂不支持用户在扣子编程对模型进行微调。若你已通过其他方式完成模型微调，你可以通过接入自定义模型的方式，将微调模型接入扣子编程。​

企业旗舰版可以选择哪些模型？​

企业旗舰版支持调用如下类型的模型，详情请参考​模型服务：​

  * 扣子编程官方模型，例如豆包模型、DeepSeek 模型等。​

  * 火山引擎方舟平台提供的模型，例如豆包语音识别模型、语音合成模型、DeepSeek 模型等。​

  * 自定义模型，企业自部署的模型或第三方在线模型。​

是否支持批量关闭模型？​

暂不支持批量关闭模型。如需关闭模型，需由空间所有者或管理员在工作空间的模型管理页面进行逐个关闭。关闭后，此工作空间中无法添加该模型。如果智能体或工作流中已添加该模型，关闭后不影响其正常运行。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27531%27%20height=%27219%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMxIiBoZWlnaHQ9IjIxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

视觉理解模型支持读取图片 URL 吗？​

暂不支持，视觉理解模型往往需要直接处理图片文件。如果输入的是网络图片的 URL 地址，扣子编程传递给模型的图片 URL 往往是字符串格式（String），而模型无法直接访问网络连接读取图片。​

在这种场景下，扣子编程提供以下方案供你参考：​

  * 对于使用视觉理解模型的智能体：建议直接在对话中发送图片文件，以供视觉理解模型解析。​

  * 对于使用视觉理解模型的工作流节点：​

a.

在开始节点设置一个 String 类型的输入参数。​

b.

在大模型节点引用这个参数作为入参，但数据类型改为 Image。​

  * 这样设置后，大模型节点可以接收开始节点 String 格式的图片 URL，并将其转换为图片格式传递给视觉理解模型。​

  * 说明

    * 注意图片 URL 应是一个公开可访问的图片地址，且图片为常见的格式类型，例如 jpg、jpge、png 等。​

​

  * 详细设置如下：​

  * ​

节点​| 说明​| 示例​  
---|---|---  
开始节点​| 设置以下输入参数：​
    * query：String 类型，表示用户的问题。​
    * image：String 类型，用于传入图片的 URL。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27357%27%20height=%27228.64044943820224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU3IiBoZWlnaHQ9IjIyOC42NDA0NDk0MzgyMDIyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
大模型节点​| 设置以下输入参数：​
    * query：引用开始节点的 query 参数，无需调整数据格式。​
    * image： 引用开始节点的 image 参数，并将数据类型设置为 Image。​
设置以下用户提示词：{{image}}，{{query}}。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27360%27%20height=%27524.4943820224719%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYwIiBoZWlnaHQ9IjUyNC40OTQzODIwMjI0NzE5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

  * 编排方式如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271365%27%20height=%27628.7847222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM2NSIgaGVpZ2h0PSI2MjguNzg0NzIyMjIyMjIyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

查看模型性能与用量

下一篇

了解项目发布