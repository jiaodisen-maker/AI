---
source_url: https://docs.coze.cn/guides/video_to_audio_extraction_node
title: '视频提取音频节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:49Z
---

# 视频提取音频节点 - 文档 - 扣子

视频提取音频节点

低代码工作流中的视频提取音频节点能够从视频文件中提取音频，并将其保存为指定格式的音频文件。​

节点说明​

视频提取音频节点可以从视频文件中提取音频，并将其保存为指定格式的音频文件。该功能可应用于视频内容处理、音频提取、多媒体编辑等场景，能够帮助用户快速获取视频中的音频部分，用于进一步的音频处理或分析。​

在低代码工作流中添加视频提取音频节点时，仅需配置视频参数和输出音频的格式，即可快速完成节点配置，提取视频中的音频。​

配置节点​

输入​

视频提取音频节点的输入参数固定为视频，表示从上传的视频中提取音频内容。视频参数为 video 类型，支持如下两种输入方式：​

  * 固定值：直接上传视频文件。​

  * 变量：引用开始节点的输入、上游节点的输出、用户变量、应用变量、系统变量，实现视频文件的动态输入。​

  * 对应变量需为 video 类型。如果要引用的变量值为视频 URL，string 类型，则你需要先将 string 类型转换为 video 类型，例如添加一个子工作流节点（只有开始节点和结束节点），完成数据类型转换。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27584%27%20height=%27129%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bb601ad5515144c78a7d05a27adcf471~tplv-goo7wpa0wc-quality:q75.image)​

​

配置​

在配置区域，你可以配置输出音频格式，以指定输出音频的格式，支持设置为 mp3、wav、aac。​

输出​

节点的输出参数固定为以下参数：​

  * audio：提取到的音频文件链接。​

  * msg：节点执行状态，success 表示执行成功。​

  * log_id：日志 ID。​

异常处理​

默认情况下，节点运行超时、运行异常时，工作流会中断，工作流调试界面或 API 中会返回错误信息。你也可以手动设置节点运行超时等异常情况下的处理方式，例如整体执行超时、是否重试、是否跳转异常分支等。​

​

异常处理设置​| 说明​  
---|---  
整体执行超时​| 整体执行超时是指节点运行的最大耗时，如果超过此时长，则判断为该节点运行超时。​默认情况下，节点的超时时间为 60s，即 1 分钟。你也可以将其改为 0.1s~60s，灵活控制超时时间。​  
重试次数​| 节点运行超时或异常时，默认不重试，你也可以设置为重试 1 次。​  
异常处理方式​| 节点运行超时或异常时，默认中断工作流。你也可以手动修改此节点的异常处理方式：​

  * 中断流程：工作流执行中断，不再运行后续节点。​

  * 返回设定内容：发生异常后，工作流运行不会中断。开发者可自定义设置需要返回的输出字段内容，必须是输出中已定义的字段，且格式为合法的 JSON 格式。另外，节点还会返回输出参数 isSuccess、errorBody，传递节点异常的详细信息。​

  * 执行异常流程：发生异常后，工作流运行不会中断，转而执行异常流程分析，开发者需要为新增的异常分支配置处理流程。异常信息会通过节点的输出参数 isSuccess、errorBody 返回。​

  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27384%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg0IiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

示例​

在工作流中添加视频提取音频节点时，需上传视频及设置输出音频格式。执行完成后，输出结果中将展示抽取到的音频文件 URL。示例中的节点说明如下：​

  * 在开始节点，使用默认的输入参数 input，设置为 File<video> 类型，用于动态上传视频提取音频节点所需的视频文件。​

  * 在视频提取音频节点，设置视频参数引用开始节点的 input 参数；设置输出音频格式为mp3。​

  * 在结束节点，设置输出变量 output 引用视频提取音频节点输出结果中的 audio 参数，用于展示抽取到的音频文件 URL。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27772%27%20height=%27269%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzcyIiBoZWlnaHQ9IjI2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

出现“ffmpeg extra audio failed:exit status 1”错误，如何处理？​

如果在执行视频提取音频节点时，出现“ffmpeg extra audio failed:exit status 1”错误，请按照如下步骤进行排查。​

1.

检查视频文件是否可以正常播放。​

2.

检查视频里是否包含音频。​

上一篇

视频生成节点

下一篇

视频抽帧节点