---
source_url: https://docs.coze.cn/guides/better_prompt_plugin
title: '提示词优化插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:13Z
---

# 提示词优化插件 - 文档 - 扣子

提示词优化插件

[提示词优化插件](<https://www.coze.cn/store/plugin/7439196919706075136>)用于智能优化图像提示词。当你需要生成特定主题、风格或内容的图像时，可先使用该插件优化提示词。该插件通过先进的算法和自然语言处理技术，能够对你所输入的提示词进行分析和处理，使其更加准确、生动，从而帮助你在生成图像时获得更符合预期的高质量图像。​

计费说明​

提示词优化插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

提示词优化插件包含 sd_better_prompt 工具。调用该工具时，你输入图像提示词。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
提示词​| 输入图像提示词。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data​| 优化后的图像提示词。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用提示词优化插件，优化提示词 生成一张圣诞图。优化后的提示词为 Best quality, ultra-detailed, masterpiece, 4K, hyper detailed, realistic photo, Christmas scene, festive lighting, beautiful color composition。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27750%27%20height=%27396.22641509433964%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUwIiBoZWlnaHQ9IjM5Ni4yMjY0MTUwOTQzMzk2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

* 提示词优化插件 ID：7439197952104710144​

上一篇

通过 MCP 方式调用付费插件

下一篇

添加文字插件