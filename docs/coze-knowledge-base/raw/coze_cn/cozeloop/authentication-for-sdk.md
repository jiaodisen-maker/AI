---
source_url: https://docs.coze.cn/cozeloop/authentication-for-sdk
title: 'SDK 鉴权 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:02Z
---

# SDK 鉴权 - 文档 - 扣子

SDK 鉴权

在使用扣子罗盘 SDK 前，需要进行身份验证和权限校验。扣子罗盘支持个人访问密钥（PAT）、服务访问令牌（SAT）和 OAuth JWT 三种授权方式。​

配置个人访问令牌​

个人访问令牌（Personal Access Token，简称 PAT）是平台提供的短效令牌。PAT 生成与使用便捷，适用于测试环境调试场景。PAT 有效期支持最长 30 天，每个令牌可以关联多个空间，并开通指定的接口权限。​

参考以下步骤，创建并配置个人访问令牌。​

说明

如果要使用已创建的 PAT，在个人访问令牌列表页面，单击对应的编辑图标，然后选择罗盘相关权限即可。​

​

1.

登录[扣子罗盘](<https://loop.coze.cn>)。​

2.

在左侧菜单栏，选择 SDK&API > 授权。​

3.

单击个人访问令牌页签，然后单击添加。​

4.

在弹出的对话框内，完成以下配置，然后单击确定。​

  * 名称：输入令牌名称。​

  * 过期时间：选择令牌的有效期，最长可选 30 天。​

  * 权限：找到罗盘选项后，选择对应权限。​

  * 访问空间：选择该令牌生效的空间范围。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27266%27%20height=%27321%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fec5a9515ff54ce3b2cfb948a446565b~tplv-goo7wpa0wc-quality:q75.image)​

​

5.

复制并保存显示的个人访问令牌。​

在获取个人访问令牌后，建议通过环境变量来管理访问密钥，以避免在代码中硬编码，从而防止密钥泄露和潜在的安全风险。配置环境变量后，你可以在不修改代码的情况下将动态的授权参数传递到相应的函数中，从而实现便捷且安全的身份认证。​

​

Shell

复制

export COZELOOP_WORKSPACE_ID=740********​

export COZELOOP_API_TOKEN=pat_****​

​

其中：​

  * COZELOOP_WORKSPACE_ID 是扣子罗盘的空间 ID。获取方式参见 ​获取扣子罗盘空间 ID。​

  * COZELOOP_API_TOKEN 是已生成的个人访问令牌。​

配置服务访问令牌​

服务访问令牌（Service Access Token，简称 SAT）是以服务身份创建的长效令牌，用于服务/应用程序的身份验证和授权。服务访问令牌的有效期可设置为永久，适合需要长期稳定的身份验证场景。​

参考以下步骤，创建并配置服务访问令牌。​

说明

如果要使用已创建的 SAT，在服务身份及凭证列表页面，单击对应的编辑图标，然后选择罗盘相关权限即可。​

​

1.

登录[扣子罗盘](<https://loop.coze.cn>)。​

2.

在左侧菜单栏，选择 SDK&API > 授权。​

3.

单击服务身份及凭证页签，然后单击添加。​

4.

在弹出的对话框内，完成以下配置，然后单击确定。​

  * 名称：输入令牌名称。​

  * 过期时间：选择令牌的有效期，最长可设置为长期有效。​

  * 权限：找到罗盘选项后，选择对应权限。​

  * 访问空间：选择该令牌生效的空间范围。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27262%27%20height=%27314%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYyIiBoZWlnaHQ9IjMxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在获取服务访问令牌后，建议通过环境变量来管理访问密钥，以避免在代码中硬编码，从而防止密钥泄露和潜在的安全风险。配置环境变量后，你可以在不修改代码的情况下将动态的授权参数传递到相应的函数中，从而实现便捷且安全的身份认证。​

​

Shell

复制

export COZELOOP_WORKSPACE_ID=740********​

export COZELOOP_API_TOKEN=sat_****​

​

其中：​

  * COZELOOP_WORKSPACE_ID 是扣子罗盘的空间 ID。获取方式参见 ​获取扣子罗盘空间 ID。​

  * COZELOOP_API_TOKEN 是已生成的服务访问令牌。​

配置 OAuth JWT 授权​

罗盘 SDK 支持 OAuth JWT 的授权方式来获取和更新访问令牌。详细授权流程，可参考 [OAuth JWT 授权（开发者）](<https://www.coze.cn/open/docs/developer_guides/oauth_jwt>)。​

1.

登录 [CozeLoop](<https://loop.coze.cn>)。​

2.

在左侧菜单栏，选择 SDK&API > 授权。​

3.

在 OAuth 应用页面，单击创建新应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27386%27%20height=%27192%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg2IiBoZWlnaHQ9IjE5MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

输入应用的基本信息，然后单击创建并继续。​

  * 应用类型：OAuth 应用的类型，此处应指定为普通。​

  * 客户端类型：客户端类型，此处设置为服务类应用。​

  * 应用名称：OAuth 应用的名称，在扣子平台中全局唯一。 ​

  * 描述：OAuth 应用的基本描述信息。 ​

5.

在配置页面，单击 \+ 创建 Key，生成公钥和私钥。​

  * 说明

请妥善保管公钥和私钥，以免数据泄露引发安全风险。 ​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27402%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAyIiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

找到罗盘选项后，选择对应权限，然后单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27314%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE0IiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

在弹出的授权确认页面，单击授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27337%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM3IiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

创建完成后，在 OAuth 应用列表复制应用 ID。该 ID 将在集成扣子罗盘 SDK 时使用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272408%27%20height=%27564.70796460177%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQwOCIgaGVpZ2h0PSI1NjQuNzA3OTY0NjAxNzciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

成功创建 OAuth 应用后，你将获得 OAuth 应用 ID、公钥和私钥。建议通过环境变量来管理授权信息，以避免在代码中硬编码，从而防止密钥泄露和潜在的安全风险。配置环境变量后，你可以在不修改代码的情况下将动态的授权参数传递到相应的函数中，从而实现便捷且安全的身份认证。​

​

Bash

复制

export COZELOOP_WORKSPACE_ID=pat_****​

export COZELOOP_JWT_OAUTH_CLIENT_ID=740********​

export COZELOOP_JWT_OAUTH_PRIVATE_KEY=740********​

export COZELOOP_JWT_OAUTH_PUBLIC_KEY_ID=740********​

​

其中：​

  * COZELOOP_WORKSPACE_ID 是扣子罗盘的空间 ID。获取方式参见 ​获取扣子罗盘空间 ID。​

  * COZELOOP_JWT_OAUTH_CLIENT_ID 是已生成的应用 ID。​

  * COZELOOP_JWT_OAUTH_PRIVATE_KEY 是私钥。​

  * COZELOOP_JWT_OAUTH_PUBLIC_KEY_ID 是公钥。​

​

上一篇

SDK 概述

下一篇

快速开始