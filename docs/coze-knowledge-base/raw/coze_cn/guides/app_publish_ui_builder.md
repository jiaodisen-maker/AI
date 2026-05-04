---
source_url: https://docs.coze.cn/guides/app_publish_ui_builder
title: '发布为 Web SDK - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:45:13Z
---

# 发布为 Web SDK - 文档 - 扣子

发布为 Web SDK

扣子 Web SDK 是一个功能强大的 JavaScript 库。开发者发布低代码应用后，扣子会将低代码应用中的用户界面和工作流打包发布到 Web SDK，方便开发者将其无缝嵌入到各类业务系统中，快速实现界面集成，适用于需要将应用界面嵌入到内部系统或第三方平台等场景。本文介绍如何将已开发的低代码应用发布到 Web SDK。​

前提条件​

  * 待发布的应用至少包含一个对话流，且已配置用户界面。​

  * 用户界面仅支持网页端，不支持小程序端。小程序端界面不支持发布为 Web SDK。​

  * 在发布前已[创建个人令牌](<https://www.coze.cn/open/oauth/pats>)，或实现了 OAuth 鉴权逻辑。详细说明可参考​鉴权方式概述。​

  * 发布者必须拥有发布权限，即发布者必须是应用的所有者或协作者。详细说明可参考​多人协作开发低代码应用。​

将应用发布到 Web SDK​

以下是将低代码应用发布为 Web SDK 的详细步骤：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择目标低代码应用。 ​

4.

在应用编排页面的右上角，单击发布，在发布页面填写版本信息：​

  * 版本号：必填，版本号用于区分不同发布版本，确保应用更新的可追溯性。​

  * 版本描述：可选，说明该版本更新的内容，以便快速了解版本变更内容。​

5.

在选择发布平台 > API 或 SDK 区域，选择 Web SDK ，单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27451.38888888888886%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8fbd7d0d8a874f0986e62ba253d94d6f~tplv-goo7wpa0wc-quality:q75.image)​

​

  * 发布完成后，你可以应用编排页面的版本记录中查看指定版本的发布结果。请注意应用审核需要一定的时间，请耐心等待。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27268.51851851851853%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI2OC41MTg1MTg1MTg1MTg1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

使用 Web SDK​

你可以在[扣子 Playground 的 UI Builder](<https://www.coze.cn/open/playground/uibuilder>) 页面体验 Web SDK 的使用效果。安装和使用 Web SDK 的详细方法请参见​Web SDK（低代码）。​

撤销发布 Web SDK​

如果不再需要通过 Web SDK 方式使用扣子应用，可以在发布页面撤销发布到 Web SDK。撤销后，调用 Web SDK 时会收到错误提示。​

撤销发布的详细操作步骤如下：​

1.

在应用编排页面右上角单击发布，进入应用发布页面。​

2.

在选择发布平台 > API 或 SDK 区域，单击 Web SDK 卡片中的撤销发布。在弹出的对话框中，单击撤销发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27310.18518518518516%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMxMC4xODUxODUxODUxODUxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 撤销发布操作立即生效。撤销后，发布历史中显示的历史版本发布状态不会变更，但是应用会与 Web SDK 解绑。你将无法通过调用 Web SDK 的方式与应用交互。​

​

上一篇

发布为 MCP 工具

下一篇

发布到小米应用商店