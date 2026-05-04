---
source_url: https://docs.coze.cn/guides/waterfall_list_mini_program
title: '瀑布流列表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:37:18Z
---

# 瀑布流列表 - 文档 - 扣子

瀑布流列表

瀑布流列表组件是一种以错落有致的多列形式展示数据项的布局工具，支持灵活地绑定数据和动态更新数据。瀑布流列表组件默认包含一个图片组件、一个容器组件和两个文本组件，你可根据业务需求自定义添加组件。​

属性配置​

瀑布流列表组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定数据源​

瀑布流列表组件支持绑定静态数据，或通过绑定工作流获取动态数据。​

1.

为瀑布流列表组件绑定一个 Array 类型的数据源。​

  * 例如将工作流的输出变量（例如 output）作为列表组件的数据源，该输出变量必须为 Array 类型。绑定工作流后，需要配置事件以触发工作流的调用，确保数据能够动态加载。​

  * 工作流输出变量​

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

​

2.

为瀑布流列表组件中的各个子组件绑定具体的数据字段。​

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

设置列数及间距​

支持通过列数量、列间距、行间距设置每行展示的列表块数量以及列表块之间的间距，灵活调整瀑布流列表布局。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27487%27%20height=%27438%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg3IiBoZWlnaHQ9IjQzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调整组件​

瀑布流列表组件默认包含一个图片组件、一个容器组件和两个文本组件。你可以根据业务需求，在瀑布流列表组件中自由添加其他组件或删除默认的子组件。当你在一个瀑布流中添加或删除子组件时，其他列表块也会同步完成相同的操作。​

例如在瀑布流列表组件中，删除原有的文本组件，然后添加一个容器组件和一个图标组件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27296%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk2IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

瀑布流列表组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。​

  * 例如添加一个单行输入组件（Input1）和一个瀑布流列表（WaterfallList1）组件，单行输入组件用于输入内容，瀑布流列表组件用于展示基于输入内容的搜索结果。为了实现瀑布流列表组件内的图片展示时，就隐藏单行输入组件，你可以在单行输入组件的可见性属性中，添加条件 Image1.src 不为空。当瀑布流列表组件内的图片展示时，条件 Image1.src 不为空 变为 true，单行输入组件将自动隐藏。​

  * 可见性配置​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27980%27%20height=%27555.9272727272727%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTgwIiBoZWlnaHQ9IjU1NS45MjcyNzI3MjcyNzI3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

图片加载完成后隐藏文本输入组件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27642%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjY0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

事件设置​

通过配置瀑布流列表组件的事件，可以为瀑布流列表组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击单元格时：当用户点击单元格时触发。​

  * 加载时：当瀑布流列表组件完成加载时触发。​

  
组件方法​| 设置隐藏：隐藏组件，使其不可见。​  
  
​

配置示例​

例如使用什么值得买插件搜索人工智能书籍的价格及购买渠道，并在应用中以瀑布流形式展示搜索结果，则你可以按照以下步骤创建一个工作流，并通过瀑布流列表组件进行展示。​

1.

创建工作流。​

  * 使用什么值得买插件（smzdm_haojia_articles）搜索人工智能书籍。其中，在结束节点中，设置输出变量 output 的值为什么值得买插件中的 Content_source 变量。Content_source 变量为 Array 类型，内容为 [{title: "书名1", item.digital_price : "价格1", item.focus_pic_url: "图片1"....}, ...]。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271873%27%20height=%27605.6965174129353%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg3MyIgaGVpZ2h0PSI2MDUuNjk2NTE3NDEyOTM1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

绑定数据。​

a.

将工作流的输出变量 output 绑定到瀑布流列表组件上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27220%27%20height=%27241%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIwIiBoZWlnaHQ9IjI0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为瀑布流列表组件添加调用工作流事件。​

  * 例如配置事件为瀑布流列表组件加载时即调用工作流，搜索人工智能书籍。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27233%27%20height=%27368%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMzIiBoZWlnaHQ9IjM2OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

为瀑布流列表组件中的图片组件（Image1）绑定数据字段 {{ item.focus_pic_url }}。​

  * focus_pic_url 为商品图片 URL。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27271%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcxIiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

为瀑布流列表组件中的文本组件（Text1）绑定数据字段 {{ item.digital_price }}。​

  * digital_price 为商品价格。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27243%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkzIiBoZWlnaHQ9IjI0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

e.

为瀑布流列表组件中的文本组件（Text2）绑定数据字段 {{ item.desc }}。​

  * desc 为商品描述。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27295%27%20height=%27208%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk1IiBoZWlnaHQ9IjIwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

预览效果。​

  * 以瀑布流形式展示搜索结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27249%27%20height=%27533%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ5IiBoZWlnaHQ9IjUzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

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