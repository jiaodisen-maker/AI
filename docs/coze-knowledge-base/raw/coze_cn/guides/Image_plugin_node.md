---
source_url: https://docs.coze.cn/guides/Image_plugin_node
title: '图像处理插件节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:44Z
---

# 图像处理插件节点 - 文档 - 扣子

图像处理插件节点

扣子编程提供了丰富的图像处理插件，你可以在低代码工作流中添加不同的图像处理插件节点，实现抠图、优化图像提示词、裁剪图片、美颜、画质提升等功能。​

使用限制​

​

限制​| 说明​  
---|---  
并发限制​| 扣子主账号及其所有子账号共享并发限制，具体的并发限制请参考​插件费用。​  
图片有效期​| 大多数图像处理插件输出的图片为链接格式，有效期为 1 年，建议在到期前及时保存。​说明​Doubao-图像生成插件中的 SeedEdit 工具输出的图片有效期约为 20 天。​​  
  
​

节点说明​

在 AI 智能处理场景下，你可以在低代码工作流中添加各个图像处理节点来处理图像，以优化图像质量和满足特定需求。例如添加抠图插件节点分离主体与背景；添加画质提升插件节点增强图片清晰度；添加图像美颜插件节点优化人像图片等。​

不同图像处理插件节点的输入参数和输出参数有所差异，基本配置流程为上传原始图片，根据各个插件特有参数完成配置，最终获取处理后的图片。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27532%27%20height=%27170%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ea56434d86c444d7ad1c5e618bb141d5~tplv-goo7wpa0wc-quality:q75.image)​

​

其中官方插件使用说明可参考：​

  * ​添加文字插件​

  * ​提示词优化插件​

  * ​图片裁剪插件​

  * ​图片叠图插件​

  * ​图片缩放插件​

  * ​图片旋转插件​

  * ​图像美颜插件​

  * ​图像调整插件​

  * ​ByteArtist 插件​

  * ​背景替换插件​

  * ​宠物风格化插件​

  * ​Doubao-图像生成插件​

  * ​风格滤镜插件​

  * ​光影融合插件​

  * ​画质提升插件​

  * ​指令编辑插件​

  * ​智能抠图插件​

  * ​智能扩图插件​

  * ​智能绘图_文生图插件​

  * ​火山图像增强插件​

  * ​图片超分辨率插件​

  * ​商品图像分割插件​

  * ​Doubao-SeedEdit-3.0 插件​

  * ​Doubao-Seedream-3.0 插件​

  * ​Doubao-Seedream-4.0 插件​

配置图像处理插件节点​

不同图像处理插件节点对应的配置不同。本文以抠图插件为例，介绍图像处理插件节点的基本配置。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27936%27%20height=%27695.6756756756756%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTM2IiBoZWlnaHQ9IjY5NS42NzU2NzU2NzU2NzU2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

输入​

图像处理插件节点的输入参数。以抠图插件节点为例，输入参数如下所示：​

  * 上传图：设置原图来源，支持上传图片或引用上游节点的输出参数。​

  * 输出图模式：设置输出图的模式。可选项包括透明背景图和蒙版矢量图。​

  * 透明背景图：输出图像的背景为透明。​

  * 蒙版矢量图：输出图像为矢量格式的蒙版。​

  * 提示词：用于定义抠图内容的提示词。如果不填，插件会自动识别图片中的主体部分。​

输出​

抠图插件节点的输出参数固定为：​

  * data：抠图后的最终图像。通常是一个公开可访问的 URL 链接。在输入参数中，设置输出图模式为透明背景图时，data 参数才生效。​

  * mask：抠图区域的蒙板矢量图。在输入参数中，设置输出图模式为蒙版矢量图时，mask 参数才生效。​

  * msg：节点执行状态，success 表示处理成功。​

示例​

例如添加一个抠图工作流，通过头条图片搜索（ToutiaoPictureSearch）插件从互联网中搜索图片，并通过智能抠图（cutout）插件对搜索结果进行智能截图，最终返回截图后的图像和搜索到的原始图像。重要配置说明如下：​

  * 智能抠图插件的输入参数​

  * 上传图：设置为变量，即引用 ToutiaoPictureSearch 节点的输出参数 display_url，获取搜索到的图片。​

  * 输出图模式：选中透明背景图。​

  * 结束节点的输出变量​

  * output：引用 cutout 节点的输出变量 data，即返回截图后的图像。​

  * output1：引用 ToutiaoPictureSearch 节点的输出参数 display_url，即返回通过头条图片搜索插件搜索到的原始图像。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27740%27%20height=%27232%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQwIiBoZWlnaHQ9IjIzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

​

​

上一篇

画板节点

下一篇

视频生成节点