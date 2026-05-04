---
source_url: https://docs.coze.cn/guides/horizontal_list_mini_program
title: '横向列表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:37:10Z
---

# 横向列表 - 文档 - 扣子

横向列表

横向列表组件用于横向展示数据项的列表视图，横向列表组件默认包含两个文本组件，你可以通过拖放组件，将目标组件拖动至横向列表组件中。​

属性设置​

横向列表组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定数据源​

横向列表组件支持绑定静态数据，或通过绑定工作流获取动态数据。​

1.

为横向列表组件绑定一个 Array 类型的数据源。​

  * 例如将工作流的输出变量（例如 output）作为列表组件的数据源，该输出变量必须为 Array 类型。绑定工作流后，需要配置事件以触发工作流的调用，确保数据能够动态加载。​

  * 工作流输出变量​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27237%27%20height=%27244%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b441eff279df442f898300bf57ca928e~tplv-goo7wpa0wc-quality:q75.image)​

​

​

绑定数据源​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27252.36496350364962%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fadfcee4a9a54029a448cb147b6d6afc~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​

配置事件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27370%27%20height=%27583.3576642335767%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3a25bc6508b34d05b59966473a2672ba~tplv-goo7wpa0wc-quality:q75.image)​

​

​

2.

为横向列表组件中的各个子组件绑定具体的数据字段。​

  * 绑定数据源后，你可以通过 item 变量遍历和访问 Array 类型数据源中的每个元素。即你可以为列表组件中的各个子组件绑定具体的数据字段。例如为文本组件绑定数据字段 {{item.name}}，为图片组件绑定数据字段 {{item.contentUrl}}。配置示例，请参考​配置示例。​

  * 说明

为图片组件绑定数据字段时，字段值需为图片地址，支持 jpg、png格式，暂不支持svg。​

​

  * item 变量​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27292%27%20height=%27178.6865671641791%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyIiBoZWlnaHQ9IjE3OC42ODY1NjcxNjQxNzkxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

为文本组件绑定数据字段​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27294%27%20height=%27158.8029197080292%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0IiBoZWlnaHQ9IjE1OC44MDI5MTk3MDgwMjkyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

为图片组件绑定数据字段​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27295%27%20height=%27209.94525547445255%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk1IiBoZWlnaHQ9IjIwOS45NDUyNTU0NzQ0NTI1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

设置间距​

横向列表组件以横向列表形式展示内容，支持通过设置间距值来调整各列表项之间的间隔，从而优化布局和视觉效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27298%27%20height=%27163%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk4IiBoZWlnaHQ9IjE2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调整组件​

横向列表组件默认包含一个图片组件、一个容器组件和两个文本组件。你可以根据业务需求，在横向列表组件中自由添加其他组件或删除默认的子组件。当你在一个横向列表组件中添加或删除子组件时，其他列表块也会同步完成相同的操作。​

例如在横向列表组件中，删除原有的文本组件，然后添加一个容器组件和一个图标组件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27522%27%20height=%27203%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIyIiBoZWlnaHQ9IjIwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

横向列表组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考​隐藏组件。​

事件设置​

通过配置横向列表组件的事件，可以为横向列表组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击单元格时：当用户点击单元格时触发。​

  * 加载时：当横向列表组件完成加载时触发。​

  
组件方法​| 支持以下组件方法：​

  * 设置隐藏：隐藏组件，使其不可见。​

  * 滚动到视图：将组件滚动到可视区域内。​

  
  
​

配置示例​

例如想要在小程序中以横向列表形式展示最近一周的科技新闻，则你可以创建一个搜索新闻的工作流，并通过横向列表组件展示。具体操作如下：​

1.

创建工作流。​

  * 使用头条新闻插件（getToutiaoNews）搜索新闻。其中，在结束节点中，设置输出变量 output 的值为头条新闻插件输出结果中的 news ，其为 Array 类型，包括新闻的标题、时间、图片、链接等信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272056%27%20height=%27539.7613365155131%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA1NiIgaGVpZ2h0PSI1MzkuNzYxMzM2NTE1NTEzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

绑定数据。​

a.

将工作流的输出变量 output 绑定到横向列表组件上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27299%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk5IiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为横向列表组件添加调用工作流事件。​

  * 例如配置事件为横向列表组件加载时，即调用工作流，搜索新闻。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27330%27%20height=%27510%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMwIiBoZWlnaHQ9IjUxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

为横向列表组件中的图片组件绑定数据字段 {{ item.cover }}。​

  * cover 字段值为新闻相关的图片 URL。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27303%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAzIiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

为横向列表组件中的文本组件（Text3）绑定数据字段 {{ item.time }}。​

  * time 字段值为新闻时间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27302%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyIiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

e.

为横向列表组件中的文本组件（Text4）绑定数据字段 {{ item.summary }}。​

  * summary 字段值为新闻内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27294%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0IiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

预览效果。​

  * 小程序以横向列表形式展示新闻内容，你可以左右滑动最近一周的科技新闻。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27191%27%20height=%27413%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxIiBoZWlnaHQ9IjQxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * ​

上一篇

组件概述

下一篇

纵向列表