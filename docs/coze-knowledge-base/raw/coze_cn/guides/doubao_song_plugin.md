---
source_url: https://docs.coze.cn/guides/doubao_song_plugin
title: '音乐生成插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:42:00Z
---

# 音乐生成插件 - 文档 - 扣子

音乐生成插件

[音乐生成插件](<https://www.coze.cn/store/plugin/7449355471418359845>)支持根据输入的提示词、歌词、演唱者性别、音乐曲风、情感风格等信息，生成对应的音乐作品。​

音乐生成插件包含 gen_song 工具和 lyrics_gen_song 工具。​

使用限制​

扣子主账号内所有子账号共享音乐生成插件的并发限制 ，其值为 1。​

计费说明​

音乐生成插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

说明

音乐生成插件内包含多个工具，调用这些工具的次数将共同计入该插件的免费额度。​

​

gen_song 工具​

gen_song 工具支持根据提示词生成一首特定风格或主题的歌曲。​

配置说明​

在调用 gen_song 工具时，你需要输入提示词，也可以补充演唱者性别、音乐曲风、情感风格等配置，生成指定风格的歌曲。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
Prompt​| 输入歌词提示词内容，仅支持中文，且需小于 500 个字符。必填选项。​  
Gender​| 设置演唱者性别，影响生成歌曲的声音特征。可选值Male（男声）、Female（女声）。​  
Genre​| 设置音乐曲风，决定生成歌曲的音乐风格。可选值：Folk、Pop、Rock、Chinese Style、Hip Hop/Rap、R&B/Soul、Punk、Electronic、Jazz、Reggae、DJ, default value is R&B/Soul。​  
Mood​| 设置歌曲的情感风格，影响旋律和编曲的情绪表达。可选值：Happy、Dynamic/Energetic、Sentimental/Melancholic/Lonely、Inspirational/Hopeful、Nostalgic/Memory、Excited、Sorrow/Sad、Chill、Romantic。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
code​| 执行插件时的状态码。​  
log_id​| 日志 ID。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
data.FailureReason.Code​| 生成失败的错误码。​  
data.FailureReason.Msg​| 生成失败的错误信息。​  
data.SongDetail.AudioUrl​| 歌曲 URL。URL 有效期为 30 天，请及时转存。​  
data.SongDetail.Captions​| 歌曲文本字幕。​  
data.SongDetail.Duration​| 歌曲时长。​  
data.SongDetail.Lyrics​| 歌曲歌词。​  
data.Status​| 任务状态。​  
data.TaskID​| 任务 ID。​  
  
​

示例​

调用 gen_song 工具生成一首关于儿童节的歌曲，输入提示词为 生成一首关于儿童节的歌曲。你可以通过输出参数中的歌曲链接，聆听这首歌曲。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27505%27%20height=%27536%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA1IiBoZWlnaHQ9IjUzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

lyrics_gen_song 工具​

lyrics_gen_song 工具支持根据指定歌词生成音乐作品。​

配置说明​

在调用 lyrics_gen_song 工具时，你需要提供歌词内容，也可以补充演唱者性别、音乐曲风、情感风格等配置，生成指定风格的歌曲。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
Lyrics​| 输入歌词内容，仅支持中文，且需小于 500 个字符。必填选项。​  
Duration​| 设置歌曲的时长，单位：秒，取值范围为 30～240。​  
Gender​| 设置演唱者性别，影响生成歌曲的声音特征。可选值：Male（男声）、Female（女声）。​  
Genre​| 设置音乐曲风，决定生成歌曲的音乐风格。可选值：Folk、Pop、Rock、Chinese Style、Hip Hop/Rap、R&B/Soul、Punk、Electronic、Jazz、Reggae、DJ。​  
Mood​| 设置歌曲的情感风格，影响旋律和编曲的情绪表达。可选值：Happy、Dynamic/Energetic、Sentimental/Melancholic/Lonely、Inspirational/Hopeful、Nostalgic/Memory、Excited、Sorrow/Sad、Chill、Romantic。​  
Timbre​| 设置歌曲的音色。可选值：Warm、Bright、Husky、Electrified voice、Sweet_AUDIO_TIMBRE、Cute_AUDIO_TIMBRE、Loud and sonorous、Powerful、Sexy/Lazy。​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
code​| 执行插件时的状态码。​  
log_id​| 日志 ID。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
data.FailureReason.Code​| 生成失败的错误码。​  
data.FailureReason.Msg​| 生成失败的错误信息。​  
data.SongDetail.AudioUrl​| 歌曲 URL。URL 有效期为 30 天，请及时转存。​  
data.SongDetail.Captions​| 歌曲文本字幕。​  
data.SongDetail.Duration​| 歌曲时长。​  
data.SongDetail.Lyrics​| 歌曲歌词。​  
data.Status​| 任务状态。​  
data.TaskID​| 任务 ID。​  
  
​

示例​

调用 lyrics_gen_song 工具重新创作歌曲，输入歌词 小燕子穿花衣年年春天来这里。你可以通过输出参数中的歌曲链接，聆听这首歌曲。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27581%27%20height=%27626%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgxIiBoZWlnaHQ9IjYyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

* 音乐生成插件 ID：7449356525468090378​

上一篇

Doubao-音乐生成插件

下一篇

语音合成插件