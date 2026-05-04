---
source_url: https://docs.coze.cn/guides/improve_image_quality_plugin
title: '画质提升插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:48Z
---

# 画质提升插件 - 文档 - 扣子

画质提升插件

[画质提升插件](<https://www.coze.cn/store/plugin/7438834453352529946>)用于提升图片的画质，支持增强 4 倍清晰度。你可以使用该插件对模糊或低清的图片进行处理，使图片呈现出更加清晰、细腻的效果。​

使用限制​

扣子主账号内所有子账号共享画质提升插件的并发限制 ，其值为 4。​

计费说明​

画质提升插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

画质提升插件包含 image_quality_improve 工具。调用该工具时，你需要上传原始图片。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 画质提升后的图片链接。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用画质提升插件，提升图片画质。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27646%27%20height=%27595%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQ2IiBoZWlnaHQ9IjU5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果如下：​

原始图片​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2713221.153846153846%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMTMyMjEuMTUzODQ2MTUzODQ2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

画质提升后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%2713255.131964809383%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMTMyNTUuMTMxOTY0ODA5MzgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

*画质提升插件 ID：7438835880728526898​

上一篇

光影融合插件

下一篇

智能换脸插件