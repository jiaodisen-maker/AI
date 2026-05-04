---
source_url: https://docs.coze.cn/tutorial/WebSocket-voice-latency-troubleshooting-and-optimization-suggestions
title: 'WebSocket 语音耗时排查与优化建议 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:52:25Z
---

# WebSocket 语音耗时排查与优化建议 - 文档 - 扣子

WebSocket 语音耗时排查与优化建议

WebSocket 语音交互的端到端延迟由客户端处理、网络传输、语音识别、智能体响应、语音合成几部分构成。要系统性地优化延迟，需先以官方 Demo 的性能数据为基准进行对比，快速锁定耗时超出正常范围的异常环节，再结合 TTFT（首 Token 生成时间）和 TPOT（后续 Token 生成时间）、推理 Token 生成速度等智能体核心性能指标进行深入拆解分析，帮助你定位和解决扣子 WebSocket 语音服务的响应延迟的问题。​

WebSocket 事件流与耗时构成​

在开始排查前，首先需要理解语音对话的完整链路和事件流转过程。延迟可能发生在链路的任何一个环节。以下图示将引导你从事件全景图，逐步聚焦到具体的耗时环节。​

WebSocket 事件流转全景​

下图是客户端与扣子服务端交互的全景图，为你展示了通信链路中所有可能的事件和流向。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27597%27%20height=%27447%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e774e87e13b44083be32c059258df763~tplv-goo7wpa0wc-quality:q75.image)​

​

按键说话模式​

该模式下的实时语音交互全链路时序图，可作为客户端性能诊断的参照标准。你可以通过对比客户端与服务端在网络传输、ASR 识别、智能体响应、TTS 生成、音频播放五个环节的耗时，来判断客户端是否引入了额外延迟。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27613%27%20height=%27437%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEzIiBoZWlnaHQ9IjQzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

自由对话模式​

该模式下新增的 speech_started 和 speech_stopped 事件，由服务器根据语音活动检测（VAD）触发。这两个 VAD 事件是实现录制自动启停的核心。因此，在排查对话被异常打断或无法自动结束等问题时，应重点检查客户端对这两个事件的接收与处理逻辑。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27615%27%20height=%27411%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE1IiBoZWlnaHQ9IjQxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

关键事件节点（以自由对话模式为例）​

通过以下语音交互全链路耗时的时序图，帮你分析从用户说话开始到听到回复的每个环节耗时占比。其中，需重点关注 LLM 阶段。LLM 阶段指图中从 “判停” 到 “LLM 首 Token” 的耗时，衡量了大语言模型从接收输入到生成首个响应 Token 所需的时间。如果 LLM 阶段耗时过长，可针对性优化智能体的工作流与插件调用逻辑。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27611%27%20height=%27262%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjExIiBoZWlnaHQ9IjI2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

与官方Demo对比定位客户端问题​

通过将自身接入服务与扣子官方 Demo 的性能数据进行对比，可以快速判断延迟是否由你的客户端实现引入。​

排查步骤​

a.

访问[扣子官方 WebSocket 实时语音对话页面](<https://www.coze.cn/open-platform/realtime/websocket/>)。​

b.

在页面右上角 Settings 中配置你的智能体 ID 和个人访问令牌。​

c.

单击配置，在高级配置对话框填写你使用的 chat.update 事件的 data 内容。​

  * 配置Settings：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27427%27%20height=%27437%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI3IiBoZWlnaHQ9IjQzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

完成高级配置：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27419%27%20height=%27478%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE5IiBoZWlnaHQ9IjQ3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

d.

完成配置后，在相同网络环境下，使用同一语音内容对官方 Demo 和自身接入服务进行测试，对比完整交互及关键节点耗时。如果自身接入服务耗时明显更高，请参考以下优化建议。​

  * 优化建议​

  * 配置 WebSocket 事件订阅​

  * 在 chat.update 事件中通过 event_subscriptions 指定需要订阅的事件，减少不必要的数据传输。如果设置了 event_subscriptions 并且值不为空，则扣子只下发订阅的事件。​

  * 配置示例：只需要音频数据，不需要字幕。​

  * ​

TypeScript

复制

{​

"id": "event_id", ​

"event_type": "chat.update", ​

"data":{​

// ...其他设置​

"event_subscriptions": [ ​

"error", ​

"conversation.chat.camplete", ​

"conversation.chat.canceled", ​

"conversation.audio.delta", ​

"conversation.chat.failed",​

// 非按键说话场景，需要添加下面两个事件​

"input_audio_buffer.speech_started", ​

"input_audio_buffer.speech_stopped"​

]​

}​

}​

​

  * 配置音频包大小​

  * PCM/G711 编码​

  * 对于 PCM/G711 音频编码，扣子默认下发的音频包大小不固定，范围从几百字节到十几 KB 不等，这可能影响音频流的稳定性。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272774%27%20height=%27580.4554913294797%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc3NCIgaGVpZ2h0PSI1ODAuNDU1NDkxMzI5NDc5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 为了优化传输，你可以在 chat.update 事件中通过设置output_audio.pcm_config 的 frame_size_ms 字段，为每个音频包指定一个固定的音频时长。设置后，扣子会将音频分割成大小均匀的数据包进行下发。​

  * 以下配置用于将音频按 50ms 的时长进行打包。​

  * ​

TypeScript

复制

{​

"id": "event_id", ​

"event_type": "chat.update", ​

"data": {​

// ...其他配置​

"output_audio": {​

"codec": "pcm", // 适用于 G711A 和 G711U​

"pcm_config": {​

"frame_size_ms": 50 // 单位 ms​

}​

}​

}​

}​

​

  * 配置后，下发的音频包会按照 50ms 每包的固定大小进行传输。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271280%27%20height=%27389.1791907514451%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4MCIgaGVpZ2h0PSIzODkuMTc5MTkwNzUxNDQ1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * OPUS 编码​

  * 对于 OPUS 编码的音频输出，扣子默认会以每帧（包）10ms 的时长下发数据。如需调整，你需要在 chat.update 事件中配置 output_audio.opus_config。​

  * ​

TypeScript

复制

{​

"id": "event_id", ​

"event_type": "chat.update", ​

"data": {​

// ...其他配置​

"output_audio": {​

"codec": "opus", ​

"opus_config": {​

// 默认值为 10。根据 OPUS 规范，只能从 2.5、5、10、20、40、60 这几个固定值中选择，不能设置为其他数值。​

"frame_size_ms": 40,​

"use_cbr": true, // 是否使用 cbr，默认是 false​

"bitrate": 48000 // 输出 opus 的码率，默认是 48000​

}​

}​

}​

}​

​

  * 配置音频下发速率​

  * 通过 chat.update 事件的 output_audio.pcm_config.limit_config 设置音频下发速率：​

  * 注意

为防止播放卡顿，请务必确保参数配置满足 max_frame_num * frame_size_ms >= period * 1000。此条件可以保证音频下发速度跟上播放速度。你还可以根据客户端本地缓冲区的大小来调整 max_frame_num，以更好地应对网络延迟。​

​

  * PCM/G711 编码​

​

TypeScript

复制

{​

"id": "event_id", ​

"event_type": "chat.update", ​

"data": {​

// ...其他配置​

"output_audio": {​

"codec": "pcm", // 适用于 G711A 和 G711U​

"pcm_config": {​

// 每个音频包 100ms​

"frame_size_ms": 100,​

// 通过 limit_config 设置 1s 内最多返回 10 个音频包​

"limit_config": {​

"period": 1,​

"max_frame_num": 10​

}​

}​

}​

}​

}​

​

​

OPUS 编码​

​

TypeScript

复制

{​

"id": "event_id", ​

"event_type": "chat.update", ​

"data": {​

// ...其他配置​

"output_audio": {​

"codec": "opus", // 适用于 OPUS​

"pcm_config": {​

// 每个音频包 60ms​

"frame_size_ms": 60,​

// 通过 limit_config 设置 1s 内最多返回 10 个音频包。​

"limit_config": {​

"period": 1,​

"max_frame_num": 10​

}​

}​

}​

}​

}​

​

​

​

  * 设置后，如下图所示，将从 11:44:13:237 开始下发 10 个 100ms 的音频包，接着从11:44:14:237 开始下发 10 个 100ms 的音频包。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273297%27%20height=%271154.9028901734105%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI5NyIgaGVpZ2h0PSIxMTU0LjkwMjg5MDE3MzQxMDUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

分析智能体耗时定位性能瓶颈​

如果自身接入服务的耗时与官方 Demo 接近甚至更短，即表明是智能体的原因导致延迟。官方 Demo 默认配置基础的智能体，而实际业务中配置的智能体通常包含复杂工作流、插件调用、多工具协同等额外处理逻辑，这些环节容易造成性能瓶颈，建议按以下步骤排查智能体处理耗时。​

排查步骤​

1.

在扣子的空间管理>发布管理页面，选择目标智能体。​

2.

在日志详情页找到对应用户输入，查看首次响应耗时。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27777%27%20height=%27189%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzc3IiBoZWlnaHQ9IjE4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

如果首次响应耗时较长，请参考以下建议进行优化。​

优化建议​

智能体的核心体验主要受稳定性、响应速度、推理效果和链路效率这几个因素影响。你可以参考以下建议进行优化。​

  * ​

优化建议​| 说明​| 参考文档​  
---|---|---  
保障服务稳定性​| 仅当 Agent 使用火山方舟接入点时，你可以通过火山方舟平台自行购买 TPM 保障包，以获得更高的服务稳定性和 SLA 保障。​
    * 说明精调模型不支持 TPM 保障包，这类模型需购买模型单元来保障服务。​​
| [火山方舟 TPM 保障包](<https://www.volcengine.com/docs/82379/1544106?lang=zh#95750410>)​  
平衡速度与推理效果​| 选择 Lite/Flash 系列模型（例如 doubao1.6-flash），并关闭 thinking 模式，可获得更快的响应速度；但该操作会导致推理回复效果有所减弱，需根据业务场景权衡选择。​| ​模型服务​  
降低模型响应时间​| 模型响应时间取决于 TTFT（首 Token 生成时间）和 TPOT（后续 Token 生成时间）。当 TTFT 耗时相对固定时，可以通过减少输出的 Token 数量来有效缩短总响应时间。​| ​优化大模型响应时间​  
提升工作流效率​| 对智能体的工作流编排进行优化，精简链路中的冗余环节，提升智能体的运行效率。​| ​搭建低延时语音助手​  
  
​

技术支持​

如果通过上述自助排查步骤仍无法解决问题，企业版（标准版、旗舰版）付费套餐用户可由火山引擎提供专属售后服务。你可以通过[火山售后在线咨询](<https://console.volcengine.com/coze-pro/overview?entry=ConsoleSideBarAftermarket&openVcopilot={"query":"","displayMode":"fullscreen"}&vcopilotExtraInfo={"accountPlanName":"企业版"}>)提交工单，获取人工客服支持。提交工单时，你需要提供LogID ，以便工程师尽快定位你的问题。​

​

协议​| 获取方式​  
---|---  
WS ​​| WS 回包中的 detail 下的 logID 字段​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271407%27%20height=%27170.29971181556195%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQwNyIgaGVpZ2h0PSIxNzAuMjk5NzExODE1NTYxOTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
HTTP​| Http Response Header 中的 x-tt-logID 字段​  
  
​

​

上一篇

硬件设备基于 WebSocket 实现语音交互

下一篇

通过关键词打断语音对话