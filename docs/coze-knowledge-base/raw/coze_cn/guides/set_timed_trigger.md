---
source_url: https://docs.coze.cn/guides/set_timed_trigger
title: '设置定时触发器节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:24Z
---

# 设置定时触发器节点 - 文档 - 扣子

设置定时触发器节点

设置定时触发器节点用于在扣子编程的低代码应用中创建一个定时触发器，或修改已创建的定时触发器。​

节点说明​

和低代码智能体一样，低代码应用也支持设置定时触发器，在指定的时间点触发定时器调用某个工作流。低代码应用的触发器分为预设触发器和用户触发器两种，前者是开发者编排应用时创建的触发器，对所有用户生效，后者是低代码应用的用户通过定时触发器节点创建的，仅对指定用户生效。关于低代码应用触发器的详细说明，可参考​为应用设置触发器。​

设置定时触发器用于用户主动设置触发器的场景，例如在一个英语学习的 AI 应用中，每个用户都可以创建自己的学习计划，A 用户可以要求每天 10 点学习 10 个单词，B 用户可以要求 12 点学习 5 个。​

说明

设置定时触发器等触发器节点仅支持在低代码应用中创建或使用，包含触发器节点的低代码工作流无法添加到智能体中。​

​

设置节点参数​

输入​

设置定时触发器节点预设多个参数，配置说明如下:​

​

变量​| 说明​| 示例​  
---|---|---  
id​| 触发器的 ID，是触发器在扣子编程中的唯一标识，由扣子编程自动创建，不支持手动创建或编辑。​说明

  * 创建触发器时，无需设置 id，系统会自动生成一个 id。​

  * 更新触发器配置时，需要输入 id，表示更新指定的触发器。​

​| ​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27746.1702127659574%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/949bdb58291b4d8eb8df44c7ca34420e~tplv-goo7wpa0wc-quality:q75.image)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27356%27%20height=%27789.2595744680851%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU2IiBoZWlnaHQ9Ijc4OS4yNTk1NzQ0NjgwODUxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
用户id​| 使用触发器的扣子用户 ID，此触发器仅对该用户生效。低代码应用的系统变量 sys_uuid 可以用来标识用户，你可以使用变量节点获取系统变量 sys_uuid 的值，并赋值给设置定时触发器节点的用户id 参数。​| ​  
名称​| 触发器的名称，用于标识触发器的用途。​| ​  
时区​| 触发器的运行时区，建议根据 AI 应用的用户所在时区设置，确保定时任务在正确的时间启动。​| ​  
触发时间​| 触发器的触发时间，触发时自动执行这个工作流。可以选择预设的时间选项（如每天 18 点），也可以使用 Cron 表达式来自定义复杂的时间。其中，Cron 表达式支持 AI 自动生成，也可以引用上游节点的输出。​说明触发器时间间隔不可少于 1 分钟。​​| ​  
绑定工作流​| 选择一个工作流，当触发器被激活时，扣子编程会自动运行该工作流。​| ​  
参数​| 工作流开始节点设置的参数，其中必选参数应设置运行时的参数值。​| ​  
  
​

输出​

设置定时触发器节点固定的输出参数为 triggerId，String 类型，表示已创建或更新的触发器 ID。​

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

​

上一篇

JSON 反序列化节点

下一篇

查询定时触发器节点