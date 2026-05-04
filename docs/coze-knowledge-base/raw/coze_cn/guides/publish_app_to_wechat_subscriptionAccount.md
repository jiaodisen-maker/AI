---
source_url: https://docs.coze.cn/guides/publish_app_to_wechat_subscriptionAccount
title: '发布到微信订阅号 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:45:00Z
---

# 发布到微信订阅号 - 文档 - 扣子

发布到微信订阅号

你可以将搭建的低代码应用发布到微信公众号（订阅号）中。发布后，订阅号就可以使用应用回复用户消息，助力运营。​

使用限制​

  * 一个应用只能发布到一个微信订阅号。​

  * 支持在回复订阅号时上传图片，但图片大小不能超过 10 MB。​

  * 每次回复消息时，只能回复一张图片。​

  * 如果模型返回的是图文混排的内容，则直接返回完整的Markdown内容。​

  * 如果模型生成了多张 Markdown 语法的图片内容，最终会解析返回第一张图片，多余图片会被丢弃。​

前提条件​

  * 已经创建了微信订阅号。​

  * 待发布的应用至少包含一个对话流。​

  * 扣子应用的发布者必须是扣子应用的所有者，协作者或管理员等角色均不支持发布应用。​

注意

发布应用到微信订阅号时，仅发布应用中的指定对话流。​

​

步骤一：获取微信订阅号的开发者 ID​

1.

访问[微信开发者平台](<https://developers.weixin.qq.com/platform>)并登录你的服务号。​

2.

在我的业务 > 公众号页面，获取开发者ID(AppID)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27306.94444444444446%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/83d9a40ca3e84618ad20caa3fc11149e~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：发布应用到微信订阅号​

以下是将应用发布到微信订阅号的详细步骤：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择目标低代码应用，在应用编排页面右上角，单击发布。 ​

4.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。​

  * 版本描述：可选，说明该版本更新的内容。​

5.

在 选择发布平台 > 发布到通讯或社交平台 选项，选择待发布的对话流。当用户在微信订阅号发送消息时，将调用该对话流来接收用户消息。​

6.

找到微信订阅号发布渠道，单击配置。​

7.

在 AppID 输入框内，填写微信订阅号的开发者 ID，并单击保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27546%27%20height=%27408%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ2IiBoZWlnaHQ9IjQwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

跳转到公众平台账号授权页面，使用公众平台绑定的管理员个人微信号扫描二维码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27604%27%20height=%27280%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA0IiBoZWlnaHQ9IjI4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

9.

在微信移动端，根据页面提示选择订阅号并确认授权。​

  * 授权成功的页面提示如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27213%27%20height=%27381%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEzIiBoZWlnaHQ9IjM4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

10.

返回应用发布页面，选中微信公众号（订阅号）发布平台，并设置发布记录后，单击页面右上角的发布。​

  * 成功发布后，你可以前往微信订阅号与应用对话。​

上一篇

发布到微信服务号

下一篇

发布到商店