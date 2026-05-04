---
source_url: https://docs.coze.cn/cozeloop/code_evaluator
title: '预置评估器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:30Z
---

# 预置评估器 - 文档 - 扣子

预置评估器

扣子罗盘内置了多种评估器 Prompt 模板，开发者可以在评测实验中直接使用这些模板，也可以基于这些预置评估器二次开发，打造符合自己业务场景的自建评估器。本文档介绍预置评估器的概念与使用方式。​

什么是预置评估器​

为了便于开发者快速创建各种评测场景的实验，扣子罗盘提供了一系列的预置评估器，适用于文本、图片、音视频等多种评估对象，覆盖了安全风控、AI coding 等多种业务场景。​

你可以在扣子罗盘的评估器 > 预置评估器页面中查看预置评估器列表，你还可以通过评估器名称、类型、评估对象等维度来快速查找和筛选评估器。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27519%27%20height=%27281%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9f98f16ab74d4fa0b59fa7f4940062c0~tplv-goo7wpa0wc-quality:q75.image)​

​

调试预置评估器​

在评测实验中使用预置评估器之前，你可以先简单调试预置评估器，测试其效果是否符合业务要求。​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，并在左侧导航栏顶部，选择一个空间。​

2.

在左侧导航栏，选择评测 > 评估器。​

3.

进入预置评估器页面，选择你想调试的预置评估器。​

  * 支持根据评估对象、评估目标、任务场景以及评估器名称的关键词筛选预置评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27440%27%20height=%27251%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQwIiBoZWlnaHQ9IjI1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

查看评估器的 Prompt 等详细信息，确认无误后在右上角单击调试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27451%27%20height=%27274%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUxIiBoZWlnaHQ9IjI3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

确认模型和 Prompt，并输入测试数据，单击运行。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27458%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU4IiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在测试区域下方查看评估器调试结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27429%27%20height=%27187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI5IiBoZWlnaHQ9IjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用预置评估器​

对于 Agent 任务完成度等常见的典型评测场景，你可以直接在评测实验中使用扣子罗盘提供的预置评估器，而无需手动创建评估器、编写 Prompt 作为评估标准。​

创建评估实验时，选择基础信息、评测集和评测对象之后，你可以在评估器页面中选择预置评估器来开展评估实验。详细操作步骤可参考​创建实验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27491%27%20height=%27430%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkxIiBoZWlnaHQ9IjQzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

管理自建评估器

下一篇

管理实验