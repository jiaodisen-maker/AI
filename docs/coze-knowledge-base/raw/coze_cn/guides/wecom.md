---
source_url: https://docs.coze.cn/guides/wecom
title: '发布到微信客服 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:21Z
---

# 发布到微信客服 - 文档 - 扣子

发布到微信客服

你可以将搭建的低代码智能体发布到微信客服机器人中，增强微信客服的能力。​

说明

  * 支持在回复微信客服时上传图片，但图片大小不能超过 10 MB。​

  * 确保已经完成了企业认证。​

​

前提条件​

1.

已开通了[微信客服](<https://kf.weixin.qq.com/>)。​

2.

已搭建了智能体。​

步骤一：获取微信客服配置信息​

1.

登录[微信客服](<https://kf.weixin.qq.com/>)平台。​

2.

单击企业信息，然后复制企业 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27470%27%20height=%27194%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d5298c9044534fa887eeadf1a5c2dc77~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

单击开发配置，然后再单击开始使用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27462%27%20height=%27236%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2bccbd00fe9c42158e1fb2f8466ff652~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

单击随机获取按钮分别生成并保存 Token 和 EncodingAESKey。​

  * 注意

复制 Token 和 EncodingAESKey 后，先不要关闭该页面。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27395%27%20height=%27266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk1IiBoZWlnaHQ9IjI2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：在扣子中配置微信客服信息​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。​

3.

在项目开发页面，选择低代码智能体。在页面右上角，单击发布。​

​

5.

找到微信客服渠道，然后单击 配置。​

6.

输入步骤一中复制的企业 ID，然后单击下一步。​

7.

输入步骤一中复制的 Token 和 EncodingAESKey，然后单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27322%27%20height=%27222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIyIiBoZWlnaHQ9IjIyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

复制 webhook 地址。​

  * 注意

复制 webhook 地址后，先不要关闭该配置窗口。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27296%27%20height=%27293%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk2IiBoZWlnaHQ9IjI5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：配置回调地址​

1.

回到步骤一中的开始企业接入页面，输入上一步中复制的 webhook 地址。单击完成。​

  * 说明

    * 确保粘贴回调地址时没有引入空格，空格会导致校验失败。​

    * 未完成企业认证时，回调地址校验失败。​

​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27394%27%20height=%27288%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk0IiBoZWlnaHQ9IjI4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在开发配置页面，复制 secret。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27358%27%20height=%27181%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU4IiBoZWlnaHQ9IjE4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

单击客服账号，复制账号。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27359%27%20height=%27106%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU5IiBoZWlnaHQ9IjEwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：发布智能体​

1.

回到扣子平台的微信客服渠道配置页面，输入复制的 secret 和客服名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27279%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc5IiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

单击保存。​

3.

在发布记录中输入发布信息，然后勾选微信客服渠道，再单击发布。​

4.

发布完成后，单击立即对话登录微信客服，体验智能体效果。​

下架智能体​

如果不再需要在该渠道中展示智能体，你可以选择将其下架。下架的操作步骤请参见​下架智能体。​

常见问题​

收不到机器人回复消息​

可尝试通过以下方法解决：​

  * 查看微信客服的启用状态​

a.

登录[企业微信管理后台](<https://work.weixin.qq.com/wework_admin/frame#apps>)，在应用管理页面，点击微信客服。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27399%27%20height=%27124%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk5IiBoZWlnaHQ9IjEyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

确保没有启用微信客服功能。如果已经开启了微信客服功能，需要关闭。​

  * 说明

关闭后，该应用在工作台入口将被隐藏，员工不可使用。请谨慎评估。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%2799%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYzIiBoZWlnaHQ9Ijk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 检查近期是否有登录企业微信应用。​

  * 确保企业至少有一个成员通过手机号验证/微信授权登录过企业微信应用。​

页面提示回调地址校验失败​

以下原因可能导致回调地址校验失败：​

  * 未完成企业认证：​

  * 企业认证中、未发起企业认证流程等状态下，配置回调地址时会触发页面提示“回调地址校验失败”。你也可以先发布到微信订阅号，待企业认证通过后再发布到微信客服中使用。发布到微信订阅号的方式可参考​发布到微信订阅号。​

  * 回调地址中存在空格：​

  * 请检查回调地址是否正确、是否存在多余的空格等不可见字符。​

如何让微信中直接显示图片？​

由于微信平台本身的限制。当一条消息中同时包含文字和图片时，系统会自动将图片以 URL 形式发送，而不是直接显示图片。​

如果需要在微信中直接显示图片，而不是图片链接，你需要确保智能体在输出图片时不输出任何其他文字内容。​

如何下架已发布到微信客服的智能体？​

如需下架发布到微信客服的智能体，需在微信客服后台完成下架操作，直接在扣子侧删除智能体并不能完成下架操作。请前往[企业微信管理后台](<https://work.weixin.qq.com/wework_admin/frame#apps>)手动解除智能体的接入状态。​

发布微信客服提示审核不通过怎么办？​

将智能体发布到微信公众号或微信客服等渠道时，需要经过微信平台的审核。如果审核未通过，请您耐心等待审核结果。根据​扣子平台内容发布标准和规范检查并修改智能体配置，确保内容符合微信平台的要求，然后重新提交审核。​

如果确认内容没有问题，但审核仍未通过，你可以在微信客服平台单击回复消息下方的转人工按钮，联系微信客服团队，并提供以下信息以便协助排查问题：​

  * 智能体编辑页面的 URL 地址。​

  * 微信客服平台上的企业 ID（以 ww 开头的字符）。​

​

上一篇

发布到微信小程序

下一篇

发布到微信服务号