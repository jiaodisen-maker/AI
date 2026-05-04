---
source_url: https://docs.coze.cn/developer_guides/realtime_error_codes
title: 'Realtime 事件错误码 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:22:08Z
---

# Realtime 事件错误码 - 文档 - 扣子

Realtime 事件错误码

本文介绍音视频通话过程中下行事件返回的错误码及其解决方案。​

​

​

code​| msg​| 说明​  
---|---|---  
4027​| Your account has an overdue payment, please recharge immediately.​| 

  * 原因：账户欠费。​

  * 解决方案：请检查[账户余额](<https://console.volcengine.com/coze-pro/overview>)。​

  
4028​| Insufficient coze credits balance, please wait for the quota refresh or upgrade to paid version.​| 

  * 原因：免费版资源点不足。​

  * 解决方案：请检查[账户余额](<https://console.volcengine.com/coze-pro/overview>)。​

  
4029​| The connection was closed due to prolonged user inactivity. Please retry your request.​| 

  * 原因: 房间长时间没有对话，自动退出。​

  * 解决方案: 通过​Realtime 上行事件修改 longest_silence_ms 提高房间的静默时间（默认 3 分钟）。退出房间后需要重新创建房间。​

  
  
​

​

上一篇

Realtime 下行事件

下一篇

双向流式语音识别