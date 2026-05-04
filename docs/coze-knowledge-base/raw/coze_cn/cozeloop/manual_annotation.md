---
source_url: https://docs.coze.cn/cozeloop/manual_annotation
title: '人工标注 Trace - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:53Z
---

# 人工标注 Trace - 文档 - 扣子

人工标注 Trace

人工标注 Trace 是扣子罗盘提供的一项用于对 Trace 数据进行精细化标注与管理的工具。本文将详细介绍如何对 Trace 数据进行人工标注。​

Trace 数据通常记录了系统或应用的调用链路、输入输出、执行状态等关键信息，是反映业务运行过程与结果的重要依据。而人工标注则是通过人工介入的方式，为这些数据添加定制化标签，实现对数据的深度解读与特征提炼。 ​

通过自定义标签并对具体 Trace 数据进行标注，你可以更精准地对业务数据进行分类、评分或补充说明。例如用 “准确性” 标签为模型输出打分，用 “场景类型” 标签区分不同业务场景下的调用，或用文本标签记录人工校验后的备注信息。这些标注结果将为后续的数据分析、模型评测与优化提供可靠的人工标注依据，帮助你快速定位问题数据、总结规律特征，进而提升业务迭代效率。 ​

步骤一：创建标签​

在人工打标之前，你需要先在工作空间中定义标签。例如创建一个标签名为“准确性”，类型为数字，表示对准确性进行打分，后续再标注 Trace 时可以选择“准确性”作为标签，并输入具体的准确性分值为标签值。​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，并使用扣子账号登录。​

2.

在左侧导航栏顶部，选择一个工作空间。​

3.

在左侧导航栏，选择标签管理。​

4.

在页面右上角单击新建标签。​

5.

填写标签配置，并单击创建。​

  * ​

配置​| 说明​  
---|---  
标签名称​| 标签的名称，50字以内，工作空间内唯一。​  
描述​| 标签的描述信息，用于标识标签的用途及使用方式。​  
标签类型​| 标签的类型，目前支持以下类型的标签，用于满足不同场景下的标注需求。​
    * 分类：常用于对 Trace 数据进行分类的场景，例如“批次一”，“批次二”。​
    * 布尔：常用于如“赞”或者“踩”，“是”或者“否”等二选一场景下的标注。​
    * 数字：常用于对 Trace 数据进行打分，例如 100、95。​
    * 文本：常用于纯文本类型的标注，对文本内容没有明确的限制。​  
  
​

  * 配置示例如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27435%27%20height=%27381%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM1IiBoZWlnaHQ9IjM4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

成功创建标签之后，你可以在标签列表中查看已创建的标签，还可以进行以下操作：​

  * 修改标签：在标签列表的操作列中单击详情，即可跳转到标签配置页面修改标签。修改完毕后在页面右上角单击保存。注意修改标签后，存量已打标数据将会自动同步更新。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27524%27%20height=%27122%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI0IiBoZWlnaHQ9IjEyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 查看修改记录：编辑标签时，可以在页面右上角单击修改记录，查看此标签的每一次修改记录，包括提交时间、提交人和具体改动。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27507%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA3IiBoZWlnaHQ9IjI1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：标注 Trace​

在工作空间中定义标签之后，就可以进入 Trace 列表页面查看指定应用上报的 Trace 数据，并开始标注。​

1.

在扣子罗盘观测 > Trace 页面，通过筛选器找到想要人工标注的 Trace 数据。​

  * 例如，筛选出最近 3 天的 Coze 智能体 Trace 数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27495%27%20height=%27232%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk1IiBoZWlnaHQ9IjIzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在筛选出的 Trace 列表中，单击任意一条 Trace，进入其详情页面。​

3.

仔细查看该条 Trace 数据的调用树，检查 input、output，开始标注。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27511%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTExIiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在页面右上角单击标注数据，选择一个已创建的标签，并填写标签值，也就是标注结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27524%27%20height=%27243%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI0IiBoZWlnaHQ9IjI0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：查看标注结果​

人工标注时，Trace 详情页面会自动保存标注结果，你可以在 Trace 详情页面的 Feedback 页签中查看标注结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27548%27%20height=%27236%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ4IiBoZWlnaHQ9IjIzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

也可以在 Trace 列表页，基于标注的结果对 Trace 列表进行筛选。筛选时，筛选项选择 Feedback-人工标注即可。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271668%27%20height=%27588.8194444444445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY2OCIgaGVpZ2h0PSI1ODguODE5NDQ0NDQ0NDQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

后续操作​

人工标注完成后，你可以将人工标注作为筛选条件，将满足条件的 Trace 数据添加到评测集，基于标注后的数据更高效地完成后续的评测与调优。Trace 数据回流的操作步骤可参考​Trace 数据回流。​

​

上一篇

Trace 自动评测

下一篇

Trace 数据回流