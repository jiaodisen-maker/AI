---
source_url: https://docs.coze.cn/guides/change_image_plugin
title: '图像调整插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:33Z
---

# 图像调整插件 - 文档 - 扣子

图像调整插件

[图像调整插件](<https://www.coze.cn/store/plugin/7438921446090637312>)用于对图片的亮度、对比度和饱和度进行调整。通过该插件，你可以轻松改变图片的视觉效果，以满足不同的图片创作需求。​

使用限制​

扣子主账号内所有子账号共享图片调整插件的并发限制 ，其值为 4。​

计费说明​

图片调整插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

图片调整插件包含 change 工具，调用该工具时，你需要上传原始图片并设置亮度、对比度和饱和度等参数。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原始图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
亮度​| 设置图片的亮度。​

  * 取值范围：[0.1, 10]​

  * 默认值：1，表示不调整亮度。​

  
对比度​| 设置图片的对比度。​

  * 取值范围：[0.1, 10]​

  * 默认值：1，表示不调整对比度。​

  
饱和度​| 设置图片的饱和度。​

  * 取值范围：[0.1, 2]​

  * 默认值：1，表示不调整饱和度。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 返回进行亮度、对比度和饱和度调整后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 返回执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用图片调整插件，调整图片的亮度、对比度和饱和度。其中，设置亮度为 2，对比度为 2，饱和度为 0.5。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27809%27%20height=%27826.4447439353099%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODA5IiBoZWlnaHQ9IjgyNi40NDQ3NDM5MzUzMDk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

效果如下：​

原始图片​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.55263157894737%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My41NTI2MzE1Nzg5NDczNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

调整后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.44370860927154%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My40NDM3MDg2MDkyNzE1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

* 调整插件 ID：7438923315269484559​

上一篇

图像美颜插件

下一篇

ByteArtist 插件