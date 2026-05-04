---
source_url: https://docs.coze.cn/guides/publish_app_to_web_sdk
title: '发布为 Chat SDK - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:43Z
---

# 发布为 Chat SDK - 文档 - 扣子

发布为 Chat SDK

扣子 Chat SDK 是一个功能强大的 JavaScript 库，旨在帮助开发者轻松集成扣子 OpenAPI 的对话和文件上传等功能。通过使用 Chat SDK，开发者可以快速、高效地构建聊天应用。本文介绍如何将已开发的低代码应用发布到 Chat SDK。​

前提条件​

  * 待发布的应用至少包含一个对话流。​

  * 在发布前已[创建个人令牌](<https://www.coze.cn/open/oauth/pats>)，或实现了 OAuth 鉴权逻辑。详细说明可参考​鉴权方式概述。​

  * 发布者必须拥有发布权限，即发布者必须是应用的所有者。详细说明可参考​多人协作开发低代码应用。​

注意

发布应用为 Chat SDK 时，仅发布应用中的指定对话流。​

​

将应用发布到 Chat SDK​

以下是将低代码应用发布为 Chat SDK 的详细步骤：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择目标项目，进入应用的编排页面。​

4.

在页面右上角，单击发布，进入应用发布页面。​

5.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。​

  * 版本描述：可选，说明该版本更新的内容。​

6.

在选择发布平台 > 发布为 API 选项，选择 Chat SDK 后，在下拉框中选择需要发布的对话流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27470%27%20height=%27274%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9b9fabf30b2a458ea4b1ca268de58fc0~tplv-goo7wpa0wc-quality:q75.image)​

​

7.

单击发布。​

  * 发布完成后，你可以在当前页面查看发布环节的整体流程进度和最终发布状态。请注意应用审核需要一定的时间，请耐心等待。​

使用 Chat SDK​

关于如何使用 Chat SDK，参阅​安装并使用 Chat SDK。​

撤销发布 Chat SDK​

如果不再需要通过 Chat SDK 方式使用扣子应用，可以在发布页面撤销发布到 Chat SDK。撤销后，调用 Chat SDK 时会收到对话流未发布的相关错误提示。​

撤销发布的详细操作步骤如下：​

1.

在应用编排页面右上角单击发布，进入应用发布页面。​

2.

在选择发布平台 > 发布为 API 选项，选择 Chat SDK，此时会显示撤销发布按钮。​

3.

单击撤销发布。​

4.

在弹出的对话框中，单击撤销发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27196%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA0IiBoZWlnaHQ9IjE5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 撤销发布操作立即生效。撤销后，发布历史中显示的历史版本发布状态不会变更，但是应用会与 Chat SDK 解绑。你将无法通过调用 Chat SDK 的方式与应用交互。​

​

​

上一篇

通过 API 运行应用工作流

下一篇

发布到抖音小程序