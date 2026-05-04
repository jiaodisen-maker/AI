---
source_url: https://docs.coze.cn/guides/message_card
title: '卡片 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:39Z
---

# 卡片 - 文档 - 扣子

卡片

扣子编程支持低代码智能体以卡片形式发送消息，提升低代码智能体的聊天交互体验。​

注意

  * 目前卡片仅在豆包客户端、飞书客户端内生效。​

  * 仅工作流和插件支持添加卡片。​

​

权限说明​

卡片暂不支持多人协作。只有卡片的所有者支持编辑和删除自己创建的卡片，工作空间所有者、管理员以及普通成员都没有权限编辑和删除其他成员创建的卡片。​

使用官方卡片​

扣子编程提供了卡片模板，你可以选择适用的模板，并根据页面提示配置卡片参数。​

1.

在智能体编排页面找到要配置卡片的工作流或插件，单击卡片图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27638%27%20height=%27105%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/32e9a4567b4e40b7b7cdfc5ec95d79eb~tplv-goo7wpa0wc-quality:q75.image)​

​

2.

配置卡片。​

a.

选择卡片模板。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27204%27%20height=%27342%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e639abd684104e759e52fec915fcd550~tplv-goo7wpa0wc-quality:q75.image)​

​

b.

选择卡片样式及配置对应参数。​

  * ​

卡片样式​| 说明​| 配置示例​  
---|---|---  
单张卡片​| 仅展示一张卡片，适用于展示单一内容。​选择单张卡片时，需完成如下配置：​
    * 为卡片内的元素绑定数据：为不同的元素绑定不同的变量。例如为卡片标题绑定 data.doc_results[0].title 变量，卡片标题将展示数组第一个元素中的 title 属性。​
    * 单张卡片只支持绑定数组中的第一个元素。​
    * 点击卡片跳转：单击卡片时，是否支持跳转到对应的 URL 页面。​
    * 打开点击卡片跳转开关，并绑定表示 URL 的变量。设置完成后，当你单击卡片时，将跳转到对应的 URL 页面。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27950%27%20height=%27479.91718426501035%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTUwIiBoZWlnaHQ9IjQ3OS45MTcxODQyNjUwMTAzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
竖项卡片​| 支持展示多张卡片。例如搜索到多条新闻时，可通过卡片列表依次展示新闻内容。​
    * 卡片列表最大长度：卡片列表的最大数量，最大值为 20。​
    * 为卡片整体绑定一个数组：为卡片绑定一个数组类型的变量，例如 data.doc_results。​
    * 为卡片内的列表项绑定数据：为不同的卡片元素绑定不同的变量。例如为卡片标题绑定 title，即表示绑定 data.doc_results 数组中 title 属性。​
    * 点击卡片跳转：选择单击卡片时，是否支持跳转到对应的 URL 页面。​
    * 打开点击卡片跳转开关，并绑定表示 URL 的变量。设置完成后，当你单击卡片时，将跳转到对应的 URL 页面。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27982%27%20height=%27648.567287784679%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTgyIiBoZWlnaHQ9IjY0OC41NjcyODc3ODQ2NzkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

c.

单击确认。​

  * 配置完成后，你在与智能体对话时，智能体将以卡片形式回复消息。​

使用自定义卡片​

如果扣子编程官方提供的卡片模板不能满足你的需求，你可以自定义卡片样式。​

步骤 1 ：创建卡片​

1.

在智能体回复卡片配置页面中，单击新增，页面将跳转至卡片编辑页面。​

2.

在页面左侧的卡片页签内，选择模版或者自行拖拽组件构建卡片样式。​

  * 模板：双击使用模板，你可以基于模板构建属于你的卡片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271520%27%20height=%27786.10101010101%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyMCIgaGVpZ2h0PSI3ODYuMTAxMDEwMTAxMDEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 组件：通过拖拽布局组件和基础组件，自定义卡片内容。​

  * 结构：以导航树的形式展示卡片的组件布局。​

3.

在页面左侧的变量页签内，创建变量。​

  * 为卡片组件创建变量，智能体会根据插件或工作流的返回值展示对应的内容。例如，新增 newMovies 变量，Array 类型，默认值如下所示。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27445%27%20height=%27331%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ1IiBoZWlnaHQ9IjMzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

为卡片组件绑定变量。​

  * 在卡片画布内，选中需要添加变量的组件，然后在组件基本配置的内容区域，单击变量图标并选择要使用的变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27768%27%20height=%27177%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzY4IiBoZWlnaHQ9IjE3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在页面右上角单击预览，扫描二维码在豆包或飞书中查看预览效果。​

6.

在页面右上角单击发布。​

步骤 2 ：为卡片绑定数据​

发布自定义卡片后，你需要为卡片绑定数据，例如插件的返回参数。​

1.

在智能体回复卡片配置对话框的工作空间卡片页签中，单击你已创建的卡片。​

2.

为卡片绑定数据。​

  * 例如绑定淘票票（GetMovieAndShow）插件的返回参数 data.return_value。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27365%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg1IiBoZWlnaHQ9IjM2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 当你在智能体中查询最近上映的电影时，智能体将以卡片形式回复。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27224%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI0IiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例​

例如搭建一个新闻助手智能体，其中添加头条搜索插件搜索新闻，并为插件的输出内容配置卡片，以卡片形式回复新闻内容。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

​

3.

在低代码模式区域，单击智能体开发。​

4.

根据页面提示，创建一个新智能体。​

5.

在智能体编排页面，添加头条搜索插件，并单击其对应的绑定卡片数据图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27739%27%20height=%27135%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzM5IiBoZWlnaHQ9IjEzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在智能体回复卡片配置对话框，完成如下配置。​

a.

选择扣子编程提供的某款官方卡片，并选择竖向列表。​

b.

设置卡片列表最大长度为 5。​

c.

在为卡片整体绑定一个数组中，绑定数组data.doc_results。​

  * 即为卡片绑定新闻插件的搜索结果集合。​

d.

为卡片内的列表项绑定数据。​

  * ①标题：为卡片标题绑定变量 title，即绑定 data.doc_results 数组中 title 字段，用于展示搜索到的新闻标题。​

  * ②内容：为卡片内容绑定变量 summary，即绑定 data.doc_results 数组中 summary 字段，用于展示搜索到的新闻内容。​

e.

设置卡片跳转链接。​

  * 打开点击卡片跳转开关，并设置卡片跳转链接为 url。设置完成后，当你单击卡片时，将跳转到对应的 URL 页面。​

d.

单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27556%27%20height=%27424%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU2IiBoZWlnaHQ9IjQyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

查看卡片效果。​

  * 当你在智能体中查询今天的科技新闻时，智能体将以卡片形式回复。单击目标卡片，将打开对应的新闻网页。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27440%27%20height=%27425%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQwIiBoZWlnaHQ9IjQyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

上一篇

触发器

下一篇

为低代码智能体添加知识