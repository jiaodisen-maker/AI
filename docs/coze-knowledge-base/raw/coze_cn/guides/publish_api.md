---
source_url: https://docs.coze.cn/guides/publish_api
title: '发布为 API 服务 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:38Z
---

# 发布为 API 服务 - 文档 - 扣子

发布为 API 服务

将低代码应用发布为 API 服务后，可以通过调用工作流 API 接口的方式使用应用程序。本文介绍如何将完成开发的应用发布为 API 服务。​

前提条件​

要将应用发布为 API，必须满足以下条件：​

  * 待发布的应用至少包含一个工作流。​

  * 在发布前已[创建个人令牌](<https://www.coze.cn/open/oauth/pats>)，或实现了 OAuth 鉴权逻辑。详细说明可参考​鉴权方式概述。​

  * 发布者必须拥有发布权限，即发布者必须是应用的所有者。详细说明可参考​多人协作开发低代码应用。​

说明

建议经过充分的试运行后再发布应用，否则可能导致发布时打包失败，或应用线上运行异常。​

​

发布应用为 API​

以下是将应用发布为 API 的详细步骤：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择目标应用，进入应用的编排页面。​

4.

在页面右上角，单击发布，进入应用发布页面。​

5.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。​

  * 版本描述：可选，说明该版本更新的内容。​

6.

在选择发布平台 > 发布为 API 选项，选择 API。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27356%27%20height=%27165%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2757ded267744b4e9e3ee6b4a2286813~tplv-goo7wpa0wc-quality:q75.image)​

​

7.

单击发布。​

  * 发布后，你可以在当前页面查看发布环节的整体流程进度、最终发布状态。其中应用审核需要一定的时间，请耐心等待。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27419%27%20height=%27259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE5IiBoZWlnaHQ9IjI1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 你也可以在应用编排页面右上角的发布状态处查看发布结果。详细说明可参考​查看应用发布状态。​

通过 API 运行应用​

将扣子应用发布为 API 服务之后，你可以通过工作流相关的 API 调用工作流和对话流。详细说明可参考：​

  * ​通过 API 运行应用工作流​

  * ​执行对话流​

撤销发布​

如果不再需要通过 API 方式使用应用，可以在发布页面撤销发布到 API。撤销后，调用工作流 API 时会收到工作流未发布的相关错误提示。​

撤销发布的详细操作步骤如下：​

1.

在应用编排页面右上角单击发布，进入应用发布页面。​

2.

在选择发布平台 > 发布为 API 选项，选择 Agent as API，此时会显示撤销发布按钮。​

3.

单击撤销发布。​

4.

在弹出的对话框中，单击撤销发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27327%27%20height=%27155%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI3IiBoZWlnaHQ9IjE1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 撤销发布操作立即生效。撤销后，发布历史中显示的历史版本发布状态不会变更，但是应用会与 API 接口解绑。你将无法通过调用 API 的方式与应用交互。​

​

​

​

上一篇

发布到企业商店

下一篇

通过 API 运行应用工作流