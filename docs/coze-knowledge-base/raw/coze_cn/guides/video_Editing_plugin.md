---
source_url: https://docs.coze.cn/guides/video_Editing_plugin
title: '视频剪辑工具插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:41:36Z
---

# 视频剪辑工具插件 - 文档 - 扣子

视频剪辑工具插件

[视频剪辑工具插件](<https://www.coze.cn/store/plugin/7514607196831940643?from=add_plugin_menu>)主要用于视频剪辑操作，包括为视频添加字幕、音视频合成、视频拼接、音频和图片合成视频、视频插帧处理、视频超分辨率处理等功能。​

说明

视频剪辑工具插件 QPS 限额为 1，即包括子用户在内的每个用户 1 秒内最多只能调用 1 次。​

​

计费说明​

视频剪辑工具插件的计费方式为基准计费项✖️抵扣系数✖️时长（分钟），具体的计费项、单价及免费额度，请参考​插件费用。​

不同工具输出不同分辨率的视频或音频时，对应的抵扣系数不同，抵扣系数列表如下。​

例如调用 image_to_video 工具生成一个 90 秒视频，视频分辨率固定为 1080 P，则该工具对应的计费抵扣系数为 6，消耗的积分为 10 积分/分钟 ✖️ 6（系数） ✖️ 1.5 分钟 = 90 积分。​

​

工具​| 抵扣系数​  
---|---  
​add_subtitles 工具​| 该类工具中，不同视频输出规格对应的抵扣系数如下：​

  * 4K（3840x2160）分辨率及以下：24​

  * 2K（2560x1440）分辨率及以下：12​

  * 1080P（1920x1080)分辨率及以下：6​

  * 720P（1280x720）分辨率及以下：3​

  * 540P （720x540）分辨率及以下：2​

  * 480P （640x480）分辨率及以下：1.5​

  * 360P（480x360）分辨率及以下：1​

  * 音频：1​

  
​compile_video_audio 工具​| ​  
​audio_extract 工具​| ​  
​video_trim 工具​| ​  
​concat_videos 工具​| ​  
​compile_image_audio 工具​| ​  
​add_subvideo 工具​| ​  
​add_text 工具​| ​  
​image_to_video 工具​| ​  
​audio_mix 工具​| ​  
​video_speed 工具​| ​  
​ajust_audio_volume 工具​| ​  
​ajust_video_resolution 工具​| ​  
​video_fps 工具​| ​  
​video_flip 工具​| ​  
​audio_loudness_normalization 工具​| ​  
​insert_frame 工具​| 该类工具中，不同视频输出规格对应的抵扣系数如下：​

  * 4K（3840x2160）分辨率及以下：600​

  * 2K（2560x1440）分辨率及以下：300​

  * 1080P（1920x1080)分辨率及以下：150​

  * 720P（1280x720）分辨率及以下：75​

  
​video_super_resolution 工具​| ​  
​video_hdr 工具​| ​  
​audio_denoise 工具​| ​  
​audio_to_subtitle 工具​| 5​  
​audio_separate 工具​| 7​  
  
​

add_subtitles 工具​

add_subtitles 工具会基于视频 URL、字幕文件 URL/自定义文本、字幕样式，为视频添加字幕。配置 add_subtitles 工具时，你可以使用 subtitle_url 参数传入字幕文件 URL 为视频添加字幕，也可以使用text_list 参数传入自定义文本及对应定位信息，在指定位置精准添加字幕。你还可以配置 subtitle_config 参数，用于指定字幕样式配置，包括字体大小、字体 ID、字体颜色及字幕显示位置和尺寸等。​

演示效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27503%27%20height=%27282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAzIiBoZWlnaHQ9IjI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

输入参数​

输入参数说明如下表所示：​

​

输出参数​

输出参数说明如下表所示：​

​

audio_to_subtitle 工具​

audio_to_subtitle 工具用于将音频转换为字幕文件。配置 audio_to_subtitle 工具时，你需要配置 source，用于输入视频或音频 URL，配置 subtitle_type 参数，用于指定输出的字幕文件的格式。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

compile_video_audio 工具​

compile_video_audio 工具用于合成音视频，通过指定待合成的音频和视频 URL，即可轻松合成音视频。此外，该工具还提供额外的灵活配置选项，包括是否保留原视频的音频轨道，以及配置音频、视频同步功能，通过设置同步方法（加速或裁剪）和同步模式（以视频或音频时长为准）来对齐音频和视频时长，从而生成同步的视听内容。​

演示效果​

为原本无声的视频配上背景音乐，效果如下：​

​

​

__

Replay

Play

00:00 / 00:10 Live

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

输入参数​

输入参数说明如下表所示：​

​

输出参数​

输出参数说明如下表所示：​

​

audio_separate 工具​

audio_separate 工具用于分离并输出音频或视频中的人声和背景音乐。在配置 audio_separate 工具时，你需要配置 source 参数，用于输入音频或视频 URL。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

audio_extract 工具​

audio_extract 工具用于抽取视频中的音频，并支持将其保存为指定格式的音频文件。在配置 audio_extract 工具时，你需要配置 video 参数，用于输入视频 URL，配置 format 参数，用于指定输出音频的格式。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

video_trim 工具​

video_trim 工具用于裁剪视频时长，保留从指定的裁剪开始时间到结束时间范围内的视频。在配置 video_trim 工具时，你需要配置 video 参数，用于输入视频 URL，配置 start_time、end_time 参数，用于指定视频裁剪的开始时间和结束时间。​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

concat_videos 工具​

concat_videos 工具内置多种转场效果，只需输入视频 URL 列表和对应的转场效果 ID 列表，工具即会自动按顺序拼接视频，并在各视频片段的拼接处添加指定的转场效果。在配置 concat_videos 工具时，你需要配置 videos 参数，用于输入视频的 URL，并配置 transitions 参数，用于指定视频转场。​

演示效果​

将两个视频合成一个视频，并添加转场，效果如下：​

​

​

__

Replay

Play

00:00 / 00:10 Live

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

输入参数​

输入参数说明如下表所示：​

​

输出参数​

输出参数说明如下表所示：​

​

compile_image_audio 工具​

compile_image_audio 工具用于将音频和图片集合成视频，该工具还提供了多种转场效果，让图片之间的衔接更自然流畅。视频的长度取决于音频长度。在配置 compile_image_audio 工具时，你需要配置 audio 和 images 参数，用于上传视频 URL 和图片 URL，并配置 transitions 参数，用于指定视频转场。​

演示效果​

基于音频和图片集生成视频，视频效果如下：​

​

​

__

Replay

Play

00:00 / 00:20 Live

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

输入参数​

输入参数说明如下表所示：​

​

输出参数​

输出参数说明如下表所示：​

​

insert_frame 工具​

insert_frame 工具基于智能算法，能够在原视频相邻帧之间生成过渡自然的新帧，使视频帧率提升至原来的 2 倍，即如果原视频为 15 FPS，经处理后可变为 30 FPS，能有效改善视频播放时的卡顿感，让画面动作更流畅连贯。在配置 insert_frame 工具时，你需要配置 video 参数，用于输入视频 URL。​

演示效果​

​

输入参数​

输入参数说明如下表所示：​

​

输出参数​

输出参数说明如下表所示：​

​

video_super_resolution 工具​

video_super_resolution 工具基于深度学习方法，能够根据视频信息对其进行空域、时域建模重构出缺失的细节，将低分辨率的视频重建出高分辨率视频。在配置 video_super_resolution 工具时，你需要配置 video 参数，用于输入视频 URL，配置 resolution 参数，用于指定输出视频的分辨率。​

演示效果​

​

输入参数​

输入参数说明如下表所示：​

​

输出参数​

输出参数说明如下表所示：​

​

add_subvideo 工具​

add_subvideo 工具用于为视频添加图片或视频水印。在配置 add_subvideo 工具时，你需要配置 video 参数，用于输入视频 URL，配置 subvideo_url 参数用于输入水印内容，配置 subvideo_config 参数，用于指定水印的样式，包括位置、大小等。其中，水印位置说明如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27306%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2IiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

add_text 工具​

add_text 工具用于为视频添加文字水印。在配置 add_text 工具时，你需要配置 video 参数，用于输入视频 URL，配置 text 参数用于设置水印的内容，配置 text_config 参数，用于指定水印的样式，包括位置、大小、颜色等。其中，水印位置说明如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27306%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2IiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

video_hdr 工具​

video_hdr 工具基于智能算法将 SDR（标准动态范围）视频转换为 HDR （高动态范围）视频，从而提升视频的对比度、色彩丰富度，实现更好的视觉效果。在配置 video_hdr 工具时，你需要配置 video 参数，用于输入视频 URL。​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

ajust_video_resolution 工具​

ajust_video_resolution 工具用于将视频从高分辨率转为低分辨率，例如将 1080P 转换为 720P，用于不同场景的播放。在配置 ajust_video_resolution 工具时，你需要配置 video 参数，用于输入视频 URL。​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

audio_mix 工具​

audio_mix 工具用于对多个音频进行叠加处理，实现混音的效果。在配置 audio_mix 工具时，你需要配置 audios 参数，用于输入多个音频 URL。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

video_speed 工具​

video_speed 工具用于调整视频或音频的播放速度。在配置 video_speed 工具时，你需要配置 video 参数，用于输入视频 URL，配置 speed 参数用于指定速度调整的倍数。​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

ajust_audio_volume 工具​

ajust_audio_volume 工具用于调整视频或音频中的音量。在配置 ajust_audio_volume 工具时，你需要配置 video 参数，用于输入视频或音频 URL，配置 volume 参数用于指定视频或音频中音量的扩大倍数。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

video_fps 工具​

video_fps 工具用于转换视频帧率。配置 video_fps 工具时，你需要配置 video 参数，用于输入视频 URL，配置 fps 参数，用于指定视频的目标帧率。​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

audio_loudness_normalization 工具​

audio_loudness_normalization 工具用于均衡调整音频或视频的音量，避免音量过大过小的现象，提升播放体验。配置 audio_loudness_normalization 工具时，你需要配置 video 参数，用于输入视频或音频 URL。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

audio_denoise 工具​

audio_denoise 工具用于去除视频或音频中的噪声，提升音质体验。配置 audio_denoise 工具时，你需要配置 video 参数，用于输入视频或音频 URL。​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

video_flip 工具​

video_flip 工具用于对视频画面进行翻转，支持上下翻转、左右翻转。配置 video_flip 工具时，你需要配置 video 参数，用于输入视频 URL，你还可以配置 xflip或 yflip 参数，用于指定视频的翻转方向​

演示效果​

​

输入参数​

​

输出参数​

输出参数说明如下表所示：​

​

image_to_video 工具​

image_to_video 工具用于将图片转换为视频。在配置 image_to_video 工具时，你需要配置 images 参数，用于输入图片 URL、图片播放时长和动画效果等信息。​

演示效果​

​

输入参数​

​

输出参数​

​

​

* 视频剪辑工具插件 ID：7514607540051640360​

上一篇

Doubao-SeedEdit-3.0 插件

下一篇

视频生成插件