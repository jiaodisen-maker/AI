---
source_url: https://docs.coze.cn/guides/vibe_coding_overview
title: '扣子 AI 编程概述 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:29:47Z
---

# 扣子 AI 编程概述 - 文档 - 扣子

扣子 AI 编程概述

扣子编程是一个 AI 驱动的应用开发平台，提供基于 Web 的 AI 编程环境，帮助你通过自然语言创建并部署属于自己的开发项目。无论你是否有编程基础，只需要清晰描述你的需求，扣子编程就能为你开发智能体、工作流、网页应用、移动应用、技能或小程序等 AI 编程项目。​

核心特性​

  * 开箱即用的云端环境：打开网页即可开始，每个项目自动分配云端运行环境和对应资源，无需安装任何工具。遇到问题也能一键重启、自动恢复。​

  * 完善的集成与基础设施：扣子编程内置多种业界领先的优秀模型服务，适用于图文生成、视频生成等多种热门场景；提供数据库、存储、身份认证等各项基础服务；支持与第三方服务的集成，方便开发者快速构建功能丰富、性能稳定的应用程序。​

  * 一键部署和项目构建服务：一键完成云端打包、构建与服务部署，支持自定义域名。版本可回退，部署记录完善、可追踪。​

说明

开发、测试、线上使用 AI 编程项目时，以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：调用大语言模型、联网搜索、图像生成等内置集成服务。​

​

配额和限制​

主账号及其名下的成员均被视为独立的扣子用户，享有独立的配额。​

​

限制项​| ​| 说明​  
---|---|---  
上传文件​| ​| 

  * 在对话区上传文件时，单个文件大小限制 20 MB， 每个项目最多上传 20 个文件。​

  * 上传的文件类型无限制。​

  
多人协作​| ​| 通过扣子 AI 编程创建的项目暂不支持多人协作。项目创建者以外的工作空间成员仅可查看项目，例如查看对话过程、历史版本、代码文件等；不可操作项目，例如修改、部署等。​  
编程环境​| 沙箱存储配额​| 在扣子 AI 编程项目中，云端沙箱磁盘使用量上限为 10GB，达到上限时项目将终止运行。项目中已生成的代码、已安装的依赖、上传到 assets 目录的文件等内容都会占用沙箱磁盘。​  
​| 沙箱空闲回收​| 在扣子 AI 编程项目中，云端沙箱存在空闲回收机制。如果项目在 1 小时内没有任何操作（例如编辑代码、访问项目页面等），系统会自动中断沙箱连接。你可以根据页面提示重新连接沙箱。​  
​| 沙箱预览数量​| 每个用户最多同时打开 10 个项目的预览页面，否则页面会提示“正在运行中的任务数已达上限”。​  
  
​

开发环境与工具​

扣子编程提供了一个基于 Web 的 AI 编程开发环境，它以浏览器为载体，自带编码所需的基础功能，提供了开箱即用的编程体验。扣子 AI 编程环境无需本地安装软件和依赖，让 AI 承担编码、调试等繁琐工作，开发者只需通过自然语言描述需求、验收成果，极大降低了编程门槛。​

AI 编程环境的核心工具如下：​

  * 代码编辑器：内置支持多种编程语言的代码编辑器，提供语法高亮、代码格式化等功能。​

  * Web 终端：模拟 Linux 终端，可执行 npm、python等命令。​

  * 云端沙箱：为每个项目创建互相隔离的云端沙箱，包含了运行代码所需的操作系统、依赖和资源，支持实时预览网页、应用效果。​

  * AI 驱动：AI 深度嵌入开发全流程，支持自然语言生成代码，生成代码后能即时运行并展示效果；提供代码生成、代码补全、智能纠错等 AI 编程能力，能自主完成复杂的开发任务。​

开发流程​

参考以下流程，快速使用扣子编程搭建你的第一个编程项目：​

1.

输入你的需求。​

  * 在扣子编程首页文本框中直接输入你的创意。建议尽可能清晰且详细地描述应用的功能、界面设计、业务逻辑等方面的要求，以便扣子 AI 生成更符合需求的应用。​

  * 例如：​

  * ​

Plain Text

复制

我希望开发一个给儿童的绘本生成网站，用户输入一个主题，自动生成一个绘本脚本，然后根据绘本脚本内容，生成最高10张画面连续的绘本内容。要求必须使用seedream 4.5 的 sequential image generation 模式，以实现连续的画风。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27335%27%20height=%27197%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM1IiBoZWlnaHQ9IjE5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

预览与调试。​

  * 扣子 AI 收到你的需求之后，将立即启动需求分析，并规划开发流程和步骤，逐步生成应用的前后端代码。代码生成完毕后，自动构建并启动服务。你可以在右侧预览页签中体验项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27605%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA1IiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

改进项目。​

  * 在对话区与扣子 AI 交互，它会帮你集成各项扣子编程的内置能力，例如集成 AI 能力、使用数据库和存储方案等。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27738%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzM4IiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 你也可以在文件树中查看扣子 AI 生成的代码文件，并通过自然语言指示扣子 AI 帮你修改代码、迭代你的项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27737%27%20height=%27316%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzM3IiBoZWlnaHQ9IjMxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

部署。 ​

  * 将你的项目部署到生产环境，让你的创意从开发阶段走向实际应用。 ​

  * 部署中：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271899%27%20height=%27811.8225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5OSIgaGVpZ2h0PSI4MTEuODIyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

部署完成后，可在浏览器访问：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27290%27%20height=%27178%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjE3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

​

​

上一篇

扣子空间「PPT发疯文学」大赛

下一篇

配额与限制