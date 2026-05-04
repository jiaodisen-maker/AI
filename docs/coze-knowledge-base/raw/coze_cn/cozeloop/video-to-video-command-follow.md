---
source_url: https://docs.coze.cn/cozeloop/video-to-video-command-follow
title: '视频生视频-指令遵循评估器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:58:36Z
---

# 视频生视频-指令遵循评估器 - 文档 - 扣子

视频生视频-指令遵循评估器

评估器信息​

​

分类​| ​| 详情​  
---|---|---  
基础信息​| 评估器名称 ​| 视频生视频-指令遵循​  
​| 评估器类型 ​| 黑盒评估器，评估标准的明细不对客展示​  
效果说明​| 功能概述 ​| 视频生视频需评估生成结果对用户诉求的遵循能力，核心指标包括：主体遵循,属性遵循度,背景遵循度,结构遵循度​  
​| 评估方式 ​| 复合评估器（LLM + Code）​  
​| 评估对象 ​| 图片​  
​| 评估目标 ​| 内容质量​  
​| 应用场景 ​| AIGC 产物质量评估​  
​| 评估规则说明​| 评估生成结果对用户诉求的遵循能力，核心指标包括：①主体遵循度：核心人物/动物/物体是否出现、身份是否正确、数量是否匹配；图生视频若有参考图，需严格一致（人脸/外观）。②属性遵循度：服装颜色材质、动作姿态与幅度、交互、表情、风格等细节是否符合；动作判定需极严（站/坐等），若要求说话则口型运动应自然。③背景遵循度：场景环境、光影、天气是否吻合，并检查是否存在不自然切换、模糊或破绽。④结构遵循度：镜头推拉摇移、视角选择、时序逻辑与空间布局是否合理连贯。⑤约束遵循度：否定指令、排除项及数量/范围限制是否被严格满足。​\- 4分 (完美) ：所有考察点均满足。​\- 3分 (优秀) ：所有重要考察点满足，存在次要考察点不满足。​\- 2分 (一般) ： 任意 重要考察点不满足 （默认上限）。​\- 1分 (差) ：核心重要考察点严重违反或多个重要考察点不满足，但画面仍有相关性。​\- 0分 (极差) ：核心需求完全缺失、严重幻觉、完全不可用。​  
​| 评估置信度​| 80.00%​  
  
​

评估器参数说明​

​

参数​| 参数名称​| 是否必填​| 参数说明​  
---|---|---|---  
输入信息​| query​| 是​| 用户指令​  
​| reference_imgs​| 是​| 用户输入图片​  
​| reference_videos​| 是​| 用户输入视频​  
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

"text": "帮我生成一个视频。将视频中的老人替换为穿牛仔衣的年轻男子，同步原视频的说话、手势动作，保留原场景光影。帮我生成一个视频。时长 5s，模型 2.0。"​

},​

"{{reference_imgs}}": {​

"content_type": "multi_part",​

"multi_part": [​

{​

"content_type": "image",​

"image": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/images/1768995934.png_1769002973"​

}​

},​

{​

"content_type": "image",​

"image": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/images/1768997519.png_1769002973"​

}​

},​

{​

"content_type": "image",​

"image": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/images/1768997515.png_1769002974"​

}​

},​

{​

"content_type": "image",​

"image": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/images/1768997517.png_1769002974"​

}​

}​

]​

},​

"{{reference_videos}}": {​

"content_type": "multi_part",​

"multi_part": [​

{​

"content_type": "video",​

"video": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/z-project/v2v/videos/ogvlQ7gZfRIuzVVWLDxpsVBexEANFpi5Dc4EW7.mp4"​

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

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/kling_20260116_%E4%BD%9C%E5%93%81_%E6%8A%8A_%E8%A7%86%E9%A2%911_%E4%B8%AD%E7%9A%84%E5%B0%8F%E5%A5%B3_4573_0.mp4"​

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

"打分细节": "", //具体的评分依据​

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

​

上一篇

文/图生视频-指令遵循评估器

下一篇

视频-运动真实性评估器