---
source_url: https://docs.coze.cn/guides/video_web
title: '视频 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:38:43Z
---

# 视频 - 文档 - 扣子

视频

视频组件用于播放视频内容，支持播放本地上传的视频文件，也可绑定工作流返回值或直接填写视频 URL，能够灵活满足不同视频播放需求。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27536%27%20height=%27245%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/03ee6d1ebfa44f608b5cd447afb8cf5f~tplv-goo7wpa0wc-quality:q75.image)​

​

视频限制​

  * 仅支持 MP4、AVI、MOV 格式。​

  * 视频文件大小需小于 500 MB。​

属性设置​

视频组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

配置视频源​

你可以上传本地视频文件、直接输入视频 URL（绑定静态数据）或绑定工作流返回的视频 URL（绑定动态数据）。​

本地上传​

在本地上传页签下，单击上传，上传本地视频文件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27181%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/433e3adcf94b428584d2c6fc0c37e236~tplv-goo7wpa0wc-quality:q75.image)​

​

绑定静态数据​

在绑定数据页签下，输入视频的 URL。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27268%27%20height=%27266%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f14b31b047e04fd8af71eb6c678c4d17~tplv-goo7wpa0wc-quality:q75.image)​

​

​

绑定动态数据​

1.

为组件添加事件，用于调用工作流。​

  * 可以选择本应用中的任意目标组件。​

2.

在绑定数据页签下，选择工作流的输出参数。具体操作，请参考​配置示例。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27248%27%20height=%27224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ4IiBoZWlnaHQ9IjIyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

全屏播放​

打开全屏播放开关后，视频组件中将显示全屏播放按钮。单击该按钮后，可以全屏播放视频。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27672%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcyIiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

循环播放​

打开循环播放后，视频会在界面中循环播放。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27294%27%20height=%27273%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0IiBoZWlnaHQ9IjI3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

隐藏组件​

视频组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考​隐藏组件。​

事件设置​

通过配置视频组件的事件，可以为视频组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 支持以下事件类型：​

  * 点击时：单击视频时，触发事件。​

  * 开始播放时：视频开始播放时，触发事件。​

  * 暂停播放时：视频暂停播放时，触发事件。​

  * 播放结束时：视频结束播放时，触发事件。​

  
组件方法​| 支持以下组件方法：​

  * 播放：播放视频​

  * 暂停：暂停视频​

  * 设置隐藏：隐藏组件，使其不可见。​

  
  
​

配置示例​

例如搭建一个用于生成及展示视频的应用，则你可以创建一个视频生成的工作流，并通过视频组件动态展示。具体操作如下：​

1.

创建工作流（video）。​

  * 使用视频生成节点生成视频。其中，在结束节点中，设置输出变量 output 的值为视频生成节点输出结果中的 video 参数（生成的视频 URL）。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27808%27%20height=%27163%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODA4IiBoZWlnaHQ9IjE2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

搭建网页。​

  * 搭建一个视频生成网页，包括容器组件、文本输入组件、按钮组件和视频组件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27692%27%20height=%27439%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjkyIiBoZWlnaHQ9IjQzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

为按钮组件（Button1）配置事件。​

  * 输入提示词，单击生成视频按钮后，将触发工作流（video）生成视频。工作流的输入参数 input 引用文本输入组件（Textarea1）的值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27243%27%20height=%27361%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQzIiBoZWlnaHQ9IjM2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

为视频组件绑定数据，即绑定工作流（video）的输出参数 output。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27244%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ0IiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

预览效果。​

  * 输入风吹动窗帘和花朵，光线变化，固定镜头，单击生成视频后，页面中将展示生成的视频。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27650%27%20height=%27490%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjUwIiBoZWlnaHQ9IjQ5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

Lottie 动画

下一篇

按钮