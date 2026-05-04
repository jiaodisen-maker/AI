---
source_url: https://docs.coze.cn/guides/agent_prompt
title: '人设与回复逻辑 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:28Z
---

# 人设与回复逻辑 - 文档 - 扣子

人设与回复逻辑

人设与回复逻辑区域用于设置大模型的系统提示词，包括指定低代码智能体的人设、核心技能及具体任务等信息。提示词是一种自然语言指令，它为大语言模型（LLM）提供任务指导。搭建低代码智能体的第一步就是设置提示词，你可以根据业务需要直接编写提示词，也可以使用提示词模版、引用提示词资源或通过 AI 自动生成提示词。​

直接编写提示词​

你可以根据业务需要编写提示词，提示词编写得越清晰明确，智能体的回复也会越符合预期。关于如何编写提示词，请参考​编写提示词。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

3.

在低代码模式区域，单击智能体开发。​

4.

根据页面提示，创建一个新智能体。​

5.

在人设与回复逻辑面板中编写提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27335%27%20height=%27512%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7e98fc79185f4d45b4985b4b07df265a~tplv-goo7wpa0wc-quality:q75.image)​

​

使用提示词模版​

扣子编程根据不同的业务场景提供了多套提示词模版，你可以直接使用模版，或参考模版编写提示词。​

1.

在人设与回复逻辑面板中，单击提示词库图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27253%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在推荐页签下，选择系统推荐的提示词模版，然后单击插入提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27446%27%20height=%27261%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ2IiBoZWlnaHQ9IjI2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

单击插入提示词后，系统会将选择的提示词自动填充到提示词的编辑框中，你可以基于自己的业务场景修改提示词。修改提示词时，你需要重点关注提示词中的高亮部分。​

  * 添加文本：你可以根据高亮部分的文字引导，添加文本内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27572%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcyIiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 添加技能：如果提示词中引用了技能，你需要添加或替换为当前智能体或工作流中已经配置的技能，以确保技能可用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27575%27%20height=%27144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc1IiBoZWlnaHQ9IjE0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

引用提示词资源​

提示词可以作为资源保存在资源库中，供工作空间内的其他成员引用。引用提示词资源前，请确保资源库中已经创建了提示词，详情可参考​创建提示词 。​

说明

如果引用的提示词中包含了插件、工作流、图像流资源，而智能体中未配置该资源，引用提示词后，提示词中资源块名称会显示为灰色。此时，大模型不会调用对应资源，为智能体添加资源后，大模型方可按照提示词指令正常执行。​

​

1.

在人设与回复逻辑面板的右下角，单击提示词库。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27327%27%20height=%27489%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI3IiBoZWlnaHQ9IjQ4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在工作空间页签下，选择工作空间内的提示词资源，然后单击插入提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

单击插入提示词后，系统会将选择的提示词自动填充到提示词的编辑框中，你可以基于自己的业务场景修改提示词。修改提示词时，你需要重点关注提示词中的高亮部分。​

  * 添加文本：你可以根据高亮部分的文字引导，添加文本内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27572%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcyIiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 添加技能：如果提示词中引用了技能，你需要添加或替换为当前智能体或工作流中已经配置的技能，以确保技能可用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27575%27%20height=%27144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc1IiBoZWlnaHQ9IjE0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

AI 生成提示词​

你可以通过自然语言告诉 AI 你希望编写或优化的提示词，大语言模型会根据你的描述，自动生成提示词；你也可以根据调试结果，告诉大语言模型提示词哪里不符合预期以及你的预期效果，大语言模型会自动帮你完成优化。​

1.

在人设与回复逻辑面板的右上角，单击优化。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27441%27%20height=%27171%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQxIiBoZWlnaHQ9IjE3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

输入你希望编写或优化的提示词，单击发送图标，AI 会根据你的描述自动生成提示词。​

  * 如果你的智能体已完成调试，你可以单击根据调试结果优化，然后输入哪里不符合预期以及你的预期效果，大语言模型会自动帮你完成优化。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27519%27%20height=%27188%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE5IiBoZWlnaHQ9IjE4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

单击替换，AI 生成的提示词会自动填充到提示词编辑框中。​

  * 你也可以对 AI 生成的提示词执行以下操作：​

  * 退出：关闭 AI 生成的页面。​

  * 复制：复制 AI 生成的提示词。​

  * 重新生成：如果你对 AI 生成的提示词不满意或想要尝试不同的结果，可以单击重新生成图标，AI 会再次根据你的输入生成新提示词。​

  * 点赞：如果 AI 生成的提示词符合你的期望或对你有帮助，可以单击点赞图标，来给予正面反馈。​

  * 点踩：如果 AI 生成的提示词不满足你的需求，可以单击点踩图标，然后选择不满意的原因，帮助 AI 学习并改进未来的输出。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27351%27%20height=%27372%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUxIiBoZWlnaHQ9IjM3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

设置模型

下一篇

插件