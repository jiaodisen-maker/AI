---
source_url: https://docs.coze.cn/cozeloop/openclaw_trace_report
title: '把 OpenClaw 的 Trace 上报到扣子罗盘 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:51Z
---

# 把 OpenClaw 的 Trace 上报到扣子罗盘 - 文档 - 扣子

把 OpenClaw 的 Trace 上报到扣子罗盘

本文引导你将 [OpenClaw](<https://github.com/openclaw/openclaw>) 执行过程的 Trace 数据上报至[扣子罗盘](<https://loop.coze.cn/console>)。Trace 数据被上报到扣子罗盘后，你可以利用扣子罗盘的分析与可视化能力，深入洞察 OpenClaw 的使用成本、性能与行为。​

上报 OpenClaw 的 Trace 数据​

根据你部署 OpenClaw 的方式，上报 Trace 数据的方式有所不同：​

  * 如果你的 OpenClaw 是在 2026 年 3 月 13 日 或之后通过[扣子编程](<https://docs.coze.cn/tutorial/openclaw>)部署的，系统会自动将 OpenClaw 的 Trace 数据上报至扣子罗盘。在这种情况下，你无需安装 OpenClaw Trace 上报插件，可以直接参考​查看 Trace 数据章节的指引，在扣子罗盘中查看 Trace 数据。​

  * 如果你的 OpenClaw 不是通过[扣子编程](<https://docs.coze.cn/tutorial/openclaw>)部署的或是在 2026 年 3 月 13 日之前通过[扣子编程](<https://docs.coze.cn/tutorial/openclaw>)部署的，你需要参考 ​安装插件章节的指引安装 OpenClaw Trace 上报插件。​

查看 Trace 数据​

实现 OpenClaw Trace 数据的上报后，启动你的 OpenClaw 应用并发起对话。接下来，你就可以在扣子罗盘中查看 OpenClaw 的 Trace 数据。​

1.

访问你的[扣子罗盘](<https://loop.coze.cn/console>)工作空间。​

2.

在扣子罗盘的 观测 > Trace 页面，把上报类型设置为 SDK 上报，你应该能看到上报的 Trace 数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27813%27%20height=%27417%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b1b9126372e64d7d92a8d994274fbc3c~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

点击任意一条 Trace 即可查看详细的 Span 调用链、属性和耗时信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27452%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

OpenClaw Trace 数据的结构如下所示（根据实际情况可能略有不同）：​

​

Plain Text

复制

openclaw_request (root)​

├── user_message（用户输入。由于 model 节点也包含此信息，该节点在后续版本中可能会被移除）​

└── agent (从 before_agent_start 到 agent_end 的完整时间跨度)​

├── model_provider/model_name (LLM 调用)​

├── read (tool 调用)​

├── write (tool 调用)​

└── ... (其他 tool)​

​

通过插件上报 OpenClaw 的 Trace 数据​

如果你的 OpenClaw 不是通过[扣子编程](<https://docs.coze.cn/tutorial/openclaw>)部署的，你可以通过扣子罗盘提供的插件来实现 OpenClaw 的 Trace 数据上报。​

安装插件​

[扣子罗盘](<https://loop.coze.cn/console>)提供了 OpenClaw Trace 上报插件。你只需要安装该插件就能实现 OpenClaw 的 Trace 数据上报。​

准备工作​

在开始之前，请确保你已完成以下准备工作：​

  * 获取了扣子罗盘空间 ID 和服务访问令牌。​

  * 扣子罗盘空间 ID：切换到目标空间，点击其右侧的复制按钮获取空间 ID。详细获取方式参考 [获取扣子罗盘空间 ID](<https://loop.coze.cn/open/docs/cozeloop/get_workspace_id_and_token#01dede13>)。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27365%27%20height=%27166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY1IiBoZWlnaHQ9IjE2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 服务访问令牌：获取方式参考 [配置服务访问令牌](<https://loop.coze.cn/open/docs/cozeloop/authentication-for-sdk#83f924a1>)。​

  * 有一个已安装并可正常运行的 OpenClaw 实例。参考 OpenClaw 的[官方文档](<https://docs.openclaw.ai/install>)了解如何安装和启动 OpenClaw。​

步骤一：安装插件​

运行以下命令安装插件。​

​

Shell

复制

npx @cozeloop/openclaw-cozeloop-trace-onboard-cli@latest install​

​

你需要按照命令行提示分别输入服务访问令牌和扣子罗盘空间 ID。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27791%27%20height=%2799%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzkxIiBoZWlnaHQ9Ijk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤二：验证插件​

你可通过以下命令查看插件状态，如果 Openclaw Cozeloop Trace 的状态为 loaded，则说明插件加载成功。此时，所有与 OpenClaw 对话的 Trace 就可以被上报到扣子罗盘。​

​

Shell

复制

openclaw plugins list​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27677%27%20height=%2744%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc3IiBoZWlnaHQ9IjQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

管理插件​

升级或重装插件​

要升级或重装插件，你可以直接重新执行 ​步骤一：安装插件。​

如果在执行过程中遇到关于“插件不存在”的报错，可以尝试运行 openclaw doctor --fix 命令进行修复。​

更新插件配置​

你安装插件时，OpenClaw 配置文件（~/.openclaw/openclaw.json）中的 plugins.allow 和 plugins.entries 字段会被自动更新。因此，一般情况下你无需手动修改 OpenClaw 配置文件。​

​

JSON

复制

{​

...​

"plugins": {​

"allow": [​

...​

"openclaw-cozeloop-trace",​

...​

],​

"entries": {​

...​

"openclaw-cozeloop-trace": { ​

"enabled": true,​

"config": {​

"authorization": "Bearer sat_iH*************A", ​

"endpoint": "https://api.coze.cn/v1/loop/opentelemetry",​

"workspaceId": "74*****"​

}​

}​

},​

...​

}​

... ​

}​

​

如果你需要手动修改 OpenClaw 配置文件中的插件配置，可参考以下配置项说明。​

​

配置项​| 是否必选​| 说明​| 示例值​  
---|---|---|---  
openclaw-cozeloop-trace.config.authorization​| 必选​| 扣子罗盘的服务访问令牌。获取方式参考 [配置服务访问令牌](<https://loop.coze.cn/open/docs/cozeloop/authentication-for-sdk#83f924a1>)。​| "Bearer {sat_iH*************A}"​  
openclaw-cozeloop-trace.config.workspaceId​| 必选​| 扣子罗盘空间 ID。详细获取方式参考 [获取扣子罗盘空间 ID](<https://loop.coze.cn/open/docs/cozeloop/get_workspace_id_and_token#01dede13>)。 ​| "74*****"​  
openclaw-cozeloop-trace.config.endpoint​| 可选​| Trace 上报地址，默认使用https://api.coze.cn/v1/loop/opentelemetry。​| "https://api.coze.cn/v1/loop/opentelemetry"​  
openclaw-cozeloop-trace.config.debug​| 可选​| 用于控制是否开启 Debug 日志。此功能默认关闭。​在安装插件时不会添加该参数。​| false​  
  
​

应用场景​

将 OpenClaw 的 Trace 数据上报至扣子罗盘后，你可以利用这些数据实现以下应用场景。​

场景一：统计 Token 消耗​

你可以在扣子罗盘中查看 OpenClaw 使用不同模型所产生的 Token 消耗。​

1.

访问你的[扣子罗盘](<https://loop.coze.cn/console>)工作空间。​

2.

在扣子罗盘的 观测 > 统计 页面，选择上报类型为 SDK 上报，然后把模型设置为 OpenClaw 所使用的模型。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271280%27%20height=%27644.4444444444445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4MCIgaGVpZ2h0PSI2NDQuNDQ0NDQ0NDQ0NDQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

场景二：排查问题​

扣子罗盘的 Trace 数据采用逐步上报机制：已完成的节点会先上报，根节点（Root Span）最后上报。这让你可以根据已完成的节点，实时跟进请求的执行情况，从而高效排查问题。​

说明

在排查问题时，建议你切换到 All Span 视图，以查看请求的最新执行状态。​

​

例如，当你向 OpenClaw 发出“帮我查看桌面上的一个文件”的指令后，若它陷入不断重复 read 操作的循环中，你可以立即在 Trace 视图中观察到这一行为。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273010%27%20height=%27934%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAxMCIgaGVpZ2h0PSI5MzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

此时，点击该请求的任意 Span，即可查看其详细的执行 Trace，帮助你快速定位问题并采取相应措施（如重启 OpenClaw）。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27522%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIyIiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

新版 OpenClaw 不上报 Token 用量​

自 openclaw 2026.3.7 版本起，其 usage 数据的处理方式发生了变化，且官方未再提供相关的控制选项。​

我们正在关注官方进展并探索新的上报方法。在此期间，你可以暂时选择将 OpenClaw 降级。例如，如果你是通过 npm 安装的，可以使用以下命令将版本强制降至 2026.3.2：​

​

Shell

复制

npm install -g openclaw@2026.3.2 --force​

​

参考 OpenClaw 的[官方文档](<https://docs.openclaw.ai/install>)了解更多降级方式。​

扣子罗盘中没有 Trace 数据​

请按照以下步骤进行排查：​

1.

验证插件安装与执行情况​

  * 检查插件状态：运行 openclaw plugins list 命令，确认 openclaw-cozeloop-trace 插件的状态为 loaded。如果状态不是 loaded，说明插件安装或配置未成功，请你重新检查并执行相关步骤。​

  * 检查运行日志：​

i.

在插件配置中，将 debug 字段的值设置为 true。​

ii.

重启 OpenClaw 网关，然后发起一次新的对话以生成日志。​

iii.

执行以下命令，查看日志中是否包含关键信息：​

  * ​

Shell

复制

tail -50 ~/.openclaw/logs/gateway.log | grep -i "CozeloopTrace"​

​

  * 日志文件的位置可能会有不同，例如 /tmp/openclaw/openclaw-2026-xx-xx.log。具体路径请参考 OpenClaw 的[官方文档](<https://docs.openclaw.ai/install>)。​

iv.

如果日志中没有 CozeloopTrace 关键字，说明插件配置有误，请你返回并仔细核对配置步骤。​

2.

验证凭证与权限​

  * 请确保配置文件中的 authorization（服务访问令牌）与 workspaceId 是正确且相互匹配的。​

  * 请确认你使用的访问令牌（服务访问令牌）已被授予向指定 workspaceId 所在的工作空间上报 Trace 数据的权限（ingestLoopTrace 权限）。​

无法正常访问扣子罗盘​

如果你的服务器需要通过 HTTP 代理访问网络，请将扣子罗盘的 API 域名添加到代理的白名单中，以避免连接失败。​

如果你未在插件中配置 endpoint 参数，默认的上报域名为 https://api.coze.cn。​

扣子罗盘中有 Trace 数据，但 Trace 数据缺失部分节点​

如果你发现上报的 Trace 数据中缺少部分节点，例如 model 和 tool 等节点，并且该问题能够稳定复现，这通常是由于 OpenClaw 版本过低所致。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27299%27%20height=%27112%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk5IiBoZWlnaHQ9IjExMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

请参考以下命令升级版本：​

​

Shell

复制

sudo su # 以 root 权限去执行 su 命令​

su openclaw # 切换到openclaw用户​

openclaw update # 升级版本​

​

openclaw --version # 升级后，查看版本​

​

​

上一篇

体验扣子罗盘

下一篇

什么是提示词？