---
source_url: https://docs.coze.cn/guides/internal_integrations
title: '内置集成 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:32Z
---

# 内置集成 - 文档 - 扣子

内置集成

内置集成是扣子编程预先打包的一系列 AI 功能和服务。你可以将它理解为“即用工具箱”，无需提供 API 密钥或进行任何配置，即可直接用来增强你的应用能力。这些内置集成包括了豆包、DeepSeek 和 Kimi 等主流供应商的 AI 模型，数据库、存储、联网搜索等基础能力。​

如何使用内置集成？​

在开发项目时，你只需与扣子 AI 对话，扣子 AI 即会加载相应的技能，为 AI 编程项目接入所需的内置集成服务。​

  * 初始构建项目：开发具有 AI 功能的新项目时，扣子 AI 会自动接入所有预置的大语言模型。例如输入如下指令：​

  * ​

Plain Text

复制

开发一个智能体，总结今天的科技新闻​

​

  * 开发完成后，你可以切换使用不同的大语言模型，具体操作，请参考​如何切换大语言模型？。​

  * 针对已有的项目：在已开发的 AI 编程项目中，你可以继续通过对话方式，让扣子 AI 搜索并加载对应技能，来为项目接入内置集成服务。例如输入如下指令：​

  * ​

Plain Text

复制

为当前的 Agent 添加一个数据库，用于存放员工的基本信息​

​

费用说明​

扣子 AI 编程目前免收存储、数据库、向量模型的内置集成费用，后续正式计费的时间计划与产品定价请关注平台公告。​

如果你的项目接入了其他内置集成，将根据不同内置集成服务的资费标准单独计费。更多信息，请参考​内置集成费用。​

支持的内置集成​

目前扣子编程已集成本文罗列的主流 AI 模型，并且支持扩展模型。你可以通过火山方舟集成服务来接入火山方舟模型，也可在 AI 编程项目对话区提供模型 API 信息，选择由扣子 AI 自动生成接入代码或者手动编写代码，完成自定义模型的接入。​

大语言模型​

扣子编程提供了各类主流的大语言模型，如豆包模型、DeepSeek 模型、Kimi 模型等。你无需任何配置，扣子 AI 会自动为你的 AI 编程项目接入 AI 能力，满足文本生成、语义理解、多轮对话等核心 AI 需求。更多信息，请参考​集成大模型能力。​

例如开发一个通过大模型总结阅读笔记的工作流，可以输入指令：​

​

Plain Text

复制

开发一个阅读笔记总结工作流，通过大模型可以将获取到的文章内容进行总结、提炼，并输出总结笔记​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27508%27%20height=%27303%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA4IiBoZWlnaHQ9IjMwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

生图大模型​

扣子编程提供了专业的豆包生图模型（如 Doubao-Seedream-5.0 ）。为 AI 编程项目接入生图大模型后，只需通过自然语言描述，即可生成高质量、风格多样的图片。具体的生图指令，请参考​基本能力。​

例如开发一个生图智能体，可以输入指令：​

​

Plain Text

复制

创建一个生图智能体​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27517%27%20height=%27289%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE3IiBoZWlnaHQ9IjI4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

视频生成大模型​

扣子编程提供了专业的豆包视频生成模型（如 Doubao-Seedance-1.5-pro）。为 AI 编程项目接入视频生成大模型后，只需通过自然语言描述，即可快速生成符合场景需求的视频。​

例如开发一个视频生成智能体，可以输入指令：​

​

Plain Text

复制

开发一个生视频智能体，能够分析用户输入的关键词，识别其中的主体、动作、环境和情感氛围，生成 5-10 秒的高清视频。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27408%27%20height=%27226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA4IiBoZWlnaHQ9IjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

内容处理​

扣子编程提供的内容处理工具，包括视频剪辑和链接读取，用于处理音视频和网页链接等多种媒体内容。​

  * 视频剪辑​

  * 为你的 AI 编程项目接入视频剪辑工具后，只需提供对应的音视频素材和指令，大模型即可调用该工具完成视频剪辑。支持的剪辑能力如下：​

  * ​

工具列表​| 说明​  
---|---  
audio_to_subtitle​| 将音频转换为字幕文件。​  
concat_videos​| 输入视频 URL 列表和对应的转场效果 ID 列表，工具即会自动按顺序拼接视频，并在各视频片段的拼接处添加指定的转场效果。​  
add_subtitles​| 基于视频 URL、字幕文件 URL/自定义文本、字幕样式，为视频添加字幕。​  
audio_extract​| 抽取视频中的音频，并支持将其保存为指定格式的音频文件。​  
video_trim​| 裁剪视频时长，保留从指定的裁剪开始时间到结束时间范围内的视频。​  
compile_video_audio​| 指定待合成的音频和视频 URL，合成音视频。​  
  
​

  * 链接读取​

  * 为你的 AI 编程项目接入链接读取工具后，只需提供网页 URL，大模型即可快速抓取并解析多类型的网页内容，包括网页、pdf、doc、docx、xlsx、csv 和 text 格式。请注意，由于部分网站设有访问限制，该工具可能无法获取其内容。​

例如开发一个音视频剪辑工作流，可以输入指令：​

​

Plain Text

复制

开发一个音视频剪辑工作流，能够将用户上传的视频、音频按照要求完成剪辑​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27425%27%20height=%27205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI1IiBoZWlnaHQ9IjIwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

向量模型​

扣子编程提供的向量模型，能够将图片、音频等非结构化的内容转换为向量并存储于数据库中，提升大模型对非结构数据的召回能力。向量是描述文本、图片等对象特征的高维数值数组。你可以把数据向量化功能想象成一个数据转化器，它能将不同类型的内容（如文档、图片）都转换为统一的数字格式—向量，让大模型能跨模态做语义级检索与匹配。更多信息，请参考​数据向量化写入与检索。​

例如开发一个智能客服智能体，并需要具备数据向量化写入与检索功能，可以输入指令：​

​

Plain Text

复制

搭建知识库智能客服Agent，支持将知识向量化写入到知识库中。​

将如下内容向量写入到知识库中，设置 Score 为 0.7，TopK 为 5。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27525%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI1IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271895%27%20height=%271263.3333333333333%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5NSIgaGVpZ2h0PSIxMjYzLjMzMzMzMzMzMzMzMzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

语音大模型​

扣子编程提供了专业的豆包语音模型，为你的 AI 编程项目赋予“能听会说”的能力，覆盖语音识别和语音合成两大场景。​

  * 语音识别：能高准确率地将语音转为文字，更能结合上下文理解多语言、多方言背后的真实意图。​

  * 语音合成：能智能判断文本的情绪，用极其自然、富有感染力的语调说话，告别冰冷的机器音，带来真人般的听觉体验。​

例如为英语学习智能体，添加语音播放功能，可以输入指令：​

​

Plain Text

复制

添加语音能力，回复的内容能够语音播放​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

联网搜索能力​

大模型本身不具备联网搜索能力，无法通过搜索引擎获取最新的知识和数据。扣子编程提供了融合信息搜索工具，为你的 AI 编程项目接入联网搜索能力，使其能够高效获取全网的公开信息，如最新的天气、新闻、热点话题等。​

该工具还深度集成豆包大模型的推理能力，能够精准解析用户检索意图，从而为大模型的决策过程提供更智能、更全面的信息补充。​

例如开发 AI 新闻获取与总结工作流，该工作流需具备联网搜索能力，可以输入指令：​

​

Plain Text

复制

建一个新闻工作流，每天获取最新的 AI 方向的信息，并提取关键内容​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27420%27%20height=%27232%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIwIiBoZWlnaHQ9IjIzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

数据库能力​

扣子编程提供的数据库服务，可帮助开发者为 AI 编程项目快速接入数据库，用于存储和管理各类结构化数据，如用户信息、订单历史等。​

该服务基于 PostgreSQL 引擎并由平台完全托管，开箱即用。开发者无需关注底层部署与运维工作，即可使用专业、稳定的数据库。更多信息，请参考​集成数据库能力。​

例如为发票信息提取工作流添加数据库能力，用来存储提取记录，可以输入指令：​

​

Plain Text

复制

添加数据库能力，将每次发票提取记录添加到数据库中​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272127%27%20height=%271116.2978723404256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEyNyIgaGVpZ2h0PSIxMTE2LjI5Nzg3MjM0MDQyNTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272056%27%20height=%27385.85994397759106%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA1NiIgaGVpZ2h0PSIzODUuODU5OTQzOTc3NTkxMDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

文件存储能力​

扣子编程提供的文件存储服务，可帮助开发者为 AI 编程项目快速接入对象存储，用于存储和管理图像、文档、音频、视频等各类非结构化数据。​

该服务开箱即用，由平台完全托管。开发者无需关注底层部署与运维工作，即可使用专业、稳定的对象存储服务。更多信息，请参考​集成对象存储能力。​

例如为 AI 新闻总结工作流添加文件存储能力，用于存储历史新闻，可以输入指令：​

​

Plain Text

复制

为我的工作流添加文件存储功能​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9IjI4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

  * ​如何查看内置集成消耗的积分？​

  * ​如何切换大语言模型？​

  * ​如何批量切换待下架模型？​

附件：内置集成模型列表​

关于模型的具体介绍，可参考​模型发布动态。​

​

内置集成服务​| 模型供应商​| 模型列表​  
---|---|---  
大语言模型​| 字节跳动​| 

  * doubao-seed-2.0-pro​

  * doubao-seed-2.0-lite​

  * doubao-seed-2.0-mini​

  * Doubao-Seed-1.8​

  * Doubao-Seed-1.6-Vision​

  * Doubao-Seed-1.6-Lite​

  * Doubao-Seed-1.6​

  
​| 深度求索​| 

  * DeepSeek-V3.2​

  * DeepSeek-R1​

  
​| 月之暗面​| Kimi-K2.5​  
​| 智谱 AI​| GLM-4.7​  
生图大模型​| 字节跳动​| 

  * Doubao-Seedream-4.5​

  * Doubao-Seedream-5.0​

  
视频生成大模型​| 字节跳动​| Doubao-Seedance-1.5-pro​  
语音大模型​| 字节跳动​| 

  * 语音识别​

  * 语音合成​

  
向量大模型​| 字节跳动​| 

  * Doubao-embedding​

  * Doubao-embedding-vision​

  
  
​

​

上一篇

集成服务概述

下一篇

飞书消息