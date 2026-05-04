---
source_url: https://docs.coze.cn/guides/opening_dialog
title: '开场白 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:55Z
---

# 开场白 - 文档 - 扣子

开场白

开场白是用户进入低代码智能体后自动展示的引导信息。它的主要目的是帮助用户理解智能体的用途，以及如何与其进行交互。​

说明

开场白功能支持如下平台：​

  * 豆包、微信公众号（服务号）、微信订阅号、微信小程序、抖音小程序、飞书、Chat SDK 和 API（可通过​查看智能体配置 API 查看）。​

  * 微信小程序和抖音小程序：仅支持展示全部预置问题，不支持展示部分预置问题。​

  * 微信公众号（服务号）和微信订阅号：不支持预置问题。​

​

常见的开场白效果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27435%27%20height=%27393%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/32cf8ea77dde4e77b1fca6817a122983~tplv-goo7wpa0wc-quality:q75.image)​

​

设置开场白​

在智能体编排页面的开场白区域，可以设置开场白文案和开场白预置问题。​

开场白文案​

开场白文案用于帮助用户快速理解智能体的能力。用户进入智能体后，智能体会默认发送这段预先设置的开场白文案。开场白文案为 Markdown 格式，你可以在 Markdown 编辑器中设计智能体的开场白，调试区域会同步展示开场白的预览效果。你也可以通过 AI 自动生成开场白。​

通过 Markdown 编辑器，你可以调整开场白文案样式，例如设置层级、加粗、斜体、删除线等样式效果。也可以添加链接、图片、代码块和 {{user_name}} 变量。其中，{{user_name}} 会自动引用扣子用户的昵称。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271119%27%20height=%27466.25%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTExOSIgaGVpZ2h0PSI0NjYuMjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

开场白预置问题​

首次使用智能体的用户往往需要一些对话示例体验智能体的能力和效果，你可以为智能体设置开场白预置问题，提供一些推荐问题。这些推荐问题会展示在开场白文案之下，用户单击问题即可发起一次对话，帮助用户快速体验 Bot。如果设置了多个开场白问题，则默认随机显示 3 条预置问题。你也可以开启全部展示，开启后，开场白会默认按顺序显示所有预置问题。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271144%27%20height=%27525.6574074074074%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE0NCIgaGVpZ2h0PSI1MjUuNjU3NDA3NDA3NDA3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例​

以[雅思口语专家](<https://www.coze.cn/store/bot/7389299390185209892>)智能体为例，同时设置开场白文案和预置问题。​

开场白配置示例：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271150%27%20height=%27471.18055555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE1MCIgaGVpZ2h0PSI0NzEuMTgwNTU1NTU1NTU1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

展示效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27399%27%20height=%27425%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk5IiBoZWlnaHQ9IjQyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

记忆库

下一篇

快捷指令