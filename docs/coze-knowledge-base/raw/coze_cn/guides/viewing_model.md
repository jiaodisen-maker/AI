---
source_url: https://docs.coze.cn/guides/viewing_model
title: '查看模型性能与用量 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:43:57Z
---

# 查看模型性能与用量 - 文档 - 扣子

查看模型性能与用量

你可以通过查看模型的性能指标和并发指标，评估模型的效率和效果。同时，你还可以通过查看用量记录，跟踪模型的使用情况，对于资源规划和成本管理至关重要。​

查看性能指标​

通过模型管理功能，你能够全面监控和评估模型的关键性能指标，包括模型的首 Token 延时、非首 Token 延时和成功率。​

说明

不同的模型，性能指标的统计方式存在差异，具体差异如下：​

  * MinMax、Kimi 模型：其性能指标是根据所有使用该模型的用户的综合数据而统计。​

  * 豆包模型：豆包模型的性能指标是根据空间内所有成员使用该模型的综合数据而统计。因此，即使是查看同一豆包模型，不同空间的用户查看的性能指标数据也可能存在差异。​

​

​

指标​| 说明​| 统计频率​  
---|---|---  
首 Token 延时​| 记录用户输入 Prompt 到模型输出第一个 token 所需时间，单位为毫秒。​首 Token 延时越低，代表模型的响应速度越快，用户的体验越好。​| 每 10 分钟统计一次。​  
非首 Token 延时​| 记录模型完成首 token 输出后，后续输出每个 token 所需的平均时长，不包括首 token 输出，单位为毫秒。​| 每 10 分钟统计一次。​  
成功率​| 记录模型调用成功次数占总调用次数的比例。​| 每 10 分钟统计一次。​  
  
​

通过综合考量这些性能指标，你可以对模型的整体表现有一个清晰的认识，并据此进行优化和调整。​

参考以下操作，查看模型的性能指标。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在顶部工作空间列表中，单击目标工作空间对应的当前空间管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27190%27%20height=%27213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwIiBoZWlnaHQ9IjIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

3.

在模型管理页面的模型列表中，单击目标模型。​

4.

在模型详情页，单击性能监控，查看各性能指标。​

  * 统计图表中支持展示性能指标的平均值、P60 值、P95 值、P99 值，用于反映指标的分布集中程度。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27679%27%20height=%27529%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc5IiBoZWlnaHQ9IjUyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看用量记录​

你可以通过用量记录看板追踪模型的用量，包括当前空间下模型每天处理的 tokens 数量以及当前模型在不同智能体、工作流中的具体用量，为资源管理与成本优化提供数据支撑。​

​

图表名称​| 说明​| 应用场景​  
---|---|---  
用量统计​| 系统会分别统计每天智能体输入和输出的 tokens 数量以及工作流输入和输出的 tokens 数量，并将这些数据汇总，得到当天 tokens 总量并展示。​用量统计图表支持展示最近 7 天的用量记录。​说明当天的用量记录可能存在延时，仅供参考。企业版（标准版、旗舰版）的模型用量可查看[方舟用量统计](<https://console.volcengine.com/ark/region:ark+cn-beijing/usageTracking>)。​​| 

  * 评估模型的使用频率和活跃度，便于你理解模型在实际应用中的负载情况。​

  * 通过监控 tokens 处理量，你可以预测资源需求，优化成本控制，并确保模型在高流量情况下的性能和稳定性。​

  
用量详情​| 用量详情图表展示了指定月份内，该模型在当前工作空间下的不同智能体、工作流中的具体用量，包括输入 tokens、输出 tokens、消耗 tokens。同时，支持按照输入 tokens、输出 tokens、消耗 tokens 维度进行排序。​​| 

  * 便于查询当前模型在不同智能体、工作流中的具体用量。​

  * 快速识别模型用量最高的智能体、工作流，便于资源规划和成本管理。​

  * 为模型下架或替换场景，提供排查的参考依据。​

  
  
​

参考以下操作，查看模型的用量记录。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在顶部工作空间列表中，单击目标工作空间对应的当前空间管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27190%27%20height=%27213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwIiBoZWlnaHQ9IjIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

3.

在模型管理页面的模型列表中，单击目标模型。​

4.

在模型详情页，单击用量记录，查看用量统计和用量详情图表。​

  * 单击指定智能体或工作流用量细则列的查看，可以查看当前模型在指定智能体或工作流中的每日用量及变化趋势。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272365%27%20height=%271025.580568720379%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2NSIgaGVpZ2h0PSIxMDI1LjU4MDU2ODcyMDM3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272270%27%20height=%27563.4751773049645%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI3MCIgaGVpZ2h0PSI1NjMuNDc1MTc3MzA0OTY0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

查看并发监控​

通过并发监控看板，你可以查看模型的 RPM 限额和 TPM 限额，以及模型实际运行的 RPM、TPM 数据。这些数据可帮助你了解模型运行状态，作为未来资源规划的依据。​

​

指标​| 说明​  
---|---  
RPM​| RPM 表示模型每分钟能处理的请求次数，是衡量模型的响应能力和处理速度的重要指标。​RPM 图表包含当前账号所有空间下使用该模型的请求，你可以通过 RPM 图表查看分钟级、日级的模型 RPM 变化趋势。​  
TPM​| TPM 表示模型每分钟消耗的 Tokens 数量，是衡量模型处理能力的重要指标。​TPM 图表包含当前账号所有空间下使用该模型的请求，你可以通过 TPM 图表查看分钟级及天级的模型 TPM 变化趋势。​  
  
​

参考以下操作，查看模型的并发监控指标。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在顶部工作空间列表中，单击目标工作空间对应的当前空间管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27190%27%20height=%27213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwIiBoZWlnaHQ9IjIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

3.

在模型管理页面的模型列表中，单击目标模型。​

4.

在模型详情页，单击并发监控，查看模型的 RPM 和 TPM 指标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27728%27%20height=%27412%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzI4IiBoZWlnaHQ9IjQxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

如何快速切换待下架模型？​

当你使用的模型即将下架时，可以采用以下两种方式为低代码项目替换模型，以确保服务的连续性。​

  * 方式一：逐个替换​

  * 项目的创建者可以在用量详情图表中，快速定位调用了待下架模型的智能体或工作流，并逐个为它们切换模型。此操作仅更新编排页面中的模型，替换后需要重新发布。​

  * 方式二：批量替换​

  * 工作空间的所有者或管理员可以在用量详情图表中，快速定位当前工作空间下所有使用该模型的智能体或工作流，并批量为这些项目的线上版本切换模型。​

方式一：逐个替换

方式二：批量替换

建议结合 tokens 消耗数据排序，优先替换高频高消耗智能体或工作流中的模型。​

说明

本步骤仅适用于低代码智能体或工作流，且仅限其创建者可以替换模型。​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在顶部工作空间列表中，单击目标工作空间对应的当前空间管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27131%27%20height=%27230%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMxIiBoZWlnaHQ9IjIzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在模型管理页面的模型列表中，单击待替换的目标模型。​

4.

在用量记录页签下，找到用量详情图表。​

5.

单击输入 tokens、输出 tokens 或 消耗 tokens 列的排序按钮，定位 tokens 消耗高的智能体或工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27377%27%20height=%27196%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc3IiBoZWlnaHQ9IjE5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

单击目标智能体或工作流的名称，跳转至对应的智能体、工作流编排页面，进行模型替换。​

  * 替换模型后，请确认试运行无误，并及时发布智能体或工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27183%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUwIiBoZWlnaHQ9IjE4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27344%27%20height=%27249%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ0IiBoZWlnaHQ9IjI0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

接入自定义模型

下一篇

模型常见问题