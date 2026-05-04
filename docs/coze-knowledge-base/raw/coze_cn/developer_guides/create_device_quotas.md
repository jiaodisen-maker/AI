---
source_url: https://docs.coze.cn/developer_guides/create_device_quotas
title: '创建用量限额配置 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:24:06Z
---

# 创建用量限额配置 - 文档 - 扣子

创建用量限额配置

创建一个用量限额配置。​

说明

  * 套餐限制：扣子企业旗舰版。​

  * 角色限制：企业超级管理员和管理员可以调用该 API。​

​

接口描述​

企业超级管理员和管理员可以调用该 API 为不同维度的对象设置用量限额。​

  * 针对设备的终端用户，配置积分用量限额或 AI 智能通话语音时长用量限额。​

  * 针对企业内的成员、空间、组织，配置积分用量限额。​

​

管控维度​| 终端用户​| 企业成员、空间、组织​  
---|---|---  
核心用途​| 为设备的终端用户配置积分用量限额或 AI 智能通话语音时长用量限额，以便终端用户在初始阶段免费体验设备功能，同时避免资源的过度使用。​未设置权益额度的设备，将默认无限制使用资源。更多信息，请参考[终端用户用量查询和配额管控（API）](<https://docs.coze.cn/dev_how_to_guides/device_usage_api>)。​| 为企业内的成员、空间、组织设置积分用量限额，来管理企业不同层级的积分用量，同时避免过度消耗积分。​  
限额维度​| 

  * 设备​

  * 自定义维度的实体（如 App 用户）​

| 

  * 企业成员/角色​

  * 企业工作空间​

  * 企业组织​

  
限额类型​| 

  * 积分：累计额度、周期额度​

  * 语音通话时长：累计额度、周期额度​

| 

  * 积分累计额度​

  * 积分每月额度​

  
生效优先级​| 若同时为单个设备和企业下所有设备配置了限额，则优先使用单个设备的限额。​| 系统会同时执行你所设置的所有限额规则，其中任一额度达到上限时，其对应范围内的成员均将无法继续使用需要消耗积分的扣子功能。​  
特殊说明​| 

  * 为终端用户配置用量限额前，需先上报企业设备信息。具体操作，请参考[设置设备信息](<https://docs.coze.cn/dev_how_to_guides/deviceInfo>)。​

  * 用量限额对象为企业所有设备或所有自定义维度的实体时，仅可创建一条累计限额规则和一条周期限额规则。​

  * 如需设置语音通话时长用量限额，需先增购 AI 智能通话许可。详细说明，请参考[智能设备语音通话](<https://docs.coze.cn/coze_pro/asr_tts_fee#6077a3b4>)。​

| 设置企业成员、空间、组织的积分限额时，无需填写 starttime、endtime 和 trigger_time 字段，系统会自动忽略这些配置。​

  * 积分累计额度：设置 trigger_unit 为 never。​

  * 积分每月额度：设置 trigger_unit 为除 never 以外的其他可选值，系统将自动转化为自然月周期。​

  
  
​

​

基础信息​

​

请求方式​| POST  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v1/commerce/benefit/limitations​  
权限​| createBenefitLimitation​确保调用该接口使用的访问令牌开通了 createBenefitLimitation 权限，详细信息参考[鉴权方式](<https://docs.coze.cn/developer_guides/authentication>)。​  
接口说明​| 创建一个用量限额配置。​  
  
​

​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考[准备工作](<https://docs.coze.cn/developer_guides/preparation>)。​  
Content-Type​| application/json​| 用于指定解析请求正文的格式，表明请求体为 JSON 格式数据。​  
  
​

Body​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
entity_type​| String​| 必选​| enterprise_all_devices​| 用量限额对象。​

  * 终端用户维度的可选值如下：​

  * enterprise_all_devices：所有已上报的设备。​

  * enterprise_all_custom_consumers：所有已上报的自定义实体。​

  * 若某设备未上报 custom_consumers，则该设备无法通过 custom_consumers 维度生效限额。​

  * single_device：单个设备。​

  * single_custom_consumer：单个自定义实体。​

  * 企业成员、空间、组织维度的可选值如下：​

  * coze_user_id：单个企业成员。​

  * coze_role：单类企业角色。​

  * coze_workspace：企业工作空间。​

  * coze_organization：企业组织。​

  
entity_id​| String​| 可选​| 12345​| 用量限额对象的 ID，可选值：​

  * entity_type 为 single_device 时，设置entity_id为设备 ID。​

  * entity_type 为 single_custom_consumer 时，需要设置entity_id为自定义实体 ID。​

  * entity_type 为 coze_workspace 时，设置 entity_id 为空间 ID。​

  * entity_type 为 coze_organization 时，设置 entity_id 为组织 ID。​

  * entity_type 为 coze_user_id 时，设置 entity_id 为扣子用户 ID。​

  * entity_type 为 coze_role 时，设置 entity_id 为角色类型，枚举值：​

  * EnterpriseGuest：访客​

  * EnterpriseMember：成员​

  * EnterpriseAdmin：管理员​

  * entity_type 为 enterprise_all_devices、enterprise_all_custom_consumers 时，无需设置 entity_id。​

  
benefit_info​| Object of [BenefitInfo](<https://docs.coze.cn/developer_guides/create_device_quotas#benefitinfo>)​| 必选​| { "benefit_type": "resource_point", "active_mode": "absolute_time", "started_at": 1741708800, "ended_at": 253402300799, "limit": 100, "status": "valid" }​| 用量限额配置信息。​  
  
​

BenefitInfo​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
limit​| Long​| 必选​| 100​| 用量限额的具体数值。​

  * benefit_type 为 resource_point 时，单位为积分。​

  * benefit_type 为 voice_unified_duration_system或voice_unified_duration_custom 时，单位为秒。​

  
benefit_type​| String​| 必选​| resource_point​| 用量限额类型，枚举值：​

  * resource_point：积分用量限额。​

  * voice_unified_duration_system：语音通话时长用量限额（系统音色）。​

  * voice_unified_duration_custom：语音通话时长用量限额（复刻音色）。​

  
active_mode​| String​| 必选​| absolute_time​| 激活模式，当前仅支持设置为 absolute_time ，即绝对时间。​该模式下，权益生效时间由 started_at 和 ended_at 两个时间确定。​  
started_at​| Long​| 必选​| 1753996800​| 用量限额配置的生效起始时间，Unixtime 时间戳格式，单位为秒。​  
ended_at​| Long​| 必选​| 253402300799​| 用量限额配置的生效截止时间，Unixtime 时间戳格式，单位为秒。过期后，该限额配置会失效。​  
entity_id​| String​| 可选​| SN12345*********​| 用量限额对象的 ID。详细说明，请参考[Body](<https://docs.coze.cn/developer_guides/create_device_quotas#Body>)中的entity_id字段。​  
status​| String​| 可选​| valid​| 用量限制规则的当前状态，枚举值：​

  * valid：正常使用。​

  * frozen：已冻结。​

  * cancel：取消。​

  
entity_type​| String​| 可选​| enterprise_all_devices​| 用量限额对象。详细说明，请参考[Body](<https://docs.coze.cn/developer_guides/create_device_quotas#Body>)中的entity_type字段。​  
trigger_unit​| String​| 可选​| day​| 用量限额的重置周期单位，系统将根据指定时间间隔重置限额。枚举值：​

  * never：不重置额度，适用于设置累计可用额度上限。​

  * minute：以分钟为周期重置额度。​

  * hour：以小时为周期重置额度。​

  * day：以天为周期重置额度。​

  
trigger_time​| Long​| 可选​| 1​| 用量限额的重置频率。​

  * 当 trigger_unit 为 never 时，trigger_time 的值为 1，无实际意义。​

  * 当 trigger_unit 为 minute、hour 或 day 时，trigger_time 表示具体的刷新频率，例如：trigger_unit=day 且 trigger_time = 1，表示每日刷新限额。​

  
  
​

​

返回参数​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
code​| Long​| 0​| 调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。​  
msg​| String​| ""​| 状态信息。API 调用失败时可通过此字段查看详细错误信息。​状态码为 0 时，msg 默认为空。​  
data​| Object of [CreateBenefitLimitationData](<https://docs.coze.cn/developer_guides/create_device_quotas#createbenefitlimitationdata>)​| { "benefit_id": 123***, "benefit_type": "resource_point", "active_mode": "absolute_time", "started_at": 1741708800, "ended_at": 1741708800, "limit": 100, "status": "valid" }​| 接口调用成功时，返回的详细数据信息。​  
detail​| Object of [ResponseDetail](<https://docs.coze.cn/developer_guides/create_device_quotas#responsedetail>)​| -​| 响应详情信息。​  
  
​

CreateBenefitLimitationData​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
benefit_info​| Object of [BenefitInfo](<https://docs.coze.cn/developer_guides/create_device_quotas#benefitinfo>)​| -​| 用量额度信息。​  
  
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

  
benefit_id​| String​| 123​| 用量限额配置的 ID。​  
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

voice_unified_duration_custom 才生效。voice_unified_duration_custom 才生效。voice_unified_duration_custom 才生效。voice_unified_duration_custom 才生效。​

示例​

请求示例​

​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/commerce/benefit/limitations' \​

\--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \​

\--header 'Content-Type: application/json'​

{​

"entity_type": "single_device",​

"entity_id": "SN12345*********",​

"benefit_info": {​

"benefit_type": "resource_point",​

"active_mode": "absolute_time",​

"started_at": 1741708800,​

"ended_at": 253402300799,​

"limit": 100,​

"status": "valid"​

}​

}

​

返回示例​

​

JSON

复制

{ ​

"data": { ​

"benefit_id": 123***, ​

"benefit_type": "resource_point", ​

"active_mode": "absolute_time", ​

"started_at": 1741708800, ​

"ended_at": 253402300799, ​

"limit": 100, ​

"status": "valid" ​

}, ​

"code": 0, ​

"msg": "" ​

}

​

错误码​

如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考[错误码](<https://docs.coze.cn/developer_guides/coze_error_codes>)文档查看对应的解决方法。​

​

上一篇

绑定设备

下一篇

查询用量限额配置