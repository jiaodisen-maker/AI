---
source_url: https://docs.coze.cn/guides/use_plugin
title: '使用插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:55Z
---

# 使用插件 - 文档 - 扣子

使用插件

插件可以直接在低代码智能体内使用，拓展智能体的能力边界。插件也可以作为节点添加到工作流，执行一个操作。​

说明

  * 仅扣子付费套餐用户可使用三方付费插件。​

  * 添加了三方付费插件的低代码智能体或应用（工作流），不支持发布到飞书多维表格、掘金、豆包及部分公共渠道。​

​

为低代码智能体绑定插件​

可以将插件添加到低代码智能体内，扩展智能体的能力。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击项目管理。​

3.

单击指定的低代码智能体。​

4.

在智能体编排页面的技能 > 插件区域，添加插件。​

  * 支持通过以下方式添加插件：​

  * 直接添加插件。单击+图标，从工作空间或插件商店中挑选已发布的插件。如果没有合适的插件，也可以根据页面提示创建一个新的插件。​

  * 自动添加插件。单击自动添加图标，大模型会根据人设与回复逻辑，自动从商店中选择合适的插件添加到智能体中。​

  * 说明

使用大语言模型自动添加插件后，建议调试智能体，检查被添加的插件是否可以正常使用。​

​

5.

在添加插件页面，搜索并展开目标插件，单击目标工具对应的添加。​

  * 支持从插件商店中添加扣子编程官方插件或三方插件，也支持从当前工作空间的资源库中添加已发布的自定义插件。​

  * 首次添加某个三方付费插件时，系统将弹出插件开通提示框。确认开通后，才能使用该三方付费插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27388%27%20height=%27202%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8538b99daf0c4a84b221386a373776f1~tplv-goo7wpa0wc-quality:q75.image)​

​

6.

在智能体的人设与回复逻辑区域，定义何时使用插件，然后在预览与调试区域测试插件功能是否符合预期。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27427%27%20height=%27305%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI3IiBoZWlnaHQ9IjMwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为低代码工作流添加插件节点​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

单击指定的低代码工作流。​

4.

在工作流的编排页面中，选择添加节点 > 插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27304%27%20height=%27323%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA0IiBoZWlnaHQ9IjMyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

搜索并展开目标插件，单击目标工具对应的添加。​

  * 支持从插件商店中添加扣子编程官方插件或三方插件，也支持从当前工作空间的资源库中添加已发布的自定义插件。​

  * 首次添加某个三方付费插件时，系统将弹出插件开通提示框。确认开通后，才能使用该三方付费插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27388%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg4IiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在工作流的画布内，连接插件节点，并配置插件的输入参数来源。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27636%27%20height=%27192%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM2IiBoZWlnaHQ9IjE5MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在对话中使用插件​

对于工作流中绑定的插件节点，你在配置工作流时已设置了插件的输入参数来源，当对话触发工作流运行时，扣子编程会根据工作流的配置逻辑自动调用插件节点，完成工作流。对于直接绑定智能体的插件，智能体会根据对话内容自动判断何时调用插件回答用户的问题，并从用户 Query 中提取插件的输入参数，如果 Query 中未包含所有的必选参数，智能体会追问用户直到获得所有的必选参数。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27527%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI3IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为了提高插件调用时机的准确性，建议在人设与回复逻辑区域明确定义插件的使用场景，从而减少因模型回复随机性导致的插件调用不符合预期的情况。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27790%27%20height=%27349%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzkwIiBoZWlnaHQ9IjM0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

扩容插件 QPS​

针对已开通且支持扩容的三方付费插件及部分官方插件，扣子编程提供付费扩容服务。你可以根据业务需求，在扩容管理页面，找到目标插件申请扩容。​

  * 官方插件：根据页面提示填写并发数量，即可完成扩容。​

  * 三方付费插件：根据页面提示添加并发数量后，需等待插件开发者审核通过，才能完成扩容。​

详细说明，请参考​资源扩容费用。​

上一篇

流式插件配置教程

下一篇

通过固定 IP 访问插件