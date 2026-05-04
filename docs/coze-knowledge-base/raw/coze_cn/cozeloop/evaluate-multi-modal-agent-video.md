---
source_url: https://docs.coze.cn/cozeloop/evaluate-multi-modal-agent-video
title: '评测多模态（视频）Agent - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:54Z
---

# 评测多模态（视频）Agent - 文档 - 扣子

评测多模态（视频）Agent

在本教程中，你将学习如何以提示词为评测对象，手动创建评测集，并使用 LLM 评估器来评测多模态（视频）Agent 的视频输出。​

准备工作​

已发布用于评测的提示词。详情参阅 ​开发提示词。​

操作步骤​

步骤一：实现 Trace 数据上报​

首先，你需要确保提示词的 Trace 数据可以被上报到扣子罗盘。​

说明

对于通过 Cozeloop SDK 拉取或调用的提示词，其 Trace 数据会被自动上报到扣子罗盘。详情参阅 Cozeloop SDK 关于 Prompt 拉取和调用的文档。​

以 Go SDK 为例，你可以参考以下文档：​

  * ​通过版本标识拉取 Prompt 版本​

  * ​调用 Prompt​

​

步骤二：创建多模态评测集与评估器​

创建评测集​

接下来，你需要创建评测集并向评测集添加数据。评测集包括用户的自然语言输入以及作为理想输出的参考视频。参考视频可作为评估器评估 Agent 时的参考标准。 ​

1.

登录扣子罗盘，在左侧导航栏顶部，选择你的工作空间。 ​

2.

在左侧导航栏，选择评测 > 评测集，然后把鼠标移动到 \+ 新建评测集 按钮上，在下拉菜单中单击 +新建评测集。 ​

3.

在 新建评测集 页面，填写评测集名称和描述。 ​

4.

在配置列区域右侧，选择 理想输出评测集，并创建以下列： ​

  * ​

名称​| 数据类型​| 必填​  
---|---|---  
input ​| String ​| 否 ​  
actual_video​| 多模态 ​| 否​  
ref_video​| 多模态 ​| 否​  
  
​

5.

单击 创建。你会被跳转到评测集的管理页面。 ​

6.

在评测集的管理页面，选择 评测集 页签，把鼠标移动到右侧的 添加数据，在下拉菜单中选择一种添加方式。在本教程中，你通过 手动添加 的方式添加数据。 详情参阅 ​向评测集添加多模态数据。​

  * ​

列​| 描述​  
---|---  
input ​| 用于生成视频的提示词。 ​  
actual_video​| Agent 实际生成的视频。​  
ref_video​| 用于评测的参考视频。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271716%27%20height=%271449.6358208955223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcxNiIgaGVpZ2h0PSIxNDQ5LjYzNTgyMDg5NTUyMjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

7.

在 评测集 页签，单击右侧的 提交新版本 按钮。在弹出的窗口中设置版本号和版本说明，然后单击 提交。 ​

创建评估器​

创建 LLM 评估器时，支持在 User Query 中添加多模态变量，并调试多模态评估效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272304%27%20height=%271475.2477611940299%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMwNCIgaGVpZ2h0PSIxNDc1LjI0Nzc2MTE5NDAyOTkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

步骤三：创建并发起实验 ​

创建实验时，你需要为实验关联评测集、评估器和评测对象。 ​

1.

访问扣子罗盘，在左侧导航栏顶部，选择你的工作空间。 ​

2.

在左侧导航栏，选择评测 > 实验，然后单击 \+ 新建实验。 ​

3.

在 评测集 页面，选择你在步骤二创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。 ​

4.

在 评测对象 页面，按照下面的参数说明配置评测对象。然后单击下一步：评估器。 ​

  * ​

参数 ​| 说明 ​  
---|---  
类型 ​| 设置为 Prompt。​  
Prompt key​| 设置为你的 Prompt key。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271798%27%20height=%271263.9671641791044%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc5OCIgaGVpZ2h0PSIxMjYzLjk2NzE2NDE3OTEwNDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

5.

在 评估器 页面，单击 +添加评估器 为评测实验设置评估器。评估器配置完成后，在页面底部设置最大并发执行条数，然后单击 确认实验配置。 ​

  * 本教程使用名称为 “视频Agent指令遵循评估器” 的自定义评估器，类型为 LLM 评估器。该评估器会根据用户输入的自然语言指令、参考视频和参考音频，对视频 Agent 生成的视频和音频进行指令遵循度评测，并输出评分。 ​

  * 评估器的字段映射为： ​

  * 评估器 input = 评测集 input​

  * 评估器 actual_video = 评测对象 actual_video​

  * 评估器 ref_video = 评测对象 ref_video​

6.

填写基础信息。输入实验名称和描述，然后检查实验配置，确认无误后，单击发起实验。发起实验后，你可以刷新实验页面，查看评测进度。 ​

步骤四：查看实验结果 ​

实验运行完成后，你可以查看实验结果。 ​

查看数据明细 ​

在 数据明细 页签，你可以查看每条评测集数据的评测结果，包括评测集数据、评测对象输出数据和评估器得分。 ​

你还可以在 操作 列单击 详情，查看每条评测集数据的详情。 ​

查看指标统计 ​

在 指标统计 页签，你可以查看评估器得分的统计数据。 ​

​

​

​

​

上一篇

评测多模态（图片） Agent

下一篇

评测扣子工作流