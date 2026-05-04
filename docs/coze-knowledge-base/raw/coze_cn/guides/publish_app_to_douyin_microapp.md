---
source_url: https://docs.coze.cn/guides/publish_app_to_douyin_microapp
title: '发布到抖音小程序 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:46Z
---

# 发布到抖音小程序 - 文档 - 扣子

发布到抖音小程序

将低代码应用发布到抖音小程序后，应用将作为独立的抖音小程序，在抖音和抖音极速版等抖音系 App 端提供服务。 ​

注意

微信小程序和抖音小程序代码下载模式已于2025年3月7日正式下线，已通过此模式开发及发布的微信/抖音小程序线上运行不受影响。发布应用或智能体到微信小程序和抖音小程序时，默认使用托管模式一键发布。​

​

扣子应用支持托管模式发布到抖音小程序，扣子应用代码打包完成后，扣子编程会将其直接部署到抖音开放平台的指定小程序项目中。你可直接提交审核并发布抖音小程序。该方式可以让你更加便捷高效地将小程序快速发布上线。​

限制说明​

​

限制​| 说明​  
---|---  
抖音小程序​| 

  * 一个扣子应用只能发布到一个抖音小程序。 ​

  * 发布应用并经由抖音审核通过后，应用将直接发布到线上。如果绑定的抖音账号中已有小程序，应用会覆盖账号中原有的小程序。 ​

  
扣子应用​| 发布小程序必须配置移动端 UI，且至少绑定 1 个工作流或对话流。​  
权限​| 扣子应用的发布者必须是扣子应用的所有者，协作者或管理员等角色均不支持发布应用。​  
  
​

前提条件​

​

操作​| 说明​  
---|---  
创建抖音小程序​| 

  * 已经注册了抖音开放平台账号、创建了抖音小程序，并完成了以下操作。详细说明可参考[抖音小程序官方文档-开发准备](<https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/guide/develop-process/prepare>)。 ​

  * 配置主体信息。 ​

  * 填写抖音小程序基本信息（名字、头像、描述等）。 ​

  * 设置抖音小程序服务类目。 ​

  * 以上信息及配置已审核通过。​

  * 已获取抖音小程序 AppID。详细步骤可参考​如何获取抖音小程序的 App ID。​

  
小程序备案​| 

  * 已满足抖音开放平台 AI 工具类目的小程序上线标准，并申请上线通过。​

  * 上线标准：开发者公司主体注册时间满一年，注册资本不低于100万。​

  * 申请方式：[AI 工具定向准入申请表](<https://developer.open-douyin.com/work-order-page/create-single-ticket?templateId=cbd4ad24-69ca-41c5-a79f-5c5818f7defc>)​

  * 审核时效：若符合要求，则在 5 个工作日评估通过。​

  * 已在[抖音开放平台](<https://developer.open-douyin.com/console?type=1>)完成了抖音小程序备案，服务类目为 AI 工具。备案流程可参考[抖音小程序官方文档-备案指引](<https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/settle/ICPFiling/ICPintroduce#d7e5a250>)。​

  
  
​

操作步骤​

以下是将应用发布到抖音小程序的详细步骤： ​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择目标项目，在页面右上角，单击发布。 ​

4.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。 ​

  * 版本描述：可选，说明该版本更新的内容。 ​

5.

在 选择发布平台 > 发布到小程序 选项，找到抖音小程序发布渠道。 ​

6.

选择托管发布，单击配置。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27338%27%20height=%27190%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM4IiBoZWlnaHQ9IjE5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

在 AppID 输入框内，填写抖音小程序的 AppID，并单击保存。 ​

  * 获取步骤可参考​如何获取抖音小程序的 App ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27286%27%20height=%27201%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg2IiBoZWlnaHQ9IjIwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

根据页面提示完成授权。 ​

a.

选择要授权的小程序。 ​

b.

选择必要的权限。 ​

  * 说明

必要权限包括开发管理权限、基本信息设置权限和运营管理权限，否则会绑定失败。 ​

​

9.

根据页面提示完成授权。 ​

  * 成功授权后，发布页面将提示已授权。 ​

10.

在发布页面选择抖音小程序，并单击发布。 ​

  * 发布页面可查看小程序打包、审核及发布的进度，详细说明可参考​查看应用发布状态。​

常见问题​

如何获取抖音小程序的 App ID​

1.

使用抖音开放平台账号登录[抖音开放平台](<https://developer.open-douyin.com/console?type=1>)。 ​

2.

在控制台 > 小程序中找到需要绑定扣子应用的小程序。 ​

3.

单击复制图标，复制小程序的 AppID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27317%27%20height=%27189%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE3IiBoZWlnaHQ9IjE4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

是否支持去除底部的“由扣子提供支持”的水印字样？​

仅扣子企业旗舰版支持去除智能体和应用中的水印。在企业工作空间中开发的应用发布到抖音小程序后，页面底部默认不展示“由扣子提供支持”的字样。​

去水印前的效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27418.43971631205676%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQxOC40Mzk3MTYzMTIwNTY3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

去水印后的效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27418.43971631205676%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQxOC40Mzk3MTYzMTIwNTY3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

为什么会绑定抖音小程序失败？​

以下场景下，绑定抖音小程序时可能会报错绑定失败：​

  * 抖音小程序未配置主体信息、名字头像等基本信息、服务类目信息。​

  * 抖音小程序未完成小程序备案，例如未申请备案，或备案审批中。​

  * 在智能体的发布页面配置抖音小程序时，填写了错误的 AppID，或未开启必要的权限（开发管理权限、基本信息设置权限和运营管理权限）。​

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

​

上一篇

发布为 Chat SDK

下一篇

发布到微信小程序