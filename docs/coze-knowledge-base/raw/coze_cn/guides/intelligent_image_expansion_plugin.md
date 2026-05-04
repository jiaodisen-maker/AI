---
source_url: https://docs.coze.cn/guides/intelligent_image_expansion_plugin
title: '智能扩图插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:56Z
---

# 智能扩图插件 - 文档 - 扣子

智能扩图插件

[智能扩图插件](<https://www.coze.cn/store/plugin/7438917721858916367>)用于扩展图片范围，生成更大尺寸且内容更丰富的图片。你可以通过设置对应的扩展比例和输入提示词，自定义扩图区域并添加新元素，轻松实现图片的智能扩展。​

使用限制​

扣子主账号内所有子账号共享智能扩图插件的并发限制 ，其值为 4。​

计费说明​

智能扩图插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

智能扩图插件包含 intelligentImageExpansion 工具。调用该工具时，你需要上传原始图片并定义各个方向的扩展比例。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原始图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
向下扩展​| 设置向下扩展的比例。取值范围：(0,1]​  
提示词​| 设置生成内容的提示词。​  
向左扩展​| 设置向左扩展比例。取值范围：(0,1]​  
向右扩展​| 设置向右扩展比例。取值范围：(0,1]​  
向上扩展​| 设置向上扩展比例。取值范围：(0,1]​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 智能扩图后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用智能扩图插件，指定向下扩展为 1，使图片下方尺寸扩展 1 倍。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27728%27%20height=%27701%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzI4IiBoZWlnaHQ9IjcwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果如下：​

原始图​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2718355.263157894737%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMTgzNTUuMjYzMTU3ODk0NzM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

扩展后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2736677.31629392971%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMzY2NzcuMzE2MjkzOTI5NzEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

  * ​

* 智能扩图插件 ID：7438919529398419491​

上一篇

智能抠图插件

下一篇

指令编辑插件