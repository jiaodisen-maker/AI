---
source_url: https://docs.coze.cn/guides/style_transfer_plugin
title: '风格滤镜插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:43Z
---

# 风格滤镜插件 - 文档 - 扣子

风格滤镜插件

[风格滤镜插件](<https://www.coze.cn/store/plugin/7438921896516763698>)用于为图片添加各种独特的滤镜效果，包括毛毡、粘土、积木、美漫、玉石、搞笑涂鸦、工笔画、水彩画和僵尸 3D 等风格。​

使用限制​

扣子主账号内所有子账号共享风格滤镜插件的并发限制 ，其值为 4。​

计费说明​

风格滤镜插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

风格滤镜插件包含 style_transfer 工具。调用该工具时，你需要上传原始图片并指定滤镜风格。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原始图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
风格​| 设置风格滤镜，必填参数。支持设置为毛毡、粘土、积木、美漫、玉石、搞笑涂鸦、工笔画、水彩画和僵尸3D等风格。默认值为毛毡。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 添加滤镜后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用风格滤镜插件，为图片添加滤镜。其中，指定滤镜风格为毛毡。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27837%27%20height=%27774.9582210242587%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODM3IiBoZWlnaHQ9Ijc3NC45NTgyMjEwMjQyNTg3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

效果如下：​

原始图片​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.55263157894737%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My41NTI2MzE1Nzg5NDczNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

添加滤镜后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.00653594771242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My4wMDY1MzU5NDc3MTI0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

* 风格滤镜插件 ID：7438923452805054473​

上一篇

宠物风格化插件

下一篇

光影融合插件