---
source_url: https://docs.coze.cn/developer_guides/oauth_code
title: 'OAuth 授权码授权 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:18:21Z
---

# OAuth 授权码授权 - 文档 - 扣子

OAuth 授权码授权

扣子编程支持应用程序通过 OAuth 授权码授权（Authorization Code Grant）的方式调用扣子编程 API。用户通过浏览器访问包含扣子编程功能的 Web 应用程序时，Web 应用程序重定向用户到扣子编程服务端以获取授权码（code），然后使用授权码向扣子编程服务端交换访问令牌。例如 Web 应用程序通过扣子编程 API 封装了扣子编程的查看 Bot 的详细信息和指定 Bot 对话等功能，用户使用这些功能之前，需要经由扣子编程服务端鉴权。​

说明

通过 OAuth 授权码方式授权时，应用程序需要拥有可通过 Web 访问的前端页面，否则无法实现重定向等一系列授权流程；同时应有稳定的后端架构，可处理前端请求、安全存储客户端密钥（Client Secret），与 OAuth 授权服务器和 OpenAPI 交互。​

​

授权流程​

Web 应用程序授权流程如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27291.6666666666667%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4b881d91c69c43908995e2d92451b1d1~tplv-goo7wpa0wc-quality:q75.image)​

​

具体流程说明如下：​

1.

在扣子编程创建 OAuth 应用。​

2.

应用程序调用 API ​获取授权页面 URL和​获取 OAuth Access Token，获取 OAuth 访问令牌。​

3.

应用程序根据访问令牌调用扣子编程 API。​

详细步骤如下：​

1 创建 OAuth 应用​

说明

在扣子企业版（企业标准版、企业旗舰版）中，仅组织超级管理员和管理员有权限创建、编辑、删除 OAuth 应用，以及对应用进行授权操作。​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左侧导航栏选择 API & SDK。​

3.

在顶部单击授权 > OAuth 应用页签。​

4.

在 OAuth 应用页面右上角单击创建新应用，填写应用的基本信息。 ​

  * ​

配置​| 说明​  
---|---  
应用类型 ​| 应用的类型，此处设置为普通。​  
客户端类型​| 客户端类型，此处设置为Web 后端应用。​  
应用名称 ​| 应用的名称，在扣子编程中全局唯一。 ​  
描述 ​| 应用的基本描述信息。 ​  
  
​

5.

填写 App 的配置信息。 ​

  * ​

6.

单击确定，完成配置。 ​

2 获取访问令牌​

1.

终端用户在 Web 应用程序中触发授权操作，例如点击和 Bot 对话的按钮。该动作对应扣子发起对话 API，应用程序需要获得扣子账号的授权。​

2.

Web 应用程序重定向用户到授权服务器以获取 code。​

  * 应用程序通过302重定向方式发起 ​获取授权页面 URL API 请求。​

  * 请求中携带 OAuth 应用的客户端 ID 和客户端密钥 、重定向 URL 等信息。请求示例如下：​

  * ​

  * Response Header 中的 location 字段中为跳转链接。例如https://www.coze.cn/oauth/consent?authorize_key=JacVeqTW93ps5m5N9n349bEBgIsWrnNp。浏览器跳转到此 URL，引导用户完成扣子账号授权。授权页面示例如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27225%27%20height=%27298%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI1IiBoZWlnaHQ9IjI5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

3.

扣子服务端会在 API 的响应中返回 code。​

  * 从重定向的 URL 地址中获取 code，例如本示例中 code 为 code_WZmPRDcjJhfwHD****。​

  * ​

4.

使用授权码交换访问令牌。​

  * 应用程序向扣子服务端发起 ​获取 OAuth Access Token 请求，请求中携带 code，扣子服务端会在 API 的响应中返回 access_token 和 refresh_token。其中：​

  * access_token 即访问令牌，用于发起扣子 API 请求时鉴权，有效期为 15 分钟。​

  * refresh_token 用于刷新 access_token，有效期为 30 天。refresh_token 到期前可以多次调用 ​刷新 OAuth Access Token 接口获取新的 refresh_token 和 access_token。​

  * 接口示例如下：​

  * ​

3 发起扣子 API 请求​

在 API 请求头中通过 Authorization=Bearer $Access_Token 指定访问令牌，发起扣子 API 请求。每个接口对应的权限点不同。​

以​获取已发布智能体的配置（即将下线） API 为例，完整的 API 请求如下：​

​

获取授权页面 URL​

Web 应用程序可调用此 API 获取 OAuth 授权页面 URL 地址。​

基础信息​

​

​

Path 参数​

​

Query​

​

返回结果 ​

返回结果的 Http code 为 302，且 Response Header 中的 location 字段中为跳转链接。例如https://www.coze.cn/oauth/consent?authorize_key=JacVeqTW93ps5m5N9n349bEBgIsWrn****。浏览器跳转到此 URL，引导用户完成 Coze 账号授权。​

示例 ​

请求示例 ​

​

返回示例​

​

获取 OAuth Access Token​

通过授权码（OAuth code）获取 OAuth Access Token。​

基础信息​

​

Header​

​

Body​

​

返回结果​

​

示例 ​

请求示例 ​

​

返回示例​

​

刷新 OAuth Access Token ​

根据 refresh_token 获取新的 OAuth Access Token。​

调用​获取 OAuth Access Token API 获取的 OAuth Access Token 有效期为 15 分钟，refresh_token 有效期为 30 天。refresh_token 有效期内可以调用此 API 获取新的 OAuth Access Token。​

接口调用成功后，入参中指定的 refresh_token 失效。​

基础信息​

​

Header​

​

Body​

​

返回结果​

​

示例 ​

请求示例 ​

​

返回示例​

​

错误码​

​

常见问题​

如何处理 OAuth 授权码授权失败，提示“OAuth 错误/请求参数错误”？​

请检查回调地址中的特殊字符是否已正确转义。例如，回调地址中的 # 需要转义为 %23。确保所有特殊字符都已按照URL 编码规则进行转义，然后重新尝试授权。​

​

上一篇

通过示例文件体验 OAuth 授权流程

下一篇

OAuth PKCE