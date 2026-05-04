---
source_url: https://docs.coze.cn/cozeloop/dataset_ai_synthesis
title: '智能合成评测数据 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:25Z
---

# 智能合成评测数据 - 文档 - 扣子

智能合成评测数据

智能合成评测数据旨在帮助大模型应用开发者与评测人员解决高质量评测数据不足的问题。它支持你通过描述业务场景，快速、低成本地一键生成可直接用于评测实验的问答数据集。​

功能介绍​

智能合成评测数据是一项数据生成服务，旨在帮助你快速、低成本地打造高质量的评测数据。该功能以已有的评测数据作为种子数据，借助 LLM 能力来智能合成更高质量的多样本数据，解决评测数据匮乏或质量不佳的问题。适用场景如下：​

  * 对线上真实数据泛化和增强：如果线上回流的 badcase 数量级较小或覆盖不足，可以快速泛化并合成更多的数据用于评测或精调。​

  * 补齐稀缺和控制数据分布：当已有的评测数据稀缺、长尾占比高、或需要控制数据分布时，通过占比配置与分类来源（标签、已有列、自定义分类），将合成数据分布锚定到你期望的线上画像或实验目标。​

  * 合成对抗测试样本：针对罕见与高风险场景（如对抗性输入、极端条件、复杂推理链），合成对抗测试样本，帮助挖掘模型或Agent薄弱点并强化。​

前提条件​

在开始使用本功能前，请确保你已满足以下条件：​

  * 已创建文本类型的评测集。多模态评测集暂不支持智能合成。​

  * 评测集中已存在高质量、覆盖面广的评测数据。评测数据内容越丰富，合成数据质量越高，建议准备 20 条以上的评测数据作为智能合成的样本。​

操作步骤​

步骤一：创建智能合成任务​

1.

访问[扣子罗盘](<https://loop.coze.cn>)。​

2.

在左侧导航栏顶部，选择一个空间。​

3.

在左侧导航栏，选择评测 > 评测集，然后进入智能合成页签。​

4.

单击智能合成。​

  * 你也可以在评测集页面中点击添加数据 > 智能合成。​

  * 添加智能合成数据：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271261%27%20height=%27449.46534653465346%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI2MSIgaGVpZ2h0PSI0NDkuNDY1MzQ2NTM0NjUzNDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

智能合成页面：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271268%27%20height=%27312.12307692307695%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI2OCIgaGVpZ2h0PSIzMTIuMTIzMDc2OTIzMDc2OTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

5.

填写合成场景集来源，并单击下一步。​

  * ​

配置项​| 说明​  
---|---  
合成场景​| 固定为基于种子数据泛化，表示从真实数据中学习本质特征，从而合成数据。​  
场景和用途描述​| 描述你的业务场景与评测数据用途。​建议采用”行业领域 + 业务场景 + 目标“的结构描述业务场景，有助于模型生成与业务需求精准适配的数据，例如”该数据集主要用于评测“舆情检测和分析”的AI机器人，需要进行情感色彩监测的文章、社媒观点或网友评论等。“​  
种子数据​| 选择用于智能合成的评测集作为种子数据，用于模型分析与学习。默认选择草稿版本，你也可以切换为其他版本。​说明建议种子数据至少包含 20 条样本，数据内容越丰富，合成数据质量越高。​​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27584%27%20height=%27358%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg0IiBoZWlnaHQ9IjM1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

填写合成样本配置，并单击开始合成。​

  * ​

配置项​| 说明​  
---|---  
需合成的列​| 需要通过此功能智能合成的评测集列。页面会展示评测集中已有的列名，你需要选择待合成的列名，或者单击添加列来合成新的列，并填写描述和合成要求，帮助模型理解如何合成新的数据。​
    * 描述：评测集列的含义。​
    * 合成要求：描述智能合成的要求，如场景侧重、特征分布、详略程度等。​
    * 模型智能合成思路（自动）：系统自动生成的新列，表示模型合成这条数据的思考过程，可选是否添加到评测集，默认不添加。​
说明
    * 仅支持合成 String 类型数据，暂不支持多模态列。​
    * 为了保障合成数据的效果，建议仔细填写描述和合成要求。​
​  
合成样本数​| 合成的样本数量。取值范围为 1~1000 之间的正整数。​建议合成样本数最好不要超过种子数据的 10 倍，否则会导致泛化能力不足、数据相似度较高。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27486%27%20height=%27327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg2IiBoZWlnaHQ9IjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：查看合成进度和结果​

1.

进入智能合成任务详情页。​

  * 成功创建合成任务之后，页面会自动跳转至智能合成详情页，你也可以在评测集的智能合成页签中找到这个任务，单击任务名称进入详情页。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27684%27%20height=%27204%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg0IiBoZWlnaHQ9IjIwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

查看任务进度和结果。​

  * 智能合成详情页会展示本次智能合成任务的进展和结果，你也可以打开任意条目，查看合成的数据内容质量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27752%27%20height=%27374%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUyIiBoZWlnaHQ9IjM3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：导出到评测集​

智能合成的评测数据默认不保存到评测集，你可以仔细查看数据质量，对于合成效果不错、符合评测需求的数据，你可以选择手动将其导出到评测集，以供评测实验使用。​

1.

在智能合成详情页数据项页面选择需要导出的数据。​

2.

在页面右上角单击导出所选数据。​

  * 如果计划导出智能生成的全部数据，可以直接在页面右上角单击导出全部数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27328%27%20height=%27189%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI4IiBoZWlnaHQ9IjE4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

填写以下配置，并单击确定。​

  * ​

配置项​| 说明​  
---|---  
目标评测集​| 用于接收智能合成数据的评测集。支持导出到新的评测集或导出到一个已有的评测集。​如果选择导出到已有评测集，则应设置评测集的名称。​  
更新模式​| 智能合成数据在评测集的保存方式：​
    * 追加更新：智能合成数据会追加到已有评测集的末尾。​
    * 覆盖更新：智能合成数据会覆盖已有评测集的全部数据。​  
字段映射​| 配置智能合成数据和目标评测集字段的映射关系。注意字段的数据类型应完全一致。​  
  
​

4.

成功导出后，你可以在目标评测集的评测集页签中查看到已添加的智能合成数据。​

​

上一篇

向评测集添加多模态数据

下一篇

管理自建评估器