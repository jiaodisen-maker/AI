---
source_url: https://docs.coze.cn/cozeloop/tool-usage-rate-evaluator
title: '轨迹-工具利用率评估器 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:58:23Z
---

# 轨迹-工具利用率评估器 - 文档 - 扣子

轨迹-工具利用率评估器

评估器信息​

​

分类​| ​| 详情​  
---|---|---  
基础信息​| 评估器名称 ​| 轨迹-工具利用率​  
​| 评估器类型 ​| 黑盒评估器，评估标准的明细不对客展示​  
效果说明​| 功能概述 ​| 本评估器会评测 Agent 运行轨迹中，各个 Model 节点声明好的预期调用工具列表里，实际使用的工具占比，并列出工具清单里，整个运行过程中都没有调用的工具​  
​| 评估方式 ​| Code/规则评估器​  
​| 评估对象 ​| Agent​  
​| 评估目标 ​| 工具调用​  
​| 应用场景 ​| Agent 通用评测​  
​| 评估规则说明​| 0<=X<=1分，0分代表注册工具全部没有调用，1分代表注册工具全部调用。具体样例如下：​正面样例：注册工具使用率为 1.00（使用个数 1 / 总注册个数 1）​反面样例：注册工具使用率为 0.36（使用个数 4 / 总注册个数 11），以下工具被注册但未使用：category_insight_report,planning_failed,generate_template_report,plan_finish_step,knowledge_search,plan_is_completed,content_strategy_gen_by_crowd_segment​  
​| 评估置信度​| 100%​  
  
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

"score" : 0.25 ,​

"reasoning" : "注册工具使用率为 0.25（使用个数 2 / 总注册个数 8），以下工具被注册但未使用：search_abtest_config,insight_search,retrieve_by_identifier,list_wiki_pages,get_wiki_page,search_wiki"​

}​

​

上一篇

轨迹-工具参数填充正确性评估器

下一篇

轨迹-工具重复调用率评估器