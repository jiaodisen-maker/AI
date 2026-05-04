---
source_url: https://docs.coze.cn/developer_guides/billing_callback_message
title: '账单推送回调事件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:24:21Z
---

# 账单推送回调事件 - 文档 - 扣子

账单推送回调事件

如果开发者订阅了账单推送回调，用户与智能体对话结束后，会收到资源点消耗的账单推送回调。订阅回调的具体操作请参见​订阅回调。​

说明

  * 仅扣子付费套餐支持订阅账单推送事件。​

  * 对于音视频通话，扣子编程会先推送除音视频通话外的账单回调，音视频通话的账单回调则预计延迟 3 至 5 小时后推送。​

​

回调结构体​

消息通知回调的回调结构体 Body 中包括 header 和 event 两个字段。​

  * header参数的参数说明请参见​回调事件。​

  * Body 的 event 参数中包括以下参数：​

  * ​

字段​| 字段类型​| 说明​  
---|---|---  
id​| String​| 账单的 ID。​  
consume_time​| Bigint​| 资源消耗发生的时间戳，Unix 时间戳，单位为秒。​  
record_root_id​| String​| root ID，标识一次完整对话，用于关联对话全链路数据（包括但不限于智能体、插件、模型等多类型资源消耗记录）。通过该字段可追溯同一会话内的所有费用明细。​  
connector_id​| String​| 渠道 ID。标识资源消耗所属的渠道类型，具体如下：​
    * API：1024​
    * ChatSDK：999​
    * 商店：10000010。​
    * 自定义渠道：自定义渠道 ID，获取方式可以参考​渠道入驻概述。需要保证使用自定义渠道的创建者的访问令牌来进行访问。​  
connector_uid​| String​| 渠道用户 ID，用于标识渠道内的终端用户身份。​  
device_id​| String​| 设备 ID。若上报的设备信息中未包含该字段，则值为空。​  
custom_consumer​| String​| 自定义维度的实体 ID，对应上报设备信息时 custom_consumer 参数中的值，具体请参见​上报设备信息。​  
space_id​| String​| 产生费用的实体所在的空间 ID。例如智能体所在的空间 ID。​  
root_entity_type​| Bigint​| 产生费用的实体类型：​
    * 低代码项目​
    * 1：智能体（bot）​
    * 2：工作流（workflow）​
    * 3：插件（plugin）​
    * 4：应用（application）​
    * 5：模型类（model）​
    * 6：语音类（voice）​
    * AI 编程项目​
    * 101：编程项目​
    * 扣子​
    * 111：历史对话（历史功能）​
    * 112：长期计划（历史功能）​
    * 113：主对话、邮箱、飞书渠道对话等​
    * 114：资产库​
    * 115：设备​  
root_entity_id​| String​| 产生费用的实体 ID，例如智能体 ID、工作流 ID 等。​说明若实体类型为语音类（voice）或模型类（model），且未与智能体绑定（例如直接调用语音合成 API），则该字段值为空。​​  
change_balance​| String​| 本次对话消耗的资源点或语音通话时长。​
    * 未增购 AI 智能通话许可的企业，默认消耗资源点。​
    * 增购 AI 智能通话许可的企业，默认先消耗语音通话时长，单位为秒。​  
balance_type​| Bigint​| 余额类型，枚举值：​
    * 2：resource_point：资源点。​
    * 3：voice_unified_duration_system，语音通话时长（系统音色），仅增购 AI 智能通话许可（系统音色）的企业支持。​
    * 4：voice_unified_duration_custom，语音通话时长（复刻音色），仅增购 AI 智能通话许可（复刻音色）的企业支持。​  
resource_type​| Bigint​| 计费项类型：​
    * 1：模型类（model）​
    * 2：插件（plugin）​
    * 3：智能语音（voice），包括语音识别 ASR 和语音合成 TTS ​
    * 4：RTC 音视频通话​  
resource_id​| String​| 计费项的 ID，根据 resource_type 不同，对应的 resource_id 如下：​
    * 模型类（model）：模型 ID​
    * 插件（plugin）：插件 ID​
    * 语音类（voice）或 rtc：具体枚举值如下：​
    * Tts_system_text_to_speech_chars：语音合成 - 系统音色文字转语音字数。​
    * Asr_large_model_streaming_duration：语音识别 - 大模型流式语音识别时长。​
    * Asr_large_model_recording_duration：语音识别 - 大模型录音文件识别时长。​
    * Rtc_miniprogram_voice_call_duration：实时音视频 - 小程序语音通话时长。​
    * Rtc_voice_call_duration：实时音视频 - 语音通话时长。​
    * Rtc_dialog_ai_audio_duration：实时音视频 - 对话式 Al - 音频时长。​
    * Rtc_video_call_4k_duration：实时音视频 - 视频通话时长（4K）。​
    * Rtc_video_call_2k_duration：实时音视频 - 视频通话时长（2K）。​
    * Rtc_video_call_1080p_duration：实时音视频 - 视频通话时长（1080P）。​
    * Rtc_video_call_720p_duration：实时音视频 - 视频通话时长（720P）。​
    * Rtc_video_call_360p_duration：实时音视频 - 视频通话时长（360P）。​  
model_id​| String​| 模型 ID。​  
model_input_token​| Bigint​| 模型输入 Token 数量。​  
model_output_token​| Bigint​| 模型输出 Token 数量。​  
tts_char_num​| Bigint​| 文字转语音的字符数。​  
tts_count​| Bigint​| 文字转语音的调用次数， 即 TTS 小模型合成的次数。​  
asr_audio_length​| Bigint​| 语音识别（ASR）的音频时长，单位为毫秒。​  
rtc_duration​| Bigint​| RTC 音视频通话时长，单位为毫秒。​  
rtc_begin_time​| Bigint​| 语音通话开始时间，Unix 时间戳，单位为秒。​  
rtc_end_time​| Bigint​| 语音通话结束时间，Unix 时间戳，单位为秒。​  
  
​

回调结构体示例​

账单推送回调的结构体示例如下：​

​

​

JSON

复制

{​

"header": {​

"event_type": "benefit.usage",​

"event_id": "bc02c5cc-a4c6-4434-9f40-e5978e54ba02-751163889***",​

"created_at": 1749042145635,​

"api_app_id": "7511638893163****"​

},​

"event": {​

"id": "684043e196f22aae6d2b4ba1",​

"consume_time": 1749042145,​

"record_root_id": "240482016171010",​

"connector_id": "10000010",​

"connector_uid": "1423241851***",​

"device_id": "",​

"custom_consumer": "",​

"space_id": "750363709788317****",​

"root_entity_id": "751197483247***",​

"root_entity_type": 1,​

"change_balance": "0.16",​

"balance_type": 2,​

"resource_type": 1,​

"resource_id": "1737521***",​

"cost_account_id": "210587***",​

"rtc_begin_time": 0,​

"rtc_end_time": 0,​

"tts_char_num": 0,​

"rtc_duration": 0,​

"model_output_token": 62,​

"model_input_token": 42,​

"model_id": "1737521813",​

"asr_audio_length": 0,​

"tts_count": 0​

}​

}​

​

响应回调​

开发者服务器收到账单推送回调后，应在 3 秒内响应，并在响应中返回 HTTP 状态码 200。​

相关文档​

​订阅回调​

​接收并处理回调​

上一篇

查询套餐权益

下一篇

创建回调应用