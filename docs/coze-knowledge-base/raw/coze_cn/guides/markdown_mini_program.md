---
source_url: https://docs.coze.cn/guides/markdown_mini_program
title: 'Markdown - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:37:28Z
---

# Markdown - 文档 - 扣子

Markdown

Markdown 组件用于渲染 Markdown 格式的文本。​

属性设置​

Markdown 组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

常用语法​

常用的 Markdown 语法及示例如下表所示。​

说明

小程序端的 Markdown 组件不支持嵌入 html 标签，不支持添加视频、音频等媒体元素。​

​

​

元素​| 语法​| 效果图​  
---|---|---  
标题​| ​Markdown复制# 一级标题​## 二级标题​### 三级标题​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27152%27%20height=%27121%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/de221062d8144d72964c8bf25fbd56ae~tplv-goo7wpa0wc-quality:q75.image)​​  
加粗文本​| ​Markdown复制**加粗文本**​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27358%27%20height=%2739%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/327311f579964bc9b9ddb047643cd170~tplv-goo7wpa0wc-quality:q75.image)​​​  
斜体文本​| ​Markdown复制*斜体文本*​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27378%27%20height=%2741%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d0d5689f9dc44642b34881597a9b9d8e~tplv-goo7wpa0wc-quality:q75.image)​​​  
有序列表​| ​Markdown复制1\. 有序列表项一​2\. 有序列表项二​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27205%27%20height=%2766%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA1IiBoZWlnaHQ9IjY2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
无序列表​| ​Markdown复制\- 无序列表项一​\- 无序列表项二​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27177%27%20height=%2768%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc3IiBoZWlnaHQ9IjY4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
引用​| ​Markdown复制> 这是一个引用。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27269%27%20height=%2754%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY5IiBoZWlnaHQ9IjU0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
链接​| ​Markdown复制单击[链接](https://www.coze.cn/docs/guides/webview)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27155%27%20height=%2736%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1IiBoZWlnaHQ9IjM2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
图片​| ​Markdown复制![这是一个图片](https://lf-coze-web-cdn.coze.cn/obj/coze-web-cn/flow/bot-studio/app-builder/example-cn.png)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27305%27%20height=%27191%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA1IiBoZWlnaHQ9IjE5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

绑定数据​

Markdown 组件支持引用工作流的返回数据、组件内容、局部上下文、系统变量、界面变量等变量内容。你可以通过引用变量为 Markdown 组件绑定动态数据。详情请参见​设置组件内容参数。​

例如创建一个搜索图片的工作流，将该工作流的搜索结果（图片 URL），绑定到 Markdown 组件的图片元素中，并为 Markdown 组件配置一个事件，当 Markdown 组件加载时，自动触发工作流的调用，从而实现动态更新组件内容。​

绑定数据​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27835%27%20height=%27255.05454545454546%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODM1IiBoZWlnaHQ9IjI1NS4wNTQ1NDU0NTQ1NDU0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置事件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27470%27%20height=%27702.4363636363637%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcwIiBoZWlnaHQ9IjcwMi40MzYzNjM2MzYzNjM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

展示效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27439%27%20height=%27314.4836363636363%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM5IiBoZWlnaHQ9IjMxNC40ODM2MzYzNjM2MzYzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

设置元素对齐方式​

你可以通过 Markdown 组件属性中的水平对齐、垂直对齐配置项，一键调整 Markdown 元素的对齐方式。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27577%27%20height=%27454%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc3IiBoZWlnaHQ9IjQ1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置文本颜色​

你可以通过 Markdown 组件属性中的颜色配置项，设置 Markdown 组件中纯文本元素的显示颜色。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27580%27%20height=%27455%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgwIiBoZWlnaHQ9IjQ1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置最大行数​

你可以通过 Markdown 组件属性中的最大行数配置项，配置 Markdown 组件中标题和正文元素的最大显示行数，超过最大行数后显示为 ...。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27576%27%20height=%27386%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc2IiBoZWlnaHQ9IjM4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

添加边框和阴影效果​

你可以通过 Markdown 组件属性中的圆角、边框、阴影等配置项，设置 Markdown 组件添加边框及阴影效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27599%27%20height=%27438%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTk5IiBoZWlnaHQ9IjQzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

Markdown 组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考​隐藏组件。​

事件设置​

通过配置 Markdown 组件的事件，可以为 Markdown 组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 当 Markdown 组件完成加载时触发事件。​  
组件方法​| 支持以下方法：​

  * 清除：清除组件的内容，例如 Markdown 组件中的文字。​

  * 设置内容：为组件设置或更新内容。​

  * 复制到剪切板：复制文本内容到剪切板。​

  
  
​

​

上一篇

图标

下一篇

音频