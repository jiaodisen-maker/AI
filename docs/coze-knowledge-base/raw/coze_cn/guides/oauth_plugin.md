---
source_url: https://docs.coze.cn/guides/oauth_plugin
title: '创建 OAuth 插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:47Z
---

# 创建 OAuth 插件 - 文档 - 扣子

创建 OAuth 插件

OAuth 是一种开放授权标准，允许第三方应用程序在用户授权的情况下访问用户存储在服务商的资源，而无需提供用户名和密码。如果服务支持 OAuth 认证，并且你希望在插件中集成该服务，你可以创建一个支持 OAuth 认证的插件。创建成功后，智能体需要通过 OAuth 授权流程来获取访问令牌，以便安全地调用集成到插件中的服务。​

本文以扣子编程 API 为例，为你演示如何创建一个支持 OAuth 认证的插件。​

前提条件​

请确保你已经在 API 服务平台创建了 OAuth 应用，并获取了客户端 ID、客户端密钥等信息，详情请参考 API 服务提供商的开发文档。​

本示例以在插件中集成扣子编程 API 为例，因此需在扣子编程中创建 OAuth 应用，详情请参考​1 创建 OAuth 应用。在创建 OAuth 应用时，需注意如下事项：​

  * 先留空重定向 URL 配置。重定向 URL 需包含插件 ID，因此需先完成​步骤一：创建插件，获取到插件 ID 后，再配置。​

  * 记录客户端 ID、客户端密钥。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27192%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7ca896bb98cc468b9c3912a35b88b117~tplv-goo7wpa0wc-quality:q75.image)​

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

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27170%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/013e73be30ef4768a3432e8017d9c325~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

填写插件基础信息。​

a.

输入插件名称和描述。​

b.

插件工具创建方式选择基于已有服务创建。​

c.

插件 URL：输入 API 的服务地址，例如 https://api.coze.cn。​

d.

将 API 的 Header 信息配置到 Header 列表中。​

e.

授权方式选择 OAuth > standard，然后配置 OAuth 参数。​

  * ​

配置​| 说明​  
---|---  
client_id​| 客户端 ID，是应用在授权服务器中的唯一标识符，授权服务器通过客户端 ID 来识别不同的三方应用。​创建 OAuth 应用时会分配 client_id，本示例输入813924812101982004357116497xxxx.app.coze。​  
client_secret​| 客户端密钥，和客户端 ID 配合使用，用于认证应用的身份，确保只有被授权的应用可以请求授权。​创建 OAuth 应用时会分配 client_secret，本示例输入8jmSA1wi********。​  
client_url​| 服务方的 OAuth 页面URL，用于拼接用户登录授权页的URL。​用户登录插件时，扣子编程会将用户引导至"[client_url]?response_type=code&client_id=[client_id]&scope=[scope]&state=xyz123&redirect_uri=[coze平台的回调安全地址]。​参考服务方的授权文档获取 client_url ，本示例参考扣子编程开发指南文档，输入https://www.coze.cn/api/permission/oauth2/authorize，详情请参考​2 获取访问令牌。​  
scope​| 允许应用程序请求访问用户数据的范围。​参考服务方的授权文档输入 scope。​  
authorization_url​| 获取用户 access token 的 URL 地址。​用户通过client_url授权成功后，三方服务会返回用于获取 token 的 code，并跳转至回调地址。此时，服务提供方会通过对应参数向authorization_url发起请求，获取用户的access_token。​参考服务方的授权文档获取 authorization_url，本示例参考扣子编程开发指南文档，输入https://api.coze.cn/api/permission/oauth2/token，详情请参考​2 获取访问令牌。​  
authorization_content_type​| 向 OAuth 提供者发送数据的内容类型，目前支持：​
    * （默认）application/json​
    * application/x-www-form-urlencoded​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27367%27%20height=%27453%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY3IiBoZWlnaHQ9IjQ1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击未授权，然后单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27515%27%20height=%27288%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE1IiBoZWlnaHQ9IjI4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在授权页，单击授权即可完成 OAuth 授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27324%27%20height=%27428%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI0IiBoZWlnaHQ9IjQyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

授权成功后，无论是插件调试还是与智能体对话，每次请求调用插件时，用户授权的 access_token 都会在 header 中传递，具体传递内容为：“Authorization”:“[Bearer] [user's access_token]”。​

步骤二：配置 OAuth 应用的重定向 URL​

创建插件后，你需要获取插件 ID，用于配置 OAuth 应用的重定向 URL。​

1.

获取插件 ID。​

  * 在插件详情页面的 URL 中，获取插件 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27559%27%20height=%2791%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU5IiBoZWlnaHQ9IjkxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

返回[OAuth 应用](<https://www.coze.cn/open/oauth/apps>)页面，单击目标 OAuth 应用对应的编辑。​

3.

输入重定向 URL，单击确定。​

  * 重定向 URL 格式为https://www.coze.cn/api/plugin_oauth/753316160413368****/authorization_code ，其中 753316160413368**** 为插件 ID，需替换为你在步骤 1 中获取到的插件 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27481%27%20height=%27339%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgxIiBoZWlnaHQ9IjMzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：创建工具​

创建插件后，还需要创建工具，以实现将目标 API 添加到插件中作为工具使用。具体操作，请参考​步骤二：添加工具。​

下图以扣子编程的[查看智能体列表](<https://www.coze.cn/docs/developer_guides/published_bots_list>) API 为例，展示了工具的配置示例。配置完成后，需单击右上角的试运行。只有当添加的工具试运行通过后，才能发布插件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27627%27%20height=%27344%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI3IiBoZWlnaHQ9IjM0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：发布插件​

发布 OAuth 插件。插件发布后，才可以被智能体使用。具体操作，请参考​步骤三：发布插件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27631%27%20height=%27131%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMxIiBoZWlnaHQ9IjEzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

授权配置​

你在低代码智能体、工作流中使用 OAuth 插件时，需要完成授权操作，以确保智能体或工作流在调用 OAuth 插件时可以正常运行。详细说明，请参考​为什么插件提示未授权？、​如何设置 OAuth 插件的授权模式？。​

​

上一篇

创建私网模式插件

下一篇

OIDC 插件配置教程