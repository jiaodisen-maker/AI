---
source_url: https://docs.coze.cn/developer_guides/install_web_sdk
title: '安装并使用 Chat SDK - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:25:03Z
---

# 安装并使用 Chat SDK - 文档 - 扣子

安装并使用 Chat SDK

本文介绍如何安装并使用扣子 Chat SDK，开发者可以参考本文档在自己开发的网站或 App 中快速实现智能对话功能。适用于智能客服、答疑助手或企业内部的 IT 支持机器人等场景。​

前置条件​

浏览器兼容性​

Chat SDK 的运行环境要求如下表所示。​

​

浏览器​| 版本限制​  
---|---  
Chrome​|  87.0 及以上 ​  
Edge​|  88.0 及以上 ​  
Safari​|  14.0 及以上 ​  
Firefox​|  78.0 及以上 ​  
  
​

获取访问密钥​

访问密钥用于 Chat SDK 的身份认证与鉴权。根据使用场景选择合适的鉴权方式，各鉴权方式的区别请参见​鉴权方式概述。​

​

场景​| 推荐方案​| 说明​| 参考文档​  
---|---|---|---  
开发调试​| 个人访问令牌（PAT）​| 快速跑通 Chat SDK 的整体流程。​| ​添加个人访问令牌​  
生产环境​| 服务访问令牌（SAT）​| 操作更简单，能够有效简化授权流程，适合需要长期稳定访问且无需进行会话隔离的场景。​仅企业版（企业标准版、企业旗舰版）支持使用 SAT 鉴权。​| ​添加服务访问令牌​  
​| OAuth 鉴权​| 支持渠道用户访问智能体、会话隔离（即智能体不同账号的消息内容互相隔离）。​| ​OAuth 应用管理​​OAuth JWT 授权（渠道场景）​  
  
​

权限要求​

访问密钥需被授予以下权限，才能正常使用 Chat SDK 的各项能力。Chat SDK 所需的权限列表如下：​

​

密钥类型​| PAT / SAT /普通 OAuth​|  渠道 OAuth 访问密钥​  
---|---|---  
权限点​​| 

  * Bot管理​

  * chat​

  * getMetadata​

  * 会话管理​

  * listConversation​

  * createConversation​

  * editConversation​

  * 对话​

  * cancelChat​

  * 工作流​

  * getMetadata​

  * 应用管理​

  * getMetadata​

  * 文件​

  * uploadFile​

  * 消息​

  * listMessage​

  * 智能音视频​

  * createTranscription​

  * createSpeech​

| 

  * botChat​

  * getMetadata​

  * listConversation​

  * createConversation​

  * editConversation​

  * uploadFile​

  * listConversationMessage​

  * cancelConversationChat​

  * createTranscription​

  * createSpeech​

​  
  
​

说明

渠道 OAuth 访问密钥的权限点是渠道类型的 OAuth 应用中设置的权限点，创建应用并授权的详细说明可参考​OAuth JWT 授权（渠道场景）。​

​

调试与体验 Chat SDK​

你可以通过 [Playground](<https://www.coze.cn/open/playground/chatsdk>) 调试与体验 Chat SDK 各配置项的功能和效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27453.6416184971098%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ1My42NDE2MTg0OTcxMDk4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

配置流程​

步骤一：发布智能体或扣子应用​

在智能体或 AI 应用的发布页面，选择 Chat SDK，并单击发布。发布的详细流程可参考：​

  * ​发布为 Chat SDK​

  * ​发布到 Chat SDK​

步骤二：获取安装代码​

进入发布页面复制 SDK 安装代码。​

​

步骤三：安装 SDK​

将步骤二中复制的安装代码粘贴到网页中，例如 <body> 标签内，通过 script 标签加载 Chat SDK 的 js 代码。​

示例代码如下：​

​

​

步骤四：初始化配置​

通过调用 CozeWebSDK.WebChatClient 初始化客户端。当前页面中聊天框包括 PC 和移动端两种布局样式，在 PC 端中，聊天框位于页面右下角，移动端聊天框会铺满全屏。​

智能体配置​

调用 CozeWebSDK.WebChatClient 时，你需要配置 config（智能体信息）和 auth（鉴权信息）。​

  * config：必选参数，表示智能体的配置信息。​

  * 调用智能体时，需要设置以下参数： ​

  * ​

  * auth：表示鉴权方式。当未配置此参数时表示不鉴权。为了账号安全，建议配置鉴权。​

  * ​

初始化示例如下：​

​

​

扣子应用配置​

调用 CozeWebSDK.WebChatClient 时，你需要配置扣子应用的基础信息以及鉴权参数：​

  * config：必选参数，表示应用的配置信息。​

  * ​

  * auth：表示鉴权方式。当未配置此参数时表示不鉴权。为了账号安全，建议配置鉴权。​

  * ​

示例如下：​

​

步骤五：自定义聊天界面与交互​

开发者可以按需调整对话框的多种展示效果，例如展示的用户信息、对话框 UI 效果、悬浮球展示、底部文案等。​

你可以在 WebChatClient 方法中添加各种属性，实现对应的效果。目前支持的属性如下：​

​

步骤六：销毁客户端​

若需在页面卸载或特定场景下关闭 Chat SDK，可调用 destroy 方法销毁客户端，释放资源。​

​

自定义聊天界面与交互​

你可以配置对话框中的用户信息、布局、悬浮球、底部文案、顶部标题栏等 UI 元素，以满足品牌风格需求。​

配置用户信息​

userInfo 参数用于设置对话框中显示的用户信息，包括对话框中的用户头像和用户昵称。同时，此处指定的用户 ID 也会通过​发起对话 API 传递给扣子服务端。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27202.7027027027027%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMi43MDI3MDI3MDI3MDI3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

配置示例如下：​

​

基础 UI 配置​

ui.base 参数用于添加聊天窗口的整体 UI 效果，包括应用图标、页面布局、语言属性等。​

​

示例代码如下：​

​

悬浮球​

ui.asstBtn 参数用于控制是否在页面右下角展示悬浮球。默认展示，用户点击悬浮球后将弹出聊天窗口。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27431%27%20height=%27239%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDMxIiBoZWlnaHQ9IjIzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

示例代码如下：​

​

Chat SDK 悬浮球的位置默认在页面右下角，不支持移动，如果需要调整悬浮球的位置，你可以隐藏默认的悬浮球，自定义悬浮球的位置和样式，具体请参见​Chat SDK 悬浮球位置如何移动？。​

底部文案​

聊天框底部会展示对话服务的提供方信息，默认为Powered by coze. AI-generated content for reference only.。开发者通过 ui.footer 参数隐藏此文案或改为其他文案，支持在文案中设置超链接。​

底部文案默认展示效果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27462%27%20height=%27156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYyIiBoZWlnaHQ9IjE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

footer 参数配置说明如下：​

​

配置示例如下：​

​

此配置的对应的展示效果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27458%27%20height=%27169%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU4IiBoZWlnaHQ9IjE2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

顶部标题栏配置​

聊天框顶部默认展示智能体名称、icon 及关闭按钮。展示效果类似如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%2777.08779443254818%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9Ijc3LjA4Nzc5NDQzMjU0ODE4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

您可以通过 ui.header 参数配置是否展示顶部标题栏和关闭按钮，header 参数配置说明如下：​

​

配置示例如下：​

​

聊天框​

chatBot 参数用于控制聊天框的 UI 和基础能力，包括标题、大小、位置等基本属性，还可以指定是否支持在聊天框中上传文件。此参数同时提供多个回调方法，用于同步聊天框显示、隐藏等事件通知。​

配置说明如下：​

​

相关回调：​

  * onHide：当聊天框隐藏的时候，会回调该方法。​

  * onShow: 当聊天框显示的时候，会回调该方法。​

  * onBeforeShow: 聊天框显示前调用，如果返回了 false，则不会显示。支持异步函数。​

  * onBeforeHide:  聊天框隐藏前调用，如果返回了 false，则不会隐藏。支持异步函数。​

在以下示例中，聊天框标题为 Kids' Playmate | Snowy，并开启上传文件功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27477%27%20height=%27482%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc3IiBoZWlnaHQ9IjQ4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

对应的代码示例如下：​

​

通过 chatbot 的 el 参数设置组件的示例代码如下：​

​

消息评价​

你可以在 chatBot 参数中配置是否允许用户对智能体的回答进行评价（点赞 / 点踩），默认禁用评价功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27565.9722222222223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjU2NS45NzIyMjIyMjIyMjIzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

示例代码如下：​

​

会话列表​

ui.conversations 参数用于控制是否展示会话列表功能。开启后，聊天框左上角会新增一个会话列表按钮，用户可借此查看历史对话、重新发起对话、创建新的会话、重命名或删除会话，实现便捷的会话管理。​

​

​

示例代码如下：​

​

相关操作​

更新 SDK 版本​

扣子 Chat SDK 将持续更新迭代，支持丰富的对话能力和展示效果。你可以在 Chat SDK 的 script 标签中指定 Chat SDK 的最新版本号，体验和使用最新的 Chat SDK 对话效果。​

在以下代码中，将 {{version}} 部分替换为 Chat SDK 的最新版本号。你可以在​Chat SDK 发布历史中查看最新版本号。​

​

解绑 Chat SDK​

如果不再需要通过 Chat SDK 使用 AI 应用，可以在发布页面点击解绑按钮。一旦解绑，智能体或应用就无法通过集成的 Web 应用程序使用。 如果您想恢复 Web 应用程序的访问，需要再次将智能体或应用发布为 Chat SDK。 ​

​

完整示例代码​

以下是一段完整的 Chat SDK 调用智能体的代码示例。​

​

相关文档​

如果需要将不同业务侧用户的会话互相隔离开来，每个用户只能看到自己和智能体的对话历史，请参见​如何实现会话隔离。​

上一篇

Chat SDK 概述

下一篇

Chat SDK 发布历史