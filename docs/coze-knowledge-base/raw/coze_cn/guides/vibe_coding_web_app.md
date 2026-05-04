---
source_url: https://docs.coze.cn/guides/vibe_coding_web_app
title: '开发网页应用 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:04Z
---

# 开发网页应用 - 文档 - 扣子

开发网页应用

扣子编程是一款云端 AI 开发工具，帮助你将创意转化为应用。通过与扣子编程对话，你可以在浏览器页面中快速开发网页应用。无需编写代码、无需搭建开发环境，只需提出明确的开发需求即可从零开始完成应用的代码编写、部署上线。本文档介绍如何使用扣子编程开发网页应用。​

功能概述​

扣子编程提供了一个基于 Web 的 AI 编程开发环境，你可以直接在网页中与扣子 AI 对话，描述你想要开发的应用的功能、界面、逻辑等需求，扣子 AI 会自动完成应用的开发、测试、迭代和发布。目前，扣子编程支持开发网页类型的应用，包含完整前后端逻辑，例如产品落地页、业务系统、网页版互动游戏、资讯站点等。​

费用说明​

开发、测试、线上使用应用时，以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：调用大语言模型、联网搜索、图像生成等内置集成服务。​

配额与限制​

开发应用时，存在可创建的项目数量、可回滚版本数、可部署的次数等配额限制，详细说明，请参考​配额与限制。​

开发应用​

参考以下流程，通过 AI 编程开发网页应用。​

步骤一：需求澄清​

1.

创建应用并输入你的需求。​

a.

在扣子编程首页，单击网页应用选项卡。​

b.

在文本框输入你的提示词。​

  * 你需要尽可能清晰且详细地描述应用的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：​

  * ​

Plain Text

复制

我希望有个网站，我输入一个热点主题，它就会自动帮我检索10条当天的相关新闻热点，并且并行生成10张 比例 3:4 的4K 信息卡片，以图片的形式概述当天的热点新闻，我可以用来发布“每日信息差”主题的小红书新闻图片合集。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27468%27%20height=%27160%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY4IiBoZWlnaHQ9IjE2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

（可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让扣子 AI 生成的结果更精准、更符合你的预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27406%27%20height=%27165%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA2IiBoZWlnaHQ9IjE2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ① 上传附件

② 选择协作模式

③ 添加技能

④ 选择编程模型

酌情上传一些图片或文件，作为附加信息提供给扣子 AI，以便扣子 AI 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助扣子 AI 更精准地把握细节要求。 ​

​

d.

在键盘中敲击回车，开始开发你的项目。​

  * 扣子 AI 会根据你输入的提示词来开始设计应用、创建项目，并自动为项目设置应用名称。​

2.

（可选）澄清你的需求。​

  * 扣子 AI 收到你的提示词之后，如果判断提示词不明确、缺失关键信息，不足以支撑 AI 生成合适的 PRD 和产品原型，则会向你发送提示，请求补充缺失的关键信息。例如开发者要求“开发一个公司官网”，但未提供公司名称、行业、核心业务、品牌材料、参考风格等任何背景信息，扣子 AI 会主动追问相关细节。​

  * 澄清需求时，你同样可以上传附件，为扣子 AI 提供更丰富的信息。 ​

步骤二：AI 编程开发应用​

扣子 AI 收到你的需求之后，将立即启动需求分析，并规划开发流程和步骤，逐步生成应用的前后端代码。代码生成完毕后，自动构建并启动服务，以提供一个可视化的界面供你预览。​

如果扣子 AI 判断你的应用需要数据库、存储、身份认证、AI 等能力，则会自动添加和配置对应的集成，为你的应用设计数据库表、配置存储系统，实现相关功能​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27387%27%20height=%27536%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg3IiBoZWlnaHQ9IjUzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：预览与测试​

初步生成后端代码后，扣子 AI 会自动生成测试用例并完成一轮单元测试。测试通过后扣子 AI 会提供后端代码的预览，同时提醒你对后端开发部分进行验收，你可以在右侧预览页面查看后端功能的实际运行效果。 ​

网页应用预览界面如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271910%27%20height=%27815.7291666666666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMCIgaGVpZ2h0PSI4MTUuNzI5MTY2NjY2NjY2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在预览与测试的环节中，你可以通过以下操作预览并测试扣子 AI 为你生成的应用。​

​

操作​| 说明​| 示例​  
---|---|---  
预览应用​| 代码生成完毕后，系统会显示应用的预览页面。你也可以在右侧开启一个新的标签页，并单击预览以进入预览页面。​预览页面支持在新标签页中查看、刷新页面或重启应用，你可以在预览区域右上角单击对应的图标来执行这些操作。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271306%27%20height=%27646.9537037037037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMwNiIgaGVpZ2h0PSI2NDYuOTUzNzAzNzAzNzAzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
全面测试​| 在预览区全面测试你的应用，通常建议关注以下问题：​

  * 功能是否可用：验证应用的核心链路是否完整可操作、数据的增删改查是否能成功执行。​

  * 交互是否完善：检查页面元素是否完整显示、布局是否合理、样式是否符合设计要求、各个按钮是否都能正确触发。 ​

  * AI 能力是否正常：如果你的应用集成了 AI 能力，例如文本生成、图片生成等，验证 AI 模型的输出是否符合预期。​

| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271121%27%20height=%27482.6527777777778%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEyMSIgaGVpZ2h0PSI0ODIuNjUyNzc3Nzc3Nzc3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
修复故障​| 通常情况下，扣子 AI 会自动识别并提示你修复故障，你可以根据页面提示，单击一键修复，允许扣子 AI 尝试修复这些问题。​如果你在体验应用的过程中触发页面报错，但扣子 AI 没有提示你修复，你也可以主动复制报错信息并粘贴到对话中，将其发送给扣子 AI，要求它修复故障。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271911%27%20height=%27813.9444444444445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMSIgaGVpZ2h0PSI4MTMuOTQ0NDQ0NDQ0NDQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
  
​

迭代应用​

修复问题和故障之后，这个应用的雏形就基本搭建完成了，你可以选择直接将其部署为网页站点。但是通常情况下，这些应用在功能或交互上仍有可改进之处，此时你可以通过自然语言或编写代码的方式，和扣子 AI 一起迭代你的应用。​

调整需求​

如果之前某次对话中你输入的描述有误或不准确，导致扣子 AI 生成的应用无法满足你的需求，相对于回滚版本再重新对话生成应用，直接修改你发送的历史消息会更加高效。你可以在对话记录中找到该历史消息，对其进行修改后敲击回车，扣子 AI 会根据新的描述对应用进行调整和优化。同时扣子 AI 的版本记录里也会另起一个分支来记录本次及后续的变更。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27548%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ4IiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

编辑应用​

和扣子 AI 一起持续优化应用，直到实现预期的效果。你可以在对话区中通过自然语言描述你的修改建议，和扣子 AI 一起优化你的应用。例如输入以下提示词：​

​

Plain Text

复制

banner 的底图改成蓝色渐变​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27709%27%20height=%27299%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzA5IiBoZWlnaHQ9IjI5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调试代码​

扣子编程提供了一个基于 Web 的 AI 编程开发环境，你可以在代码编辑器中修改代码文件、在终端中执行命令调试代码，和扣子 AI 一起开始开发你的应用。关于 AI 编程开发环境的使用技巧，可参考​AI 编程环境。​

常见操作如下：​

​

操作​| 说明​| 示例​  
---|---|---  
通过扣子 AI 修改代码​| 在页面右上角单击文件树图标进入代码编辑器，找到你想修改的前端代码文件或代码片段，并单击引用到对话，然后通过自然语言描述你的修改建议。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271913%27%20height=%27814.7962962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMyIgaGVpZ2h0PSI4MTQuNzk2Mjk2Mjk2Mjk2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
手动编写代码​| 在页面右上角单击文件树图标进入代码编辑器，你可以在其中查看扣子 AI 生成的所有代码文件，并直接修改代码。​修改代码之后，需要重新构建才能预览项目。你可以在终端中执行命令，或者通过对话请扣子 AI 帮你构建、重启服务，以供预览项目。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271305%27%20height=%27863.9583333333334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMwNSIgaGVpZ2h0PSI4NjMuOTU4MzMzMzMzMzMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
调试代码​| 代码编辑器下方是 Web 终端，你可以通过终端执行常见的命令来调试并迭代你的应用，例如执行npm install安装项目依赖、python app.py启动后端服务等，与本地终端操作逻辑一致。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271911%27%20height=%27805.0972222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMSIgaGVpZ2h0PSI4MDUuMDk3MjIyMjIyMjIyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

回滚开发版本​

扣子 AI 使用当前的先进模型来完成任务，但由于模型生成代码的随机性，有时可能无法完全满足你的需求，生成了不符合预期的代码，或者出现了反复修复失败的故障，此时你可以使用回滚版本功能，将应用恢复到之前正常的版本状态。​

在对话区顶部单击版本历史图标，找到要恢复的版本，在其右侧单击回滚图标。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27234.22897196261684%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIzNC4yMjg5NzE5NjI2MTY4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

集成能力​

扣子编程通过技能方式封装了一批常见的集成能力接口，方便你快速为应用添加各种功能，例如数据库、存储、AI 能力等，使应用更好地满足多样化的业务需求。​

在和扣子 AI 对话，添加集成能力之前，你需要先在扣子 AI 对话区域单击技能，确认扣子 AI 已添加了你想要的技能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27422%27%20height=%27423%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIyIiBoZWlnaHQ9IjQyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

存储与数据库​

扣子编程提供了结构化数据托管方案，对于需要集成数据库和存储能力的应用，扣子 AI 会根据任务要求自动集成并设置数据库能力和存储能力。例如开发一个电商应用，扣子 AI 会自动集成数据库来管理商品信息、订单数据等，同时设置存储能力以存储商品图片、用户上传的评价图片等。 ​

你也可以在对话区发送自然语言指令，为应用集成存储或数据库能力。例如：​

​

Plain Text

复制

使用数据库记录用户登录、浏览和购买行为数据​

​

关于存储和数据库集成的详细说明，可参考​集成数据库能力、​集成对象存储能力。​

AI 能力​

为应用程序添加 AI 能力时，通常需要开通模型服务并获取 API 密钥、并自行完成模型调用的配置与开发。扣子编程托管了业界先进的各种模型服务，无需任何配置，扣子 AI 会自动为你的应用添加 AI 能力，帮助你开发更为智能的应用程序。例如，搭建一个多语言翻译的网页应用，通过大模型翻译将用户的输入翻译为指定的语言，提供高效、低成本的翻译服务。​

默认情况下，你的项目已开通了大模型集成的权限，扣子编程会在收到指令后，自动为应用添加 AI 功能。你也可以在对话区发送自然语言指令，让扣子 AI 集成大模型能力。例如：​

​

Plain Text

复制

使用豆包模型总结检索到的资讯，并整理为资讯日报​

​

关于大模型集成详细说明，可参考​内置集成。​

后续操作​

部署应用​

完成应用的开发与测试之后，你可以在页面右上角单击部署，将扣子编程搭建的应用部署成为一个公开可访问的在线项目，将你的创意和原型，转化为服务于真实用户的产品。详细操作步骤可参考​部署网页应用。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27748%27%20height=%27320%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQ4IiBoZWlnaHQ9IjMyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

分享项目​

在项目搭建页面右上角单击分享按钮，可以将部署成功的项目分享给他人。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271420%27%20height=%27359.93055555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQyMCIgaGVpZ2h0PSIzNTkuOTMwNTU1NTU1NTU1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看线上日志​

查看已发布的应用、智能体和工作流的前后端运行日志，以便在出现问题时进行故障排查和分析。详细说明可参考​查看日志和 Trace。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27462%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYyIiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

开发儿童绘本制作工具

下一篇

开发移动应用