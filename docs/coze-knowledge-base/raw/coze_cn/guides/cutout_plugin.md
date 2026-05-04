---
source_url: https://docs.coze.cn/guides/cutout_plugin
title: '智能抠图插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:54Z
---

# 智能抠图插件 - 文档 - 扣子

智能抠图插件

[智能抠图插件](<https://www.coze.cn/store/plugin/7438917083918024738>)支持自动识别图片中的主体部分并去除背景，实现智能抠图，输出透明背景图或蒙版矢量图。同时，你也可以输入提示词，自定义抠图的对象，满足更精准的抠图需求。​

使用限制​

扣子主账号内所有子账号共享智能抠图插件的并发限制 ，其值为 4。​

计费说明​

智能抠图插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

智能抠图插件包含 cutout 工具。调用该工具时，你需要上传原始图片。如果需要精细化抠图，可配置提示词，自定义抠图的对象。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
上传图​| 设置原图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
产物尺寸​| 设置输出图的尺寸。​

  * 抠图结果尺寸：使用抠图结果的尺寸，去除透明部分。​

  * 原图尺寸：使用原图尺寸。​

  
输出图模式​| 设置输出图的模式。​

  * 透明背景图：输出图像的背景为透明。​

  * 蒙版矢量图：输出图像为矢量格式的蒙版。​

  
提示词​| 用于定义抠图内容的提示词。​如果不填，插件会自动识别图片中的主体部分。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 智能抠图后的图片 URL。URL 有效期为 30 天，请及时转存。​在输入参数中，设置输出图模式为透明背景图时，data 参数才生效。​  
mask​| 抠图区域的蒙板矢量图 URL。URL 有效期为 30 天，请及时转存。​在输入参数中，设置输出图模式为蒙版矢量图时，mask 参数才生效。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用智能抠图插件，完成抠图。其中，指定输出图模式为透明背景图。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27577%27%20height=%27574%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc3IiBoZWlnaHQ9IjU3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果如下：​

原始图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2720075.18796992481%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMjAwNzUuMTg3OTY5OTI0ODEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

抠图后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2728507.462686567163%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMjg1MDcuNDYyNjg2NTY3MTYzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

​

* 智能抠图插件 ID：7438919188246413347​

上一篇

智能换脸插件

下一篇

智能扩图插件