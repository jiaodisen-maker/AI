---
source_url: https://docs.coze.cn/guides/swap_face_plugin
title: '智能换脸插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:51Z
---

# 智能换脸插件 - 文档 - 扣子

智能换脸插件

[智能换脸插件](<https://www.coze.cn/store/plugin/7438916871795228722>)用于将图片中的人脸替换为其他参考图中的人脸，可帮忙你轻松实现人脸的替换和融合，创造出各种有趣和创意的图片效果。​

使用限制​

扣子主账号内所有子账号共享智能换脸插件的并发限制 ，其值为 4。​

计费说明​

智能换脸插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

智能换脸插件包含 swap_face 工具。调用该工具时，你需要上传换脸图和底图。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
换脸图​| 设置换脸图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
底图​| 设置底图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 智能换脸后的图片链接。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用智能换脸插件，将底图中的人脸替换为换脸图中的人脸。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27617%27%20height=%27643%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE3IiBoZWlnaHQ9IjY0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果如下：​

换脸图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.9572192513369%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My45NTcyMTkyNTEzMzY5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

底图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27141.2742382271468%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE0MS4yNzQyMzgyMjcxNDY4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

智能换脸后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27141.02564102564102%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE0MS4wMjU2NDEwMjU2NDEwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

* 智能换脸插件 ID：7438917954420621339​

上一篇

画质提升插件

下一篇

智能抠图插件