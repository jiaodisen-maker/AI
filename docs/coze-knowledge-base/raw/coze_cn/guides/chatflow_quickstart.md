---
source_url: https://docs.coze.cn/guides/chatflow_quickstart
title: '使用对话流搭建低代码应用 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:12Z
---

# 使用对话流搭建低代码应用 - 文档 - 扣子

使用对话流搭建低代码应用

随着人工智能技术的不断进步，AI 助手开始越来越受欢迎，它们基于大模型的文本生成能力，用户可以通过自然语言与 AI 助手进行交流。对话式 AI 助手也可以集成到各种社交软件、应用程序中，提供给更多平台的用户使用。​

本教程详细指导你如何在扣子编程中基于对话流开发一个移动端 AI 助手，并将其发布到扣子商店。​

AI 助手介绍​

AI 助手利用大语言模型强大的文本生成能力，在对话过程中扮演助手的角色回答用户问题。AI 助手能够理解和回应用户的指令，提供信息查询、知识问答等多种服务。​

步骤一：设计 AI 助手功能​

在开始开发前，你需要设计 AI 助手的功能及对应的用户界面。​

通常情况下，AI 助手的核心功能是通过大语言模型回答用户的问题，且 AI 助手的界面应是类似通讯软件的对话式页面。此场景可以通过一个包含大模型节点的对话流实现。​

完成主体功能设计和规划后，就可以开始搭建低代码应用了。​

步骤二：创建低代码应用​

首先，你需要创建一个低代码应用。​

低代码应用支持使用工作流来完成复杂的业务逻辑编排，也支持使用数据库、知识库、插件等资源实现与本地数据或线上数据的交互。此外，低代码应用支持通过拖拉拽的方式搭建用户界面，并且能够实现与业务逻辑的联动。​

参考以下操作，创建低代码应用。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

3.

在低代码模式区域，将鼠标移动到更多，然后单击打开应用开发。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27444%27%20height=%27262%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/43cfb709f00d49e682f9668d4bab56cb~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

在应用模板页面，单击创建空白应用。​

5.

输入应用名称，并单击图标旁的 AI 图标使用 AI 自动生成一个图标。然后单击确认。​

  * 应用创建成功后，你会直接进入到应用的集成开发环境 (IDE)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27151%27%20height=%27153%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUxIiBoZWlnaHQ9IjE1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：编排业务逻辑​

创建完低代码应用项目后，你可以开始进行业务逻辑编排了。扣子编程提供了大模型、代码、意图识别、知识库写入与检索等丰富的工作流节点，以满足复杂的业务场景需求。此外，你还可以通过使用变量、插件、知识库等方式与你的本地数据和线上数据进行集成。​

本教程中的 AI 助手应用，主要使用大模型实现对话交互，所以只需要创建一个包含大模型节点的对话流即可。​

1.

在业务逻辑页面，找到工作流，然后单击 \+ > 新建对话流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27624%27%20height=%27284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI0IiBoZWlnaHQ9IjI4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

输入对话流名称和描述，然后单击确认。​

  * 扣子编程默认创建一个同名的会话，并为对话流绑定这个会话。对话流运行过程中产生的消息都会记录到这个会话中，大模型会参考会话中记录的历史消息，生成适合当前场景的回复。会话中的消息是用户的个人数据，用户之间的会话消息是相互隔离的，每个用户只能看到本人发起的对话数据。会话管理说明，请参考​管理低代码应用会话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27218%27%20height=%27219%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE4IiBoZWlnaHQ9IjIxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在工作流画布，单击开始节点的连接线或画布下方的添加节点按钮，然后选择大模型节点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27425%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI1IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

将开始节点、大模型节点和结束节点按顺序连接起来。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272238%27%20height=%27481.0902612826603%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzOCIgaGVpZ2h0PSI0ODEuMDkwMjYxMjgyNjYwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击开始节点进行配置。开始节点用于设定启动对话流需要的信息。​

  * 本场景中，用户需要提供要咨询的问题。这些内容默认通过开始节点的 USER_INPUT 参数传入，无需增加其他输入参数。为USER_INPUT 参数指定一个默认值，例如“你好”。其他参数维持默认配置即可。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27494%27%20height=%27339%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk0IiBoZWlnaHQ9IjMzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

单击大模型节点进行配置。大模型节点用于接收用户问题，并生成对应的回复。​

  * 需要添加的设置如下，其他参数维持默认的配置。​

  * ​

参数配置​| 说明​| 示例​  
---|---|---  
输入​| 在输入区域可以看到大模型节点预置了一个默认参数 input，单击设置图标，选择开始节点的 USER_INPUT 参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271208%27%20height=%27422.79999999999995%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwOCIgaGVpZ2h0PSI0MjIuNzk5OTk5OTk5OTk5OTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
开启对话历史​| 开启对话历史功能后，扣子编程会将会话中已存的近期消息作为对话历史传递给大模型，供大模型生成回复时作为参考，生成更符合语境的回复。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27758%27%20height=%27306.99%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzU4IiBoZWlnaHQ9IjMwNi45OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
系统提示词​| 在系统提示词区域，输入以下内容。​系统提示词是一组指示模型行为和功能范围的指令，可以包括如何提问、如何提供信息、如何请求特定功能等。系统提示词也用于设定对话的边界，比如告知用户哪些类型的问题或请求是不被接受的。​​Markdown复制# 角色​你是一个全能的 AI 助手，能够快速准确地回答用户的各种问题，并提供详细的解释和建议。​​## 技能：回答问题​1\. 当用户提出问题时，仔细分析问题的关键信息，使用工具进行搜索以获取准确的答案。​2\. 以清晰、简洁的语言回答问题，并提供相关的解释和例子。​​## 限制:​\- 只回答真实、准确的信息，拒绝编造或猜测答案。​\- 回答内容应简洁明了，避免冗长和复杂的表述。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27712%27%20height=%27843.72%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzEyIiBoZWlnaHQ9Ijg0My43MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
用户提示词​| 用户提示词通常是直接的命令，告诉模型要执行的任务或意图。指令越清晰，模型的输出也更贴近你的实际需求。​直接引用输入参数中定义的变量 {{input}}，表示使用开始节点的 USER_INPUT 参数作为用户提示词。​说明引用变量成功后，变量应是蓝色字体。如果你没有可用的变量，请检查是否按照教程配置了大模型节点的输入变量。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27702%27%20height=%27326.43%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAyIiBoZWlnaHQ9IjMyNi40MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

7.

选择结束节点进行配置。结束节点用于输出对话流的最终结果。​

a.

单击结束节点，然后选择返回文本。​

b.

选择大模型节点的输出结果作为输出参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27331%27%20height=%27215%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMxIiBoZWlnaHQ9IjIxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

在回答内容文本框中输入{{output}}，使用大模型的输出内容作为最终的回复。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27330%27%20height=%27132%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMwIiBoZWlnaHQ9IjEzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

开启流式输出，实现打字机一样的输出效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27324%27%20height=%27124%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI0IiBoZWlnaHQ9IjEyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 至此，你已经完成整个对话流的搭建。​

8.

设置 AI 角色信息。​

  * 单击角色，在角色配置对话框中设置角色信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27767%27%20height=%27514%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzY3IiBoZWlnaHQ9IjUxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 重要参数说明如下，详细的参数说明，请参考​AI 对话。​

  * ​

配置​| 说明​  
---|---  
角色名称​| 设置 AI 助手的名称，将显示在对话框中，例如 AI 助手。​  
角色描述​| 设置 AI 助手的角色描述，帮助用户了解角色的背景和功能。​  
角色头像​| 设置 AI 助手的头像。​  
开场白​| 设置 AI 助手的开场白，可以直接使用以下示例文案。​​Plain Text复制你好！我是你的专属 AI 助手。无论你需要查询信息、提供建议、还是简单的聊天，我都在这里为你服务。​告诉我你的需求，让我们开始愉快的对话吧！​​  
开场白预置问题。​| 为 AI 对话组件预置三个开场白问题，示例如下：​
    * 双子座有什么特点​
    * 推荐一本好书​
    * 想去新疆，有什么行程建议吗​  
  
​

9.

为了保证业务逻辑实现符合预期，需试运行对话流。​

a.

单击试运行。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27465%27%20height=%27180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY1IiBoZWlnaHQ9IjE4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

填写对话流入参配置。​

  * 根据页面提示选择一个会话。会话用于存储对话流产生的消息，包括用户的提问和模型的回复。下次执行时，对话流可以从会话中读取到之前存储的消息记录。在本教程中我们在创建对话流的同时创建了一个同名会话，这个同名会话会作为对话流的默认会话。​

  * 单击保存并开始对话调试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27680%27%20height=%27349%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgwIiBoZWlnaHQ9IjM0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

在输入框中输入一段内容，并按回车键发送。​

  * 我们在对话流的开始节点设置了 USER_INPUT 参数的默认值“你好”，这个默认值会自动填写在输入框，作为你的输入参考。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27170%27%20height=%27256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcwIiBoZWlnaHQ9IjI1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

扣子编程会自动运行对话流，并在试运行面板中展示你的输入和对话流执行的返回结果。​

  * 对话流的试运行面板默认为对话式，类似智能体的调试区域，展示每一次试运行此工作流时用户和模型的对话交互过程。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27686%27%20height=%27361%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg2IiBoZWlnaHQ9IjM2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 在完成业务逻辑搭建并通过试运行后，你就可以开始用户界面搭建了。​

步骤四：搭建用户界面​

​

扣子编程提供了可视化的用户界面搭建能力，你可以通过拖拉拽的方式搭建一个用户界面，无需编写一行代码。​

参考以下操作，搭建 AI 助手应用的用户界面。​

1.

在低代码应用 IDE 中，单击页面上方的用户界面页签。​

2.

选择页面类型。​

  * 低代码应用支持发布为小程序等移动端应用，也可以发布为 Web 页面等网页应用。这里我们选择小程序和 H5。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27451%27%20height=%27269%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUxIiBoZWlnaHQ9IjI2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

搭建页面布局。​

  * AI 助手应用只有一个简单的对话窗口，所以我们只需要搭建一个页面并添加 AI 对话组件即可。​

a.

在画布中选中页面，并在右侧 Page1 配置面板中关闭导航栏。​

  * 移动端页面默认开启首页底部的导航栏，AI 助手应用只有一个页面，所以需要手动关闭底部的导航栏。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27388%27%20height=%27249%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg4IiBoZWlnaHQ9IjI0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

在组件面板中，找到 AI 组件 > AI对话组件，然后将 AI 对话组件拖入到画布中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27501%27%20height=%27242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAxIiBoZWlnaHQ9IjI0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

设置组件属性。​

a.

在画布中，选中拖入的 AI对话组件。组件名称为Chat1。​

b.

在 Chat1 组件的属性配置面板中，选择步骤三中搭建的对话流，即 ai_assistant。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27347%27%20height=%27213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ3IiBoZWlnaHQ9IjIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置效果如下： ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27567%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI0IiBoZWlnaHQ9IjU2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤五：效果测试​

完成上述所有配置后，单击预览查看整体功能并进行体验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27277%27%20height=%27196%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc3IiBoZWlnaHQ9IjE5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

页面会展示 AI 助手在移动端的页面预览效果，你可以在页面下方的输入框中输入一段文字，并按回车键发送消息。AI 助手会立即回复你的问题。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27203%27%20height=%27418%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAzIiBoZWlnaHQ9IjQxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤六：发布应用​

完成应用测试后，你就可以将应用发布到商店、模板、各种社交渠道，或发布成 API 服务与其他应用集成。​

本教程中以发布到商店为例。​

1.

在应用 IDE 中，单击右上角的发布按钮。​

2.

在发布页面，输入版本号和发布描述。​

3.

选择扣子商店，然后选择应用分类。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272796%27%20height=%271348.1900237529692%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc5NiIgaGVpZ2h0PSIxMzQ4LjE5MDAyMzc1Mjk2OTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

4.

单击页面上的发布按钮，完成应用发布。​

  * 发布完成后，你就可以在扣子商店上使用这个应用了。​

相关文档​

  * ​编排业务逻辑​

  * ​用户界面编辑器概述​

  * ​低代码工作流介绍​

  * ​了解项目发布​

​

​

上一篇

快速搭建一个低代码应用

下一篇

使用低代码应用模板