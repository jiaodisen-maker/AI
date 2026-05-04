---
source_url: https://docs.coze.cn/guides/vibe_coding_agent
title: '开发智能体 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:13Z
---

# 开发智能体 - 文档 - 扣子

开发智能体

扣子编程提供全栈式的 AI 编程体验，通过简单的对话即可开发全代码的 AI 智能体项目，覆盖从创意构思到产品落地的全流程，为开发者提供一站式的 AI 编程服务。 ​

功能概述​

智能体是基于对话的 AI 项目，它通过对话方式接收用户的输入，由大模型自动加载技能，执行用户指定的业务流程，并生成最终的回复。智能体的典型场景包括智能客服、虚拟伴侣、个人助理、英语外教等。​

扣子编程提供了一个基于 Web 的 AI 编程开发环境，你只需要通过自然语言描述智能体创意，扣子 AI 会自动完成智能体的开发、测试、迭代和发布，帮助开发者聚焦核心创意与价值设计，高效实现从创意构思到产品落地。​

费用说明​

开发、测试、线上使用智能体时，以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：调用大语言模型、联网搜索、图像生成等内置集成服务。​

配额与限制​

开发智能体时，存在可创建的项目数量、可回滚版本数、可部署的次数等配额限制，详细说明，请参考​配额与限制。​

开发智能体​

参考以下流程，通过自然语言开发智能体。​

步骤一：输入开发提示词​

1.

在[扣子编程](<https://code.coze.cn/home>)首页，单击智能体选项卡。​

2.

在文本框输入你的提示词。​

  * 你需要尽可能清晰且详细地描述智能体功能、业务逻辑、约束等方面的要求。例如，你可以输入以下提示：​

  * ​

Plain Text

复制

帮我开发一个全平台爆款种草文案策划的Agent，核心功能是基于用户输入的产品名称，自动生成符合“小红书”或“抖音”平台调性的高质量种草文案。Agent需要具备极强的“网感”，能够熟练使用Emoji表情，并提供不同营销角度的文案方案。​

核心工作逻辑​

接收输入数据：包括产品名称。​

风格迁移与润色：​

若为小红书：采用“集美/姐妹”口吻，标题必须包含吸引眼球的关键词（如“绝绝子”、“按头安利”、“无限回购”），正文大量使用Emoji（✨💖🔥），注重分段和视觉舒适度，文末包含相关话题标签。​

若为抖音：采用短视频脚本格式，注重开头的“黄金3秒”完播率设计，语言犀利、节奏快，突出反转或强情绪引导。​

多方案生成：针对同一个产品，必须输出3套不同侧重点的文案（例如：痛点直击型、情感共鸣型、性价比分析型），供用户选择。​

​

约束​

拒绝AI味：生成的文案严禁出现“综上所述”、“总而言之”、“这款产品具有...”等生硬的机器翻译腔调，必须口语化、生活化。​

Emoji浓度：小红书风格文案中，Emoji的占比需适中，每段话至少包含1-2个表情符号。​

长度限制：小红书正文控制在200-400字之间；抖音脚本时长控制在45秒口播以内。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27455%27%20height=%27197%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU1IiBoZWlnaHQ9IjE5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

（可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让扣子 AI 生成的结果更精准、更符合你的预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27318%27%20height=%27170%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE4IiBoZWlnaHQ9IjE3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ① 上传附件

② 选择协作模式

③ 调用技能

④ 选择编程模型

酌情上传一些图片或文件，作为附加信息提供给扣子 AI，以便扣子 AI 能更理解你的需求。例如上传你想参考的实现方案等。​

​

4.

单击提交按钮。​

  * 扣子 AI 会根据你输入的提示词来开始设计智能体、创建项目，并自动为项目设置智能体名称。过程预计需要几分钟，请耐心等待。​

  * 你可以在左侧实时查看扣子 AI 开发智能体的步骤和详细进展。智能体开发完毕后，你可以查看开发完成总结，查看智能体的主要功能、项目文件路径等信息。​

步骤二：预览与测试​

智能体生成完毕后，扣子 AI 会自动生成测试用例并完成一轮单元测试。测试通过后扣子 AI 会提供预览页面，你可以在右侧预览页面， 通过与智能体对话，测试其表现是否符合预期。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27362.5%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM2Mi41IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

操作​| 说明​  
---|---  
全面测试​| 在预览区全面测试你的智能体，通常建议关注以下问题：​

  * 输出效果是否符合业务场景：输出结果是否符合设计要求，例如内容的准确性、格式的规范性、逻辑的正确性等。 ​

  * AI 能力是否正常：如果你的智能体集成了 AI 能力，例如文本生成、图片生成等，验证 AI 模型的输出是否符合预期。​

  
修复故障​| 通常情况下，扣子 AI 会自动识别并提示你修复故障，你可以根据页面提示，单击一键修复，允许扣子 AI 尝试修复这些问题。​如果你在调试智能体的过程中出现页面报错，你可以复制报错信息并粘贴到左侧对话中，将其发送给扣子 AI，要求它修复故障。​  
  
​

迭代智能体​

测试并修复问题之后，如果已经生成的智能体仍有可改进之处，你可以通过自然语言，和扣子 AI 一起迭代你的应用。​

调整需求​

如果之前某次对话中你输入的描述有误或不准确，导致扣子 AI 生成的智能体无法满足你的需求，相对于回滚版本再重新对话生成智能体，直接修改你发送的历史消息会更加高效。​

你可以在对话记录中找到该历史消息，对其进行修改后敲击回车，扣子 AI 会根据新的描述对应用进行调整和优化。同时扣子 AI 的版本记录里也会另起一个分支来记录本次及后续的变更。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27397%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjM5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

编辑智能体​

和扣子 AI 一起持续优化智能体，直到实现预期的效果。你可以通过以下方式来修改扣子 AI 生成的智能体：​

自然语言

修改系统提示词

在智能体开发页面左侧的对话框中，描述你需要优化的具体方面和期望达到的效果，扣子 AI 将基于你的输入自动进行迭代。​

示例指令：​

​

Markdown

复制

智能体的输出文案需要为纯净的JSON格式，不包含多余的解释性文字。​

输出格式​

JSON​

{​

"product_name": "{{product_name}}",​

"platform": "{{platform}}",​

"plans": [​

{​

"angle": "<文案切入角度，如：痛点直击型>",​

"title": "<生成的爆款标题，含表情>",​

"content": "<生成的正文内容，含表情和排版>",​

"tags": ["<话题标签1>", "<话题标签2>"]​

},​

{​

"angle": "<文案切入角度，如：情感共鸣型>",​

"title": "<生成的爆款标题，含表情>",​

"content": "<生成的正文内容，含表情和排版>",​

"tags": ["<话题标签1>", "<话题标签2>"]​

},​

{​

"angle": "<文案切入角度，如：干货测评型>",​

"title": "<生成的爆款标题，含表情>",​

"content": "<生成的正文内容，含表情和排版>",​

"tags": ["<话题标签1>", "<话题标签2>"]​

}​

]​

}​

​

​

选择模型并设置模型参数​

你可以为智能体选择不同的大模型，并对其进行精细化的参数设置（如生成随机性、Top P 和最大回复长度等）。各个模型支持调整的参数不同，具体以界面为准。​

说明

模型默认不开启前缀缓存，你可以通过对话方式让扣子 AI 开启此功能（如为智能体开启前缀缓存），以加快模型响应速度并降低使用成本。计费详情请参考​内置集成费用，操作步骤请参考​开启缓存。​

​

1.

在智能体开发页面的预览窗口，单击智能体当前使用的模型。​

2.

在右侧弹出的 Agent 节点窗口中，选择要切换的模型。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27523%27%20height=%27246%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIzIiBoZWlnaHQ9IjI0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

单击设置图标，设置模型参数，详细参数说明可参考​配置大语言模型参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27203%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAzIiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

回滚开发版本​

扣子 AI 使用当前的先进模型来完成任务，但由于模型生成代码的随机性，有时可能无法完全满足你的需求，生成了不符合预期的代码，或者出现了反复修复失败的故障，此时你可以使用回滚版本功能，将智能体恢复到之前正常的版本状态。​

在智能体开发页面单击版本历史图标，在目标版本右侧单击回滚图标，可以将智能体回滚至该版本。回滚后，扣子编程会自动生成一个新的部署版本，原始的历史记录不会被修改或删除。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27234.22897196261684%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIzNC4yMjg5NzE5NjI2MTY4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

集成能力​

扣子编程通过技能方式封装了一批常见的集成能力接口，方便你快速为智能体添加各种功能，例如数据库、存储、AI 能力等，使智能体更好地满足多样化的业务需求。​

在和扣子 AI 对话，添加集成能力之前，你需要先在扣子 AI 对话区域单击技能，确认扣子 AI 已添加了你想要的技能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27368%27%20height=%27354%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY4IiBoZWlnaHQ9IjM1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

对象存储与数据库​

扣子编程提供了结构化、非结构化数据托管方案。若智能体需要持久化存储、查询或更新用户记录、业务数据、历史交互结果等数据，你可以为其集成数据库。如果智能体需要存储图片、文档、音频、视频等各类文件，你可以为其集成对象存储。详细使用方法，请参考​集成数据库能力、​集成对象存储能力。​

例如开发一个英语单词学习智能体，并为智能体添加一个数据库，用于存储已学习的单词、学习时间、掌握状态及错误记录，支持智能体根据历史数据生成个性化复习计划。在开发过程中，扣子 AI 是根据提示词加载数据库技能来接入数据库集成服务。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271790%27%20height=%271129.8581560283687%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc5MCIgaGVpZ2h0PSIxMTI5Ljg1ODE1NjAyODM2ODciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271790%27%20height=%27592.434988179669%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc5MCIgaGVpZ2h0PSI1OTIuNDM0OTg4MTc5NjY5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

飞书消息等外部集成​

扣子编程提供丰富的外部集成服务，包括飞书消息、飞书多维表格、微信、火山方舟等。使用前，需要由空间管理员在工作空间中配置外部集成。配置完成后，开发智能体时，扣子编程会基于当前的开发场景与功能需求，自动识别并加载对应的技能来接入外部集成服务。​

例如，你需要实现将智能体生成的内容发送飞书消息，实现方法如下：​

1.

在扣子编程的集成服务中配置相应的外部集成，如集成飞书消息，具体操作步骤参考​飞书消息。 ​

2.

在对话框中，通过自然语言描述需要接入的外部集成，例如：​

  * ​

Plain Text

复制

智能体完成任务后，自动向指定飞书群推送结果通知​

​

  * 在开发过程中，扣子 AI 将加载飞书消息技能来为智能体接入飞书消息集成服务。​

后续操作​

部署智能体​

将你在扣子编程上开发的智能体，快速部署成为可访问的 API 服务，以便后续通过 OpenAPI 方式将智能体的 AI 功能集成到你的应用中。详细说明可参考​部署智能体。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27659%27%20height=%27439%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU5IiBoZWlnaHQ9IjQzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

分享项目​

在智能体开发页面右上角单击分享按钮，可以将部署成功的项目分享给他人。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27243.05555555555551%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI0My4wNTU1NTU1NTU1NTU1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看线上日志​

查看已发布的智能体的后端运行日志，以便在出现问题时进行故障排查和分析。详细说明可参考​查看日志和 Trace。​

常见问题​

  * ​工作空间中的成员为什么无法编辑项目？​

  * ​如何查看智能体使用的模型？​

  * ​如何切换大语言模型？​

​

上一篇

开发小程序

下一篇

开发工作流