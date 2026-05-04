---
source_url: https://docs.coze.cn/guides/publish_app_to_wechat_mini_program
title: '发布到微信小程序 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:49Z
---

# 发布到微信小程序 - 文档 - 扣子

发布到微信小程序

将低代码应用发布到微信小程序后，应用将作为独立的微信小程序，在微信 App 端提供服务。​

注意

微信小程序和抖音小程序代码下载模式已于2025年3月7日正式下线，已通过此模式开发及发布的微信/抖音小程序线上运行不受影响。当前发布应用或智能体到微信小程序和抖音小程序时，默认使用托管模式一键发布。​

​

说明

现已支持个人主体发布微信小程序，欢迎体验！​

​

扣子应用支持托管发布到微信小程序，扣子应用代码打包完成后，扣子编程会将其直接部署到微信开放平台的指定小程序项目中。你可直接提交审核并发布微信小程序。该方式可以让你更加便捷高效地将小程序快速发布上线。​

限制说明​

​

限制​| 说明​  
---|---  
微信小程序​| 

  * 一个扣子应用只能发布到一个微信小程序。 ​

  * 发布应用并经由微信审核通过后，应用将直接发布到线上。如果绑定的微信账号中已有小程序，应用会覆盖账号中原有的小程序。​

  
扣子应用​| 发布小程序必须配置移动端 UI，且至少绑定 1 个工作流或对话流。​  
权限​| 扣子应用的发布者必须是扣子应用的所有者，协作者或管理员等角色均不支持发布应用。​  
  
​

说明

应用发布微信小程序时不支持语音输入、语音输出、触发器和快捷指令，各发布渠道的能力差异请参见​发布渠道能力差异。​

​

前提条件​

  * 已经注册了微信小程序号，并完成了以下操作。详细说明可参考[微信开放平台文档](<https://developers.weixin.qq.com/miniprogram/introduction/>)。 ​

  * 登记主体信息。 ​

  * 填写微信小程序基本信息（名字、头像、描述等）。 ​

  * 设置微信小程序服务类目。​

  * 如果微信小程序账号是企业主体，可以选择 AI 问答类目以提升微信审核通过率。如果页面提示需要提供《互联网信息服务算法备案》和合作协议，可以在火山引擎控制台的[合同管理](<https://console.volcengine.com/finance/contract/>)页面下载订单合同作为合作协议，算法备案材料可参考[客户应用上架指南-算法备案资质申请流程](<https://www.volcengine.com/docs/82379/1326340>)。​

  * 已完成了微信小程序备案，备案流程可参考[微信开放平台文档](<https://developers.weixin.qq.com/miniprogram/product/record/record_guidelines.html>)。 ​

操作步骤​

以下是将应用发布到微信小程序的详细步骤： ​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。 ​

3.

在项目开发页面，选择目标应用，在应用编排页面右上角，单击发布。 ​

4.

在发布页面填写版本信息：​

  * 版本号：必填，必须是一个应用从未设置过的新版本号。 ​

  * 版本描述：可选，说明该版本更新的内容。 ​

5.

在 选择发布平台区域，找到微信小程序发布渠道。单击配置。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27402.3121387283237%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMi4zMTIxMzg3MjgzMjM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

6.

在 AppID 输入框内，填写微信小程序 AppID，并单击保存。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27356.4189189189189%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM1Ni40MTg5MTg5MTg5MTg5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

7.

根据页面提示完成授权。 ​

  * 页面跳转到公众平台账号授权页面，使用公众平台绑定的管理员个人微信号扫描二维码。 在微信移动端，根据页面提示选择小程序号并确认授权。​

  * ​

授权界面 ​| 授权成功的页面提示 ​  
---|---  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27842%27%20height=%271094%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODQyIiBoZWlnaHQ9IjEwOTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271172%27%20height=%272534%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE3MiIgaGVpZ2h0PSIyNTM0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

8.

返回发布页面，选中微信小程序发布平台，并设置版本号后，单击页面右上角的发布。 ​

  * 发布页面可查看小程序打包、审核及发布的进度，详细说明可参考​查看应用发布状态。成功发布后，你可以前往微信小程序号使用应用。 ​

常见问题​

如何获取微信小程序的 AppID​

1.

使用微信小程序账号登录 [微信公众平台](<https://mp.weixin.qq.com/>)。 ​

2.

在设置 > 账号信息页面获取AppID(小程序ID)。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27397.8798586572438%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjM5Ny44Nzk4NTg2NTcyNDM4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

如何在扣子应用中跳转到其他小程序？​

如果需要在扣子应用中实现跳转到其他小程序，你可以在页面 UI 中添加目标小程序的二维码，用户扫描该二维码后，即可跳转到对应的小程序。​

发布后为什么调用工作流失败？​

工作流的个别节点在不同发布渠道的支持情况存在差异。如果某个节点不支持当前的发布渠道，可能会导致发布失败。检查应用的工作流，确认其中的节点是否支持目标发布渠道，各发布渠道的能力差异请参见​发布渠道能力差异。​

是否支持去除底部的“由扣子提供支持”的水印字样？​

仅扣子企业旗舰版支持去除智能体和应用中的水印。在企业工作空间中开发的应用发布到微信小程序后，页面底部默认不展示“由扣子提供支持”的字样。​

去水印前的效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27418.43971631205676%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQxOC40Mzk3MTYzMTIwNTY3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

去水印后的效果图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27418.43971631205676%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQxOC40Mzk3MTYzMTIwNTY3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

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

​

上一篇

发布到抖音小程序

下一篇

发布到飞书