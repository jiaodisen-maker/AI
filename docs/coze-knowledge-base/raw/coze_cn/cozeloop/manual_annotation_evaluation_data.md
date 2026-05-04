---
source_url: https://docs.coze.cn/cozeloop/manual_annotation_evaluation_data
title: '人工标注评测数据 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:35Z
---

# 人工标注评测数据 - 文档 - 扣子

人工标注评测数据

扣子罗盘评测能力支持人工标注与校准，你可以：​

  * 人工校准评估器机评结果：当你认为系统评分不准确时，可在数据明细列表或详情页中直接修改评分并记录校准原因，校准后可随时查看历史记录与原因，且指标统计页面会同步展示校准后的聚合得分（略有延迟）。​

  * 人工标注新指标：当你需要在实验报告上建立新的评估指标，并引入业务专家进行打标时，平台提供了人工标注功能。你可通过普通模式在详情页标注，或开启快速标注模式在数据明细页直接操作，可添加预设标签或自定义新标签进行分类与备注。此外，基于人工标注结果，你能通过过滤器筛选特定数据，如筛选人工校准数据或指定标签数据，并在指标统计页查看聚合得分与数据分布，为业务决策提供精准数据支持。​

人工标注新指标​

扣子罗盘支持对评测实验的运行结果进行人工标注，例如通过 “功能模块” 标签进行分类，或通过文本标签记录备注信息等等。评测实验运行结果支持以下两种人工标注方式：​

  * 普通模式：正常展示评测实验的运行结果，需要在评测数据详情页进行人工标注。​

  * 快速标注模式：可直接在当前页面中快速标注，无需跳转详情页，适用于快速、批量标注的场景。​

人工标注评测实验数据的操作步骤如下：​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择一个空间。​

2.

在左侧导航栏，选择评测 > 实验，然后单击实验名称。​

3.

在数据明细页签中，单击人工标注管理。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27329%27%20height=%27155%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/821c0595216247a0861ae96cc7e64de5~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

导入标签。​

  * 在标签列表中输入标签名称，搜索想要添加的标签，并单击添加。此步骤会将定义好的标签添加到指定的评测实验中，如果没有合适的标签，也可以根据页面提示定义一个新的标签。定义标签的操作步骤可参考​步骤一：创建标签。​

  * 如果没有合适的标签，也可以根据页面提示定义一个新的标签。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27306%27%20height=%27167%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2IiBoZWlnaHQ9IjE2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

对实验运行结果进行人工标注。​

  * 快速标注模式：​

  * 添加标签后，默认进入快速标注模式，数据明细页签中会新增一列，名为标签名称，你可以在标签列中设置标签值，完成该条数据的人工标注。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271390%27%20height=%27622.3202614379085%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM5MCIgaGVpZ2h0PSI2MjIuMzIwMjYxNDM3OTA4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

普通模式：​

普通模式下数据展示更简洁，如果你选择普通模式，则需要进入详情页，在人工标注区域设置标签值。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27277%27%20height=%27158%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc3IiBoZWlnaHQ9IjE1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

对每一行运行结果进行人工标注之后，可以基于人工标注结果筛选数据，也可以在指标统计页签中查看聚合得分、数据项分布等明细数据。​

人工校准评测得分​

发起评测实验之后，扣子罗盘会根据评估器设置的规则，在各个评分维度上对评测结果逐个打分。扣子罗盘现已支持评测得分的人工校准，如果你认为大模型评分结果不准确，可以通过人工校准修改评分。人工校准得分之后，你还可以查看人工校准结果、校准原因，指标统计页面也会展示人工校准的聚合得分结果。​

人工校准数据方式：​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，在左侧导航栏顶部，选择一个空间。​

2.

在左侧导航栏，选择评测 > 实验，然后单击实验名称。​

3.

在数据明细页签中，查看评测实验的 input 和 output，结合评测数据、评测对象的实际输出，根据业务专家经验，检查异常得分，并进行校准。​

4.

如果认定裁判模型的评分不准确，可以通过以下方式人工校准：​

  * 在数据明细列表中直接校准：找到评估器一列，单击人工校准图标，设置评分，并填写人工校准的原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27414%27%20height=%27147%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE0IiBoZWlnaHQ9IjE0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 在详情页中校准：在操作列单击详情，进入评测数据的详情页，展开评估器得分区域，在得分列中单击人工校准图标，设置评分，并填写人工校准的原因。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27270%27%20height=%27151%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcwIiBoZWlnaHQ9IjE1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

人工校准之后，你可以在评测数据列表中查看人工校准的历史记录。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27506%27%20height=%27152%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA2IiBoZWlnaHQ9IjE1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

基于标注筛选数据​

扣子罗盘支持基于人工标注的结果对实验运行结果进行筛选和过滤，例如筛选出标签为功能模块：API 的运行结果、筛选出对评测得分进行人工校准的运行结果等。​

你可以在数据明细页签中，单击过滤器，并设置筛选条件。人工校准场景下，支持的筛选项包括：​

  * 是否人工校准得分：筛选出对评测得分进行人工校准的运行结果，分析裁判模型评分不准确的原因，以便后续定向提升和优化。​

  * 人工标注：基于人工标注的结果进行筛选，例如筛选指定标签值的数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271397%27%20height=%27357.5162721893491%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM5NyIgaGVpZ2h0PSIzNTcuNTE2MjcyMTg5MzQ5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

标注数据统计​

对每一行运行结果进行人工标注之后，你可以在指标统计页签中查看聚合得分、数据项分布等明细数据，查看人工校准后的整体数据统计结果，进而支撑业务决策。​

聚合得分：​

查看本次实验中，评测对象在各个评估指标上的聚合得分，此得分是人工校准后的聚合得分。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271220%27%20height=%27602.560975609756%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIyMCIgaGVpZ2h0PSI2MDIuNTYwOTc1NjA5NzU2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

得分明细 - 数据项分布​

查看本次实验中，评测对象的所有评测数据，在各个评估指标上的得分分布占比。除指定评估器的得分以外，也会展示每个标签的标注结果分布。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271595%27%20height=%27461.9664634146341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU5NSIgaGVpZ2h0PSI0NjEuOTY2NDYzNDE0NjM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

管理实验

下一篇

轨迹评测介绍