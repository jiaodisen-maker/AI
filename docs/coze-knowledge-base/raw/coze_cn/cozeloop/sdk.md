---
source_url: https://docs.coze.cn/cozeloop/sdk
title: 'SDK 概述 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:59Z
---

# SDK 概述 - 文档 - 扣子

SDK 概述

扣子罗盘提供多语言 SDK（Go、Python、Node.js 和 Java），支持开发者通过标准化接口集成 Trace 数据上报。SDK 提供 PAT（个人访问令牌）和 JWT（OAuth 2.0）等多种鉴权协议，确保与扣子罗盘服务的安全高效交互。​

使用 SDK​

扣子罗盘 SDK 支持集成 Eino 和 LangChain 框架，快速实现 AI 应用的接入和数据上报。同时，也支持通过使用扣子罗盘的 API 以更加灵活的方式进行数据上报。你可以通过快速开始教程，查看如何使用扣子罗盘 SDK 实现数据上报。​

说明

在使用扣子罗盘 SDK 进行 Trace 上报前，需要完成应用鉴权。详情请参考​SDK 鉴权。​

​

​

SDK ​| 下载地址​| 使用说明​  
---|---|---  
扣子罗盘 SDK for Go​| [https://github.com/coze-dev/cozeloop-go](<https://github.com/coze-dev/cozeloop-go>)​| ​快速开始​  
扣子罗盘 SDK for Python​| [https://github.com/coze-dev/cozeloop-python](<https://github.com/coze-dev/cozeloop-python>)​| ​快速开始​  
扣子罗盘 SDK for Node.js​| [https://github.com/coze-dev/cozeloop-js](<https://github.com/coze-dev/cozeloop-js>)​| ​快速开始​  
扣子罗盘 SDK for Java​| [https://github.com/coze-dev/cozeloop-java](<https://github.com/coze-dev/cozeloop-java>)​| ​快速开始​  
  
​

异常处理​

  * 错误码：如果成功调用扣子罗盘 的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败，此时 msg 字段中包含详细错误信息。错误码说明，请参考​错误码。​

  * 错误日志：扣子罗盘 SDK 的错误日志，带有cozeloop标识。​

​

上一篇

火山智能体注册

下一篇

SDK 鉴权