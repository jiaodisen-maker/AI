---
source_url: https://docs.coze.cn/guides/oidc_plugin
title: 'OIDC 插件配置教程 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:50Z
---

# OIDC 插件配置教程 - 文档 - 扣子

OIDC 插件配置教程

OIDC 是一种广泛使用的授权框架，它基于 OAuth 2.0 协议之上，提供了身份验证和授权的功能。本教程介绍扣子编程插件如何与 Google Cloud Platform（GCP）集成，实现安全访问 GCP Cloud Storage Bucket。​

前置条件​

你已经创建了一个非公开访问的 Bucket，本教程 Bucket 名称设置为 coze-plugin-oidc-test，详情可参考 [Create buckets](<https://cloud.google.com/storage/docs/creating-buckets>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272555%27%20height=%27372.6041666666667%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f162ce1eca0f4554a74faea47fffdda1~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤一：配置工作负载身份联合​

借助 Workload Identity，你的工作负载无需服务账号密钥即可访问 Google Cloud。​

1.

登录 [Google Cloud 的 IAM&Admin 控制台](<https://console.cloud.google.com/iam-admin/iam>)。​

2.

在左侧导航栏，单击 Workload Identity Federation，然后单击 GET STARTED。​

3.

创建身份池，使用池来管理外部身份，然后单击 CONTINUE。​

  * Name：自定义池的名称，本教程输入 coze-plugin-federation。​

  * Pool ID：输入池的 ID，本教程 ID 与 Name 设置一致。​

  * Description：添加池的描述。​

  * Enabled Pool：选择启用池。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27638%27%20height=%27275%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5b7b824b0bb542919123d30a972bd64e~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

向池添加提供方，提供方可管理和验证身份，然后单击 CONTINUE。​

  * Select a provider：选择与你的外部身份源匹配的提供商类型，本教程选择 OpenID Connection（OIDC）。​

  * Provider name：配置提供商名称，本教程输入coze-cn。​

  * Issuer (URL)：配置颁发者网址，必须以 https:// 开头，本教程输入 https://api.coze.cn。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27642%27%20height=%27277%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQyIiBoZWlnaHQ9IjI3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 在 Audiences -> Default audience，复制 URL，在扣子编程插件配置中需要使用该 URL。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27648%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQ4IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

配置提供方属性，本教程输入 assertion.sub。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27654%27%20height=%27282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU0IiBoZWlnaHQ9IjI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

单击Save，在池详细信息页，复制并保存 IAM principal，配置访问控制策略时会使用 IAM principal的值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27657%27%20height=%27283%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU3IiBoZWlnaHQ9IjI4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：配置 OIDC 插件​

OIDC 是一种广泛使用的授权框架，它基于 OAuth 2.0 协议之上，提供了身份验证和授权的功能。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，选择 +资源 > 插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27170%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA0IiBoZWlnaHQ9IjE3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

配置插件信息并单击确认。​

a.

设置基础信息。​

  * ​

配置项​| 说明​  
---|---  
插件图标​| 单击默认图标后，您可以上传本地图片文件作为新的图标。​  
插件名称​| 自定义插件名称，用于标识当前插件。建议输入清晰易理解的名称，便于大语言模型搜索与使用插件。​  
插件描述​| 插件的描述信息，一般用于记录当前插件的用途。​  
插件工具创建方式​| 本教程选择基于已有服务创建。​  
插件 URL​| 插件的访问地址或相关资源的链接，本教程输入 Google Cloud Storage 的默认域名https://storage.googleapis.com。​说明插件 URL 必须为域名格式，暂不支持 IP 格式的 URL 地址。​​  
Header 列表​| HTTP 请求头参数列表。您需要根据 API 自身的参数配置要求来填写。​  
  
​

b.

选择授权方式，本教程选择 Service > OAuth 2.0 & OIDC。​

  * 配置参数说明如下：​

  * ​

配置项​| 说明​  
---|---  
grant_type​| 根据 GrantType 来选择使用的 OAuth Flow，支持的 Flow 包括：​
    * TokenExchange：用于在不同服务之间交换令牌。​
    * ClientCredential：用于客户端凭据授权流程，适用于没有用户直接参与的情况。​
本教程选择 TokenExchange。​  
endpoint_url​| 授权服务器的端点 URL，用于发送授权请求和接收响应。配置时需要指定授权服务器的地址，以便客户端可以正确地向服务器发起请求。​本教程输入 Google Cloud 的 Security Token Service（STS）API 的端点URL：https://sts.googleapis.com/v1/token。​  
audience​| 资源服务器，客户端告诉授权服务器它希望代表用户访问哪个资源服务器。配置时需要指定资源服务器的标识符。​本教程，输入步骤一中从 Audiences -> Default audience 复制的值。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27129%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjEyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
scope​| 客户端请求的权限范围。对于 OIDC，通常需要包含openid作用域，以请求身份验证，配置时需要根据需要请求的权限范围来设置。​本教程输入 https://www.googleapis.com/auth/devstorage.read_only，更多 GCP OAuth 权限点请参考 [Google文档](<https://developers.google.com/identity/protocols/oauth2/scopes?hl=zh-cn>)。​  
client_id​| 客户端在授权服务器注册时获得的唯一标识符，配置时需要使用在授权服务器注册应用时获得的 client_id。​本教程无需配置 client_id。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27303%27%20height=%27630%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAzIiBoZWlnaHQ9IjYzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：配置插件工具​

参考以下操作，配置插件工具：​

1.

在已创建的插件页面，单击创建工具。​

2.

在创建工具页面，配置基本信息，然后单击确定。​

  * 工具名称：用于标识当前工具。建议输入清晰易理解的名称，便于后续大语言模型搜索与使用工具。​

  * 工具描述：工具的描述信息，一般用于记录当前工具的用途。​

3.

在更多信息区域，单击编辑，配置工具路径和请求方法，然后单击保存。​

  * 工具路径：输入 API 路径。本教程API路径设置为 https://storage.googleapis.com/storage/v1/b/coze_plugin_oidc。​

  * 请求方法：参数传入方法，本教程选择 Get 方法。​

4.

在配置输入参数区域，配置工具的输入参数。​

  * 本教程不配置输入参数。​

5.

在配置输出参数区域，配置工具的输出参数，然后单击保存。​

  * 本教程新增一个名称为 name 的参数，以获取 Bucket 的 名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27603%27%20height=%27265%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAzIiBoZWlnaHQ9IjI2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：配置访问控制策略​

配置 Bucket 访问控制策略，实现步骤一中配置的 Provider 能够访问对应的 Bucket。​

1.

登录 [Google Cloud 的 Cloud Storage 控制台](<https://console.cloud.google.com/storage/overview;tab=overview?hl=EN&inv=1&invt=AbjvEw&orgonly=true&project=coze-plugin-oidc-test-444309&supportedpurview=project>)。​

2.

在左侧导航栏，单击 Buckets，然后单击 PERMISSIONS -> GRANT ACCESS。​

3.

添加访问控制权限，然后单击 SAVE。​

  * 在 Add Principals 填写步骤一中复制的 IAM principal，并根据以下规则调整 SUBJECT_ATTRIBUTE_VALUE ：​

  * ​

Plain Text

复制

// account_id: coze 账号 ID，这个账号必须是 workspace owner 的账号 ID​

// workspace_id: 空间 ID​

// plugin_id: 插件 ID​

acct:${account_id}/ws:${workspace_id}/pln:${plugin_id}​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27610%27%20height=%27304%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEwIiBoZWlnaHQ9IjMwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤五：调试插件​

完成上述所有配置，在扣子编程插件页面进行试运行，测试能够获取 Bucket 的名称。​

1.

在编辑工具页面，单击试运行。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27396%27%20height=%27115%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk2IiBoZWlnaHQ9IjExNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在试运行页面，单击运行。​

  * 本教程无需配置输入参数。若在 Response 页签中成功返回 Bucket 名称，即表示创建工具成功。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27613%27%20height=%27415%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEzIiBoZWlnaHQ9IjQxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * ​

上一篇

创建 OAuth 插件

下一篇

流式插件配置教程