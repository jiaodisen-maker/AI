---
source_url: https://docs.coze.cn/guides/lottie_mini_program
title: 'Lottie 动画 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:37:36Z
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

支持从本地上传 Lottie JSON 文件并自动解析。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27563%27%20height=%27227%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a2e3fe7b9f2846ecb57cf983f30720f1~tplv-goo7wpa0wc-quality:q75.image)​

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

例如在解题详情页面，添加了 Lottie 动画组件（Lottie1）和文本组件（text14），Lottie 动画组件用于展示应用正处于解题状态中，文本组件用于展示解题分析内容。为了实现当文本组件开始输出解题内容时，自动隐藏 Lottie 动画组件的效果，你可以在 Lottie 动画组件的可见性属性中，添加变量{{ Text14.content }}。当文本组件中开始输出解题内容时，{{ Text14.content }} 值变为 true，Lottie 动画组件将自动隐藏。​

可见性配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27749%27%20height=%271024.4942528735633%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQ5IiBoZWlnaHQ9IjEwMjQuNDk0MjUyODczNTYzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

开始解题时播放动画​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27431%27%20height=%27970.4451612903225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDMxIiBoZWlnaHQ9Ijk3MC40NDUxNjEyOTAzMjI1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

出现答案解析时隐藏 Lottie 动画组件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27441%27%20height=%27945.3620689655173%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQxIiBoZWlnaHQ9Ijk0NS4zNjIwNjg5NjU1MTczIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

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

[拍照解题模板](<https://www.coze.cn/template/project/7475734454254895131?from=store_search_suggestion>)为扣子编程的官方模板，本示例基于拍照解题模板，添加了 Lottie 动画，提升应用的交互体验。例如使用者上传题目，单击开始解题后，应用立即开始解题并自动播放 Lottie 动画，清晰地表达应用正在解题的状态中，使得界面交互更加生动友好；当应用完成解题后，Lottie 动画消失同时界面上展示具体的答案。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272441%27%20height=%271044.5076201641266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ0MSIgaGVpZ2h0PSIxMDQ0LjUwNzYyMDE2NDEyNjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

具体效果图如下：​

开始解题时自动播放动画​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27431%27%20height=%27970.4451612903225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDMxIiBoZWlnaHQ9Ijk3MC40NDUxNjEyOTAzMjI1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

解题过程中循环播放动画​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27436%27%20height=%27967.6387096774193%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM2IiBoZWlnaHQ9Ijk2Ny42Mzg3MDk2Nzc0MTkzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

展示答案后隐藏动画​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27434%27%20height=%27971.6%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM0IiBoZWlnaHQ9Ijk3MS42IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

​

​

​

上一篇

图片

下一篇

轮播