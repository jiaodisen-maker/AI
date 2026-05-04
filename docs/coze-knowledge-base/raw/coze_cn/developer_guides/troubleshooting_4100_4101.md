---
source_url: https://docs.coze.cn/developer_guides/troubleshooting_4100_4101
title: '错误码 4100/4101 问题排查 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:24:53Z
---

# 错误码 4100/4101 问题排查 - 文档 - 扣子

错误码 4100/4101 问题排查

当调用 API 报错 4100 或 4101 时，表示当前使用的访问密钥不正确，或密钥不具备对应资源的权限。​

问题排查流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27299%27%20height=%27534%27/%3e)![](https://p16-arcosite-va.ibyteimg.com/https://p16-arcosite-va.ibyteimg.com/obj/tos-maliva-i-10qhjjqwgv-us/8ea9c70e32ea42229c585d2209b4b609~tplv-10qhjjqwgv-quality:q75.image)​

​

​

问题排查步骤如下：​

1.

检查访问密钥。​

  * 在此步骤中，检查密钥的权限、有效期和对应的工作空间。​

  * 对于 OAuth 访问密钥，参考​OAuth 应用管理，检查授权流程是否完整且正确。​

  * 对于个人访问密钥（PAT），你可以在[个人访问令牌](<https://www.coze.cn/open/oauth/pats>)页面找到你使用的 PAT，并参考以下方式检查密钥。​

  * ​

检查项​| 说明​  
---|---  
检查密钥权限​| 确认密钥已被授予指定接口要求的权限点，各个接口的权限点要求可参考 API 文档。例如：​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27267%27%20height=%27162%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY3IiBoZWlnaHQ9IjE2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
检查密钥有效期​| 确认密钥未过期、状态为有效。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271230%27%20height=%27320.8695652173913%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIzMCIgaGVpZ2h0PSIzMjAuODY5NTY1MjE3MzkxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
检查密钥工作空间​| 确认密钥授权工作空间中包括你调用的、知识库所在的空间。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27251%27%20height=%27211%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUxIiBoZWlnaHQ9IjIxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​说明如果希望使用的、知识库位于其他人拥有的工作空间中，可以联系空间所有者获取一个有效的密钥。​​  
  
​

2.

检查访问域名和请求 URL。​

  * 通过对应的 API 文档，确认当前使用的访问域名正确、URL 完整，包含了所有必选的请求 Query 参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27388%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg4IiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

检查 Header 的 Authorization 传参。​

  * 确认请求 Header 中 Authorization 参数格式正确、完整、无多余字符。Authorization 参数格式为 Bearer {Access_Token}，例如Bearer pat_***。​

  * 你也可以直接复制文档中的示例，并替换其中的访问密钥。​

  * ​

Shell

复制

curl --location --request GET 'https://api.coze.cn/v1/bot/get_online_info?bot_id=7381****' \​

\--header 'Authorization: Bearer pat_***' \​

​

4.

检查其他必选字段的传参。​

  * 通过对应的 API 文档，确认已正确设置了请求中所有必选的参数。你也可以直接复制文档中的请求示例，并替换其中的参数值。​

5.

对于企业版用户，如果通过以上步骤排查仍未解决问题，可以记录以下错误信息并联系扣子技术支持，我们将协助您排查问题。​

  * Response header 中的 X-Tt-Logid 字段值，例如 20240708143040790E78F9318B35A2910B。你可以在使用 curl 发起请求时通过 -i 参数打印 Response header 完整内容。​

  * Response Body 中的 code、msg 字段值，例如 { "code": 700012006, "msg": "access token invalid" }。​

​

​

上一篇

通过对话接口获取智能体回复

下一篇

如何实现会话隔离