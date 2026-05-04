---
source_url: https://docs.coze.cn/guides/asynchronous_task_node
title: '异步任务节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:56Z
---

# 异步任务节点 - 文档 - 扣子

异步任务节点

扣子编程支持通过异步任务执行低代码工作流。你可以创建异步任务，并通过任务中心、低代码工作流的异步任务节点方式触发执行。本文介绍异步任务节点的具体配置说明。​

节点说明​

在内容生成、数据写入等场景中，用户常常需要使用复杂、长耗时的工作流。而工作流的同步执行模式往往无法满足长耗时、高并发的需求，易阻塞工作流的运行，导致超时。​

例如在通过工作流生成数十个视频并将视频 URL 写入数据库的场景中，耗时较长、并发大，你可以使用异步任务功能来实现。配置示例，请参考​示例。​

1.

将业务工作流设置为异步任务。​

2.

搭建一个包含异步任务节点的工作流来触发该异步任务。​

每次运行异步任务节点时，系统会立即触发一次异步任务。任务触发成功即表示该节点运行完成，可继续执行下一次触发，无需等待业务工作流执行完成。每次触发均会在任务中心生成一个异步任务执行实例，并异步运行一次业务工作流。系统会记录此次业务工作流的运行状态、积分消耗、执行结果等信息，便于后续追溯、查询与管理。关于异步执行工作流的详细说明，请参考​异步执行低代码工作流。​

在异步任务节点中，你需要选择待执行的异步任务，并配置异步任务工作流的输入参数。​

说明

异步执行时，低代码工作流整体超时时间为 24 小时，模型节点等部分节点为 10 分钟，数据库节点等部分节点为 1 分钟，具体请参考​低代码工作流使用限制。​

​

准备工作​

已创建异步任务。具体操作，请参考​步骤一：创建异步任务。​

添加节点​

在工作流画布中，单击 \+ 添加节点，在业务逻辑区域选择异步任务，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27213%27%20height=%27254%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/438336e226ef4c419c48931ba722d427~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

异步任务​

在异步任务区域，你需要添加待执行的异步任务。每个异步任务节点仅支持添加一个异步任务。​

说明

  * 搭建资源库低代码工作流时，仅支持添加绑定了资源库低代码工作流的异步任务。​

  * 搭建低代码应用的工作流时，支持添加绑定了资源库工作流或当前低代码应用工作流的异步任务。​

  * 如果异步任务所绑定的低代码工作流中包含会话相关节点、变量相关节点，则试运行异步任务节点时，需要先绑定对应的低代码智能体或低代码工作流。​

​

输入​

添加异步任务后，系统将根据你在异步任务中绑定的工作流，并在输入区域展示该工作流的输入参数。你可以设置为固定值，也可以引用上游节点的输出参数。运行异步任务时，将根据该输入参数执行异步任务中的工作流，​

例如你创建一个生成视频的异步任务，该任务所绑定的工作流中，输入参数为 prompt，则输入区域将展示输入参数 prompt。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27412%27%20height=%27229%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEyIiBoZWlnaHQ9IjIyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

输出​

异步任务节点固定输出如下输出参数。​

  * taskId：任务运行实例 ID。你可以在任务中心，通过该 ID 查询具体的运行记录。​

  * msg：任务执行信息。​

查看节点运行结果​

试运行异步任务节点后，你可以单击查看任务，跳转至异步任务的详情页面，查看对应的任务详情。详细说明，请参考​步骤三：查看异步任务运行详情。​

说明

通过异步任务节点触发异步任务成功，即表示该节点运行完成，无需等待业务工作流执行完成。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27330%27%20height=%27386%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMwIiBoZWlnaHQ9IjM4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272862%27%20height=%27921.9327731092437%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg2MiIgaGVpZ2h0PSI5MjEuOTMyNzczMTA5MjQzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

上一篇

变量聚合节点

下一篇

输入节点