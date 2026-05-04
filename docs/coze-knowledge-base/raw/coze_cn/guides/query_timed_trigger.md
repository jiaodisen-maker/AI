---
source_url: https://docs.coze.cn/guides/query_timed_trigger
title: '查询定时触发器节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:25Z
---

# 查询定时触发器节点 - 文档 - 扣子

查询定时触发器节点

查询定时触发器节点用于查看指定用户的触发器。​

节点说明​

和低代码智能体一样，低代码应用也支持设置定时触发器，在指定的时间点触发定时器调用某个工作流。设置定时触发器用于用户主动设置触发器的场景，例如在一个英语学习的 AI 应用中，每个用户都可以创建自己的学习计划，A 用户可以要求每天 10 点学习 10 个单词，B 用户可以要求 12 点学习 5 个。关于低代码应用触发器的详细说明，可参考​为应用设置触发器。​

通过​设置定时触发器节点节点创建触发器之后，可以通过查询定时触发器节点查看指定用户的触发器，支持查看某个触发器的详情，也可以查看触发器列表。​

说明

设置定时触发器等触发器节点仅支持在低代码应用中创建或使用，包含触发器节点的工作流无法添加到智能体中。​

​

设置节点参数​

输入​

查询定时触发器节点预设多个参数，配置说明如下:​

​

参数​| 说明​  
---|---  
id​| 触发器的 ID，是触发器在扣子编程中的唯一标识，由扣子编程自动创建。可以通过设置定时触发器节点的输出参数中获取，也可以先不指定 id，查看此用户的所有触发器详情，详情中包括每一个触发器的 ID。​说明

  * 未指定 id 时，此节点返回指定用户的所有触发器。​

  * 指定 id 时，此节点仅返回指定触发器的详细信息。​

​  
用户id​| 使用触发器的扣子用户 ID，此触发器仅对该用户生效。低代码应用的系统变量 sys_uuid 可以用来标识用户，你可以使用变量节点获取系统变量 sys_uuid 的值，并赋值给设置定时触发器节点的用户id 参数。​  
  
​

输出​

查询定时触发器节点固定的输出参数为 ouputList，数组类型，表示触发器列表。其中包含每个触发器的 ID 等信息，结构体详细说明如下：​

​

参数​| 说明​  
---|---  
triggerId​| 已创建的触发器 ID。​  
triggerName​| 已创建的触发器名称。​  
createTime​| 触发器的创建时间。​  
triggerTime​| 触发器的触发时间，展示为 Cron 表达式格式。​  
userId​| 触发器对应的用户 ID。​  
  
​

示例​

为一个低代码应用添加每日个性化书单推荐的功能，可以根据不同用户的偏好推荐好书、为每个用户设置触发器，更新推荐书单，用户可以主动查看自己更新后的每日书单。​

主要功能及对应流程如下：​

​

功能模块​| 说明​| 工作流示例​  
---|---|---  
更新推荐书单​| 通过变量节点获取用户 ID 和读书偏好，通过数据库节点查看过去已经推荐过的图书名称，大模型根据读书偏好和已推荐的书单，生成新的推荐书单，并写入数据库中。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271884%27%20height=%27458.2702702702703%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg4NCIgaGVpZ2h0PSI0NTguMjcwMjcwMjcwMjcwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
创建或更新用户触发器​| 通过变量节点获取用户 ID，为用户设置个性化的触发器，绑定更新推荐书单的工作流，每天定时为每个用户更新书单。​此工作流可以绑定用户界面中的某个按钮，用户单击按钮时触发工作流，创建触发器，每天定时更新书单。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271606%27%20height=%27236.3183183183183%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYwNiIgaGVpZ2h0PSIyMzYuMzE4MzE4MzE4MzE4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看每日书单​| 通过变量节点获取用户 ID，根据用户 ID 在数据库中查询今日推荐书单。​这个工作流可以绑定用户界面中的某个按钮，用户单击按钮时触发工作流，展示今日推荐书单。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720000%27%20height=%273063.063063063063%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iMzA2My4wNjMwNjMwNjMwNjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
查看触发器列表​| 查看用户已创建的所有触发器列表。通过变量节点获取用户 ID，根据用户 ID 查询触发器列表。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271614%27%20height=%27232.64864864864865%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYxNCIgaGVpZ2h0PSIyMzIuNjQ4NjQ4NjQ4NjQ4NjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
删除书单触发器​| 不再需要获取每日书单时，可以删除书单触发器，每日书单不会定时更新。​通过变量节点获取用户 ID，根据用户 ID 查询触发器列表、获取触发器 ID，根据用户 ID 和触发器 ID 删除指定用户的触发器。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271613%27%20height=%27213.12912912912913%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYxMyIgaGVpZ2h0PSIyMTMuMTI5MTI5MTI5MTI5MTMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
  
​

上一篇

设置定时触发器节点

下一篇

删除定时触发器节点