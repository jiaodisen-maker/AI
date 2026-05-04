---
source_url: https://docs.coze.cn/developer_guides/create_workspace
title: '创建工作空间 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:19:36Z
---

# 创建工作空间 - 文档 - 扣子

创建工作空间

创建工作空间。​

基础信息​

​

请求方式​| POST​  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v1/workspaces​​  
权限​| createWorkspace​确保调用该接口使用的访问令牌开通了 createWorkspace 权限，详细信息参考[鉴权方式](<https://docs.coze.cn/developer_guides/authentication>)。​  
接口说明​| 创建工作空间。​  
  
​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Content-Type​| application/json​| 解释请求正文的方式。 ​  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考[准备工作](<https://docs.coze.cn/developer_guides/preparation>)。​  
  
​

Body​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
name​| String​| 必选​| 文档组的工作空间​| 自定义的空间名称，最大长度为 50 个字符。​  
description​| String​| 必选​| 文档组内部使用的工作空间。​| 空间的描述信息，用于详细说明空间的用途或特点，最大长度为 2000 个字符。​  
icon_file_id​| String​| 可选​| 73694959811****​| 作为空间图标的文件 ID。​

  * 未指定文件 ID 时，使用扣子编程默认的工作空间图标。​

  * 如需使用自定义图标，应先通过[上传文件](<https://docs.coze.cn/developer_guides/upload_files>) API 上传本地文件，从接口响应中获取文件 ID。文件 ID 作为空间图标时，有效期为永久有效。​

  
coze_account_id​| String​| 可选​| 749088814445***​| 组织 ID，用于标识工作空间所属的组织。​扣子个人版中，无需设置此参数。​说明默认在个人账号下创建工作空间，如果需要在企业的组织下创建工作空间，你需要传入组织 ID。​你可以在组织设置页面查看对应的组织 ID。​​  
owner_uid​| String​| 可选​| user_1234567890​| 指定空间所有者的扣子用户的 UID。​说明

  * 扣子个人版中，无需设置此参数，默认当前用户为空间所有者。​

  * 扣子企业版（企业标准版、企业旗舰版）中，可以指定 coze_account_id 对应组织中的员工为空间所有者，未指定时默认 Token 的创建者为空间所有者。​

​你可以单击扣子编程左下角的头像，选择账号设置，在页面底部查看扣子用户的 UID。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27341.90751445086704%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUwIiBoZWlnaHQ9IjM0MS45MDc1MTQ0NTA4NjcwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

返回参数​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
data​| Object of [OpenCreateSpaceRet](<https://docs.coze.cn/developer_guides/create_workspace#opencreatespaceret>)​| {"id":"753232939603****"}​| 工作空间的相关信息。​  
code​| Long​| 0​| 调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。​  
msg​| String​| ""​| 状态信息。API 调用失败时可通过此字段查看详细错误信息。​状态码为 0 时，msg 默认为空。​  
detail​| Object of [ResponseDetail](<https://docs.coze.cn/developer_guides/create_workspace#responsedetail>)​| {"logid":"20241210152726467C48D89D6DB2****"}​| 包含请求的详细信息的对象，主要用于记录请求的日志 ID 以便于排查问题。​  
  
​

OpenCreateSpaceRet​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
id​| String​| 753232939603****​| 创建的工作空间的 ID。​  
  
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

curl --location --request POST 'https://api.coze.cn/v1/workspaces' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"name": "文档组的工作空间",​

"description": "文档组内部使用的工作空间。",​

"icon_file_id": "73694959811****",​

"coze_account_id": "749088814445***",​

}'​

​

返回示例​

​

JSON

复制

{​

"data": {​

"id": "753232939603****"​

},​

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

智能体下架回调事件

下一篇

查看空间列表