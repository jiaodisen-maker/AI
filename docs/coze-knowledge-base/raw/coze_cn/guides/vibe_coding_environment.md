---
source_url: https://docs.coze.cn/guides/vibe_coding_environment
title: 'AI 编程环境 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:33Z
---

# AI 编程环境 - 文档 - 扣子

AI 编程环境

扣子编程提供了一个基于 Web 的 AI 编程开发环境，可以帮助你使用自然语言、图片等多模态的提示来快速开发应用项目，例如生成网页应用或移动端应用。​

什么是扣子 AI 编程环境​

扣子 AI 编程环境是一个 AI 驱动的云端开发环境，它以浏览器为载体，自带编码所需的基础功能，提供了开箱即用的编程体验。扣子 AI 编程环境融合了 AI 编程能力，完美适配氛围编程（Vibe Coding）范式，可满足从编辑到运行的全流程需求。扣子 AI 编程环境无需本地安装软件和依赖，让 AI 承担编码、调试等繁琐工作，开发者只需通过自然语言描述需求、验收成果，极大降低了编程门槛。​

其核心特性如下：​

  * 代码编辑器：内置支持多种编程语言的代码编辑器，提供语法高亮、代码格式化等功能。​

  * 集成 Web 终端：模拟 Linux 终端，可执行 npm 、python 等命令。​

  * 云端沙箱：为每个项目创建互相隔离的云端沙箱，包含了运行代码所需的操作系统、依赖和资源，支持实时预览网页、应用效果。​

  * AI 驱动：AI 深度嵌入开发全流程，支持自然语言生成代码，生成代码后能即时运行并展示效果；提供代码生成、代码补全、智能纠错等 AI 编程能力，能自主完成复杂的开发任务。​

了解编程环境​

用户界面​

在扣子编程首页输入你的需求，即可进入扣子 AI 编程环境。操作界面如下，从左到右依次为 AI 对话区、文件树、工作区。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271913%27%20height=%27864.6580796252928%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c58f5f7a5e3c4b61b6d15ca03e46f04c~tplv-goo7wpa0wc-quality:q75.image)​

​

​

编号​| 区域​| 说明​  
---|---|---  
①​| AI 对话区​| 简称对话区，是开发者和扣子 AI 的对话窗口，开发者可通过自然语言下达 AI 编程的指令，控制 AI 生成代码、修改代码。​该区域还支持精准关联上下文、提供多样化的交互形式，详细说明可参考​对话区。​  
②​| 文件树​| 文件树用于可视化展示项目目录结构，开发者可通过文件树查看扣子编程生成的代码文件。在扣子 AI 编程环境右上角单击文件夹图标，即可打开文件树区域。​详细说明可参考​文件树。​  
③​| 工作区​| 工作区是扣子 AI 编程环境的主面板，它集成了代码编辑、运行调试等多种功能，开发者可在此对扣子 AI 生成的代码进行编辑和测试。 ​

  * 代码编辑：在文件树中单击指定代码文件，即可在工作区查看并编辑此文件。详细说明可参考​代码编辑器。​

  * 界面预览：扣子 AI 生成的项目，可在工作区中查看并预览。​

  * 执行命令、查看输出：工作区下方设有终端区域，开发者可在此执行各类命令、调试项目，详细说明可查看​终端；此外还有输出区域，展示应用或后端服务的输出信息。​

  
  
​

对话区​

对话区，是开发者和扣子 AI 的对话窗口。开发者可通过自然语言下达 AI 编程的指令，控制 AI 生成代码、修改代码。在对话区，你可以：​

​

特性​| 说明​| 示例​  
---|---|---  
编辑消息​| 支持修改开发者已发送的历史消息。​找到要编辑的消息，单击编辑图标之后即可修改自己发送的历史消息。​重新发送编辑后的 Query 相当于发起一次全新的对话请求。扣子 AI 将基于当前最新的项目状态和上下文来处理这个新的 Query。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271204%27%20height=%27452.704%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwNCIgaGVpZ2h0PSI0NTIuNzA0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
重新生成​| 如果某一轮对话中，扣子 AI 的回复或者执行结果没有达到预期，你可以在对话区找到这条指令，点击重新生成图标，让扣子 AI 重新生成回复或执行操作。 ​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27729%27%20height=%27402.408%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzI5IiBoZWlnaHQ9IjQwMi40MDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
上传文件​| 除自然语言之外，你还可以在输入框左下角单击 + 来上传附件，支持图片、代码文件等多种格式，作为扣子 AI 理解需求、生成代码或版本迭代的上下文和参考信息。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271230%27%20height=%27472.32%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIzMCIgaGVpZ2h0PSI0NzIuMzIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
生成配置​| 控制扣子 AI 在处理当前 Query 时是否可以调用外部工具完成指定操作，例如调用联网搜索工具获取最新信息。开启某个工具后，扣子 AI 会自动根据任务需求，自行决定是否调用工具。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271180%27%20height=%27396.48%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE4MCIgaGVpZ2h0PSIzOTYuNDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
添加到对话​| 将代码片段、控制台或终端的输出、文件树中的文件、应用界面元素、工作流节点等元素添加到对话中，作为对话的上下文，提升用户与扣子 AI 协作的效率和精确性。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272904%27%20height=%271405.536%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwNCIgaGVpZ2h0PSIxNDA1LjUzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看积分消耗​| 每轮对话结束后，你可以在扣子 AI 回复的末尾查看本轮对话消耗的积分数量。积分消耗和对话中各类资源消耗有关，详细说明可参考​扣子编程任务费用。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27166%27%20height=%27133%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY2IiBoZWlnaHQ9IjEzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

代码编辑器​

扣子 AI 编程提供了代码编辑器，以供开发者实时查看或手动编辑 AI 生成的代码文件。该编辑器具备语法高亮、智能补全、Diff 展示、主题风格设置等实用功能，提升开发者的代码编辑效率和体验。 ​

​

特性​| 说明​| 示例​  
---|---|---  
查看代码文件​| 在文件树中单击指定代码文件，即可在工作区查看并编辑此文件。代码编辑器支持语法高亮、展示行号，还可以设置编辑器主题风格，提升交互体验。​如果 AI 修改了代码文件，也会高亮展示编辑前后的差异Diff），便于开发者理解代码的修改细节，从而更高效地进行代码审查。 ​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272922%27%20height=%271572.4322033898306%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyMiIgaGVpZ2h0PSIxNTcyLjQzMjIwMzM4OTgzMDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
编辑文件​| 支持前端 HTML/CSS、后端接口代码等多类型代码编辑，支持撤销和重做、变更自动保存等功能，保证代码编辑的灵活性和便捷性。常用的编辑器快捷键可参考​编辑器快捷键。​你也可以将代码文件或代码片段添加到对话中，让扣子 AI 帮助你根据需求定向修改代码内容，提高编程效率。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272922%27%20height=%271572.4322033898306%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyMiIgaGVpZ2h0PSIxNTcyLjQzMjIwMzM4OTgzMDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
代码检查​| 编辑器实时检查代码内容，可识别语法错误、编码规范问题、逻辑错误及安全漏洞，并提供详细的错误提示和修复建议，帮助开发者及时发现并解决代码中的潜在问题，确保代码的质量和安全性。 ​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272870%27%20height=%271386.3559322033898%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg3MCIgaGVpZ2h0PSIxMzg2LjM1NTkzMjIwMzM4OTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
AI 解释、编辑代码​| 代码编辑器支持与扣子 AI 联动，你可以将代码文件、代码内容引用到对话区，让扣子 AI 解释代码含义、编写代码、修复问题。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271908%27%20height=%27865.0677966101695%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwOCIgaGVpZ2h0PSI4NjUuMDY3Nzk2NjEwMTY5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

终端​

终端窗口是开发者与扣子 AI 编程环境进行交互的开发工具，是融合了 AI 能力的命令行窗口，兼容传统终端的命令操作。该区域还提供了控制台、输出和运行记录页签，可用于查看项目前后端的输出信息。​

​

特性​| 说明​| 示例​  
---|---|---  
执行命令行​| 终端支持开发者熟悉的基础命令执行能力，适配多开发场景的基础操作需求。​

  * 支持系统与开发相关的常规命令：比如执行npm install安装项目依赖、python run app.py启动后端服务等，与本地终端操作逻辑一致，降低开发者上手成本。​

  * 适配多环境命令解析：无论是前端的构建命令npm run build、后端的数据库连接命令，还是移动端的打包命令等，都能正常执行并在输出区域中实时打印日志，同时日志中会高亮标注错误信息，方便快速定位问题。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271312%27%20height=%27856.135593220339%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMxMiIgaGVpZ2h0PSI4NTYuMTM1NTkzMjIwMzM5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
查看前端控制台输出​| 对于网页应用，你可以在控制台区域查看前端控制台输出的日志信息，支持清空和过滤，便于快速定位问题。控制台日志也会同步打印到日志文件，以供扣子 AI 读取并自动修复问题。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271311%27%20height=%27577.728813559322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMxMSIgaGVpZ2h0PSI1NzcuNzI4ODEzNTU5MzIyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
查看服务端输出​| 在输出区域查看服务端打印的日志信息，包括安装依赖、服务启动、运行过程等信息。服务端日志也会同步打印到日志文件，以供扣子 AI 读取并自动修复问题。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271044%27%20height=%27778.5762711864406%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA0NCIgaGVpZ2h0PSI3NzguNTc2MjcxMTg2NDQwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看运行记录​| 开发智能体和工作流时，在右侧工作区的每一次试运行和调试记录都会被自动保存到工作区下方的运行记录中，你可以找到指定记录，查看各个节点的运行状态、输入输出数据等详细信息，便于对智能体和工作流进行问题排查。 ​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27165%27%20height=%27135%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY1IiBoZWlnaHQ9IjEzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
AI 解释​| 终端支持与对话区联动，在遇到命令执行结果不明确时，你可以将终端区域中的命令回显等信息引用到对话中，让扣子 AI 来解释含义，辅助操作。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271921%27%20height=%27870.9618644067797%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyMSIgaGVpZ2h0PSI4NzAuOTYxODY0NDA2Nzc5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

文件树​

文件树用于可视化展示项目目录结构，开发者可通过文件树查看扣子编程生成的代码文件。在扣子 AI 编程环境右上角单击文件夹图标，即可打开文件树区域。你可以在文件树区域执行以下操作：​

​

操作​| 说明​| 示例​  
---|---|---  
管理文件及文件夹​| 

  * 手动管理：你可以在终端中执行命令行来创建、删除、重命名文件或文件夹，实现对项目文件的灵活管理。​

  * 通过 AI 对话：你也可以将代码文件的管理操作交给扣子 AI，通过对话的方式让扣子 AI 为你管理项目文件或文件夹，例如创建、删除、重命名等基础操作。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271296%27%20height=%27851.1864406779662%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI5NiIgaGVpZ2h0PSI4NTEuMTg2NDQwNjc3OTY2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271906%27%20height=%27848.0084745762712%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwNiIgaGVpZ2h0PSI4NDguMDA4NDc0NTc2MjcxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
导出项目​| 你可以在文件树右上角单击下载图标，一键下载项目代码的压缩文件。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27141%27%20height=%27146%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQxIiBoZWlnaHQ9IjE0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
上传文件​| 你可以拖拽上传本地文件，也可以拖拽方式移动文件、调整目录结构。​也可以单击上传图标，并选择本地文件来上传文件。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27138%27%20height=%27129%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM4IiBoZWlnaHQ9IjEyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
检索代码​| 一站式检索，检索范围为整个项目的所有代码文件。支持的检索方式如下：​

  * 关键词检索：根据关键词检索，可设置区分大小写、模糊或完全匹配。​

  * 正则匹配：根据正则表达式进行匹配。​

如果检索结果过多，可以通过包含的文件和排除的文件进行二次筛选。​说明对于大型、复杂项目，检索代码可能耗时较久，建议通过多种筛选条件进行精确搜索，提高检索效率。​​| ​  
  
​

相关信息​

全局设置​

在扣子 AI 编程环境的右上角单击设置图标，可以调整编辑器、对话区等区域的显示设置、主题风格、字体大小等参数，提升开发体验。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27661%27%20height=%27297%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYxIiBoZWlnaHQ9IjI5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置说明如下：​

​

类型​| 设置​| 说明​  
---|---|---  
编辑器设置​| 编辑器主题​| 编辑器的主题会影响代码编辑器中的代码高亮风格。​目前支持 VSCode、GitHub、Duotone 主题。​如果你想设置扣子 AI 编程环境的整体主题，可以在页面右上角单击主题图标，设置整体 UI 主题，例如亮色或暗色模式。​  
​| 字体设置​| 编辑器字体相关的设置。​

  * 字形：选择代码编辑器中用于显示文本的字体。​

  * 字体大小：设置代码编辑器中字体的大小。​

  * 行高：设置代码编辑器中文字的行高。​

  
​| 代码编辑行为​| 编辑代码时可用的高级设置。包括：​

  * 自动补全：控制是否启用代码自动补全功能。开启后，在您输入代码时编辑器会自动提供补全建议。​

  * 括号自动闭合：控制是否自动闭合括号和引号。开启后，当您输入 (, [, {, ', " 等起始符号时，编辑器会自动补全对应的结束符号。​

  * 制表符大小：设置按下 Tab 键时缩进的空格数量。​

  
对话区设置​| 消息显示​| 在多轮对话中，如果对话数据量大，每次上滑鼠标查看历史对话时，系统会自动分段加载处理。分段加载数量用于设置每次加载的回复数量。​  
​| 上下文管理​| 设置触发自动压缩的上下文长度阈值。当上下文长度达到模型上限的一定比例时，将自动触发压缩。​  
高级设置​| 调试模式​| 开启或关闭调试模式。排障场景下建议开启，可以在对话区查看每一轮对话的 LogID 和调试日志，便于扣子团队帮助你排查问题。​  
  
​

编辑器快捷键​

在扣子 AI 编程环境中，常用快捷键能帮助开发者更高效地操作，目前支持的常用快捷键如下：​

​

快捷键​| 功能​  
---|---  
Option + B​| 切换文件目录可见性​  
Ctrl + `(反引号)​| 切换底部面板可见性​  
Option + N​| 打开新标签页​  
Option + W​| 关闭当前文件​  
cmd+f、ctrl+f​| 检索代码​  
  
​

​

上一篇

查看日志和 Trace

下一篇

版本控制