---
source_url: https://docs.coze.cn/guides/rotate_image_plugin
title: '图片旋转插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:28Z
---

# 图片旋转插件 - 文档 - 扣子

图片旋转插件

[图片旋转插件](<https://www.coze.cn/store/plugin/7438921878921560102>)用于对图片进行旋转操作。它能根据你指定的旋转角度，对输入的原始图片进行顺时针方向的旋转处理，轻松调整图片方向。​

计费说明​

图片旋转插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

图片旋转插件包含 image_rotate 工具。调用该工具时，你需要上传原始图片并指定旋转角度。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原始图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
旋转角度​| 设置图片的旋转角度。​

  * 取值范围：[0~360]，即支持 360° 顺时针旋转。​

  * 默认值：0，表示不旋转。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 图片旋转后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用图片旋转插件，旋转图片。其中指定图片旋转角度为 90 度。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27750%27%20height=%27717.654986522911%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUwIiBoZWlnaHQ9IjcxNy42NTQ5ODY1MjI5MTEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

效果如下：​

原始图片​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.55263157894737%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My41NTI2MzE1Nzg5NDczNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

旋转后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27217.8988326848249%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIxNy44OTg4MzI2ODQ4MjQ5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

* 旋转插件 ID：7438922485959245834​

上一篇

图片缩放插件

下一篇

图像美颜插件