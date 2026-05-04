---
source_url: https://docs.coze.cn/guides/resize_image_plugin
title: '图片缩放插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:24Z
---

# 图片缩放插件 - 文档 - 扣子

图片缩放插件

[图片缩放插件](<https://www.coze.cn/store/plugin/7438917029320491008>)用于按照指定的长边或短边尺寸来等比例缩放图片。当你需要调整图片尺寸以满足不同场景需求（网页端图片、移动应用端图片等）时，可以自定义调整插件参数，以实现图片尺寸定制化处理。​

注意事项​

缩小图片不会改变图片的清晰度，放大图片通常会使图像变模糊。​

计费说明​

图片缩放插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

图片缩放插件包含 resize 工具。调用该工具时，你需要上传原始图片并设定缩放的最大尺寸。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原始图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
最大尺寸​| 设置图片缩放后的最大尺寸，必填参数。单位为像素。​  
缩放模式​| 设置缩放模式，即按图片的长边或短边缩放。​

  * 1（默认值）：长边。​

  * 2：短边。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 图片缩放后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用图片缩放插件，缩放图片。其中，指定按照长边（默认模式）等比例缩小图片，并指定缩小后的图片长边为 100 像素。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27811%27%20height=%27779.3032345013478%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODExIiBoZWlnaHQ9Ijc3OS4zMDMyMzQ1MDEzNDc4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

效果如下：​

原始图片​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27304%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA0IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

缩放后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27100%27%20height=%2792%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjkyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

* 缩放插件 ID：7438918747382890511​

上一篇

图片叠图插件

下一篇

图片旋转插件