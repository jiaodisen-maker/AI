---
source_url: https://docs.coze.cn/tutorial/dynamic_modification_of_prompt
title: '动态修改提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:19Z
---

# 动态修改提示词 - 文档 - 扣子

动态修改提示词

本文介绍在智能体和工作流中如何动态修改提示词。通过设置变量，并动态传入变量的值，开发者可以灵活调整提示词，以便提升智能体的适应性和灵活性，使其能够根据不同的用户需求和场景动态调整输出。例如多语言支持、个性化回答或特定领域的问答。​

在智能体中动态修改提示词​

智能体支持在人设与回复逻辑中设置提示词变量，调用发起对话 API 时，通过 custom_variables 参数动态替换变量的值。无需将提示词硬编码为固定内容。本文以翻译场景为例，演示如何在智能体中动态修改提示词。​

步骤一：智能体的提示词中定义变量​

在智能体的人设或回复逻辑中，使用双大括号定义可替换的变量，例如 {{language}}。发布智能体。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27220.35398230088495%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/86647330403647dca4fa9d07da85869e~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：发起对话时在变量中动态传入提示词​

调用​发起对话 API 时，通过 custom_variables 参数传入提示词变量及其对应的值。​

custom_variables 中的变量名需与智能体提示词中双大括号中的变量完全一致。在本场景中，变量名为language，通过设置不同的值，可以动态修改提示词。示例代码如下：​

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v3/chat?' \​

-H 'Authorization: Bearer pat_hfwkehfncaf****' \​

-H 'Content-Type: application/json' \​

-d '{​

"bot_id": "734829333445931****",​

"user_id": "12345678***",​

"stream": true,​

"additional_messages": [​

{​

"content": "你好",​

"content_type": "text",​

"role": "user",​

"type": "question"​

}​

],​

"custom_variables": {​

"language": "英文"​

}​

}'​

​

场景演示​

在 language 中设置翻译为英文，智能体将自动将用户输入的内容翻译成英文并返回结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27565.0118203309693%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjU2NS4wMTE4MjAzMzA5NjkzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

在 language 中设置翻译为法文，智能体将自动将用户输入的内容翻译成法文并返回结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27578.0141843971631%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjU3OC4wMTQxODQzOTcxNjMxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

在对话流中动态修改提示词​

在对话流中，你可以在对话流的开始节点定义自定义参数（例如 prompt），并在执行对话流时通过 parameters 参数动态传入自定义参数的值，从而实现提示词的动态修改。​

步骤一：在对话流开始节点添加自定义参数​

在对话流的开始节点添加一个自定义参数，例如 prompt。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27325.9259259259259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjMyNS45MjU5MjU5MjU5MjU5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤二：在大模型节点引用提示词变量​

1.

在大模型节点的输入参数中，添加 prompt 和 USER_INPUT 参数，参数的值分别引用开始节点的 USER_INPUT 和 prompt。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27500%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在系统提示词中，引用 {{prompt}} 变量，通过变量动态传入提示词。在用户提示词中，引用 {{USER_INPUT}} 变量，获取用户实际输入的内容。​

3.

发布工作流。​

步骤三：执行对话流时动态传入提示词​

调用 ​执行对话流 API，在 parameters 参数中传入自定义参数及其对应的值。​

parameters 参数中的变量名需与工作流中定义的变量名保持一致。在本场景中，变量名为 prompt，通过设置不同的值，可以动态修改系统提示词。示例代码如下：​

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v1/workflows/chat' \​

-H 'Authorization: Bearer pat_hfwkehfncaf****' \​

-H 'Content-Type: application/json' \​

-d '{​

"parameters": {​

"prompt": "将用户的输入翻译为英文"​

},​

"workflow_id": "74423***",​

"bot_id": "7439828073***",​

"conversation_id": "74834801244913****",​

"additional_messages": [​

{​

"content": "你好",​

"content_type": "text",​

"role": "user",​

"type": "question"​

}​

]​

}'​

​

场景演示​

设置 prompt 参数为将用户的输入翻译为英文，智能体将自动将用户输入的内容翻译成英文并返回结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27287.2037914691943%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI4Ny4yMDM3OTE0NjkxOTQzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

设置 prompt 参数为续写用户输入，智能体将根据用户的输入内容生成后续内容，实现文本续写功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27285.3080568720379%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI4NS4zMDgwNTY4NzIwMzc5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

上一篇

迁移至企业版

下一篇

通过抖音支付插件变现