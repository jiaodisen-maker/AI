---
source_url: https://docs.coze.cn/cozeloop/tool-parameter-correctness-evaluator
title: '轨迹-工具参数填充正确性评估器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:58:22Z
---

# 轨迹-工具参数填充正确性评估器 - 文档 - 扣子

轨迹-工具参数填充正确性评估器

评估器信息​

​

分类​| ​| 详情​  
---|---|---  
基础信息​| 评估器名称​| 轨迹-工具参数填充正确性​  
​| 评估器类型​| 黑盒评估器，评估标准的明细不对客展示​  
效果说明​| 功能概述 ​| 本评估器会评测 Agent 运行轨迹中，所有工具的定义与调用参数，判断工具参数填充是否完整，参数的数据类型正确，且没有幻觉入参​  
​| 评估方式 ​| 复合评估器（LLM + Code）​  
​| 评估对象 ​| Agent​  
​| 评估目标 ​| 工具调用​  
​| 应用场景 ​| Agent 通用评测​  
​| 评估规则说明​| 0<=X<=1分，0分代表工具调用参数填充不准确，1分代表工具调用参数填充不准确。具体样例如下：​本次工具调用评估如下： ​1\. 必需参数完整率：1.0（完整） - Schema 定义的参数只有一个：query，类型为 string，且从语义上可视为必需参数。 - 实际调用为：{"query":"哈尔滨 冰雪大世界 2024-2025 开放时间 门票 官方"} - 已正确提供 query 参数，没有缺失任何必需参数，因此必需参数完整率为 1.0。 ​2\. 类型一致率：1.0（完全一致） - Schema 中 query 的类型为 string。 - 调用中 query 的值为 "哈尔滨 冰雪大世界 2024-2025 开放时间 门票 官方"，是标准字符串类型。 - 没有出现类型不符的情况，因此类型一致率为 1.0。 ​3\. 无幻觉参数率：1.0（无幻觉） - Schema 中仅定义了 query 这一参数。 - 调用参数中也仅包含 query，没有多出任何 Schema 未定义的字段。 - 因此不存在幻觉参数，无幻觉参数率为 1.0。 ​综合以上三个维度，工具调用在必需参数、类型匹配和参数范围上均完全符合 Schema，故给出综合得分 1.0。​  
​| 评估置信度​| 95%​  
  
​

评估器参数说明​

​

参数​| 参数名称​| 是否必填​| 参数说明​  
---|---|---|---  
输入信息​| trajectory​| 是​| Agent 执行轨迹（必须遵循扣子罗盘定义的轨迹数据格式，详情参见 ​轨迹评测介绍 ）​  
输出信息​| result_str​| 是​| 评估分数和具体评估理由​  
  
​

输入格式 (Input Schema)​

​

JSON

复制

{​

"trajectory": {​

"content_type": "text",​

"json_schema": "{\"type\": \"string\"}",​

"text": "String格式的完整轨迹"​

}​

}​

​

输出格式 (Output Schema)​

​

JSON

复制

{​

"score": 1 ，​

"reasoning":"综合评分：1.0（满分）。共评估 7 次工具调用（1 次 search_wiki，6 次 insight_search），在以下三个维度上表现如下：\n\n1. 必需参数完整率\n- search_wiki#1：Schema 要求 keyword（必选），module_name（可选）。调用仅传入 keyword，已覆盖全部必选参数，完整率 100%。\n- insight_search#1~#6：Schema 要求 keyword、kinds 为必选。6 次调用均同时提供 keyword 和 kinds，未缺失任何必选参数，完整率均为 100%。\n\n2. 类型一致率\n- 所有调用中，keyword 均为字符串；kinds 均为枚举值 'type'，符合字符串枚举要求。\n- 传入的 module_names（仅 insight_search#4、#5 调用中使用）均为字符串数组 ['kmp:core']，类型与 Schema 中的 array<string> / null 选型相匹配。\n- 其它可选字段（如 include_external、page、hybrid、module_name）未传入，由默认值处理，不涉及类型冲突。\n=> 所有 7 次调用参数类型与 Schema 定义完全一致，类型一致率为“完全一致”。\n\n3. 无幻觉参数率\n- search_wiki 调用仅使用 keyword 参数，未出现 Schema 中未定义的字段。\n- 全部 insight_search 调用仅使用 keyword、kinds，以及部分调用中的 module_names，均为 Schema 中明确定义的字段。\n- 未发现任何额外多出的、未在 Schema 中声明的“幻觉参数”。\n=> 所有调用均“无幻觉参数”。\n\n综合来看，每一次工具调用在“必需参数完整率”“类型一致率”“无幻觉参数率”三个维度上均达到满分水平，因此整体评分为 1.0。"​

}​

​

​

上一篇

轨迹-工具调用成功率评估器

下一篇

轨迹-工具利用率评估器