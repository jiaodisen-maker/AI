---
source_url: https://docs.coze.cn/cozeloop/evaluate_coze_agent
title: '评测扣子智能体 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:58Z
---

# 评测扣子智能体 - 文档 - 扣子

评测扣子智能体

本文档介绍在扣子罗盘中评测扣子智能体的操作步骤。​

场景描述​

当你在扣子编程搭建智能体（如翻译助手、客服机器人、代码生成工具等）后，需要系统性评估其功能表现（如翻译准确性、回答相关性、代码正确性等）以验证是否符合预期时，可通过扣子罗盘提供的评测功能，对智能体进行标准化、量化的质量检测。​

例如，你开发了一个翻译助手智能体，希望验证其翻译结果的准确性，本文将演示如何通过评测集、LLM 评估器和实验来对该智能体进行评测。​

准备工作​

  * 已在扣子编程搭建翻译助手智能体，详细步骤参考​搭建一个低代码智能体。​

  * 已准备评测数据，本文将使用以下评测数据作为示例：​

  * ​

​

翻译助手评测 .csv

​

​

操作步骤​

步骤一：创建评测集​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择目标工作空间。​

2.

在左侧导航栏，选择评测 > 评测集，单击右上角的 \+ 新建评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27217%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/286983f23f644939ac27242a92855610~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

在新建评测集页面，输入评测集的名称，配置评测集的输入数据列和输出列信息，然后单击创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27379.0509259259259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM3OS4wNTA5MjU5MjU5MjU5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

添加测试数据。​

  * 扣子罗盘支持本地上传和手动导入两种方式来添加测试数据。本文以本地上传方式为例，将已准备的评测数据批量上传至评测集。​

  * 在评测集详情页面，选择添加数据 > 本地导入，导入准备工作中准备好的测试数据，并配置列映射关系， 单击导入。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27171.875%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjE3MS44NzUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27403.6269430051814%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQwMy42MjY5NDMwMDUxODE0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

5.

单击提交新版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27260.4166666666667%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjI2MC40MTY2NjY2NjY2NjY3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤二：创建评估器​

1.

在左侧导航栏选择评测 > 评估器，单击 \+ 新建评估器 > LLM评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271629%27%20height=%27446.84375000000006%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYyOSIgaGVpZ2h0PSI0NDYuODQzNzUwMDAwMDAwMDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

在评估器模板页面，扣子罗盘提供了多个预置的模板，如果没有合适的模板，你也可以单击自定义创建LLM评估器创建评估器。​

  * 在本场景中，你需要评估翻译助手智能体的翻译准确性，因此选择选择内容质量 > 正确性模板，单击应用。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27358.7962962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM1OC43OTYyOTYyOTYyOTYzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

修改评估器的名称和模型，单击调试，测试一下评估器效果。​

  * 说明

在调试评估器时，会产生 Token 消耗。​

​

  * 在弹出的预览与调试页面，输入一组测试数据，然后单击运行查看评估效果是否符合预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27658%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU4IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击创建，单击提交新版本。完成评估器创建并提交评估器版本。​

  * 说明

在创建评测实验时，只能使用已提交的评估器。​

​

步骤三：发起实验​

在准备好评测集和评估器后，就可以发起实验来测试翻译助手智能体的翻译准确性了。​

1.

在左侧导航栏，选择评测 > 实验，然后单击 \+ 新建实验。​

2.

输入一个实验名称，然后单击下一步: 评测集。​

3.

选择已创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27591%27%20height=%27334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTkxIiBoZWlnaHQ9IjMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

评测对象选择 Coze 智能体，然后选择要评测的智能体和版本，再通过字段映射的方式选择评测集中的哪列数据作为智能体的输入传递给智能体，最后单击下一步：评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27446.52777777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ0Ni41Mjc3Nzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击添加评估器，选择已创建的评估器和版本，然后将评测集的字段、评测对象的实际输出与评估器的参数关联，确保评估器准确获取数据并执行评估，最后单击确认实验配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27447.9166666666667%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ0Ny45MTY2NjY2NjY2NjY3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

6.

检查实验配置，确认无误后，单击发起实验。​

  * 发起实验后，你可以刷新实验页面，查看评估进度。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272374%27%20height=%271265.894259818731%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM3NCIgaGVpZ2h0PSIxMjY1Ljg5NDI1OTgxODczMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：分析实验结果​

在评估器执行完所有评估任务后，你可以在实验页面查看实验报告。通过实验报告来判断评估对象是否符合预期。​

查看评测结果​

在数据明细页面，你可以查看评估器对每个测试数据的执行结果的评分，以及评分的具体原因。​

如果某个测试数据的评估器自动打分不准确，你可以将鼠标悬浮至评分上，然后点击出现的人工校准图标。在弹出的页面中输入修正的分数和原因。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272410%27%20height=%271263.5285714285712%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQxMCIgaGVpZ2h0PSIxMjYzLjUyODU3MTQyODU3MTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看实验报告​

在实验详情页面，单击指标统计页签查看实验数据报告。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272374%27%20height=%271051.3428571428572%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM3NCIgaGVpZ2h0PSIxMDUxLjM0Mjg1NzE0Mjg1NzIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

上一篇

评测扣子工作流

下一篇

实时评测行程规划 Agent 的轨迹