---
source_url: https://docs.coze.cn/guides/gen_podcast_plugin
title: '语音播客插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:42:07Z
---

# 语音播客插件 - 文档 - 扣子

语音播客插件

[语音播客插件](<https://www.coze.cn/store/plugin/7537546789688213523>)支持根据文本生成双人对话形式的播客音频，广泛应用于播客创作。本文介绍语音播客插件的使用方法。​

插件说明​

用户可以输入一篇现成的文章，或者仅输入一个主题，语音播客插件即可自动生成播客内容和音频。该插件不仅能够智能理解文本内容，还能生成流畅自然的播客音频，支持双人对谈、交叉附和，听觉效果高度拟人化。相比传统的真人播客，该插件具备成本低、速度快、时效性高、个性化等显著优势，为音频内容生产带来高效智能的新体验。​

语音播客插件基于火山引擎[语音播客 API](<https://www.volcengine.com/docs/6561/1668014>) 开发，包含两个工具： genPodcastURL 和 genPodcastStream。​

  * genPodcastURL：基于输入的文本，生成播客内容和音频链接。你可以通过此链接访问生成的播客音频。​

  * genPodcastStream：基于输入的文本，流式返回播客的音频内容。该工具只支持在语音通话场景使用，用户可以在语音通话过程中，通过语音指令，使智能体生成播客，例如输入“大学生暑假如何提升自己”，插件就能即时创作并生成语音播客。​

体验效果​

播客试听：​

​

​

播客音频示例.mp3

​

​

使用限制​

  * 输入内容限制：语音播客插件暂不支持图片理解，也不支持读取 URL 里的内容。​

  * 如果只输入主题，生成的播客会比较短，建议提供更详细的输入。​

费用说明​

语音播客插件将根据豆包语音播客大模型消耗的 Token 数计费。对应的计费项及单价说明，请参考​模型费用。​

说明

  * 在低代码工作流中试运行语音播客插件，或在低代码智能体编排页面通过语音通话生成播客时，均计入豆包语音播客大模型费用，优先消耗赠送的免费额度。​

  * 生成播客所消耗的积分以实际消耗的 Tokens 为准。​

​

以生成一段时长为 30 分钟、语速 150 字/分钟的播客为例，播客插件费用包括输入和输出两部分，具体如下：​

  * 输入：输入 1 个字约消耗 1.5 tokens，输入文本 4500 字将消耗 6.75 千tokens，费用为 6.75*0.12=0.81 元。​

  * 输出：输出 1 秒音频约消耗 25 tokens，输出 30 分钟音频将消耗 45 千tokens，费用为 45*0.1=4.5 元。​

因此本示例中生成 30 分钟的播客，费用约为 5.31 元。​

genPodcastURL​

基于输入的文本，生成播客内容和音频链接。你可以通过此链接访问生成的播客音频。​

输入参数​

输入参数说明如下表所示。​

​

参数名称​| 是否必填​| 说明​  
---|---|---  
input_text ​| 必选​| 播客的文本内容，最多支持 15000 个单词或汉字。​你可以输入一篇现成的文章，或输入一个主题，让插件自动根据输入的文本生成播客内容和音频。​说明

  * 该插件暂不支持图片理解，如果输入的文档中包含图片，会自动跳过图片部分。​

  * 该插件暂不支持读取 URL 里的内容，如果需要实现通过 URL 生成播客内容，你可以在工作流中增加[链接读取](<https://www.coze.cn/store/plugin/7329410795979161663?from=plugin_card>)插件，将获取的 URL 链接中的内容输入给语音播客插件。​

​  
use_head_music​| 可选​| 是否在播客开头添加默认的音效，默认为 false。​你可以在播客音频示例中试听默认音效的效果。​  
  
​

输出参数​

输出参数说明如下表所示。​

​

参数​|  说明 ​  
---|---  
code ​|  返回状态码，0 表示成功，非 0 表示失败，具体错误码请参见​错误码。​  
data.content.podcast_url​|  生成的播客音频的在线文件链接。 默认为 MP3 格式。​说明生成的播客音音频 URL 有效期为 3 天，请及时转存。​  
data.content.text​| 生成的播客文本内容。​  
usage.output_audio_tokens​| 插件输出播客音频所消耗的 Token 数。​  
usage.input_text_tokens​| 输入的内容和提示词所消耗的 Token 数。​  
log_id ​|  日志 ID，用于问题排查和调试。 ​  
msg ​|  执行插件时的状态描述或错误提示信息。 ​  
  
​

示例​

在工作流中添加语音播客插件中的 genPodcastURL 工具。输入播客的文本内容，语音播客插件输出生成的播客音频的在线文件链接。工作流的整体设计类似如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271705%27%20height=%27284.16666666666663%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcwNSIgaGVpZ2h0PSIyODQuMTY2NjY2NjY2NjY2NjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

配置节点说明如下：​

​

节点​| 说明​| 示例​  
---|---|---  
开始节点​| 输入参数使用默认的 input 参数，用于输入播客的文本内容。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27104.63215258855585%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjEwNC42MzIxNTI1ODg1NTU4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
语音播客插件​| 添加语音播客插件中的 genPodcastURL 工具，输入参数 input_text 的值引用开始节点的 input 变量，用于获取待生成播客的文本内容。​注意超时时间需要设置为 600 s，因为生成播客的处理时间可能较长，若超时时间设置过短，容易出现超时错误。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27234.87738419618526%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIzNC44NzczODQxOTYxODUyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
选择器节点​| 如果 genPodcastURL 工具返回的 code 为 0 ，则通过输出节点返回生成的播客音频，否则，则直接结束。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27189.1008174386921%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE4OS4xMDA4MTc0Mzg2OTIxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
输出节点​| 输出节点的输出变量的值引用语音播客插件输出的 data.content.podcast_url 参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27202.724795640327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMi43MjQ3OTU2NDAzMjciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
结束节点​| 结束节点输出变量的值引用语音识别插件输出的 data.text 参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27116.07629427792916%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjExNi4wNzYyOTQyNzc5MjkxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

genPodcastStream​

基于输入的内容，生成语音播客，并流式返回音频内容。用户可以在语音通话过程中，通过语音指令，使智能体生成播客，例如输入“大学生暑假如何提升自己”，插件就能即时创作并生成语音播客。​

输入参数​

输入参数说明如下表所示。​

​

参数名称​| 是否必填​| 说明​  
---|---|---  
input_text ​| 必选​| 播客的主题或内容，最多支持 15000 千个单词或汉字。​说明

  * 如果只输入主题，生成的播客会比较短，建议提供更详细的输入。​

  * 该插件暂不支持图片理解，如果输入的文档中包含图片，会自动跳过图片部分。​

  * 该插件暂不支持读取 URL 里的内容，如果需要实现通过 URL 生成播客内容，你可以在工作流中增加[链接读取](<https://www.coze.cn/store/plugin/7329410795979161663?from=plugin_card>)插件，将获取的 URL 链接中的内容输入给语音播客插件。​

​  
use_head_music​| 可选​| 是否在播客开头添加默认的音效，默认为 false。​你可以在播客音频示例中试听默认音效的效果。​  
  
​

输出参数​

输出参数说明如下表所示。​

​

参数​|  说明 ​  
---|---  
code ​|  返回状态码，0 表示成功，非 0 表示失败，具体错误码请参见​错误码。​  
data​|  生成的播客音频。 默认格式为 PCM，采样率为 24 kHz。​  
log_id ​|  日志 ID，用于问题排查和调试。 ​  
msg ​|  执行插件时的状态描述或错误提示信息。 ​  
  
​

示例​

本文以搭建一个流式生成播客的智能体为例。​

1.

创建对话流，对话流的整体设计类似如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27349.07407407407413%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjM0OS4wNzQwNzQwNzQwNzQxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 在语音播客插件节点，设置 input_text 参数引用开始节点的 USER_INPUT 参数，用于输入生成播客的文本内容。​

  * 注意

语音播客插件节点的超时时间需要设置为 600 s，因为生成播客的处理时间可能较长，若超时时间设置过短，容易出现超时错误。​

​

  * 在结束节点，不需要设置输出变量，智能体直接获取插件节点的输出。​

2.

测试并发布智能体。​

a.

试运行并发布对话流后，在智能体中添加对话流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27408.33333333333337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwOC4zMzMzMzMzMzMzMzMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

发布智能体至 API 渠道。​

  * 后续可以通过 WebSocket 或 RTC 方式实现语音通话功能，具体请参见​智能音视频概述。​

错误码​

​

错误码​| 错误描述​| 说明​  
---|---|---  
702322003​| 并发数超过限制​| 

  * 可能原因：当前请求并发量已达上限 。​

  * 解决方案：稍后重试。​

  
702322002​| 输入的参数错误​| 

  * 可能原因：播客文本内容不符合要求，例如字数超出 15000 字。​

  * 解决方案：根据输入参数的说明检查并修改。​

  
  
​

​

* 语音播客插件 ID：7537547135328419903​

上一篇

语音识别插件

下一篇

火山联网问答插件