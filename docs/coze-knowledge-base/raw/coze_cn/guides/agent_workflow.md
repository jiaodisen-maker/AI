---
source_url: https://docs.coze.cn/guides/agent_workflow
title: '工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:34Z
---

# 工作流 - 文档 - 扣子

工作流

低代码工作流支持通过可视化的方式，对插件、大语言模型、代码块等功能进行组合，从而实现复杂、稳定的业务流程编排，例如旅行规划、报告分析等。当目标任务场景包含较多的步骤，且对输出结果的准确性、格式有严格要求时，适合配置工作流来实现。​

关于低代码工作流的详细介绍，请参考​低代码工作流介绍。​

添加低代码工作流​

为低代码智能体添加低代码工作流，并在提示词中引用工作流的名称来调用工作流，智能体会按照工作流编排的流程来响应用户需求。工作流开始节点通常设置了输入参数，用户和智能体对话时的用户提示词（Query）中必须包含开始节点的必选参数，否则工作流可能不会按预期执行。​

用户通过与智能体的对话输入指令或问题，智能体首先会解析这些输入内容。例如，用户在对话框中输入“查询北京的天气”，智能体会将这段文本解析为工作流的输入参数，作为工作流的初始输入传递到开始节点。工作流的开始节点会根据预设的逻辑，将数据传递到后续节点。​

前提条件​

在工作空间资源库中，已经创建了工作流，且工作流的状态为已发布，详情请参见​步骤一：创建工作流。​

操作步骤​

参考以下操作，为智能体添加资源库中的工作流：​

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

在智能体编排页面的工作流区域，单击右侧的加号图标。​

6.

在添加工作流对话框，选择目标工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271420%27%20height=%27397.86635404454864%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c54ded8d7e774598b129a8cb8f43a5f9~tplv-goo7wpa0wc-quality:q75.image)​

​

7.

在智能体的人设与回复逻辑区域，引用工作流的名称来调用工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271567%27%20height=%27372.92028135990626%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU2NyIgaGVpZ2h0PSIzNzIuOTIwMjgxMzU5OTA2MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

设置异步运行​

注意

功能升级中，暂不支持新建的智能体设置异步运行。​

​

工作流默认为同步运行，即智能体必须在工作流运行完毕后才会将工作流的输出传递给智能体用户。如果工作流复杂，或包含一些运行耗时长的节点，可能会导致工作流整体运行耗时长、智能体判断工作流运行超时，并在其运行完毕前就结束对话。例如包含图像流节点、多个大模型节点，或编排逻辑复杂的工作流节点。​

说明

  * 如果工作流或节点运行超时，智能体可能无法提供符合预期的回复。各场景的超时时间说明如下：​

  * 未开启工作流异步运行：​

  * 工作流整体超时时间为 10 分钟，数据库等部分节点的超时时间为 1分钟，具体请参见​低代码工作流使用限制。​

  * 用户问题和智能体回复的时间间隔最长为 2 分钟，如果智能体回复耗时 2 分钟以上，智能体可能会判断工作流超时。如果工作流运行耗时大于 2 分钟，建议添加输出节点用于输出中间消息，或者结束节点开启流式输出，保持对话状态。​

  * 开启工作流异步运行后：工作流整体超时时间为 24 小时，模型节点等部分节点为 10 分钟，数据库节点等部分节点为 1 分钟，具体请参见​低代码工作流使用限制。​

  * 工作流异步运行，仅在调试智能体或与商店中的智能体对话时生效，飞书、豆包等渠道暂不支持工作流异步运行。 ​

  * 工作流开启异步运行后，模型节点无法查看智能体对话历史。​

​

在这种场景下，你可以设置工作流为异步运行，设置后，智能体对话不依赖工作流的运行结果。工作流异步运行时会默认返回一条预设的回复内容，用户可以继续与智能体对话，工作流运行完毕后智能体会针对触发工作流的指令做出最终回复。​

操作步骤​

参考以下操作，为工作流开启异步运行：​

1.

在指定工作流右侧单击设置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27398%27%20height=%2790%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk4IiBoZWlnaHQ9IjkwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

开启异步运行，并设置回复内容。​

  * 回复内容是工作流在异步运行时，智能体回复用户的默认文案。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27398%27%20height=%27129%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk4IiBoZWlnaHQ9IjEyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

异步运行效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI0IiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

绑定卡片数据​

添加到智能体的工作流支持绑定消息卡片。绑定成功后，智能体以消息卡片的形式发送消息。​

注意

目前，消息卡片仅在豆包客户端、飞书客户端内生效。​

​

操作步骤​

参考以下操作，为智能体中的工作流绑定消息卡片：​

1.

在指定工作流右侧，单击绑定卡片数据图标，并单击绑定卡片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27664%27%20height=%27150%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjY0IiBoZWlnaHQ9IjE1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在智能体回复卡片配置对话框，选择扣子提供的官方卡片，或创建自定义卡片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27622%27%20height=%27324%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjIyIiBoZWlnaHQ9IjMyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

配置消息卡片后，卡片图标将会显示绿点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27449%27%20height=%27122%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ5IiBoZWlnaHQ9IjEyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

发布智能体，使配置生效。​

移除低代码工作流​

你可以为智能体移除一个不需要的工作流。移除后，智能体将不会按照该工作流编排的流程执行任务。​

在指定工作流右侧，单击移除图标，即可移除添加到智能体中的工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27379%27%20height=%27232%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5IiBoZWlnaHQ9IjIzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

插件

下一篇

触发器