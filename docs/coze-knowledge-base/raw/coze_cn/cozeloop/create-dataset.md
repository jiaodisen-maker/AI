---
source_url: https://docs.coze.cn/cozeloop/create-dataset
title: '管理评测集 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:21Z
---

# 管理评测集 - 文档 - 扣子

管理评测集

在评测场景中，评测集是一个精心设计的标准化测试数据集，用于系统化地评测 AI Agent 的性能。评测集通常包含输入样本和预期输出。输入样本作为评估对象的输入数据，预期输出提供了评估基准。在开始执行评测实验前，需要先准备好评测集。本文指导你在扣子罗盘中创建和管理评测集。​

评测集介绍​

评测集是用于评测评估对象的一组数据。它通常包含输入数据和预期的输出结果，帮助开发者验证评估对象的效果。​

对于评测集中通常包含以下列：​

  * 输入数据（input）：这些是提供给评测对象的标准化测试样本，用于评测 AI Agent 在不同场景下的表现。​

  * 预期输出（reference_output）：这些是理想的结果，作为评估基准，帮助评估者或评估器对输出做出判断。​

  * 实际输出（actual_output）：评测对象的实际输出，通常用于线上 Trace 数据回流场景。​

评测集限制​

设计评测集之前，你需要了解评测集文件的以下限制：​

  * 最多可添加 5000 条测试数据，文件大小限制为 200 MB。​

  * 本地上传的 CSV 文件仅支持 UTF-8 编码格式。​

  * 最多添加 50 个自定义列。​

评测集设计原则​

设计评测集的用户问题时，应注意：​

  * 确保核心链路通畅：评测集需要覆盖 AI Agent 的各个功能点，尽量模拟真实的用户交互、设计典型对话，以确保 AI Agent 的表现符合产品设计和业务需求。 ​

  * 评估范围全面：评测集应该包含不同难度、不同领域的数据，以便全面评估模型的性能。如果包含多种任务，需要确保各个类别之间的数据量均衡，保证每种任务都有足够的样本数据。​

  * 覆盖极端场景和异常输入：尝试通过评测集识别出 AI Agent 响应质量不符合预期的场景，同时也需要模拟异常输入、超限输入、违规输入的情况，判断 AI Agent 在各种场景下是否都可以按照预期执行任务。​

  * 确保覆盖异常案例：对于用户反馈不合理的 AI Agent 响应案例，将其添加到测试集中，确保 AI Agent 的新版本已解决这些问题，可以按预期执行任务。​

构建评测集​

评测集构建包含创建评测集和添加测试数据两个操作。​

步骤一：创建评测集​

参考以下步骤，创建评测集。扣子罗盘支持 本地上传 和 手动导入 两种方式来创建评测集。当前步骤介绍 手动导入 的方式。关于 本地上传 的方式，详情参见 ​导入和导出评测集。​

1.

登录 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择评测 > 评测集，然后把鼠标移动到 \+ 新建评测集 按钮上，在下拉菜单中单击 +新建评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273786%27%20height=%271316.6768149882903%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc4NiIgaGVpZ2h0PSIxMzE2LjY3NjgxNDk4ODI5MDMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

3.

在新建评测集页面，参考以下信息配置评测集的数据列信息。单击 +添加列 可以添加自定义列。数据列信息配置完成后，单击创建。​

  * ​

配置项​| ​| 说明​  
---|---|---  
基本信息​| 名称​| 输入一个评测集名称。​  
​| 描述​| 提供一个评测集描述。​  
配置列​| 选择场景一键快速配置​| 你可以选择以下场景。本文仅介绍理想输出评测集的场景。​
    * 理想输出评测集：（默认）用于评测 LLM 或 AI Agent 实际输出与预期结果的匹配程度。​
    * 工作流评测集：用于评测扣子工作流。详情参见 ​评测扣子工作流。​
    * 轨迹评测集：用于评测 AI Agent 的轨迹（Trajectory）。详情参见 ​通过数据回流评测行程规划 Agent 的轨迹。​  
​| input​| 指定输入样本列配置：​
    * 名称：输入列名称。必须以英文字母开头，支持添加字母、数字和下划线。​
    * 数据类型：选择一种数据类型。通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。​
    * 查看格式：选择一种渲染评测数据的格式，提高数据的可读性和维护性。​
    * 描述信息：提供描述信息，帮助评测对象理解这个输入数据。​  
​| reference_output​| 指定数据集中期望输出列配置：​
    * 名称：输入列名称。必须以英文字母开头，支持添加字母、数字和下划线。​
    * 数据类型：选择一种数据类型。扣子罗盘通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。关于评测集数据类型的详细说明，可参考​评测集数据类型。​
    * 查看格式：选择一种渲染评测数据的格式，提高数据的可读性和维护性。​
    * 描述：提供预期输出的补充信息，可作为评估时的参考标准。​  
  
​

  * 系统会根据指定的数据列配置创建一个草稿版本的评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272354%27%20height=%271152.9093567251462%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM1NCIgaGVpZ2h0PSIxMTUyLjkwOTM1NjcyNTE0NjIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

步骤二：添加测试数据​

接下来，就可以在已创建的评测集中添加数据了。扣子罗盘支持 本地上传、手动导入 和 智能合成 三种方式来添加测试数据。当你需要批量上传测试数据时，选择本地上传方式。​

说明

本文档以文本数据为例。关于多模态数据，参阅 ​向评测集添加多模态数据 。​

​

手动添加

本地上传

智能合成

1.

在评测集详情页面，选择添加数据 > 手动添加来添加测试数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272900%27%20height=%271530.168269230769%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwMCIgaGVpZ2h0PSIxNTMwLjE2ODI2OTIzMDc2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在添加数据页面，输入第一组测试数据，然后单击 \+ 添加数据项添加更多测试数据。最后，单击添加完成数据添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27529%27%20height=%27434%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI5IiBoZWlnaHQ9IjQzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

修改评测集​

修改评测集基础信息​

  * 方法一：在评测集列表页面，选中目标评测集，然后单击修改来修改评测集的名称和描述。​

  * 方法二：在评测集详情页面，单击评测集名称旁边的编辑图标修改评测集名称和描述。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27518%27%20height=%27104%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE4IiBoZWlnaHQ9IjEwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

修改数据列​

你可以在评测集草稿状态下，修改评测集的列配置。​

在评测集详情页面，单击编辑列。然后，在列配置页面，删除、增加列或修改列的数据类型。​

注意

仅当评测集草稿数据为0时，方可修改数据类型。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272382%27%20height=%27595.5%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM4MiIgaGVpZ2h0PSI1OTUuNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

修改评测集数据​

你可以在评测集草稿状态下，修改评测集数据。​

说明

草稿版本的评测集数据修改不影响已提交的历史版本。如果历史版本的评测集关联了实验，也可以根据历史版本的实验回溯原版本数据。​

​

  * 新增数据项：在评测集详情页面，单击添加数据。详细说明参考​步骤二：添加测试数据。​

  * 修改数据项：在评测集详情页面，单击目标数据项操作列下的编辑，然后修改数据并保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27613%27%20height=%27151%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEzIiBoZWlnaHQ9IjE1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 删除数据项：​

  * 单条删除：在评测集详情页面，单击目标数据项操作列下的删除，即可删除该条数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272368%27%20height=%27538.1818181818181%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2OCIgaGVpZ2h0PSI1MzguMTgxODE4MTgxODE4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 批量删除：评测集详情页面，先单击批量操作，然后选择要删除的数据项，再单击删除即可删除所选数据项。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27577%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc3IiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

管理评测集版本​

评测集提供了版本管理能力，用于满足数据驱动型团队持续迭代评测数据以提高数据质量。​

评测集创建后默认为草稿状态。在不同评测阶段，测试集的版本作用也不同：​

  * 数据完备阶段：完成测试数据导入后，可提交首个测试版本并关联实验任务，系统将基于该版本进行全量评估。​

  * 评估验证阶段：通过实验报告分析当前版本的数据表现，定位待优化数据样本。​

  * 优化升级阶段：根据评估结果修正数据集后，提交升级版本并重新关联实验，开启新一轮验证循环。​

这种版本机制通过"提交-评估-优化"的递进式循环，确保评测集持续满足评估迭需求。​

新建评测集版本​

1.

在添加测试数据后，单击提交新版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272390%27%20height=%271072.704678362573%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM5MCIgaGVpZ2h0PSIxMDcyLjcwNDY3ODM2MjU3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在弹出的对话框内容，确认版本号后，再单击提交。​

查看评测集历史版本​

在评测集详情页，单击历史版本。版本记录区域会显示全部已提交的版本，单击一个目标历史版本，就可以切换到该评测集的历史版本。​

说明

不支持修改历史版本的测试集数据。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272368%27%20height=%271294.7836257309941%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2OCIgaGVpZ2h0PSIxMjk0Ljc4MzYyNTczMDk5NDEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

导入和导出评测集​

扣子罗盘支持将 Trace 数据手动沉淀到评测集。通常情况下，回流到评测集中的数据还需要经过二次处理，例如将线上真实的高质量问答对数据，沉淀为基准评测集；将评测分数低、耗时长、耗费 Token 多、应用输出不符合预期等类型的 Badcase，分类沉淀为问题数据集。​

在这种场景下，你需要先把整个评测集导出到本地文件，经过二次处理后再把文件导入为评测集。​

把本地文件导入为评测集​

说明

在上传文件时，请遵循以下限制：​

  * 支持格式：.csv、.xlsx、.xls、.jsonl、.zip（.zip 文件用于多模态评测集，详情参见 ​向评测集添加多模态数据）。​

  * 文件数量：一次只能导入一个文件。​

  * 文件大小：最大 500 MB。​

  * 数据条数：最多 5000 条。​

  * 自定义列：最多 50 个。​

  * 编码要求：CSV 文件仅支持 UTF-8 编码。​

​

1.

登录 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择评测 > 评测集，然后把鼠标移动到 \+ 新建评测集 按钮上，在下拉菜单中单击 +新建评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273340%27%20height=%271302.3653395784543%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM0MCIgaGVpZ2h0PSIxMzAyLjM2NTMzOTU3ODQ1NDMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

3.

在 导入本地文件 页面的 上传文件 区域，单击上传区域上传或直接把文件拖拽到上传区域。为确保数据格式正确，建议你先单击 下载模版，并按照模版文件的格式整理数据后再上传。文件上传完成后，扣子罗盘会自动填充评测集名称、各个列名称和数据类型。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272424%27%20height=%271473.1334894613583%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQyNCIgaGVpZ2h0PSIxNDczLjEzMzQ4OTQ2MTM1ODMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

4.

在 导入本地文件 页面的 基本信息 区域，输入评测集的名称和描述，并确认 配置列 区域的预览信息。确认无误后，单击 创建并导入。​

  * 注意

扣子罗盘默认会把多模态和轨迹的 数据类型 填充为 String，因此：​

    * 对于多模态数据，你必须手动把 数据类型 设置为 多模态。​

    * 对于轨迹数据，你必须手动把 数据类型 设置为 轨迹。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27798%27%20height=%27726%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzk4IiBoZWlnaHQ9IjcyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

等待几秒钟后刷新页面。你可以看到已经被导入的数据项。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273330%27%20height=%27828.6458333333334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzMCIgaGVpZ2h0PSI4MjguNjQ1ODMzMzMzMzMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

数据内容确认无误后，单击右侧的 提交新版本 按钮。在弹出的窗口中，输入版本号和版本说明，然后单击 提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273346%27%20height=%271452.2569444444446%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM0NiIgaGVpZ2h0PSIxNDUyLjI1Njk0NDQ0NDQ0NDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

把评测集导出为本地文件​

1.

登录 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择评测 > 评测集。​

3.

找到你需要导出的评测集。在 操作 列单击 详情。​

4.

在评测集的详情页，单击右侧的 ... 按钮，在下拉菜单中选择需要导入的文件格式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273330%27%20height=%27855.6249999999999%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzMCIgaGVpZ2h0PSI4NTUuNjI0OTk5OTk5OTk5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在弹出的窗口中，选择需要导出的评测集版本，然后单击 导出。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273316%27%20height=%271174.4166666666667%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMxNiIgaGVpZ2h0PSIxMTc0LjQxNjY2NjY2NjY2NjciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

6.

文件导出完成后，在右上角的弹窗中单击 下载文件 把文件下载到本地。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273310%27%20height=%27854.3171296296297%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMxMCIgaGVpZ2h0PSI4NTQuMzE3MTI5NjI5NjI5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

后续操作​

新建实验​

你可以在评测数据构建完成并提交版本后，直接从评测集发起实验进行评测。​

在评测集详情页，单击 \+ 新建实验。关于实验的配置过程，参考​管理实验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27560%27%20height=%27145%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYwIiBoZWlnaHQ9IjE0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

关联实验​

关联实验模块提供了一个聚合视图，展示与同一评测集关联的所有评测实验。你可以在此页面查看当前实验列表中各个实验在不同评估器指标下的得分。​

如果需要更深入的对比分析，你可以选择多个实验并发起实验对比，以获得详细的比较结果和洞察。该方式可以帮助你更好地理解实验之间的差异和性能表现，从而支持更精准的优化和决策。详情请参考​多实验对比。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272360%27%20height=%271400.8187134502923%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2MCIgaGVpZ2h0PSIxNDAwLjgxODcxMzQ1MDI5MjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

相关信息​

评测集数据类型​

创建评测集时，你需要为每个字段设置数据类型，扣子罗盘通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。​

目前扣子罗盘评测集支持以下常见类型的数据字段：​

​

数据类型​| 说明​| 示例​  
---|---|---  
string​| 字符串，可用于存储任何数据类型。​| "helloworld"​  
int​| 整数，等同于 int64。​| 1​  
float​| 浮点数，等同于 float64。​| 1.23​  
boolean​| 布尔值。​| true​  
Object​| 对象数据类型，典型适用场景包括：​

  * 评测对象有相对固定的 IDL（接口定义语言）。​

  * 线上 Trace 回流时，需要确保流入评测集的数据的规整，避免数据污染。​

  * 配置实验时，需要下钻到 Object 对象的某个内部字段。​

| ​JSON复制{​ "content": "hello world",​ "user_name": "alice"​}​​  
Array​| 数组数据类型，数组内部的 Item 类型支持设置为：​

  * String​

  * Int​

  * Float​

  * Boolean​

  * Object​

| [1,2,3,4,5]​  
多模态​​| 多模态数据类型，可以是图片、音频或视频，也可以是文字、图片、音频与视频的混合。​多模态类型的字段固定为 Array<Object> 类型。参阅 ​向评测集添加多模态数据 。​| ​JSON复制[​ {​ "type": "text",​ "text": "What is in this image?"​ },​ {​ "type": "image_url",​ "image_url": {​ "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"​ }​ }，​ {​ "type": "audio_url",​ "audio_url": {​ "url": "https://example.com/audio"​ }​ }，​ {​ "type": "video_url",​ "video_url": {​ "url": "https://example.com/video"​ }​ }​]​​  
轨迹​| 轨迹（Trajectory）数据类型。​轨迹是指 AI Agent 在任务执行过程中生成的结构化时序数据，数据格式为 JSON。轨迹完整记录了从接收用户指令开始，Agent 在多轮交互中进行的思考、行动和观察的全链路历史。详情参见 ​通过数据回流评测行程规划 Agent 的轨迹。​| 详情参见 ​通过数据回流评测行程规划 Agent 的轨迹。​  
  
​

​

​

上一篇

评测入门教程

下一篇

向评测集添加多模态数据