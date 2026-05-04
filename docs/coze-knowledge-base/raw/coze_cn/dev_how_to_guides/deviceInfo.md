---
source_url: https://docs.coze.cn/dev_how_to_guides/deviceInfo
title: '上报设备信息 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:49:37Z
---

# 上报设备信息 - 文档 - 扣子

上报设备信息

为实现终端用户用量管控及账单记录功能，你需要将终端用户信息上报给扣子编程。​

说明

套餐限制：扣子企业版。​

​

方案对比​

扣子编程提供两种设备信息传递方式，你可根据业务场景选择合适的接入方式。​

​

方案​| 使用场景​| 说明​  
---|---|---  
在 JWT 授权时传递设备信息（推荐）​| 适用于每个终端用户具有独立的密钥的场景。​| 将终端用户信息嵌入 JWT 的 Payload 中，终端用户获取 Token 时上报设备信息。​  
API Header 中传递设备信息​| 适用于后端采用集中管理模式，且未为每个终端用户分配独立密钥的场景。​| 需要在所有涉及到积分消耗的 API 的 Header 中添加设备字段，若未正确添加该字段，可能会导致终端用户用量统计不准确。​  
  
​

方式一：在 JWT 授权时传递（推荐）​

适用于每个设备具有独立的密钥的场景。通过将设备信息嵌入 JWT 的 Payload 部分，设备在签署 JWT 并获取 Access Token 时，上报对应的设备信息，扣子编程将通过 Access Token 解析设备信息。具体参数及配置可参考​OAuth JWT 授权（渠道场景）。​

在 Payload 的 session_context.device_info 参数中配置设备相关信息，参数说明如下表所示。​

​

参数​| 类型​| 是否必选​| 说明​  
---|---|---|---  
session_context​| Object​| 可选 ​| 会话上下文信息，包含设备相关信息等。​​  
session_context.device_info​| Object​| 可选 ​| 用于配置设备相关信息，扣子编程基于该部分信息对设备做用量管控以及账单记录。​  
session_context.device_info.device_id​| String​| 可选 ​| IoT 等硬件设备 ID，一个设备对应一个唯一的设备号。​  
session_context.device_info.custom_consumer​​| String​| 可选 ​| 自定义维度的实体 ID，你可以根据业务需要进行设置，例如 APP 上的用户名等。​说明

  * device_id 和 custom_consumer 建议选择其中一个即可。​

  * custom_consumer 参数用于设备用量管控，与对话等 API 传入的 user_id 无关，user_id 主要用于上下文、数据库隔离等场景。​

  * 出于数据隐私及信息安全等方面的考虑，不建议使用业务系统中定义的用户敏感标识（如手机号等）作为 custom_consumer 的值。​

​  
  
​

Payload 示例代码如下：​

​

JSON

复制

{​

"session_context": {​

"device_info": {​

"device_id": "1234567890" // IoT 等硬件设备的唯一标识 ID​

}​

}​

}​

​

方式二：API Header 传递​

建议优先采用方式一。仅在以下场景中可考虑使用此接入方式：后端采用集中管理模式且未为每个设备分配独立密钥。​

注意

需要确保设备信息传递的准确性，扣子编程不验证该信息的真实性。​

​

API 列表​

采用 Header 方式传递时，你需要在所有涉及到积分消耗的 API 的 Header 中添加 X-Coze-DeviceInfo 字段。若未正确添加该字段，可能会导致设备用量统计不准确。具体需要添加该字段的 API 如下表所示。​

​

分类​| API ​  
---|---  
音视频​| ​语音合成​  
​| ​语音识别​  
​| ​创建房间​  
对话​| ​发起对话​  
工作流​| ​执行工作流​  
​| ​执行工作流（流式响应）​  
​| ​执行对话流​  
​| ​恢复运行工作流（流式响应）​  
  
​

添加 Header 参数​

在 API 的 Header 中添加如下参数。​

​

参数​| 取值​| 说明​  
---|---|---  
X-Coze-DeviceInfo​​| JSON Marshal of [DeviceInfo](<https://bytedance.larkoffice.com/docx/MZOWder6NoIX4HxJxEBclx6Onzh#share-Z0Sfd5rIMoHIncxgzDmcTikinjf>)​| 用于传递设备相关信息，扣子编程基于该部分信息对设备做用量管控以及账单记录。​  
  
​

DeviceInfo​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
device_id​| String​| SN12345*****​| IoT 等硬件设备 ID，一个设备对应一个唯一的设备号。​  
custom_consumer​​| String​​| 1334567****​​| 设备的自定义用户标识，你可以根据业务需要进行设置，例如用户名等。​说明

  * custom_consumer 参数用于用量管控，与对话等 API 传入的 user_id 无关，user_id 主要用于上下文、数据库隔离等场景。​

  * 出于数据隐私及信息安全等方面的考虑，不建议使用业务系统中定义的用户敏感标识（如手机号等）作为 custom_consumer 的值。​

​  
  
​

示例​

以下是调用创建房间 API 时，使用 API Header 传递设备信息的示例：​

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v1/audio/rooms' \ ​

\--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \ ​

\--header 'Content-Type: application/json' \ ​

\--header 'X-Coze-DeviceInfo: {"device_id": "SN123456****", "custom_consumer": "1334567****"}' \​

\--data-raw '{ ​

"bot_id": "734829333445931****" ​

}'​

​

上一篇

音色复刻

下一篇

终端用户用量查询和配额管控