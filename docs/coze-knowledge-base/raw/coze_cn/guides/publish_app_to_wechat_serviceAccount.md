---
source_url: https://docs.coze.cn/guides/publish_app_to_wechat_serviceAccount
title: '发布到微信服务号 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:57Z
---

# 发布到微信服务号 - 文档 - 扣子

发布到微信服务号

你可以将搭建的低代码应用发布到微信公众号（服务号）中。发布后，服务号就可以使用应用回复用户消息，助力运营。​

注意

如果您之前绑定过微信服务号，则在应用发布页面的原绑定渠道区域会提示【即将下线】微信公众号（服务号），该场景下您需要先解绑原发布渠道，然后参考本文操作重新绑定微信公众号（服务号）渠道进行发布。​

​

使用限制​

  * 一个应用只能发布到一个企业服务号。​

  * 确保微信服务号已经完成了认证。未认证和认证中的服务号无法接收消息。​

  * 支持在回复服务号时上传图片，但图片大小不能超过 10 MB。​

前提条件​

  * 已经创建了微信服务号。​

  * 待发布的应用至少包含一个对话流。​

  * 扣子应用的发布者必须是扣子应用的所有者，协作者或管理员等角色均不支持发布应用。​

注意

发布应用到微信服务号时，仅发布应用中的指定对话流。​

​

步骤一：获取微信服务号的开发者 ID​

1.

访问[微信开发者平台](<https://developers.weixin.qq.com/platform>)并登录你的服务号。​

2.

在我的业务 > 公众号页面，获取开发者ID(AppID)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27306.94444444444446%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/83d9a40ca3e84618ad20caa3fc11149e~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：发布应用到微信服务号​

以下是将应用发布到微信服务号的详细步骤：​

3.

登录[扣子编程](<https://code.coze.cn/home>)。​

4.

在页面顶部空间列表中选择目标工作空间。 ​

5.

在项目开发页面，选择目标低代码应用，在应用编排页面右上角，单击发布。 ​

6.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。​

  * 版本描述：可选，说明该版本更新的内容。​

7.

在 选择发布平台 > 发布到通讯或社交平台 选项，选择待发布的对话流。当用户在微信服务号发送消息时，将调用该对话流来接收用户消息。​

8.

找到微信服务号发布渠道，单击配置。​

9.

在 AppID 输入框内，填写微信服务号的开发者 ID，并单击保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27544%27%20height=%27407%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ0IiBoZWlnaHQ9IjQwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

10.

跳转到公众平台账号授权页面，使用公众平台绑定的管理员个人微信号扫描二维码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27602%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAyIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

11.

在微信移动端，根据页面提示选择服务号并确认授权。​

  * 授权成功的页面提示如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27203%27%20height=%27367%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAzIiBoZWlnaHQ9IjM2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

12.

返回应用发布页面，选中微信公众号（服务号）发布平台，并设置发布记录后，单击页面右上角的发布。​

  * 成功发布后，你可以前往微信服务号与应用对话。​

上一篇

发布到微信客服

下一篇

发布到微信订阅号