---
source_url: https://docs.coze.cn/tutorial/0_code_wechat_customer_service
title: '0 代码搭建微信智能客服 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:48Z
---

# 0 代码搭建微信智能客服 - 文档 - 扣子

0 代码搭建微信智能客服

在扣子编程中搭建的客服智能体可以一键发布到微信公众号，作为公众号客服向订阅用户提供智能问答服务。本文档介绍扣子低代码智能体接入微信公众号的详细操作步骤。​

场景说明​

微信公众号是产品运营的重要信息传播与互动平台，内容创作者和媒体机构可以在微信公众号中向订阅用户群发消息，用于内容传播和粉丝运营，是自媒体、新闻媒体、知识分享等领域的重要运营渠道。基于微信公众号庞大的粉丝量，人工客服往往难以及时响应订阅用户的咨询与答疑。​

基于扣子编程搭建的低代码智能体可以一键发布到微信公众号，作为公众号客服实时响应订阅用户的消息，快速解答常见问题。例如电商行业解答产品咨询、处理售后服务；教育行业提供课程咨询、学习资料查询等等。​

本教程将以扣子编程的客服小助手为例，详细演示在扣子编程中搭建低代码智能体并发布为微信公众号客服的详细操作步骤。智能客服具备以下能力：​

  * 产品答疑：解答使用扣子编程过程中遇到的咨询与疑问，帮助用户排查故障。​

  * 视觉理解：查看用户发送的图片，基于图片内容回复用户咨询，例如识别用户发送的扣子编程报错信息，并提供对应的处理方式。​

准备工作​

  * 已成功申请一个微信公众号，且公众号状态正常。​

  * 获取公众号开发者 ID。​

  * 访问[微信公众平台](<https://mp.weixin.qq.com/>)并登录你的订阅号。在设置与开发 > 开发接口管理 > 基本配置页面，获取开发者ID(AppID)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27189%27%20height=%27170%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cb4dd991fc87488bb7b4776242628eeb~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤一：搭建低代码智能体​

本教程将以扣子编程的客服小助手为例。我们需要先搭建一个低代码智能体，并为其上传扣子知识库，并设置开场白与提示词。​

1 创建低代码智能体​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

3.

在低代码模式区域，单击智能体开发。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27446%27%20height=%27246%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ2IiBoZWlnaHQ9IjI0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

4.

根据页面提示设置智能体名称、头像。设置之后自动进入智能体编排页面。​

2 设置人设与回复逻辑​

用于定义智能体的人设和回复风格，帮助智能体生成符合当前场景与指定风格的回复。在本教程中，我们需要为客服智能体设置一个扣子编程的客服人设，并规定它的回复风格与范围。​

你可以手动设置人设与回复逻辑，也可以直接选择 AI 生成，或者参考扣子编程提供的提示词模板。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271010%27%20height=%27253.3859649122807%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAxMCIgaGVpZ2h0PSIyNTMuMzg1OTY0OTEyMjgwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置后：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27506%27%20height=%27370%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA2IiBoZWlnaHQ9IjM3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3 选择模型​

在扣子编程中，智能体是基于模型技术开发的应用程序。搭建智能体时，系统已预设默认模型，你也可以根据模型能力和业务场景灵活切换，利用更匹配的模型能力来调度技能与知识，从而更精准地响应用户问题。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27661%27%20height=%27156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYxIiBoZWlnaHQ9IjE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4 添加插件​

插件用于扩展智能体的功能，使其能够执行特定任务，如搜索、文件处理、日程管理等，增强智能体的实用性。​

在本教程中，我们需要为客服智能体添加搜索插件和图片理解插件。​

  * 搜索插件：智能体知识库中未命中的问题，尝试联网搜索、生成回复。​

  * 图片理解：对于不支持视觉理解的模型，需要借助图片理解插件来识别用户发送的图片内容。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271022%27%20height=%27453.6245614035088%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyMiIgaGVpZ2h0PSI0NTMuNjI0NTYxNDAzNTA4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5 上传知识库​

通过知识库为客服智能体添加私有知识。​

在本教程中，我们需要为客服智能体添加扣子编程的文档作为知识库，并上传日常沉淀的常见问题。所以需要创建并绑定以下两个知识库：​

  * 文档知识库：通过 URL 上传扣子编程的文档。​

  * 表格知识库：上传表格形式的常见问题文档。​

本教程以上传文档知识库为例，演示通过 URL 上传扣子编程文档中心作为扣子知识库的操作步骤：​

1.

在智能体编排页面的文本知识库区域单击添加图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27447%27%20height=%27126%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ3IiBoZWlnaHQ9IjEyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

单击创建知识库，选择创建扣子知识库，然后选择文本格式、在线数据，并单击创建并导入。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27447%27%20height=%27249%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ3IiBoZWlnaHQ9IjI0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择自动采集方式、批量添加，并填写扣子编程文档中心的根目录，根据页面提示完成上传。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27439%27%20height=%27224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM5IiBoZWlnaHQ9IjIyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6 设置开场白​

为客服智能体设置开场白文案，订阅用户访问公众号时，智能体会先送一段开场白文案，提升客服对话体验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27442%27%20height=%27218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQyIiBoZWlnaHQ9IjIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在本教程中，开场白文案可以设置为：​

​

Markdown

复制

你好，欢迎来到扣子 🎉​

​

扣子是新一代大模型 AI 应用开发平台。无论你是否有编程基础，都可以快速搭建出各种智能体，并一键发布到各大社交平台，或者轻松部署到自己的网站 🔗​

​

使用扣子过程中有任何问题请随时问我 ⚡️​

​

很高兴与你交流任何话题，欢迎随时来找我！​

​

7 调试低代码智能体​

在调试区与智能体对话，查看它的答疑效果。例如我们输入一段问题“你可以做什么？”或者“什么是扣子？”​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27494%27%20height=%27242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk0IiBoZWlnaHQ9IjI0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：将低代码智能体发布到微信客服​

1.

在扣子编程的智能体编排页面右上角，单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27479%27%20height=%27229%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc5IiBoZWlnaHQ9IjIyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在发布页面，找到微信公众号（订阅号）发布渠道，单击配置。​

  * 在 AppID 输入框内，填写微信订阅号的开发者 ID，并单击保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27479%27%20height=%27226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc5IiBoZWlnaHQ9IjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

跳转到公众平台账号授权页面，使用公众平台绑定的管理员个人微信号扫描二维码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27143%27%20height=%27187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQzIiBoZWlnaHQ9IjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在微信移动端，根据页面提示选择订阅号并确认授权。​

  * 授权成功的页面提示如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27138%27%20height=%27247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM4IiBoZWlnaHQ9IjI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

返回智能体发布页面，选中微信公众号（订阅号）发布平台，并设置发布记录后，单击页面右上角的发布。​

  * 成功发布后，你可以前往微信订阅号与智能体对话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27731%27%20height=%27180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzMxIiBoZWlnaHQ9IjE4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：在微信体验智能客服​

在发布页面单击立即对话，根据页面提示扫描二维码，即可和微信公众号的客服智能体展开对话。​

例如，我们可以咨询“什么是扣子编程？”，查看智能客服是否能够正常回复。​

​

上一篇

Openclaw 常见问题

下一篇

5 分钟快速接入 DeepSeek 模型