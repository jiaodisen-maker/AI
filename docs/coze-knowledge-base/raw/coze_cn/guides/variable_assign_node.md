---
source_url: https://docs.coze.cn/guides/variable_assign_node
title: '变量赋值节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:17Z
---

# 变量赋值节点 - 文档 - 扣子

变量赋值节点

低代码工作流中的变量赋值节点是工作流中用于修改和存储变量值的节点。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27152.50463821892393%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6e2bed846bce455a82e66945f31fcb50~tplv-goo7wpa0wc-quality:q75.image)​

​

节点说明​

通过变量赋值节点，将特定的值赋给变量，可以实现数据的动态更新和传递，使工作流能够根据实时数据做出相应的处理和决策。变量赋值节点应用广泛，例如：​

  * 存储中间结果：在工作流中，将中间计算或处理的结果通过变量赋值节点存储到变量中，以便后续节点使用。例如，在开发一个智能医疗诊断应用时，需要对患者的病历数据进行预处理，如提取关键症状、检查结果等信息。此时，可以设置一个变量patient_info，将患者的病例数据通过变量赋值节点存储起来，后续在进行疾病诊断时，可以直接从patient_info变量中获取患者的详细信息。​

  * 记录用户输入：在与用户交互的工作流中，用户的输入信息是后续处理的重要依据。通过变量赋值节点，可以将用户的输入存储到变量中。例如，在开发一个智能客服机器人时，当用户向客服机器人咨询产品问题时，机器人提取用户关心的问题的关键词，然后将这些关键词通过变量赋值节点存储到一个名为user_query的变量中。在后续的处理节点中，机器人会根据user_query变量中的内容，从知识库中检索相关的答案或解决方案，并生成回复文本。​

  * 控制流程分支：在工作流中，通常需要根据不同的条件来决定执行不同的分支流程。变量赋值节点可以用来设置控制流程分支的条件变量，通过赋予变量不同的值，来引导工作流走向相应的分支。例如，在开发一个个性化推荐系统时，需要收集用户的基本信息和行为数据，如年龄、性别、浏览历史等，然后分析用户的兴趣偏好，并将结果通过变量赋值节点存储到一个名为user_preference的变量中。在生成推荐内容时，根据user_preference变量值来决定推荐策略。​

配置变量赋值节点​

为变量赋值时，在变量赋值节点的输入中添加需要赋值的参数。​

  * 变量名对应关联的智能体或应用中已创建的变量，如果该工作流未绑定包含变量的智能体或应用，单击变量名时根据页面提示选择智能体或应用中的相应变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27254.6641791044776%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjI1NC42NjQxNzkxMDQ0Nzc2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 变量值可以设置为固定值，也可以引用上游节点的输出参数。​

说明

变量赋值节点可以为用户变量、应用变量赋值，但不能为系统变量赋值。​

​

配置示例​

例如，在应用中搭建一个猜谜游戏对话流。​

1.

先创建一个空白应用，并定义应用变量score，默认值设置为 0 。​

2.

在对话流中添加变量赋值节点，每猜对一个谜语，变量score数值加 1，重新开始新的一局游戏时，score都会重置为游戏设定的初始值 0。​

对话流流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272274%27%20height=%27566.4768683274021%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI3NCIgaGVpZ2h0PSI1NjYuNDc2ODY4MzI3NDAyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

节点配置如下：​

​

节点类型​| 说明​| 示例​  
---|---|---  
开始节点​| 工作流的起始节点，本示例保持默认参数即可。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27354%27%20height=%27518.4981412639405%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU0IiBoZWlnaHQ9IjUxOC40OTgxNDEyNjM5NDA1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
循环节点​| 用于指定猜谜游戏的次数，需要设置：​

  * 循环类型：选择指定循环次数。​

  * 循环次数：本示例设置为 5。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27228.3464566929134%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIyOC4zNDY0NTY2OTI5MTM0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
大模型节点（出谜人）​| 用于生成谜语，需要设置：​

  * 系统提示词：设置出谜专家的人设，可以通过 AI 自动生成。​

  * 输出：定义两个变量。​

  * riddle：模型生成的谜语。​

  * answer：谜语的谜底。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27362%27%20height=%271098.1115241635687%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYyIiBoZWlnaHQ9IjEwOTguMTExNTI0MTYzNTY4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
问答节点​| 用于向用户提出谜语问题，需要设置：​

  * 输入：定义 riddle 参数，引用大模型节点（出谜人）生成的谜语问题。​

  * 提问内容：本示例设置为{{riddle}}。​

  * 回答类型：本示例选择直接回答。​

  * 输出：定义 user_answer 参数，用于接收用户的回答。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27360%27%20height=%27772.193308550186%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYwIiBoZWlnaHQ9Ijc3Mi4xOTMzMDg1NTAxODYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
大模型节点（谜语裁判）​| 用于判断用户回答的正确性，需要设置：​

  * 输入：定义四个变量。​

  * riddle：引用大模型节点（出谜人）生成的谜语问题。​

  * answer：引用大模型节点（出谜人）生成的谜底。​

  * user_answer：引用问答节点的输出参数。​

  * score：引用应用变量score。​

  * 系统提示词：设置谜语裁判的人设，可以通过 AI 自动生成。​

  * 用户提示词：设置为谜语的谜面是{{riddle}}，正确答案是{{answer}}，用户的回答是{{user_answer}}。​

  * 输出：定义两个参数。​

  * total_score：用户猜谜游戏的分数。​

  * conclusion：用户猜谜的结果。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27344%27%20height=%271213.5910780669146%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ0IiBoZWlnaHQ9IjEyMTMuNTkxMDc4MDY2OTE0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
变量赋值节点​| 用于存储用户在猜谜游戏中的分数，将大模型节点（谜语裁判）中 total_score 的值赋给变量 score。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27352%27%20height=%27259.092936802974%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUyIiBoZWlnaHQ9IjI1OS4wOTI5MzY4MDI5NzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
输出节点​| 用于输出用户猜谜的结论，并告知游戏的得分，需要设置：​

  * 输出变量：定义两个变量。​

  * output：引用大模型节点（谜语裁判）的输出参数 conclusion。​

  * score：引用应用变量 score。​

  * 输出内容：设置为{{output}}，你当前得分为：{{score}}。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27356%27%20height=%27385.11524163568777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU2IiBoZWlnaHQ9IjM4NS4xMTUyNDE2MzU2ODc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
文本处理节点​| 用户游戏结束，展示最终的游戏得分，需要设置：​

  * 输入：将应用变量 score 的值赋给 String1。​

  * 字符串拼接：设置为游戏结束！你本次总得分为{{String1}}，欢迎再次挑战哦~。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27358%27%20height=%27459.1449814126394%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU4IiBoZWlnaHQ9IjQ1OS4xNDQ5ODE0MTI2Mzk0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
结束节点​| 选择返回文本模式，并设置输出变量和回答内容。​

  * 输出变量：定义 output 参数，引用文本处理节点的输出参数 output。​

  * 回答内容：设置为{{output}}。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27358%27%20height=%27391.271375464684%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU4IiBoZWlnaHQ9IjM5MS4yNzEzNzU0NjQ2ODQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

常见问题​

变量赋值节点能为系统变量赋值吗？​

系统变量仅可读不可写，所以不能通过变量赋值节点为系统变量赋值。​

变量赋值节点能读取变量值吗？​

目前，除了开始节点、输入节点、知识库写入节点外，其他所有节点都能读取变量值，详细可参考​读取变量值。​

​

上一篇

删除数据节点

下一篇

知识库写入节点