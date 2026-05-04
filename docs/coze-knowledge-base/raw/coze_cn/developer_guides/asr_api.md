---
source_url: https://docs.coze.cn/developer_guides/asr_api
title: '双向流式语音识别 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:22:10Z
---

# 双向流式语音识别 - 文档 - 扣子

双向流式语音识别

扣子编程提供流式语音识别 WebSocket OpenAPI，可以将指定的音频判断转为文字，支持识别中英文双语种。​

双向流式语音识别场景下的各类事件详细信息可参考​双向流式语音识别事件。​

接口信息​

​

URL​| wss://ws.coze.cn/v1/audio/transcriptions​  
---|---  
Headers​| Authorization Bearer $Access_Token​用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息请参考[准备工作](<https://www.coze.cn/docs/developer_guides/preparation>)。​  
权限​| createTranscription​  
接口说明​| 将指定的音频判断转为文字，支持识别中英文双语种。​  
  
​

建连示例代码​

ws module(Node.js)

websocket-client(Python)

Websocket(browsers)

​

​

JavaScript

复制

import WebSocket from 'ws';​

​

const url = `wss://ws.coze.cn/v1/audio/transcriptions?authorization=Bearer ${ACCESS_TOKEN}`;​

const ws = new WebSocket(url);​

​

ws.on('open', function open() {​

console.log('Connected to server.');​

});​

​

ws.on('message', function incoming(message) {​

console.log(JSON.parse(message.toString()));​

});​

​

​

​

API 时序图​

交互流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27526.4739884393064%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjUyNi40NzM5ODg0MzkzMDY0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

上一篇

Realtime 事件错误码

下一篇

双向流式语音识别事件