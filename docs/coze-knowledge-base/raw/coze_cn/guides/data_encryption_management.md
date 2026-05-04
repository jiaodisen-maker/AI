---
source_url: https://docs.coze.cn/guides/data_encryption_management
title: '数据加密管理 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:47:16Z
---

# 数据加密管理 - 文档 - 扣子

数据加密管理

扣子企业旗舰版支持使用火山引擎 KMS 密钥对会话数据进行存储加密，从而满足企业对数据安全的高要求。本文介绍如何使用火山引擎 KMS 实现数据加密管理。​

功能简介​

扣子企业旗舰版支持两种密钥类型：扣子编程自带的加解密密钥和火山引擎 KMS 密钥。默认情况下，扣子使用自带密钥加密存储的会话数据。在金融、政府等对数据安全有更高要求的场景中，企业可选择使用火山引擎 KMS 密钥进行加解密，以满足其数据安全保障需求。企业可以在火山引擎上创建 KMS 密钥，将扣子侧的密钥类型修改为 KMS，并填写火山引擎 KMS 上创建的密钥，从而实现更高级别的数据加密。​

使用火山引擎 KMS 密钥的优势包括：​

  * 自主管理密钥：企业可以自主创建、管理和控制加密密钥，提升对数据的掌控力。​

  * 可靠的安全保障：为会话数据提供更可靠的安全保障，确保企业在享受扣子编程服务时，数据安全无忧。​

费用说明​

使用火山引擎 KMS 密钥，火山引擎 KMS 产品会收取密钥托管费，这些费用自动从你的火山引擎余额中扣款，具体收费标准可参考[密钥管理计费说明](<https://www.volcengine.com/docs/6476/71331>)。​

注意事项​

​

类别​| 说明​  
---|---  
扣子套餐限制​| 数据加密管理为扣子企业旗舰版白名单功能，如果需要使用该功能，你可以提供企业 ID，联系扣子商务经理添加白名单。你可以在企业管理页面的 URL 路径中查看企业 ID。例如，在 URL https://www.coze.cn/enterprise/volcano_210195***/enterprise/workspace 中，企业 ID 为 volcano_210195***。​  
火山账号​| 

  * 需要使用企业的超级管理员或管理员对应的火山引擎账号创建 KMS 密钥。​

  * 火山引擎账号欠费后，密钥无法使用，会话数据无法加解密，需及时充值以保证功能正常。​

  
密钥规格​| 扣子侧支持的 KMS 密钥类型仅支持 SYMMETRIC_256，密钥用途仅支持 ENCRYPT_DECRYPT。​  
加密生效范围​| 

  * 设置火山引擎 KMS 加密后，仅对之后创建的会话数据进行加密，不影响历史会话数据。​

  * 数据加密管理仅针对企业内的会话数据进行加密。​

  
密钥更换​| 更换密钥后，请勿删除原密钥，否则会导致无法解析历史会话或获取上下文信息。​  
  
​

步骤一：创建火山引擎 KMS 密钥​

你需要创建火山引擎 KMS 密钥，用于加解密数据。​

1.

登录火山引擎 [KMS控制台](<https://console.volcengine.com/kms/region:kms+cn-beijing/primary>)开通 KMS 服务，新建密钥环，详细步骤请参见[密钥管理快速入门](<https://www.volcengine.com/docs/6476/71333>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27507.175925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjUwNy4xNzU5MjU5MjU5MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

单击密钥环，在密钥环详情页面，单击新建密钥，关键参数说明如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27378.698224852071%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM3OC42OTgyMjQ4NTIwNzEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * ​

参数​| 说明​  
---|---  
密钥类型​| 本场景中需要选择 SYMMETRIC_256。​  
密钥用途​| 本场景中需要选择 ENCRYPT_DECRYPT。​  
保护等级​| 根据需要选择 SOFTWARE（软件保护） 或 HSM（硬件安全模块），详细说明请参见[密钥保护等级](<https://www.volcengine.com/docs/6476/71338#密钥保护等级>)。​  
别名​| 自定义一个易于识别的别名，便于后续管理和识别。​  
  
​

3.

拷贝密钥 TRN，后续在扣子编程中需要使用该密钥 TRN 配置数据加密。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27268.1712962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjI2OC4xNzEyOTYyOTYyOTYzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤二：配置数据加密类型​

扣子默认的密钥类型为扣子的加解密密钥，企业的超级管理员和管理员可以修改密钥类型为 KMS，并填写火山引擎 KMS 上创建的密钥进行加解密。​

说明

角色限制：组织超级管理员或管理员。​

​

1.

在[扣子编程](<https://code.coze.cn/home>)左下角单击个人头像，选择企业，然后单击对应组织的设置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27313%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEzIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

2.

在企业组织管理页面的顶部选择数据加密管理页签，修改密钥类型为 火山 cloud_kms 主密钥，并填写步骤一中拷贝的密钥 TRN，单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27159.1435185185185%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjE1OS4xNDM1MTg1MTg1MTg1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

常见问题​

为什么数据加密管理的状态为已失效？​

当密钥类型为 火山 cloud_kms 主密钥 类型时，如果状态为已失效，你可以按以下思路进行排查：​

  * 确保火山引擎侧 KMS 密钥的状态为启用中，如果状态为已停用、已计划删除、已归档，则扣子侧数据加密管理将变成已失效。此时，扣子将无法对会话消息进行解密，导致回复消息报错。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27350.8101851851852%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjM1MC44MTAxODUxODUxODUyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 确保火山引擎账号未欠费，如果账号欠费，密钥无法使用，则扣子侧数据加密管理将变成已失效，你需要尽快续费，以免影响会话功能。​

更换密钥对历史会话有影响吗？​

更换密钥后，新会话数据将使用更换后的密钥进行加解密，历史会话数据会使用原密钥进行解密。因此，更换密钥后，请不要删除原密钥。​

  * 如果删除原密钥，将导致历史会话数据无法解密，进而无法解析历史会话或获取上下文信息。​

  * 原密钥存在时，更换密钥不会影响历史会话数据的正常使用。​

​

​

上一篇

通过飞书进行 SAML SSO 登录

下一篇

对话内容安全策略