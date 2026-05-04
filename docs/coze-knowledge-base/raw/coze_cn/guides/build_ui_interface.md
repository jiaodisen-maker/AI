---
source_url: https://docs.coze.cn/guides/build_ui_interface
title: '快速搭建网页端用户界面 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:43Z
---

# 快速搭建网页端用户界面 - 文档 - 扣子

快速搭建网页端用户界面

本教程以搭建一个AI 翻译应用的用户界面为例，为你演示如何搭建用户界面。​

前提条件​

你已经通过工作流编排完后端业务逻辑。本教程中的 AI 翻译应用，主要是使用大模型实现多语言翻译，所以只需要创建一个包含大模型节点的工作流即可，详情请参考​步骤三：编排业务逻辑。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271684%27%20height=%27370.3240740740741%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9d741c3025be44c9883b465e4e1b2ab5~tplv-goo7wpa0wc-quality:q75.image)​

​

本教程搭建用户界面的步骤如下图：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27569%27%20height=%27134%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a88137b5bcbf4621bf1599591ba76509~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤 1：设计用户界面​

首先，你需要根据低代码应用的功能设计用户界面，规划用户界面的组件功能和布局。​

这个 AI 翻译应用的核心功能是能够满足用户的文本翻译需求，并支持用户选择指定翻译的语言。翻译功能可以通过创建一个包含大模型节点的工作流来实现。​

基于以上功能规划，这个低代码应用的用户界面需包含以下组件：​

  * 一个让用户可以输入翻译内容的区域​

  * 一个让用户选择翻译语言的列表​

  * 一个翻译按钮来触发翻译操作​

  * 一个展示翻译结果的内容区域​

完成组件功能设计和规划后，就可以开始用户界面的搭建了。​

步骤 2：搭建用户界面​

扣子编程提供了可视化的用户界面搭建能力，你可以通过拖拉拽的方式搭建一个用户界面，无需写一行代码。​

参考以下操作，搭建网页端翻译应用的用户界面。​

1.

在应用 IDE，单击页面上方的用户界面页签。​

2.

选择桌面网页，然后单击开始搭建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27391%27%20height=%27289%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkxIiBoZWlnaHQ9IjI4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

添加页面组件，完成页面搭建。​

  * 翻译页面由3个块级组成，具体使用的组件和配置请参考下述步骤。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27499%27%20height=%27225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk5IiBoZWlnaHQ9IjIyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

1 搭建页面结构​

整体上 AI 翻译应用的用户界面由上下两个部分组成。​

  * 上面是标题区域。​

  * 下面是功能区域。功能区域又分为左右两个区域。​

想要实现这样的页面结构就需要使用容器组件。容器组件是用来进行页面布局的，可以把页面划分成不同的区域和排列顺序。容器组件中可以添加其他各种组件例如文本组件、按钮组件等。​

参考以下操作，完成页面布局：​

1.

确认画布的排列方向为纵向。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27625%27%20height=%27354%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI1IiBoZWlnaHQ9IjM1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在组件面板中，找到布局组件 > 容器组件，然后将容器组件拖入到中间的画布中。​

3.

在画布中，选中拖入的容器组件。组件名称为Div1。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27628%27%20height=%27197%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI4IiBoZWlnaHQ9IjE5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

参考以下配置，修改容器组件Div1的属性。​

  * ​

Div1的属性设置​| 示例​  
---|---  
设置尺寸和布局。​
    * 将宽度设置为填充容器（即100%）。​
    * 将高度设置为60 px。​
    * 将排列方向设置为横向。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272366%27%20height=%27659.3770491803278%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2NiIgaGVpZ2h0PSI2NTkuMzc3MDQ5MTgwMzI3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
设置样式。​
    * 找到填充属性，然后单击删除图标去掉背景色。​
    * 将边框设置为灰色。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271926%27%20height=%271073.5081967213114%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyNiIgaGVpZ2h0PSIxMDczLjUwODE5NjcyMTMxMTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

5.

再拖入一个容器组件用来组织功能区，并在画布中选中该组件。组件名称为Div2。然后选中该组件，参考下表中的属性配置进行修改。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27674%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc0IiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

Div2的属性设置​| 示例​  
---|---  
    * 设置尺寸，将宽度和高度都设置为填充容器（即100%）。​
    * 排列方向设置为横向。​
    * 设置样式。找到填充属性，然后单击删除图标去掉背景色。​
​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271958%27%20height=%271000.9179104477612%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1OCIgaGVpZ2h0PSIxMDAwLjkxNzkxMDQ0Nzc2MTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

6.

向画布的容器组件Div2的左侧区域中，拖入一个容器组件Div3，用来组织左侧的内容翻译区域。然后选中该组件，参考下表中的属性配置进行修改。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg1IiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

Div3的属性设置​| 示例​  
---|---  
    * 将宽度设置为50%。​
    * 将高度设置为固定值550px。​
    * 删除背景色。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271950%27%20height=%27935.7758620689655%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1MCIgaGVpZ2h0PSI5MzUuNzc1ODYyMDY4OTY1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

7.

向画布中容器组件Div2的右侧区域中，拖入一个容器组件Div4，用来组织右侧的翻译结果区域。然后选中该组件，参考下表中的属性配置进行修改。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27630%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMwIiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

Div4的属性设置​| 示例​  
---|---  
    * 将宽度设置为50%。​
    * 将高度设置为固定值550px。​
    * 删除背景色。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271993%27%20height=%27886.9945054945055%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk5MyIgaGVpZ2h0PSI4ODYuOTk0NTA1NDk0NTA1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

至此，我们就完成了这个翻译应用的页面结构搭建。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27444%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ0IiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2 搭建页面标题​

参考以下操作，搭建页面的标题区域。​

1.

在组件面板中，找到推荐组件 > 文本组件，然后将文本组件拖入到顶部的容器组件Div1上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27680%27%20height=%27127%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgwIiBoZWlnaHQ9IjEyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在画布中，选中拖入的文本组件，然后在右侧的属性面板中设置文本内容，字号大小等。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27287%27%20height=%27214%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg3IiBoZWlnaHQ9IjIxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

至此，你已经完成了标题区域的搭建。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27541%27%20height=%27118%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQxIiBoZWlnaHQ9IjExOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3 搭建左侧翻译内容区​

参考以下操作，搭建翻译内容区域。​

1.

在组件面板中，将表单组件拖入到画布的容器组件Div3中，然后选中不需要的组件并按下 Backspace 键进行删除，只保留文本组件、选择组件和按钮组件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27537%27%20height=%27336%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM3IiBoZWlnaHQ9IjMzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选中表单组件，参考下表修改它的属性。​

  * ​

Form表单组件的属性设置​| 示例​  
---|---  
    * 将宽度和高度都设置为填充容器。​
    * 删除边框。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271950%27%20height=%271189.2857142857144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1MCIgaGVpZ2h0PSIxMTg5LjI4NTcxNDI4NTcxNDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

3.

选中表单内的文本输入框，然后将其拉伸它的大小，再修改属性配置。​

  * 标签内容和占位文案都修改为：请输入翻译内容。​

  * 宽度设置百分比 100%。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27606%27%20height=%27306%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA2IiBoZWlnaHQ9IjMwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

选中表单组件中的选择组件，然后修改它的属性配置。​

  * 标签内容修改为：目标语言。​

  * 选项设置：保留两个选项，分别为英语和日语。确保名称和选项值正确。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27613%27%20height=%27330%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEzIiBoZWlnaHQ9IjMzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

选中表单组件中的按钮组件，将内容修改为开始翻译。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27521%27%20height=%27262%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIxIiBoZWlnaHQ9IjI2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

至此，我们就完成了左侧的翻译内容区域的页面功能搭建。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27303%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4 搭建右侧翻译结果区​

参考以下操作，搭建翻译结果区域。​

1.

在组件面板中，将 Markdown 组件拖入到画布的容器组件Div4中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27635%27%20height=%27370%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM1IiBoZWlnaHQ9IjM3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选中新拖入的组件，配置以下属性。​

  * 内容：删除已有内容，输入 Markdown 格式内容：###### 翻译结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27471%27%20height=%27177%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcxIiBoZWlnaHQ9IjE3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 高度和宽度：设置为填充容器。​

  * 圆角：设置为10。​

  * 内边距：设置为20。​

  * 外边距：设置为0。​

  * 边框：设置为灰色。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjI2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

至此，我们就完成了翻译应用的用户界面搭建，可单击属性面板上方的预览选项进行页面预览。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27682%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgyIiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5 添加事件​

搭建好页面后，就可以通过配置事件和添加数据实现业务逻辑与用户页面的联动了。​

本场景中，预期是希望用户点击开始翻译时，触发翻译工作流，并且将用户输入的译文和目标语言作为输入传入给工作流。所以，需要为开始翻译按钮组件添加一个点击事件。​

1.

在用户页面页签下，单击已添加的开始翻译按钮组件，然后在配置面板中选择事件，最后单击新建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27512%27%20height=%27314%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEyIiBoZWlnaHQ9IjMxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

事件类型选择点击时。​

3.

执行动作选择调用工作流，然后选择已经创建的工作流。选择工作流后，会自动展示所选工作流配置的输入参数。​

4.

将鼠标悬浮至content参数的文本框上，然后单击右侧的配置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27209%27%20height=%27333%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA5IiBoZWlnaHQ9IjMzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在展开的配置面板中，找到用户输入翻译内容的组件 (Textarea)，选择表单值作为工作流中content参数的值。配置完成后关闭参数配置面板。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27689%27%20height=%27281%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg5IiBoZWlnaHQ9IjI4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

6.

重复上述操作，将目标语言组件的值作为工作流lang参数的值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27697%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjk3IiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

a.

单击确认完成工作流的调用。​

7.

配置翻译结果数据。​

  * 最后需要将工作流返回的翻译内容展示在用户页面中。​

a.

在画布中，选中最后添加的Markdown组件。​

b.

在右侧的属性面板中，将鼠标悬浮至内容文本框内，然后单击出现的配置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27573%27%20height=%27360%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTczIiBoZWlnaHQ9IjM2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

在展开的面板中，首先在翻译结果下增加一行，然后选择工作流的返回数据作为翻译结果展示给用户。配置完成后，关闭配置面板。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27597%27%20height=%27276%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTk3IiBoZWlnaHQ9IjI3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤 3：预览用户界面​

1.

单击页面右侧配置面板的预览选项，查看页面效果，并进行测试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27274%27%20height=%27301%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc0IiBoZWlnaHQ9IjMwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在预览页面，进行测试。​

  * 说明

如果测试结果不符合预期，重新修改界面布局后，需要手动刷新 IDE 页面，再单击预览进行测试。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272134%27%20height=%27990.7857142857143%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEzNCIgaGVpZ2h0PSI5OTAuNzg1NzE0Mjg1NzE0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

界面模块

下一篇

快速搭建移动端用户界面