---
source_url: https://docs.coze.cn/guides/publish_to_wechat_app
title: '发布到微信小程序 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:18Z
---

# 发布到微信小程序 - 文档 - 扣子

发布到微信小程序

将低代码智能体发布到微信小程序后，智能体将作为独立的微信小程序，在微信端提供服务。​

使用限制 ​

  * 一个智能体只能发布到一个微信小程序。 ​

  * 不支持主体类型为个人的微信小程序号。​

  * 发布智能体并经由微信审核通过后，智能体将直接发布到线上。如果绑定的微信账号中已有小程序，智能体会覆盖账号中原有的小程序。​

  * 智能体发布微信小程序后，不支持语音输入、语音输出 TTS 和语音通话功能。​

前提条件 ​

  * 已经注册了微信小程序号，并完成了以下操作。详细说明可参考[微信开放平台文档](<https://developers.weixin.qq.com/miniprogram/introduction/>)。​

  * 登记主体信息，主体类型为个人以外的其他类型。​

  * 填写微信小程序基本信息（名字、头像、描述等）。​

  * 设置微信小程序服务类目。​

  * 设置类目时，如果页面提示需要提供《互联网信息服务算法备案》和合作协议，可以在火山引擎控制台的[合同管理](<https://console.volcengine.com/finance/contract/>)页面下载订单合同作为合作协议，算法备案材料可参考[客户应用上架指南-算法备案资质申请流程](<https://www.volcengine.com/docs/82379/1326340>)。​

  * 已完成了微信小程序备案，备案流程可参考[微信开放平台文档](<https://developers.weixin.qq.com/miniprogram/product/record/record_guidelines.html>)。​

  * 已经完成了智能体的创建与调试。 ​

步骤一：获取微信小程序号的开发者 ID ​

1.

使用微信小程序账号登录 [小程序后台](<https://mp.weixin.qq.com/>)。 ​

2.

在设置 > 账号信息页面获取AppID(小程序ID)。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27525%27%20height=%27261%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ceca7e8a372a4e359e3e394726155a08~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：在扣子中配置并发布智能体​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。​

3.

在项目开发页面，选择低代码智能体。在页面右上角，单击发布。​

​

3.

在发布页面，找到微信小程序发布渠道，单击配置。 ​

4.

在 AppID 输入框内，填写微信小程序号的开发者 ID，并单击保存。 ​

5.

根据页面提示完成授权。​

  * 页面跳转到公众平台账号授权页面，使用公众平台绑定的管理员个人微信号扫描二维码。 在微信移动端，根据页面提示选择小程序号并确认授权。​

  * ​

授权界面​| 授权成功的页面提示​  
---|---  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27213%27%20height=%27277%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEzIiBoZWlnaHQ9IjI3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27161%27%20height=%27348%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYxIiBoZWlnaHQ9IjM0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

9.

返回智能体发布页面，选中微信小程序发布平台，并设置发布记录后，单击页面右上角的发布。 ​

  * 成功发布后，你可以前往微信小程序号与智能体对话。 ​

下架智能体​

如果不再需要在该渠道中展示智能体，你可以选择将其下架。下架的操作步骤请参见​下架智能体。​

常见问题 ​

发布到微信小程序需要审核吗？​

首次发布到微信小程序时，页面将提示审核中，表示小程序正在经由微信审核中。审核通常在在 1-7 个工作日内完成，你可以通过发布历史查看审核结果，或在发布页面查看发布结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27598%27%20height=%27137%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTk4IiBoZWlnaHQ9IjEzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为什么不能使用主体类型为个人的微信小程序号？​

扣子目前通过 web-view 实现智能体的微信小程序接入，但 web-view 暂不支持个人类型的微信小程序。​

如何在扣子智能体中跳转到其他小程序？​

如果需要在扣子智能体中实现跳转到其他小程序，你可以在页面中添加目标小程序的二维码，用户扫描该二维码后，即可跳转到对应的小程序。​

发布后为什么调用工作流失败？​

工作流的个别节点在不同发布渠道的支持情况存在差异。如果某个节点不支持当前的发布渠道，可能会导致发布失败。检查智能体的工作流，确认其中的节点是否支持目标发布渠道，各发布渠道的能力差异请参见​发布渠道能力差异。​

是否支持去除底部的“由扣子提供支持”的水印字样？​

仅扣子企业旗舰版支持去除智能体和应用中的水印。在企业工作空间中开发的智能体发布到微信小程序后，页面底部默认不展示“由扣子提供支持”的字样。​

去水印前的效果图​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27250%27%20height=%27527.6580459770115%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjUyNy42NTgwNDU5NzcwMTE1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

去水印后的效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27250%27%20height=%27527.1867612293144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjUyNy4xODY3NjEyMjkzMTQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

如何让微信中直接显示图片？​

由于微信平台本身的限制。当一条消息中同时包含文字和图片时，系统会自动将图片以 URL 形式发送，而不是直接显示图片。​

如果需要在微信中直接显示图片，而不是图片链接，你需要确保智能体在输出图片时不输出任何其他文字内容。​

如何获取加盖鲜章的备案合同？​

你可以在火山引擎控制台的[合同管理](<https://console.volcengine.com/finance/contract/>)页面，获取微信小程序上架的算法备案相关材料，包括加盖鲜章的备案合同，在备案合同中会提供算法备案号。详细步骤可参考[客户应用上架指南-算法备案资质申请流程](<https://www.volcengine.com/docs/82379/1326340>)。​

申请备案合同需满足以下条件：​

  * 账号存在方舟大模型或火山引擎豆包系列相关付费订单。​

  * 账号存在对应商品的预付费/部分预付实例，或运行中的后付费实例，且近 6 个月的调用量大于 0。​

  * 后付费账单在次月第 4 个自然日后可申请合同。​

说明

  * 若使用 DeepSeek 等第三方模型需自行申请算法备案，具体可参考[大模型备案说明(含算法备案及人工智能备案)](<https://www.volcengine.com/docs/82379/1471389>)。​

  * 若使用火山引擎豆包系列模型，可通过申请豆包合作协议及备案证明获取材料，详细步骤可参考[客户应用上架指南-算法备案资质申请流程](<https://www.volcengine.com/docs/82379/1326340>)。​

​

发布智能体到微信小程序提示审核不通过，如何解决？ ​

如果你的智能体在发布到微信小程序时被提示审核不通过，可以参考以下建议进行解决：​

  * 检查类目设置：确保提交的小程序类目完全符合实际业务场景，避免选择与业务无关或模糊的类目。​

  * 避免敏感词汇：智能体中不能出现 AI、人工智能、大模型等可能引起审核敏感的词汇。建议使用更通用或具体的描述来替代这些词汇。​

  * 重新提交审核：如果智能体被拒绝，你可以复制原智能体内容，创建一个新的智能体，并根据审核反馈进行调整后重新发布。​

如何将生成的智能体嵌入到自有小程序并自定义界面？​

目前，通过代发布微信小程序的智能体不支持界面定制化。建议您通过 API 接入自有页面，以实现界面的完全定制化，包括去除底部标识等。具体操作可参考​发起对话 API。​

智能体发布微信小程序如何解除授权？​

在智能体编排页面右上角单击发布，在微信小程序右侧单击解除授权。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27180.55555555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjE4MC41NTU1NTU1NTU1NTU1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

发布到抖音小程序

下一篇

发布到微信客服