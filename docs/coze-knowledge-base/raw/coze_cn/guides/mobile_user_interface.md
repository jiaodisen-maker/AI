---
source_url: https://docs.coze.cn/guides/mobile_user_interface
title: '快速搭建移动端用户界面 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:47Z
---

# 快速搭建移动端用户界面 - 文档 - 扣子

快速搭建移动端用户界面

本教程以搭建一个AI 助手的用户界面为例，为你演示如何搭建移动端的用户界面。​

前提条件​

你已经通过工作流编排完后端业务逻辑。本教程中的 AI 助手应用，主要是通过大模型回答用户的问题，所以只需要创建一个包含大模型节点的对话流即可，详情请参考​步骤三：编排业务逻辑。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271842%27%20height=%27375.22222222222223%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/922d674948e9467089e5d65cd64c087a~tplv-goo7wpa0wc-quality:q75.image)​

​

本教程搭建用户界面的步骤如下图：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27569%27%20height=%27134%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a88137b5bcbf4621bf1599591ba76509~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤 1：设计用户界面​

在开始开发前，你需要设计 AI 助手的用户界面。​

AI 助手的界面应是类似通讯软件的对话式页面，以便用户能够与 AI 助手进行互动。用户界面编辑器提供了 AI 对话组件，你可以直接使用这个组件来快速搭建 AI 助手用户界面，从而简化开发流程。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27365%27%20height=%27181%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/be54f8e531154d40a0e79fb42ebc55d2~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤 2：搭建用户界面​

扣子编程提供了可视化的用户界面搭建能力，你可以通过拖拉拽的方式搭建一个用户界面，无需编写一行代码。​

参考以下操作，搭建 AI 助手应用的用户界面。​

1.

在低代码应用 IDE 中，单击页面上方的用户界面页签。​

2.

选择页面类型。​

  * 低代码应用支持发布为小程序等移动端应用，也可以发布为 Web 页面等网页应用。这里我们选择小程序和 H5。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27451%27%20height=%27269%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUxIiBoZWlnaHQ9IjI2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

搭建页面布局。​

  * AI 助手应用只有一个简单的对话窗口，所以我们只需要搭建一个页面并添加 AI 对话组件即可。​

a.

在画布中选中页面，并在右侧 Page1 配置面板中关闭导航栏。​

  * 移动端页面默认开启首页底部的导航栏，AI 助手应用只有一个页面，所以需要手动关闭底部的导航栏。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27388%27%20height=%27249%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg4IiBoZWlnaHQ9IjI0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

在组件面板中，找到 AI 组件 > AI对话组件，然后将 AI 对话组件拖入到画布中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27501%27%20height=%27242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAxIiBoZWlnaHQ9IjI0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

设置组件属性。​

a.

在画布中，选中拖入的 AI对话组件。组件名称为Chat1。​

b.

在 Chat1 组件的属性配置面板中，选择步骤三中搭建的对话流，即 ai_assistant。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27347%27%20height=%27213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ3IiBoZWlnaHQ9IjIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置效果如下： ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27567%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI0IiBoZWlnaHQ9IjU2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤 3：预览用户界面​

完成上述所有配置后，单击预览查看整体功能并进行体验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27277%27%20height=%27196%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc3IiBoZWlnaHQ9IjE5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

页面会展示 AI 助手在移动端的页面预览效果，你可以在页面下方的输入框中输入一段文字，并按回车键发送消息。AI 助手会立即回复你的问题。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27203%27%20height=%27418%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAzIiBoZWlnaHQ9IjQxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

上一篇

快速搭建网页端用户界面

下一篇

创建页面