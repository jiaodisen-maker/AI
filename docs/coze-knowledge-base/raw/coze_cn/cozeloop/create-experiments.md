---
source_url: https://docs.coze.cn/cozeloop/create-experiments
title: '管理实验 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:32Z
---

# 管理实验 - 文档 - 扣子

管理实验

实验是指通过组合评测数据集、评测对象、若干评估器三元组，执行评测动作得到实验结果的过程。通过分析实验结果，可以获得有助于业务决策的信息。本文档指导你如何创建和启动评测实验。​

实验流程概述​

扣子罗盘支持的评估对象包括扣子罗盘中创建的 Prompt、扣子智能体等。你需要先准备评测集和评估器，然后才能发起评测实验。​

实验流程如下：​

1.

指定评测集：构建包含输入样本的数据集，可选择性地添加预期输出作为评估参考。​

2.

添加评测对象：选择需要评估的目标，并通过字段映射建立输入数据与评测对象的连接。评测对象将基于评测集的输入样本生成相应输出。​

  * 说明

对于扣子智能体，当前仅支持文本内容的评测。​

​

3.

添加评估器：配置至少一个评估器执行评测任务。扣子罗盘支持 LLM 和 Code 评估器，可自动对评测对象的输出进行多维度评估。​

4.

分析实验结果：实验完成后，通过详细的数据分析报告对评估对象进行效果验证和优化迭代。​

创建实验​

说明

在创建实验前，确保已​构建评测集。​

​

参考以下步骤，创建实验。​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择一个空间。​

2.

在左侧导航栏，选择评测 > 实验，然后单击 \+ 新建实验。​

  * 如下图所示，你也可以在评测集详情页面，单击 \+ 新建实验来创建时间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27606%27%20height=%27226%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d53e5674c1834d59b88dd2b7fec66707~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

填写基础信息。​

  * 输入实验名称和描述，然后单击下一步: 评测集。​

4.

选择评测集。​

  * 选择已创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27641%27%20height=%27324%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQxIiBoZWlnaHQ9IjMyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

（可选）配置评测对象。​

设置本次评测实验的评测对象，目前支持评测：​

  * 扣子罗盘创建的 Prompt​

  * 在扣子编程中创建的扣子智能体和扣子工作流​

  * 在扣子罗盘注册的火山智能体。​

  * 如果你希望将评测集作为评测对象，那么你可以直接跳过此步骤，不设置评测对象，在后续步骤配置评估器、设置评估标准时，指定你的评测集作为实际输出。这种方式创建的评估实验适用于 Trace 回流评测集的场景，可以针对线上已经产生的 Agent 实际输出进行评测。​

  * Prompt

Coze 智能体

Coze 工作流

火山智能体

    * 类型：选择评测对象类型，这里以 Prompt 为例。​

    * Prompt Key：从当前空间的 Prompt 列表中选择一个 Prompt Key。​

    * 版本：选择 Prompt 已提交的某个版本，表示对此版本发起评测。​

    * Prompt 详情：你可以展开 Prompt 详情，确认指定版本的 Prompt 内容。如果不符合需求，还可以单击查看详情，重新编写并提交一个新的 Prompt 版本。​

    * 字段映射：选择评测集中的哪列数据作为输入数据传递给评测对象。对于 Prompt 评测，无需选择映射的字段。​

    * 参数注入：配置评测 Prompt 时的模型与参数，以便来拿到指定模型配置下的输出结果。目前支持选择模型、设置最大回复长度和生成随机性等模型参数配置。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27306%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2IiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * 说明

如果评测对象、评估器中定义了多模态类型的变量，在配置评测对象与评估器的字段映射关系时，应注意数据类型匹配，均为多模态类型数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27205%27%20height=%27136%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA1IiBoZWlnaHQ9IjEzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

6.

（可选）设置评估器。​

  * 为评测实验设置评估器。​

  * 如果你没有准备评估器，扣子罗盘提供一系列预置评估器供你选择。如果没有合适的预置评估器，你也可以根据页面提示，基于评估器模板创建一个符合当前评测场景的自建评估器。​

  * 如果你希望由人工标注实验结果，那么也可以直接跳过此步骤，不设置评估器。评测实验运行完成后，人工查看评测数据并标注，操作步骤可参考​人工标注评测数据。​

  * 准备好评估器之后，参考以下步骤为评测实验设置评估器。​

a.

在4.评估器页签中选择已创建的评估器和版本。​

b.

将评测集的字段、评测对象的实际输出actual_output与评估器的参数关联，确保评估器准确获取数据并执行评估。​

c.

单击确认实验配置。​

  * 说明

    * 扣子罗盘支持在自建评估器中配置变量，详情请参考​创建 LLM 评估器。​

    * 如果评测对象是火山智能体，且你选择了可以对轨迹（Trajectory）进行评测的评估器，你可以在 字段映射 中把评估器的轨迹类型的字段映射到火山智能体的轨迹。详情参阅 ​轨迹评测介绍。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272732%27%20height=%271897.2222222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjczMiIgaGVpZ2h0PSIxODk3LjIyMjIyMjIyMjIyMjIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

7.

在页面底部，设置最大并发执行条数。​

  * 评测实验支持并发执行评测集中的条目，默认为 5 条，最大可设置为 50 条。这里你需要设置理想的最大执行条数，但实际生效的并发数受限于评测对象的并发度限制和调用评估器的模型 TPM 限制。​

8.

检查实验配置，确认无误后，单击发起实验。​

  * 发起实验后，你可以刷新实验页面，查看评估进度。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27566%27%20height=%27302%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY2IiBoZWlnaHQ9IjMwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

实验洞察：单实验分析​

通过单次实验报告，开发者可以通过「宏观」维度的指标统计，与「微观」视角的数据明细，分析洞察本次实验评测对象的效果，进而支撑业务决策。​

指标统计​

在指标统计页面，可查看聚合得分、得分分布。​

查看聚合得分​

  * 查看本次实验中，评测对象在各个评估指标上的聚合得分。​

  * 聚合方式：平均、最大、最小、求和。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27530%27%20height=%27284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMwIiBoZWlnaHQ9IjI4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看得分分布​

  * 查看本次实验中，评测对象的所有评测数据，在各个评估指标上的得分分布占比。​

  * 例如，10 条评测数据，在正确性指标得分如下图所示。一条 0.8 分，一条 0.6 分，一条 0.3 分，一条 0.5 分，其余为 1 分。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27530%27%20height=%27196%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMwIiBoZWlnaHQ9IjE5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 单击指标统计，查看正确性的得分分布。​

  * 说明

只统计 Top5 分数与占比情况，长尾得分归入其他。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27464%27%20height=%27226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY0IiBoZWlnaHQ9IjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

数据明细​

在数据明细页面，可调整页面展示、配置过滤器，并详细分析评测数据。​

可视化调整​

在列管理中，隐藏不关注的指标、视图调整（紧凑宽松视图切换）调整到方便分析的方式。​

搜索和过滤数据​

实验完成后，你可以在实验结果页面对实验结果进行模糊搜索和筛选。​

  * 通过筛选器，你可以基于统计指标中较差的指标、或者不符合预期的指标，通过过滤器筛选出来在目标指标上得分较低的 badcase。筛选范围是实验结果的所有列。​

  * 通过模糊搜索，你可以快速定位到匹配关键词的数据项，提高分析效率。目前模糊搜索的范围包括评测集的列数据、评测对象的输出、数据项的 ID。其中数据项的 ID 必须是完全匹配。​

说明

  * 搜索框和过滤器均支持通过 Shift+Enter 进行换行。​

  * 隐藏的列不在筛选或检索的范围内。​

​

对于 Object 和 Array 类型的数据，开发者上传的数据结构中可能会存在大量的空格、换行符和符号 { } [ ] : , 。扣子罗盘存储数据时，会保留 key、value 中的空格和换行符，移除评测集、实际输出列中的其他空格、换行符后再进行存储。所以在检索这些复杂结构时，你需要确保关键字和空格、回车等都完全匹配。例如：​

​

数据类型​| 原始结构示例​| 检索引擎存储内容​  
---|---|---  
Object​| ​Plain Text复制{​​​ "key1" ： "hello world",​ ​ "key2": "look"​}​​| ​Plain Text复制{"key1":"hello world","key2":"look"}​​  
Array​| ​Plain Text复制[​​​"hello world", "look"​]​​| ​Plain Text复制["hello world", "look"]​​  
  
​

分析评测数据​

查看并分析详细评测数据项，以优化评估过程：​

  * 分支1：查找评测对象的异常案例。​

  * 检查得分及其原因，人工核对评测集输入与实际输出，识别评估不准确的异常案例。​

  * 点击 actual_output 列下的输出内容旁边的 Trace 图标查看评测对象的 Trace 链路，结合 Trace 排查问题原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27565%27%20height=%27116%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY1IiBoZWlnaHQ9IjExNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 进入下一轮迭代优化​

  * 分支2：评估器评估不准确的异常案例。​

  * 检查得分及其原因，人工核对评测集输入与实际输出，识别评估器评估不准确的异常案例。​

  * 点击评估指标对应的 Trace 图标查看评估器的 Trace 链路，结合 Trace 排查问题原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27582%27%20height=%27163%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgyIiBoZWlnaHQ9IjE2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 人工校准得分​

  * 刷新数据明细页面，指标统计页面也会联动刷新。然后，再进行对比分析。​

通过单实验报告的分析，评估评测对象的整体表现，识别异常案例并进行问题排查定位，指导业务决策。​

实验洞察：多实验对比分析​

在真实的开发环境中，单实验分析可能无法满足需求。因为随着评测对象的迭代，常常会出现多个版本（例如多种 Prompt 优化策略）。开发者需要评估这些版本在目标指标上的优化情况，以及现有功能指标是否出现退化。​

为此，多实验对比分析功能为开发者提供：​

  * 控制变量的实验思路：保持评测集和评估器不变，针对评测对象的不同版本进行实验。​

  * 设置对照组（基准）和多个实验组（开发过程中可能通过调优产生了多个版本）。​

  * 提供指标统计和数据明细，帮助开发者从「宏观」角度对比多个实验的整体优劣，从「微观」视角比较每条评测数据在不同实验中的表现。​

发起对比​

你可以通过以下方式发起多实验对比。​

说明

仅关联了同个评测集（不区分版本）且已经达到稳态的实验（实验状态为成功、失败或中止）可以被发起多实验对比。​

​

方式一：在实验列表页面发起​

1.

在实验列表页面，单击批量选择。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27642%27%20height=%27167%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQyIiBoZWlnaHQ9IjE2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选择要对比的实验，然后单击实验对比。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27637%27%20height=%27156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM3IiBoZWlnaHQ9IjE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

方法二：在实验详情页发起​

1.

在实验列表页面，选择一个目标实验。​

2.

在实验详情页，单击实验对比。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27564%27%20height=%27257%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY0IiBoZWlnaHQ9IjI1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择要关联对比的实验，然后单击发起实验对比。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27554%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU0IiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

方法三：在评测集详情页发起​

1.

在评测集列表页面，选择一个目标评测集。​

2.

在评测集详情页，单击关联实验，然后单击批量选择。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27550%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTUwIiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择要对比的实验，然后单击实验对比。​

方法四：在多实验对比看板继续添加实验​

1.

在实验对比页面，单击 \+ 添加对比实验。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27492%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkyIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选择要对比的实验，然后单击发起对比实验。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27502%27%20height=%27231%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAyIiBoZWlnaHQ9IjIzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看指标统计​

指标统计提供了参与对比的实验的所有评估指标的综合看板，使开发者能够快速掌握多个实验的整体效果。​

  * 设置对照组（基准）​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27539%27%20height=%27317%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM5IiBoZWlnaHQ9IjMxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * （可选）可视化配置：隐藏暂不关心的评估指标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27542%27%20height=%27324%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQyIiBoZWlnaHQ9IjMyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 对比基准，查看实验组的效果，识别不符合预期的指标。​

  * 进入数据明细，洞察劣化指标。​

查看数据明细（行级对比）​

通过数据明细对比，开发者可以深入分析指标统计中存疑或感兴趣的指标项，对单条评测数据在不同实验中的表现进行详细对比。通过检查实际输出、评估器打分及其原因，验证宏观指标统计的准确性，从而得出多实验对比的结论，指导下一步的业务决策。​

  * 可视化配置：隐藏暂不关注评测集列、实际输出列、评估指标；调整视图紧凑型。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27230%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA0IiBoZWlnaHQ9IjIzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 筛选：通过过滤器筛选出低于某个指标分数线的评测数据项。​

  * 行级对比：​

  * 对比多个版本的评测对象在相同评测数据输入下的输出和表现。例如，指标得分、Token 消耗和时延。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%27229%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYzIiBoZWlnaHQ9IjIyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 数据明细除评测集数据外，还包括以下信息：​

  * 基准实验的评测集的数据项 ID 列​

  * 基准实验的评测集的列​

  * 基准实验结果列​

  * 评测对象的实际输出​

  * 各评估器指标得分​

  * 实验组结果列*N​

  * 评测对象的实际输出​

  * 各评估器指标得分​

  * 多实验对比行级数据，会有两个分支。​

  * 分支1：评测对象的异常案例。​

  * 检查得分及其原因，人工核对评测集输入与实际输出，识别评估不准确的异常案例。​

  * 点击评测对象的执行 Trace 图标，结合 Trace 排查问题原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27469%27%20height=%27192%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY5IiBoZWlnaHQ9IjE5MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * 分支2：评估器评估不准的异常案例。​

  * 检查得分及其原因，人工核对评测集输入与实际输出，识别评估器评估不准确的异常案例。​

  * 点击评估指标对应的 Trace 图标查看评估器的 Trace 链路，结合 Trace 排查问题原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27484%27%20height=%27124%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg0IiBoZWlnaHQ9IjEyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 人工校准得分​

  * 刷新数据明细页面，指标统计页面也会联动刷新。然后，再进行对比分析。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27411%27%20height=%27268%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDExIiBoZWlnaHQ9IjI2OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 根据多实验对比结果，选择表现更佳的实验版本进行下一步业务决策。可以选择发布该版本上线，或者针对该版本中存在的badcase进行进一步优化。​

导出实验报告​

实验结束后，你可以将已完成的评测实验运行记录报告导出为 CSV 或 Zip 文件，并下载到本地。​

使用限制​

  * 套餐版本限制：仅企业旗舰版和企业标准版套餐支持导出并下载报告。​

  * 实验状态限制：仅成功状态的实验可导出并下载报告。​

  * 报告格式：​

  * 实验报告内列的内容为纯文本场景时，导出和下载为 CSV。​

  * 实验报告内列的内容存在多模态文件时，导出文件格式为 Zip。​

  * 实验报告保存时长：100天。导出实验报告后 100 天内可下载，超时后应重新导出才能下载。​

操作步骤​

导出并下载实验报告的操作步骤如下：​

1.

找到指定的评测实验。​

a.

登录[扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择一个空间。​

b.

在左侧导航栏选择评测 > 实验。​

c.

在实验列表中找到指定的评测实验，确保实验状态为成功。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27492%27%20height=%27157%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkyIiBoZWlnaHQ9IjE1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

导出评测报告。​

a.

在实验列表中单击评测实验名称，进入评测实验详情页。​

b.

在页面右上角单击导出 > CSV 格式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27563%27%20height=%27171%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYzIiBoZWlnaHQ9IjE3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

导出完成后，页面右上角会有状态提示。​

  * 你可以根据页面提示直接下载报告，也可以查看导出记录，下载当前实验的已导出的任意文件报告。​

3.

下载实验报告。​

a.

在评测实验详情页右上角单击导出 > 查看并下载文件。​

b.

找到指定的导出记录，在操作列单击下载。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27408%27%20height=%27214%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA4IiBoZWlnaHQ9IjIxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

实验报告格式​

实验报告文件中包含评测记录的 ID 列、评测集的每一列、执行结果列和评测得分列。各列的详细说明如下：​

​

评测集列名​| 说明​  
---|---  
ID​| 评测数据的 ID。​  
Tags​| 评测集数据行对应的标签。​  
status​| 评测记录的运行状态。Status 表示执行成功。​  
评测集的列​| 评测集中定义的每一列。各个评测集结构不同，此处不再展开说明。​  
actual_output​| 评测对象在本次实验中的实际输出。​  
评估器​| 列名为评估器名称及版本号。其值为每条评测记录的评分。​  
reason​| 对应评分的理由。​  
  
​

​

上一篇

预置评估器

下一篇

人工标注评测数据