---
source_url: https://docs.coze.cn/guides/agent_plugin
title: '插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:32Z
---

# 插件 - 文档 - 扣子

插件

插件是一个工具集，一个插件内可以包含一个或多个工具（API）。​

目前，扣子编程集成了类型丰富的插件，包括资讯阅读、旅游出行、效率办公、图片理解等 API 及多模态模型。使用这些插件，可以帮助你拓展低代码智能体能力边界。例如，在你的低代码智能体内添加新闻搜索插件，那么该智能体将拥有搜索新闻资讯的能力。​

关于插件的详细介绍，请参考​插件介绍。​

添加插件​

插件可以直接在智能体内使用，拓展智能体的能力边界。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

​

3.

在低代码模式区域，单击智能体开发。​

4.

根据页面提示，创建一个新智能体。​

5.

在智能体编排页面的技能 > 插件区域，添加插件。​

  * 支持通过以下方式添加插件：​

  * 直接添加插件：单击+图标，从工作空间或插件商店中挑选已发布的插件。如果没有合适的插件，也可以根据页面提示创建一个新的插件。​

  * 自动添加插件：单击自动添加图标，大模型会根据人设与回复逻辑，自动从商店中选择合适的插件添加到智能体中。​

  * 说明

使用大语言模型自动添加插件后，建议调试智能体，检查被添加的插件是否可以正常使用。​

​

6.

在添加插件页面，展开目标插件查看工具，然后单击添加。​

  * 单击资源库工具，可查看资源库中可用的插件工具。​

7.

在智能体的人设与回复逻辑区域，定义何时使用插件，然后在预览与调试区域测试插件功能是否符合预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27447%27%20height=%27294%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2888ec585ae34c3c92f60eb7f2e7797d~tplv-goo7wpa0wc-quality:q75.image)​

​

参数配置​

在智能体中添加插件后，可以通过参数配置灵活设置参数的默认值及可见性。参数的默认值可有效避免大模型运行时因插件参数值缺失而导致的报错。同时，针对一些值较为稳定的参数，设置其默认值且隐藏其可见性可减少大模型的无效判断，从而提高插件调用效率。​

使用场景​

场景 1：避免调用报错​

当用户与智能体交互时，如果未输入某些必要信息，而这些信息对于智能体中的大模型调用插件至关重要，那么在没有参数默认值时，大模型可能无法正常工作。例如在调用天气插件查询天气时，如果用户与智能体对话时未输入具体地域且对应的插件参数无默认值，那么智能体可能无法回答问题。如果为该参数设置了默认值（如杭州），即使用户未输入具体地域，大模型也会按照默认值进行调用，并返回答案，从而有效避免因参数值缺失导致的错误。​

未设置默认值​

  * 参数配置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27954%27%20height=%27297.0683544303797%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTU0IiBoZWlnaHQ9IjI5Ny4wNjgzNTQ0MzAzNzk3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 智能体问答​

  * 大模型未能正常回复问题。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27351%27%20height=%27156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUxIiBoZWlnaHQ9IjE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

设置默认值​

  * 参数配置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27937%27%20height=%27274.13429256594725%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTM3IiBoZWlnaHQ9IjI3NC4xMzQyOTI1NjU5NDcyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 智能体问答​

  * 大模型使用默认值回复问题。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27871%27%20height=%27407.3021582733813%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODcxIiBoZWlnaHQ9IjQwNy4zMDIxNTgyNzMzODEzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

场景 2：参数值稳定​

某些插件参数值较为稳定，不需要动态传入参数值，则建议为参数设置默认值，并关闭开启开关（参数对模型不可见），减少智能体中的大模型调用插件时的流程，提高调用效率。例如在调用头条搜索插件时，如果只希望每次返回三条信息，不需要模型进行动态判断，则可以设置插件 count 参数的默认值为 3，且关闭开启开关（参数对模型不可见）。如果设置 count 参数默认值为 3，但打开开启开关（参数对模型可见），则大模型仍会根据自身的逻辑判断返回的信息数量。​

  * 参数配置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27883%27%20height=%27445.915%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODgzIiBoZWlnaHQ9IjQ0NS45MTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 智能体问答​

  * 根据默认值，返回 3 条信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27857%27%20height=%27561.0575539568346%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODU3IiBoZWlnaHQ9IjU2MS4wNTc1NTM5NTY4MzQ2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

  * 参数配置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27869%27%20height=%27419.29249999999996%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODY5IiBoZWlnaHQ9IjQxOS4yOTI0OTk5OTk5OTk5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 智能体问答​

  * 虽然设置了默认值，但大模型仍自行判断了返回的信息数量，仅返回 2 条信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27859%27%20height=%27572.6666666666666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODU5IiBoZWlnaHQ9IjU3Mi42NjY2NjY2NjY2NjY2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

操作步骤​

1.

在指定插件右侧，单击编辑参数图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27108%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9IjEwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

修改参数配置。​

  * 默认值：设置参数的默认值。你可以输入固定值，或引用变量值，例如启动系统变量，并引用系统变量值。变量说明，请参考​变量。​

  * 开启：打开开关，表示参数对大模型可见，大模型可以读取该参数；关闭开关，表示隐藏参数，大模型无法读取该参数。​

  * 如果设置了参数默认值且打开开启开关，那么调用插件时，大模型会以该默认值为基础，但仍会根据自身的逻辑判断是否使用其他值。​

  * 如果设置了参数默认值且关闭开启开关，那么调用插件时，大模型只会使用这个默认值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27602%27%20height=%27148%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAyIiBoZWlnaHQ9IjE0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

绑定卡片数据​

添加到智能体的插件支持绑定消息卡片。绑定成功后，智能体以消息卡片的形式发送消息。​

注意

目前，消息卡片仅在豆包客户端、飞书客户端内生效。​

​

1.

在指定插件右侧，单击绑定卡片数据图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27427%27%20height=%27225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI3IiBoZWlnaHQ9IjIyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在智能体回复卡片配置对话框，选择扣子编程提供的官方卡片，或创建自定义卡片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

配置消息卡片后，卡片图标将会显示绿点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27449%27%20height=%27122%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ5IiBoZWlnaHQ9IjEyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

发布智能体，使配置生效。​

删除插件​

你可以为智能体删除一个不需要的插件。​

在指定插件的右侧，单击移除图标，即可删除添加到智能体中的插件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27475%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc1IiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

智能体无法正常调用插件如何解决？​

当智能体无法正常调用插件时，请参考如下步骤排查：​

1.

确认大模型是否支持调用插件。​

  * 在智能体中，大模型通过 Functioncall 能力调用插件或工作流，即你需判断所需的大模型是否支持 Functioncall 能力。​

2.

确认提示词是否合理，是否明确表达了调用插件的意图及时机。​

3.

对话里可正常提取插件的必选参数。​

为什么豆包·角色扮演·Pro模型无法调用插件？​

大模型通过 Functioncall 能力调用插件或工作流，而豆包·角色扮演·Pro模型暂不支持 Functioncall 能力。你可以使用豆包·工具调用模型，同时在提示词中明确描述插件调用场景。​

为什么插件提示未授权？​

OAuth 插件执行时需要通过 OAuth 方式获取用户授权，才能访问对应账号下的资源。在智能体或工作流节点中添加 OAuth 插件之后，智能体或工作流页面会提示未授权，你需要单击未授权，并根据页面提示完成授权，否则在当前页面调试智能体或试运行工作流时，插件会执行中断，引导你完成授权后才会继续执行。​

对于绑定了 OAuth 插件的智能体，每个用户调用插件时都需要使用各自的账号授权。工作流中的 OAuth 插件节点支持设置共享授权模式，智能体或工作流发布后，用户使用插件时默认使用开发者账号进行授权，无需用户手动授权。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27480%27%20height=%27271%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgwIiBoZWlnaHQ9IjI3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为什么无法添加扣子编程插件商店中的插件？​

如果在添加插件页面仅显示资源库工具和企业插件，未显示扣子编程插件商店中的插件，是因为企业超级管理员或管理员设置了仅允许使用企业商店中的插件，限制了对扣子编程插件商店的访问权限。​

如需使用扣子编程插件商店中的相关插件，可联系企业超级管理员或管理员将对应插件添加至企业插件商店中，具体请参见​添加扣子插件商店中的插件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27121.38728323699421%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjEyMS4zODcyODMyMzY5OTQyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

人设与回复逻辑

下一篇

工作流