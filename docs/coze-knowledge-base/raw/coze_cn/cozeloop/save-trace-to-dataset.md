---
source_url: https://docs.coze.cn/cozeloop/save-trace-to-dataset
title: 'Trace 数据回流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:55Z
---

# Trace 数据回流 - 文档 - 扣子

Trace 数据回流

在 AI 应用场景中，离线评测往往难以全部覆盖线上用户真实的问题场景，需要回流线上用户的真实请求数据，补充评测集或训练集，用于 AI 应用、Prompt 策略或模型的效果评测，便于后续的效果优化迭代。​

扣子罗盘支持将 Trace 数据手动沉淀到评测集，提升数据质量，便于后续开展评测实验，优化 AI 应用表现。例如将线上真实的高质量问答对数据，沉淀为基准评测集；将评测分数低、耗时长、耗费 Tokens 多、应用输出不符合预期等类型的 Badcase，分类沉淀为问题数据集。高质量的基准评测集后续可用于验证新版本应用的效果。​

说明

回流观测数据之前，应确认：​

  * 你的 AI 应用已接入扣子罗盘，并上报了观测数据，详细配置方式可参考​数据上报概述。​

  * 可在观测页面查看到观测数据，详细操作步骤可参考​查看 Trace 数据。​

​

使用限制​

回流 Trace 数据之前，建议先了解以下限制：​

​

限制​| 说明​  
---|---  
单次回流的数据量​| 每次回流最多选择 200 条 Trace 数据。如需导入更多数据，建议分批次进行。​  
单条 Trace 数据大小​| 上限为 200KB，超出上限的 Trace 数据会回流失败。​  
数据类型​| 配置 Trace 数据字段和评测集字段的映射关系时，应确认写入前后的数据类型完全一致，否则可能因数据类型不匹配导致数据回流失败。例如回流的 Trace 字段是Input.name，数据类型为 String，评测集已有列数据类型为 Float，无法转换，则可能导致回流失败。​  
评测集上限​| 每个评测集行数最多 5000 行。如果 Trace 数据导入期间并发写入了其他数据，使评测集行数超过 5000 行，会导致数据回流失败。建议控制评测集的写入并发操作。​  
  
​

步骤一：选择 Trace 数据​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，并使用扣子账号登录。​

2.

在左侧导航栏顶部，选择一个工作空间。​

3.

在左侧导航栏，选择观测 > Trace，并使用过滤器筛选出 Trace 数据。​

4.

在页面右上角单击添加到评测集。​

5.

选择需要回流的 Trace 数据，并再次单击添加到评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27677%27%20height=%27225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc3IiBoZWlnaHQ9IjIyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：配置回流规则​

页面自动跳转至Trace添加到评测集页面，你需要在页面左侧确认样本 span 是否准确，确认无误后根据页面提示配置回流规则。​

​

配置​| 说明​  
---|---  
目标评测集​| Trace 数据要写入的评测集。支持写入一个已有的评测集，或者写入新的评测集。​暂不支持选择数据行达到上限（5000 行）的评测集，除非全量覆盖已有的评测数据。​  
导入方式​| Trace 数据导入评测集的方式，支持追加数据或全量覆盖。​

  * 追加数据：在评测集已有数据行下新增 Trace 数据。应确保导入 Trace 数据后，评测集的数据行数不超过容量上限（5000 行）。​

  * 全量覆盖：清除评测集已有数据行后，新增数据。​

  
字段映射​| 选择需要回流的 Trace 数据字段和评测集字段的映射关系。你可以在左侧确认查看样本 span 的字段名称及字段值，选择对应的字段进行配置。​

1.选择需要回流的 Trace 字段。支持回流 Trace 的 Input、Output、Tags 和轨迹（Trajectory）信息，默认回流 Input、Output 的完整内容。支持新增回流字段。你也可以通过.+字段名的方式下钻提取特定字段内容，详细说明可参考​配置回流字段映射关系时，如何下钻提取字段？​

  * 说明关于如何回流轨迹数据，参见 ​通过数据回流评测行程规划 Agent 的轨迹。​​

2.为各个 Trace 字段设置对应的评测集字段，即需要将选定的Trace字段回流到评测集具体哪一列。支持选择回流到评测集已有列或新增列，不支持多个Trace字段回流到评测集同一列。​

  * 如果选择回流到已有列，已有列的数据类型不支持修改，数据类型不一致可能导致回流失败。例如回流的Trace字段是Input.name，数据类型为 String，评测集已有列数据类型为 Float，无法转换，则可能导致回流失败。​

  * 如果选择回流到新增列，需要选择新增列数据类型，列名不允许与评测集已有列重名。​

  
  
​

配置示例如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27612%27%20height=%27417%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEyIiBoZWlnaHQ9IjQxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：导入评测集​

1.

校验并预览效果。​

  * 在页面下方单击校验并预览。在效果预览页面查看待写入评测集各个字段的 Trace 数据内容是否正确。如果写入评测集字段的内容不准确，可以单击关闭，修改回流规则中的字段映射关系。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27509%27%20height=%27284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA5IiBoZWlnaHQ9IjI4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

如果确认无误，关闭预览页面，并单击开始导入。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27516%27%20height=%27351%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE2IiBoZWlnaHQ9IjM1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

查看导入结果。​

  * 导入完毕后，页面会提示导入结果，包括导入的总条数及成功条数。如果某些数据导入失败，你可以查看失败原因。通常情况下，失败原因是未遵循观测数据回流的使用限制，详细限制说明可参考​使用限制。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27383%27%20height=%27370%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgzIiBoZWlnaHQ9IjM3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

查看评测集。​

  * 你可以在执行结果页面单击查看评测集，查看已导入评测集的 Trace 数据。​

常见问题​

如果页面提示超出评测集上限，如何处理​

配置回流规则时，如果导入方式设置为追加数据，应确保导入 Trace 数据后，评测集的数据行数不超过容量上限（5000 行）。​

如果页面提示超出评测集上限，你可以尝试以下方案。​

  * 返回 Trace 列表页，减少回流数据量级。​

  * 更换数据导入方式，选择全量覆盖。​

  * 说明

进行全量覆盖操作后，现有的评测数据将被覆盖。请务必谨慎执行此操作，以避免数据丢失。​

​

  * 更换导入的目标评测集。​

配置回流字段映射关系时，如何下钻提取字段？​

通过.+字段名的方式下钻提取特定字段内容，例如：​

  * 希望回流input.query.content信息，只需要输入input.query.content 即可回流。​

  * 除回流Input.name信息外，还希望回流Input里的description信息和Tags里的tokens信息，只需要新增字段映射行，分别输入Input.description和Tags.tokens 即可。​

  * 扣子罗盘支持模糊搜索，输入关键词时系统会自动查找相关的字段。当然，你也可以指定一个不在样本 span 中的新字段，但是配置时无法预览 value 值。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271092%27%20height=%27855.6527777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA5MiIgaGVpZ2h0PSI4NTUuNjUyNzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

人工标注 Trace

下一篇

火山智能体注册