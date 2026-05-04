---
source_url: https://docs.coze.cn/cozeloop/trajectory-evaluation
title: '轨迹评测介绍 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:38Z
---

# 轨迹评测介绍 - 文档 - 扣子

轨迹评测介绍

你可以在扣子罗盘中评测 Agent 的轨迹。与传统的仅关注输出结果的评测方法不同，轨迹评测的目标是 Agent 的推理过程与执行逻辑，从而验证 Agent 决策链条的合理性。 ​

在扣子罗盘中，只有火山智能体才能被用作轨迹评测的评测对象。详情参见 ​火山智能体注册。​

什么是轨迹​

轨迹（Trajectory）是指 AI Agent 在任务执行过程中生成的结构化时序数据，数据格式为 JSON。轨迹完整记录了从接收用户指令开始，Agent 在多轮交互中进行的思考、行动和观察的全链路历史。​

扣子罗盘定义了轨迹的标准数据结构，旨在将不同开发框架（如 LangChain、Eino）产生的异构 Trace 数据，归一化为标准的 根节点 - Agent 步骤 - 原子步骤 层级架构。详情参见 ​轨迹数据结构说明。​

下面的示例展示了行程规划 Agent 完成 “规划上海行程” 任务时生成的轨迹数据。该轨迹数据的核心内容如下： ​

  * root_step：全局概览，记录了任务的总输入（“规划上海行程”）与最终产出（“因雨调整为博物馆行程”）。通过内置的 metrics_info，评测者无需遍历细节即可了解该任务的健康度：工具调用占比 40%，且主要耗时集中在 LLM 推理（3200ms）而非工具响应上。​

  * agent_steps：Agent 步骤，记录了 Agent 的完整执行流。Agent 处理“天气制约”和“预约规则”的复杂逻辑被封装为一个扁平化的有序列表，清晰界定了本次行程规划的决策边界。​

  * steps：原子步骤，还原了 5 个具体的执行步骤。 ​

  * model 类型的原子步骤：展示了与 LLM 交互的思维链（如“周日下雨 -> 放弃迪士尼 -> 改去博物馆”），并通过 reasoning_tokens 量化了模型处理突发状况的思考深度。 ​

  * tool 类型的原子步骤：记录了 weather_tool 和 search_tool 工具的实际输入输出，验证了 Agent 是否正确获取了“周日大雨”和“需提前3天预约”的关键事实。​

​

JSON

复制

{​

"id": "trace_shanghai_001",​

"root_step": {​

"id": "span_root_001",​

"name": "Travel_Planning_Session",​

"input": "帮我规划上海三日游，这周末出发。",​

"output": "已为你规划行程：周六去外滩和迪士尼（晴天），周日安排上海博物馆（大雨）。注意：博物馆需提前3天预约。",​

"basic_info": {​

"started_at": "1715400000000",​

"duration": "4500"​

},​

"metrics_info": {​

"llm_duration": "3200",​

"tool_duration": "1300",​

"tool_errors": {},​

"tool_error_rate": 0,​

"model_errors": {},​

"model_error_rate": 0,​

"tool_step_proportion": 0.4,​

"input_tokens": 850,​

"output_tokens": 420​

},​

"agent_steps": [​

{​

"id": "span_agent_001",​

"parent_id": "span_root_001",​

"name": "TravelPlannerAgent",​

"input": "帮我规划上海三日游，这周末出发。",​

"output": "已为你规划行程...",​

"basic_info": {​

"started_at": "1715400000100",​

"duration": "4400"​

},​

"metrics_info": {​

"llm_duration": "3200",​

"tool_duration": "1300",​

"tool_errors": {},​

"tool_error_rate": 0,​

"model_errors": {},​

"model_error_rate": 0,​

"tool_step_proportion": 0.4,​

"input_tokens": 850,​

"output_tokens": 420​

},​

"steps": [​

{​

"id": "span_step_001",​

"parent_id": "span_agent_001",​

"type": "model",​

"name": "Reasoning_Weather_Check",​

"input": "用户请求：上海三日游，本周末。",​

"output": "思考：户外活动依赖天气，需先查天气。\nAction: 调用 weather_tool",​

"basic_info": {​

"started_at": "1715400000100",​

"duration": "400"​

},​

"model_info": {​

"input_tokens": 100,​

"output_tokens": 50,​

"reasoning_tokens": 20,​

"latency_first_resp": "400",​

"input_read_cached_tokens": 0,​

"input_creation_cached_tokens": 0​

}​

},​

{​

"id": "span_step_002",​

"parent_id": "span_agent_001",​

"type": "tool",​

"name": "weather_tool",​

"input": "{\"location\": \"Shanghai\", \"date\": \"this_weekend\"}",​

"output": "{\"Saturday\": \"Sunny\", \"Sunday\": \"Heavy Rain\"}",​

"basic_info": {​

"started_at": "1715400000500",​

"duration": "500"​

}​

},​

{​

"id": "span_step_003",​

"parent_id": "span_agent_001",​

"type": "model",​

"name": "Reasoning_Itinerary_Logic",​

"input": "天气结果：周六晴，周日雨。",​

"output": "思考：周日下雨，不能去迪士尼，改去博物馆。需确认博物馆预约规则。\nAction: 调用 search_tool",​

"basic_info": {​

"started_at": "1715400001000",​

"duration": "600"​

},​

"model_info": {​

"input_tokens": 200,​

"output_tokens": 60,​

"reasoning_tokens": 30,​

"latency_first_resp": "300",​

"input_read_cached_tokens": 0,​

"input_creation_cached_tokens": 0​

}​

},​

{​

"id": "span_step_004",​

"parent_id": "span_agent_001",​

"type": "tool",​

"name": "search_tool",​

"input": "{\"query\": \"上海博物馆 预约规则\"}",​

"output": "需提前3天在官网预约，实名制。",​

"basic_info": {​

"started_at": "1715400001600",​

"duration": "800"​

}​

},​

{​

"id": "span_step_005",​

"parent_id": "span_agent_001",​

"type": "model",​

"name": "Final_Response_Generation",​

"input": "博物馆规则：需提前3天预约。",​

"output": "已为你规划行程：周六去外滩和迪士尼（晴天），周日安排上海博物馆（大雨）。注意：博物馆需提前3天预约。",​

"basic_info": {​

"started_at": "1715400002400",​

"duration": "2100"​

},​

"model_info": {​

"input_tokens": 350,​

"output_tokens": 150,​

"reasoning_tokens": 0,​

"latency_first_resp": "500",​

"input_read_cached_tokens": 0,​

"input_creation_cached_tokens": 0​

}​

}​

]​

}​

]​

}​

}​

​

为什么要评测轨迹​

与 LLM 不同，Agent 是一个包括了 LLM、提示词、工具调用、记忆等多个组件的系统。因此，对于 Agent，仅评测最终结果是不够的。轨迹评测能够深入 Agent 系统内部，达到以下效果：​

  * 定位问题节点: 当 Agent 表现不佳时，只看最终结果很难判断问题究竟出在提示词设计、工具调用参数，还是模型推理能力上。轨迹评测能帮助你定位问题发生的具体环节。​

  * 阻断错误传播: Agent 的任务执行是多步串行的，早期步骤的微小偏差（如错误的搜索关键词）会随着链路逐步放大，最终导致任务失败。轨迹评测能帮助你在错误发生的节点定位问题，无需等到最终结果出错后再回溯排查。​

  * 提升执行效率: 结果正确的 Agent 未必是高效的。轨迹评测能识别出冗余的思考步骤、死循环调用或过长的上下文堆积。优化这些低效轨迹可以显著节省 Token 成本、降低响应延时，并更高效地利用 LLM 的上下文窗口。​

扣子罗盘如何获取轨迹数据​

扣子罗盘中的轨迹数据来源于 Trace 数据。​

Trace 是一次完整请求的调用链记录。轨迹的数据结构是通过拼接 Trace 数据中的 agent 节点、model 节点、tool 节点和 graph 节点的输入输出信息形成的结构化序列。虽然不同 Agent 开发框架的 Trace 数据结构存在差异，但是扣子罗盘可以基于不同 Agent 开发框架的 Trace 数据结构自动提取出通用的轨迹数据结构。​

说明

如果你通过以下 SDK 上报 Eino、LangGraph 或 LangChain 的 Trace 数据，请确保使用下面的指定版本或更高版本，以便扣子罗盘能够成功提取轨迹： ​

  * 上报 Eino 的 Trace 数据：go get github.com/cloudwego/eino-ext/callbacks/cozeloop@v0.1.7​

  * 上报 LangGraph 的 Trace 数据：pip install cozeloop==0.1.20 ​

  * 上报 LangChain 的 Trace 数据：npm i @cozeloop/langchain@0.0.3​

​

每种节点对应轨迹数据中不同类型的成员：​

  * agent 节点：即 JSON 数据中的 agent_steps 数组，通常作为父节点存在，负责维护会话状态、管理上下文以及执行决策逻辑。​

  * model 节点：即 JSON 数据的 steps 数组中 type 为 model 的成员， 记录了一次完整的请求响应，负责将结构化的 Prompt 转换为非结构化的文本或结构化的函数调用指令。​

  * tool 节点：即 JSON 数据的 steps 数组中 type 为 tool 的成员， 代表了 Agent 与外部环境（如 Web Search、Database、API）进行的数据交换过程。​

  * graph 节点：即 JSON 数据的 steps 数组中 type 为 graph 的成员，代表每个 LangGraph 或 Eino Graph 的入口点。​

Agent 的 Trace 数据被上报到扣子罗盘后，扣子罗盘可以自动提取出轨迹数据。例如：​

  * 你在查看 Trace 数据时，可以单击 仅展示轨迹节点 按钮查看轨迹数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273044%27%20height=%271916.5925925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA0NCIgaGVpZ2h0PSIxOTE2LjU5MjU5MjU5MjU5MjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 你可以直接从 Trace 数据中把轨迹数据回流到评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273804%27%20height=%271778.7222222222224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgwNCIgaGVpZ2h0PSIxNzc4LjcyMjIyMjIyMjIyMjQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

在实验中，评测对象的实际轨迹数据也可以被发送到评估器。​

如何评测轨迹数据​

你可以通过以下方法来评测轨迹数据：​

  * LLM-as-Judge：利用一个 LLM 作为裁判，依据内置评估器或你自定义的评估器对轨迹数据进行评估并打分。该方法灵活性更强，适用于对 Agent 决策逻辑的评估标准较为灵活、难以用固定匹配规则衡量，需要根据具体场景和规则进行动态评估的场景。 ​

  * 轨迹匹配：使用 code 评估器或预置评估器，检查轨迹中是否包含特定模式，例如 Agent 是否调用了某个工具，或工具的调用是否成功。该方法确定性更强，适用于对 Agent 决策逻辑有明确预期，且期望精准衡量实际表现与理想情况差距的场景。​

轨迹评测的流程​

在扣子罗盘中，评测 Agent 轨迹主要有以下两种流程：​

说明

你可以使用任意一种流程，也可以结合使用这两种流程。例如，你可以把从 Trace 回流的轨迹数据作为参考，用于评测 Agent 实时产生的轨迹数据。参见 ​通过数据回流评测行程规划 Agent 的轨迹。​

​

  * 实时评测：创建实验时，在 评估器 步骤，你可以将评估器的轨迹类型的字段映射到评测对象的轨迹上，从而对评测对象的实时轨迹进行评测。详情参阅 ​实时评测行程规划 Agent 的轨迹。​

  * 注意

评测集中无需包含轨迹数据，但评测集的场景必须是 轨迹评测集。详情参阅 ​管理评测集。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27698%27%20height=%27485%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjk4IiBoZWlnaHQ9IjQ4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 回流后评测：你也可以先将 Trace 数据中的轨迹数据回流到评测集，然后再对评测集中的轨迹数据进行评测。​

轨迹数据与 Trace 数据的区别​

虽然轨迹数据源自 Trace，但两者的抽象层级不同：​

  * Trace：Trace 是未经处理的原始调用链数据。Trace 数据完整记录了系统底层的执行细节，包含工程噪音（如 HTTP Headers、网络延迟、堆栈信息等）。此外，不同开发框架（如 LangChain、Eino）的 Trace 数据结构差异巨大且高度嵌套。因此。Trace 数据不适合直接用于评测。​

  * 轨迹：轨迹是从 Trace 中提炼出的标准化语义序列。扣子罗盘通过清洗和重构，把复杂的调用链扁平化为标准的 根节点 - Agent 交互 - 原子步骤 时序结构。这让评测能够聚焦于 Agent 的决策逻辑与业务表现，而非底层代码实现。​

Trace​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27347%27%20height=%27374%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ3IiBoZWlnaHQ9IjM3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

轨迹​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27354%27%20height=%27435%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU0IiBoZWlnaHQ9IjQzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

轨迹数据结构说明​

轨迹数据结构主要包含以下核心组件： ​

  * root_step： 全局概览，记录整个任务的输入输出与核心指标。包含预聚合的 metrics_info（如 Token 消耗、工具错误率、首字延迟等），支持在不遍历详情的情况下快速评估任务质量。 ​

  * agent_steps： 交互链路，记录 Agent 的逻辑执行流。将复杂的调用链扁平化为有序的步骤列表，清晰还原 Agent 的决策路径。 ​

  * steps： 原子步骤，标准化的执行单元。无论底层实现如何，所有的操作都被统一分类到 agent 节点、model 节点、tool 节点和 graph 节点，并剥离了框架特定的工程噪音，仅保留评测所需的语义信息（如 reasoning_tokens、tool_errors）。 ​

​

JSON

复制

{​

"$schema": "http://json-schema.org/draft-07/schema#",​

"type": "object",​

"title": "Trajectory",​

"description": "Trajectory structure for coze loop tracking",​

"properties": {​

"id": {​

"type": "string",​

"description": "trace_id"​

},​

"root_step": {​

"type": "object",​

"description": "根节点，记录整个轨迹的信息",​

"properties": {​

"id": {​

"type": "string",​

"description": "唯一ID，trace导入时取span_id"​

},​

"name": {​

"type": "string",​

"description": "name，trace导入时取span_name"​

},​

"input": {​

"type": "string",​

"description": "输入"​

},​

"output": {​

"type": "string",​

"description": "输出"​

},​

"metadata": {​

"type": "object",​

"description": "保留字段，可以承载业务自定义的属性",​

"additionalProperties": {​

"type": "string"​

}​

},​

"basic_info": {​

"type": "object",​

"properties": {​

"started_at": {​

"type": "string",​

"description": "单位毫秒"​

},​

"duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"error": {​

"type": "object",​

"properties": {​

"code": {​

"type": "integer"​

},​

"msg": {​

"type": "string"​

}​

}​

}​

}​

},​

"metrics_info": {​

"type": "object",​

"properties": {​

"llm_duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"tool_duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"tool_errors": {​

"type": "object",​

"description": "Tool错误分布，格式为：错误码-->list<ToolStepID>",​

"additionalProperties": {​

"type": "array",​

"items": {​

"type": "string"​

}​

}​

},​

"tool_error_rate": {​

"type": "number",​

"description": "Tool错误率"​

},​

"model_errors": {​

"type": "object",​

"description": "Model错误分布，格式为：错误码-->list<ModelStepID>",​

"additionalProperties": {​

"type": "array",​

"items": {​

"type": "string"​

}​

}​

},​

"model_error_rate": {​

"type": "number",​

"description": "Model错误率"​

},​

"tool_step_proportion": {​

"type": "number",​

"description": "Tool Step占比(分母是总子Step)"​

},​

"input_tokens": {​

"type": "integer",​

"description": "输入token数"​

},​

"output_tokens": {​

"type": "integer",​

"description": "输出token数"​

}​

}​

}​

}​

},​

"agent_steps": {​

"type": "array",​

"description": "agent step列表，记录轨迹中agent执行信息",​

"items": {​

"type": "object",​

"properties": {​

"id": {​

"type": "string",​

"description": "唯一ID，trace导入时取span_id"​

},​

"parent_id": {​

"type": "string",​

"description": "父ID， trace导入时取parent_span_id"​

},​

"name": {​

"type": "string",​

"description": "name，trace导入时取span_name"​

},​

"input": {​

"type": "string",​

"description": "输入"​

},​

"output": {​

"type": "string",​

"description": "输出"​

},​

"steps": {​

"type": "array",​

"description": "子节点，agent执行内部经历了哪些步骤",​

"items": {​

"type": "object",​

"properties": {​

"id": {​

"type": "string",​

"description": "唯一ID，trace导入时取span_id"​

},​

"parent_id": {​

"type": "string",​

"description": "父ID， trace导入时取parent_span_id"​

},​

"type": {​

"type": "string",​

"description": "类型"​

},​

"name": {​

"type": "string",​

"description": "name，trace导入时取span_name"​

},​

"input": {​

"type": "string",​

"description": "输入"​

},​

"output": {​

"type": "string",​

"description": "输出"​

},​

"model_info": {​

"type": "object",​

"description": "type=model时填充",​

"properties": {​

"input_tokens": {​

"type": "integer"​

},​

"output_tokens": {​

"type": "integer"​

},​

"latency_first_resp": {​

"type": "string",​

"description": "首包耗时，单位毫秒"​

},​

"reasoning_tokens": {​

"type": "integer"​

},​

"input_read_cached_tokens": {​

"type": "integer"​

},​

"input_creation_cached_tokens": {​

"type": "integer"​

}​

}​

},​

"metadata": {​

"type": "object",​

"description": "保留字段，可以承载业务自定义的属性",​

"additionalProperties": {​

"type": "string"​

}​

},​

"basic_info": {​

"type": "object",​

"properties": {​

"started_at": {​

"type": "string",​

"description": "单位毫秒"​

},​

"duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"error": {​

"type": "object",​

"properties": {​

"code": {​

"type": "integer"​

},​

"msg": {​

"type": "string"​

}​

}​

}​

}​

}​

}​

}​

},​

"metadata": {​

"type": "object",​

"description": "保留字段，可以承载业务自定义的属性",​

"additionalProperties": {​

"type": "string"​

}​

},​

"basic_info": {​

"type": "object",​

"properties": {​

"started_at": {​

"type": "string",​

"description": "单位毫秒"​

},​

"duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"error": {​

"type": "object",​

"properties": {​

"code": {​

"type": "integer"​

},​

"msg": {​

"type": "string"​

}​

}​

}​

}​

},​

"metrics_info": {​

"type": "object",​

"properties": {​

"llm_duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"tool_duration": {​

"type": "string",​

"description": "单位毫秒"​

},​

"tool_errors": {​

"type": "object",​

"description": "Tool错误分布，格式为：错误码-->list<ToolStepID>",​

"additionalProperties": {​

"type": "array",​

"items": {​

"type": "string"​

}​

}​

},​

"tool_error_rate": {​

"type": "number",​

"description": "Tool错误率"​

},​

"model_errors": {​

"type": "object",​

"description": "Model错误分布，格式为：错误码-->list<ModelStepID>",​

"additionalProperties": {​

"type": "array",​

"items": {​

"type": "string"​

}​

}​

},​

"model_error_rate": {​

"type": "number",​

"description": "Model错误率"​

},​

"tool_step_proportion": {​

"type": "number",​

"description": "Tool Step占比(分母是总子Step)"​

},​

"input_tokens": {​

"type": "integer",​

"description": "输入token数"​

},​

"output_tokens": {​

"type": "integer",​

"description": "输出token数"​

}​

}​

}​

}​

}​

}​

}​

}​

​

上一篇

人工标注评测数据

下一篇

什么是观测？