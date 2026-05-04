---
source_url: https://docs.coze.cn/guides/batch_run_workflow
title: '批量执行低代码工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:23Z
---

# 批量执行低代码工作流 - 文档 - 扣子

批量执行低代码工作流

批量任务是一个自动化工具，当你上传 CSV 格式的工作流输入参数后，系统将托管式批量执行低代码工作流。本文介绍批量执行低代码工作流的操作步骤及相关配置说明。​

使用场景​

在视频生成、图像生成、文本打标等场景中，用户通常希望通过工作流批量生成结果，以满足规模化生产需求。然而，工作流批处理节点或节点的批处理模式单次执行时长上限为 10 分钟，无法适配视频生成这类耗时较长的场景。​

相比之下，批量任务是异步执行的，采用托管模式执行工作流，支持 10 分钟以上的长时间任务，并且单个任务最多可执行 1000 个子任务，能高效满足大批次处理需求，用户只需在 CSV 表格中配置工作流输入参数并上传，系统便会批量执行工作流，生成结果。​

套餐权益​

执行任务时，扣子编程会根据你所在的订阅套餐将任务分配至不同类型的队列中，按顺序依次执行。​

  * 共享队列：扣子全平台用户共享一个队列。​

  * 独享队列：各个企业具备独享队列，并发执行任务，但企业内部的任务将按提交顺序排队执行。​

说明

  * 任务中心的批量任务和异步任务共享队列与执行条数（即子任务数量）限制。​

  * 主账号及其所有子账号共享任务执行条数权益。​

​

​

订阅套餐​| 个人免费版​| 个人付费版​| 企业标准版​| 企业旗舰版​  
---|---|---|---|---  
队列​| 共享队列​| 共享队列​| 共享队列​| 独享队列​  
执行条数（月）​| 50​| 1,000​| 100,000​| 无限制​  
  
​

前提条件​

  * 批量执行资源库工作流时，已发布指定的工作流。​

  * 批量执行应用工作流时，已发布指定的应用。​

创建批量任务​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左侧导航栏中单击任务中心，然后选择创建任务 > 批量任务。​

3.

选择任务对象，即选择要批量执行的工作流。​

a.

设置任务名称。​

b.

选择任务对象。​

  * 你可以从资源库或应用中，选择某个工作流及其版本。​

  * 资源库工作流​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272207%27%20height=%27464.35697399527186%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIwNyIgaGVpZ2h0PSI0NjQuMzU2OTczOTk1MjcxODYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

应用工作流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272190%27%20height=%27450.4255319148936%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE5MCIgaGVpZ2h0PSI0NTAuNDI1NTMxOTE0ODkzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

c.

单击下一步。​

4.

准备任务数据。​

a.

在工作流参数区域，单击下载模板。​

  * 系统将依据你所选定工作流的开始节点，自动生成一个名为 ${工作流名称}_input_template.csv 的 CSV 表格，你需要下载此表格。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27603%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAzIiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

在 CSV 表格中配置输入参数值。​

  * 根据工作流开始节点的输入参数要求来设置参数值，关于输入参数的具体配置说明，请参考​输入参数配置说明。​

c.

在导入参数配置区域，上传 CSV 表格。​

d.

设置任务模式。​

  * 扣子编程提供两种任务模式：共享队列和独享队列。​

  * 共享队列：扣子全平台用户共享一个队列，任务将按提交顺序依次执行。​

  * 独享队列：企业旗舰版套餐可以选择独享队列，提高执行效果。企业之间并发执行任务，但企业内部的任务将按提交顺序排队执行。​

e.

单击创建任务。​

5.

等待任务执行完成后，查看工作流产物。​

  * 你可以单击各个子任务的执行详情图标，跳转到对应的工作流页面查看执行结果，也可以单击导出文件，然后在本地环境中查看执行结果数据。其中，导出的文件名格式为 ${任务名称}+output.csv。​

  * 任务详情​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272237%27%20height=%27396.63120567375887%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzNyIgaGVpZ2h0PSIzOTYuNjMxMjA1NjczNzU4ODciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

工作流执行详情​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271891%27%20height=%27921.4327272727272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5MSIgaGVpZ2h0PSI5MjEuNDMyNzI3MjcyNzI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

任务结果文件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271430%27%20height=%2798.8%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQzMCIgaGVpZ2h0PSI5OC44IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

输入参数配置说明​

在准备任务数据阶段，系统将依据你所选定工作流的开始节点，自动生成一个名为 ${工作流名称}_input_template.csv 的 CSV 表格。你需要下载此表格，并根据工作流开始节点的输入参数要求填写表格内容。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27328%27%20height=%27165%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI4IiBoZWlnaHQ9IjE2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置表格​

CSV 表格包含序号列和输入参数列。配置说明如下：​

说明

  * 为确保数据的正确解析及批量任务的正常运行，请勿修改 CSV 表格结构和列名。​

  * 序号列和必选的输入参数必须配置。​

​

1.

配置序号。​

  * 第一列为序号列，一个序号代表一个子任务，批量任务会根据序号，生成对应数量的子任务。最大值为 1000。​

2.

配置输入参数。​

  * 第二列开始为输入参数列，列名由开始节点的输入参数名（如 prompt）自动生成，多个输入参数将对应生成多列。​

  * 说明

特殊数据类型的参数说明如下：​

    * Object 类型：子字段名称将包含完整父级路径（如 data.url、data.message），表格中不展示父级字段，仅需配置子字段值。​

    * Array 类型：需添加 CSV 表格的转义符 "" 包裹输入参数值，例如"[""a"",""b"",10]"​

    * File 类型：参数值需使用公网可访问的文件 URL。​

​

配置示例​

例如搭建一个工作流用于提取发票数据中的金额，发票数据为 Array 类型，因此需将开始节点输入参数 input 设置为 Array<string> 类型，用于输入发票数据，并使用文本处理节点提取数组中的第四个元素（发票金额）。​

然后创建一个批量任务，批量提取各发票中的金额。在 CSV 表格的序号列填写好序号， 在 input 列输入 4 行发票数据（如 "[""INV001"",""2023-10-01"",""ABC"",""1800.00"",""192.00"",""VAT""]"），当批量任务运行成功后将在输出参数列展示发票金额。​

工作流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271241%27%20height=%27591.1672727272727%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI0MSIgaGVpZ2h0PSI1OTEuMTY3MjcyNzI3MjcyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

CSV 表格​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271480%27%20height=%27409.0181818181818%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ4MCIgaGVpZ2h0PSI0MDkuMDE4MTgxODE4MTgxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

输出结果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272293%27%20height=%27516.9672727272728%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI5MyIgaGVpZ2h0PSI1MTYuOTY3MjcyNzI3MjcyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

相关操作​

创建批量任务后，你还可以在任务详情页面执行如下相关操作。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27581%27%20height=%27165%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgxIiBoZWlnaHQ9IjE2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

相关操作​| 说明​  
---|---  
查看任务详情​| 查看各个子任务的运行状态、消耗的积分、输入参数、输出参数等信息。​  
查看任务状态​| 批量任务包含如下运行状态。​

  * 排队中：队列中还有其他任务在执行，需排队执行。​

  * 进行中：开始执行任务。开始时，系统会给你发送扣子站内信通知。​

  * 已完成：任务执行完成，你可以查看执行结果。​

  * 已取消：任务被取消。​

  
取消任务​| 当你需要终止任务时，你可以在任务详情页面，取消任务。​

  * 如果批量任务还在排队中，你可以单击页面右上角的取消任务，取消整个任务。​

  * 如果批量任务已在进行中，你可以取消还未执行的子任务。​

  
重试任务​| 当任务执行失败或你对任务的执行结果不满意时，你可以在任务详情页面，重试单个子任务，或者批量重试多个任务。单次最多可重试 50 个子任务。​  
  
​

​

上一篇

导入与导出低代码工作流

下一篇

异步执行低代码工作流