---
source_url: https://docs.coze.cn/guides/music_agent_plugin
title: '音乐搜索和播放插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:41:56Z
---

# 音乐搜索和播放插件 - 文档 - 扣子

音乐搜索和播放插件

[音乐搜索和播放插件](<https://www.coze.cn/store/plugin/7524979011345236014>)支持根据输入的提示词搜索并播放字节易颂曲库中的歌曲。插件后台集成了字节易颂曲库中的几万首歌曲，涵盖了各种风格和类型的歌曲，包括抖音热门歌曲等。用户可以在语音通话过程中，通过语音指令，使低代码智能体搜索并播放歌曲，为用户提供全新的音乐体验。​

体验效果​

以下展示了 [WebSocket 实时语音 Demo](<https://www.coze.cn/open-platform/realtime/websocket>)，在语音通话过程中通过语音指令使智能体播放歌曲的效果。​

​

​

__

Replay

Play

00:00 / 01:07 Live

00:00

Fullscreen 

Cssfullscreen 

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag 

​

​

使用限制​

  * 仅扣子企业旗舰版用户支持使用音乐搜索和播放插件。​

  * 该音乐插件有版权协定，需要在添加插件时签署补充用户协议后才可以用。​

  * 扣子主账号内所有子账号共享音乐搜索和播放插件的并发限制为 10 。​

计费说明​

音乐搜索和播放插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

在调用 music_agent 工具时，你需要输入提示词，播放指定风格的歌曲。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 是否必选​| 说明​  
---|---|---  
content​| 必选​| 输入提示词内容，用于指定播放的歌曲风格或具体歌曲名称，例如：播放一首适合作为背景音的轻音乐。​  
session_id​| 可选​| 该参数用于关联对话上下文，帮助插件在多轮对话中更好的理解用户意图。如果未传入 session_id，每轮对话结束后上下文将自动清空。建议将 session_id 的值设置为扣子编程的 Conversation ID。​示例说明：​假设用户在第一轮对话中说：“播放一首轻松的音乐。”在下一轮对话中说：“换一首音乐。”如果使用了上下文关联（即传入了 session_id），插件会理解“换一首音乐”仍然是指“轻松的音乐”。如果没有上下文关联，插件可能无法很好的理解用户的意图。​使用方法：​

1.在开始节点的输入参数中添加 session_id 参数，在插件节点引用该参数。​

2.在语音通话时为自定义参数赋值。通过在chat_config.parameters中为session_id 赋值，传入 Conversation ID 的值，具体请参见​为自定义参数赋值。你可以在[发起对话](<https://www.coze.cn/docs/developer_guides/chat_v3>)接口 Response 中查看 Conversation ID 的值。​
  
  
​

输出参数​

​

参数​| 说明​  
---|---  
code​| 执行插件时的状态码。​  
log_id​| 日志 ID。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
data.songs.song_id​| 歌曲 ID。​  
data.songs.play_url​| 歌曲的 URL 链接，链接有效期为 1 小时。​当插件返回多首歌曲时，语音通话中默认播放第一首歌曲。​  
data.songs.play_vid​| 歌曲的视频 ID。​  
  
​

示例​

本文以搭建一个支持音乐播放与语音聊天的对话流模式智能体为例，通过意图识别精准判断用户需求，从而决定是播放音乐还是进入闲聊模式。​

1.

搭建一个既支持播放音乐又支持闲聊的对话流，对话流的整体设计类似如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272227%27%20height=%27517.4878612716763%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIyNyIgaGVpZ2h0PSI1MTcuNDg3ODYxMjcxNjc2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 配置节点如下：​

  * ​

节点​| 说明​| 示例​  
---|---|---  
开始节点​| 如果需要插件更好的理解上下文，你可以在开始节点添加 session_id 参数，以便在插件节点引用该参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27138.3177570093458%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjEzOC4zMTc3NTcwMDkzNDU4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
意图识别节点​| 智能体对用户输入的语音指令进行意图识别，判断用户是否需要播放音乐。如果是，则调用音乐搜索和播放插件。如果不是，则进入闲聊节点。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27244.23676012461058%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI0NC4yMzY3NjAxMjQ2MTA1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
音乐搜索和播放插件​| 添加音乐搜索和播放插件中的 music_agent 工具，并设置相关参数的值，具体说明如下：​
    * content 参数：引用开始节点的 USER_INPUT 变量，用于获取用户输入的提示词内容。​
    * session_id 参数：引用开始节点中的 session_id 参数，以便插件更好的理解上下文。如果不传入 session_id，则每轮对话时都会清空上下文。​
​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27255.45171339563862%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI1NS40NTE3MTMzOTU2Mzg2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
延时安抚（输出节点）​| 由于音乐搜索链路耗时较长，可以在插件节点前，增加输出节点，流式输出安抚的内容，提升用户等待体验。​当用户发送完消息后，智能体会返回安抚话术，例如 ：正在查询音乐。​说明安抚内容的结尾需要加标点符号，因为扣子编程语音合成需要识别到断句后才会将文本转换为语音。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27173.83177570093457%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE3My44MzE3NzU3MDA5MzQ1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
文本输出（输出节点）​| 在插件节点后，你还可以增加输出节点，引导用户进行下一轮对话。​当插件播放完音乐后，智能体会返回引导句，例如 ：你还想听什么呢？。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27171.9626168224299%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE3MS45NjI2MTY4MjI0Mjk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
闲聊（大模型节点）​| 根据实际需求设计闲聊节点的提示词，包括回复逻辑和风格等。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27343.3021806853583%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjM0My4zMDIxODA2ODUzNTgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
结束节点​| 结束节点不需要设置输出变量，智能体直接获取插件或闲聊节点的输出。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27117.13395638629282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjExNy4xMzM5NTYzODYyOTI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

2.

测试并发布智能体。​

a.

试运行并发布对话流后，在智能体中添加对话流，在智能体右侧的调试页面打开语音通话，验证通过语音指令使智能体播放音乐。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27390.97222222222223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM5MC45NzIyMjIyMjIyMjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

发布智能体至 API 渠道。​

  * 后续可以通过 WebSocket 或 RTC 等方式实现语音通话功能，具体请参见​智能音视频概述。​

3.

体验效果。​

  * 在​体验智能音视频 Demo页面，通过语音指令验证智能体播放音乐的实际效果。​

常见问题​

如果曲库中没有对应歌曲怎么办？​

如果曲库中没有对应版权的歌曲，智能体会提示未找到对应版权的歌曲，请换一首。​

此外，当插件未返回歌曲时，本次插件调用不会收取费用。​

​

​

* 音乐搜索和播放插件 ID：7524979194451935283​

上一篇

视频生成插件

下一篇

Doubao-音乐生成插件