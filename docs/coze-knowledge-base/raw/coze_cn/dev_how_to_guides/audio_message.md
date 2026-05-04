---
source_url: https://docs.coze.cn/dev_how_to_guides/audio_message
title: '基于 HTTP 请求实现语音消息 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:49:26Z
---

# 基于 HTTP 请求实现语音消息 - 文档 - 扣子

基于 HTTP 请求实现语音消息

本文介绍基于 HTTP 请求实现用户给智能体发送语音消息的功能。用户侧发送一条语音消息，智能体接收音频文件后，由大模型生成语音形式的回复。语音回复以流式音频片段的形式返回，应用程序可选择实时播放或在智能体回复完成后将音频片段合并后再播放。​

说明

通过发起对话 API 发送语音消息的功能已停止迭代，推荐使用 WebSocket 语音通话，其具备更优性能、更低延迟，具体请参见​基于 WebSocket OpenAPI 实现音频通话。​

​

步骤一：上传音频文件​

1.

准备音频文件。​

  * 调用​发起对话 API 之前，需要先准备待输入给智能体的音频文件，也就是语音形式的用户 Query。​

  * 音频文件的格式需为 WAV 或 OGG 封装的 OPUS 格式。你可以使用扣子编程提供的​语音合成 接口，将指定的文本内容转成符合要求的音频文件。​

2.

上传音频文件。​

  * 将音频文件上传至扣子编程或第三方存储工具，并获取相应的文件标识或链接。​

  * 上传到扣子编程：调用​上传文件接口，将音频文件上传到扣子编程，并在接口响应中获取文件的 file_id。​

  * 上传到第三方存储工具：将文件上传到对象存储或其他第三方存储工具中，并获取一个公网可访问的链接，此链接为文件的 file_url。​

步骤二：调用发起对话 API​

请求结构​

调用​发起对话时，需在入参中指定已上传的音频文件，并选择流式响应。必选输入参数的说明如下表所示。​

​

请求参数​| 说明​  
---|---  
bot_id​| 智能体 ID。智能体开发页面 URL 中 bot 参数后的数字就是智能体 ID。​  
user_id​| 与智能体对话的用户 ID。不同的 user_id，其对话的上下文消息、数据库等对话记忆数据互相隔离。如果不需要用户数据隔离，可将此参数固定为一个任意字符串​  
stream​| 是否采用流式响应。语音场景下固定设置为 true，表示采用流式响应。​说明语音消息只支持流式响应，所以此处 stream 必须设置为 true。​​  
additional_messages​| 对话中的消息内容，包括对话的历史消息和本次对话中的用户问题。​消息应按对话流程顺序排列，且最后一条消息应为 role=user 的记录，表示本次对话中的用户问题。​数组长度限制为 100，即最多传入 100 条消息。​additional_messages 的字段结构请参见下表。​  
  
​

additional_messages 为 JSON 数组格式，每个 JSON 对象代表一条独立的消息，其结构如下：​

​

字段 ​|  说明 ​  
---|---  
role ​|  发送消息的实体，取值包括：​

  * user：用户​

  * assistant：智能体​

  
type ​|  消息类型。默认为 question。​

  * 当 role 为 user 时，type 应设置为 question。​

  * 当 role 为 assistant 时，type 应设置为 answer。 ​

  
content ​|  消息内容。在语音场景下，content 字段为一个经过序列化的 JSON 字符串，该字符串表示一个包含多个对象的数组，其中每个对象的类型为 object_string。包含 type、file_id 和 file_url 三个参数。type 固定为 audio。 ​说明

  * 如果音频文件上传到扣子编程，在 content 中应指定 type、file_id。​

  * 如果音频文件上传到第三方的存储工具，在 content 中应指定 type 和 file_url。​

​  
content_type ​|  消息内容类型。语音场景下设置为 object_string，表示多模态内容。 ​  
  
​

additional_messages 语音消息示例如下：​

通过 API 上传的文件

通过第三方存储工具上传的文件

​

JSON

复制

[​

{​

"role":"user",​

"content":"[{\"type\":\"audio\",\"file_id\":\"736949598110202****\"}]",​

"content_type":"object_string"​

}​

]​

​

​

响应结构​

语音场景下，​发起对话接口的响应为流式响应。conversation.audio.delta 响应事件中包含模型回复的音频片段。data 字段为 Message Object，其中 content_type 为 audio，content 为音频片段的 Base64 编码字符串。​

根据输入音频文件格式，content 的格式有所不同：​

  * 若输入音频文件为 WAV 格式， content 为 PCM 音频片段的 Base64 编码字符串。音频片段采样率为 24kHz，16 位，单声道，little-endian。​

  * 若输入音频文件为 OGG_OPUS 格式，content 为 OPUS 音频片段的 Base64 编码字符串。音频片段码率为 48kbps，单声道，帧长为 10ms。如需自定义 OPUS 编码格式，可参考下文中的​自定义 opus 编码。​

请求示例

响应示例

​

Bash

复制

curl --location --request POST 'https://api.coze.cn/v3/chat' \ ​

\--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \ ​

\--header 'Content-Type: application/json' \ ​

\--data-raw '{ ​

"bot_id": "734829333445931****", ​

"user_id": "123456789", ​

"stream": true, ​

"auto_save_history":true, ​

"additional_messages":[ ​

{ ​

"role":"user", ​

"content":"[{\"type\": \"audio\", \"file_id\": \"734829333445931****\"}]", ​

"content_type":"object_string" ​

} ​

] ​

}'​

​

​

自定义 opus 编码​

若输入音频文件为 OGG_OPUS 格式，开发者可自定义返回的 OPUS 编码格式。在​发起对话接口中，通过 extra_params 参数配置返回的 OPUS 音频片段编码格式，audio_message_config配置的值为 JSON 字符串，结构如下：​

​

JSON

复制

{​

"opus_codec": {​

"bitrate": 16000, // 码率，不传默认为48000，opus 支持 6kb/s 到 510kb/s 的码率​

"use_cbr": false, // 是否使用 CBR 编码，默认为 false​

"frame_size_ms": 10 // opus 帧大小，默认为 10ms。opus 支持 2.5ms 到 60ms 的帧大小​

}​

}​

​

请求示例：​

​

Bash

复制

curl --location --request POST 'https://api.coze.cn/v3/chat' \ ​

\--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \ ​

\--header 'Content-Type: application/json' \ ​

\--data-raw '{ ​

"bot_id": "734829333445931****", ​

"user_id": "123456789", ​

"stream": true, ​

"auto_save_history":true, ​

"additional_messages":[ ​

{ ​

"role":"user", ​

"content":"[{\"type\": \"audio\", \"file_id\": \"734829333445931****\"}]", ​

"content_type":"object_string" ​

} ​

],​

"extra_params": {​

"audio_message_config": "{\"opus_codec\": {\"bitrate\": 16000, \"use_cbr\": false, \"frame_size_ms\": 60}}"​

} ​

}'​

​

步骤三：处理音频片段​

通过发起对话 API 的返回结果中获取音频片段后，开发者可选择实时播放，或在流式响应结束后将音频片段合并写入音频文件，一次性播放给用户。​

以下是使用 Go 语言处理音频片段的示例代码，展示如何使用 WAV 封装 PCM 和 OGG 封装 OPUS。​

WAV 封装 PCM 格式音频

OGG 封装 OPUS 格式音频

​

Go

复制

import (​

"log"​

"os"​

​

"github.com/go-audio/audio"​

"github.com/go-audio/wav"​

)​

​

func callCoze() {​

​

pcmData := make([]byte, 0)​

​

// 调用 coze ，从 http response 中一直拿返回的 event 和 data​

for {​

// 伪代码，从 http response 中流式读取 event 和 data​

event, data := resp.Recv()​

// 对于所有 event 为 conversation.audio.delta 的事件，取出 data 中的音频片段​

if event == "conversation.audio.delta" {​

audioData := make(map[string]interface{})​

err := json.Unmarshal([]byte(data), &audioData)​

if err != nil {​

log.Fatalf("Error Unmarshal: %v", err)​

}​

if base64AudioStr, exist := audioData["content"]; exist {​

pcmPart, err := base64.StdEncoding.DecodeString(base64AudioStr.(string))​

if err != nil {​

log.Fatalf("Error DecodeString: %v", err)​

}​

pcmData = append(pcmData, pcmPart...)​

}​

}​

// 结束事件，退出循环​

if event == "done" {​

break​

}​

}​

​

writeWav(pcmData)​

}​

​

func writeWav(pcmData [][]byte) {​

// 采样率​

sampleRate := 24000​

// 位深​

bitDepth := 16​

// 通道数​

numChannels := 1​

f, err := os.Create("pcm-example.wav")​

if err != nil {​

log.Fatalf("Error Create: %v", err)​

}​

​

intData := make([]int, 0)​

for i := 0; i < len(pcmData); i += 2 {​

intData = append(intData, int(uint16(pcmData[i])|uint16(pcmData[i+1])<<8))​

}​

intBuffer := &audio.IntBuffer{​

Format: &audio.Format{​

NumChannels: numChannels,​

SampleRate: sampleRate,​

},​

Data: intData,​

SourceBitDepth: bitDepth,​

}​

​

e := wav.NewEncoder(f, sampleRate, bitDepth, numChannels, 1)​

defer e.Close()​

err = e.Write(intBuffer)​

if err != nil {​

log.Fatalf("Error Write: %v", err)​

}​

return ​

}​

​

​

上一篇

集成火山引擎 RTC SDK

下一篇

语音合成与识别