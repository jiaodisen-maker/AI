---
source_url: https://docs.coze.cn/developer_guides/get_device_quotas
title: '查询用量限额配置 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:24:09Z
---

# 查询用量限额配置 - 文档 - 扣子

查询用量限额配置

查询已创建的用量限额配置，包括用量限额、状态、重置周期等详细信息。​

说明

  * 套餐限制：扣子企业旗舰版。​

  * 角色限制：企业超级管理员和管理员可以调用该 API。​

​

接口描述​

企业超级管理员和管理员可以调用该 API 查询已创建的用量限额配置。​

  * 针对设备的终端用户，查询积分用量限额或 AI 智能通话语音时长用量限额。​

  * 针对企业内的成员、空间、组织，查询积分用量限额。​

接口限制​

查询企业成员、空间、组织的积分限额时， starttime、endtime 、 trigger_time 字段可忽略，无参考意义。​

基础信息​

​

请求方式​| GET  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v1/commerce/benefit/limitations​  
权限​| listBenefitLimitation​确保调用该接口使用的访问令牌开通了 listBenefitLimitation 权限，详细信息参考[鉴权方式](<https://docs.coze.cn/developer_guides/authentication>)。​  
接口说明​| 查询用量限额配置。​  
  
​

​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考[准备工作](<https://www.coze.cn/docs/developer_guides/preparation>)。​  
Content-Type​| application/json​| 用于指定解析请求正文的格式，表明请求体为 JSON 格式数据。​  
  
​

Query​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
entity_type​| String​| 必选​| enterprise_all_devices​| 用量限额对象，枚举值：​

  * 终端用户维度的可选值如下：​

  * enterprise_all_devices：所有已上报的设备。​

  * enterprise_all_custom_consumers：所有已上报的自定义实体。​

  * single_device：单个设备。​

  * single_custom_consumer：单个自定义实体。​

  * 企业成员、空间、组织维度的可选值如下：​

  * coze_user_id：单个企业成员。​

  * coze_role：单类企业角色。​

  * coze_workspace：企业工作空间。​

  * coze_organization：企业组织。​

  
entity_id​| String​| 可选​| SN12345*********​| 用量限额对象的 ID。​

  * entity_type 为 single_device 时，设置 entity_id 为设备 ID。​

  * entity_type 为 single_custom_consumer 时，设置 entity_id为自定义实体 ID。​

  * entity_type 为 enterprise_all_devices、enterprise_all_custom_consumers 时，无需设置 entity_id。​

  * entity_type 为 coze_workspace 时，设置 entity_id 为空间 ID。​

  * entity_type 为 coze_organization 时，设置 entity_id 为组织 ID。​

  * entity_type 为 coze_user_id 时，设置 entity_id 为扣子用户 ID。​

  * entity_type 为 coze_role 时，设置 entity_id 为角色类型，枚举值：​

  * EnterpriseGuest：访客​

  * EnterpriseMember：成员​

  * EnterpriseAdmin：管理员​

  
benefit_type​| String​| 必选​| resource_point​| 用量限额类型，枚举值：​

  * resource_point：积分用量限额。​

  * voice_unified_duration_system：语音通话时长用量限额（系统音色）。​

  * voice_unified_duration_custom：语音通话时长用量限额（复刻音色）。​

说明查询企业成员、空间、组织维度的用量限额配置时，需设置为 resource_point。​​  
status​| String​| 可选​| valid​| 用量限额配置的当前状态，枚举值：​

  * valid：正常使用。​

  * frozen：已冻结。​

  * cancel：已取消。​

  
page_token​| String​| 可选​| -​| 翻页标识，表示下一页的起始位置。当查询结果超过 page_size 时，返回的 page_token可用于获取下一页数据。​首次请求不填或置空，后续翻页需带上上一次返回的 page_token。​  
page_size​| Integer​| 可选​| 30​| 查询结果分页展示时，此参数用于设置每页返回的数据量。取值范围为 1~200，默认为 20。​  
  
​

​

返回参数​

​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
code​| Long​| 0​| 调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。​  
msg​| String​| ""​| 状态信息。API 调用失败时可通过此字段查看详细错误信息。​状态码为 0 时，msg 默认为空。​  
data​| Object of [ListBenefitLimitationData](<https://docs.coze.cn/developer_guides/get_device_quotas#listbenefitlimitationdata>)​| { "benefit_id": 123***, "benefit_type": "resource_point", "active_mode": "absolute_time", "started_at": 1741708800, "ended_at": 1741708800, "limit": 100, "status": "valid" }​| 接口调用成功时，返回的详细数据信息。​  
detail​| Object of [ResponseDetail](<https://docs.coze.cn/developer_guides/get_device_quotas#responsedetail>)​| -​| 响应详情信息。​  
  
​

ListBenefitLimitationData​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
has_more​| Boolean​| true ​| 是否还有下一页。​

  * true：还有下一页。​

  * false：没有下一页。​

  
page_token​| String​| -​| 翻页标识。​  
benefit_infos​| Array of [BenefitInfo](<https://docs.coze.cn/developer_guides/get_device_quotas#benefitinfo>)​| -​| 用量额度信息列表。​  
  
​

BenefitInfo​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
limit​| Long​| 100​| 用量限额的具体数值。​

  * benefit_type 为 resource_point 时，单位为积分。​

  * benefit_type 为 voice_unified_duration_system或voice_unified_duration_custom 时，单位为秒。​

  
benefit_type​| String​| resource_point​| 用量限额类型，枚举值：​

  * resource_point：积分用量限额。​

  * voice_unified_duration_system：语音通话时长用量限额（系统音色）。​

  * voice_unified_duration_custom：语音通话时长用量限额（复刻音色）。​

  
active_mode​| String​| absolute_time​| 激活模式，当前仅支持设置为 absolute_time ，即绝对时间。​该模式下，权益生效时间由 started_at 和 ended_at 两个时间确定。​  
started_at​| Long​| 1753996800​| 用量限额配置的生效起始时间，Unixtime 时间戳格式，单位为秒。​  
ended_at​| Long​| 253402300799​| 用量限额配置的生效截止时间，Unixtime 时间戳格式，单位为秒。过期后，该限额配置会失效。​  
entity_id​| String​| SN12345*********​| 用量限额对象的 ID。 详细说明，请参考[Body](<https://docs.coze.cn/developer_guides/create_device_quotas#Body>)中的entity_id字段。​  
status​| String​| valid​| 用量限制规则的当前状态，枚举值：​

  * valid：正常使用。​

  * frozen：已冻结。​

  * cancel：取消。​

  
entity_type​| String​| enterprise_all_devices​| 用量额度的限制对象， 详细说明，请参考[Body](<https://docs.coze.cn/developer_guides/create_device_quotas#Body>)中的entity_type字段。​  
trigger_unit​| String​| day​| 用量限额的重置周期单位，系统将根据指定时间间隔重置限额。枚举值：​

  * never：不重置额度，适用于设置累计可用额度上限。​

  * minute：以分钟为周期重置额度。​

  * hour：以小时为周期重置额度。​

  * day：以天为周期重置额度。​

  
trigger_time​| Long​| 1​| 用量限额的重置频率。​

  * 当 trigger_unit 为 never 时，trigger_time 的值为 1，无实际意义。​

  * 当 trigger_unit 为 minute、hour 或 day 时，trigger_time 表示具体的刷新频率，例如：trigger_unit=day 且 trigger_time = 1，表示每日刷新限额。​

  
  
​

ResponseDetail​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
logid​| String​| 20241210152726467C48D89D6DB2****​| 本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此logid及错误码联系扣子团队获取帮助。详细说明可参考[获取帮助和技术支持](<https://docs.coze.cn/guides/help_and_support>)。​  
  
​

​

示例​

请求示例​

​

JSON

复制

curl --location --request GET 'https://api.coze.cn/v1/commerce/benefit/limitations?entity_type=enterprise_all_devices&entity_id=SN12345*********&benefit_type=resource_point' \​

\--header 'Authorization : Bearer pat_OYDacMzM3WyOWV3P****' \​

\--header 'Content-Type : application/json'​

​

返回示例​

​

JSON

复制

{​

"code": 0,​

"msg": "",​

"data": {​

"has_more": true,​

"page_token": "next_page_token_123",​

"benefit_infos": [​

{​

"limit": 100,​

"status": "valid",​

"ended_at": 1804185600,​

"entity_id": "SN12345*********",​

"started_at": 1753996800,​

"active_mode": "absolute_time",​

"entity_type": "enterprise_all_devices",​

"benefit_type": "resource_point",​

"trigger_time": 1,​

"trigger_unit": "never"​

}​

]​

},​

"detail": {​

"logid": "20241210152726467C48D89D6DB2****"​

}​

}

​

错误码​

如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考[错误码](<https://docs.coze.cn/developer_guides/coze_error_codes>)文档查看对应的解决方法。​

​

上一篇

创建用量限额配置

下一篇

更新用量限额配置