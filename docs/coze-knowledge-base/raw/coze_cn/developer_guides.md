---
source_url: https://docs.coze.cn/developer_guides
title: 'Coze CLI 介绍 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:17:50Z
---

# Coze CLI 介绍 - 文档 - 扣子

Coze CLI 介绍

Coze CLI 是什么​

Coze CLI （包名 @coze/cli）是专为 AI Agent 设计的命令行工具，简单来说，你平时在扣子编程网页端做的操作，Agent 用 Coze CLI 在自己的后台里都能完成，而且更便捷、更高效。你无需切换浏览器，只要下发指令，Agent 就能帮你操作扣子账号，通过扣子编程来开发和部署应用、生成文档、语音、制作视频等等。​

通过 Coze CLI，你的 Agent 可以在后台执行命令，从而快速操作扣子编程的所有核心功能，高效搞定 AI 编程项目创建、部署、多媒体内容生成等所有需求，大幅提升开发效率。​

更进一步，扣子 Agent 现已全面接入 Coze CLI，无需打开扣子编程网页，只需在对话中告诉扣子你的需求，它就能帮你自动创建编程项目、一键开发并部署 Web 和 App 应用。​

为什么需要 Coze CLI​

在扣子编程中，我们习惯用鼠标在界面上通过点击按钮，来完成 AI 编程项目的开发与部署，但进入智能体（Agent）时代，我们已经可以通过 Agent 对话来操作各类软件与系统，创建项目、配置技能、调试流程、上线应用……这些标准且重复的动作，完全可以交由 Agent 来完成。​

Coze CLI 正是为此而生，并对所有 Agent 开放。Coze CLI 不只是一个提供给开发者的终端工具，更是扣子给所有 Agent 开放的一套底层原生接口。它让 Agent 不再只是“会想”，而是真正开始“会动手”。之前那个能帮你完成全栈开发、一键部署上线的扣子编程，现在，你的 Agent 也能用了。​

在 AI Agent 时代，你无需学习如何安装和使用 Coze CLI，甚至无需感知它的存在，只要用自然语言和你的 Agent 对话，它会自己用 CLI 去操作 Coze，实现更为自动化的氛围编程。​

Coze CLI 能做什么​

一句话开发应用​

不用在页面上反复点选、配置、调试。告诉 AI 你的需求，它直接通过 CLI 生成项目结构、编写代码，创建 App 和 Web 应用、一键部署上线，不用你写一行代码。你只需要下发指令，剩下的都交给 AI。​

你的指令：​

​

Plain Text

复制

使用 Coze CLI，做一个好玩又实用的小东西吧，做个决策助手网站​

​

对话过程：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271524%27%20height=%271280%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyNCIgaGVpZ2h0PSIxMjgwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

你的产物：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271988%27%20height=%271794%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk4OCIgaGVpZ2h0PSIxNzk0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

AI 调试与排障​

优秀的应用往往不是一次性生成的，而是在不断迭代、优化。通过 Coze CLI，你还可以通过对话修改应用、添加功能、调整样式等。​

你的指令：​

​

Plain Text

复制

换个风格，换成活泼可爱的​

​

​

对话过程：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271558%27%20height=%271532%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1OCIgaGVpZ2h0PSIxNTMyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

你的产物：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272820%27%20height=%271652%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgyMCIgaGVpZ2h0PSIxNjUyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

在遇到运行错误时，AI 会自动读取 CLI 的后台运行日志，精准定位报错位置、分析执行链路，并自动修复问题。​

简单来说，当你在度假时忽然收到线上报错，你甚至不需要打开电脑，随手跟 Agent 说一句就行。它会自己去看报错日志，找出是哪里卡住了，然后自己修改错误、重新测试，直到帮你把整个流程彻彻底底地跑通。​

你的指令：​

​

Plain Text

复制

“决策助手”这个项目，抛硬币这里有点问题，图片是正面，文字提示是反面，帮我修复一下​

​

​

对话过程：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271490%27%20height=%27790%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ5MCIgaGVpZ2h0PSI3OTAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

修复结果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272896%27%20height=%271662%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg5NiIgaGVpZ2h0PSIxNjYyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

一站式内容创作​

AI 可通过 Coze CLI 直接调用扣子编程内置集成的内容生成能力，一站式完成内容创作、存储与发布。支持文本、图片、音频、视频全模态生成，覆盖文案、插画、配音、自动成片等场景。​

例如直接对话，就能生成小红书高密度风格信息图、生成视频、音频：​

对话过程：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271380%27%20height=%27874%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM4MCIgaGVpZ2h0PSI4NzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

生成的信息图：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271280%27%20height=%27450%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4MCIgaGVpZ2h0PSI0NTAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

生成的视频：​

​

​

__

Replay

Play

00:00 / 02:02 Live

00:00

Fullscreen 

Cssfullscreen 

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag 

​

​

​

​

云端存储产物​

之前用过 Openclaw 的朋友可能都遇到过一个痛点：Agent 明明生成了文件，但给出的链接却经常无法打开。这其实是因为文件只存在于 Agent 的虚拟沙盒里，缺乏公共的对象存储能力。​

现在通过 扣子编程 CLI 接口，Agent 可以直接把生成的内容上传到云端，可以理解为给 Agent装上了一个“自动同步云盘”，这样你最终收到的，就是一个能直接点击预览、随时下载的公网链接，让文件获取更轻松！​

核心能力​

​

模块​| 功能​  
---|---  
AI 编程开发​| 

  * 一句话创建应用程序：支持通过自然语言一键创建 Web、App 应用，更多类型敬请期待。​

  * AI 指令交互：和编程 AI 对话，发送自然语言指令，让 AI 自动执行编码、开发等相关任务；支持通过 @本地文件等方式，向 AI 传递开发上下文信息​

  * AI 任务管理：查询 AI 开发任务的执行状态、取消任务。​

  
预览与部署​| 

  * 一键预览：获取项目沙箱预览链接，用于开发环境测试、项目效果展示，无需正式部署。​

  * 一键部署：将项目一键部署至生产环境，支持同步和异步模式、查询部署状态。​

  * 域名管理：绑定、解绑、查看项目自定义域名，配置外网访问地址。​

  
项目管理​| 

  * 基础操作：查看编程项目列表、项目详情、删除项目​

  * 环境变量：增删改查开发、生产环境变量​

  * 编程技能：查看项目可用编程技能列表、添加编程技能、移除编程技能​

  
多模态生成​| 

  * 文生图：通过文本生成图片，可配置图片尺寸、去水印、参考图、批量生成等参数​

  * 文本转语音（TTS）：将文本转换为语音，可自定义音色、语速、音量，支持 SSML 格式配置​

  * 文生视频：通过文本生成视频，可控制视频分辨率、时长、首尾帧等核心参数​

  * 任务管理：查询多模态生成任务的执行状态，便于监控生成进度、获取生成结果​

  
账号与空间管理​| 

  * 身份认证：登录或退出扣子账号、账号鉴权等​

  * 组织管理：查看或切换组织、设置默认组织​

  * 空间管理：查看或切换空间、设置默认空间​

  
  
​

快速开始​

扣子使用 Coze CLI​

扣子中已经预安装了扣子编程 CLI，你可以直接打开扣子，随时随地跟扣子对话，让它完成编程开发。​

你的指令：​

​

Plain Text

复制

帮我用 Coze CLI 创建一个网页应用，介绍 Coze CLI 的功能及使用方式 ​

​

对话过程：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271550%27%20height=%271216%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1MCIgaGVpZ2h0PSIxMjE2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

预览作品：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272238%27%20height=%271480%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzOCIgaGVpZ2h0PSIxNDgwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

其他 Agent 使用 Coze CLI​

如果你使用 TRAE、Claude Code、扣子编程 OpenClaw 助手等其他 Agent，需要先安装 Coze CLI。​

1.

安装 Coze CLI。​

  * 通过 Skill 安装。​

  * 我们已经把安装过程打包成了 Skill 并上传到了虾评。把这段话发给你的Agent，它自己就能学会如何安装并使用 Coze CLI。​

  * ​

Plain Text

复制

去这里学一下 Coze CLI Skill：​

https://xiaping.coze.site/skill/aee0a560-9634-415e-9ff3-77b1587a4134?ref=628be309-5da3-434f-8b1a-722e65b450e3​

​

  * 对话中直接安装。​

  * 可以复制以下信息，并发送给你的 AI Agent，立即完成安装。​

  * ​

Plain Text

复制

# 帮我安装 Coze CLI​

npm install -g @coze/cli​

​

2.

登录你的扣子账号。 ​

  * 复制以下信息，并发送给你的 AI Agent。Agent 会自动生成授权链接，你需要按照页面提示完成账号授权。​

  * ​

Plain Text

复制

# 帮我登录扣子账号 ​

coze auth login --oauth​

​

3.

发起第一个任务。​

  * 复制以下信息，并发送给你的 AI Agent。通过简单对话，快速生成并部署一个网页应用。​

  * ​

Plain Text

复制

帮我用 Coze CLI 创建一个网页应用，介绍 Coze CLI 的功能及使用方式 ​

创建完成后，请将预览链接发给我​

​

下一篇

Coze CLI 最佳实践