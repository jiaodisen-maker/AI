---
source_url: https://docs.coze.cn/guides/integrate_llm
title: '集成大模型能力 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:53Z
---

# 集成大模型能力 - 文档 - 扣子

集成大模型能力

扣子编程提供了各类主流的大语言模型，如豆包模型、DeepSeek 模型、Kimi 模型等。你无需任何配置，扣子 AI 会自动为你的 AI 编程项目接入 AI 能力，满足文本生成、语义理解、多轮对话等核心 AI 需求。​

费用说明​

以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：调用大语言模型。​

为项目接入大模型能力​

在扣子编程中，你只需输入开发 AI 编程项目的指令，扣子 AI 会自动为项目接入内置集成中的大语言模型。例如输入指令：​

​

Plain Text

复制

开发一个阅读笔记总结工作流，通过大模型可以将获取到的文章内容进行总结、提炼，并输出总结笔记​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27529%27%20height=%27316%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/13c779ff13cc4d81bdd545e1ec1a8119~tplv-goo7wpa0wc-quality:q75.image)​

​

配置大语言模型参数​

接入大模型能力后，你可以精细化设置大语言模型的参数，例如生成随机性、Top P 和最大回复长度等。各个模型支持调整的参数不同，具体以界面为准。​

例如在智能体的预览页面，单击模型名称，然后单击设置图标，可以设置模型参数，参数说明如下表所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27537%27%20height=%27283%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM3IiBoZWlnaHQ9IjI4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

配置项​| 说明​  
---|---  
生成随机性​​​| 即 temperature，用于控制生成结果的随机性。取值范围：0~2。​

  * 调高此参数值，会使模型的输出更具多样性和创新性。​

  * 降低此参数值，会使输出内容更加严格遵循指令要求。当该数值接近零时，模型将变得确定和重复。​

在基于事实的问答场景，你可以使用较低的回复随机性数值，以获得更真实和简洁的答案，例如售后客服场景；在创造性的任务（如小说创作）中，你可以适当调高回复随机性数值。​  
重复语句惩罚​| frequency penalty，用于控制模型输出重复语句的频率。​当该值为正时，会阻止模型频繁使用相同的词汇和短语，从而增加输出内容的多样性。​  
Top P​| 累计概率。​模型在生成输出时会从概率最高的词汇开始选择，直到这些词汇的总概率累计达到 Top P 值。这样可以限制模型只选择这些高概率的词汇，从而控制输出内容的多样性。​  
最大回复长度​| 大模型在生成提示和响应时，所输出的最大 Tokens 数量，不同模型的 Tokens 限制也不同。指定最大长度可以防止过长或不相关的响应并控制成本。​  
最大推理&回答长度​| 如果开启了深度思考，可以通过该参数限制模型“思维链推理过程+最终回复内容”的最大 Tokens 消耗，避免因过度推理造成资源浪费。​该参数优先级高于最大回复长度，当两者同时配置时，最大回复长度不生效。​  
深度思考开关​| 部分支持深度思考的模型，开发者可以选择开启或关闭深度思考，从而灵活控制模型在交互过程中的 Token 消耗。​

  * 开启：大模型在与用户对话时会先输出一段思维链内容，通过逐步拆解问题、梳理逻辑，提升最终输出答案的准确性。但该模式会因额外的推理步骤消耗更多 Tokens。​

  * 关闭：大模型将直接生成最终答案，不再经过额外的思维链推理过程，可有效降低 Tokens 消耗，提升响应速度。​

  * 自动：启用自动模式后，模型会根据对话内容的复杂度，自动判断是否启用深度思考：​

  * 简单问题（如事实查询、基础指令等）：自动关闭深度思考，快速响应。​

  * 复杂问题（如逻辑推理、创意生成等）：自动开启深度思考，保证答案质量。​

  
深度思考程度​| 精细化控制思维链的推理深度与步骤数量，仅在深度思考开关为开启或自动时生效。​

  * 关闭：关闭深度思考，直接生成最终答案，与关闭深度思考开关的效果一致。​

  * 低：进行基础逻辑拆解，Tokens 消耗较低，响应速度快。​

  * 中：中等复杂度推理，兼顾答案质量与执行效率。​

  * 高：深度逻辑链推理，适用于复杂任务，答案准确性更高，但 Tokens 消耗增加，响应速度略有延迟。​

  
输出格式​| 指定模型输出内容的格式，例如文本、json object、json schema。​  
  
​

开启缓存​

部分模型支持开启上下文缓存功能。通过缓存常用上下文信息，可减少每次请求时重复处理的加载开销，加快模型的响应速度，降低模型使用成本，计费详情请参考​大语言模型。​

模型默认不开启上下文缓存，你可以通过自然语言对话方式，让扣子 AI 开启模型的缓存功能。例如输入如下指令：​

​

Plain Text

复制

为模型开启缓存功能​

​

开启后，你可以在智能体的 agent.py 文件或工作流的 node.py 文件中确认缓存是否开启成功。如果添加了 caching 配置和use_responses_api=True参数，则表示开启了模型缓存功能。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27117%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9IjExNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看模型详情​

在[扣子编程](<https://code.coze.cn/home>)的集成管理页面，单击目标大语言模型，即可在模型详情页签下查看该模型的详细信息，包括价格、限制和能力等。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27492%27%20height=%27193%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkyIiBoZWlnaHQ9IjE5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27486%27%20height=%27248%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg2IiBoZWlnaHQ9IjI0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

查看模型用量​

你可以通过模型用量看板追踪模型的用量。该看板会展示模型在当前工作空间的各个 AI 编程项目中的具体用量，包括输入 tokens、输出 tokens 和消耗 tokens，并支持按照输入 tokens、输出 tokens、消耗 tokens 维度进行排序。​

1.

在[扣子编程](<https://code.coze.cn/home>)的集成管理页面，单击目标大语言模型。​

2.

在模型用量页签下，查看该模型的用量信息。​

  * 单击指定 AI 编程项目用量细则列的查看，可以查看当前模型在指定项目中的每日用量及变化趋势。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271684%27%20height=%27529.4846335697399%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY4NCIgaGVpZ2h0PSI1MjkuNDg0NjMzNTY5NzM5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271479%27%20height=%27786.7021276595744%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ3OSIgaGVpZ2h0PSI3ODYuNzAyMTI3NjU5NTc0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

批量切换模型​

当某个模型即将停运时，工作空间的所有者或管理员可以快速定位当前工作空间下所有使用该模型的 AI 编程项目，并批量为这些项目的线上版本切换模型。模型停运 7 天内，仍支持批量切换模型。​

说明

  * 批量切换模型仅作用于已部署的线上版本。切换后，线上版本将使用新模型，但开发预览界面仍使用旧模型。如需切换预览界面的模型，请参考​如何切换大语言模型？。​

  * 切换前后模型价格、输入输出类型与限额可能存在差异。​

  * 切换后新模型默认使用标准配置，若需自定义参数，可手动调整配置后重新部署即可。​

​

1.

在[扣子编程](<https://code.coze.cn/home>)的集成管理页面，单击目标大语言模型。​

2.

在模型用量页签下，单击切换模型。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27510%27%20height=%27130%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEwIiBoZWlnaHQ9IjEzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选中待切换模型的项目，单击确认切换模型，然后选择新模型，单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271449%27%20height=%27622.1694915254237%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ0OSIgaGVpZ2h0PSI2MjIuMTY5NDkxNTI1NDIzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27304%27%20height=%27402%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA0IiBoZWlnaHQ9IjQwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

4.

查看新旧模型的对比信息，确认新模型符合需求后，单击确定，完成模型切换。​

切换完成后，状态将更新为项目已完成模型切换。新模型的用量图表数据将在次日自动更新。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27529%27%20height=%27142%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI5IiBoZWlnaHQ9IjE0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

管理外部集成服务

下一篇

集成数据库能力