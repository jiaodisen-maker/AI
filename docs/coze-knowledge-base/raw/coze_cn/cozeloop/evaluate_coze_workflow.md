---
source_url: https://docs.coze.cn/cozeloop/evaluate_coze_workflow
title: '评测扣子工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:55Z
---

# 评测扣子工作流 - 文档 - 扣子

评测扣子工作流

本文档介绍在扣子罗盘中评测扣子工作流的操作步骤。​

功能概述​

在扣子罗盘评测工作流时，你可以将工作流的线上 Trace 数据回流为评测集，也可以本地上传构造好的 CSV 文件、或者手动逐条创建评测数据。扣子罗盘会调用扣子​执行工作流 OpenAPI 来获取工作流的输出结果，指定的评测集会作为 API 的请求参数。​

场景描述​

例如，你搭建了一个抖音爆款文案创作的工作流，希望验证该工作流生成的文案是否具有创造性和独特性。本文将演示如何通过评测集、LLM 评估器和实验来对该工作流进行评测。​

前提条件​

  * 工作流已经过完善的试运行、调试，并已成功发布。​

  * 确保当前账号仍有足够的免费评测额度，或余额充足。​

  * 仅支持资源库中的工作流评测，暂不支持评测扣子应用工作流。​

操作步骤​

步骤一：准备评测集​

在评测场景中，评测集是一个精心设计的标准化测试数据集，通常包含输入样本和预期输出（可选）。输入样本作为评估对象的输入数据，预期输出提供了评估基准。在工作流评测中，准备评测集的本质是在构造​执行工作流 OpenAPI 的请求数据，以便扣子罗盘成功调用 API 获取工作流的执行结果。你需要先新建评测集并声明​执行工作流 OpenAPI 请求的数据结构，再将构造好的请求数据上传至评测集。​

工作流评测集要求​

  * 必须存在一个 Object 类型的字段，建议命名为 parameter。其中包含工作流开始节点定义的输入参数，尤其是必选参数；参数字段名称必须与工作流开始节点的变量名称完全匹配。​

  * 如果工作流输入参数为 Image 等类型的文件，可以直接使用公开可访问的文件 URL。​

  * 输入样本的数据类型应和工作流开始节点的变量类型匹配，同样地，输出样本的数据类型也应和结束节点的变量类型匹配。​

  * 如果工作流开始节点的输入参数是 Object 类型，还需要在评测集样本中增加对应的子字段。​

1 创建评测集​

1.

登录[扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择一个工作空间。​

2.

在左侧导航栏，选择评测 > 评测集，然后单击 \+ 新建评测集。​

3.

在新建评测集页面，填写评测集名称和描述。​

4.

在配置列区域右侧，选择 Coze 工作流。​

  * 该操作可一键将评测集的列调整为兼容执行工作流 OpenAPI 的数据格式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27455.2204176334107%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ1NS4yMjA0MTc2MzM0MTA3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

5.

填写配置列，声明执行工作流 OpenAPI 请求的数据结构，并单击创建。​

  * 参考以下信息配置评测集的输入数据列和输出列信息。创建成功后，系统会根据指定的数据列配置创建一个草稿版本的评测集。​

  * ​

列名​| 配置说明​  
---|---  
parameter​| 工作流开始节点的输入参数，你可以在指定工作流的编排页面查看参数列表。parameter 必须为 Object 格式，且必须包含所有必选参数、参数名称与类型和工作流完全一致。​你可以在数据结构区域中单击 + 字段来新增输入参数，也可以导入一段 JSON 样例，扣子罗盘会自动解析 JSON 中的字段。如何为 parameter 构造 JSON 样例，并导入样例数据，可参考​配置列如何导入样例数据？。​  
bot_id​| 工作流需要关联的智能体 ID。部分工作流执行时需要指定关联的智能体，例如存在数据库节点、变量节点等节点的工作流。​  
ext​| 用于指定一些额外的字段，例如某些插件会隐式用到的经纬度等字段。目前仅支持latitude、longitude 和 user_id。​  
app_id​| 该工作流关联的应用的 ID。部分工作流执行时需要指定关联的应用，例如存在数据库节点、变量节点等节点的工作流。​  
reference_output​| 预期理想输出，可作为评估时的参考标准。​  
  
​

  * 工作流设计：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27127%27%20height=%27105%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI3IiBoZWlnaHQ9IjEwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

parameter 列配置：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27124%27%20height=%27120%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI0IiBoZWlnaHQ9IjEyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2 准备评测数据​

  * 方式一：将 Trace 数据回流至评测集​

  * 基于扣子罗盘支持的工作流 Trace 观测能力，你可以将 Workflow Trace Log 中的请求数据（调试日志、线上真实日志）回流到评测集中，作为回归测试数据。关于数据回流的详细说明，可参考​Trace 数据回流。​

  * 此方式适用于对线上 BadCase 进行回归测试的场景。关于如何通过 Trace 数据识别 BadCase，可参考​Trace 自动评测。​

a.

检索出工作流日志。​

  * 在观测 > Trace 页面，设置过滤条件，检索出扣子工作流日志。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271665%27%20height=%27443%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY2NSIgaGVpZ2h0PSI0NDMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

b.

添加到评测集。​

  * 点击添加到评测集，选择需要回流的 Trace Span 节点，再次确认添加到评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271726%27%20height=%27465%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcyNiIgaGVpZ2h0PSI0NjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271681%27%20height=%27493%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY4MSIgaGVpZ2h0PSI0OTMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

c.

查看评测集样本 Span，配置映射的字段。​

  * 注意应确保字段映射中，左值 Span 变量的数据结构能够对应右值评测集列的数据结构，否则评测集将会根据​1 创建评测集时声明的校验规则（如字段必填）将不符合数据规范拦截下来。这可以帮你规范化评测集，过滤掉 Trace Log 中的噪音数据，避免在后续评测中引入额外的 Token 成本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27480%27%20height=%27274%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgwIiBoZWlnaHQ9IjI3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

点击预览并校验，查看回流到评测集后的效果。​

  * 进入预览页面​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271369%27%20height=%27972%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM2OSIgaGVpZ2h0PSI5NzIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看预览数据​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27365%27%20height=%27267%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY1IiBoZWlnaHQ9IjI2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

e.

单击开始导入。​

f.

进入此评测集的详情页，即可看到测试数据已经被成功回流至草稿版本，单击提交新版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27532%27%20height=%27157%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMyIiBoZWlnaHQ9IjE1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 方式二：本地上传​

  * 如果你之前曾使用工作流的 API，平时在本地积累了一些调用 API 的测试数据，则可以将此类数据作为基础评测集，用于工作流每轮迭代前的准出基准评测集。​

a.

本地准备测试数据，并导出为 CSV 文件。​

  * 列名与评测集列名对应，每列下每个单元格中的数据格式，对应你在​1 创建评测集中声明的工作流 API 请求数据结构一致。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27132.2505800464037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjEzMi4yNTA1ODAwNDY0MDM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

b.

在评测集详情页面选择添加数据 > 本地导入，导入评测集，配置列映射。左侧为评测集列，右侧为 CSV 列。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27410.67285382830624%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQxMC42NzI4NTM4MjgzMDYyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 方式三：手动添加​

  * 在 parameter 中输入工作流开始节点的输入参数名称和待测试的参数值。目前 Object 仅支持 JSON 模式手动添加数据，您可以通过单击字段补全 ，快速添加数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27455.91647331786544%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQ1NS45MTY0NzMzMTc4NjU0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：准备评估器​

在评测过程中，评估器充当裁判的角色，通过量化评测对象的输出结果来评估其表现。在发起评测实验前，至少要创建一个评估器。在执行评测实验时，评估器会根据 Prompt 中预设的标准和规则对评估对象的输出进行打分，并提供得分原因。得分范围从 0.0 到 1.0，1.0 表示完全满足评分标准，0.0 表示完全不满足评分标准。​

1.

在左侧导航栏选择评测 > 评估器，单击 \+ 新建评估器 > LLM评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27164.58333333333334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE2NC41ODMzMzMzMzMzMzMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在评估器模板页面，扣子罗盘提供了多个预置的模板，如果没有合适的模板，你也可以单击自定义创建LLM评估器创建评估器。​

  * 在本场景中，你需要评估爆款文案创作助手的创造性，因此选择创造性模板，单击应用。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27430.85846867749416%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQzMC44NTg0Njg2Nzc0OTQxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

修改评估器的名称和模型，单击调试，测试一下评估器效果。​

  * 说明

在调试评估器时，会产生 Token 消耗。​

​

4.

单击创建，单击提交新版本。完成评估器创建并提交评估器版本。​

  * 说明

在创建评测实验时，只能使用已提交的评估器。​

​

步骤三：创建评测实验​

在准备好评测集和评估器后，就可以发起实验来测试扣子工作流。每次评测实验仅支持评测一个工作流的一个指定版本，如需对比多个工作流版本，需要分别创建评测实验。​

1.

在左侧导航栏，选择评测 > 实验，然后单击 \+ 新建实验。​

2.

输入一个实验名称，然后单击下一步: 评测集。​

3.

选择已创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27450.3480278422274%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ1MC4zNDgwMjc4NDIyMjc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

配置评测对象，配置完成后单击下一步：评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27444.7795823665893%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ0NC43Nzk1ODIzNjY1ODkzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * ​

配置​| 说明​  
---|---  
类型​| 评测对象的类型，此处应选择 Coze 工作流。​  
工作流名称​| 选择待评测的工作流，仅支持选择当前工作空间资源库内已发布的工作流，不支持对话流。​  
版本​| 指定工作流待评测的版本。​仅支持评测发布版本，不支持评测草稿版本或提交版本。​  
字段映射​| 配置评测对象和评测集的字段映射关系。​
    * parameter：工作流开始节点的输入参数。此处必须选择一个 Object 格式的字段，扣子罗盘会自动解析其中的子字段，并根据字段名一一映射为工作流的输入参数。​
    * bot_id：工作流需要关联的智能体 ID。 部分工作流执行时需要指定关联的智能体，例如存在数据库节点、变量节点等节点的工作流。​
    * ext：用于指定一些额外的字段，例如某些插件会隐式用到的经纬度等字段。目前仅支持latitude、longitude 和 user_id。​
    * app_id：该工作流关联的应用的 ID。部分工作流执行时需要指定关联的应用，例如存在数据库节点、变量节点等节点的工作流。​
说明工作流的所有必选输入参数均应映射到对应的评测集字段，否则评测实验可能执行失败。​​  
  
​

5.

单击添加评估器，选择已创建的评估器和版本，然后将评测集的字段、评测对象的实际输出与评估器的参数关联，确保评估器准确获取数据并执行评估，最后单击确认实验配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27450.3480278422274%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ1MC4zNDgwMjc4NDIyMjc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

6.

检查实验配置，确认无误后，单击发起实验。​

  * 发起实验后，你可以刷新实验页面，查看评估进度。​

步骤四：分析实验结果​

在评估器执行完所有评估任务后，你可以在实验页面查看实验报告。通过实验报告来判断评估对象是否符合预期。​

查看评测结果​

在数据明细页面，你可以查看评估器对每个测试数据的执行结果的评分，以及评分的具体原因。​

如果某个测试数据的评估器自动打分不准确，你可以将鼠标悬浮至评分上，然后点击出现的人工校准图标。在弹出的页面中输入修正的分数和原因。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27164.96519721577727%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE2NC45NjUxOTcyMTU3NzcyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看实验报告​

在实验详情页面，单击指标统计页签查看实验数据报告。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27457.87545787545787%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQ1Ny44NzU0NTc4NzU0NTc4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

配置列如何导入样例数据？​

扣子推荐你在配置评测集字段时，对于 parameter 等 Object 类型的字段，可以直接导入 JSON 格式的工作流的输入参数，提升评测集的构建效率。输入 JSON 之后，系统会自动解析字段，并以此定义评测集字段。操作方式如下：​

1.

获取 JSON 格式的工作流的输入参数。​

  * 在工作流编排页面单击试运行，开启 JSON 格式，并复制 “_input” 字段值。注意复制的 JSON 中只包含开始字段的参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27587%27%20height=%27284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg3IiBoZWlnaHQ9IjI4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

导入 JSON 样例，自动解析字段。​

  * 在新建评测集的页面，找到 Object 类型的字段（例如 parameter），单击导入样例数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271292%27%20height=%27916.1454545454545%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI5MiIgaGVpZ2h0PSI5MTYuMTQ1NDU0NTQ1NDU0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

将复制好的 JSON 填入样例区域，单击提取数据结构。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271330%27%20height=%27909.2363636363635%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMzMCIgaGVpZ2h0PSI5MDkuMjM2MzYzNjM2MzYzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看导入效果，并确认字段配置，例如字段名、数据类型、是否必选等。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271342%27%20height=%27917.4399999999999%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM0MiIgaGVpZ2h0PSI5MTcuNDM5OTk5OTk5OTk5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

评测多模态（视频）Agent

下一篇

评测扣子智能体