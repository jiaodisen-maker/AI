---
source_url: https://docs.coze.cn/guides/vibe_coding_miniapp
title: '开发小程序 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:10Z
---

# 开发小程序 - 文档 - 扣子

开发小程序

扣子编程现已支持自然语言开发微信小程序。在扣子编程首页输入你的创意，从零开始开发你的微信小程序，并一键部署上线。​

功能概述​

扣子编程提供了一个基于 Web 的 AI 编程开发环境，你可以直接在网页中与扣子 AI 对话，描述你想要开发的小程序的功能、界面、逻辑等需求，扣子 AI 会自动完成小程序的开发、测试、迭代和发布。​

说明

目前仅支持开发微信小程序。​

​

费用说明​

开发、测试、线上使用小程序时，以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：调用大语言模型、联网搜索、图像生成等内置集成服务。​

配额与限制​

开发小程序时，存在可创建的项目数量、可回滚版本数、可部署的次数等配额限制，详细说明，请参考​配额与限制。​

开发小程序​

参考以下流程，通过 AI 编程开发小程序。​

准备工作​

在开始开发之前，你需要在微信公众平台完成小程序的注册和基础配置。​

  * 注册小程序：前往 [微信公众平台](<https://mp.weixin.qq.com/>)，按照官方[小程序注册指引](<https://developers.weixin.qq.com/miniprogram/introduction/#小程序注册>)完成小程序账号的注册。​

  * 获取 AppID：在[微信公众平台](<https://mp.weixin.qq.com/>)左侧导航栏单击管理 > 开发管理，在开发设置页签的开发者 ID 区域找到并复制 AppID。这是小程序的唯一标识，后续步骤将会用到。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkzIiBoZWlnaHQ9IjE2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤一：需求澄清​

1.

创建小程序并输入你的需求。​

a.

在扣子编程首页，单击小程序选项卡。​

b.

在文本框输入你的提示词。​

  * 你需要尽可能清晰且详细地描述小程序的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：​

  * ​

Plain Text

复制

帮我制作一个小程序，用于学习普通话情景对话​

1\. 模型随机生成并展示 3 个不同主题，例如买菜、问路、面试等，用户进入页面时，选择一个主题，模型根据主题生成一段对话数据，并展示给用户​

2\. 类似聊天气泡的布局展示对话，每个汉字上方标注拼音，点击气泡可以朗读语句，整体有个录音按钮，用户可以跟读并录音，跟读完听回放​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27544%27%20height=%27198%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ0IiBoZWlnaHQ9IjE5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

（可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让扣子 AI 生成的结果更精准、更符合你的预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27403%27%20height=%27166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAzIiBoZWlnaHQ9IjE2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ① 上传附件

② 选择协作模式

③ 调用技能

④ 选择编程模型

酌情上传一些图片或文件，作为附加信息提供给扣子 AI，以便扣子 AI 能更理解你的需求。例如上传一张你想参考的界面截图、想要的风格示例图片等，这些都能帮助扣子 AI 更精准地把握细节要求。 ​

​

d.

在键盘中敲击回车，开始开发你的项目。​

  * 扣子 AI 会根据你输入的提示词来开始设计小程序、创建项目，并自动为项目设置小程序名称。​

2.

（可选）澄清你的需求。​

  * 扣子 AI 收到你的提示词之后，如果判断提示词不明确、缺失关键信息，不足以支撑 AI 生成合适的 PRD 和产品原型，则会向你发送提示，请求补充缺失的关键信息。​

  * 澄清需求时，你同样可以上传附件，为扣子 AI 提供更丰富的信息。 ​

步骤二：AI 编程开发小程序​

扣子 AI 收到你的需求之后，将立即启动需求分析，并规划开发流程和步骤，逐步生成小程序的前后端代码。代码生成完毕后，自动构建并启动服务，以提供一个可视化的界面供你预览。​

如果扣子 AI 判断你的小程序需要数据库、存储、身份认证、AI 等能力，则会自动添加和配置对应的集成，为你的小程序设计数据库表、配置存储系统，实现相关功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27341%27%20height=%27430%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQxIiBoZWlnaHQ9IjQzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：预览与测试​

初步生成后端代码后，扣子 AI 会自动生成测试用例并完成一轮单元测试。测试通过后扣子 AI 会提供后端代码的预览，同时提醒你对后端开发部分进行验收，你可以在右侧预览页面查看后端功能的实际运行效果。 ​

说明

录音等部分功能仅在小程序真机调试时可用，建议配置 AppID 之后通过微信扫码预览真机效果。​

​

小程序预览界面如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27663%27%20height=%27385%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYzIiBoZWlnaHQ9IjM4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为了体验小程序在手机上的效果，建议参考以下流程真机调试小程序。​

1\. 绑定微信小程序​

a.

在扣子编程打开小程序项目，在页面右下角单击 AppID 设置。​

  * ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27372%27%20height=%27305%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzcyIiBoZWlnaHQ9IjMwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

在弹出页面中填写 AppID，并单击绑定。​

  * AppID 是你在​准备工作中获取的 AppID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27226%27%20height=%27377%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI2IiBoZWlnaHQ9IjM3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

完成公众平台账号授权。​

  * 单击绑定后，系统默认打开授权页面，使用小程序的管理员微信号扫描授权二维码，并根据页面提示完成授权。​

  * ​

1.管理员扫描二维码​| 2.选择账号​| 3.授权确认​| 4.授权成功​  
---|---|---|---  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27186%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg2IiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27185%27%20height=%27401%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg1IiBoZWlnaHQ9IjQwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27187%27%20height=%27405%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg3IiBoZWlnaHQ9IjQwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27197%27%20height=%27427%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk3IiBoZWlnaHQ9IjQyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

2\. 真机调试小程序​

成功绑定小程序之后，就可以使用管理员微信号扫描页面右侧的二维码，在手机上调试小程序。​

调试方式如下：​

​

操作​| 说明​| 示例​  
---|---|---  
预览小程序​| 使用管理员微信号，在预览页面右下角扫描二维码，即可在手机上预览你的小程序。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271117%27%20height=%27941.1759259259259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTExNyIgaGVpZ2h0PSI5NDEuMTc1OTI1OTI1OTI1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
全面测试​| 全面测试你的小程序，通常建议关注以下问题：​

  * 功能是否可用：验证小程序的核心链路是否完整可操作、数据的增删改查是否能成功执行。​

  * 交互是否完善：检查页面元素是否完整显示、布局是否合理、样式是否符合设计要求、各个按钮是否都能正确触发。 ​

  * AI 能力是否正常：如果你的小程序集成了 AI 能力，例如文本生成、图片生成等，验证 AI 模型的输出是否符合预期。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27120%27%20height=%27260%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwIiBoZWlnaHQ9IjI2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
修复故障​| 如果页面报错，扣子 AI 会自动识别并提示你修复故障，你可以根据页面提示，单击一键修复，允许扣子 AI 尝试修复这些问题。​如果你在体验小程序的过程中触发页面报错，或者页面交互、生成结果不符合你的预期，你也可以主动复制报错信息、描述预期的结果，并粘贴到左侧输入框中，要求扣子 AI 修复故障。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271324%27%20height=%271048.1666666666665%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyNCIgaGVpZ2h0PSIxMDQ4LjE2NjY2NjY2NjY2NjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

迭代小程序​

修复问题和故障之后，这个小程序的雏形就基本搭建完成了，你可以选择直接部署，以供其他微信用户使用。但是通常情况下，这些小程序在功能或交互上仍有可改进之处，此时你可以通过自然语言或编写代码的方式，和扣子 AI 一起迭代你的小程序。​

调整需求​

如果之前某次对话中你输入的描述有误或不准确，导致扣子 AI 生成的小程序无法满足你的需求，相对于回滚版本再重新对话生成小程序，直接修改你发送的历史消息会更加高效。你可以在对话记录中找到该历史消息，对其进行修改后敲击回车，扣子 AI 会根据新的描述对小程序进行调整和优化。同时扣子 AI 的版本记录里也会另起一个分支来记录本次及后续的变更。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27478%27%20height=%27471%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc4IiBoZWlnaHQ9IjQ3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

编辑小程序​

和扣子 AI 一起持续优化小程序，直到实现预期的效果。你可以在对话区中通过自然语言描述你的修改建议，和扣子 AI 一起优化你的小程序。例如输入以下提示词：​

​

Plain Text

复制

增加一个返回首页的按钮​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27735%27%20height=%27505%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzM1IiBoZWlnaHQ9IjUwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

回滚开发版本​

扣子 AI 使用当前的先进模型来完成任务，但由于模型生成代码的随机性，有时可能无法完全满足你的需求，生成了不符合预期的代码，或者出现了反复修复失败的故障，此时你可以使用回滚版本功能，将小程序恢复到之前正常的版本状态。​

在对话区顶部单击版本历史图标，找到要恢复的版本，在其右侧单击回滚图标。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27541%27%20height=%27398%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQxIiBoZWlnaHQ9IjM5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

集成能力​

扣子编程通过技能方式封装了一批常见的集成能力接口，方便你快速为小程序添加各种功能，例如数据库、存储、AI 能力等，使小程序更好地满足多样化的业务需求。​

在和扣子 AI 对话，添加集成能力之前，你需要先在扣子 AI 对话区域单击技能，确认扣子 AI 已添加了你想要的技能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27439%27%20height=%27318%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM5IiBoZWlnaHQ9IjMxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

存储与数据库​

扣子编程提供了结构化数据托管方案，对于需要集成数据库和存储能力的小程序，扣子 AI 会根据任务要求自动集成并设置数据库能力和存储能力。例如开发一个电商小程序，扣子 AI 会自动集成数据库来管理商品信息、订单数据等，同时设置存储能力以存储商品图片、用户上传的评价图片等。 ​

你也可以在对话区发送自然语言指令，为小程序集成存储或数据库能力。例如：​

​

Plain Text

复制

使用数据库记录用户登录、浏览和购买行为数据​

​

关于存储和数据库集成的详细说明，可参考​集成数据库能力、​集成对象存储能力。​

AI 能力​

为小程序添加 AI 能力时，通常需要开通模型服务并获取 API 密钥、并自行完成模型调用的配置与开发。扣子编程托管了业界先进的各种模型服务，无需任何配置，扣子 AI 会自动为你的小程序添加 AI 能力，帮助你开发更为智能的小程序程序。例如，搭建一个多语言翻译的小程序，通过大模型翻译将用户的输入翻译为指定的语言，提供高效、低成本的翻译服务。​

默认情况下，你的项目已开通了大模型集成的权限，扣子编程会在收到指令后，自动为小程序添加 AI 功能。你也可以在对话区发送自然语言指令，让扣子 AI 集成大模型能力。例如：​

​

Plain Text

复制

使用豆包模型总结检索到的资讯，并整理为资讯日报​

​

关于大模型集成详细说明，可参考​内置集成。​

后续操作​

部署小程序​

完成小程序的开发与测试之后，你需要在微信开放平台完成小程序的配置和备案，然后在页面右上角单击部署，将扣子编程搭建的小程序部署成为一个公开可访问的微信小程序，将你的创意和原型，转化为服务于真实用户的产品。详细操作步骤可参考​部署小程序。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271639%27%20height=%27597.4292565947243%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYzOSIgaGVpZ2h0PSI1OTcuNDI5MjU2NTk0NzI0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27506%27%20height=%27362%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA2IiBoZWlnaHQ9IjM2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

分享项目​

部署完成，微信平台审核通过之后，你的用户可在微信中根据小程序名称搜索并使用这个小程序。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271146%27%20height=%27480.9352517985611%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE0NiIgaGVpZ2h0PSI0ODAuOTM1MjUxNzk4NTYxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27168%27%20height=%27236%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY4IiBoZWlnaHQ9IjIzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

查看线上日志​

查看已发布的小程序、智能体和工作流的前后端运行日志，以便在出现问题时进行故障排查和分析。详细说明可参考​查看日志和 Trace。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27675%27%20height=%27398%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc1IiBoZWlnaHQ9IjM5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

下架小程序​

如果要下架小程序，需要在微信开放平台解除扣子编程的绑定关系，然后暂停小程序服务。操作步骤如下：​

1.

管理员登录微信开放平台，解除绑定关系。​

a.

在页面左下角单击头像，单击账号设置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27320%27%20height=%27184%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIwIiBoZWlnaHQ9IjE4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

单击第三方设置页签。​

c.

找到扣子编程，并在操作列单击解除授权，根据页面提示完成后续操作。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI2IiBoZWlnaHQ9IjIwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

暂停小程序服务。​

a.

进入设置 > 基本设置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27329%27%20height=%27225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI5IiBoZWlnaHQ9IjIyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

在账号信息区域单击暂停服务按钮。​

c.

选择暂停原因和预计恢复时间，单击确定关闭。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27421%27%20height=%27266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIxIiBoZWlnaHQ9IjI2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

开发移动应用

下一篇

开发智能体