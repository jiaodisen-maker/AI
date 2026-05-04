---
source_url: https://docs.coze.cn/cozeloop/configure-model
title: '配置模型 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:10Z
---

# 配置模型 - 文档 - 扣子

配置模型

扣子罗盘提供各个品牌版本的模型，你可以在调试提示词查看不同模型的生成效果。本文档介绍如何选择模型并设置模型参数。​

选择模型​

你可以在提示词详情页面的模型配置区域为提示词选择一个合适的大模型，例如对于长文生成或优化相关的智能体选择一个支持长文本的大模型、对于具有复杂业务逻辑的智能体选择一个支持 Function call 的大模型。如果调试提示词时，发现模型效果不及预期，你也可以切换成其他模型，测评同一个提示词在各个模型上的效果，选择最合适的模型。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27481%27%20height=%27263%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f42ff92dfbdd45698d1bb9d486403509~tplv-goo7wpa0wc-quality:q75.image)​

​

设置模型参数​

选择模型之后，你可以直接使用扣子罗盘预设的模型参数来调试提示词，也可以根据调试场景的需求，自行设置模型参数。目前支持设置的模型参数如下：​

​

参数​| ​| 说明​  
---|---|---  
最大回复长度​| ​| 设置模型单次生成内容的最大长度，单位为 Token。通常 100 Tokens 约等于 150 个中文汉字。该值会影响生成内容的篇幅。​  
生成随机性​| ​| 控制生成结果的随机程度，也称为 Temperature。值越高，回复的随机性和创造性越强；值越低，回复的确定性和逻辑性越强。建议不要与 “Top p” 同时调整。​  
Top P​| ​| 控制生成结果的多样性，也称为核采样（Nucleus Sampling）。模型会从累积概率超过该值的词汇中进行采样。建议不要与 “生成随机性” 同时调整。​  
重复语句惩罚​| ​| 设置对生成内容中重复词语的惩罚力度。值越高，越能有效降低模型生成重复语句的概率。当该值为正时，会阻止模型频繁使用相同的词汇和短语，从而增加输出内容的多样性。​  
深度思考​| 深度思考开关​| 

  * 开启深度思考：开启后，智能体在与用户对话时会先输出一段思维链内容，通过逐步拆解问题、梳理逻辑，提升最终输出答案的准确性。但该模式会因额外的推理步骤消耗更多 Token。 ​

  * 关闭深度思考：关闭后，智能体将直接生成最终答案，不再经过额外的思维链推理过程，可有效降低 Token 消耗，提升响应速度。 ​

  * 自动：当前仅豆包·1.6·自动深度思考·多模态模型支持该参数。启用自动模式后，模型会根据对话内容的复杂度，自动判断是否启用深度思考： ​

  * 简单问题（如事实查询、基础指令等）：自动关闭深度思考，快速响应。 ​

  * 复杂问题（如逻辑推理、创意生成等）：自动开启深度思考，保证答案质量。​

说明目前仅豆包·1.6·自动深度思考等部分模型支持深度思考开关，你可以根据模型列表中的“深度思考”标签来判断模型是否具备深度思考能力。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27164%27%20height=%27115%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY0IiBoZWlnaHQ9IjExNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
​| 深度思考长度​| 对于部分模型，开启深度思考后，还可以通过设置深度思考长度来控制思考内容的长度上限，深度思考长度的单位为 Token。​  
  
​

配置示例如下：​

模型配置：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27338%27%20height=%27480%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM4IiBoZWlnaHQ9IjQ4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

开启深度思考的效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27466%27%20height=%27748%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY2IiBoZWlnaHQ9Ijc0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

关闭深度思考的效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27465%27%20height=%27749%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY1IiBoZWlnaHQ9Ijc0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

上一篇

管理扣子提示词

下一篇

什么是评测