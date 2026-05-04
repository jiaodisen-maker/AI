---
source_url: https://docs.coze.cn/developer_guides/streaming_chat_api
title: '双向流式语音对话 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:22:20Z
---

# 双向流式语音对话 - 文档 - 扣子

双向流式语音对话

扣子编程提供流式语音对话 WebSocket OpenAPI，向指定的智能体发起语音对话。​

双向流式语音对话场景下的各类事件详细信息可参考​双向流式对话上行事件。​

接口信息​

​

URL​| wss://ws.coze.cn/v1/chat​  
---|---  
Headers​| Authorization Bearer $Access_Token​用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息请参考[准备工作](<https://www.coze.cn/docs/developer_guides/preparation>)。​  
权限​| chat​  
接口说明​| 向指定的智能体发起语音对话。​  
  
​

Query​

​

参数​| 类型​| 是否必选​| 说明​  
---|---|---|---  
bot_id​​| String ​​| 必选​​| 需要关联的智能体 ID。​进入智能体的开发页面，开发页面 URL 中 bot 参数后的数字就是智能体 ID。例如 https://www.coze.com/space/341****/bot/73428668*****，Bot ID 为 73428668*****。 ​说明

  * 确保调用该接口使用的令牌开通了此智能体所在空间的权限。​

  * 确保该智能体已发布为 API 服务。​

​  
device_id​| String​| 可选​| 设备的唯一标识符，在建立 Websocket 连接时建议带上此参数，便于排查问题。​说明device_id 的格式为 int64 数字类型的字符串。如果设备 ID 是纯数字， 可直接填写该数字作为 device_id。如果设备 ID 包含非数字字符，则需先将其转换为纯数字字符串，再填写到 device_id 中。​​  
  
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

const url = `wss://ws.coze.cn/v1/chat?bot_id=${BOT_ID}&authorization=Bearer ${ACCESS_TOKEN}`;​

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

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27633%27%20height=%27617%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMzIiBoZWlnaHQ9IjYxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

双向流式语音合成事件

下一篇

双向流式对话上行事件