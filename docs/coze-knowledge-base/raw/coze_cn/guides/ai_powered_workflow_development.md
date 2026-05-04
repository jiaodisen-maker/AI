---
source_url: https://docs.coze.cn/guides/ai_powered_workflow_development
title: '开发工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:16Z
---

# 开发工作流 - 文档 - 扣子

开发工作流

扣子编程全新推出 AI 生成式工作流功能，核心是将复杂工作流搭建流程转化为自然语言描述驱动的高效模式。你无需编写代码，只需用文字清晰描述业务需求，扣子 AI 即能自动生成对应的工作流完整代码，并完成代码测试、需求迭代等全流程操作。​

扣子编程改变了传统工作流搭建逻辑，帮助开发者从「如何分步实现」转向「需要实现什么目标」，大幅降低工作流搭建门槛，提升开发效率。​

费用说明​

开发、测试、线上使用工作流时，以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：调用大语言模型、联网搜索、图像生成等内置集成服务。​

配额与限制​

开发工作流时，存在可创建的项目数量、可回滚版本数、可部署次数等配额限制，详细说明，请参考​配额与限制。​

开发工作流​

参考以下流程，通过 AI 编程开发全代码工作流。​

步骤一：输入开发提示词​

1.

在[扣子编程](<https://code.coze.cn/home>)首页，单击工作流选项卡。​

2.

在文本框输入你的提示词。​

  * 你需要尽可能清晰且详细地描述工作流的功能、业务逻辑、交互等方面的要求。例如，你可以输入以下提示：​

  * ​

Plain Text

复制

搭建一个发票读取工作流，支持上传并解析发票类 PDF 文件，自动提取 PDF 中的关键信息，提取完成后，生成结构化输出结果（支持 JSON 格式或表格格式），确保字段清晰、数据准确。若涉及多页 PDF 发票，需支持批量解析与信息汇总。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27489%27%20height=%27248%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/dc6030481c3642af89e3d980718a0210~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

（可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让扣子 AI 生成的结果更精准、更符合你的预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27410%27%20height=%27164%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEwIiBoZWlnaHQ9IjE2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ① 上传附件

② 选择协作模式

③ 调用技能

④ 选择编程模型

酌情上传一些图片或文件，作为附加信息提供给扣子 AI，以便扣子 AI 能更理解你的需求。例如上传你想参考的实现方案等。​

​

4.

单击运行图标，开始开发你的工作流。​

步骤二：AI 编程开发工作流​

在工作流开发过程中，扣子 AI 会根据你输入的提示词，自动判断需要加载的技能，并生成符合你功能、交互等要求的工作流代码。​

扣子 AI 判断你的工作流需要数据库、存储、AI 等能力时，会自动加载官方技能来接入对应的集成服务，并遵循技能使用指南完成开发。如果扣子 AI 未自动集成这些能力，你也可以通过自然语言要求扣子 AI 添加相关能力，例如，你可以说：​

​

Plain Text

复制

为我的工作流添加数据库功能，用于存储用户提交的表单数据​

​

关于技能与集成能力的详细说明，请参考​集成能力。​

步骤三：预览工作流​

初步生成代码后，扣子 AI 会自动生成测试用例并完成自动化测试。测试通过后，扣子 AI 将在画布中呈现完整的工作流，你可直观查看工作流的整体架构、各节点的关联逻辑。​

扣子编程工作流采用语义层、 参数层和代码层三层协同驱动架构，基于语义驱动，无需预先定义抽象化节点模板，可高效生成覆盖全流程的节点。所有工作流均以开始节点为起点，以结束节点为终点。开始节点用于设定启动工作流需要的输入信息，结束节点用于返回工作流运行后的结果。任务执行节点是工作流的核心功能单元，既可能是单个独立功能组件，也可能是多个关联功能的组合组件。它能覆盖图像生成、数据库读写、第三方工具调用等多种业务场景。​

你可以单击画布中的任意节点，可以查看该节点的详细信息，包括输入、输出参数及对应的配置等。如果你对工作流节点存在疑问，可以框选一个或多个目标节点，单击解释，扣子 AI 会解读该节点，提供详细的节点介绍、关键执行逻辑以及异常与降级策略。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271258%27%20height=%271180.8967741935485%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1OCIgaGVpZ2h0PSIxMTgwLjg5Njc3NDE5MzU0ODUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27215%27%20height=%27496%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE1IiBoZWlnaHQ9IjQ5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤四：试运行工作流​

确认工作流的结构与节点配置初步满足需求后，你可以试运行工作流，对工作流进行全链路验证。​

  * 验证工作流整体运行状态是否正常，无执行报错、流程中断等异常情况。​

  * 验证各节点间的数据传递链路是否畅通、逻辑交互是否匹配预期，确保上游节点的输出数据格式与下游节点的输入要求完全兼容，且节点的执行顺序、分支逻辑、条件判断等均符合需求。​

你可以在画布上，单击试运行，然后根据页面提示配置合适的参数值，最后单击试运行。在试运行过程中，画布会实时展示运行进度，包括执行状态、单节点消耗时间等信息。试运行完成后，界面上将展示工作流的返回结果。你还可以单击画布中的任意节点，查看该节点在此次试运行中的详细输入与输出信息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27533%27%20height=%27497%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMzIiBoZWlnaHQ9IjQ5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

如果出现故障，扣子 AI 通常会自动识别并提示你修复故障，你可以根据页面提示，单击一键修复或自动修复，允许扣子 AI 尝试修复这些问题。如果在调试工作流过程中出现报错，你可以复制报错信息到对话中，要求扣子 AI 进行修复。​

迭代工作流​

测试并修复问题之后，如果已生成的工作流仍有可改进之处，你可以通过自然语言或编写代码的方式，和扣子 AI 一起迭代你的工作流。​

调整需求​

如果历史对话中存在不准确的描述，导致生成的工作流无法满足需求，你可以修改历史对话，让扣子 AI 根据新的描述对工作流进行调整和优化，无需回滚版本。同时扣子 AI 的版本记录里也会另起一个分支来记录本次及后续的变更。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27347%27%20height=%27165%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ3IiBoZWlnaHQ9IjE2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

编辑工作流​

当扣子 AI 生成初步的工作流后，你可以继续通过多种方式与其协作，对工作流进行修改和优化，直至达到预期效果。​

方式一：通过自然语言调整​

这是最直接、简便的方式。你只需在对话框中用自然语言提出修改建议，扣子 AI 就会理解你的意图并对整个工作流进行调整。例如：​

​

Plain Text

复制

增加一个配置参数，用于选择飞书消息类型。​

​

方式二：引用特定节点进行精确修改​

如果你想针对画布中的某些节点进行精准修改，引用功能是最高效的方式。​

1.

在画布中，框选目标一个或多个工作流节点，单击引用。​

2.

系统将在对话框中引用该节点，然后你可以输入修改指令。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27471%27%20height=%27247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcxIiBoZWlnaHQ9IjI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

方式三：通过画布进行可视化编排​

当你想在工作流的特定位置进行节点的增加、修改、删除操作时，可以直接在画布上手动编排与设计。手动编排工作流并不会直接更新代码，需要单击发送并执行变更，让扣子 AI 完成实际的修改工作。​

此处以增加节点的操作为例。​

1.

在画布中选择目标节点，单击➕ 。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27521%27%20height=%27274%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIxIiBoZWlnaHQ9IjI3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在新建节点对话框中，选择节点类型及对应配置。​

  * ​

节点类型​| 说明​| 图示​  
---|---|---  
动作​| 执行具体任务的节点，例如发送飞书消息、生成图片、生成视频、调用大模型等。​选择类型为动作后，需要在描述节点功能文本框中，清晰说明该节点要完成的具体操作。例如：​​Plain Text复制增加一个发送消息到飞书的节点，将提取到的发票信息自动发送到飞书群组。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27783.75%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9Ijc4My43NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
条件​| 逻辑判断与分支流转的节点，可根据不同的条件，决定工作流的走向。​选择类型为条件后，你可以按需设置条件分支数量，并在条件节点中，设置对应的条件及执行动作。例如：​
    * 条件1：发票金额大于5000、执行动作增加标签字段 tag，值为“大额待审批“。​
    * 条件2：否则，默认执行此分支、增加标签字段 tag，值为“小额免审批“。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271183%27%20height=%27805.4468085106383%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE4MyIgaGVpZ2h0PSI4MDUuNDQ2ODA4NTEwNjM4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
并发​| 当多个操作之间无先后依赖关系时，可通过并发节点并行处理，减少整体耗时。​选择类型为并发后，你可以按需设置并发分支数量，并在并发节点中，设置对应的执行动作。​例如同时执行发送飞书通知和写入飞书多维表格两个动作。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271091%27%20height=%27520.8645161290323%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA5MSIgaGVpZ2h0PSI1MjAuODY0NTE2MTI5MDMyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

3.

在画布右上角，单击发送并执行变更。​

  * 扣子 AI 将接管任务，然后理解你在画布中的配置，完成工作流编排。​

调试代码​

扣子编程提供了一个基于 Web 的 AI 编程环境，你可以在代码编辑器中修改代码文件、在终端中执行命令调试代码，和扣子 AI 一起开始开发你的工作流。关于 AI 编程开发环境的使用技巧，可参考​AI 编程环境。​

常见操作如下：​

​

操作​| 说明​| 示例​  
---|---|---  
通过扣子 AI 修改代码​| 在页面右上角单击文件树图标进入代码编辑器，找到你想修改的代码文件或片段，并单击引用到对话，然后通过自然语言描述你的修改需求。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271936%27%20height=%271025.9907834101384%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkzNiIgaGVpZ2h0PSIxMDI1Ljk5MDc4MzQxMDEzODQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
手动修改代码​| 在页面右上角单击文件树图标进入代码编辑器，你可以在其中查看扣子 AI 生成的所有代码文件，并直接修改代码。​修改代码之后随时切回预览页面，刷新画布，即可体验最新的工作流效果。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271800%27%20height=%271028.5714285714284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgwMCIgaGVpZ2h0PSIxMDI4LjU3MTQyODU3MTQyODQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
终端运行代码​| 代码编辑器下方是 Web 终端，你可以通过终端执行常见的命令来调试并迭代你的工作流，例如执行npm install安装项目依赖等，与本地终端操作逻辑一致。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271796%27%20height=%271100.774193548387%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc5NiIgaGVpZ2h0PSIxMTAwLjc3NDE5MzU0ODM4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

回滚版本​

扣子 AI 使用当前先进模型来完成任务，但由于模型生成代码的随机性，有时可能无法完全满足你的需求，生成了不符合预期的代码，或者出现了反复修复失败的故障，此时你可以使用回滚版本功能，将工作流恢复到之前正常的版本状态。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27445%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ1IiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

集成能力​

扣子编程通过技能方式封装了一批常见的集成能力接口，方便你快速为工作流添加各种功能，例如数据库、存储、AI 能力等，使工作流更好地满足多样化的业务需求。​

在和扣子 AI 对话，添加集成能力之前，你需要先在扣子 AI 对话区域单击技能，确认扣子 AI 已添加了你想要的技能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27351%27%20height=%27346%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUxIiBoZWlnaHQ9IjM0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

AI 能力​

为工作流添加 AI 能力时，通常需要开通模型服务并获取 API 密钥、并自行完成模型调用的配置与开发。扣子编程托管了业界先进的各种模型服务，无需任何配置，扣子 AI 会自动为你的工作流添加 AI 能力，帮助你开发更为智能的工作流。例如开发一个阅读笔记总结工作流，通过大模型可以将获取到的文章内容进行总结、提炼，并输出总结笔记。​

默认情况下，工作流已开通了大模型集成的权限，扣子 AI 会在收到指令后，自动为工作流添加 AI 功能。你也可以在对话区发送自然语言指令，让扣子 AI 集成大模型能力。例如：​

​

Plain Text

复制

使用大模型总结检索到的文章，并整理阅读笔记​

​

更多信息，请参考​内置集成。​

存储与数据库​

扣子编程提供了结构化、非结构化数据托管方案，对于需要集成数据库和存储能力的工作流，扣子 AI 会根据任务要求自动集成并设置数据库能力和存储能力。​

例如运行提取发票信息的工作流时，将发票提取记录写入到数据库中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272127%27%20height=%271116.2978723404256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEyNyIgaGVpZ2h0PSIxMTE2LjI5Nzg3MjM0MDQyNTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272056%27%20height=%27385.85994397759106%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA1NiIgaGVpZ2h0PSIzODUuODU5OTQzOTc3NTkxMDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

更多信息，请参考​集成数据库能力、​集成对象存储能力。​

飞书消息等外部集成​

除了扣子编程内置的存储、数据库等能力之外，你还可以为你的工作流集成外部功能和服务，例如飞书消息、飞书多维表格等。只需要简单的配置，即可在你的项目中使用这些外部集成能力，详细配置说明可参考​管理外部集成服务。​

例如集成飞书多维表格服务，在运行提取发票信息的工作流时，将发票提取结果写入到飞书多维表格中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271486%27%20height=%27959.049645390071%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ4NiIgaGVpZ2h0PSI5NTkuMDQ5NjQ1MzkwMDcxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27752%27%20height=%27116%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUyIiBoZWlnaHQ9IjExNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

更多信息，请参考​支持的集成服务。​

后续操作​

部署项目​

完成工作流的开发与测试之后，你可以在页面右上角单击部署，将扣子编程开发的工作流部署成为一个可调用的 API 服务，以便后续通过 OpenAPI 方式将工作流的 AI 功能集成到你的应用中。具体操作，请参考​部署工作流。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27586%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg2IiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

分享项目​

在项目开发页面右上角单击分享按钮，可以将部署成功的项目分享给他人。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27556%27%20height=%27321%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU2IiBoZWlnaHQ9IjMyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看线上日志​

查看已发布的应用、智能体和工作流的后端运行日志，以便在出现问题时进行故障排查和分析。详细说明可参考​查看日志和 Trace。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27546%27%20height=%27365%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ2IiBoZWlnaHQ9IjM2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

  * ​工作空间中的成员为什么无法编辑项目？​

  * ​如何查看内置集成消耗的积分？​

​

​

上一篇

开发智能体

下一篇

导入项目