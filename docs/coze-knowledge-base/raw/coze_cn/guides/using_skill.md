---
source_url: https://docs.coze.cn/guides/using_skill
title: '使用技能 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:27:43Z
---

# 使用技能 - 文档 - 扣子

使用技能

技能是一个专为特定领域设计的知识库和工具包，用于指导智能体如何完成指定的任务。使用技能后，扣子 AI 会在处理专业任务上有更好的表现，例如根据指定的风格指南与格式撰写文档、根据指定的设计风格开发一个应用等。本文档介绍如何在扣子编程、扣子中使用技能。​

使用场景​

扣子 AI 会加载技能的介绍信息，如果判断技能与当前任务有关，将自动安装并触发技能来完成任务。通过技能的渐进式披露机制，扣子 AI 可以在节约上下文窗口的同时访问专业领域的知识。​

在不同使用环境下，技能对应不同的使用场景，例如：​

  * 在扣子编程中辅助开发​

  * 使用前端设计类技能，让扣子 AI 根据指定的设计风格开发网页应用。​

  * 使用流程类技能，让扣子 AI 根据指定的提取流程开发发票提取工作流。​

  * 在扣子中协助处理复杂任务​

  * 使用写作类技能，让扣子 AI 根据指定的风格指南与格式撰写文档。​

  * 使用审核类技能，让扣子 AI 依据公司的法务标准审查合同文件。​

在扣子编程中使用技能​

在扣子编程中开发智能体、工作流或应用等项目时，扣子 AI 会在已添加的技能中自动搜索并加载合适的技能，然后读取技能的使用指南，并遵循该指南来完成开发任务。​

说明

  * 最多添加 50 个编程技能。​

  * 存在同名技能时，扣子 AI 会根据技能的功能描述，选择最贴合当前任务的技能。如果功能描述类似，则遵循“自定义技能 > 官方技能”以及“最新上传 > 早期上传”的选择原则。​

​

技能类型​

在扣子编程中，扣子 AI 可以加载已添加的官方技能和我的技能。​

  * 官方技能：由扣子官方开发和维护的编程技能。不同项目能用的官方技能并不完全一样，系统会根据项目类型自动添加匹配的技能。目前，所有扣子编程的集成服务均有配套的官方技能。如果要使用外部集成相关的技能，需要先完成集成配置。关于集成服务的更多信息，请参考​集成服务概述。​

  * 说明

请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

  * 我的技能：由开发者自行维护的自定义技能。你可以根据个人经验和工作需求来开发技能并使用。自定义的编程技能仅限你本人使用。​

步骤一：上传你的技能​

如果你要使用自定义技能，包括通过扣子编程以及通过其他渠道开发的技能，均需要通过本地上传方式，将技能包上传到扣子编程。​

说明

  * 通过扣子编程开发的技能，暂不支持直接在扣子编程中使用。你需要先将技能的 .skill 文件下载到本地，再通过本地上传功能上传到编程技能列表中。具体操作，请参考​下载技能包。​

  * 技能商店中的技能不支持在扣子编程中使用。​

​

1.

在开发项目对话框中，单击技能。​

2.

在编程技能面板中，选择创建技能 > 本地上传。​

3.

选择待上传的技能包。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271703%27%20height=%27620.0047281323878%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcwMyIgaGVpZ2h0PSI2MjAuMDA0NzI4MTMyMzg3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271695%27%20height=%27793.404255319149%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY5NSIgaGVpZ2h0PSI3OTMuNDA0MjU1MzE5MTQ5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

步骤二：添加技能​

上传技能包后， 你在当前账号下均可以使用该自定义技能。但为扣子 AI 添加自定义技能是单次生效的，每次开启新任务时，你都需要重新添加所需的自定义技能。​

1.

在开发项目对话框中，单击技能。​

2.

在我的技能中，单击目标技能对应的添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27580%27%20height=%27144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgwIiBoZWlnaHQ9IjE0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：扣子 AI 加载技能​

添加技能后，扣子 AI 会在项目开发过程中，会根据当前任务和上下文，自动搜索并加载合适的技能，然后读取技能的使用指南，并遵循该指南来完成开发任务。此外，你也可以在对话中通过自然语言明确指定需要使用的技能。​

在任务开发过程中，你也可以随时单击对话框中的技能来添加更多技能，新添加的技能将在下一轮对话中生效。​

例如，当你需要开发一个视觉风格鲜明的网页应用时，可以上传并添加一个前端设计类技能，扣子 AI 会加载该技能及其他所需官方技能来完成开发任务。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27615%27%20height=%27331%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE1IiBoZWlnaHQ9IjMzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在扣子中使用技能​

说明

  * 技能数量限制：每个用户最多只能启用 30 个第三方技能，其他类型的技能无数量限制。​

  * 企业技能商店限制：​

  * 套餐限制：仅企业版（企业标准版、企业旗舰版）支持企业技能商店。​

  * 角色限制：仅企业员工可访问企业市场，访客不支持发布、查看和使用企业市场中的技能。​

​

在扣子首页的对话框中输入你的任务指令，敲击回车键即可发起一个对话任务。扣子 AI 会根据你的任务指令，自动在技能商店中查找相关的技能。扣子 AI 会加载技能的介绍信息，如果判断技能与当前任务有关，将自动安装并触发技能来完成任务。更多信息，请参考​使用技能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27490%27%20height=%27242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkwIiBoZWlnaHQ9IjI0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

你也可以在对话中指定要使用的技能：​

  * 在商店中选用技能：在技能商店中选择感兴趣的技能，安装之后再单击使用，页面会自动跳转至扣子首页，输入你的任务要求即可。​

  * 选择商店技能：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271096%27%20height=%27849.4%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA5NiIgaGVpZ2h0PSI4NDkuNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用商店技能：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27889%27%20height=%27459.24644549763036%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODg5IiBoZWlnaHQ9IjQ1OS4yNDY0NDU0OTc2MzAzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

  * 在对话框中 @ 指定技能：​

  * 在扣子首页文本框中输入 @，并在技能页签中选择要使用的技能。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27450%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUwIiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

发布技能

下一篇

技能环境变量