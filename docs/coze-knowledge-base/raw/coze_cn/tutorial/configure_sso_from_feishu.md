---
source_url: https://docs.coze.cn/tutorial/configure_sso_from_feishu
title: '通过飞书进行 SAML SSO 登录 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:14Z
---

# 通过飞书进行 SAML SSO 登录 - 文档 - 扣子

通过飞书进行 SAML SSO 登录

通过单点登录功能（即 Single Sign On，SSO）可实现飞书和扣子编程之间登录身份互通互认。企业用户只需登录飞书，就可以直接访问扣子编程中的企业工作空间，免去每次访问都需要输入扣子账号和密码的步骤。本文档以飞书为例，演示飞书作为 IdP 时，企业管理员开启 SSO 登录的详细操作步骤，帮助你理解企业 IdP 与扣子编程进行 SSO 的端到端配置流程。​

场景说明​

某企业使用飞书作为移动办公平台，在飞书中维护自己的员工身份信息。企业使用员工邮箱前缀作为员工的唯一标识，例如用户 Alice 的员工邮箱为 Alice_123@enterprise.com，该员工在扣子编程中作为企业成员的用户名为 Alice_123。​

企业管理员购买了扣子企业旗舰版之后可以开启 SSO 登录，能够让 Alice 通过链接基于飞书已经登陆的身份直接跳转扣子编程，以企业成员的身份访问扣子企业旗舰版工作空间。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27173.61111111111111%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2aaa427078694e7d80f57aef14fe6887~tplv-goo7wpa0wc-quality:q75.image)​

​

准备工作​

  * 已在扣子编程中创建企业组织、创建企业成员 Alice_123，并将其加入企业。​

  * 已获取飞书集成平台管理员权限、扣子编程企业超级管理员权限。​

步骤一：在扣子编程中获取配置信息​

在扣子编程中获取以下配置信息：​

​

信息​| 查看方式​| 示例​  
---|---|---  
SAML 服务提供者（SP）元数据 URL​| 

1.企业超级管理员登录[扣子编程企业管理页面](<https://docs.coze.cn/tutorial/admin.coze.cn>)。​

2.在左侧导航栏选择 SSO 设置，并单击去配置。页面会自动跳转到火山引擎扣子控制台，引导你查看 SP 元数据。​

3.在弹出页面中 SSO 登录 > 服务提供商信息一栏复制 ACS URL 和 Entity ID。​

  * 你也可以根据页面提示，直接下载元数据文档。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27250%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
扣子企业超级管理员对应的火山引擎主账号 ID​| 扣子企业超级管理员登录到火山引擎扣子编程后，在[账号管理](<https://console.volcengine.com/user/basics/>)页面查看账号 ID。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27234%27%20height=%27208%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM0IiBoZWlnaHQ9IjIwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
确认用户的唯一标识​| NameID 是 SAML 断言中用于标识用户的一个元素。它是一个唯一标识符，用于在 IdP 和 SP 之间唯一地标识用户。​注意本示例中，SAML 响应的 Name ID 为邮箱名（不包含@及后缀），开始配置前请确认：​

  * 企业用户 Alice 在火山扣子控制台 > 用户管理页面的用户名为 Alice_123。​

  * 企业用户 Alice 在飞书中配置的邮箱前缀同样为 Alice_123。​

​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271816%27%20height=%27908%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgxNiIgaGVpZ2h0PSI5MDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

步骤二：在飞书集成平台创建并配置应用​

作为身份提供商（IdP），飞书集成平台需要以应用的形式感知服务提供商扣子编程，实现单点登录。因此，企业管理员需要飞书集成平台创建对应扣子编程的应用，应用类型为自建应用。​

1.

使用飞书租户的管理员用户或具有同等权限的飞书用户登录[飞书集成平台](<https://anycross.feishu.cn/console/identity/sso-app-manager>)。​

2.

在身份集成 > 应用单点登录 > 应用管理页面中，单击新建应用，创建一个新的自建应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27580%27%20height=%27282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgwIiBoZWlnaHQ9IjI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在新建应用页面，选择应用类型为自建应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27315%27%20height=%27190%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE1IiBoZWlnaHQ9IjE5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在基本配置页面，配置应用程序的名称等基本信息，然后单击下一步。​

  * 此示例中可以填写应用名称为扣子编程，该名称仅用作在 IdP 处展示。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27363%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYzIiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在应用配置页面填写 SAML 配置。​

a.

在更多配置区域，展开配置，启用 SAML 2.0 协议。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27338%27%20height=%27301%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM4IiBoZWlnaHQ9IjMwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

填写以下设置，并单击保存并启用。​

  * ​

配置​| 说明​| 示例​  
---|---|---  
授权配置​| 在快捷导入 SAML 元数据区域，单击上传文件，上传步骤一中下载的 SP 元数据文件。​上传文件后，系统会默认填写登录回调地址。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271518%27%20height=%27948.75%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUxOCIgaGVpZ2h0PSI5NDguNzUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
支持 IdP 侧发起登录​| 可选。配置 IdP 登录后，企业用户 Alice 可从飞书提供的登录地址访问扣子编程。​开启支持 IdP 侧发起登录，并手动填写以下配置：​
    * ACS URL、Destination 和 Destination：设置为步骤一中获取的 ACS URL。​
    * Audience：设置为步骤一中获取的 Entity ID。 ​
配置成功后，页面右侧展示的认证请求端点则是从 IdP 侧（也就是飞书侧）访问扣子编程的 URL。​| IdP 登录：​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272144%27%20height=%271284.1666666666667%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE0NCIgaGVpZ2h0PSIxMjg0LjE2NjY2NjY2NjY2NjciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​认证请求端点：​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272832%27%20height=%271194.75%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgzMiIgaGVpZ2h0PSIxMTk0Ljc1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
Name ID 配置​| 选择进行 SSO 身份映射时使用的飞书用户字段。建议此处选择在飞书侧维护的全局唯一的、仅包含英文字母的字段。​本示例选择邮箱名（不含"@"及后缀），表示通过飞书用户的邮箱前缀去匹配扣子编程中的企业成员用户名。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271888%27%20height=%271160.3333333333335%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg4OCIgaGVpZ2h0PSIxMTYwLjMzMzMzMzMzMzMzMzUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
SAML 2.0 协议端点​| 在页面右侧 SAML 2.0 协议端点区域中，单击下载元数据文档，下载身份提供商（IdP）元数据文件，并将其保存在本地目录。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272696%27%20height=%271291.8333333333335%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY5NiIgaGVpZ2h0PSIxMjkxLjgzMzMzMzMzMzMzMzUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

  * 完整配置示例如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27627%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI3IiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

配置完成后，点击保存并启用。​

7.

确认可访问范围。​

  * 在刚创建的应用中的访问授权页面配置可以进行单点登录的飞书用户范围。默认全部成员均可通过飞书用户身份以 SSO 方式登录扣子编程，访问企业工作空间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27420%27%20height=%27287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIwIiBoZWlnaHQ9IjI4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：在扣子编程中上传 IdP SAML 配置​

在扣子编程中上传企业身份管理系统（IdP）的元数据信息，建立扣子编程对 IdP 的信任，并开启 SSO 登录，实现企业 IdP 通过用户 SSO 登录扣子编程。​

1.

企业超级管理员登录[扣子编程](<https://code.coze.cn/home>)。在左下角单击个人头像，选择账号 > 企业管理。​

  * 你也可以直接访问[扣子编程企业管理页面](<https://docs.coze.cn/tutorial/admin.coze.cn>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27213.45291479820628%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIxMy40NTI5MTQ3OTgyMDYyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在左侧导航栏选择 SSO 设置，单击去配置。​

3.

在弹出页面中 SSO 登录 > 身份提供商信息一栏，上传步骤二中下载的 IdP 元数据文档。​

4.

在 SSO 登录区域，开启 SSO 登录。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27107.63636363636364%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjEwNy42MzYzNjM2MzYzNjM2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27389.84771573604064%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM4OS44NDc3MTU3MzYwNDA2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27457.83132530120486%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ1Ny44MzEzMjUzMDEyMDQ4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

结果验证​

完成 SSO 登录配置后，企业用户 Alice 可以从扣子编程或者飞书侧发起单点登录。​

通过 SP 登录

通过 IdP 登录

通过扣子编程登录页面登录：​

1.

企业成员访问管理员提供的扣子编程登录地址。​

  * 管理员可以在[火山扣子控制台](<https://console.volcengine.com/coze-pro/overview>) > 成员管理页面查看这个登录地址。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27568%27%20height=%27150%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY4IiBoZWlnaHQ9IjE1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

企业成员 Alice 在登录页面中输入企业别名和用户名 Alice_123，并单击下一步。​

  * 说明

用户名要填写火山子用户的用户名（user_name），而不是扣子用户名（coze_user_name）。​

​

3.

单击企业账号免密登录。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27286%27%20height=%27177%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg2IiBoZWlnaHQ9IjE3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

页面会自动跳转至飞书的登录页面，根据界面提示，输入账号密码或者扫描二维码登录。​

5.

登录成功后，页面将自动跳转至扣子编程，企业成员 Alice 可以选择访问火山引擎扣子控制台或扣子编程。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27418%27%20height=%27211%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE4IiBoZWlnaHQ9IjIxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

优化大模型响应时间

下一篇

配置 SSO 登录后跳转至扣子编程指定页面