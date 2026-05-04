---
source_url: https://docs.coze.cn/guides/waterfall_list_web
title: '瀑布流列表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:38:19Z
---

# 瀑布流列表 - 文档 - 扣子

瀑布流列表

瀑布流列表组件是一种以错落有致的多列形式展示数据项的布局工具，支持灵活地添加组件、绑定数据和动态更新数据。瀑布流列表组件默认包含一个图片组件、一个容器组件和两个文本组件，你可根据业务需求自定义添加组件。​

属性配置​

瀑布流列表组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定数据源​

瀑布流列表组件支持绑定静态数据，或通过绑定工作流获取动态数据。​

1.

为瀑布流列表组件绑定一个 Array 类型的数据源。​

  * 例如将工作流的输出变量（例如 output）作为列表组件的数据源，该输出变量必须为 Array 类型。绑定工作流后，需要配置事件以触发工作流的调用，确保数据能够动态加载。​

  *     * 工作流输出变量​

    * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27237%27%20height=%27244%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b441eff279df442f898300bf57ca928e~tplv-goo7wpa0wc-quality:q75.image)​

​

​

绑定数据源​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27288%27%20height=%27317.32363636363635%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/273b52b25f584bbea831bc7a60f2df6a~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​

配置事件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27382%27%20height=%27575.0836363636363%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ddeb67f57fa846d384ce038fa30ec686~tplv-goo7wpa0wc-quality:q75.image)​

​

​

2.

为瀑布流列表组件中的各个子组件绑定具体的数据字段。​

  * 绑定数据源后，你可以通过 item 变量遍历和访问 Array 类型数据源中的每个元素。即你可以为列表组件中的各个子组件绑定具体的数据字段。例如为文本组件绑定数据字段 {{item.name}}，为图片组件绑定数据字段 {{item.contentUrl}}。配置示例，请参考​配置示例。​

  * 说明

为图片组件绑定数据字段时，字段值需为图片地址，支持 jpg、png格式，暂不支持svg 格式。​

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

为图片组件绑定数据​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27295%27%20height=%27209.94525547445255%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk1IiBoZWlnaHQ9IjIwOS45NDUyNTU0NzQ0NTI1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

设置列数及间距​

瀑布流组件支持灵活调整布局，以满足不同场景的需求。具体功能包括：​

  * 固定列数：设置每行固定的列表块数量，确保布局的一致性。​

  * 动态列数：根据屏幕宽度或容器宽度自动调整每行的列表块数量，以实现响应式布局。​

  * 间距设置：支持通过列间距、行间距设置列表块之间的间距，灵活调整瀑布流列表布局。​

固定列表​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27291%27%20height=%27164%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkxIiBoZWlnaHQ9IjE2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

动态列数​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27286%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg2IiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

调整组件​

瀑布流列表组件默认包含一个图片组件、一个容器组件和两个文本组件。你可以根据业务需求，在瀑布流列表组件中自由添加其他组件或删除默认的子组件。当你在一个瀑布流列表组件中添加或删除子组件时，其他列表块也会同步完成相同的操作。​

例如在瀑布流列表组件中，删除原有的文本组件，然后添加一个容器组件和一个图标组件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27389%27%20height=%27367%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg5IiBoZWlnaHQ9IjM2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

瀑布流列表组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考​隐藏组件。​

事件设置​

通过配置瀑布流列表组件的事件，可以为瀑布流列表组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击单元格时：当用户点击单元格时触发。​

  * 加载时：当瀑布流列表组件完成加载时触发。​

  
组件方法​| 支持以下组件方法：​

  * 设置隐藏：隐藏组件，使其不可见。​

  * 滚动到视图：将组件滚动到可视区域内。​

  
  
​

配置示例​

例如使用头条图片搜索插件搜索小狗图片，并在网页中以瀑布流形式展示搜索结果，则你可以按照以下步骤创建一个工作流，并通过瀑布流列表组件进行展示。​

1.

创建工作流。​

  * 使用头条图片搜索插件（ToutiaoPictureSearch）搜索小狗图片。其中，在结束节点中，设置输出变量 output 的值为头条图片搜索插件输出结果中的 result ，其为 Array 类型，包含图片标题、URL、尺寸等信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272096%27%20height=%27545.2601431980908%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA5NiIgaGVpZ2h0PSI1NDUuMjYwMTQzMTk4MDkwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

绑定数据。​

a.

将工作流的输出变量 output 绑定到瀑布流列表组件上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27240%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQwIiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为瀑布流列表组件添加调用工作流事件。​

  * 例如配置事件为瀑布流列表组件加载时，即调用工作流，搜索小狗图片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27245%27%20height=%27378%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ1IiBoZWlnaHQ9IjM3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

为瀑布流列表组件中的图片组件绑定数据字段 {{item.picture_info.display_url }}。​

  * picture_info.display_url 为图片地址。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27258%27%20height=%27197%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU4IiBoZWlnaHQ9IjE5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

删除瀑布流列表组件自带的两个文本组件。​

3.

预览效果。​

  * 以瀑布流形式展示搜索结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27656%27%20height=%27453%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU2IiBoZWlnaHQ9IjQ1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * ​

​

​

  * ​

  * ​

上一篇

宫格列表

下一篇

容器