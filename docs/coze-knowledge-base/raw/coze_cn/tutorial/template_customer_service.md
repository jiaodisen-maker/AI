---
source_url: https://docs.coze.cn/tutorial/template_customer_service
title: '扣子智能客服 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:52:52Z
---

# 扣子智能客服 - 文档 - 扣子

扣子智能客服

扣子助手是扣子官方提供的客服场景的智能体。你可以通过复制该模板，快速创建和定制一个满足自己业务场景的智能客服智能体。​

说明

扣子编程的智能客服搭建方案已全面升级。升级后的方案编排更简洁、效果更优秀、满意度更高。具体方案，请参考​升级版扣子助手能力拆解。​

​

​

​

__

Replay

Play

00:00 / 03:59 Live

00:00

Fullscreen 

Cssfullscreen 

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag 

​

​

点击[这里](<https://www.coze.cn/template/agent/7416353271499096116?>)体验扣子助手智能体。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27605%27%20height=%27322%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ebe28f5a17b74c6db3a33bb8a6ce2724~tplv-goo7wpa0wc-quality:q75.image)​

​

AI 客服智能体的优势​

随着大语言模型能力的提高，智能客服已成为生成式 AI 的典型应用场景之一。与传统的智能客服机器人相比，基于 AI 能力的智能客服无论是用户使用体验还是维护成本上都有着显著优势。扣子集成了丰富的大语言模型供你选择，可快速生成问答能力。此外，扣子的开放能力和丰富的 AI 应用搭建能力，极大地简化了客服智能体的搭建和维护成本。​

​

对比项​| 传统智能客服​| AI-Powered 智能客服​  
---|---|---  
用户使用体验对比​| ​| ​  
交互体验​| 由于依赖预定义的规则和关键词匹配，传统客服机器人的对话往往显得生硬、不自然。​| 利用高级的自然语言处理（NLP）技术，能够理解和生成自然语言，使对话更加自然流畅。​  
回复准确性和效率​| 

  * 提供预定义的固定回答，无法灵活应对用户的多样化需求。​

  * 通常只能进行简单的问答，无法处理多轮对话，用户需要重复输入信息。​

| 

  * 支持多轮对话，能够进行更复杂和深入的互动，减少用户的重复输入。​

  * 能够理解对话的上下文，并且能够通过知识库的内容进行总结和提炼，提供更相关和准确的回答。​

  
个性化服务​| 无法根据用户的历史记录和偏好提供个性化的服务，用户体验较为单一。​| 根据用户的历史记录和偏好，提供个性化的服务和推荐，提升用户体验。​  
搭建和维护成本对比​| ​| ​  
搭建成本​| 

  * 通常需要借助第三方客服机器人平台或工具，需要一定的搭建和部署成本。​

  * 规则和关键词设置：需要大量时间和人力来定义规则和关键词。​

| 

  * 基于扣子的智能客服模板可以快速复制一个智能客服智能体，并支持进行定制化改造。​

  * 除了丰富的发布渠道外，扣子提供了各种接口和 Web SDK 能力，支持与已有应用快速集成。​

  
维护成本​| 

  * 需要手工、定期维护知识库内容。容易因为知识库更新不及时导致回复内容不准确。​

| 

  * 支持实时自动更新在线知识库，并能够对知识库内容进行提炼和总结。​

  
  
​

扣子智能客服模板介绍​

基于扣子的官方智能客服——扣子助手的最佳实践和经验沉淀，扣子将扣子助手制作成智能体模板，方便开发者一键复制和定制改造。​

业务流程​

扣子智能客服智能体解决了智能客服在落地过程中的共同痛点问题：​

  * 无法准确识别用户意图并做出分类解答。​

  * 无法准确召回企业知识库进行正确回复。​

  * 无法高效分析智能客服回复效果并及时更新知识库。​

下图展示了扣子助手智能体的流程。​

1.

当用户向小助手发起咨询后，小助手会首选判断用户咨询的问题是否与扣子产品有关。​

2.

如果是扣子使用的相关问题，则调用扣子知识库查找相关说明并使用大模型能力进行总结和回复。并且将消息记录写入到多维表格中，进行自动分析。​

3.

如果不是扣子使用的相关问题，则直接调用大语言模型进行回复，且不进行问题记录。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272112%27%20height=%27946.6508875739645%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjExMiIgaGVpZ2h0PSI5NDYuNjUwODg3NTczOTY0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

实现流程​

扣子助手智能体使用的是工作流模式（workflow-as-agent），工作流整体编排如下。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272505%27%20height=%27605.9548611111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwNSIgaGVpZ2h0PSI2MDUuOTU0ODYxMTExMTExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

问题分发​

通过意图识别节点判断用户意图，将问题分发到对应的分支处理。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27622%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjYyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

各节点说明如下：​

​

工作流节点​| 说明​| 示例​  
---|---|---  
开始节点​| 使用用户问题开始启动工作流。​实现方式：默认使用用户在智能体中提交的问题作为开始。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27127.55102040816327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjEyNy41NTEwMjA0MDgxNjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
意图识别节点​| 判断用户是否在咨询与产品使用的相关问题。​实现方式：使用意图识别节点，基于豆包·1.5·Pro·32k 模型对用户问题分类：扣子产品使用相关的问题、不相关的问题，并在系统提示词中对问题分类的规则进行定义。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27622%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjYyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

处理产品相关问题​

大模型参考历史对话改写用户的 Query，再根据 Query 检索知识库，并由大模型进行总结和输出。用户 Query、大模型回复均通过插件记录在指定的飞书多维表格中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271431%27%20height=%27498.53125000000006%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQzMSIgaGVpZ2h0PSI0OTguNTMxMjUwMDAwMDAwMDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

各节点说明如下：​

​

工作流节点​| 说明​| 示例​  
---|---|---  
大模型 0​| 参考历史对话改写用户的 Query。​实现方式：在大模型节点中定义一个用户问题理解专家的角色，并提供详细的提示词。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27631.413612565445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjYzMS40MTM2MTI1NjU0NDUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
知识库节点​| 根据用户问题检索并召回对应的产品知识。​实现方式：首先将产品相关的资料上传至扣子知识库，然后使用知识库节点选择要使用的知识库内容，并使用混合检索策略对内容进行召回，提升命中率。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27628.6472148541114%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjYyOC42NDcyMTQ4NTQxMTE0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
大模型 1​| 本工作流中添加了两个大模型节点。其中一个大模型节点用于对知识库召回的扣子产品教程内容进行进一步总结和输出。​实现方式：在大模型节点中定义一个具备产品专业知识的角色，并提供详细的提示词。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27515.6812339331619%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjUxNS42ODEyMzM5MzMxNjE5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
代码节点​| 将和产品相关的用户问题和回复进行标准化的数据处理。​实现方式：根据输入的参数构建一个包含用户问题和对应的的回复的结构化数据对象。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27328.0612244897959%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjMyOC4wNjEyMjQ0ODk3OTU5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
插件节点​| 将代码节点处理的用户问题和回复写入小助手管理员的飞书多维表格。​实现方式：使用[飞书多维表格插件](<https://www.coze.cn/store/plugin/7395043460165779483>)，设置授权方式，填入创建好的多维表格 URL。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27672%27%20height=%27446.22924901185775%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcyIiBoZWlnaHQ9IjQ0Ni4yMjkyNDkwMTE4NTc3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

处理其他问题​

此分支中有一个大模型节点，用于当用户咨询非产品问题时进行回复。​

实现方式：定义一个具备产品基础知识的回复助手。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27498.47715736040607%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ5OC40NzcxNTczNjA0MDYwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用扣子智能客服模板​

准备工作​

创建飞书应用​

扣子助手智能体模板中使用飞书应用将智能体的用户问题写入到多维表格中。因此，你需要创建一个飞书应用。​

1.

登录[飞书开发者后台](<https://open.larkoffice.com/app?lang=zh-CN>)。​

2.

单击创建企业自建应用，根据引导完成应用创建。更多详细信息可参考[创建自建应用](<https://open.feishu.cn/document/home/introduction-to-custom-app-development/self-built-application-development-process>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27142%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在应用配置页面，单击权限管理，应用开通多维表格的读写（新增记录和查看、评论、编辑和管理多维表格）权限。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27321%27%20height=%27155%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIxIiBoZWlnaHQ9IjE1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击版本管理与发布，创建一个版本并完成应用发布。​

创建并配置飞书多维表格​

扣子助手智能体模板中使用飞书多维表格来记录用户问题，并使用飞书多维表格的 AI 能力自动实现问题分析。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27703%27%20height=%27259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAzIiBoZWlnaHQ9IjI1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为了方便体验，你可以使用我们提供的多维表格模板，快速复制一个多维表格。​

1.

访问[这里](<https://ncpkm88jg5.feishu.cn/base/IRhBbIsCkaqxUSsS0GictKoLnze?from=from_copylink>)打开小助手用户问题记录多维表格模板。​

2.

单击使用该模板复制一个多维表格文档，并修改复制的多维表格名称。​

3.

单击设置图标，选择更多 > 添加文档应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27346%27%20height=%27378%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ2IiBoZWlnaHQ9IjM3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在搜索框中输入上一步已发布的飞书应用名称，然后选中该应用，并给该应用授予编辑权限。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27147%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUwIiBoZWlnaHQ9IjE0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置表格数据同步​

当小助手发布后，你可以将小助手记录在多维表格中的有效问题，通过自动化的方式自动同步到这个常见问题文档中。​

我们可以借助飞书机器人指令模板来搭建一个数据同步流程，将小助手的多维表格问答记录中添加为 FAQ 数据标注为是的问答记录同步到一个常见问题的飞书表格中。​

1.

创建一个飞书表格文档，并添加常见问题和解决方案两个字段。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27310%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEwIiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

访问飞书应用中心的[飞书机器人助手](<https://app.feishu.cn/app/cli_9d4d38c2a8bd5102>)，然后单击打开，根据引导完成应用安装。​

3.

打开[飞书机器人助手页面](<https://botbuilder.feishu.cn/home>)。​

4.

在我的指令页签下，找到多维表格跨表数据同步，然后单击使用模板。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27546%27%20height=%27198%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ2IiBoZWlnaHQ9IjE5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在展示的指令配置页面，删除第一个节点。​

6.

单击触发器选择框，然后选择多维表格内容变更。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27373%27%20height=%27234%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzczIiBoZWlnaHQ9IjIzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

单击由数据表内容变更触发文本框，然后选择用于记录小助手问答的多维表格，将条件设置为添加为 FAQ 为“是”时触发。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27366%27%20height=%27319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY2IiBoZWlnaHQ9IjMxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

删除第二个节点，参考上述步骤，添加新增电子表格记录事件。​

9.

单击新增记录文本框，然后选择步骤一中创建的飞书表格文档，将多维表格中记录的用户问题和回复写入到这个表格中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27373%27%20height=%27216%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzczIiBoZWlnaHQ9IjIxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

10.

单击启用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27373%27%20height=%27182%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzczIiBoZWlnaHQ9IjE4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 启用后，每次当你将一条多维表格中记录的添加为 FAQ 标记为是时，该条记录就会自动写入到飞书表格中。​

  * 完成以上准备工作后，你就可以通过扣子助手模板快速搭建一个智能客服智能体了。​

步骤一：创建知识库​

RAG （Retrieval-Augmented Generation 检索增强生成）技术被广泛应用于问答类型的智能体搭建中。RAG 指的是在回答问题或生成文本时，先从大规模文档库中检索相关信息，然后利用这些检索到的信息来生成响应或文本，从而提高回复内容的质量。​

RAG 的两个关键阶段：​

  * 检索阶段：使用编码模型基于问题检索相关文档。​

  * 生成阶段：使用检索到的上下文作为条件生成文本。​

RAG 技术的应用可以很好地解决大模型的胡乱编造的问题，即让大模型在回答用户问题前先参考知识库中的相关内容，可极大抑制大模型的幻觉现象。​

扣子的知识库功能支持上传外部数据，上传后可自动分段和编码，实现 RAG 对话。因此，在开始搭建客服智能体前，你需要先收集和整理要上传至知识库的产品资料。​

当你准备好知识库内容后，可以先将这些资料上传至知识库。​

上传在线资料​

参考以下操作，将产品相关的在线资料上传至扣子知识库中。本教程中以一个火山引擎产品的帮助文档为例。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

选择一个工作空间。单击知识库页签。​

3.

在知识库页面，单击创建知识库。​

4.

在创建知识库页面，选择文本格式，然后输入一个知识库名称，再选择在线数据，最后单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27270%27%20height=%27407%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcwIiBoZWlnaHQ9IjQwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

选择自动采集，然后选择批量添加方式，输入帮助中心的地址，再单击导入。​

6.

选择要导入的内容，然后单击确认。全部内容上传完成后，单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27261%27%20height=%27405%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYxIiBoZWlnaHQ9IjQwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

分段方式选择自动分段与清洗，然后单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27333%27%20height=%27256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzIiBoZWlnaHQ9IjI1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

单击确认完成知识库内容创建和分段。​

上传飞书表格文档​

在本模板中，需要添加一个表格文档记录产品使用的常见问题。这些常见问题从小助手的问答记录中整理而来，作为知识库内容提升问题回复的准确性和覆盖度。​

参考以下操作创建表格文本知识库：​

1.

在知识库页面，单击创建知识库。​

2.

在创建知识库页面，选择表格格式，然后输入一个知识库名称，再选择飞书表格，最后单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27236%27%20height=%27350%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2IiBoZWlnaHQ9IjM1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

如果你是第一次上传飞书文档，根据提示完成授权。​

4.

选择已创建的飞书表格文档并选择自动更新频率，然后单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27484%27%20height=%27125%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg0IiBoZWlnaHQ9IjEyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

配置表格结构，将用户问题配置为索引列，然后单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27488%27%20height=%27158%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg4IiBoZWlnaHQ9IjE1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

根据引导完成上传。​

步骤二：复制并修模板配置​

完成知识库内容准备后，就可以复制模板进行智能体搭建了。​

2.1 复制模板​

1.

打开[扣子助手](<https://www.coze.cn/template/agent/7416353271499096116?>)智能体，然后单击复制。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI0IiBoZWlnaHQ9IjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选择智能体的所属空间并输入一个智能体名称，然后单击确定。​

3.

在复制的智能体编排页面，单击智能体名称旁的修改图标，修改智能体名称。​

4.

根据实际需求，修改开场白文案和预置问题。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27401%27%20height=%27205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAxIiBoZWlnaHQ9IjIwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.2 修改工作流​

1.

进入复制的智能体。​

2.

单击左侧搭建面板中的工作流。​

3.

按需修改工作流配置。​

a.

（可选）单击工作流名称旁边的修改图标，修改工作流名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27487%27%20height=%2766%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg3IiBoZWlnaHQ9IjY2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

b.

找到工作流中的意图识别节点，展开系统提示词修改提示词内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27565.4450261780105%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjU2NS40NDUwMjYxNzgwMTA1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

c.

找到工作流中的大模型节点，根据自己的实际需求修改大模型的提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27437.66578249336874%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQzNy42NjU3ODI0OTMzNjg3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

找到工作流中的知识库节点，删除复制的知识库，添加上一步中准备好的知识库。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27604.7745358090186%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjYwNC43NzQ1MzU4MDkwMTg2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

e.

找到工作流中的多维表格插件节点，修改插件中的以下配置。​

  * app_token：输入已创建的多维表格 URL。​

  * records：引用使用异步函数构建用户问题节点的输出参数 records。​

  * 授权方式：选择单独授权。详细说明，请参考​如何设置 OAuth 插件的授权模式？。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27475%27%20height=%27186%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc1IiBoZWlnaHQ9IjE4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

f.

单击试运行测试工作流，工作流测试通过后，再单击发布。​

2.3 测试并发布智能体​

完成工作流修改后，你就可以测试智能体效果并发布上线了。​

1.

进入智能体编排页面。​

2.

在右侧调试区域，输入问题进行测试。你也可以单击创建测试集，方便测试调优效果。​

3.

完成测试后，单击发布将智能体发布到需要的渠道中。​

步骤三：分析用户问题​

根据工作流的配置，每次用户提交的问题都会写入到飞书多维表格中并通过 AI 能力自动完成分析。完成小助手发布上线后，你就可以对小助手的问答进行分析和总结了。​

1.

打开记录小助手问答的多维表格查看用户问题记录。​

  * 下图是根据模板创建的一个智能客服智能体的问答记录（记录的内容是通过工作流中的多维表格插件自动生成的），其中：​

  * 用户问题和 Bot 回复 分别是用户提交的问题和智能体的回复内容。​

  * 原始问答、分类和解决状态都是通过多维表格的 AI 能力自动生成的。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27608%27%20height=%2795%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA4IiBoZWlnaHQ9Ijk1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

分析用户问答。如果某一个问答记录可以作为一个常见问题补充到扣子智能体知识库中，你可以将是否添加为FAQ设置为是。配置后，这条记录会自动同步到飞书常见问题文档中。​

  * 打标后的多维表格文档示例。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27583%27%20height=%27111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgzIiBoZWlnaHQ9IjExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 自动同步后的常见问题文档示例。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27580%27%20height=%27234%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgwIiBoZWlnaHQ9IjIzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

你也可以基于多维表格的仪表盘功能，对问答情况进行数据分析，查看问题分布和解决率等。​

​

上一篇

升级版扣子助手能力拆解

下一篇

提炼电商卖点