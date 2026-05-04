---
source_url: https://docs.coze.cn/cozeloop/p3hj6izn
title: 'Claude Code - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:40Z
---

# Claude Code - 文档 - 扣子

Claude Code

本文介绍如何通过集成扣子罗盘 SDK，将 Claude Code 的开发会话与工具调用轨迹上报至扣子罗盘，实现开发过程的可观测性、分析与评测。​

说明

扣子罗盘 SDK 会自动处理数据构型与上报细节，你只需关注核心业务逻辑。​

​

功能介绍​

集成方案通过 Claude Code 内置的 hooks 系统实现。该系统允许在会话生命周期的特定节点（如每次响应结束后的 Stop 阶段）执行自定义命令。​

通过一个简单的 Python Hook 脚本，你可以自动捕获 Claude Code 的本地会话记录 (.jsonl)，并将其构造成符合 OpenTelemetry 规范的 Span，实时上报至扣子罗盘。Python Hook 脚本的主要优势如下：​

  * 全链路追踪：完整记录用户输入、模型响应、思考过程及每一次工具调用的输入输出。​

  * 低侵入性：无需修改 Claude Code 源码，通过配置文件即可一键集成。​

  * 灵活扩展：支持自定义标签、过滤特定工具调用，适配多种分析需求。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272504%27%20height=%27428.925925925926%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c3bb0587e0144662bbe3bbea8ade2e93~tplv-goo7wpa0wc-quality:q75.image)​

​

准备工作​

在开始之前，请确保你的开发环境满足以下要求：​

  * 已安装了 [Claude Code](<https://code.claude.com/docs/en/overview>)。​

  * 已安装了扣子罗盘 Python SDK。详情参阅 ​安装扣子罗盘 Python SDK。​

  * 注意

扣子罗盘 Python SDK 需要 Python 3.8 或更高版本。​

​

  * ​

Bash

复制

pip install cozeloop​

​

步骤一：配置环境变量​

为了安全地管理访问凭证，请在你的项目的 .claude/settings.local.json 文件中设置环境变量。​

在你的项目根目录下，创建或编辑 .claude/settings.local.json：​

​

JSON

复制

{​

"env": {​

"COZELOOP_WORKSPACE_ID": "你的扣子罗盘工作空间 ID",​

"COZELOOP_API_TOKEN": "你的个人访问令牌（PAT）或服务访问令牌（SAT）"​

}​

}​

​

​

变量名​| 说明​  
---|---  
COZELOOP_WORKSPACE_ID​| 扣子罗盘工作空间 ID。获取方式请参考 ​获取扣子罗盘空间 ID。​  
COZELOOP_API_TOKEN​| 个人访问令牌（PAT）或服务访问令牌（SAT）。获取方式请参考 ​SDK 鉴权。​  
  
​

步骤二：创建并配置 Hook 脚本​

说明

Hook 脚本的核心逻辑包括：​

  * 查找最新的会话文件：自动在 ~/.claude/projects/ 目录中定位最近修改的 .jsonl 文件。​

  * 增量处理：通过状态文件 (~/.claude/cozeloop_state/) 记录已处理的行号，避免重复上报。​

  * 会话分组：为每个独立的会话生成并复用一个 session_id。​

  * 数据上报：调用 cozeloop.start_span() 和 span.finish() 等方法，将用户输入、模型响应和工具调用分别作为独立的 Span 上报。​

  * 优雅关闭：在脚本结束前调用 client.close()，确保所有缓存的 Trace 数据都被成功发送。​

​

1.

在 Claude Code 的用户配置目录下创建 hooks 文件夹。​

​

Bash

复制

mkdir -p ~/.claude/hooks​

​

2.

把 [Hook 脚本](<https://github.com/coze-dev/cozeloop-examples/tree/main/python/tool/claude_code_hook>) 下载到你创建的目录，并将其命名为 cozeloop_hook.py。​

步骤三：配置全局 Hook​

修改 Claude Code 的全局配置文件 ~/.claude/settings.json，注册 Stop 阶段的 Hook。​

注意

确保 command 中使用的 python 路径正确。如果使用了虚拟环境，建议指定绝对路径。​

​

​

JSON

复制

{​

"hooks": {​

"Stop": [​

{​

"matcher": "",​

"hooks": [​

{​

"type": "command",​

"command": "python ~/.claude/hooks/cozeloop_hook.py"​

}​

]​

}​

]​

}​

}​

​

步骤四：验证与查看 Trace​

完成配置后，正常使用 Claude Code 进行几轮会话。然后：​

1.

登录[扣子罗盘](<https://loop.coze.cn/>)，进入 观测 > Trace 页面。找到 Claude Code 上报的 Trace 数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273158%27%20height=%271600.9305555555554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE1OCIgaGVpZ2h0PSIxNjAwLjkzMDU1NTU1NTU1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

点击 Trace 数据查看详情。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273048%27%20height=%271728.611111111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA0OCIgaGVpZ2h0PSIxNzI4LjYxMTExMTExMTExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

更多信息​

Trace 数据说明​

cozeloop_hook.py 脚本会将 Claude Code 的会话映射为扣子罗盘中的 Trace 和 Span。​

Span 命名与层级结构​

Claude Code 的每个会话轮次都会被上报为一个独立的 Trace。在这个 Trace 内部，包含一个根 Span (claude_code_turn_*)，以及多个代表不同操作的子 Span。​

一个典型的 Trace 结构如下：​

​

Plain Text

复制

claude_code_turn_{i} (root span, type: main)​

├── user_input (type: query)​

│ └── input: "用户输入的完整内容"​

├── assistant_response (type: model)​

│ ├── input: "用户输入的完整内容"​

│ └── output: "模型生成的完整响应，包括思考过程和文本"​

├── tool_{tool_name} (type: tool)​

│ ├── input: {"command": "ls -l"}​

│ └── output: "total 0..."​

└── ... (其他 tool spans)​

​

  * claude_code_turn_{i}：作为根 Span，代表一个完整的“用户-模型”交互轮次。​

  * user_input：记录用户的提问或指令。​

  * assistant_response：记录模型的完整回答，包括其思考过程和最终的文本输出。​

  * tool_*：每个工具调用都对应一个独立的 Span，例如 tool_Bash、tool_write_file 等。input 字段记录了调用工具时传入的参数，output 字段记录了工具执行后的返回结果。​

标签​

为了方便在 CozeLoop 平台上进行筛选和聚合，每个 Span 都会附带一组结构化的标签（Tag）。​

​

标签 ​| 说明​| 附加于​  
---|---|---  
session_id​| 整个对话会话的唯一标识符。格式如 claude-code-20240318-103000-12345。​| Root Span​  
turn_index​| 当前对话轮次在整个会话中的索引号，从 0 开始。​| Root Span​  
source​| 数据来源标识，固定为 "claude_code"。​| Root Span​  
role​| 消息的角色，如 "user" 或 "assistant"。​| user_input, assistant_response Spans​  
tool_name​| 被调用的工具名称，例如 "Bash", "read_file"。​| Tool Spans​  
tool_id​| Claude Code 为每次工具调用生成的唯一 ID。​| Tool Spans​  
  
​

会话 ID​

一个连续的 Claude Code 会话中的所有轮次都将共享同一个会话 ID（session_id）。这使得你可以在 CozeLoop 中轻松地筛选出特定会话的全部交互历史。session_id 由 Hook 脚本在首次处理会话时生成，格式为：claude-code-YYYYMMDD-HHMMSS-PID。​

按项目启用/禁用 Trace 上报​

只需在项目的 .claude/settings.local.json 中设置 TRACE_TO_COZELOOP：​

​

JSON

复制

{​

"env": {​

"TRACE_TO_COZELOOP": "false"​

}​

}​

​

开启调试模式​

如果你发现数据没有正常上报，可以开启调试模式来排查问题。在 .claude/settings.local.json 中添加 CC_COZELOOP_DEBUG 环境变量：​

​

JSON

复制

{​

"env": {​

"COZELOOP_WORKSPACE_ID": "your-workspace-id",​

"COZELOOP_API_TOKEN": "your-api-token",​

"CC_COZELOOP_DEBUG": "true"​

}​

}​

​

启用后，cozeloop_hook.py 脚本的详细执行日志将输出到 Claude Code 的终端中，包括：​

  * 脚本启动与结束时间。​

  * 找到的会话文件路径。​

  * 处理的新消息数量。​

  * CozeLoop SDK 的初始化与关闭状态。​

  * 数据上报过程中的关键事件或错误。​

配置文件说明​

以下是与 Claude Code Trace 上报相关的所有文件的位置和用途说明。​

​

文件路径​| 说明​  
---|---  
~/.claude/settings.json​| Claude Code 的全局配置文件，用于注册全局 Stop Hook。​  
<project>/.claude/settings.local.json​| 项目级配置文件，用于存储敏感的环境变量，如 CozeLoop 的凭证。此文件应被加入 .gitignore。​  
~/.claude/hooks/cozeloop_hook.py​| 核心的 Hook 脚本，负责数据解析和上报。​  
~/.claude/projects/**/*.jsonl​| Claude Code 自动生成的会话日志文件，是数据源。​  
~/.claude/cozeloop_state/​| Hook 脚本自动创建的状态文件目录，用于存放每个会话文件的处理进度。​  
  
​

自定义扩展 cozeloop_hook.py 脚本​

你可以直接修改 cozeloop_hook.py 脚本以满足更高级的追踪需求。​

添加自定义标签​

在创建 Span 后，可以使用 .set_tags() 方法添加任何你需要的自定义标签，以便在 CozeLoop 平台上进行更精细的分析。​

例如，在 send_to_cozeloop 函数中，为 root_span 添加项目名称标签：​

​

Python

复制

# 在 cozeloop_hook.py 的 send_to_cozeloop 函数中​

with client.start_span(name=f"claude_code_turn_{i}", span_type="main") as root_span:​

root_span.set_tags({​

"session_id": session_id,​

"turn_index": i,​

"source": "claude_code",​

"project_name": os.environ.get("CLAUDE_PROJECT_NAME", "unknown"), # 添加项目名​

"custom_eval_metric": "some_value" # 添加自定义评测指标​

})​

​

过滤特定工具​

如果你不希望追踪某些工具的调用（例如，频繁但价值不高的 read_file），可以在创建 Tool Span 前添加过滤逻辑。​

​

Python

复制

# 在 cozeloop_hook.py 的 send_to_cozeloop 函数中​

ignored_tools = ["read_file", "list_directory"]​

​

for tool_call in tool_calls:​

tool_name = tool_call.get("name", "unknown_tool")​

​

if tool_name in ignored_tools:​

debug_log(f"Skipping ignored tool: {tool_name}")​

continue # 跳过上报​

​

# ... 创建并上报 tool_span 的逻辑 ...​

​

常见问题​

终端提示 cozeloop: command not found​

可能原因：执行 Hook 的 Python 环境中未安装 cozeloop 库。​

解决方案：​

a.

打开 ~/.claude/settings.json 文件，检查 command 字段中指定的 Python 解释器路径是否正确。​

b.

使用该路径的 Python 解释器执行 pip install cozeloop 来安装所需依赖。​

在扣子罗盘平台看不到上报的数据​

请按照以下顺序进行排查：​

1.

检查鉴权信息：确认项目级配置文件 .claude/settings.local.json 中的 COZELOOP_WORKSPACE_ID 和 COZELOOP_API_TOKEN 是否已正确配置，并确保所用令牌拥有 Trace 上报权限。​

2.

检查 Hook 配置：检查全局配置文件 ~/.claude/settings.json 中的 hooks 部分，确保其指向了正确的脚本路径，且 JSON 格式无误。​

3.

检查脚本执行日志：在 Hook 脚本中开启调试模式，然后重新触发操作，并查看终端日志中是否有相关的错误信息输出。​

并行运行多个 Claude Code 实例时数据混乱​

可能原因：这是由 Hook 脚本的实现机制导致的。默认的 find_latest_conversation_file 函数通过文件的“最后修改时间”来定位会话文件。在多个实例并行写入时，这种方式无法保证找到正确的对应文件，从而导致数据归属错误。​

解决方案：当前的 Hook 实现是一个轻量级方案，最适用于单实例运行的场景。对于多实例并行使用的场景，这是一个已知的局限。你需要自行实现更复杂的 Hook 逻辑（例如，通过进程 ID 或启动参数来唯一标识和定位会话文件）来确保数据的准确性。​

上一篇

LiteLLM Proxy

下一篇

获取扣子罗盘空间 ID