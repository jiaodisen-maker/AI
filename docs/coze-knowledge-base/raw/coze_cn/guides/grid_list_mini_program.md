---
source_url: https://docs.coze.cn/guides/grid_list_mini_program
title: '宫格列表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:37:15Z
---

# 宫格列表 - 文档 - 扣子

宫格列表

宫格组件是一种以宫格形式展示数据项的布局工具，支持灵活地添加组件、绑定数据和动态更新数据。宫格列表组件默认包含一个图片组件、一个容器组件和两个文本组件，你可根据业务需求自定义添加组件。​

属性配置​

宫格列表组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定数据源​

为宫格列表组件支持绑定静态数据，或通过绑定工作流获取动态数据。​

1.

为宫格列表组件绑定一个 Array 类型的数据源。​

  * 例如将工作流的输出变量（例如 output）作为列表组件的数据源，该输出变量必须为 Array 类型。绑定工作流后，需要配置事件以触发工作流的调用，确保数据能够动态加载。​

  *     * 工作流输出变量​

    * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27237%27%20height=%27244%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b441eff279df442f898300bf57ca928e~tplv-goo7wpa0wc-quality:q75.image)​

​

​

绑定数据源​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27295%27%20height=%27328.25454545454545%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/860e6278ee84429097ff875c8e5d5f47~tplv-goo7wpa0wc-quality:q75.image)​

​

配置事件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27425%27%20height=%27614.2335766423357%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4b196e6a523a4ab286a6bccf6c915e7a~tplv-goo7wpa0wc-quality:q75.image)​

​

​

2.

为宫格列表组件中的各个子组件绑定具体的数据字段。​

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

支持通过列数量、列间距、行间距设置每行展示的宫格数量以及宫格之间的间距，灵活调整宫格布局。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27352%27%20height=%27299%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUyIiBoZWlnaHQ9IjI5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调整组件​

宫格列表组件默认包含一个图片组件、一个容器组件和两个文本组件。你可以根据业务需求，在宫格列表组件中自由添加其他组件或删除默认的子组件。当你在一个宫格中添加或删除子组件时，其他宫格中也会同步完成相同的操作。​

例如在宫格列表组件中，删除原有的文本组件，然后添加一个容器组件和一个图标组件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27257%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU3IiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

宫格列表组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。​

  * 例如添加一个单行输入组件（Input1）和一个宫格列表（GridList1）组件，单行输入组件用于输入内容，宫格列表组件用于展示基于输入内容生成的图像。为了实现宫格列表组件内的图片展示时，就隐藏单行输入组件，你可以在单行输入组件的可见性属性中，添加条件 Image1.src 不为空。当宫格列表组件内的图片展示时，条件 Image1.src 不为空 变为 true，文本输入组件将自动隐藏。​

  * 可见性配置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27980%27%20height=%27555.9272727272727%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTgwIiBoZWlnaHQ9IjU1NS45MjcyNzI3MjcyNzI3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

图片加载完成后隐藏文本输入组件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27309%27%20height=%27654%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA5IiBoZWlnaHQ9IjY1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

事件设置​

通过配置宫格列表组件的事件，可以为宫格列表组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击单元格时：当用户点击单元格时触发。​

  * 加载时：当宫格列表组件完成加载时触发。​

  
组件方法​| 设置隐藏：隐藏组件，使其不可见。​  
  
​

配置示例​

例如要在小程序中以宫格形式展示小狗图片，则你可以创建一个搜索小狗图片的工作流，并通过宫格列表展示。具体操作如下：​

1.

创建工作流。​

  * 使用头条图片搜索插件（ToutiaoPictureSearch）搜索小狗图片。其中，在结束节点中，设置输出变量 output 的值为头条图片搜索插件输出结果中的 result，其为 Array 类型，包括图片地址、图片名称、图片大小等数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271817%27%20height=%27500.5162037037037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgxNyIgaGVpZ2h0PSI1MDAuNTE2MjAzNzAzNzAzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

绑定数据。​

a.

将工作流的输出变量 output 绑定到宫格列表组件上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27319%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE5IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为宫格列表组件添加调用工作流事件。​

  * 例如配置事件为宫格列表组件加载时，即调用工作流，搜索小狗图片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27299%27%20height=%27443%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk5IiBoZWlnaHQ9IjQ0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

为宫格列表组件中的图片组件（Image3）绑定数据字段 {{ item.picture_info.display_url }}。​

  * display_url 字段值为图片的 URL 地址。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27508%27%20height=%27277%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA4IiBoZWlnaHQ9IjI3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

为宫格列表组件中的文本组件（Text1）绑定数据字段 {{ item.picture_info.title }}。​

  * title 字段值为图片名称。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27436%27%20height=%27237%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM2IiBoZWlnaHQ9IjIzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

e.

为宫格列表组件中的文本组件（Text2）绑定数据字段 {{item.picture_info.size.width }}。​

  * width 字段值为图片宽度。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27285%27%20height=%27250%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg1IiBoZWlnaHQ9IjI1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

预览效果。​

  * 以宫格列表形式展示搜索结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27242%27%20height=%27519%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQyIiBoZWlnaHQ9IjUxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

  * ​

  * ​

​

​

上一篇

纵向列表

下一篇

瀑布流列表