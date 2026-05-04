---
source_url: https://docs.coze.cn/guides/light_plugin
title: '光影融合插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:45Z
---

# 光影融合插件 - 文档 - 扣子

光影融合插件

[光影融合插件](<https://www.coze.cn/store/plugin/7438920651794284559>)用于使图像与光影图融合，为图像增添丰富的层次感和真实感。​

使用限制​

扣子主账号内所有子账号共享光影融合插件的并发限制 ，其值为 4。​

计费说明​

光影融合插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

光影融合插件包含 light 工具。调用该工具时，你需要上传光影图和主题图。如果需要定制图片样式，可配置亮度、对比度、光影方向等参数。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
光影图​| 设置光影图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
主体图​| 设置主体图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
亮度​| 设置图片的亮度。​

  * 取值范围：[0, 100]​

  * 默认值：10。​

  
对比度​| 设置图片的对比度。​

  * 取值范围：[0, 100]​

  * 默认值：10。​

  
补光强度​​| 设置逆光时的补光强度。值越小，暗面越亮。​

  * 取值范围：(0,-100)。​

  * 默认值：-50。​

  
光影方向​| 设置光影方向，包括顺光和逆光。默认值为顺光。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 进行光影融合后的图片链接。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用光影融合插件，为主题图添加光影。其中，设置补光强度为 \- 20。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27706%27%20height=%27791%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzA2IiBoZWlnaHQ9Ijc5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果如下：​

原始图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2720000%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMjAwMDAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

光影图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2723943.661971830985%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMjM5NDMuNjYxOTcxODMwOTg1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

光影融合后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2720000%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMjAwMDAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

​

​

*光影融合插件 ID：7438922908631580724​

上一篇

风格滤镜插件

下一篇

画质提升插件