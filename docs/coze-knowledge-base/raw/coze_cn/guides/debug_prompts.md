---
source_url: https://docs.coze.cn/guides/debug_prompts
title: '调试提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:43:13Z
---

# 调试提示词 - 文档 - 扣子

调试提示词

在搭建低代码智能体时，开发者可通过一键对比功能实现不同场景下大模型回复效果的可视化对比，从而精准调优提示词及选定最合适的大模型。​

背景信息​

在搭建低代码智能体时，系统提示词是开发者为大语言模型设定的初始参数和行为准则，在整个会话中持续影响大模型的响应模式。特别在专业的开发场景中，往往需要反复调试提示词，以达到最优的大模型回复效果。当前，扣子编程提供提示词对比调试功能和模型对比调试功能，助力开发者一键对比不同场景下的大模型回复效果，高效调优提示词及选定最合适的大模型。​

  * 提示词对比调试：输入两版提示词，对比大模型回复结果的差异。​

  * 模型对比调试：基于同一提示词，对比不同大模型或同模型不同配置下的回复结果差异。​

使用限制​

  * 仅单 Agent （LLM 模式）支持提示词对比调试、模型对比调试功能。​

  * 在模型对比调试场景下，暂不支持配置模型参数中的携带上下文轮数参数。​

提示词对比调试​

提示词对比调试功能支持输入两版提示词，对比大模型回复效果的差异。​

在智能体编排页面的人设与回复逻辑区域，单击提示词对比调试，即可进入对比调试页面。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27420%27%20height=%27115%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0a2609a315b1414291a5f9aa5fdb2c91~tplv-goo7wpa0wc-quality:q75.image)​

​

开发者在默认提示词、对比提示词区域输入提示词或从提示词库中选择提示词后，再选择一个大模型进行对话。提示词对比调试区域将实时直观地展示大模型基于两版提示词的回复结果差异。基于回复结果，开发者可以进一步调整提示词或大模型，直至获得最优的提示词和大模型。​

说明

对比调试数据不会永久保存。对比调试完成后，请及时单击完成对比，将选中的提示词及大模型同步到智能体草稿中，否则可能因为开启新的对比调试模式而清空此前未完成的对比调试数据。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272518%27%20height=%271211.016333938294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUxOCIgaGVpZ2h0PSIxMjExLjAxNjMzMzkzODI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

模型对比调试​

模型对比调试功能支持基于同一提示词，对比不同模型或同模型不同配置下的回复结果差异。​

在智能体编排页面的模型选择框中，单击模型对比调试，即可进入对比调试页面。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271075%27%20height=%27231.66351606805293%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA3NSIgaGVpZ2h0PSIyMzEuNjYzNTE2MDY4MDUyOTMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

开发者在提示词区域输入提示词或从提示词库中选择提示词后，再选择两个大模型或不同配置的大模型进行对话。提示词对比调试区域将实时直观地展示不同大模型或同模型不同配置下对相同提示词的回复结果差异。基于回复结果，开发者可以进一步调整提示词或大模型，直至获得最优的提示词和大模型。​

说明

对比调试数据不会永久保存。对比调试完成后，请及时单击完成对比，将选中的提示词及大模型同步到智能体草稿中，否则可能因为开启新的对比调试模式而清空此前未完成的对比调试数据。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272522%27%20height=%271208.3629764065336%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUyMiIgaGVpZ2h0PSIxMjA4LjM2Mjk3NjQwNjUzMzYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

上一篇

编写提示词

下一篇

管理提示词资源