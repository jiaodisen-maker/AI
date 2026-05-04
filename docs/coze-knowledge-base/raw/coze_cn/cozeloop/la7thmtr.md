---
source_url: https://docs.coze.cn/cozeloop/la7thmtr
title: '图片-结构正确评估器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:57:23Z
---

# 图片-结构正确评估器 - 文档 - 扣子

图片-结构正确评估器

评估器信息​

​

分类​| ​| 详情​  
---|---|---  
基础信息​| 评估器名称​| 图片-结构正确​  
​| 评估器类型​| 黑盒评估器，评估标准的明细不对客展示​  
效果说明​| 功能概述​| 评估图片中生物体、物体及空间结构的完整性与合理性，检测生成模型的结构理解缺陷。当前仅支持真实人体结构检测，不支持非人体或漫画等非真实人体结构检测​  
​| 评估方式​| LLM 评估器​  
​| 评估对象​| 图片​  
​| 评估目标​| 内容质量​  
​| 应用场景​| AIGC 产物质量评估​  
​| 评估规则说明​| 评分标准：​0分：图像中结构不存在关键结构缺失、极度畸形等验证结构性错误​1分：图像整体结构完整合理，或仅存在局部细微错误，不影响整体结构​  
​| 评估置信度​| 85%​  
  
​

评估器参数说明​

​

参数​| 参数名称​| 是否必填​| 参数说明​  
---|---|---|---  
输入信息​| image_url_list​| 是​| 字段类型list，指待评估图片列表​  
输出信息​| result_str​| 是​| 评估分数和具体评估理由​  
  
​

输入格式 (Input Schema)​

​

JSON

复制

{​

"{{image_url_list}}": {​

"content_type": "multi_part",​

"multi_part": [​

{​

"content_type": "image",​

"image": {​

"url": "https://lf-stark-public.bytetos.com/obj/stark-public/vlm_benchmark/Instructions/output_7.png"​

}​

}​

]​

}​

}​

}​

​

输出格式 (Output Schema)​

​

JSON

复制

{​

"score": {​

"content_type": "Text",​

"text": "4.0"​

},​

"reasoning": {​

"content_type": "Text",​

"text": ""​

}​

}​

​

​

上一篇

图片-文字畸变检测评估器

下一篇

图片-水印检测评估器