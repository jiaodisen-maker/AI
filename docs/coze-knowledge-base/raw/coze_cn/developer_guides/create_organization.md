---
source_url: https://docs.coze.cn/developer_guides/create_organization
title: '创建组织 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:20:06Z
---

# 创建组织 - 文档 - 扣子

创建组织

在指定的企业中创建组织。​

接口限制​

  * 套餐限制：扣子企业旗舰版。​

  * 数量限制：一个企业中最多存在 20 个组织。​

基础信息​

​

请求方式​| POST​  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v1/enterprises/:enterprise_id/organizations​​  
权限​| Enterprise.createOrganization​确保调用该接口使用的访问令牌开通了企业特权应用中的 Enterprise.createOrganization 权限，详细信息参考[OAuth JWT 授权（企业特权应用）](<https://docs.coze.cn/developer_guides/oauth_jwt_privilege>)。​  
接口说明​| 在指定的企业中创建组织。​  
  
​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息参考[OAuth JWT 授权（企业特权应用）](<https://docs.coze.cn/developer_guides/oauth_jwt_privilege>)。​  
Content-Type​| application/json​| 解释请求正文的方式。​  
  
​

Path​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
enterprise_id​| String​| 必选​| volcano_210195***​| 企业 ID，用于标识该组织所属的企业。​你可以在组织管理 > 组织设置页面查看企业 ID。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27384.94623655913983%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM4NC45NDYyMzY1NTkxMzk4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

Body​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
name​| String​| 必选​| 研发部​| 自定义组织的名称。​最大长度为 30 个字符。​  
super_admin_user_id​| String​| 必选​| 411345614833****​| 指定组织的超级管理员的扣子用户 UID。​你可以调用火山引擎的 [ListCozeUser-成员列表](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=ListCozeUser>) API，CozeUserId 的值即为扣子用户 UID。​说明只有已加入企业的员工能被指定为组织的超级管理员。​​  
description​| String​| 可选​| 研发部内部使用的组织​| 自定义组织的描述信息，最大长度为 100 个字符。默认为空。​  
  
​

返回参数​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
code​| Long​| 0​| 调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。​  
msg​| String​| ""​| 状态信息。API 调用失败时可通过此字段查看详细错误信息。​状态码为 0 时，msg 默认为空。​  
data​| Object of [CreateOrganizationData](<https://docs.coze.cn/developer_guides/create_organization#createorganizationdata>)​| {"organization_id":"74908881444562***"}​| 返回的组织信息。​  
detail​| Object of [ResponseDetail](<https://docs.coze.cn/developer_guides/create_organization#responsedetail>)​| {"logid":"20241210152726467C48D89D6DB2****"}​| 包含本次请求的详细信息，主要用于异常报错场景下的问题排查。​  
  
​

CreateOrganizationData​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
organization_id​| String​| 74908881444562***​| 组织 ID。​  
  
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

curl --location --request POST 'https://api.coze.cn/v1/enterprises/volcano_210195***/organizations' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type : application/json' \​

\--data-raw '{​

"name": "研发部",​

"super_admin_user_id": "411345614833****",​

"description": "研发部内部使用的组织"​

}'​

​

返回示例​

​

JSON

复制

{​

"code": 0,​

"msg": "",​

"data": {​

"organization_id": "74908881444562***"​

},​

"detail": {​

"logid": "20241210152726467C48D89D6DB2****"​

}​

}

​

错误码​

如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考[错误码](<https://docs.coze.cn/developer_guides/coze_error_codes>)文档查看对应的解决方法。​

上一篇

移除企业成员

下一篇

修改组织基本信息