---
source_url: https://docs.coze.cn/guides/wechat_subscription
title: '发布到微信订阅号 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:26Z
---

# 发布到微信订阅号 - 文档 - 扣子

发布到微信订阅号

你可以将搭建的低代码智能体发布到微信公众号（订阅号）中。发布后，订阅号就可以使用智能体回复用户消息，助力运营。​

使用限制​

  * 一个智能体只能发布到一个微信订阅号。​

  * 支持在回复订阅号时上传图片，但图片大小不能超过 10 MB。​

  * 每次回复消息时，只能回复一张图片。​

  * 如果模型返回的是图文混排的内容，则直接返回完整的Markdown内容。​

  * 如果模型生成了多张Markdown语法的图片内容，最终会解析返回第一张图片，多余图片会被丢弃。​

前提条件​

  * 已经创建了微信订阅号。​

  * 已搭建一个低代码智能体。具体操作，请参见​搭建一个低代码智能体。​

步骤一：获取微信订阅号的开发者 ID​

1.

访问[微信开发者平台](<https://developers.weixin.qq.com/platform>)并登录你的服务号。​

2.

在我的业务 > 公众号页面，获取开发者ID(AppID)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27306.94444444444446%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/83d9a40ca3e84618ad20caa3fc11149e~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：在扣子中配置并发布智能体​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。​

3.

在项目开发页面，选择低代码智能体。在页面右上角，单击发布。​

​

4.

在发布页面，找到微信公众号（订阅号）发布渠道，单击配置。​

5.

在 AppID 输入框内，填写微信订阅号的开发者 ID，并单击保存。​

6.

跳转到公众平台账号授权页面，使用公众平台绑定的管理员个人微信号扫描二维码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27604%27%20height=%27280%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA0IiBoZWlnaHQ9IjI4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

在微信移动端，根据页面提示选择订阅号并确认授权。​

  * 授权成功的页面提示如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27213%27%20height=%27381%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEzIiBoZWlnaHQ9IjM4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

返回智能体发布页面，选中微信公众号（订阅号）发布平台，并设置发布记录后，单击页面右上角的发布。​

  * 成功发布后，你可以前往微信订阅号与智能体对话。​

下架智能体​

如果不再需要在该渠道中展示智能体，你可以选择将其下架。下架的操作步骤请参见​下架智能体。​

常见问题​

给订阅号发消息后，为什么收到了思考中请回复“继续” 的回复？​

当发送消息到回复用户这个过程时间超过15秒时，就会收到思考中请回复“继续” 的回复。为了解决该问题，你可以：​

1.

回复“继续”，让智能体继续回复用户。​

2.

在智能体编排页面的人设与回复逻辑区域，修改智能体的提示词，控制智能体的回复长度，尽量保证在 15 秒内完成回复。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27473%27%20height=%27379%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDczIiBoZWlnaHQ9IjM3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 以下是一个提示词示例。​

  * ​

Plain Text

复制

##角色​

你是一个极简主义者，喜欢用最简单的方式回答问题。​

​

##技能​

\- 使用极简的方式回答问题。​

\- 当用户提出复杂问题时,将其简化并提供易于理解的答案。​

\- 只回答与问题相关的内容,避免冗长和不必要的信息。​

​

##限制​

\- 只回答与问题相关的内容，避免冗长和不必要的信息。​

\- 回答应尽可能简洁明了。​

​

已经完成了渠道配置，但配置状态为未授权，如何解决？​

  * 问题描述​

  * 如下图所示，虽然完成了配置，但渠道的状态仍是未授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27188.82681564245812%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE4OC44MjY4MTU2NDI0NTgxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 当在配置渠道信息点击保存按钮后出现报错信息，或者在授权回调时出现报错信息时就会出现未授权的问题。​

  * 解决方案​

  * 可尝试重新进行渠道配置：​

a.

单击目标渠道的配置选项。​

b.

解绑已绑定的账号，然后重新配置渠道信息。​

在扫码授权时，出现错误提示，如何解决？​

  * 错误提示： 缺少必须权限​

  * 解决方案：请确认在扫码时是否漏勾选了部分权限，重新扫码授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27140.78212290502793%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE0MC43ODIxMjI5MDUwMjc5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 错误提示：请确认并选择正确的微信公众号类型​

  * 解决方案：请确认是否在订阅号渠道绑定了服务号，或者在服务号渠道绑定了订阅号。​

发布到微信订阅号需要审核吗？​

首次发布到微信订阅号时，页面将提示审核中，表示微信订阅号正在经由微信审核中。审核通常在在 1-7 个工作日内完成，你可以通过发布历史查看审核结果，或在发布页面查看发布结果。​

如何让微信中直接显示图片？​

由于微信平台本身的限制。当一条消息中同时包含文字和图片时，系统会自动将图片以 URL 形式发送，而不是直接显示图片。​

如果需要在微信中直接显示图片，而不是图片链接，你需要确保智能体在输出图片时不输出任何其他文字内容。​

智能体发布微信订阅号后，是否可以暂停使用？​

智能体发布微信订阅号后，可以暂停使用该智能体，具体操作如下：​

选择对应智能体，单击右上角的发布，在发布页面的微信订阅号右侧执行解绑操作。​

​

上一篇

发布到微信服务号

下一篇

发布到掘金