---
source_url: https://docs.coze.cn/developer_guides/tts_api
title: '双向流式语音合成 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:22:15Z
---

# 双向流式语音合成 - 文档 - 扣子

双向流式语音合成

扣子编程提供流式语音合成 WebSocket OpenAPI，可以将文字信息转为指定音色的语音片段。​

双向流式语音合成场景下的各类事件详细信息可参考​双向流式语音合成事件。​

接口信息​

​

URL​| wss://ws.coze.cn/v1/audio/speech​  
---|---  
Headers​| Authorization Bearer $Access_Token​用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息请参考[准备工作](<https://www.coze.cn/docs/developer_guides/preparation>)。​  
权限​| createSpeech​  
接口说明​| 将文字信息转为指定音色的语音片段。​  
  
​

限制说明​

单次请求的文字信息长度最大为 1024 个字节。超过上限时会提示 3010 错误。​

建议一次性不要传输太多文字。​

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

const url = `wss://ws.coze.cn/v1/audio/speech?authorization=Bearer ${ACCESS_TOKEN}`;​

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

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27619%27%20height=%27580%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE5IiBoZWlnaHQ9IjU4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

双向流式语音识别事件

下一篇

双向流式语音合成事件