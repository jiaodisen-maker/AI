---
source_url: https://docs.coze.cn/dev_how_to_guides/message_feedback
title: '消息评价 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:05Z
---

# 消息评价 - 文档 - 扣子

消息评价

消息评价功能允许用户对智能体或应用回复的消息进行点赞、点踩及详细评论。该功能支持通过 API 调用和 Chat SDK 集成两种方式实现，为用户提供便捷反馈渠道。同时，它帮助开发者快速收集用户意见，使开发者能够直接了解智能体回复的质量，并针对性地优化算法、调整知识库内容或改进对话逻辑，从而为用户提供更精准、更有帮助的回答。​

功能简介​

消息评价功能允许用户对智能体或应用回复的消息进行评价，主要包括点赞、点踩以及提交详细的评论。无论是“一问一答”还是“一问多答”场景，每条消息的评价都是独立的，不会相互覆盖或影响。如果用户对同一条消息多次提交评价，系统将仅保留最后一次的评价内容。​

消息评价功能仅支持对以下两种发布渠道中的消息进行评价：​

  * Chat SDK：集成 Chat SDK 的应用界面中，用户可直接在消息下方操作点赞 / 点踩。​

  * API 渠道：通过调用发起对话 API 或执行对话流 API 获取文本消息回复后，可调用评价 API 提交反馈。​

通过 Chat SDK 配置消息评价功能​

当智能体或扣子应用发布 Chat SDK 后，开发者可以设置是否允许用户对消息进行点赞或点踩，默认禁用消息评价功能。​

开发者可以在 WebChatClient 方法的 ui.chatBot 参数中，配置是否允许用户对智能体的回答进行评价（点赞 / 点踩）。详细参数说明参见​安装并使用 Chat SDK。​

开启消息评价的示例代码如下：​

​

TypeScript

复制

ui: {​

chatBot: {​

// 基础UI配置​

title: "智能助手",​

​

// 消息评价功能配置（独立模块）​

feedback: {​

isNeedFeedback: true, // 是否启用反馈功能​

feedbackPanel: { // 反馈面板详细配置​

title: '您对这个回答有什么看法？请告诉我们',​

placeholder: '请详细描述您的问题...',​

tags: [ // 反馈标签选项​

{​

label: '内容不够详细'​

},​

{​

label: '内容错误'​

},​

{​

label: '其他',​

isNeedDetail: true // 选择此标签时需要填写详细说明​

}​

]​

}​

}​

}​

}​

​

说明

仅点踩时会弹出反馈卡片，供用户填写反馈标签内容。​

​

通过上述代码，开发者可以轻松地在 App 中启用消息评价功能，用户可直接在智能体或扣子应用回复的消息下方操作点赞 / 点踩。消息评价的界面效果类似如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27397.22222222222223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM5Ny4yMjIyMjIyMjIyMjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

通过 API 对消息进行评价​

通过调用发起对话 API 或执行对话流 API 获取文本消息回复后，可调用评价 API 提交反馈。​

1.

发起对话，获取智能体或扣子应用的回复消息的消息 ID。​

  * 调用​发起对话API 创建对话。​

  * 如果是流式响应，可以直接在返回结果中获取智能体返回的 type=answer 类型的文本消息的消息 ID。如果是非流式响应，返回结果中不返回消息 ID，可以执行步骤 2 查看消息 ID。​

  * 调用​执行对话流API，在对话流返回的 conversation.message 对象中获取 type=answer 类型的文本消息的消息 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27308.5714285714286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwOC41NzE0Mjg1NzE0Mjg2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

（可选）你也可以调用​查看消息列表 API 查看对应的消息 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27429.5874822190612%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQyOS41ODc0ODIyMTkwNjEyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

提交消息评价。​

  * 说明

仅支持评价以下来源的文本消息：​

    * 通过发起对话 API 生成的 type=answer 类型的文本消息。​

    * 通过执行对话流 API 返回的文本消息。​

​

  * 会话创建者调用​提交消息评价 API，根据会话 ID 和消息 ID 对智能体或应用回复的指定消息进行评价，包括点赞、点踩、添加自定义的反馈标签、具体评论。​

  * ​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v1/conversations/7515364893***/messages/752173729302***/feedback' \ ​

\--header 'Authorization: Bearer pat_xFWpGsNio4S7sfAzpu02vHCkAdL38VnSsTOIu8CkySdY9Z2xmeM8jjn***' \ ​

\--header 'Content-Type: application/json' \ ​

\--data-raw '{ ​

"feedback_type": "unlike", ​

"reason_types": [ ​

"内容有误", ​

"不够详细" ​

], ​

"comment": "实际参数应为 5.0 版本而非 4.0 版本。" ​

}' ​

​

  * 说明

无论是点赞的数据还是点踩的数据，都可以添加自定义的反馈标签。​

​

4.

（可选）删除消息评价。​

  * 如果出现误操作、评价内容错误或无效等情况，会话创建者可以调用​删除消息评价 API 删除指定消息的评价。 ​

查看消息评价数据​

开发者可以在扣子罗盘中根据 Feedback-Coze 对话 字段筛选消息的评价数据，以便快速收集和分析用户意见。通过对点踩的数据进行分析，开发者可以了解智能体回复的质量，并针对性地优化算法、调整知识库内容或改进对话逻辑。​

说明

仅智能体或扣子应用的所有者和协作者可以查看消息评价数据。​

​

1.

在扣子罗盘左侧导航栏选择观测 > Trace，在 Trace 列表中选择某条消息，或通过过滤器筛选消息评价的数据。查看方式选择 All Span，数据来源选择 Coze 智能体或 Coze 应用，过滤字段设置为 Feedback-Coze 对话属于点赞或点踩。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27203.125%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIwMy4xMjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

在 Trace 详情页面的调用树中单击 Message 节点，在右侧查看该消息的反馈结果和标签。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27465.74074074074076%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ2NS43NDA3NDA3NDA3NDA3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

​

上一篇

接收并处理回调

下一篇

通过 API 调用工作流