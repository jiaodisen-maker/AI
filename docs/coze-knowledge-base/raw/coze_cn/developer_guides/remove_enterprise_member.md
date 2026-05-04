---
source_url: https://docs.coze.cn/developer_guides/remove_enterprise_member
title: '移除企业成员 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:20:04Z
---

# 移除企业成员 - 文档 - 扣子

移除企业成员

移除企业成员，并指定资源接收人。​

接口限制​

  * 套餐限制：扣子企业版（企业标准版、企业旗舰版）。​

  * 需要先调用[移除组织成员 ](<https://docs.coze.cn/developer_guides/remove_organization_member>)API 将用户从所有组织中移除，再执行本 API 将其移出企业。​

  * 被移除成员的资源只能转移给企业超级管理员或企业管理员。​

说明

  * 每次请求只能移除一位成员。如需移除多位成员，请依次发送请求。​

  * 该 API 不支持并发请求。​

​

基础信息​

​

请求方式​| DELETE​  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v1/enterprises/:enterprise_id/members/:user_id​​  
权限​| Enterprise.removePeople​确保调用该接口使用的访问令牌开通了企业特权应用中的 Enterprise.removePeople 权限，详细信息参考[OAuth JWT 授权（企业特权应用）](<https://docs.coze.cn/developer_guides/oauth_jwt_privilege>)。​  
接口说明​| 移除企业成员。​  
  
​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考[准备工作](<https://docs.coze.cn/developer_guides/preparation>)。​  
Content-Type​| application/json​| 解释请求正文的方式。 ​  
  
​

Path​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
enterprise_id​| String​| 必选​| volcano_210195***​| 需要移除用户的企业 ID。​你可以在组织管理 > 组织设置页面查看企业 ID。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27384.94623655913983%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM4NC45NDYyMzY1NTkxMzk4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
user_id​| String​| 必选​| 247877439325****​| 需要移除的扣子用户 UID。​你可以调用火山引擎的 [ListCozeUser-成员列表](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=ListCozeUser>) API，查看 CozeUserId 的值即为扣子用户 UID。​  
  
​

Body​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
receiver_user_id​| String​| 必选​| 41134548551****​| 接收被移除成员资源的扣子用户 UID，需填写企业超级管理员或管理员的用户 UID。被移除成员的工作空间、智能体、工作流等资源将转移给该用户。​获取企业超级管理员或管理员用户 UID 的方法如下：​

1.在企业管理 > 成员管理页面查看企业的超级管理员或管理员信息。​

2.企业的超级管理员或管理员在扣子编程左下角单击头像，选择账号设置，查看账号的 UID。​
  
  
​

返回参数​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
code​| Long​| 0​| 调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。​  
msg​| String​| ""​| 状态信息。API 调用失败时可通过此字段查看详细错误信息。​状态码为 0 时，msg 默认为空。​  
detail​| Object of [ResponseDetail](<https://docs.coze.cn/developer_guides/remove_enterprise_member#responsedetail>)​| {"logid":"20241210152726467C48D89D6DB2****"}​| 包含请求的详细信息的对象，主要用于记录请求的日志 ID 以便于排查问题。​  
  
​

ResponseDetail​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
logid​| String​| 20241210152726467C48D89D6DB2****​| 本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考[获取帮助和技术支持](<https://docs.coze.cn/guides/help_and_support>)。​  
  
​

示例​

请求示例​

​

JSON

复制

curl --location --request DELETE 'https://api.coze.cn/v1/enterprises/volcano_210195***/members/247877439325****' \​

\--header 'Authorization: Bearer pat_O******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"receiver_user_id": "41134548551****"​

}'​

​

返回示例​

​

JSON

复制

{​

"code": 0,​

"msg": "",​

"detail": {​

"logid": "20241210152726467C48D89D6DB2****"​

}​

}

​

错误码​

如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考[错误码](<https://docs.coze.cn/developer_guides/coze_error_codes>)文档查看对应的解决方法。​

上一篇

修改企业员工的角色

下一篇

创建组织