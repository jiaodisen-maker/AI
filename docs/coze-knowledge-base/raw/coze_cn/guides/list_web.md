---
source_url: https://docs.coze.cn/guides/list_web
title: '纵向列表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:38:11Z
---

# 纵向列表 - 文档 - 扣子

纵向列表

纵向列表组件是一种以纵向列表形式展示数据项的布局工具，支持灵活添加组件、绑定数据和动态更新数据，以满足多样化的展示需求。它默认包含一个图片组件、一个容器组件和两个文本组件，你可根据业务需求自定义添加组件。​

属性设置​

纵向列表组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定数据源​

为纵向列表组件支持绑定静态数据，或通过绑定工作流获取动态数据。​

1.

为纵向列表组件绑定一个 Array 类型的数据源。​

  * 例如将工作流的输出变量（例如 output）作为列表组件的数据源，该输出变量必须为 Array 类型。绑定工作流后，需要配置事件以触发工作流的调用，确保数据能够动态加载。​

  *     * 工作流输出变量​

    * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27237%27%20height=%27244%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b441eff279df442f898300bf57ca928e~tplv-goo7wpa0wc-quality:q75.image)​

​

​

绑定数据源​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27269%27%20height=%27229.8544776119403%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/156c4179a27d40e193d4ead5f78b99e6~tplv-goo7wpa0wc-quality:q75.image)​

​

​

配置事件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27532.8358208955224%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/991b8f865f2c4ebaa776a3ffdab352ff~tplv-goo7wpa0wc-quality:q75.image)​

​

​

2.

为纵向列表组件中的各个子组件绑定具体的数据字段。​

  * 绑定数据源后，你可以通过 item 变量遍历和访问 Array 类型数据源中的每个元素。即你可以为列表组件中的各个子组件绑定具体的数据字段。例如为文本组件绑定数据字段 {{item.name}}，为图片组件绑定数据字段 {{item.contentUrl}}。具体示例，请参考​配置示例。​

  * 说明

为图片组件绑定数据字段时，字段值需为图片地址，支持上传 jpg、png格式，暂不支持svg。​

​

  * item 变量​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27292%27%20height=%27178.6865671641791%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyIiBoZWlnaHQ9IjE3OC42ODY1NjcxNjQxNzkxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

为文本组件绑定数据字段​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27156.62181818181818%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkzIiBoZWlnaHQ9IjE1Ni42MjE4MTgxODE4MTgxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

为图片组件绑定数据字段​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27291%27%20height=%27210.5781818181818%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkxIiBoZWlnaHQ9IjIxMC41NzgxODE4MTgxODE4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

设置列数及间距​

支持通过间距值设置每个列表项之间的间距。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27393%27%20height=%27134%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkzIiBoZWlnaHQ9IjEzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调整组件​

纵向列表组件默认包含一个图片组件、一个容器组件和两个文本组件。你可以根据业务需求，在纵向列表组件中自由添加其他组件或删除默认的子组件。当你在一个列表项中添加或删除子组件时，其他列表项中也会同步完成相同的操作。​

例如在纵向列表组件中，删除原有的文本组件，然后添加一个图标组件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27241%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkzIiBoZWlnaHQ9IjI0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

指针设置​

配置鼠标在指定组件区域内的指针样式。​

你可以选择根据元素类型自动显示，也可以指定某一特定的指针样式。​

属性配置项​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27212%27%20height=%27215%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEyIiBoZWlnaHQ9IjIxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27234%27%20height=%27175%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM0IiBoZWlnaHQ9IjE3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

隐藏组件​

纵向列表组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考​隐藏组件。​

事件设置​

通过配置列表组件的事件，可以为列表组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击单元格时：当用户点击列表组件中的单元格时触发。​

  * 加载时：当组件完成加载时触发。​

  
组件方法​| 支持以下方法：​

  * 滚动到视图：将组件滚动到可视区域内。​

  * 滑动单元格到视图：自动将当前活动的单元格平滑地滚动到可视区域内。​

  * 设置隐藏：隐藏组件，使其不可见。​

  
  
​

配置示例​

例如需要搭建一个新闻播报网页，则你可以创建一个搜索新闻的工作流，并通过纵向列表组件来展示新闻搜索结果。该组件的每个列表项都可根据绑定的数据动态展示对应的新闻标题和内容。​

1.

创建工作流（list2）。​

  * 使用头条新闻插件（getToutiaoNews）搜索新闻。其中，在结束节点中，设置输出变量 output 的值为头条新闻插件输出结果中的 news ，其为 Array 类型，包括新闻的标题、时间、图片、链接等信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27816%27%20height=%27214%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODE2IiBoZWlnaHQ9IjIxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

搭建网页。​

  * 搭建一个新闻播报网页，当你输入搜索内容，单击搜索新闻后，纵向列表中将展示搜索到的新闻内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27769%27%20height=%27535%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzY5IiBoZWlnaHQ9IjUzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

为按钮组件（Button1）配置事件。​

  * 单击搜索新闻按钮时，将调用工作流（list 2）搜索新闻。工作流的输入参数 input 引用单行输入组件（Textarea1）的值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27230%27%20height=%27348%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMwIiBoZWlnaHQ9IjM0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

为纵向列表绑定数据。​

a.

将工作流（list2）的输出变量 output 绑定到纵向列表组件上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27299%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk5IiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为纵向列表组件中的图片组件绑定数据字段 {{ item.cover }}。​

  * cover 字段值为新闻相关的图片 URL。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27303%27%20height=%27286%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAzIiBoZWlnaHQ9IjI4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

为纵向列表组件中的文本组件（Text3）绑定数据字段 {{ item.time }}。​

  * time 字段值为新闻时间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27302%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyIiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

为纵向列表组件中的文本组件（Text4）绑定数据字段 {{ item.summary }}。​

  * summary 字段值为新闻内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27294%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0IiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

预览效果。​

  * 输入搜索本月的科技新闻，单击搜索新闻后，页面中将以纵向列表形式展示搜索到的新闻。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27650%27%20height=%27365%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjUwIiBoZWlnaHQ9IjM2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

组件概述

下一篇

横向列表