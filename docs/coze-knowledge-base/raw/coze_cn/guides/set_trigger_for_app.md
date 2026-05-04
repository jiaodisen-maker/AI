---
source_url: https://docs.coze.cn/guides/set_trigger_for_app
title: '为应用设置触发器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:37Z
---

# 为应用设置触发器 - 文档 - 扣子

为应用设置触发器

在扣子编程中，触发器通常指的是低代码应用中的自动运行机制，它不需要用户直接调用，而是在满足特定条件时自动触发、运行指定的工作流。触发器可以用于实现自动化流程，例如指定低代码应用每天 10:00 搜索新闻、每日更新用户的个性化书单等等。​

触发器介绍​

低代码应用支持设置定时触发器，开发者或低代码应用的用户均可以设置触发时间和对应的处理逻辑，成功发布后，低代码应用会在指定的触发时间执行对应的处理逻辑。低代码应用的触发器通常用于执行定时任务，例如每天定时获取热点新闻、定时生成每日海报等。​

低代码应用提供以下两种类型的触发器：​

  * 预设触发器：由开发者在搭建低代码应用时设置的触发器，发布低代码应用之后将定期执行。预设触发器在所有支持触发器的发布渠道均生效，面向所有用户。​

  * 用户触发器：发布低代码应用后，由低代码应用的用户设置的触发器，根据用户所在时区在指定时间执行某个工作流，仅面向用户本人。​

说明

  * 低代码应用的触发器目前仅支持定时触发。如需事件触发，可以在用户界面中设计一个按钮，绑定事件触发某个工作流。​

  * 低代码应用的触发器暂不支持主动推送消息，目前仅用于定时处理和记录离线数据。例如你可以使用触发器来新增或更新数据库、变量中的数据，再通过另一个工作流来主动获取数据库中的最新数据。​

  * 为低代码智能体或应用设置触发器后，其关联工作流中插件节点的授权操作以及问答节点、输入节点将运行异常。​

  * 触发器的时间间隔不可少于 1 分钟。​

​

预设触发器​

预设触发器指的是低代码应用的开发者在开发过程中提前设置好的触发器，发布低代码应用后，触发器定时执行某个指令。​

设置方式​

你可以在工作流的开始节点中，为应用配置一个触发器。​

1.

在低代码应用的业务逻辑页面，新建或选择一个已有的工作流。​

2.

在工作流开始节点的触发器页签中，打开触发器设置，并设置时区、触发时间及参数值。​

  * ​

配置项​| 说明​  
---|---  
时区​| 触发器的运行时区，建议根据低代码应用的用户所在时区设置，确保定时任务在正确的时间启动。​  
触发时间​| 触发器的触发时间，触发时自动执行这个工作流。可以选择预设的时间选项（如每天 18 点），也可以使用 Cron 表达式来自定义复杂的时间。其中，Cron 表达式支持 AI 自动生成。​  
参数​| 工作流开始节点的输入参数及其参数值。如果是必选参数，需指定工作流运行时必选参数的值。​  
  
​

设置完成后，应用会在指定时区的指定时间点自动运行这个工作流。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271556%27%20height=%27949.049645390071%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1NiIgaGVpZ2h0PSI5NDkuMDQ5NjQ1MzkwMDcxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271559%27%20height=%27715.0023640661939%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1OSIgaGVpZ2h0PSI3MTUuMDAyMzY0MDY2MTkzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

示例​

例如为 AI 助手添加每日 10:00 总结热点新闻的功能，可以通过预设触发器实现。​

创建一个工作流 getDailyNews，开始节点设置触发器，每日10点获取当天的热点新闻，大模型总结后输出到结束节点。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271329%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyOSIgaGVpZ2h0PSIyNTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

开始节点的触发器设置如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27377%27%20height=%27428%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc3IiBoZWlnaHQ9IjQyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

用户触发器​

用户触发器指工作流运行过程中，由低代码应用的用户根据实际需求动态创建并管理的触发器。开发者可以在工作流中灵活编排触发器节点，为用户提供个性化的体验。例如在一个英语学习的低代码应用中，预设了一个定时任务，每天更新 10 个单词解析，支持每个用户可以选择是否设置触发器，A 用户可以开启触发器，每天 10 点学习 10 个单词，B 用户可以不设置每日学习任务。​

设置方式​

在工作流中添加设置定时触发器节点，工作流运行到此节点时，自动为指定用户添加定时任务，在指定的时间调用某个已编排好的工作流。设置定时触发器节点可用于创建一个触发器，或更新一个已创建的触发器。创建触发器时需要指定触发器名称和触发时间，并为触发器绑定一个工作流。关于设置定时触发器节点的详细说明，可参考​设置定时触发器节点。​

说明

触发器 ID 为扣子编程自动生成，不支持手动设置。创建触发器时无需设置触发器 ID，系统会自动生成一个 ID，更新触发器时才需要指定触发器 ID 来修改触发器的配置。​

​

例如参考​示例创建一个工作流 getDailyNews，但开始节点不设置触发器。另外创建一个工作流 setTrigger，其中包含设置定时触发器节点，触发器的对应行为是每天 10 点调用工作流 getDailyNews。为工作流 setTrigger 绑定用户界面中的某个按钮，当用户单击此按钮时自动创建一个触发器。​

setTrigger 的编排如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271609%27%20height=%27308%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYwOSIgaGVpZ2h0PSIzMDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

设置定时触发器节点的配置示例如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27263%27%20height=%27435%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYzIiBoZWlnaHQ9IjQzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

相关操作​

  * 查看触发器列表：在​设置定时触发器节点可查看通过设置定时触发器节点设置的触发器列表，列表中展示触发器的 ID、名称、创建时间、触发时间、用户 ID。还可以在操作列运行一次触发器，或删除指定的触发器。​

  * 查询定时触发器：通过​查询定时触发器节点可查看指定用户对应的触发器，可查看所有触发器或指定 ID 查看某个触发器。​

  * 删除定时触发器：通过​删除定时触发器节点可以删除指定用户对应的所有触发器。可删除所有触发器或指定 ID 删除某个触发器。​

  * 试运行触发器：试运行​设置定时触发器节点会同步创建一个触发器，如需立即调试触发器、查看执行效果，可以在此节点的配置页面顶部单击查看，找到已创建的触发器，并单击执行图标。触发器成功执行后，你可以在用户界面页签的预览模式下查看执行效果。​

上一篇

为低代码应用添加数据库

下一篇

用户界面编辑器概述