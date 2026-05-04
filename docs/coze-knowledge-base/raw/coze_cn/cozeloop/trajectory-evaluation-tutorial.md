---
source_url: https://docs.coze.cn/cozeloop/trajectory-evaluation-tutorial
title: '通过数据回流评测行程规划 Agent 的轨迹 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:57:03Z
---

# 通过数据回流评测行程规划 Agent 的轨迹 - 文档 - 扣子

通过数据回流评测行程规划 Agent 的轨迹

本文演示如何通过 Trace 数据回流的方式对一个行程规划 Agent 的轨迹（Trajectory）进行离线评测。该行程规划 Agent 能够根据用户输入的旅游需求，如目的地、出行时间、预算等，生成合理的旅游行程安排。 ​

背景信息​

推荐你先阅读 ​轨迹评测介绍了解什么是轨迹和轨迹评测。​

前提条件​

在扣子罗盘中，只有火山智能体才能被用作轨迹评测的评测对象。详情参见 ​火山智能体注册。​

操作步骤​

参考以下步骤通过轨迹评测一个行程规划 Agent。​

扣子罗盘支持将 Trace 数据手动沉淀到评测集，提升数据质量，便于后续开展评测实验，优化 AI 应用表现。因此，在本教程中，评测集中的轨迹数据是通过 Trace 数据回流的。​

你将同时使用 LLM-as-Judge 和轨迹匹配的方式评估 Agent 的轨迹： ​

  * 一个 LLM 评估器用于实时评估 Agent 的轨迹质量。LLM 评估器会评估 Agent 在评测实验时实时产生的轨迹数据。​

  * 一个代码评估器用于评估 Agent 调用的工具是否符合预期。代码评估器会使用从 Trace 回流的轨迹数据作为参考。​

步骤一：实现 Trace 数据上报​

首先，你需要确保 Agent 的 Trace 数据可以被上报到扣子罗盘。详情参阅 ​数据上报概述 和 ​VeADK。​

步骤二：创建评测集​

接下来，你需要创建评测集并向评测集添加数据。评测集包括用户输入、Agent 的理想输出轨迹数据和 Agent 必须调用的工具。 在本教程中，你从指定的 Trace 数据中把轨迹数据回流到评测集中的理想输出轨迹数据列。​

1.

登录 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择评测 > 评测集，然后把鼠标移动到 \+ 新建评测集 按钮上，在下拉菜单中单击 +新建评测集。​

3.

在 新建评测集 页面，填写评测集名称和描述。​

4.

在配置列区域右侧，选择 轨迹评测集，并创建三个列：​

  * ​

名称​| 数据类型​| 必填​  
---|---|---  
input​| String​| 否​  
groundtruth_trajectory​| 轨迹​| 否​  
required_tool​| String​| 否​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272232%27%20height=%273508.166666666667%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzMiIgaGVpZ2h0PSIzNTA4LjE2NjY2NjY2NjY2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击 创建。你会被跳转到评测集的管理页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272230%27%20height=%271281.4179104477612%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzMCIgaGVpZ2h0PSIxMjgxLjQxNzkxMDQ0Nzc2MTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

步骤三：把轨迹数据回流到评测集​

接下来，你从指定的 Trace 数据中把轨迹数据回流到评测集中的理想输出轨迹数据列。​

说明

本教程不涉及轨迹数据的二次处理。但是，在一些复杂场景下，你可能需要对回流至评测集的轨迹数据进行二次处理（例如筛选或分类）。对数据进行二次处理时，你需要先将初步回流的轨迹数据导出为本地文件，完成二次处理后，再将处理后的文件重新导入评测集。详情参见 ​导入和导出评测集。​

​

1.

登录 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择 应用 > 应用注册。​

3.

在 Trace 页面，单击右侧的 添加到评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273328%27%20height=%271773.1147540983607%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMyOCIgaGVpZ2h0PSIxNzczLjExNDc1NDA5ODM2MDciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

4.

选择一条或多条 Trace，然后单击右上角的 添加到评测集 按钮。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273339%27%20height=%271743.7868852459017%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzOSIgaGVpZ2h0PSIxNzQzLjc4Njg4NTI0NTkwMTciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

5.

在 添加到评测集 页面，配置以下参数：​

  * ​

参数​| 说明​  
---|---  
目标评测集​| 选择 已有评测集。​  
目标评测集名称​| 选择你在步骤二创建的评测集。​  
导入方式​| 因为你创建的评测集数据为空，因此选择 追加数据 或 全量覆盖 均可。​注意如果评测集中已有数据且你需要保留这些数据，选择 追加数据。​​  
字段映射​| 完成以下字段映射：​
    * 把 Trace 中的 Input 字段映射到评测集中已有的 input 列。​
    * 把 Trace 中的 Trajectory 字段映射到评测集中已有的 trajectory 列。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272732%27%20height=%271928.8425925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjczMiIgaGVpZ2h0PSIxOTI4Ljg0MjU5MjU5MjU5MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

6.

单击 校验并预览 按钮预览导入后评测集的数据内容。校验无误后，单击 关闭 回到 添加到评测集 页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272714%27%20height=%271916.1342592592591%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcxNCIgaGVpZ2h0PSIxOTE2LjEzNDI1OTI1OTI1OTEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

7.

在 添加到评测集 页面，单击 开始导入。导入完成后，你会被跳转回 Trace 页面。然后，单击右上角提示信息中的 查看评测集 按钮回到评测集页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273778%27%20height=%271779.6828703703704%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc3OCIgaGVpZ2h0PSIxNzc5LjY4Mjg3MDM3MDM3MDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

8.

在 评测集 页签，单击每条评测数据 操作 列的 编辑 按钮，添加 required_tool 数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273798%27%20height=%271881.4166666666665%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5OCIgaGVpZ2h0PSIxODgxLjQxNjY2NjY2NjY2NjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

9.

在 评测集 页签，单击右侧的 提交新版本 按钮。在弹出的窗口中设置版本号和版本说明，然后单击 提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273792%27%20height=%271904.7777777777776%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5MiIgaGVpZ2h0PSIxOTA0Ljc3Nzc3Nzc3Nzc3NzYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

步骤四：创建并发起实验​

创建实验时，你需要为实验关联评测集、评估器和评测对象。​

1.

访问 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择评测 > 实验，然后单击 \+ 新建实验。​

3.

填写基础信息。输入实验名称和描述，然后单击 下一步: 评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272916%27%20height=%271491.75%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkxNiIgaGVpZ2h0PSIxNDkxLjc1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

在 评测集 页面，选择你在步骤二创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272902%27%20height=%271484.587962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwMiIgaGVpZ2h0PSIxNDg0LjU4Nzk2Mjk2Mjk2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在 评测对象 页面，按照下面的参数说明配置评测对象。然后单击下一步：评估器。​

  * ​

参数​| 说明​  
---|---  
类型​| 选择 火山智能体。​  
应用​| 选择你的行程规划 Agent。​  
字段映射​| 把评测对象的 user_input 映射到评测集的 input​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272920%27%20height=%271463.3796296296298%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyMCIgaGVpZ2h0PSIxNDYzLjM3OTYyOTYyOTYyOTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

6.

在 评估器 页面，单击 +添加评估器 为评测实验设置评估器。评估器配置完成后，单击确认实验配置。 ​

  * 本文使用以下评估器：​

  * 一个预置评估器，类型为 LLM 评估器，用于评估 Agent 的轨迹质量。字段映射为：评估器 messages = 评测对象 trajectory。这里的 评测对象 Trajectory 就是行程规划 Agent 的实时轨迹。​

  * 一个自建评估器，类型为代码评估器，用于评估 Agent 调用的工具是否与评测集的 groundtruth_trajectory 字段中的轨迹数据中的工具相同。​

  * 注意

一般情况下，字段映射的参数类型必须完全相同。但是，如果评估器中用于接收轨迹数据的参数为 String 类型，你也可以将包含轨迹数据的字段映射到该参数。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273308%27%20height=%271872.236111111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMwOCIgaGVpZ2h0PSIxODcyLjIzNjExMTExMTExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

在页面底部，设置最大并发执行条数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272862%27%20height=%271901.375%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg2MiIgaGVpZ2h0PSIxOTAxLjM3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

检查实验配置，确认无误后，单击发起实验。发起实验后，你可以刷新实验页面，查看评测进度。​

步骤五：查看实验结果​

实验运行完成后，你可以查看实验结果。​

查看数据明细​

在 数据明细 页签，你可以查看每条评测集数据的评测结果，包括评测集数据、评测对象输出数据和评估器得分。你还可以在 操作 列单击 详情，查看每条评测集数据的详情。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273770%27%20height=%271391.9328703703704%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc3MCIgaGVpZ2h0PSIxMzkxLjkzMjg3MDM3MDM3MDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

其中每列数据的说明如下：​

  * ID：代表数据项的 ID。​

  * input、trajectory 轨迹 和 required_tool 是评测集的列名。​

  * actual_output：代表评测对象（即行程规划 Agent）的实际输出。你可以单击 actual_output 右侧的 查看实际输出的 Trace 图标 查看评测对象实际输出的 Trace 数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273062%27%20height=%271754.2708333333333%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2MiIgaGVpZ2h0PSIxNzU0LjI3MDgzMzMzMzMzMzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * trajectory 运行轨迹：代表评测对象的轨迹数据。你可以单击 trajectory 运行轨迹 右侧的 轨迹可视化 图标查看评测对象的轨迹可视化数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273786%27%20height=%271923.673611111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc4NiIgaGVpZ2h0PSIxOTIzLjY3MzYxMTExMTExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * Agent 轨迹质量 和 轨迹中是否调用了符合预期的工具 这两列展示了对应名称的评估器的得分和原因。每个评估器的得分会显示在各自的列中。将鼠标悬停在得分上可以看到得分和原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273350%27%20height=%271419.0972222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM1MCIgaGVpZ2h0PSIxNDE5LjA5NzIyMjIyMjIyMjIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 单击得分右侧的 查看评估器 Trace 图标，即可查看评估器的 Trace。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273074%27%20height=%271106.4976851851852%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA3NCIgaGVpZ2h0PSIxMTA2LjQ5NzY4NTE4NTE4NTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * Total Latency(ms)：评测对象从请求到完整响应的总耗时 (ms)。​

  * Input Tokens：评测对象执行过程中模型调用输入 Tokens 总消耗量。​

  * Output Tokens：评测对象执行过程中模型调用输出 Tokens 总消耗量。​

  * Total Tokens：评测对象执行过程中模型调用的总 Tokens 消耗量。​

你可以在 操作 列单击 详情，查看每个评测集数据项对应的详细分析数据。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273790%27%20height=%271921.3194444444443%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5MCIgaGVpZ2h0PSIxOTIxLjMxOTQ0NDQ0NDQ0NDMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看指标统计​

在 指标统计 页签，你可以查看评估器得分的统计数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273778%27%20height=%271902.1180555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc3OCIgaGVpZ2h0PSIxOTAyLjExODA1NTU1NTU1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

上一篇

实时评测行程规划 Agent 的轨迹

下一篇

图片-清晰度评估器