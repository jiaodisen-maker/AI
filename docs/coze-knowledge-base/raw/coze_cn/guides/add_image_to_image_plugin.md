---
source_url: https://docs.coze.cn/guides/add_image_to_image_plugin
title: '图片叠图插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:23Z
---

# 图片叠图插件 - 文档 - 扣子

图片叠图插件

[图片叠图插件](<https://www.coze.cn/store/plugin/7438921536473612288>)用于将一张图片叠加到另一张图片上，实现多层图像的合成效果。通过定义上层图片的位置、边距、缩放比例、透明度等属性，你可以将上层图片（图标、水印、装饰元素等）精准地叠加到底层图片中，满足多样化的设计需求。​

使用限制​

扣子主账号内所有子账号共享叠图插件的并发限制 ，其值为 10。​

计费说明​

图片叠图插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

图片叠图插件包含 add_image_to_image 工具。调用该工具时，你需要上传底层图片和上层图片。如果需要定制化叠加效果，可通过配置缩放、水平边距、位置、垂直边距等参数实现。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
上层图​| 设置上层图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​​  
底图​| 设置底层图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
缩放​| 设置上层图片缩放的百分比。例如设置为 50，则上层图片将缩小 50%。​  
水平边距​| 设置上层图片离底部图片边缘的水平距离。只有当上层图片的初始位置为左上、左中、左下、右上、右中、右下时，该配置才生效。​

  * 取值范围：[0,4096]。​

  * 默认值：10。​

  * 单位：px。​

  
位置​| 设置上层图片叠放的空间位置。​

  * se（默认值）：右下。​

  * nw：左上。​

  * north：中上。​

  * ne：右上。​

  * west：左中。​

  * center：中部。​

  * east：右中。​

  * sw：左下。​

  * south：中下。​

  
透明度​| 设置上层图片的透明度。​

  * 取值范围：[0,100] ​

  * 默认值：100，表示不透明。​

  
垂直边距​| 设置上层图片离底部图片边缘的垂直距离。只有当上层图片的初始位置为左上、中上、右上、左下、中下、右下时，该配置才生效。​

  * 取值范围：[0,4096]。​

  * 默认值：10。​

  * 单位：px。​

  
垂直偏移​| 设置上层图片的中线垂直偏移量。只有当上层图片的初始位置为左中、中部、右中时，该配置才生效。​

  * 取值范围：[-1000,1000]，其中正值表示向上偏移，负值表示向下偏移。​

  * 默认值：0，不偏移。​

  * 单位：px。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 被添加图片后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用图片叠图插件，将上层图片叠加到底层图片上。其中，指定上层图片位于底层图片的右上角，同时将上层图片缩小至 20%，透明度调整为 50 %，​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27814%27%20height=%27926.9946091644205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODE0IiBoZWlnaHQ9IjkyNi45OTQ2MDkxNjQ0MjA1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

叠图效果如下：​

上层图片​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.96226415094338%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My45NjIyNjQxNTA5NDMzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

底层图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27187.93103448275863%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4Ny45MzEwMzQ0ODI3NTg2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

叠图效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27188.03418803418802%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4OC4wMzQxODgwMzQxODgwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

* 叠图插件 ID：7438922391696326696​

​

上一篇

图片裁剪插件

下一篇

图片缩放插件