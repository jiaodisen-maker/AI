---
source_url: https://docs.coze.cn/developer_guides/benefit_plugin_scale_requested
title: '申请插件扩容回调事件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:23:49Z
---

# 申请插件扩容回调事件 - 文档 - 扣子

申请插件扩容回调事件

如果三方付费插件支持扩容，插件开发者可以订阅申请插件扩容回调事件。当用户申请插件扩容时，扣子编程会向指定的回调地址推送回调消息，消息中包含插件扩容的详细信息。订阅回调的具体操作请参见​订阅回调。​

说明

申请插件扩容回调仅支持普通回调，不支持渠道回调。​

​

触发条件​

仅插件开发者可订阅，当用户申请插件扩容时，对应的回调地址会收到申请插件扩容回调事件。​

回调结构体​

回调消息的结构体 Body 中包含两个主要字段：header 和 event。​

  * header参数的参数说明请参见​回调事件。​

  * event 参数中包括以下参数：​

  * ​

字段​| 类型​| 说明​  
---|---|---  
apply_id​| String​| 扩容申请的 ID。​  
begin_at​| Integer​| 扩容生效开始时间，采用 Unix 时间戳格式，单位：秒。​  
end_at​| Integer​| 扩容过期时间，采用 Unix 时间戳格式，单位：秒。​  
resource_id​| String​| 扩容插件的 ID。​  
usage_in_30d​| Number​| 该用户在最近 30 天内调用该插件的次数。​  
applicant_info.user_id​| Integer​| 发起扩容申请的扣子用户 ID。​  
applicant_info.user_name​| String​| 发起扩容申请的扣子用户名称。​  
extension_type​| String​| 扩容类型， 当前仅支持 QPS（Queries Per Second），即每秒最大请求数。​  
origin_capacity​| Number​| 扩容前的原始 QPS。​  
target_capacity​| Number​| 扩容后期望达到的目标 QPS。​  
  
​

回调结构体示例：​

​

JSON

复制

{​

"header": {​

"event_type": "benefit.plugin.scale.requested", //申请插件扩容回调事件​

"event_id": "83453324-0863-4abc-bcdf-80818705f29e-7545743825545740332", // 此次触发的事件唯一ID，用户应该用这个ID做去重​

"api_app_id": "75457438255457***",​

"created_at": 1757318670060,​

"coze_account_id": ""​

},​

"event": {​

"apply_id": "754761756009177***", // 申请单号​

"begin_at": 1757318663, // 扩容生效时间，时间戳（秒）​

"end_at": 1757664263, // 扩容过期时间，时间戳（秒）​

"resource_id": "75454180821776***", // 扩容插件的 ID​

"usage_in_30d": 0, // 该用户在最近 30 天内该插件的调用量​

"applicant_info": { // 申请人信息​

"user_id": 2100288***, // 申请人的扣子用户ID​

"user_name": "" // 申请人的扣子用户名​

},​

"extension_type": "QPS", // 扩容类型：QPS（每秒最大请求数）​

"origin_capacity": 20, // 扩容前的原始 QPS​

"target_capacity": 30 // 扩容后期望达到的目标 QPS​

}​

}​

​

响应回调​

开发者服务器收到申请插件扩容回调后，应在 3 秒内响应，并返回 HTTP 状态码 200。​

相关文档​

​订阅回调​

​接收并处理回调​

上一篇

调用插件工具

下一篇

插件扩容到期回调事件