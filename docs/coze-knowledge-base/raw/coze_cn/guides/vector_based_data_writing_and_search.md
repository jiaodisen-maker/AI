---
source_url: https://docs.coze.cn/guides/vector_based_data_writing_and_search
title: '数据向量化写入与检索 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:58Z
---

# 数据向量化写入与检索 - 文档 - 扣子

数据向量化写入与检索

在 AI 检索场景中，我们常常需要让大模型理解和检索大量的非结构化内容，如产品手册、图片库等。扣子编程支持调用向量模型，将图片、音频等非结构化的内容转换为向量并存储于数据库中，提升系统对非结构数据的召回能力。​

功能概述​

向量是描述文本、图片等对象特征的高维数值数组。 你可以把数据向量化功能想象成一个数据转化器，它能将不同类型的内容（如文档、图片）都转换为统一的数字格式—向量，让系统能跨模态做语义级检索与匹配。​

例如搜索退货需要什么流程时，扣子 AI 会将其转换为一组向量，然后与知识库中的如何申请退货？、退货的运费由谁承担？、订单发货后多久能收到？等已有问题的向量数据进行比较，并发现与 如何申请退货？ 的相似度最高（如 0.98），则大模型会基于该问题的答案生成回复。​

主要的应用场景如下：​

  * 构建私有化知识库：存储大规模的非结构化数据，搭建检索增强生成（RAG）系统，为大模型提供专业背景知识。​

  * 检索智能信息：将知识文档与用户查询均转换为向量，通过语义匹配理解用户真实意图，返回最相关的检索结果。​

  * 推荐个性化内容：将用户行为数据向量化，计算用户兴趣与内容库之间的相似度，实现精准推荐。​

  * 辅助内容创作：依据给定主题或关键词的向量表示，召回相关的上下文素材，辅助 AI 生成逻辑更严密、语境更契合的内容。​

工作流程​

1.

语义分片​

  * 在扣子 AI 对话区，输入可公网访问的文档 URL、扣子对象存储文件 URI、纯文本内容。扣子 AI 会调用内置的分片组件，将文本按语义结构切分为大小适中的片段，也支持你在对话中指定分片的分隔符和大小。​

2.

向量化处理​

  * 扣子 AI 调用内置的向量模型，将每个内容分片转化为 1024 维的向量。​

3.

写入数据库​

  * 扣子 AI 将文本片段、向量数据及其元数据（文档 ID、URI等）写入到专属的数据库。​

  * 扣子编程新增了 Knowledge 类型数据库，使数据库能够作为知识库使用，存储经向量化处理的非结构化数据。具体存储位置说明如下：​

  * 向量数据：Knowledge 数据库。​

  * 知识库导入记录：Knowledge_observability 数据库。​

  * 原始内容：对象存储的 coze_knowledge_origin 文件夹。​

4.

高效检索​

  * 扣子 AI 同样会将你输入的检索 Query 转化为向量，并利用内置的 IVFFlat 索引，在数据库中快速完成向量对比。你无需关注其技术细节，只需输入检索 Query 即可，扣子 AI 会精准锁定目标区域并避免全量数据扫描，最终召回关联度最高的内容，并将其作为大模型生成回复的依据。​

费用说明​

以下操作将消耗你的扣子积分。​

  * [编程任务](<https://docs.coze.cn/coze_pro/task_fee>)：在开发项目过程中，你与扣子 AI 的每轮对话。​

  * [内置集成](<https://docs.coze.cn/coze_pro/internal_integrations_fee>)：目前免收存储、数据库、向量模型的内置集成费用，后续正式计费的时间计划与产品定价请关注平台公告。​

使用限制​

  * 目前仅智能体、工作流支持数据向量化写入与检索功能。​

  * 不支持编辑 Knowledge 类型的数据表结构。​

  * 不支持通过可视化方式插入、删除、编辑 Knowledge 数据库表中的数据，需通过对话方式操作。​

  * 支持通过可公网访问的文档 URL、扣子对象存储的文件 URI、纯文本内容形式写入数据。如果要写入本地文件，需先上传文件到扣子对象存储服务中。​

向量化写入​

你可以通过自然语言与扣子 AI 对话，将文本内容写入数据库。​

1.

构建有效的指令。​

  * 一个清晰的指令能帮助扣子 AI 更准确地完成任务。建议指令中包含以下信息：​

  * ​

指令要素​| 说明​  
---|---  
关键词​| 明确包含知识库、向量化写入等关键词，扣子 AI 能够识别这些关键词，启动向量化写入功能。​当前项目没有 Knowledge 类型的数据库表时，系统将自动创建。​  
数据来源​| 提供你要写入的内容：​
    * 公网访问的文档 URL​
    * 扣子对象存储的文件 URI​
    * 直接粘贴纯文本内容​  
分块规则​| 指定分隔符、分片大小。未指定时，扣子 AI 会自动切分为合适的片段。​
    * 分隔符：用于分片的分隔符，例如换行符、中文句号、中文叹号、英文句号、英文叹号、中文问号、英文问号、自定义符号（如"###"）等。​
    * 分片大小：每个分片允许的最大字符数，最大为 5000 字符。​  
检索参数​| 指定检索的 Score 阈值、TopK。​
    * Score 阈值：相似度分值（如 0.7 以上），以过滤掉匹配度不高的文本。​
    * TopK：检索时返回的最相关片段数量。​  
  
​

  * 写入指令示例如下：​

  * ​

Plain Text

复制

搭建知识库智能客服Agent，支持将知识向量化写入到知识库中。​

将如下内容向量写入到知识库中，设置 Score 为 0.7，TopK 为 5。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27525%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI1IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

查看写入结果。​

  * 完成写入操作后，你可以在 Knowledge Schema 下的数据库表中，查看写入的向量数据，还可以在对象存储中查看对应的原始内容。​

  * 数据库​

  * 数据表中的 embedding 列的数据类型为 vector 类型，表示标准稠密向量，是 content 列的文本片段经向量模型处理后的向量数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271895%27%20height=%271266.3270142180095%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5NSIgaGVpZ2h0PSIxMjY2LjMyNzAxNDIxODAwOTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

对象存储​

对象存储服务中将生成如下两个文件夹：​

  * coze_knowledge_origin：存储原始内容文件。​

  * coze_knowledge_base：存储从原始文件中提取出的素材数据。例如 PDF 文件中包含图片，经处理后，提取到的图片将存储在该文件夹中。​

  * 每次部署项目时，coze_knowledge_base 文件夹中的数据都会同步到生产环境。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271882%27%20height=%27258.0520094562648%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg4MiIgaGVpZ2h0PSIyNTguMDUyMDA5NDU2MjY0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

向量化检索​

在智能体或工作流中，你可以直接输入查询内容，扣子 AI 将从海量数据中精准召回关联度最高的内容片段。最后，大模型会根据召回结果生成回复内容。​

例如在下述案例中，查询什么是扣子编程时，大模型会自动调用检索工具从数据库中检索数据，返回相似度分值（如 0.8）高的文本片段，并基于该片段生成最终回答。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27446%27%20height=%27392%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ2IiBoZWlnaHQ9IjM5MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

集成数据库能力

下一篇

集成对象存储能力