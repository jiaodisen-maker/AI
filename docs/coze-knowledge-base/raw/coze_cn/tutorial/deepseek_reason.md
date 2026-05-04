---
source_url: https://docs.coze.cn/tutorial/deepseek_reason
title: '为智能体接入 DeepSeek  - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:29Z
---

# 为智能体接入 DeepSeek  - 文档 - 扣子

为智能体接入 DeepSeek 

扣子编程现已推出满血版 Deepseek 全家桶，支持免费体验 R1、V3 模型。除此之外，扣子编程支持 DeepSeek 思维链（Chain-of-Thought，CoT）和 Function Calling 能力，为你的低代码智能体添加私有知识和多种技能，拓展低代码智能体的能力边界，一键满足多种场景需求。​

特色能力​

扣子编程推出的 Deepseek 系列模型特色能力如下：​

  * 思维链：DeepSeek R1 模型在输出最终回答之前，模型会将复杂问题逐步分解为多个简单步骤，并按照这些步骤逐一推导出最终答案，这个拆解的步骤就是思维链。思维链适用于复杂数学问题、逻辑推理问题、科学实验设计、代码调试与优化等场景，呈现完整的认知路径，帮助用户循序渐进地理解思考逻辑。​

  * 扣子编程现已支持实时展示 Deepseek 模型思维链内容，你可以在扣子编程调试区、扣子商店等场景中查看效果，也可以通过 API 获取思维链字段（reasoning_content）的具体内容。​

  * Function Calling：DeepSeek R1 和 V3 的 functionCall 版本支持在 Single-Agent 模式下调用各类扣子编程工具，例如插件、工作流、知识库等。支持 Function Calling 的 Deepseek 模型可以通过扣子编程工具拓展能力、获取实时数据或执行复杂任务。​

你可以在扣子编程满血版 Deepseek 全家桶中选择任意一款 Deepseek 模型，体验 Deepseek 的思维链和 Function Calling 能力。​

说明

Chat SDK 1.0.0-beta.4 及后续版本支持使用 DeepSeek。关于 Chat SDK 的详细说明，请参考​Chat SDK 概述。​

​

此外，需要注意的是：​

  * 工作流模式和多 Agent 模式下，思维链和 Function Calling 可能不会生效。​

  * 工作流的大模型、意图识别等支持配置模型的节点中，思维链和 Function Calling 可能不会生效，请勿为模型添加技能。​

以上使用场景正在接入中，敬请期待。​

搭建基于 DeepSeek 的低代码智能体​

本案例以 Deepseek R1 工具调用模型为例，搭建一个基于 DeepSeek 的低代码智能体。和这个低代码智能体对话时，你可以体验 Deepseek 的深度思考过程。​

操作步骤​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

创建智能体。​

a.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

b.

在低代码模式区域，单击智能体开发。​

c.

根据页面提示设置智能体名称、功能介绍，并选择一个合适的图标。​

3.

开发智能体。​

  * 在智能体的编排页面，为智能体设添加知识、技能和数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27403%27%20height=%27289%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAzIiBoZWlnaHQ9IjI4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 扣子编程提供的 Deepseek R1 工具调用模型支持思维链，无需任何额外配置即可查看完整的模型深度思考过程。除此之外，该模型支持 Function Calling 能力，我们可以添加一个搜索插件，为其赋予联网搜索的技能。​

  * ​

配置​| 说明​| 示例​  
---|---|---  
模型​| 为智能体设置 Deepseek R1 工具调用模型。此模型同时支持思维链和 Function Call，可以通过插件、工作流等处理复杂问题，并在回复中展示深度思考过程。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27849%27%20height=%27284.50531914893617%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODQ5IiBoZWlnaHQ9IjI4NC41MDUzMTkxNDg5MzYxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
插件​| 添加一个搜索插件，为 DeepSeek R1 模型赋予联网搜索的技能。通过搜索插件，DeepSeek 模型可以联网搜索实时信息与数据，例如天气、股市、时事新闻、汇率等不在模型训练数据中的信息。​如需为模型添加文生图等技能，可以通过对应的插件或工作流实现。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271276%27%20height=%27414.02127659574467%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI3NiIgaGVpZ2h0PSI0MTQuMDIxMjc2NTk1NzQ0NjciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

  * 你还可以按需为智能体添加知识库、数据库、设置变量。​

4.

调试智能体。​

  * 在预览与调试区域，和你的 DeepSeek 模型对话。体验 DeepSeek 的思维链和 Function Calling 技能。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27468%27%20height=%27355%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY4IiBoZWlnaHQ9IjM1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

发布智能体。​

  * 在页面右上角单击发布，将智能体发布到扣子商店、飞书、微信等其他渠道，成功发布后可以在对应的社交渠道中体验 DeepSeek 模型。如果你需要将 DeepSeek 模型接入到你的自建应用中，也可以将其发布为 API，通过调用 ​发起对话 API 和这个具备思维链和联网搜索技能的 DeepSeek 模型实时对话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27538%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM4IiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

体验效果​

你可以在智能体的编排页面调试区域体验 DeepSeek 模型能力，也可以发布智能体后在对应的发布渠道体验。注意部分发布渠道可能暂不支持展示 DeepSeek 模型的思维链。​

确认模型：​

先询问模型名称，确认为 DeepSeek R1 模型。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27247%27%20height=%27187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ3IiBoZWlnaHQ9IjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

简单测试一下能力：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27238%27%20height=%27153%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM4IiBoZWlnaHQ9IjE1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

逻辑推理：​

输入一个逻辑谜题或推理问题，模型逐步分析条件，推导出正确答案。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27639%27%20height=%27563.2890995260664%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM5IiBoZWlnaHQ9IjU2My4yODkwOTk1MjYwNjY0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

代码优化：​

输入一段有问题的代码，模型逐步分析代码逻辑，找出错误并提供优化建议。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27319%27%20height=%27321%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE5IiBoZWlnaHQ9IjMyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

联网搜索：​

输入一个需要联网搜索才能处理的问题，查看模型调用搜索插件的过程。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27663%27%20height=%27493.3222748815166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYzIiBoZWlnaHQ9IjQ5My4zMjIyNzQ4ODE1MTY2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

工作流方式接入 DeepSeek​

你可以在搭建工作流时，添加一个大模型节点，并在该节点中选择 DeepSeek 模型。使用 DeepSeek-R1 模型后，大模型节点的输出参数中默认返回 DeepSeek 模型的回复内容（output）和思维链内容（reasoning_content）。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271744%27%20height=%27302.77777777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc0NCIgaGVpZ2h0PSIzMDIuNzc3Nzc3Nzc3Nzc3NzciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

节点​| 说明​| 截图​  
---|---|---  
开始节点​| 开始节点用于传入用户指定的关键词。设置方法如下：​定义一个输入变量 input，数据类型为 String。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27361%27%20height=%27181.80797101449275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYxIiBoZWlnaHQ9IjE4MS44MDc5NzEwMTQ0OTI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
大模型节点​| 大模型节点用于调用大型语言模型，根据输入参数和提示词生成回复。设置方法如下：​

  * 模型：选择 DeepSeek-R1。​

  * 输入：定义输入变量 input，其值引用开始节点的输入变量 input。​

选择 DeepSeek-R1 模型时，大模型节点的输出参数包括 output 和 reasoning_content。​

  * output：返回 DeepSeek 模型的回复内容。​

  * reasoning_content：返回 DeepSeek 模型的思维链内容。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27360%27%20height=%27464.3478260869565%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYwIiBoZWlnaHQ9IjQ2NC4zNDc4MjYwODY5NTY1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
输出节点​| 输出节点用于输出 DeepSeek 模型的思维链内容。设置方法如下：​

  * 输出变量：定义一个输出变量 reasoning_content，其值引用大模型节点的输出变量 reasoning_content。​

  * 输出内容：引用输出变量 reasoning_content，输出 DeepSeek 模型的思维链内容。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27357%27%20height=%27353.1195652173913%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU3IiBoZWlnaHQ9IjM1My4xMTk1NjUyMTczOTEzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
结束节点​| 结束节点用于输出 DeepSeek 模型的回复内容。设置方法如下：​

  * 输出变量：定义一个输出变量 output，其值引用大模型节点中的输出变量 output。​

  * 回答内容：引用输出变量 output，输出 DeepSeek 模型的回复内容。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27351%27%20height=%27392.96739130434787%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUxIiBoZWlnaHQ9IjM5Mi45NjczOTEzMDQzNDc4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

API 方式接入 DeepSeek​

说明

低代码智能体为对话流模式时，思维链内容源自于大模型节点的输出，​发起对话 API 不会返回思维链内容（reasoning_content）。​

​

将你的智能体发布为 API 服务之后，就可以通过 API 方式调用智能体，和 DeepSeek 模型对话了。扣子编程 OpenAPI 通过响应参数 reasoning_content 展示 DeepSeek 模型思维链。具体使用方式如下：​

1.

调用​发起对话 API，在 API 响应中获取思维链及模型回复。​

  * 我们可以选择流式响应模式，在 message 事件的 reasoning_content 参数中获取思维链内容。流式响应中，模型会生成并流式返回成思维链内容，解析模型思考问题时的中间推理过程，再返回具体的 content。​

  * 调用示例如下：​

  * 请求示例

响应示例

​

Shell

复制

curl --location 'https://api.coze.cn/v3/chat' \​

\--header 'Authorization: Bearer pat_vpjxq05nflaMYavcrRgklNKueSKEbQ1ddnUYjmDsBAubvmUBqSr4WGlZ0TGq****' \​

\--header 'Content-Type: application/json' \​

\--header 'Accept: */*' \​

\--header 'Host;' \​

\--header 'Connection: keep-alive' \​

\--data '{​

"bot_id": "747349265604416****",​

"user_id": "123456789",​

"stream": true,​

"auto_save_history":true,​

"additional_messages":[​

{​

"role":"user",​

"content":"What day is it today",​

"content_type":"text"​

}​

]​

}'​

​

​

2.

调用消息相关 API，查看包含思维链的完整消息内容。​

  * 如果智能体选用了 DeepSeek R1 等支持思维链的模型，和智能体对话后，你可以调用以下消息相关 API，查看包含思维链的完整模型回复。API 响应参数中 reasoning_content 为具体的思维链内容，content 是智能体回复。​

  * ​查看消息列表​

  * ​查看消息详情​

  * ​查看对话消息详情​

  * 以​查看消息列表为例，包含 reasoning_content 的响应示例如下：​

  * ​

JSON

复制

{​

"code": 0,​

"data": [​

{​

"bot_id": "747349265604416****",​

"chat_id": "747351144190404****",​

"content": "Today is Thursday, February 20, 2025.",​

"content_type": "text",​

"conversation_id": "747351144190402****",​

"created_at": 1740062481,​

"id": "747351144190420****",​

"meta_data": {},​

"reasoning_content": "Okay, the user is asking what day it is today. Let me check the current date. According to the timestamp provided, it's 2025/02/20 22:41:20 Thursday. Wait, the date is already given in the prompt. So today is February 20, 2025, which is a Thursday. I don't need any tools here because the information is already available. Just need to format the answer clearly. Let me make sure there's no mistake in the day name. February 20, 2025... I can double-check by maybe thinking about a calendar, but the timestamp clearly says Thursday. So the final answer should be straightforward.\n",​

"role": "assistant",​

"section_id": "747351144190402****",​

"type": "answer",​

"updated_at": 1740062488​

},​

{​

"bot_id": "",​

"chat_id": "7473511441904042023",​

"content": "What day is it today",​

"content_type": "text",​

"conversation_id": "747351144190402****",​

"created_at": 1740062480,​

"id": "747351142093689****",​

"meta_data": {},​

"reasoning_content": "",​

"role": "user",​

"section_id": "747351144190402****",​

"type": "question",​

"updated_at": 1740062480​

}​

],​

"first_id": "747351144190420****",​

"has_more": false,​

"last_id": "747351142093689****",​

"msg": ""​

}​

​

上一篇

技能安全指南

下一篇

联网搜索