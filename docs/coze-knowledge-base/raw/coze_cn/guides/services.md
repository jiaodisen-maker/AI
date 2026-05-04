---
source_url: https://docs.coze.cn/guides/services
title: '基于 API 创建插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:35Z
---

# 基于 API 创建插件 - 文档 - 扣子

基于 API 创建插件

本文介绍如何通过插件页面向导，基于已有服务创建自定义插件。基于已有服务创建插件时，直接将公开使用或本人开发的 API 配置为插件。创建插件后，必须发布插件才可以被低代码智能体使用。​

说明

  * 个人工作空间中的插件，仅能被个人调用；企业工作空间中插件，能被任意企业成员调用。​

  * 插件发布了新版本后，使用了这个插件的低代码智能体会自动使用发布的最新版本。​

​

操作视频​

本视频以扣子编程的查看智能体列表 API 为例，演示将 API 服务转化为实用插件的全流程，包括创建插件、添加工具、发布插件等步骤。相关教程，请参考​快速搭建智能体列表查询插件。​

​

​

__

Replay

Play

00:00 / 03:47 Live

00:00

Fullscreen 

Cssfullscreen 

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag 

​

​

步骤一：创建插件​

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
插件工具创建方式​| 选择云侧插件-基于已有服务创建。​  
私网连接​| 基于已有服务创建云侧插件时，只支持选择不使用私网连接。​  
插件 URL​| 插件的访问地址或相关资源的链接，例如https://www.example.com/api。​说明插件 URL 必须为域名格式，暂不支持 IP 格式的 URL 地址。​​  
Header 列表​| HTTP 请求头参数列表。您需要根据 API 自身的参数配置要求来填写。​  
  
​

b.

设置授权方式。​

  * ​

配置项​| 说明​  
---|---  
不需要授权​| 无需授权，不指定授权参数。​  
Service​| 服务认证，支持 Service token / API key 和 OAuth 2.0 & OIDC：​
    * Service token / API key：该认证方式是指 API 通过秘钥或令牌校验请求者的身份。配置参数说明如下：​
    * 位置：选择秘钥或令牌在 API 请求中的位置，及 Header（请求头）或是 Query （查询参数）内。​
    * Parameter name：秘钥或令牌对应的参数名称。​
    * Service token / API key：秘钥或令牌的值。后续根据该值进行服务认证。​
    * OAuth 2.0 & OIDC：OIDC 一种广泛使用的授权框架，它基于 OAuth 2.0 协议之上，提供了身份验证和授权的功能。配置参数说明如下：​
    * grant_type：根据 GrantType 来选择使用的 OAuth Flow，支持的 Flow 包括：​
    * TokenExchange：用于在不同服务之间交换令牌。​
    * ClientCredential：用于客户端凭据授权流程，适用于没有用户直接参与的情况。​
    * endpoint_url：授权服务器的端点 URL，用于发送授权请求和接收响应。配置时需要指定授权服务器的地址，以便客户端可以正确地向服务器发起请求。​
    * audience：资源服务器，客户端告诉授权服务器它希望代表用户访问哪个资源服务器。配置时需要指定资源服务器的标识符。​
    * scope：客户端请求的权限范围。对于 OIDC，通常需要包含openid作用域，以请求身份验证，配置时需要根据需要请求的权限范围来设置。​
    * client_id：客户端在授权服务器注册时获得的唯一标识符，配置时需要使用在授权服务器注册应用时获得的 client_id。​  
Oauth > standard​| OAuth 是一种常用于用户代理身份验证的标准，它允许第三方应用程序在不共享用户密码的情况下访问用户下的特定资源。​
    * client_id：注册 OAuth 后获取的唯一标识符。​
    * client_secret：与 client_id 匹配的密码。​
    * client_url：重定向授权 URL，在授权过程中，扣子编程会将用户引导至 [client_url]?response_type=code&client_id=[client_id]&scope=[scope]&state=****&redirect_uri=[扣子编程平台的回调安全地址]。​
    * scope：您的应用需要访问的资源范围或级别。​
    * authorization_url：获取用户令牌（token）的 URL。当用户通过上述 client_url 引导链接授权成功后，三方服务会返回用于获取 token 的 code，并跳转至扣子编程的回调安全地址，此时，扣子编程会通过对应参数向 authorization_url 对应地址发起请求，获取用户的 access_token。​
    * authorization_content_type：向 OAuth 发送授权请求时的内容类型或数据格式。​  
  
​

  * 授权示例：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27433%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI2IiBoZWlnaHQ9IjQzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：创建工具​

1.

在已创建的插件页面，单击创建工具。​

2.

配置工具名称和描述信息，然后单击确定。​

3.

在编辑工具页面，完成以下操作。​

a.

单击更多信息区域右上角的编辑，配置工具的路径和请求方法，然后单击保存。​

  * ​

配置项​| 说明​  
---|---  
工具路径​| 输入 API 路径。​
    * 如果 API 没有路径，直接填写 / 作为路径。​
    * 如果您需要在 API 的请求路径内插入变量，可以使用大括号 {} 包裹变量名作为占位符，例如 https://www.example.com/api/{id}/getTime。此外，在后续添加输入参数时，你需要新增一个和变量名相同的输入参数，并将参数的传入方法设置为 Path。​  
请求方法​| 选择 API 的请求方式。​  
  
​

b.

单击配置输入参数区域右上角的编辑，单击新增参数配置请求参数，然后单击保存。​

  * 说明

如果 API 没有输入参数，则直接单击保存并继续。​

​

  * ​

配置项​| 说明​  
---|---  
参数名称​| 参数名称，支持字母、数字或下划线。​  
参数描述​| 参数描述。准确的参数描述可以帮助用户或 LLM 理解当前参数的作用。​  
参数类型​| 参数的数据类型。​  
传入方法​| 参数传入方法。可选值：​
    * Body：请求参数​
    * Path：路径参数​
    * Query：查询参数​
    * Header：请求头参数​  
是否必填​| 参数是否必填。​
    * 打开开关表示当前参数为必填参数。​
    * 关闭开关表示当前参数为选填参数。​  
默认值​| 设置参数的默认值。​  
开启​| 当参数设置为不可见时，插件的使用者和大模型将无法看到该参数。如果该参数设置了默认值并且不可见，则在调用插件时，智能体会默认只使用这个设定值。​  
  
​

c.

单击配置输出参数区域右上角的编辑，单击自动解析，在弹出的页面输入请求参数值，再单击自动解析。接口调用成功后，会将返回参数自动填充到输出参数列表，你也可以单击新增参数，手动设置输出参数。​

  * ​

配置项​| 说明​  
---|---  
参数名称​| 参数名称，支持字母、数字或下划线。参数名称​  
参数描述​| 参数描述。准确的参数描述可以帮助用户或 LLM 理解当前参数的作用。​  
参数类型​| 参数的数据类型。​  
开启​| 当设置为不可见时，该参数将不会被返回给大模型。​  
  
​

4.

单击试运行。​

5.

在试运行页面，输入入参，然后单击运行测试接口。测试成功后，单击完成。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27615%27%20height=%27296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE1IiBoZWlnaHQ9IjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：发布插件​

当添加的工具调试成功后，你就可以发布插件了。发布后，插件才可以被智能体使用。​

1.

在插件页面，单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272189%27%20height=%27402.96723868954757%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE4OSIgaGVpZ2h0PSI0MDIuOTY3MjM4Njg5NTQ3NTciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

选择是否需要收集个人信息。本教程的接口不涉及个人信息收集，选择否，直接发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27369%27%20height=%27171%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY5IiBoZWlnaHQ9IjE3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上架到商店​

你可以将插件上架到扣子插件商店或企业插件商店。不能同时上架扣子插件商店和企业插件商店，仅支持选择其中一个渠道。​

  * 上架扣子插件商店​

  * 对于通用功能、不涉及敏感数据且具有广泛适用性的公开插件，你可以将其上架到扣子商店，以便更多扣子用户发现、使用。详情请参考​将插件上架到插件市场。​

  * 上架企业插件商店​

  * 企业旗舰版支持。​

  * 对于企业自主开发的涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的插件，你可以将其上架到企业插件商店，供企业成员使用。详情请参考​管理企业插件。​

​

上一篇

插件介绍

下一篇

通过 JSON 或 YAML 文件导入插件