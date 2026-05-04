---
source_url: https://docs.coze.cn/developer_guides/python_access_token
title: '配置访问密钥 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:25:17Z
---

# 配置访问密钥 - 文档 - 扣子

配置访问密钥

通过 Python SDK 方式调用扣子编程 OpenAPI 时，需要在 SDK 请求中配置访问密钥，用于身份信息认证和权限校验。扣子编程 OpenAPI 提供个人访问密钥和 OAuth 两种鉴权方式，你可以选择当前业务场景适合的鉴权方式，并获取对应的访问密钥。​

对于 OAuth 授权码等授权方式，Coze Python SDK 已经封装了这部分代码，并处理了不同的返回错误代码，简化你的操作。​

配置方式​

扣子编程 OpenAPI 目前支持的鉴权方式如下。​

​

访问密钥类型​| 鉴权方式​| 说明​| 示例文件​  
---|---|---|---  
个人访问密钥（PAT）​| 个人访问密钥（PAT）​| Personal Access Token，简称 PAT。扣子编程中生成的个人访问令牌。PAT 生成与使用便捷，适用于测试环境调试等场景。每个令牌可以关联多个空间，并开通指定的接口权限。生成方式可参考​添加个人访问令牌。​| [examples/](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_pat.py>)[auth_pat.py](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_pat.py>)​  
服务访问令牌（SAT）​| 服务访问令牌（SAT）​| Service Access Token（简称 SAT）是以服务身份创建的访问凭证，可长期有效访问扣子编程资源，通常用于服务/应用程序的身份验证和授权。生成方式可参考​添加服务访问令牌。​SAT 的示例代码与 PAT 通用，可直接参考 PAT 的示例文件。​| [examples/](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_pat.py>)[auth_pat.py](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_pat.py>)​  
OAuth 认证​​| 授权码授权 ​（Authorization Code Flow） ​| 适用于有显著前后端之分的应用程序授权场景。其中前端模块负责与用户交互，后端服务处理前端请求，与扣子编程授权服务器和 OpenAPI 交互。 实现流程可参考​OAuth 授权码授权。​| [examples/](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_web.py>)[auth_oauth_web.py](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_web.py>)​  
​| PKCE 授权 ​（Authorization Code Flow with PKCE） ​| 应用程序无后端服务，所有操作都发生在应用程序的前端。 实现流程可参考​OAuth PKCE。​| [examples/](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_pkce.py>)[auth_oauth_pkce.py](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_pkce.py>)​  
​| 设备码授权 ​（Device Code Flow） ​| 应用程序无后端服务，所有操作都发生在应用程序的 Command Line，且 Command Line 无法提供“同意授权”的操作。 实现流程可参考​OAuth 设备授权。​| [examples/](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_device.py>)[auth_oauth_device.py](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_device.py>)​  
​| JWT 授权 ​（JWT Flow） ​| 应用程序服务端直接调用扣子编程 OpenAPI。 ​应用程序后端服务代理应用程序自己的用户获取身份凭据，应用程序用户基于凭据直接访问 OpenAPI。 实现流程可参考​OAuth JWT 授权（开发者）。​| [examples/](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_jwt.py>)[auth_oauth_jwt.py](<https://github.com/coze-dev/coze-py/blob/main/examples/auth_oauth_jwt.py>)​  
  
​

配置个人访问密钥（PAT）​

如果选择使用个人访问密钥鉴权，你需要先申请一个个人访问密钥，并添加指定空间和权限。操作步骤可参考[添加个人访问令牌](<https://www.coze.cn/docs/developer_guides/pat>)。​

扣子编程建议你通过环境变量的方式管理访问密钥，避免在代码中通过硬编码方式进行编程，以免密钥泄露、引发安全风险。配置环境变量之后，您可以在不修改代码的情况下，将动态的鉴权参数传递到对应的函数，实现便捷安全的身份认证。​

1.

设置环境变量。​

  * 其中 COZE_API_TOKEN 是扣子编程中申请的个人访问密钥。关于环境变量的详细说明可参考 [Python 官方文档](<https://docs.python.org/zh-cn/3/using/windows.html#excursus-setting-environment-variables>)。​

  * ​

Shell

复制

export COZE_API_TOKEN="pat_****"​

​

2.

初始化客户端。​

  * 示例代码如下：​

  * ​

Python

复制

import os​

​

from cozepy import Coze, TokenAuth, COZE_CN_BASE_URL​

​

# 通过环境变量引入密钥，访问 coze.cn 服务​

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")), base_url=COZE_CN_BASE_URL)​

​

配置 OAuth 授权码流程​

如果选择使用 OAuth 授权码方式完成授权，可参考以下流程及示例代码。​

1.

创建 OAuth 应用。​

  * 具体操作步骤可参考​OAuth 授权码授权。成功创建 OAuth 应用后，你将获得客户端 ID、客户端密钥和重定向地址。你需要妥善保管客户端密钥，以免数据泄露引发安全风险。​

2.

在代码中通过环境变量方式设置客户端 ID、客户端密钥和重定向地址。​

  * ​

Python

复制

import os​

from cozepy import Coze, TokenAuth, WebOAuthApp, COZE_CN_BASE_URL​

​

# Auth应用的客户端ID，创建 OAuth 应用时获取的客户端 ID。 ​

web_oauth_client_id = os.getenv("COZE_WEB_OAUTH_CLIENT_ID")​

# 客户端密钥​

web_oauth_client_secret = os.getenv("COZE_WEB_OAUTH_CLIENT_SECRET")​

​

# 访问 coze.cn 服务​

web_oauth_app = WebOAuthApp(​

client_id=web_oauth_client_id,​

client_secret=web_oauth_client_secret,​

base_url=COZE_CN_BASE_URL,​

)​

​

3.

授权码流程中，会自动生成一个扣子编程授权页面，然后将其发送给需要授权的用户。扣子用户可访问此链接，并根据页面提示完成授权流程。​

  * ​

Python

复制

# redirect link​

web_oauth_redirect_uri = os.getenv("COZE_WEB_OAUTH_REDIRECT_URI")​

​

# Generate the authorization link and direct the user to open it.​

url = web_oauth_app.get_oauth_url(redirect_uri=web_oauth_redirect_uri)​

​

4.

用户点击同意授权按钮后，扣子网页会将请求重定向到授权链接中配置的重定向地址，并通过 Query 在地址中携带授权码和状态参数。​

  * 通过授权码（OAuth code）调用 OpenAPI 接口即可获取 OAuth Access Token。示例代码如下：​

  * ​

Python

复制

# Open the authorization link in your browser and authorize this OAuth App​

# After authorization, you will be redirected to the redirect_uri with a code and state​

# You can use the code to get the access token​

code = 'mock code'​

​

# After obtaining the code after redirection, the interface to exchange the code for a​

# token can be invoked to generate the coze access_token of the authorized user.​

oauth_token = web_oauth_app.get_access_token(redirect_uri=web_oauth_redirect_uri, code=code)​

​

# use the access token to init Coze client​

coze = Coze(auth=TokenAuth(oauth_token.access_token), base_url=COZE_CN_BASE_URL)​

​

# When the token expires, you can also refresh and re-obtain the token​

oauth_token = web_oauth_app.refresh_access_token(oauth_token.refresh_token)​

​

配置 OAuth PKCE 授权流程​

如果选择使用 OAuth PKCE 方式完成授权，可参考以下流程及示例代码。​

1.

创建 OAuth 应用。​

  * 具体操作步骤可参考​OAuth PKCE。成功创建 OAuth 应用后，你将获得客户端 ID 和重定向地址。​

2.

在代码中通过环境变量方式设置客户端 ID 和重定向地址。​

  * ​

Python

复制

import os​

​

from cozepy import PKCEOAuthApp, COZE_CN_BASE_URL​

​

# OAuth应用的客户端ID，创建 OAuth 应用时获取的客户端 ID。 ​

pkce_oauth_client_id = os.getenv("COZE_PKCE_OAUTH_CLIENT_ID")​

# 重定向地址，创建 OAuth 应用时指定的重定向 URL。 ​

pkce_oauth_redirect_uri = os.getenv("COZE_WEB_OAUTH_REDIRECT_URI") ​

​

pkce_oauth_app = PKCEOAuthApp(client_id=pkce_oauth_client_id, base_url=COZE_CN_BASE_URL)​

​

3.

在代码中实现 OAuth PKCE 授权流程、​

  * 客户端生成一个随机值 code_verifier，并根据指定算法将其转换为 code_challenge，算法通常使用 SHA-256 算法。然后基于回调地址、code_challenge 和 code_challenge_method，生成一个授权链接。​

  * ​

Python

复制

# In the SDK, we have wrapped up the code_challenge process of PKCE. Developers only need​

# to select the code_challenge_method.​

code_verifier = "random code verifier"​

url = pkce_oauth_app.get_oauth_url(​

redirect_uri=web_oauth_redirect_uri,​

code_verifier=code_verifier,​

code_challenge_method="S256"​

)​

​

4.

完成授权。​

  * 开发者应该引导用户打开这个授权链接。当用户同意授权时，扣子编程会将页面重定向到开发者配置的回调地址，开发者可以获取这个 code，换取访问密钥。​

  * ​

Python

复制

# Open the authorization link in your browser and authorize this OAuth App​

# After authorization, you can exchange code_verifier for access token​

code = 'mock code'​

​

# After obtaining the code after redirection, the interface to exchange the code for a​

# token can be invoked to generate the coze access_token of the authorized user.​

oauth_token = pkce_oauth_app.get_access_token(​

redirect_uri=web_oauth_redirect_uri, code=code, code_verifier=code_verifier​

)​

​

# use the access token to init Coze client​

coze = Coze(auth=TokenAuth(oauth_token.access_token), base_url=COZE_CN_BASE_URL)​

​

# When the token expires, you can also refresh and re-obtain the token​

oauth_token = pkce_oauth_app.refresh_access_token(oauth_token.refresh_token)​

​

配置 OAuth 设备码授权流程​

如果选择使用 OAuth 设备码方式完成授权，可参考以下流程及示例代码。​

1.

创建 OAuth 应用。​

  * 具体操作步骤可参考​OAuth 设备授权。成功创建 OAuth 应用后，你将获得客户端 ID。​

2.

在代码中通过环境变量方式设置客户端 ID。​

  * ​

Python

复制

import os​

from cozepy import Coze, TokenAuth, DeviceOAuthApp, COZE_CN_BASE_URL​

​

# OAuth应用的客户端ID，创建 OAuth 应用时获取的客户端 ID。​

device_oauth_client_id = os.getenv("COZE_DEVICE_OAUTH_CLIENT_ID")​

​

device_oauth_app = DeviceOAuthApp(client_id=device_oauth_client_id, base_url=COZE_CN_BASE_URL)​

​

3.

通过 OAuth 设备码授权流程获得访问密钥。​

  * 应用程序需要调用扣子编程 OpenAPI 生成设备代码，以获取 user_code 和 device_code。通过 user_code 生成授权链接，并引导用户打开该链接、填写 user_code、同意授权。应用程序调用扣子编程 OpenAPI，通过 device_code 生成访问密钥。​

  * 如果用户尚未授权或拒绝了授权，接口将抛出异常并返回特定的错误代码。用户同意授权后，接口将成功并返回访问密钥。​

  * ​

Python

复制

# First, you need to request the server to obtain the device code required in the device auth flow​

device_code = device_oauth_app.get_device_code()​

​

# The returned device_code contains an authorization link. Developers need to guide users​

# to open up this link.​

# open device_code.verification_url​

​

4.

应用程序还需要使用 device_code 来轮询扣子编程 OpenAPI 以获取访问密钥。​

  * Coze Python SDK已经封装了这部分代码，并处理了不同的返回错误代码。开发者只需要调用 get_access_token 即可。​

  * ​

Python

复制

try:​

oauth_token = device_oauth_app.get_access_token(​

device_code=device_code.device_code,​

poll=True,​

)​

except CozePKCEAuthError as e:​

if e.error == CozePKCEAuthErrorType.ACCESS_DENIED:​

# The user rejected the authorization.​

# Developers need to guide the user to open the authorization link again.​

pass​

elif e.error == CozePKCEAuthErrorType.EXPIRED_TOKEN:​

# The token has expired. Developers need to guide the user to open​

# the authorization link again.​

pass​

else:​

# Other errors​

pass​

​

raise # for example, re-raise the error​

​

# use the access token to init Coze client​

coze = Coze(auth=TokenAuth(oauth_token.access_token), base_url=COZE_CN_BASE_URL)​

​

# When the token expires, you can also refresh and re-obtain the token​

oauth_token = device_oauth_app.refresh_access_token(oauth_token.refresh_token)​

​

配置 OAuth JWT 授权流程​

如果选择使用 OAuth JWT 方式完成授权，可参考以下流程及示例代码。​

1.

创建 OAuth 应用并授权。​

  * 具体操作步骤可参考​OAuth JWT 授权（开发者）。成功创建 OAuth 应用后，你将获得客户端 ID、公钥和私钥。你需要妥善保管公钥和私钥，以免数据泄露引发安全风险。​

2.

在代码中通过环境变量方式设置客户端 ID、公钥和私钥。​

  * ​

Python

复制

import os​

from cozepy import Coze, TokenAuth, JWTOAuthApp, COZE_CN_BASE_URL​

​

# OAuth应用的客户端ID，创建 OAuth 应用时获取的客户端 ID。​

jwt_oauth_client_id = os.getenv("COZE_JWT_OAUTH_CLIENT_ID")​

# OAuth 应用的私钥，创建 OAuth 应用时获取的私钥。​

jwt_oauth_private_key = os.getenv("COZE_JWT_OAUTH_PRIVATE_KEY")​

# OAuth 应用的公钥指纹，可以在 [OAuth 应用](<https://www.coze.cn/open/oauth/apps>)页面找到这个应用，在操作列单击编辑图标，进入配置页面查看公钥指纹。​

jwt_oauth_public_key_id = os.getenv("COZE_JWT_OAUTH_PUBLIC_KEY_ID")​

​

jwt_oauth_app = JWTOAuthApp(​

client_id=jwt_oauth_client_id,​

private_key=jwt_oauth_private_key,​

public_key_id=jwt_oauth_public_key_id,​

base_url=COZE_CN_BASE_URL​

)​

​

3.

应用程序通过公钥和私钥签署 JWT，并通过扣子编程提供的 API 获取访问密钥。​

  * Coze Python SDK 封装了这一过程，你只需要在OAuth JWT 流程中使用 get_access_token 来获取访问密钥即可。​

  * ​

Python

复制

# The jwt process does not require any other operations, you can directly apply for a token​

oauth_token = jwt_oauth_app.get_access_token(ttl=3600)​

​

# use the access token to init Coze client​

coze = Coze(auth=TokenAuth(oauth_token.access_token), base_url=COZE_CN_BASE_URL)​

​

# The jwt oauth process does not support refreshing tokens. When the token expires,​

# just directly call get_access_token to generate a new token.​

​

上一篇

安装 Python SDK

下一篇

快速开始