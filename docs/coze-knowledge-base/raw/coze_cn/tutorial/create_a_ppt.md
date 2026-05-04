---
source_url: https://docs.coze.cn/tutorial/create_a_ppt
title: '制作 PPT - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:59Z
---

# 制作 PPT - 文档 - 扣子

制作 PPT

本文档演示如何搭建生成 PPT 的低代码工作流，其核心在于支持生成及预览 PPT 缩略图，并确认用户满意生成效果后再返回可编辑的 PPTX 源文件。如果不满意，用户可重新输入 PPT 关键信息，再次生成 PPT。​

场景说明​

扣子编程提供的 [iSlide 插件](<https://www.coze.cn/store/plugin/7525010179218489379>)，融合了 AI 大模型与专业设计资源，能够大幅节省制作时间和精力，帮助用户轻松创建专业级的 PPT。本教程以生成大学生实习报告 PPT 为例，用户仅需输入 PPT 关键信息和模板偏好信息，即可通过运行工作流生成 PPT。首先，通过 iSlide 插件的 get_themes 工具筛选出所需的 PPT 模板。接着，通过 generate_outline 工具生成 PPT 大纲。然后，generate_presentation 工具会基于模板 ID 和 PPT 大纲生成 PPT 并返回缩略图 URL。​

整个工作流的重点在于通过循环节点实现了用户对生成效果的确认和重新生成环节，用户满意生成效果时，系统将运行 download_presentation 工具返回 PPTX 源文件，不满意则会提示用户重新输入 PPT 关键信息及模板信息，再次生成 PPT。生成的 PPTX 源文件可下载到本地，用于后续的编辑与使用。​

本教程的循环节点也为其他需要用户确认的场景提供了参考，例如在文生图场景中，由大模型生成图像生成的提示词后，可以先让用户确认，再执行图像生成操作。如果用户对生成的提示词不满意，则可以输入修改建议重新生成提示词。​

说明

download_presentation 工具为付费工具，每次调用将扣除 9900 资源点（9.9 元）。为避免产生不必要的费用，建议在工作流中添加确认节点，确认对生成的 PPT 完全满意后再执行 download_presentation 工具获取 PPTX 源文件。​

​

效果演示​

执行 PPT 生成工作流时，会展示 PPT 缩略图及询问用户是否满意当前生成效果。待确认满意后，返回可编辑的 PPTX 源文件。​

输出预览​

可以在低代码智能体中以卡片形式预览 PPT 缩略图。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27478%27%20height=%271049.861818181818%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/32374f70769d44729eae0da4cc0f0c75~tplv-goo7wpa0wc-quality:q75.image)​

​

确认节点​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27403%27%20height=%27194.90545454545455%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ab0c19cf6a144540aab73ad696942e58~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​

最终效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272546%27%20height=%271212.3809523809523%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/51c85bddc04c4846a743b45baab10389~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​

​

低代码工作流设计​

生成 PPT 工作流的设计方案说明如下：​

  * 工作流压缩包​

  * 你可以下载该压缩包，并将其导入到任意工作空间中以复用该工作流。具体操作，请参考​导入与导出低代码工作流。​

  * ​

​

Workflow-PPT-draft-4301.zip

​

​

  * 工作流设计说明​

a.

输入节点：传入 PPT 关键信息、搜索 PPT 模板的关键词和标签。在生成 PPT 工作流中，对工作流的运行对输入参数有较强的依赖，因此添加输入节点。例如在智能体中调用工作流时，运行到输入节点中会展示参数输入提示框，便于用户配置。​

b.

循环节点：循环获取 PPT 模板，生成 PPT 大纲和缩略图。用户满意则结束循环，不满意则重新生成 PPT。​

c.

提取最后一个任务 ID 节点：用户不满意 PPT 生成效果时，系统会循环重新生成 PPT。此时，循环节点输出的任务 ID 将是一个数组。因此，需要添加代码节点，提取数组的最后一个元素，即最后一次循环生成的任务 ID。​

d.

生成 PPTX 源文件节点：用户确认满意后，返回最终的 PPTX 源文件，支持下载到本地进行编辑与使用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%276158%27%20height=%271658.7445086705202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE1OCIgaGVpZ2h0PSIxNjU4Ljc0NDUwODY3MDUyMDIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

核心节点​

工作流的核心节点配置如下：​

​

节点名称​| 说明​| 示例​  
---|---|---  
开始节点​| 本教程无需设置开始节点。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27676%27%20height=%27207.78688524590166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc2IiBoZWlnaHQ9IjIwNy43ODY4ODUyNDU5MDE2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
输入 PPT 关键信息节点（输入节点）​| 输入 PPT 关键信息节点为输入节点，用于输入 PPT 关键信息和模板信息。如果在智能体中调用工作流，运行到输入节点时会展示输入提示框，引导用户配置相关的输入参数。而直接在开始节点设置输入参数，再在智能体中运行时不会提示输入框。​节点配置说明如下：​

  * 新增 topic 参数：输入 PPT 关键信息，用于生成 PPT 大纲。例如 生成一份大学生实习报告，展示工作成果与收获，包括实习公司介绍、实习工作、心得体会、未来展望等内容。​

  * 新增 theme_keyword 参数：输入 PPT 模板关键字，用于筛选模板。例如 实习总结、职业规划、工作报告，职业风。​

  * 新增 theme_tags 参数：输入 PPT 模板标签，用于筛选模板。例如 color.blue。​

| 

  * 节点配置​

  * ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27675%27%20height=%27320.90163934426226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc1IiBoZWlnaHQ9IjMyMC45MDE2MzkzNDQyNjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​

  * 智能体对话​

  * ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27419%27%20height=%27458.49590163934425%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE5IiBoZWlnaHQ9IjQ1OC40OTU5MDE2MzkzNDQyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​

  
循环节点​| 循环节点用于循环筛选 PPT 模板以及生成 PPT 大纲和缩略图，直到用户满意再停止循环，并输出 PPT 任务 ID。包括如下节点：​

  * 获取 PPT 模板节点（插件节点）​

  * 生成 PPT 大纲节点（插件节点）​

  * 生成 PPT 节点（插件节点）​

  * 展示 PPT 缩略图节点（输出节点）​

  * 确认节点（问答节点）​

  * 重新输入 PPT 关键信息节点（输入节点）​

  * 设置变量节点​

  * 终止循环节点​

循环节点配置说明如下：​

  * 循环设置​

  * 循环类型：选择指定循环次数。​

  * 循环次数：按需设置循环次数。​

  * 中间变量：用于在多次循环中传递变量。​

  * 新增 var_topic 变量：引用开始节点的输入参数 topic。​

  * 新增 var_theme_keyword 变量：引用开始节点的输入参数 theme_keyword。​

  * 新增 var_theme_tags 变量：引用开始节点的输入参数 theme_tags。​

  * 输出：引用生成 PPT 节点的输出参数historyId，设置为 Array<string> 类型。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27680%27%20height=%27635.4098360655738%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgwIiBoZWlnaHQ9IjYzNS40MDk4MzYwNjU1NzM4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
获取 PPT 模板节点（插件节点）​| 获取 PPT 模板节点为插件节点，调用 iSlide 插件的 get_themes 工具，用于根据输入的模板关键字和标签等信息，筛选 PPT 模板。​节点配置说明如下，参数详细说明请参考​get_themes 工具。​

  * keywords：引用循环节点的中间变量 var_theme_keyword。​

  * tags：引用循环节点的中间变量 var_theme_tags。​

  * 其他参数保持默认配置。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27678%27%20height=%27447.3688524590164%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc4IiBoZWlnaHQ9IjQ0Ny4zNjg4NTI0NTkwMTY0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
生成 PPT 大纲节点（插件节点）​| 生成 PPT 大纲节点为插件节点，调用 iSlide 插件的 generate_outline 工具，用于根据输入的 PPT 关键信息生成 PPT 大纲。​节点配置说明如下，参数详细说明请参考​generate_outline 工具。​topic： PPT 关键信息，引用循环节点的中间变量 var_topic。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27672%27%20height=%27280.91803278688525%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcyIiBoZWlnaHQ9IjI4MC45MTgwMzI3ODY4ODUyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
生成 PPT 节点（插件节点）​| 生成 PPT 节点为插件节点，调用 iSlide 插件的 generate_presentation 工具，基于 PPT 大纲和 PPT 模板 ID 生成 PPT，并返回 PPT 缩略图。​节点配置说明如下，参数详细说明请参考​generate_presentation 工具。​

  * outline： PPT 大纲 ID，引用生成 PPT 大纲节点的输出参数 data.id。​

  * themeId：PPT 模板 ID，引用获取 PPT 模板节点的输出参数 data.items.id。​

  * 其他参数保持默认配置。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27679%27%20height=%27361.17021276595744%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc5IiBoZWlnaHQ9IjM2MS4xNzAyMTI3NjU5NTc0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
展示 PPT 缩略图节点（输出节点）​| 展示 PPT 缩略图节点为输出节点，用于展示 PPT 缩略图。节点配置说明如下：​

  * 输出变量：引用生成 PPT 节点的输出参数 data.pages，设置为 Array<object> 类型。​

  * 输出内容：输入 {{output}}，用于输出缩略图相关信息。​

此节点可以和工作流卡片配合使用，用于展示 PPT 缩略图。​

1.在智能体中，单击该工作流的卡片图标，选择为展示 PPT 缩略图节点绑定卡片。​

2.在卡片配置页面，选择合适的卡片模板，设置卡片数据源。​

  * 本教程以官方卡片为例，为卡片绑定展示 PPT 缩略图节点的输出参数output。output 中包含三个字段 index（数组索引）、slideLayout（PPT 版式）和 thumbnail 字段（PPT 缩略图）。因此，为标题元素绑定 index 字段，为内容元素绑定 slideLayout 字段，为图片元素绑定 thumbnail 字段。本卡片模板最多展示 20 张 PPT 缩略图，你也可以自定义卡片。具体操作，请参考​卡片。​

| 

  * 节点配置​

  * ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27679%27%20height=%27422.9836065573771%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc5IiBoZWlnaHQ9IjQyMi45ODM2MDY1NTczNzcxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​

  * 绑定卡片​

  * ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271178%27%20height=%27360.8288288288288%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE3OCIgaGVpZ2h0PSIzNjAuODI4ODI4ODI4ODI4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​

  * ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271481%27%20height=%271116.8196721311474%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ4MSIgaGVpZ2h0PSIxMTE2LjgxOTY3MjEzMTE0NzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​

  
确认节点（问答节点）​| 确认节点为问答节点，用于询问用户是否满意生成的 PPT，满足则结束循环，不满意则重新输入 PPT 关键信息，重新生成 PPT 。节点配置说明如下：​

  * 模型：选择合适的模型，例如豆包·1.5·Pro·32k。​

  * 提问内容：设置为对生成的 PPT 是否满意？。​

  * 回答类型：选择选项回答。​

  * 选项内容：​

  * A：不满意，重新生成​

  * B：满意，直接下载​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27676%27%20height=%27963.6595744680851%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc2IiBoZWlnaHQ9Ijk2My42NTk1NzQ0NjgwODUxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
重新输入 PPT 关键信息节点（输入节点）​| 重新输入 PPT 关键信息节点为输入节点，当用户不满意 PPT 生成效果时，可以通过该节点重新输入 PPT 关键信息。节点配置说明如下：​

  * 新增 topic：输入 PPT 关键信息，用于生成 PPT 大纲。例如 生成一份大学生实习报告，展示工作成果与收获，包括实习公司介绍、实习工作、心得体会、未来展望等内容。​

  * 新增 theme_keyword：输入模板关键字，用于筛选模板。例如 实习总结、职业规划、工作报告，职业风。​

  * 新增 theme_tags：输入模板标签，用于筛选模板。例如 color.blue。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27683%27%20height=%27316.30737704918033%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgzIiBoZWlnaHQ9IjMxNi4zMDczNzcwNDkxODAzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
设置变量节点​| 设置变量节点用于重置循环变量的值，使其下次循环时使用重置后的值，即用户不满意 PPT 生成效果时，循环节点将根据重新输入的 PPT 关键信息生成 PPT。节点配置说明如下：​

  * 新增中间变量 1，引用循环节点的中间变量 var_topic，其值引用重新输入 PPT 关键信息节点的输入参数topic。​

  * 新增中间变量 2，引用循环节点的中间变量 var_theme_keyword，其值引用重新输入 PPT 关键信息节点的输入参数theme_keyword。​

  * 新增中间变量 3，引用循环节点的中间变量 var_theme_tags，其值引用重新输入 PPT 关键信息节点的输入参数theme_tags。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27674%27%20height=%27312.1393442622951%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc0IiBoZWlnaHQ9IjMxMi4xMzkzNDQyNjIyOTUxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
提取最后一个任务 ID 节点（代码节点）​| 提取最后一个任务 ID 节点为代码节点，用于提取最后一个 PPT 生成任务 ID。节点配置说明如下：​

  * 输入：新增input 参数，引用循环节点的输出参数 output，设置为 Array<string>类型。​

  * 代码：通过代码，提取 output 中的最后一个元素，即最后一个 PPT 生成任务 ID。​

  * ​JavaScript复制async function main({ params }: Args): Promise<Output> {​ // 构建输出对象​ const lastElement = params.input.length > 0 ​ ? params.input[params.input.length - 1] ​ : "";​ ret ={ lastElement}​ return ret;​}​​

  * 输出：新增 lastElement参数，用于输出最后一个 PPT 生成任务 ID，设置为 String 类型。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27677%27%20height=%27660.3524590163934%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc3IiBoZWlnaHQ9IjY2MC4zNTI0NTkwMTYzOTM0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
返回 PPTX 源文件节点（插件节点）​| 返回 PPTX 源文件节点为插件节点，调用 iSlide 插件的 download_presentation 工具，用于返回 PPTX 源文件，支持下载到本地进行编辑。​节点配置说明如下，参数详细说明请参考​download_presentation 工具。​ historyId 参数，表示 PPT 生成任务 ID，引用提取最后一个任务 ID 节点的输出参数lastElement。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27684%27%20height=%27283.1311475409836%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg0IiBoZWlnaHQ9IjI4My4xMzExNDc1NDA5ODM2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
结束节点​| 结束节点用于输出 PPTX 源文件 URL。节点配置说明如下：​

  * 输出模式：选择返回文本。​

  * 输出：定义变量 output，引用返回 PPTX 源文件节点的输出参数file。​

  * 回答内容：设置为 {{output}}，表示输出 PPTX 源文件 URL。​

说明file有效期 2 小时，请及时转存。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27678%27%20height=%27475.155737704918%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc4IiBoZWlnaHQ9IjQ3NS4xNTU3Mzc3MDQ5MTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

​

上一篇

动态设置大模型工具入参

下一篇

搭建漫画视频工作流