---
source_url: https://docs.coze.cn/guides/shortcuts
title: '快捷指令 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:01Z
---

# 快捷指令 - 文档 - 扣子

快捷指令

扣子编程支持开发者在搭建低代码智能体时创建一些快捷指令，方便用户在与低代码智能体会话时通过快捷指令快速、准确地输入信息。​

功能说明​

配置快捷指令后，智能体用户在智能体的对话框中可以直接通过指令发起预设的对话。快捷指令的行为可以是发送一段简单的文字、上传文件、使用插件或工作流等。多 Agent 模式下，全局配置中也支持添加快捷指令，默认不指定节点回答，智能体根据用户输入匹配对应的节点处理。​

例如在翻译智能体中增加一个快捷指令，即原文输入框和目标语言列表，对话时你只需输入待翻译的内容和语言即可快速下发一条翻译指令。​

快捷指令效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27392%27%20height=%27699.5980861244019%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0da970f1014543f48fc7dd8e0bf87154~tplv-goo7wpa0wc-quality:q75.image)​

​

​

配置示例：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271187%27%20height=%27557.0488188976378%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fa552a6ce35d4afab134975a9a42a1b9~tplv-goo7wpa0wc-quality:q75.image)​

​

​

创建简单指令​

参考以下步骤，创建一个简单快捷指令。​

1.

在编排页面，定位到快捷指令功能，然后单击 +。​

2.

在弹出的页面，完成以下配置。​

  * ​

配置​| 说明​  
---|---  
按钮名称​| 输入快捷指令的按钮名称。例如：AI 。​  
指令名称​| 输入唤起该指令的名称，只支持使用字母和下划线。例如get_ai_news。​仅发布到扣子商店会展示快捷指令框，其他渠道均不会展示快捷指令框，需输入指令名称唤起快捷指令。详细说明，请参考​发布渠道说明。​  
指令描述​| 添加指令说明信息。​  
指令行为​| 选择直接发送，即用户点击该指令时，直接发送一条消息给智能体。​  
指令内容​| 输入用户点击该指令时发送的内容。例如：发送最新的三条 AI 新闻。​  
  
​

3.

配置完成后，可以在调试区，直接点击快捷指令查看效果。​

  * 如下图所示（左侧是快捷指令配置截图，右侧是调试截图），当点击AI新闻指令时，会自动发送配置好的指令内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27447%27%20height=%27250%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ3IiBoZWlnaHQ9IjI1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

创建组件指令​

扣子编程提供了选择器、上传等组件，通过添加这些组件，可以设计更符合使用场景的快捷指令。​

参考以下步骤，创建一个带组件的快捷指令。​

1.

在智能体编排页面，定位到快捷指令功能，然后单击 +。​

2.

在弹出的页面，完成以下配置。​

  * ​

配置​| 说明​  
---|---  
按钮名称​| 输入快捷指令的按钮名称。例如：翻译 。​  
指令名称​| 输入唤起该指令的名称，只支持使用字母和下划线。例如translate。​仅发布到扣子商店会展示快捷指令框，其他渠道均不会展示快捷指令框，需输入指令名称唤起快捷指令。详细说明，请参考​发布渠道说明。​  
指令描述​| 添加指令说明信息。​  
指令行为​| 选择显示组件模板。​1.添加组件名称，并选择组件的类型。​2.单击+按钮，增加组件。​你可以在右侧面板实时预览组件效果。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271152%27%20height=%27289.74545454545455%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE1MiIgaGVpZ2h0PSIyODkuNzQ1NDU0NTQ1NDU0NTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​如果你想直接使用工作流或插件的输出结果作为组件组成，勾选直接使用插件或工作流，并选择一个插件/工作流。​系统会根据选择的插件/工作流的输出数据格式自动填充组件信息。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27416%27%20height=%27190%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE2IiBoZWlnaHQ9IjE5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
指令内容​| 输入用户点击该指令时发送的内容。​单击文本框上方的绑定按钮，插入组件。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27778%27%20height=%27196.54736842105262%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzc4IiBoZWlnaHQ9IjE5Ni41NDczNjg0MjEwNTI2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​所有添加的组件都必须要在指令内容中进行关联。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27739%27%20height=%27194.4736842105263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzM5IiBoZWlnaHQ9IjE5NC40NzM2ODQyMTA1MjYzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

3.

配置完成后，可以在调试区，直接点击快捷指令查看效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27488%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg4IiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

内置指令名称​

扣子编程提供了一些内置的指令名称。​

说明

微信/抖音小程序、微信、飞书、掘金渠道支持使用内置指令。​

​

  * /clear：清除当前智能体的对话上下文。​

  * /cancel_oauth：清除当前智能体中所有插件的 OAuth 鉴权。​

  * /shortcuts：列出当前智能体所有可用的快捷名称列表，包括自定义的指令名称和内置的指令名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27314%27%20height=%27214%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE0IiBoZWlnaHQ9IjIxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

发布渠道说明​

创建快捷指令后，仅发布到扣子商店会展示快捷指令框，其他渠道均不会展示快捷指令框，需输入指令名称唤起快捷指令。​

​

发布渠道​| 说明​  
---|---  
扣子商店​| 在智能体对话页面展示快捷指令框。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27523%27%20height=%27107%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIzIiBoZWlnaHQ9IjEwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
微信/抖音小程序、微信、飞书、豆包、多维表格、掘金、Chat SDK、API​| 在智能体对话页面，输入指令名称（例如 /getweather）唤起快捷指令。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27527%27%20height=%27144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI3IiBoZWlnaHQ9IjE0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

其他操作​

  * 拖拽快捷指令卡片调整快捷指令的顺序。​

  * 单击编辑图标修改快捷指令。​

  * 单击删除图标删除快捷指令。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27408%27%20height=%27136%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA4IiBoZWlnaHQ9IjEzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

开场白

下一篇

声纹识别