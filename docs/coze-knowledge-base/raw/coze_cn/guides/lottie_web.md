---
source_url: https://docs.coze.cn/guides/lottie_web
title: 'Lottie 动画 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:38:40Z
---

# Lottie 动画 - 文档 - 扣子

Lottie 动画

Lottie 动画是一款轻量级、高性能的动画解决方案。扣子低代码应用支持添加 Lottie 动画组件用于播放 Lottie 动画，增强低代码应用的视觉效果和交互体验。​

属性设置​

Lottie 动画组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

内置丰富的动画库​

Lottie 动画组件内置了丰富的动画资源库，你可以直接挑选并应用合适的动画效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27257%27%20height=%27356%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1c5f6a0c09a745e58c02f4ea9d01fd0d~tplv-goo7wpa0wc-quality:q75.image)​

​

自定义 Lottie 动画​

支持从本地上传 Lottie JSON 文件并自动解析为 Lottie 动画。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27548%27%20height=%27137%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a14cac9b3eb745e0a47056ec23b897a7~tplv-goo7wpa0wc-quality:q75.image)​

​

循环播放​

打开循环播放后，Lottie 动画会在界面加载时循环播放。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27289%27%20height=%27166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg5IiBoZWlnaHQ9IjE2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

自动播放​

打开自动播放后，Lottie 动画会在界面加载时自动播放。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27292%27%20height=%27201%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyIiBoZWlnaHQ9IjIwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

控制 Lottie 动画组件隐藏或显示的参数，支持在特定条件下隐藏 Lottie 动画组件。​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制图片组件的可见性。​

例如在文本生成页面，添加了 Lottie 动画组件（Lottie1）和 Markdown 组件（Markdown1），Lottie 动画组件用于展示应用正处于文本生成状态中，Markdown 组件用于展示生成的文本内容。为了实现当 Markdown 组件开始输出内容时，自动隐藏 Lottie 动画组件的效果，你可以在 Lottie 动画组件的可见性属性中，添加变量{{ Markdown1.content }}。当文本组件中开始输出文本内容时，{{ Markdown1.content }} 值变为 true，Lottie 动画组件将自动隐藏。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271514%27%20height=%27850.1828839390387%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUxNCIgaGVpZ2h0PSI4NTAuMTgyODgzOTM5MDM4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

生成文本后，Lottie 动画组件被隐藏。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27280%27%20height=%27289%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgwIiBoZWlnaHQ9IjI4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

事件设置​

通过配置 Lottie 动画组件的事件，可以为 Lottie 动画组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击时：当用户点击 Lottie 动画组件时触发。​

  * 加载时：当 Lottie 动画组件完成加载时触发。​

  * 播放完成时：当 Lottie 动画播放完成时触发。​

  
组件方法​| 支持以下方法：​

  * 播放：播放 Lottie 动画。​

  * 停止：停止 Lottie 动画。​

  * 暂停：暂停 Lottie 动画。​

  * 设置隐藏：隐藏 Lottie 动画。​

  
  
​

配置示例​

[城市天气画报模板](<https://www.coze.cn/template/project/7442325596329295872?>)为扣子官方模板，本案例基于城市天气画报模板，添加了 Lottie 动画，提升应用的交互体验。当使用者输入城市名，单击确认后，应用立即开始生成城市画报并自动播放 Lottie 动画，清晰地表达应用正在生成天气画报的状态中，使得界面交互更加生动友好。当应用生成天气画报后，Lottie 动画消失同时界面上展示城市天气画报。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272437%27%20height=%271054.223915592028%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQzNyIgaGVpZ2h0PSIxMDU0LjIyMzkxNTU5MjAyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

具体效果图如下：​

输入城市名称​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27486%27%20height=%27338.94464944649445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg2IiBoZWlnaHQ9IjMzOC45NDQ2NDk0NDY0OTQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

开始生成图片时循环播放动画​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27630%27%20height=%27485.8671586715867%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMwIiBoZWlnaHQ9IjQ4NS44NjcxNTg2NzE1ODY3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

生成图片后隐藏动画​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27625%27%20height=%27618.0811808118082%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI1IiBoZWlnaHQ9IjYxOC4wODExODA4MTE4MDgyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

​

上一篇

图片

下一篇

视频