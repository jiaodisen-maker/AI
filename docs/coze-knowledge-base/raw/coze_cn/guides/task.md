---
source_url: https://docs.coze.cn/guides/task
title: '触发器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:37Z
---

# 触发器 - 文档 - 扣子

触发器

你可以为低代码智能体添加触发器（Triggers），使得低代码智能体发布到飞书后，可以在特定时间或接收到特定事件时自动执行任务。​

注意

功能升级中，暂不支持为低代码智能体添加触发器。已添加的触发器不受影响，仍可使用。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27347%27%20height=%27353%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a597a1cb83b8431399b2c56e2236e783~tplv-goo7wpa0wc-quality:q75.image)​

​

什么是触发器​

触发器功能是智能体的预置任务，添加触发器后，智能体会在指定的时间和指定事件发生时自动执行任务。​

​

类别​| 说明​  
---|---  
触发方式​| 触发器根据触发方式，可以分为以下两种：​

  * 定时触发（Scheduled trigger）：让智能体在指定时间执行任务，无需编写任何代码。​

  * 事件触发（Event trigger）：当你的服务端向触发器指定的 Webhook URL 发送 HTTPS 请求时，自动执行任务。​

  
任务类型​| 触发器被触发后，可执行的任务类型包括：​

  * 智能体提示词：自动执行某个自然语言指令。选择该模式时，需要同时设置一条自然语言的指令，扣子编程会在指定时间把这条指令发送给智能体，智能体也会立即回复用户。例如设置触发时间 13:00，机器人提示为提醒我午休，智能体会在每天 13:00 主动发送一条消息提醒用户午休。​

  * 调用插件：自动调用某个插件，并将插件的返回结果发送给用户。例如添加一个查询天气的插件，定时向用户发送指定地点的天气信息。​

  * 调用工作流：自动调用某个工作流，并将工作流的返回结果发送给用户。例如可以添加一个审批工作流，当触发后执行工作流完成业务审批。​

  
设置方式​| 开发者和用户都可以为智能体设置触发器，其区别如下：​

  * 开发者设置：开发者在编排智能体时可创建各种类型的触发器，此触发器在所有支持触发器的发布渠道均生效，提示所有用户。​

  * 用户设置：用户在和智能体对话时可以设置定时任务。智能体会根据用户的 IP 地址判断其所在时区，并基于时区与用户指定的时间执行某个指令。例如每天早上八点推送新闻。​

  
  
​

使用限制​

  * 开发者在每个智能体中最多可添加 10 个触发器，用户侧设置的定时任务不计入触发器数量。​

  * 触发器功能仅对飞书渠道生效，只有将智能体发布到飞书渠道，才可以自动执行触发器的任务。​

  * 触发器绑定的工作流或插件应在 1 分钟内运行完毕，且工作流应关闭流式输出功能，否则触发器可能不会按照预期的方式运行，例如不推送消息、推送的消息不完整。​

  * 为智能体或应用设置触发器后，其关联工作流中插件节点的授权操作以及问答节点、输入节点将运行异常。​

用户设置定时任务​

当开发者在智能体编排页面的触发器区域，开启允许用户在对话中创建定时任务开关后，用户在飞书平台与智能体进行对话时，可以输入自然语言来创建定时任务。例如发送一条消息 每天16:00推送新闻。​

触发器配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271649%27%20height=%27336.0521327014218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY0OSIgaGVpZ2h0PSIzMzYuMDUyMTMyNzAxNDIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

在飞书中与智能体对话​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27297%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk3IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

开发者添加触发器​

开发者在智能体编排页面的技能区域添加触发器并将智能体发布到飞书后，智能体将根据指定的时区和时间执行预设的定时任务。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27415%27%20height=%27195%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE1IiBoZWlnaHQ9IjE5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

定时触发器​

单击+图标，添加一个触发器，并在创建触发器对话框，完成以下配置。​

​

配置​| 说明​  
---|---  
名称​| 触发器名称。​  
触发器类型​| 选择定时触发。​  
触发时间​| 设置定时触发器的时区以及触发时间，智能体会在指定的时间执行指定的任务。支持设置固定时间和时间间隔，例如每天 13:00 执行任务、间隔 2 天执行任务等。​  
任务执行​| 设置触发后执行任务的方式。支持设置为：​

  * 机器人提示：执行某个指令。选择该模式时，需要同时设置一条自然语言的指令。​

  * 插件：执行某个插件。选择该模式时，需要同时单击右侧 + 图标，添加一个插件。​

  * 工作流：执行某个工作流。选择该模式时，需要同时单击右侧 + 图标，添加一个工作流。​

如果插件或工作流有输入参数，则需要设置参数值。​  
  
​

例如创建一个定时任务，每天8:00练习口语。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27302%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyIiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

事件触发器​

在智能体的编排页面的技能区域，为智能体添加一个事件触发类型的触发器。成功添加后，如果你的服务端向触发器指定的 Webhook URL 发送 HTTPS 请求时，智能体会自动执行任务。​

​

配置​| 说明​  
---|---  
名称​| 触发器名称。​  
触发器类型​| 选择事件触发。​  
模式​| 目前仅支持 Webhook 模式。在该模式下，你将获取到触发器的 Webhook URL，通过向 Webhook URL 发送 HTTPS 请求，可触发该触发器。​  
Bearer Token​| 请求校验令牌。你可以直接使用默认提供的 Token，也可以修改 Token 值。向 Webhook URL 发送 HTTPS 请求时，请求头必须包含该 Token，用于完成请求的安全校验。​  
请求参数​| 请求参数列表，单击右侧 + 图标即可添加参数。该参数列表为可选配置，用于关联触发器中插件或者工作流的请求参数，后续向 Webhook URL 发送请求时，需要以 JSON 格式传入参数值。​  
任务执行​| 设置触发后执行任务的方式。支持选择：​

  * 机器人提示：该方式需要通过自然语言设置提示词。​

  * 插件或工作流：这两种方式需要你单击右侧 + 图标，添加插件或工作流（仅可添加一个）。如果插件或工作流有输入参数，则需要设置参数值。参数值可以在触发器内直接设置；也可以关联 Webhook 的请求参数列表，后续在发送 HTTPS 请求时传入参数值。​

  
  
​

示例如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27387%27%20height=%27374%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg3IiBoZWlnaHQ9IjM3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行触发器​

在开发调试阶段，你可以在智能体编排页面的预览与调试区域，单击技能 > 触发器，运行某一事件触发器，进行调试。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271844%27%20height=%27466.0659340659341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg0NCIgaGVpZ2h0PSI0NjYuMDY1OTM0MDY1OTM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

当智能体发布后，则需要向触发器的 Webhook URL 发送 HTTPS POST 请求，触发任务执行。​

以 cURL 构成的 HTTPS 请求为例，格式如下：​

​

Bash

复制

curl --location --request POST '<Trigger Webhook URL>' \​

\--header 'Authorization: Bearer <Trigger Bearer Token>' \​

\--header 'Content-Type: application/json' \​

\--data '<Trigger Parameters>'​

​

  * curl：命令行工具，支持通过 HTTP、HTTPS、FTP 等多种协议发送请求或接收数据。​

  * \--request POST '<Trigger Webhook URL>'：定义当前请求为 HTTPS POST 请求，其中 <Trigger Webhook URL> 为占位符，你需要替换为触发器真实的 Webhook 地址（可在智能体的事件触发器详情页复制 URL）。​

  * \--header 'Authorization: Bearer <Trigger Bearer Token>'：请求头参数，通过 Authorization 完成请求校验来确保安全性，其中 <Trigger Bearer Token> 为占位符，你需要替换为触发器真实的 Bearer Token。​

  * \--header 'Content-Type: application/json'：固定取值，用于定义消息体类型为 JSON。​

  * \--data '<Trigger Parameters>'：HTTPS POST 请求包含的数据内容。如果触发器内的插件或工作流需要输入参数，则需要将 <Trigger Parameters> 占位符替换为 JSON 格式的请求参数体。​

示例如下：​

​

Bash

复制

curl --location 'https://api.xxxx/api/xxxx' \​

\--header 'Authorization: Bearer ABCxxxxx' \​

\--header 'Content-Type: application/json' \​

\--data '{​

"url": "www.example.com"​

}'​

​

发送请求后，响应结果包含的 BaseResp 中的 StatusCode 为 0 表示请求成功。如果 StatusCode 不为 0，你可以通过 HttpCallBackRespDatas 获取错误信息，并根据错误信息作出相应调整。​

​

上一篇

工作流

下一篇

卡片