---
source_url: https://docs.coze.cn/guides/change_background_plugin
title: '背景替换插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:39Z
---

# 背景替换插件 - 文档 - 扣子

背景替换插件

[背景替换插件](<https://www.coze.cn/store/plugin/7438917173386428450>)用于为图片替换背景图。你可以通过该插件为人物照更换自然风景背景，为产品图更换展示背景，为艺术照更换与之风格相符的背景。​

使用限制​

扣子主账号内所有子账号共享背景替换插件的并发限制 ，其值为 4。​

计费说明​

背景替换插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

背景替换插件包含 background_change 工具。调用该工具时，你需要上传主体图和背景图。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
背景图​| 设置背景图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​​  
主体图​| 设置主体图来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 背景替换后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用背景替换插件，为图片替换背景。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27830%27%20height=%27873.6253369272237%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODMwIiBoZWlnaHQ9Ijg3My42MjUzMzY5MjcyMjM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

效果如下：​

主体图​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.55263157894737%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My41NTI2MzE1Nzg5NDczNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

背景图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27188.03418803418802%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4OC4wMzQxODgwMzQxODgwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

替换背景后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27183.27759197324414%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4My4yNzc1OTE5NzMyNDQxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

* 背景替换插件 ID：7438917859713138723​

​

上一篇

ByteArtist 插件

下一篇

宠物风格化插件