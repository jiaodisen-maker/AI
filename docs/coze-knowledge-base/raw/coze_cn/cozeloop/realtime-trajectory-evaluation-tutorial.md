---
source_url: https://docs.coze.cn/cozeloop/realtime-trajectory-evaluation-tutorial
title: '实时评测行程规划 Agent 的轨迹 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:57:00Z
---

# 实时评测行程规划 Agent 的轨迹 - 文档 - 扣子

实时评测行程规划 Agent 的轨迹

本文演示如何对一个行程规划 Agent 的轨迹（Trajectory）进行实时离线评测。该行程规划 Agent 能够根据用户输入的旅游需求，如目的地、出行时间、预算等，生成合理的旅游行程安排。 ​

背景信息​

推荐你先阅读 ​轨迹评测介绍了解什么是轨迹和轨迹评测。​

前提条件​

在扣子罗盘中，只有火山智能体才能被用作轨迹评测的评测对象。详情参见 ​火山智能体注册。​

操作步骤​

参考以下步骤评测一个行程规划 Agent 的轨迹。​

你将使用 LLM-as-Judge 方法评估 Agent 的轨迹，在实验中添加两个 LLM 评估器，分别用于评估 Agent 实时轨迹的工具参数填充正确性和工具利用率 ​

步骤一：实现 Trace 数据上报​

首先，你需要确保 Agent 的 Trace 数据可以被上报到扣子罗盘。详情参阅 ​数据上报概述 和 ​VeADK。​

步骤二：创建评测集​

注意

评测集中不需要有轨迹数据，但评测集的场景必须是 轨迹评测集。​

​

接下来，你需要创建评测集并向评测集添加数据。评测集包括用户输入。​

1.

登录 [扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择你的工作空间。​

2.

在左侧导航栏，选择评测 > 评测集，然后把鼠标移动到 \+ 新建评测集 按钮上，在下拉菜单中单击 +新建评测集。​

3.

在 新建评测集 页面，填写评测集名称和描述。​

4.

在配置列区域右侧，选择 轨迹评测集，并创建一个列：​

  * ​

名称​| 数据类型​| 必填​  
---|---|---  
input​| String​| 否​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27722%27%20height=%27424%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzIyIiBoZWlnaHQ9IjQyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击 创建。你会被跳转到评测集的管理页面。​

步骤三：向评测集添加评测数据​

1.

在评测集的管理页面，选择 评测集 页签，把鼠标移动到右侧的 添加数据，在下拉菜单中选择一种添加方式。在本教程中，你通过 手动添加 的方式添加以下数据：​

  * ​

元旦去哈尔滨旅行，如何规划5天4晚的行程，既能兼顾冰雪大世界、中央大街等热门景点，又能体验东北特色美食？​  
---  
暑假去敦煌旅行5天，计划游览莫高窟、鸣沙山月牙泉，还想体验玉门关、雅丹魔鬼城的戈壁风光，考虑到当地气候和交通，行程该怎么调整更合理？​  
重阳节带父母去北京旅行6天，想参观故宫、天坛等适合长辈的文化景点，还想安排颐和园的休闲漫步，如何规划节奏舒缓的行程？​  
端午小长假去重庆旅行4天，既要打卡洪崖洞、解放碑的夜景，又想挑战长江索道和李子坝轻轨站，还想抽空去磁器口古镇逛吃，行程怎么安排不绕路？​  
寒假去三亚旅行5天，想避开人挤人的热门海滩，同时体验蜈支洲岛的水上项目和南山文化旅游区的祈福活动，行程如何设计更舒适？​  
清明假期去杭州旅行3天，除了西湖、灵隐寺这些必去景点，还想加1天西溪国家湿地公园的徒步，该怎么规划每日行程才不赶？​  
国庆去大理旅行7天，计划环洱海、登苍山，还想留出时间去沙溪古镇感受小众静谧，如何平衡热门景点与小众目的地的行程？​  
中秋小长假去苏州旅行4天，想深度体验园林文化（拙政园、留园等），还想夜游平江路、品尝苏帮菜，行程顺序该怎么安排更顺路？​  
暑假带孩子去青岛旅行6天，既要满足孩子玩海的需求（如石老人海水浴场），又想参观栈桥、八大关等经典景点，如何规划亲子友好型行程？​  
五一假期去成都玩3天，想打卡宽窄巷子、大熊猫繁育研究基地，还想安排1天周边游（比如都江堰或青城山），行程该怎么合理分配？​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273338%27%20height=%271429.4675925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzOCIgaGVpZ2h0PSIxNDI5LjQ2NzU5MjU5MjU5MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

在 评测集 页签，单击右侧的 提交新版本 按钮。在弹出的窗口中设置版本号和版本说明，然后单击 提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273324%27%20height=%271442.7083333333335%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMyNCIgaGVpZ2h0PSIxNDQyLjcwODMzMzMzMzMzMzUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

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

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27810%27%20height=%27514%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODEwIiBoZWlnaHQ9IjUxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在 评测集 页面，选择你在步骤二创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272708%27%20height=%271626.6805555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcwOCIgaGVpZ2h0PSIxNjI2LjY4MDU1NTU1NTU1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

5.

在 评测对象 页面，按照下面的参数说明配置评测对象。然后单击下一步：评估器。​

  * ​

参数​| 说明​  
---|---  
类型​| 选择 火山智能体。​  
应用​| 选择你的行程规划 Agent。​  
字段映射​| 把评测对象的 user_input 映射到评测集的 input。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272584%27%20height=%271632.9444444444443%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU4NCIgaGVpZ2h0PSIxNjMyLjk0NDQ0NDQ0NDQ0NDMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

6.

在 评估器 页面，单击 +添加评估器 为评测实验设置评估器。评估器配置完成后，单击确认实验配置。 ​

  * 本文使用以下评估器：​

  * 名称为 “轨迹-工具参数填充正确性” 的预置评估器，类型为 LLM 评估器，字段映射为：评估器 Trajectory = 评测对象 Trajectory。​

  * 名称为 “轨迹-工具利用率” 的预置评估器，类型为 LLM 评估器。字段映射为：评估器 Trajectory = 评测对象 Trajectory。​

  * 注意

    * 这里的 评测对象 Trajectory 就是行程规划 Agent 的实时轨迹。​

    * 一般情况下，字段映射的参数类型必须完全相同。但是，如果评估器中用于接收轨迹数据的参数为 String 类型，你也可以将包含轨迹数据的字段映射到该参数。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272598%27%20height=%271626.7569444444446%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU5OCIgaGVpZ2h0PSIxNjI2Ljc1Njk0NDQ0NDQ0NDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

7.

在页面底部，设置最大并发执行条数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272536%27%20height=%271626.0925925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUzNiIgaGVpZ2h0PSIxNjI2LjA5MjU5MjU5MjU5MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

8.

检查实验配置，确认无误后，单击发起实验。发起实验后，你可以刷新实验页面，查看评测进度。​

步骤五：查看实验结果​

实验运行完成后，你可以查看实验结果。​

查看数据明细​

在 数据明细 页签，你可以查看每条评测集数据的评测结果，包括评测集数据、评测对象输出数据和评估器得分。你还可以在 操作 列单击 详情，查看每条评测集数据的详情。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27864%27%20height=%27377%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODY0IiBoZWlnaHQ9IjM3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

其中每列数据的说明如下：​

  * ID：代表数据项的 ID。​

  * input 是评测集的列名。​

  * actual_output：代表评测对象（即行程规划 Agent）的实际输出。你可以单击 actual_output 右侧的 查看实际输出的 Trace 图标 查看评测对象实际输出的 Trace 数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273028%27%20height=%271703.25%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyOCIgaGVpZ2h0PSIxNzAzLjI1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * trajectory 运行轨迹：代表评测对象的轨迹数据。你可以单击 trajectory 运行轨迹 右侧的 轨迹可视化 图标查看评测对象的轨迹可视化数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273796%27%20height=%271748.6203703703704%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5NiIgaGVpZ2h0PSIxNzQ4LjYyMDM3MDM3MDM3MDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 轨迹-工具参数填充正确性 和 轨迹-工具利用率 这两列展示了对应名称的评估器的得分和原因。每个评估器的得分会显示在各自的列中。将鼠标悬停在得分上可以看到得分和原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273344%27%20height=%271726.1851851851852%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM0NCIgaGVpZ2h0PSIxNzI2LjE4NTE4NTE4NTE4NTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 单击得分右侧的 查看评估器 Trace 图标，即可查看评估器的 Trace。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273062%27%20height=%271201.4097222222222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2MiIgaGVpZ2h0PSIxMjAxLjQwOTcyMjIyMjIyMjIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * Total Latency(ms)：评测对象从请求到完整响应的总耗时 (ms)。​

  * Input Tokens：评测对象执行过程中模型调用输入 Tokens 总消耗量。​

  * Output Tokens：评测对象执行过程中模型调用输出 Tokens 总消耗量。​

  * Total Tokens：评测对象执行过程中模型调用的总 Tokens 消耗量。​

你可以在 操作 列单击 详情，查看每个评测集数据项对应的详细分析数据。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27576%27%20height=%27561%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc2IiBoZWlnaHQ9IjU2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看指标统计​

在 指标统计 页签，你可以查看评估器得分的统计数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273326%27%20height=%271724.5925925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMyNiIgaGVpZ2h0PSIxNzI0LjU5MjU5MjU5MjU5MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

上一篇

评测扣子智能体

下一篇

通过数据回流评测行程规划 Agent 的轨迹