---
source_url: https://docs.coze.cn/tutorial/set_sso_relaystate
title: '配置 SSO 登录后跳转至扣子编程指定页面 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:10Z
---

# 配置 SSO 登录后跳转至扣子编程指定页面 - 文档 - 扣子

配置 SSO 登录后跳转至扣子编程指定页面

通过在单点登录（SSO）配置中传递特定参数，实现用户登录后直接跳转到扣子编程指定页面，例如某个工作空间或者智能体。通过精确的登录后跳转，可以无缝优化用户登录体验，提升工作效率。​

功能介绍​

SSO 登录支持 SAML 和 OAuth 两种主流 SSO 协议。你可以通过构造 RelayState（SAML）或 state（OAuth）参数来携带跳转路径信息，在用户完成身份验证后，将其重定向至预设的 URL。​

前提条件​

已​配置单点登录（SSO）。​

SAML SSO 登录​

通过构造 RelayState 参数携带跳转路径信息，实现登录后直达扣子编程指定页面，操作步骤如下：​

1.

拼接 RelayState 参数。​

  * RelayState 参数的格式如下：​

  * ​

TypeScript

复制

// 字符串中的域名和client_id为固定值，请勿修改​

// js代码示例​

const RelayState ='redirect_uri=' \+ encodeURIComponent('https://signin-saas.volccloudidentity.com/api/cloudidentity/authorize/federateOAuth?client_id=9836804098&state=' \+ encodeURIComponent(`{"platform":"eps_cloud_identity","navigatePath":"${需要替换的path}","type":"login"}`)​

\+ '&response_type=code&redirect_uri=' \+ encodeURIComponent('https://www.coze.cn/auth/callback'))​

​

  * 通过修改 state 参数中 navigatePath 的值、执行两次 URL 编码、拼接至 RelayState，即可得到 RelayState 参数的值。具体流程与示例如下表所示：​

  * ​

拼接流程​| 主页​| 工作空间​| 工作空间中的智能体​  
---|---|---|---  
1.在state参数的navigatePath字段中配置 SSO 跳转的目标页面。​| {"platform":"eps_cloud_identity","navigatePath":"/home","type":"login"}​| {"platform":"eps_cloud_identity","navigatePath":"/space","type":"login"}​| {"platform":"eps_cloud_identity","navigatePath":"/space/7436975598481899583/bot/754166928014542***5","type":"login"}​  
2.使用在线 URL 编码工具对 state 中的 JSON 字符串执行两次 URL 编码。​​| %257B%2522platform%2522%253A%2522eps_cloud_identity%2522%252C%2522navigatePath%2522%253A%2522%252Fhome%2522%252C%2522type%2522%253A%2522login%2522%257D​| %257B%2522platform%2522%253A%2522eps_cloud_identity%2522%252C%2522navigatePath%2522%253A%2522%252Fspace%2522%252C%2522type%2522%253A%2522login%2522%257D​| %257B%2522platform%2522%253A%2522eps_cloud_identity%2522%252C%2522navigatePath%2522%253A%2522%252Fspace%252F7436975598481899583%252Fbot%252F7541669280145****%2522%252C%2522type%2522%253A%2522login%2522%257D​  
3.将编码后的值拼接到 RelayState 参数中。​| redirect_uri=https%3A%2F%2Fsignin-saas.volccloudidentity.com%2Fapi%2Fcloudidentity%2Fauthorize%2FfederateOAuth%3Fclient_id%3D9836804098%26state%3D%257B%2522platform%2522%253A%2522eps_cloud_identity%2522%252C%2522navigatePath%2522%253A%2522%252Fhome%2522%252C%2522type%2522%253A%2522login%2522%257D%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.coze.cn%252Fauth%252Fcallback%26scenario%3Dcoze​| redirect_uri=https%3A%2F%2Fsignin-saas.volccloudidentity.com%2Fapi%2Fcloudidentity%2Fauthorize%2FfederateOAuth%3Fclient_id%3D9836804098%26state%3D%257B%2522platform%2522%253A%2522eps_cloud_identity%2522%252C%2522navigatePath%2522%253A%2522%252Fspace%2522%252C%2522type%2522%253A%2522login%2522%257D%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.coze.cn%252Fauth%252Fcallback%26scenario%3Dcoze​| redirect_uri=https%3A%2F%2Fsignin-saas.volccloudidentity.com%2Fapi%2Fcloudidentity%2Fauthorize%2FfederateOAuth%3Fclient_id%3D9836804098%26state%3D%257B%2522platform%2522%253A%2522eps_cloud_identity%2522%252C%2522navigatePath%2522%253A%2522%252Fspace%252F7436975598481899583%252Fbot%252F75416692****5%2522%252C%2522type%2522%253A%2522login%2522%257D%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.coze.cn%252Fauth%252Fcallback%26scenario%3Dcoze​  
  
​

2.

将拼接好的 RelayState 参数的值配置至 IdP 平台的登录跳转地址中：​

  * ​

TypeScript

复制

// js代码示例​

// POST方式​

{"RelayState": `${RelayStateString}`}​

​

//Redirect方式​

`&RelayState=${encodeURIComponent(RelayStateString)}`​

​

OAuth SSO 登录​

通过构造并传递 state 参数携带跳转路径信息，实现登录后直达扣子编程指定页面，操作步骤如下：​

1.

构造一个 coze_state JSON 对象。​

a.

按以下示例构造coze_state JSON 对象，用于指定扣子编程的目标跳转页面。​

  * ​

JavaScript

复制

const coze_state = '{"platform":"eps_cloud_identity","navigatePath":"/space","type":"login"}'​

​

  * 参数说明如下：​

  * ​

参数​| 说明​  
---|---  
platform​| 平台标识，固定值为eps_cloud_identity。​  
navigatePath​| 扣子编程的目标页面路径。取值如下：​
    * /home：主页​
    * /space：工作空间​
    * /space/74****/bot/75****：工作空间下的某个智能体​
说明如果路径中包含传参，需要进行 encodeURIComponent 编码。​​  
type​| 操作类型，固定值为login。​  
  
​

b.

将上一步生成的coze_state JSON 字符串进行encodeURIComponent编码。​

2.

构造 redirect_uri。​

a.

将云身份中心实例名、client_id 、编码后的coze_state等参数填入模板。​

  * ​

TypeScript

复制

const redirect_uri = `https://${instance_name}.volccloudidentity.com/api/cloudidentity/authorize/federateOAuth?client_id=9836804098&state=${encodeURIComponent(coze_state)}&response_type=code&redirect_uri=https%3A%2F%2Fwww.coze.cn%2Fauth%2Fcallback&scenario=coze`​

​

  * ​

    * 参数​
| 说明​  
---|---  
instance_name​| 云身份中心实例名称。​  
client_id​| 云身份中心的client_id，固定值为9836804098。​  
state​| 步骤 1 中生成的编码后的 coze_state 字符串。​  
response_type​| 响应类型，固定值为 code。​  
redirect_uri​| 扣子编程的回调地址，固定值为 https%3A%2F%2Fwww.coze.cn%2Fauth%2Fcallback。​  
scenario​| 场景标识，固定值为 coze。​  
  
​

b.

对整个redirect_uri再执行一次 URL 编码，得到encodeURIComponent(redirect_uri)。​

3.

构造state参数。​

  * 将编码后的redirect_uri作为值，拼接到redirect_uri=前缀后，再执行一次 URL 编码，得到最终用于 OAuth 请求的state参数：​

  * ​

TypeScript

复制

const state = encodeURIComponent('redirect_uri=' \+ encodeURIComponent(redirect_uri))​

​

4.

构造完整的 SSO 登录地址。​

  * 将云身份中心EntityID和最终的state参数填入地址模板：​

  * ​

TypeScript

复制

https://signin.volcengine.com/cloud-identity/cn-beijing/${entity_id}/userlogin/oauth/sso?state=${state}​

​

  * 用户访问该地址，即可完成 OAuth SSO 登录并直接跳转扣子编程指定页面。​

​

​

上一篇

通过飞书进行 SAML SSO 登录

下一篇

迁移至企业版