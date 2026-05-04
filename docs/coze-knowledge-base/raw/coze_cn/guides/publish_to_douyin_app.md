---
source_url: https://docs.coze.cn/guides/publish_to_douyin_app
title: '发布到抖音小程序 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:15Z
---

# 发布到抖音小程序 - 文档 - 扣子

发布到抖音小程序

将低代码智能体发布到抖音小程序后，智能体将作为独立的抖音小程序，在抖音和抖音极速版等抖音系 App 端提供服务。 ​

使用限制​

  * 一个智能体只能发布到一个抖音小程序。 ​

  * 不支持主体类型为个人的抖音小程序号。 ​

  * 发布智能体并经由抖音审核通过后，智能体将直接发布到线上。如果绑定的抖音账号中已有小程序，智能体会覆盖账号中原有的小程序。 ​

  * 首次发布智能体到抖音小程序时，需要由智能体的所有者在发布页面授权。​

  * 智能体发布抖音小程序后，不支持语音输入、语音输出 TTS 和语音通话功能。​

前提条件​

  * 已经注册了抖音开放平台账号、创建了抖音小程序，并完成了以下操作。详细说明可参考[抖音小程序官方文档-开发准备](<https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/guide/develop-process/prepare>)。​

  * 配置主体信息。​

  * 填写抖音小程序基本信息（名字、头像、描述等）。 ​

  * 设置抖音小程序服务类目。 ​

  * 以上信息及配置已审核通过。​

  * 已在[抖音开放平台](<https://developer.open-douyin.com/console?type=1>)完成了抖音小程序备案，备案流程可参考[抖音小程序官方文档-备案指引](<https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/settle/ICPFiling/ICPintroduce#d7e5a250>)。 ​

  * 已在[扣子编程](<https://code.coze.cn/home>)完成了智能体的创建与调试。 ​

步骤一：获取抖音小程序的 AppID​

1.

使用抖音开放平台账号登录[抖音开放平台](<https://developer.open-douyin.com/console?type=1>)。 ​

2.

在控制台 > 小程序中找到需要绑定扣子智能体的小程序。​

3.

单击复制图标，复制小程序的 AppID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27300%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a82bce22b0ad4c84b5944e2d54d74755~tplv-goo7wpa0wc-quality:q75.image)​

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

在发布页面，找到抖音小程序发布渠道，单击配置。 ​

5.

在 AppID 输入框内，填写​步骤一：获取抖音小程序的 AppID中获取的 AppID，并单击保存。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27471%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcxIiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

根据页面提示完成授权。​

a.

选择要授权的小程序。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27238%27%20height=%27278%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM4IiBoZWlnaHQ9IjI3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

选择必要的权限。​

  * 说明

必要权限包括开发管理权限、基本信息设置权限和运营管理权限，否则会绑定失败。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27197%27%20height=%27231%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk3IiBoZWlnaHQ9IjIzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

根据页面提示完成授权。​

  * 成功授权后，发布页面将提示已授权。​

7.

在发布页面选择抖音小程序，并单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271610%27%20height=%27644.9847094801223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYxMCIgaGVpZ2h0PSI2NDQuOTg0NzA5NDgwMTIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

等待审核通过。​

  * 成功提交发布后，抖音开放平台会对绑定智能体的抖音小程序进行审核，预计 7 个工作日内审核完成。审核通过后，抖音小程序会自动发布上线，你可以在抖音 App 内搜索小程序并使用。​

下架智能体​

如果不再需要在该渠道中展示智能体，你可以选择将其下架。下架的操作步骤请参见​下架智能体。​

常见问题​

发布到抖音小程序需要审核吗？​

首次发布到抖音小程序时，页面将提示审核中，表示小程序正在经由抖音审核中。审核通常在在 1-7 个工作日内完成，你可以通过发布历史查看审核结果，或在发布页面查看发布结果。​

为什么不能使用主体类型为个人的抖音小程序号？​

抖音开放平台暂不支持个人主体申请抖音小程序。详细信息可查看[抖音开放平台官方文档](<https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/settle/authentication/Subject>)。​

为什么会绑定抖音小程序失败？​

以下场景下，绑定抖音小程序时可能会报错绑定失败：​

  * 抖音小程序未配置主体信息、名字头像等基本信息、服务类目信息。​

  * 抖音小程序未完成小程序备案，例如未申请备案，或备案审批中。​

  * 在智能体的发布页面配置抖音小程序时，填写了错误的 AppID，或未开启必要的权限（开发管理权限、基本信息设置权限和运营管理权限）。​

是否支持去除底部的“由扣子提供支持”的水印字样？​

仅扣子企业旗舰版支持去除智能体和应用中的水印。在企业工作空间中开发的智能体发布到抖音小程序后，页面底部默认不展示“由扣子提供支持”的字样。​

去水印前的效果图​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27250%27%20height=%27527.6580459770115%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjUyNy42NTgwNDU5NzcwMTE1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

去水印后的效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27250%27%20height=%27527.1867612293144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjUyNy4xODY3NjEyMjkzMTQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

如何获取第三方算法服务的备案信息？​

你可以在火山引擎控制台的[合同管理](<https://console.volcengine.com/finance/contract/>)页面，获取发布抖音小程序所需的算法备案相关材料，包括加盖鲜章的备案合同，在备案合同中会提供算法备案号。详细步骤可参考[客户应用上架指南-算法备案资质申请流程](<https://www.volcengine.com/docs/82379/1326340>)。​

申请备案合同需满足以下条件：​

  * 账号存在方舟大模型或火山引擎豆包系列相关付费订单。​

  * 账号存在对应商品的预付费/部分预付实例，或运行中的后付费实例，且近 6 个月的调用量大于 0。​

  * 后付费账单在次月第 4 个自然日后可申请合同。​

说明

  * 若使用 DeepSeek 等第三方模型需自行申请算法备案，具体可参考[大模型备案说明(含算法备案及人工智能备案)](<https://www.volcengine.com/docs/82379/1471389>)。​

  * 若使用火山引擎豆包系列模型，可通过申请豆包合作协议及备案证明获取材料，详细步骤可参考[客户应用上架指南-算法备案资质申请流程](<https://www.volcengine.com/docs/82379/1326340>)。​

​

为什么抖音企业号发布渠道无法使用了？​

由于抖音开发平台的企业号策略调整，扣子抖音企业号发布渠道已于2025年3月13日正式下线。​

​

上一篇

发布到飞书

下一篇

发布到微信小程序