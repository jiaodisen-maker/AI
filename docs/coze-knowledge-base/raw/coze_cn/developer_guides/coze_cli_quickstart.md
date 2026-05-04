---
source_url: https://docs.coze.cn/developer_guides/coze_cli_quickstart
title: 'Coze CLI 最佳实践  - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:16:22Z
---

# Coze CLI 最佳实践  - 文档 - 扣子

Coze CLI 最佳实践 

本指南将引导你学习如何使用 Coze CLI，通过与 AI Agent 对话来完成各项任务。你将了解如何快速创建和上线 Web 应用、批量生成多媒体营销内容，以及进行企业级资源管理，从而将复杂的开发与内容创作流程简化为自然语言指令，显著提升工作效率。​

账号登录与授权​

Agent 调用 Coze CLI 时，需要使用你的扣子账号与权限操作，并将创建好的应用保存在你的账号下。所以使用 Coze CLI 创建应用之前，你的 Agent 会引导你先登录扣子账号，并完成授权。​

第一次和 Agent 一起使用 Coze CLI，你需要先完成授权。将以下内容发给你的 Agent，让它帮你完成登录：​

​

Plain Text

复制

使用 Coze CLI 帮我登录扣子账号​

​

Agent 会自动执行 Coze CLI 的登录命令，并返回给你一个授权链接和授权码，你需要：​

1.

访问授权链接，输入授权码。​

  * 注意授权码有效期 5 分钟，过期后需要重新生成授权链接。​

2.

完成授权。​

  * 个人版：默认授予此账号在个人版下所有空间的权限。​

  * 企业版：你需要选择授予哪些企业组织和工作空间的权限。​

3.

回到 Agent 对话中，告知它已完成授权。​

​

要求登录​| 确认授权码​| 完成授权​| 登录成功​  
---|---|---|---  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271564%27%20height=%27742%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/11b43f75e9b54ba08080d190b21bd3a2~tplv-goo7wpa0wc-quality:q75.image)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272662%27%20height=%271536%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fa5e9af5b0be404e98a5b81b066a383a~tplv-goo7wpa0wc-quality:q75.image)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272792%27%20height=%271516%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a557d1b5188f4489bc97f72c8335683a~tplv-goo7wpa0wc-quality:q75.image)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27121%27%20height=%27110%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4f9567b37629421796c8bfcf863cabe7~tplv-goo7wpa0wc-quality:q75.image)​​  
  
​

登录账号之后，你还可以：​

  * 查看登录状态：如果创建资源时报错无权限、找不到组织空间，可以查看登录状态，检查是否登录了错误账号。​

  * 刷新授权：Agent 通常会帮你定期刷新授权，保持登录状态。如果你意外掉线了，Agent 会重新生成授权链接，提示你重新登录。​

  * 退出登录：一般在切换账号、测试完后清理身份等场景下操作。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271582%27%20height=%27946%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU4MiIgaGVpZ2h0PSI5NDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看登录状态​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27373%27%20height=%27160%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzczIiBoZWlnaHQ9IjE2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

退出登录​

​

​

场景一：10 分钟完成 Web 应用从开发到上线​

以下步骤中，我们以快速搭建 Coze CLI 产品落地页为例，演示如何通过 Coze CLI 快速开发并上线一个 Web 应用。 这个应用需要：​

  * 灵活增删功能，及时根据用户反馈定向优化​

  * 可在线调试、AI 自动排障​

  * 一键部署，支持自定义品牌域名​

步骤一：创建应用​

Coze CLI 可调用扣子编程，通过自然语言创建 AI 编程项目。你无需下载编程 IDE、无需了解 React 等框架，只要清晰描述你的诉求， Agent 就能帮你生成应用程序，并自动编译测试，交付给你一个符合要求的应用。​

和你的 AI Agent 对话，提供内容素材和具体要求，让它直接帮你制作 Coze CLI 的产品落地页。例如：​

​

你的指令​| 对话过程​  
---|---  
​Plain Text复制使用 Coze CLI，帮我制作一个 Coze CLI 的落地页​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27316%27%20height=%27281%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE2IiBoZWlnaHQ9IjI4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

步骤二：预览应用​

下发任务之后，Agent 会自动监控任务进度，完成任务后调用 Coze CLI 生成一个在线预览的页面，供你查看和体验。你可以打开链接，简单测试应用的效果、查看应用的界面风格，验收成果。​

例如：​

​

对话过程​| 生成的落地页​  
---|---  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271560%27%20height=%271388%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU2MCIgaGVpZ2h0PSIxMzg4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27479%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc5IiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

步骤三：调试应用​

扣子编程通过编程 AI 对话来帮你创建应用、调试应用。通过自然语言，你可以直接在对话中调试代码逻辑、实时编译预览效果。让你的 Agent 调用 Coze CLI 来和编程 AI 对话，让它优化应用、排查并修复问题，即使你是编程新手也能快速迭代功能。​

通过 Coze CLI，你可以通过以下方式调试和修改应用：​

  * 添加功能：通过自然语言为应用添加新的功能，支持使用扣子编程内置的集成能力、外部集成能力，例如对象存储、邮件服务等。例如“帮我在网页里添加一个一键生成图片的能力，生成的图片保存在对象存储里”。​

  * 配置环境变量：敏感信息隔离，保障生产环境密钥安全，避免敏感信息泄露。例如“帮我把 API Key 配置成环境变量”。​

  * 问题修复：调试时遇到的问题都可以让 Agent 通过 Coze CLI 帮你修复，例如“快速开始这个按钮不响应，帮我修复一下”。​

例如，我们预览应用之后，发现需要在落地页中增加 Coze CLI 文档的链接，可以通过对话来添加。和你的 AI Agent 对话，让它直接操作：​

​

你的指令​| 对话过程​| 调试结果​  
---|---|---  
​Plain Text复制帮我在落地页里添加一个查看文档的按钮，文档链接：https://docs.coze.cn/developer_guides/coze_cli​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271424%27%20height=%27660%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQyNCIgaGVpZ2h0PSI2NjAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27232%27%20height=%27139%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMyIiBoZWlnaHQ9IjEzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

步骤四：部署到线上​

在线预览并体验这个落地页之后，确认页面展示效果和核心功能没有问题，就可以将页面部署到线上​

扣子编程创建的应用可一键部署到线上环境，扣子编程提供云端环境和域名服务，无需运维介入，即使编程新手也能把自己的应用公开发布到线上以供其他用户访问。​

​

你的指令​| 对话过程​  
---|---  
​Plain Text复制这个网页帮我部署到正式环境吧​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271444%27%20height=%271060%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ0NCIgaGVpZ2h0PSIxMDYwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

除了基础的部署功能之外，通过 Coze CLI，你还可以将项目部署到自定义域名，提升品牌专业性，支持 SSL 证书自动配置。例如“帮我配置一下自定义域名 test.com，把项目发到这个域名下。”注意需要提前申请并备案自定义域名。​

场景二：批量生成 AI 营销内容​

Coze CLI 支持通过扣子编程 AI 的官方集成能力，调用各类多模态模型，来生成图片、音频或者视频。​

以下步骤中，我们以批量生成 Coze CLI 的 AI 营销内容为例，演示如何通过 Coze CLI 生成多媒体图文，例如图片、视频、音频等。​

在这个场景中，我们需要为 Coze CLI 打造全渠道营销内容，要求：​

  * 每周产出 10 + 小红书笔记、5 期播客、3 条广告短片​

  * 内容风格统一，符合品牌调性，批量生成不耗时​

1 文生图：批量制作小红书信息图​

Coze CLI 可以调用扣子编程的官方集成能力，让你用自然语言就能生成专业级设计图，无需设计师，1 分钟出图。​

支持批量生成、风格定制，适配小红书、公众号等多平台尺寸；可直接导出高清图，用于笔记配图、海报设计，答复提升内容产出效率。​

和你的 AI Agent 对话，提供内容素材和具体要求，让它直接帮你制作小红书信息图。例如：​

​

你的指令​| 对话过程​| 调试结果​  
---|---|---  
​Plain Text复制帮我写一篇小红书笔记，主题是 Coze CLI 正式发布，要求图文并茂，图片是一张主图+一张信息图​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27173%27%20height=%27522%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTczIiBoZWlnaHQ9IjUyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271600%27%20height=%272848%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYwMCIgaGVpZ2h0PSIyODQ4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

2 文字转语音：快速制作产品介绍音频​

Coze CLI 可以批量生成播报音频、配音、有声内容、智能语音，支持数十种音色、多语言，适配不同内容风格（科普、种草、干货），直接上传到喜马拉雅、小宇宙等平台，打造音频内容矩阵。​

和你的 AI Agent 对话，提供内容素材和具体要求，让它直接帮你制作 Coze CLI 的介绍音频。例如：​

生成的音频：​

​

你的指令​| 对话过程​  
---|---  
​Plain Text复制这是 Coze CLI 的文档（https://docs.coze.cn/developer_guides/coze_cli），帮我用 Coze CLI 生成一段音频，介绍 Coze CLI 是什么、能做什么​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271404%27%20height=%27665.0526315789473%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQwNCIgaGVpZ2h0PSI2NjUuMDUyNjMxNTc4OTQ3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
  
​

3 文生视频：一键生成广告短片​

Coze CLI 可通过自然语言生成专业级短视频、图片动效视频、产品演示、营销短片，支持配置时长、参考图、分辨率、帧率、配音，适配不同平台的内容要求。可直接用于产品推广、流量投放，快速打造视频内容矩阵。​

和你的 AI Agent 对话，提供内容素材和具体要求，让它直接帮你制作 Coze CLI 的介绍短片。例如：​

​

你的指令​| 对话过程​  
---|---  
​Plain Text复制这是 Coze CLI 的文档（https://docs.coze.cn/developer_guides/coze_cli），帮我用 Coze CLI 生成一段视频，介绍 Coze CLI 是什么、能做什么​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271404%27%20height=%27665.0526315789473%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQwNCIgaGVpZ2h0PSI2NjUuMDUyNjMxNTc4OTQ3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
  
​

场景三：企业级资源管理​

Agent 在使用 Coze CLI 操作你的扣子账号时，默认使用你的个人版账号，在你的个人空间中创建项目。但是在企业生产场景下，往往需要：​

  * 统一团队组织架构，员工在各自组织和工作空间中操作。​

  * 设置默认的组织和空间，简化操作流程。​

  * 偶尔也需要忽略默认的组织和空间，在指定的空间创建项目。​

默认在个人账号操作​

登录 Coze CLI 后，Agent 默认拥有了你个人账号下所有工作空间的操作权限。后续创建应用、生成多媒体内容时，也会默认保存在你的个人空间中。​

例如：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27271%27%20height=%27273%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcxIiBoZWlnaHQ9IjI3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置默认组织和空间​

对于企业版用户，往往需要在企业版某个组织、某个工作空间中创建项目，以便企业统一管理员工权限和资源。使用 Coze CLI 时，Agent 可以帮你设置默认组织和工作空间，当你要求创建编程项目时无需和你确认项目保存位置，简化操作流程。​

和你的 AI Agent 对话，请它设置默认组织和空间。如果你不记得默认组织和工作空间的名称，可以先请 Agent 帮你查看组织和空间列表。​

​

你的指令​| 对话过程​  
---|---  
​Plain Text复制帮我使用 coze cli设置默认组织和空间，默认组织是“扣子文档”，默认空间是“ForMe”​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271280%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4MCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

在指定工作空间创建项目​

即使设置了默认的组织和工作空间，也偶尔需要切换到个人版或者切换到其他企业组织操作，尤其是企业外部访客可能需要在多个企业下来回切换。​

和你的 Agent 对话，在创建项目时使用指定的工作空间，精细管理资源。​

​

你的指令​| 对话过程​| 最终产物​  
---|---|---  
​Plain Text复制用 coze cli，根据你对我的理解，帮我创建一个个人主页，保存在我的个人版个人空间下面​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271402%27%20height=%271304%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQwMiIgaGVpZ2h0PSIxMzA0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272592%27%20height=%271458%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU5MiIgaGVpZ2h0PSIxNDU4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

​

上一篇

Coze CLI 介绍

下一篇

API 介绍