---
source_url: https://docs.coze.cn/cozeloop/optimize-prompts-with-ai
title: '智能优化提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:05Z
---

# 智能优化提示词 - 文档 - 扣子

智能优化提示词

扣子罗盘支持通过大模型智能优化提示词，本文档介绍智能优化的操作方式。​

功能介绍​

扣子罗盘的智能优化功能可基于评测实验结果和评测集来定向优化提示词，相较于传统的智能优化提示词方案有更明确的优化方向和目标，可靠性更高。​

  * 基于评测实验优化提示词：将评测实验中相对低分的数据作为 Badcase 来优化提示词。模型会根据评测实验中的问题、模型回复、参考答案以及对应评估器得分来定位提示词的问题与不足，定向优化提示词。此方式适用于提示词评测标准明确、已经基于评测问题进行过提示词评测实验的情况。​

  * 基于优质的评测集优化提示词：将已准备好的优质评测集作为 Goodcase 来优化提示词。模型会学习和参考评测集中准备好的问题、模型回复和参考答案，判断开发者的预期输出标准，智能优化提示词使实际输出更接近优质评测集的参考答案。此方式适用于提示词质量无法或难以量化、但是有明确参考答案的情况。​

说明

智能优化提示词功能正在定向邀测中，若有相关业务需求，可联系商务经理申请加入白名单。​

​

使用限制​

​

限制​| 说明​  
---|---  
提示词限制​| 为保证智能优化效果，以下类型的提示词不支持发起智能优化：​

  * 使用了Jinja2 模板​

  * 包含多模态变量​

  * 不包含 String 类型变量​

  
评测集限制​| 你可以从评测集中选择一部分作为 Goodcase 来智能优化 Prompt。选择数据时具体要求如下：​

  * 数据条数必须大于 10 条。​

  * 最多可选择 500 条。​

  * 评测数据必须存在预期输出字段，通常名为 actual_output。​

  
评测实验限制​| 

  * 评测实验状态必须为成功、至少有一条不是满分的结果，且设置了评估器和评估对象。​

  * 你可以从评测实验数据中选择一部分作为 Badcase 来智能优化 Prompt。选择数据时具体要求如下：​

  * 数据条数必须大于 10 条，且成功评估的数据不少于 10 条。最多可选择 500 条。​

  * 已选择的评测数据得分至少有一条不是满分（1.0）。​

  * 设置了评估器或评估对象。​

  * 评测实验数据明细中必须存在预期输出字段，通常名为 actual_output。​

  
  
​

根据评测集优化提示词​

如果你已经有一个优质的评测集，可以基于评测集中的预期输出来智能优化提示词。操作步骤如下：​

1.

发起智能优化。​

a.

在扣子罗盘左侧导航栏中单击 Prompt 开发。​

b.

在 Prompt 详情页面右上角单击智能优化，并选择基于优质的评测集优化提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27473%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDczIiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

配置智能优化任务。​

  * 填写以下配置，新建一个智能优化任务，并单击确定。​

  * 评测集：选择作为参考的优质评测集。注意评测集必须已经提交过版本。​

  * 版本：优质评测集的版本。你也可以根据页面提示查看指定版本评测集的详细信息。​

  * Prompt 版本：待优化的 Prompt 版本，默认为最新版本。你也可以根据页面提示查看此版本 Prompt 的具体内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27227%27%20height=%27170%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI3IiBoZWlnaHQ9IjE3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择评测集数据。​

  * 选择作为 Goodcase 参考的优质评测集数据，并单击下一步。注意评测集数据中需要包含 Prompt 的预期输出，否则模型无法判断优化的预期标准。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27348%27%20height=%27236%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ4IiBoZWlnaHQ9IjIzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

配置映射与优化模式。​

  * 映射：配置 Prompt 中变量、模型回答和参考回答和评测集中字段的对应关系。智能优化任务会自动用评测集中的指定字段作为变量注入到 Prompt，并对比模型回答、参考回答与优质评测集的差距，定向优化评测集。​

  * 优化模式：拖动滑块，设置更偏向效果还是性价比。​

  * 效果优先：算法会尝试更多的优化策略、迭代更多次数，尽力提升优化效果，但是相对的资源消耗会更大。​

  * 性价比优先 ：会平衡资源消耗与优化效果，资源消耗相对较少，但可能会损失一定的优化效果。​

  * 预估值：预览当前优化模式下预计消耗的资源点，仅用于估计成本，具体 Token 消耗以火山引擎账单为准。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27345%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA0IiBoZWlnaHQ9IjM0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击开始智能优化，扣子罗盘会自动提交智能优化任务。​

6.

查看优化报告。​

  * 你可以在 Prompt 详情页面的智能优化页签下找到智能优化任务，单击智能优化报告，查看优化详情。关于报告的详细信息，可参考​查看智能优化报告。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27419%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE5IiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

提交新版本。​

  * 如果优化后的效果符合预期，你可以选择将智能优化后的提示词版本同步至提示词新版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27466%27%20height=%27287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY2IiBoZWlnaHQ9IjI4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27903%27%20height=%27457%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTAzIiBoZWlnaHQ9IjQ1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * ​

根据评测实验优化提示词​

如果你曾经发起过针对 Prompt 的评测实验，且实验状态为成功，则可以基于评测实验中的低分数据来智能优化提示词。操作步骤如下：​

1.

发起智能优化。​

a.

在扣子罗盘左侧导航栏中单击 Prompt 开发。​

b.

在 Prompt 详情页面右上角单击智能优化，并选择基于评测结果优化提示词。​

  * 除此之外，你也可以在评测实验的详情页面快速发起智能优化。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272342%27%20height=%271415.3093525179856%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM0MiIgaGVpZ2h0PSIxNDE1LjMwOTM1MjUxNzk4NTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271147%27%20height=%27513.7037914691944%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE0NyIgaGVpZ2h0PSI1MTMuNzAzNzkxNDY5MTk0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

2.

配置智能优化任务。​

  * 选择作为参考的评测实验，并单击确定。注意评测实验状态必须为成功、至少有一条不是满分的结果，且设置了评估器及评估对象。​

  * 说明

扣子罗盘支持通过评估器 Prompt 来自行定义得分区间。但是如果要根据评测实验优化提示词，扣子罗盘建议你选择评分范围为默认范围（0.0~1.0）的实验，以获得更好的优化效果。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27386%27%20height=%27224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg2IiBoZWlnaHQ9IjIyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择评测实验数据。​

  * 选择作为 Badcase 参考的评测实验结果数据，数量范围为 10~500 条，并单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27384%27%20height=%27262%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg0IiBoZWlnaHQ9IjI2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

设置映射与优化模式。​

  * 映射：配置 Prompt 中变量、模型回答和参考回答和评测集中字段的对应关系。智能优化任务会自动用评测集中的指定字段作为变量注入到 Prompt，并对比模型回答、参考回答与优质评测集的差距，定向优化评测集。​

  * 优化模式：拖动滑块，设置更偏向效果还是性价比。​

  * 效果优先：算法会尝试更多的优化策略、迭代更多次数，尽力提升优化效果，但是相对的资源消耗会更大。​

  * 性价比优先 ：会平衡资源消耗与优化效果，资源消耗相对较少，但可能会损失一定的优化效果。​

  * 预估值：预览当前优化模式下预计消耗的资源点，仅用于估计成本，具体消耗可参考火山引擎账单。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27467%27%20height=%27270%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY3IiBoZWlnaHQ9IjI3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击开始智能优化，扣子罗盘会自动提交智能优化任务。​

6.

查看优化报告。​

  * 你可以在 Prompt 详情页面的智能优化页签下找到智能优化任务，单击智能优化报告，查看优化详情。关于报告的详细信息，可参考​查看智能优化报告。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27419%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE5IiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

提交新版本。​

  * 如果优化后的效果符合预期，你可以选择将智能优化后的提示词版本同步至提示词新版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27466%27%20height=%27287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY2IiBoZWlnaHQ9IjI4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27903%27%20height=%27457%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTAzIiBoZWlnaHQ9IjQ1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

查看智能优化结果​

查看任务列表和详情​

成功创建智能优化任务之后，你可以在 Prompt 详情页面的智能优化页签下查看该 PromptKey 发起过的智能优化任务。支持根据任务名称和状态进行快速筛选，你也可以通过关联的评测实验和评测集来过滤出对应的优化任务。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27506%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA2IiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在操作列单击详情，可查看任务的配置细节，包括评测实验、优化配置等信息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27525%27%20height=%27327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI1IiBoZWlnaHQ9IjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看智能优化报告​

成功创建智能优化任务之后，你可以在 Prompt 详情页面的智能优化页签下查看该 PromptKey 发起过的智能优化任务，单击智能优化报告即可查看详细报告信息。​

智能优化报告包含以下内容：​

  * Prompt 优化前后对比：包含 Prompt 得分对比、Prompt 内容对比。​

  * 数据详情​

  * 综合得分：包含评分分布对比、评测数据明细​

  * 评估器得分（仅基于评测实验发起的智能优化展示）：包含评分分布对比、评测数据明细​

Prompt 优化前后对比：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271328%27%20height=%27823%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyOCIgaGVpZ2h0PSI4MjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

评分分布对比：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271325%27%20height=%27774%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyNSIgaGVpZ2h0PSI3NzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

数据详情-评估器得分​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271328%27%20height=%27851%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyOCIgaGVpZ2h0PSI4NTEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

评测数据明细​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271329%27%20height=%27902%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyOSIgaGVpZ2h0PSI5MDIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

常见问题​

如何选择智能优化的方式？​

  * 基于现有素材：若有明确评测标准（已建立评估体系），优先选基于评测实验优化；若无明确评测标准，选基于评测集优化​

  * 数量建议：选择实验数据时，不推荐选择全部满分的实验数据发起优化，建议采用批量 Badcase 优化、实验数据量级建议在20-500条范围内。​

Jinja2 模板 Prompt 能否发起优化？​

所选 Prompt 使用 Jinja2 模版时暂不支持发起智能优化。​

评测实验未完成能否进行优化？​

实验未全部执行完成时无法进行智能优化。​

是否支持下载智能优化报告？​

仅企业标准版和企业旗舰版用户可下载，且任务为成功状态下才可点击下载智能优化报告。​

终止智能优化任务后资源点是否返还？​

终止正在运行的智能优化任务不可逆，已消耗的资源点不返还。​

上一篇

调试提示词

下一篇

管理提示词版本