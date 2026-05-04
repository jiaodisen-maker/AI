---
source_url: https://docs.coze.cn/guides/configure_custom_domain
title: '配置自定义域名 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:12Z
---

# 配置自定义域名 - 文档 - 扣子

配置自定义域名

在扣子编程部署网页应用时支持使用扣子编程默认域名或自定义域名。若希望项目有更强的品牌辨识度，你可以将项目部署到自定义域名，以便打造独特的品牌形象，提升用户对品牌的认知度和信任感。本文介绍配置自定义域名的详细步骤。​

域名概述​

扣子编程会为每个部署项目自动分配以 .coze.site 为后缀的默认域名。你也可以将项目绑定至自定义域名，以便打造专属品牌访问地址，使网站地址更容易被用户记住，还能提升品牌知名度。​

你可以从火山引擎购买域名，或使用从第三方服务商处购买的域名。使用自定义域名时，你需要在火山引擎为自定义域名进行备案，并配置 SSL 证书。​

默认域名和自定义域名使用方式的区别如下：​

​

功能​| 扣子默认域名​| 自定义域名​  
---|---|---  
备案​​| 扣子编程已统一备案，你无需单独备案。​​| 需要在火山引擎备案域名。​火山引擎域名或第三方域名均需要在火山引擎完成域名备案。​  
SSL 证书​| 扣子编程已自动配置长期有效的 SSL 证书，无需手工配置。​| 需要手工配置证书。​  
  
​

费用说明​

  * 购买火山引擎域名时，火山引擎域名服务产品会收取域名服务费用，这些费用自动从你的火山引擎余额中扣款，不支持用扣子积分抵扣。具体收费标准可参考[域名服务计费文档](<https://www.volcengine.com/docs/6568/103928?lang=zh>)。​

  * 购买火山引擎的证书时，火山引擎证书中心会收取 SSL 证书费用，这些费用自动从你的火山引擎余额中扣款，不支持用扣子积分抵扣。具体收费标准可参考[SSL证书计费说明](<https://www.volcengine.com/docs/6638/117994?lang=zh>)。​

使用限制​

配置自定义域名时，存在项目类型、免费证书额度等限制。详情请参见​配额与限制。​

操作步骤​

步骤一：购买域名​

在配置自定义域名之前，你需要先购买一个域名。本文以购买火山引擎域名为例，如果你已经从其他服务商处购买了域名，可以跳过本步骤。​

使用限制​

仅火山主账号或具备 DomainFullAccess 权限的 IAM 用户，才支持购买火山引擎域名。​

操作步骤​

1.

打开[扣子编程建站域名特惠](<https://www.volcengine.com/activity/domain-coze>)页面。注册域名的详细说明请参见[注册域名](<https://www.volcengine.com/docs/6568/81255?lang=zh>)。​

2.

单击相应的域名类型卡片，在域名搜索框中，输入你想注册的域名，单击搜索按钮。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27366.3194444444444%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM2Ni4zMTk0NDQ0NDQ0NDQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

在对应域名右侧单击立即购买。根据界面提示完成支付，域名就注册成功了。​

  * 注册域名后，域名会自动进入实名认证流程。打开[域名列表](<https://console.volcengine.com/domain-service/domain>)页面，你可以查看实名认证的状态。​

步骤二：备案域名​

根据国家相关法规，所有在中国内地提供服务的网站都必须进行 ICP 备案。由于你的网页应用由扣子编程统一部署在火山引擎的服务器上，因此需要在火山引擎备案系统对域名进行备案。​

说明

  * 已在其他服务商备案过的域名，仍需在火山引擎重新备案。​

  * 备案审核通常需要 1 到 20 个工作日。建议你提前规划，尽早提交备案申请，以免影响应用上线计划。​

​

1.

登录[火山引擎备案控制台](<https://console.volcengine.com/beian>)，单击开始备案。​

2.

根据页面提示，填写主办者信息和备案信息，等待审核通过。不同场景的备案流程稍有差异，具体如下表所示。​

  * ​

场景​| 备案流程​  
---|---  
首次购买域名，且没有任何备案历史。​| [首次备案流程](<https://www.volcengine.com/docs/6428/68739?lang=zh>)​  
域名已在其他服务商备案，现需指向火山引擎服务器。​| [接入备案流程](<https://www.volcengine.com/docs/6428/68740>)​  
你已有其他域名在火山引擎备案，需为新域名备案。​| [新增服务流程](<https://www.volcengine.com/docs/6428/68741>)​  
  
​

步骤三：购买或上传 SSL 证书​

为确保数据传输的安全，你需要为你的域名准备 SSL证书，以免访问网页时被拦截。扣子编程支持三种证书，具体说明如下。​

​

证书类型​| 注意事项​| 操作说明​  
---|---|---  
免费证书​| 有效期三个月且有额度限制。​| 无需提前准备，参考​步骤四：在扣子侧配置自定义域名直接生成即可。​  
火山引擎证书​|  有效期 1 年。​| 需要提前在火山引擎控制台购买，详细操作说明请参见 [SSL 证书快速入门](<https://www.volcengine.com/docs/6638/118049?lang=zh>)。你需要完成下图中红框中的步骤。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27118.05555555555556%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjExOC4wNTU1NTU1NTU1NTU1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
其他来源的证书​| \​| 在火山引擎证书中心控制台上传证书，具体请参考[上传证书](<https://www.volcengine.com/docs/6638/118039?lang=zh>)。​  
  
​

步骤四：在扣子侧配置自定义域名​

完成域名准备和备案后，就可以在你的 AI 编程开发的项目中绑定自定义域名。​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的项目，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27212.96296296296296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIxMi45NjI5NjI5NjI5NjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在 AI 编程开发界面的右上角单击部署。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27376.97929354445796%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM3Ni45NzkyOTM1NDQ0NTc5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在部署页面的部署域名右侧单击添加域名。​

4.

在域名页面单击添加域名，在添加域名对话框中，输入该项目使用的具体域名。​

  * 域名后缀为步骤一中准备好的域名。例如，备案的域名为二级域名example.com，此处可以填写三级域名web.example.com。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27157.40740740740742%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjE1Ny40MDc0MDc0MDc0MDc0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击保存域名，下一步。​

  * 扣子编程会为你生成一条解析记录。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27330.8056872037915%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMzMC44MDU2ODcyMDM3OTE1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

6.

复制解析记录中的记录值，并在 DNS 中添加对应的解析记录，DNS 侧的配置方法请参考​在 DNS 侧为域名配置解析记录。​

7.

配置 SSL 证书。​

  * 为确保数据传输的安全，你需要为你的域名配置 SSL证书。扣子编程提供两种证书配置方式。​

  * ​

证书类型​| 说明​| 配置方式​  
---|---|---  
免费证书​| 适用于需要为自定义域名快速、免费启用 HTTPS 的场景，例如个人项目或开发测试环境。​
    * 有效期与额度：[免费证书](<https://www.volcengine.com/docs/6638/139126?lang=zh>)遵循火山引擎的统一策略，有效期为 3 个月，每个主账号在一个自然年内拥有 20 次免费证书的生成额度。​
    * 额度可用：为避免证书过期导致服务中断，强烈建议勾选自动轮转。只要年度额度有剩余，系统将在证书到期前自动为你生成并替换新证书。​
    * 额度用尽：当年度免费证书额度用尽时，自动轮转功能将失效。​
    * 过期通知：扣子会在证书到期前 3 个工作日向你发送过期提醒。收到通知后，你需要及时切换为付费的火山引擎证书，或等待下一自然年额度重置后，重新生成免费证书。​
| 单击生成免费证书。扣子编程将自动生成免费证书并完成证书安装，整体过程预计需要 3~5 分钟。同时，建议你勾选自动轮转。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271085%27%20height=%271179.1324200913243%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4NSIgaGVpZ2h0PSIxMTc5LjEzMjQyMDA5MTMyNDMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
火山引擎证书​| 适用于对稳定性要求较高的生产环境，或当免费证书额度用尽后，需要为自定义域名提供长期、可靠的 HTTPS 服务。​
    * 有效期：通常为 1 年。​
    * 购买：根据页面提示先购买火山引擎证书，详细操作说明请参见 [SSL 证书快速入门](<https://www.volcengine.com/docs/6638/118049?lang=zh>)。​
    * 续费：在证书到期前 30天 内执行续费，否则证书将自动失效，详细操作说明请参见[续费 SSL 证书](<https://www.volcengine.com/docs/6638/125688>)。​
| 单击选择并添加，在下拉列表中选择你已购买的火山引擎证书，扣子编程将自动完成证书安装。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271079%27%20height=%271177.538812785388%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA3OSIgaGVpZ2h0PSIxMTc3LjUzODgxMjc4NTM4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

相关操作​

在 DNS 侧为域名配置解析记录​

在你的域名服务商的 DNS 控制台，将扣子编程提供的解析记录添加到对应域名的解析记录中，从而让域名指向扣子编程为你分配的应用服务器地址。​

以下是某域名服务商 DNS 控制台的配置示例，在公网权威解析页面，添加对应的域名，并为对应的域名添加一条解析记录。其中，解析记录中的记录值为​步骤四：在扣子侧配置自定义域名中复制的解析记录的值。火山引擎 DNS 的配置方法请参考[添加解析记录](<https://www.volcengine.com/docs/6758/109959?lang=zh>)。​

扣子编程侧​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27330.8056872037915%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMzMC44MDU2ODcyMDM3OTE1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

DNS 侧​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27263.0331753554502%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI2My4wMzMxNzUzNTU0NTAyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

说明

扣子编程侧解析记录的状态变为已验证，说明 DNS 侧已正确配置解析记录。​

​

部署项目​

完成自定义域名配置后，单击右上角的部署，即可部署该项目，具体步骤可参考​部署网页应用。​

查看域名配置​

你可以查看自定义域名的配置，包括完整的域名、域名解析记录、证书的有效期等信息，你也可以重新添加证书。​

说明

仅自定义域名支持查看域名配置，扣子编程默认域名不支持查看域名配置。​

​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的项目，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27212.96296296296296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIxMi45NjI5NjI5NjI5NjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在 AI 编程开发界面，在右侧单击➕打开新的标签页，在弹出的标签页中选择部署。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27345.0867052023121%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM0NS4wODY3MDUyMDIzMTIxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

在部署页面的域名页签中，在目标域名右侧单击查看配置。你可以执行以下操作：​

  * 查看完整域名：你可以复制此地址，用于分享给你的用户，以便访问网页。​

  * 查看 DNS 解析记录：你可以复制此处的解析记录，将其添加到 DNS 的解析记录中。​

  * 查看证书类型和有效期：你可以查看当前配置证书的类型和有效期。如果证书即将过期，你可以添加新的证书。​

  * 删除域名：当需要更换项目的域名时，你可以从你的项目中解除该域名的绑定。​

  * 说明

删除域名后，用户将无法通过此域名访问该服务。此操作不可逆，请在执行前仔细确认。​

​

常见问题​

  * ​域名已在其他服务商那边备案，还需要重新备案吗？​

  * ​备案审核需要多长时间？​

  * ​备案未完成会影响部署吗？​

  * ​扣子生成的免费证书和火山证书有什么区别？​

  * ​可以使用其他厂商的 SSL 证书吗？​

  * ​免费证书到期后能生成新的免费证书吗？​

​

上一篇

部署运维概述

下一篇

部署网页应用