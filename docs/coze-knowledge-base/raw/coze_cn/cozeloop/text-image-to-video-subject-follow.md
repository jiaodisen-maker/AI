---
source_url: https://docs.coze.cn/cozeloop/text-image-to-video-subject-follow
title: '文/图生视频-主体遵循度评估器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:58:32Z
---

# 文/图生视频-主体遵循度评估器 - 文档 - 扣子

文/图生视频-主体遵循度评估器

评估器信息​

​

分类​| ​| 详情​  
---|---|---  
基础信息​| 评估器名称 ​| 文/图生视频-主体遵循度​  
​| 评估器类型 ​| 黑盒评估器，评估标准的明细不对客展示​  
效果说明​| 功能概述 ​| 文/图生视频需评估生成结果对用户诉求的遵循能力，主要考察核心人物/动物/物体是否出现、身份是否正确、数量是否匹配；图生视频若有参考图，需严格一致（人脸/外观）​  
​| 评估方式 ​| 复合评估器（LLM + Code）​  
​| 评估对象 ​| 图片​  
​| 评估目标 ​| 内容质量​  
​| 应用场景 ​| AIGC 产物质量评估​  
​| 评估规则说明​| \- 4分 (完美) ：所有考察点均满足。​\- 3分 (优秀) ：所有重要考察点满足，存在次要考察点不满足。​\- 2分 (一般) ： 任意 重要考察点不满足 （默认上限）。​\- 1分 (差) ：核心重要考察点严重违反或多个重要考察点不满足，但画面仍有相关性。​\- 0分 (极差) ：核心需求完全缺失、严重幻觉、完全不可用。​  
​| 评估置信度​| 86.00%​  
  
​

评估器参数说明​

​

参数​| 参数名称​| 是否必填​| 参数说明​  
---|---|---|---  
输入信息​| query​| 是​| 用户指令​  
​| reference_imgs​| 是​| 用户输入图片​  
​| reply_videos​| 是​| 生成的视频视频​  
输出信息​| result_str​| 是​| 评估分数和具体评估理由​  
  
​

输入格式 (Input Schema)​

​

JSON

复制

{​

"{{query}}": {​

"content_type": "text",​

"json_schema": "{\"type\": \"string\"}",​

"text": "帮我生成一个视频：把第二张图男生的灰色连帽卫衣和阔腿牛仔裤穿到第一张图的小女孩身上，让她站在第三张图的幼儿园户外里，开心地对着镜头说：“今天我很酷！”"​

},​

"{{reference_imgs}}": {​

"content_type": "multi_part",​

"multi_part": [​

{​

"content_type": "image",​

"image": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/z-project/i2v/image/5955748_0.png"​

}​

}​

]​

},​

"{{reply_videos}}": {​

"content_type": "multi_part",​

"multi_part": [​

{​

"content_type": "video",​

"video": {​

"url": "https://v3-default.douyin.com/dd8306212af91fa65d11fcdeae0ad110/7c31def6/video/tos/cn/tos-cn-v-9ecd54/2457d493e5144263b30f99c87c8331f1/?a=1938&ch=0&cr=7&dr=0&lr=video_gen_watermark_new_v_sec&cd=0%7C0%7C0%7C1&cv=1&br=1375&bt=1375&cs=4&ds=4&ft=9eVLSJUrBBkq8ZmoB7oaU_vjVQWw&mime_type=video_mp4&qs=0&rc=aTY3OGQ6ODw6MzxnZTVkNkBpand5N2s5cnJ3ODczNGY5M0AtL19gX18vX2MxYTVhNC1hYSNhLTY0MmQ0a2ZhLS1kNi9zcw%3D%3D&btag=c0000e00008000&dy_q=1768283121&feature_id=2fb334f183a6fc38f70ff4979e874b55&l=02176828301761700000000000000000000ffff0a7ab0def80bdb&download=true"​

}​

}​

]​

}​

}​

​

输出格式 (Output Schema)​

​

JSON

复制

{​

"最终得分": "0",// 表示整体的评估分数​

"理由": "", //具体的评分依据​

"782": {}, //主体遵循度的评估分数和理由​

"783": {}, //属性遵循度的评估分数和理由​

"784": {}, //结构遵循度的评估分数和理由​

"785": {}, //约束遵循度的评估分数和理由​

}​

​

​

​

​

​

上一篇

视频生有声视频-语音指令遵循评估器

下一篇

文/图生视频-指令遵循评估器