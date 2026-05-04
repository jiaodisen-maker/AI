---
source_url: https://docs.coze.cn/tutorial/openclaw
title: '一键部署 OpenClaw 并集成飞书 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:33Z
---

# 一键部署 OpenClaw 并集成飞书 - 文档 - 扣子

一键部署 OpenClaw 并集成飞书

什么是 OpenClaw​

[OpenClaw](<https://openclaw.ai/>)（原 Moltbot、Clawdbot） 是一款开源的个人 AI 助理和智能代理系统，可运行在个人电脑或服务器上。和传统的 AI 助理不同，OpenClaw 不是普通的聊天机器人，被授予操作权限之后，它能控制你的终端执行操作，可以“动手工作”，而不是“只出主意”。你可以通过飞书等即时通信工具与它对话交互，让它帮你完成各类任务，例如生成图文、处理邮件、管理日程等。​

扣子编程现已支持一键安装 OpenClaw。开发者可以在扣子编程的云主机环境里快速安装部署 OpenClaw，打造一个定制的个人 AI 助理。​

相较于其他部署方案，扣子编程部署的 OpenClaw 具备以下优势：​

  * 和本地运行 OpenClaw 相比：扣子编程部署 OpenClaw 操作便捷，环境隔离、可保护数据和 API Key 的隐私安全，保障助手全天 24 小时稳定运行。​

  * 和云服务器运行 OpenClaw 相比：扣子编程部署 OpenClaw 是真正的一键部署。无需选购服务器、开通并配置模型；无需终端命令行操作，一键打通飞书等 IM 工具。只需通过自然语言交互，就可以让扣子 AI 为你调整运行配置、添加个性化技能，打造开箱即用的 AI 助手。​

  * 和 QQ 等 IM 工具提供的 OpenClaw 相比：扣子编程提供了安全的云主机环境和配套的 AI 编程助手，可实现高度定制化、更高的能力上限，例如便捷的浏览器工具，可无障碍访问各类网站。生态开放，支持便捷打通各类 IM 工具，无功能裁剪与限制。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273810%27%20height=%271640%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/96a8506ea9db44a6992fff36262e5653~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271514%27%20height=%27872%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b36199bc74d84f6caafa6cbae91ef4e5~tplv-goo7wpa0wc-quality:q75.image)​

​

​

使用须知​

在开始部署前，请花一分钟了解相关的限制、费用和安全建议。​

使用限制​

  * 如果取消部署，对话随时可能因云主机被回收而中断。​

  * 暂不支持 QQ 渠道。​

  * 使用 OpenClaw 会消耗你的扣子编程积分（包括对话、大模型调用、图片生成等）。OpenClaw 的 Token 消耗较高，你可以选择省流版以节省 Token 成本。​

安全提醒​

建议企业用户谨慎使用 OpenClaw，它可能存在明文存储凭证等安全风险。扣子编程建议你：​

  * 定期轮换所有提供给 OpenClaw 的凭证。​

  * 不要将任何生产环境的敏感信息交给 OpenClaw 处理。​

  * 谨慎判断是否要将 OpenClaw 个人助理添加到群聊中，避免其泄露 API Key 等敏感信息。​

准备工作​

​

事项​| 说明​  
---|---  
扣子账号​| 注册并登录[扣子编程](<https://code.coze.cn/home>)。​  
订阅套餐及配额​| [购买以下任一一款订阅套餐](<https://code.coze.cn/subscription-paywall>)：​

  * 个人高阶版：最多 1 个 OpenClaw 项目。​

  * 个人旗舰版：最多 3 个 OpenClaw 项目。​

  * 企业标准版：最多 1 个 OpenClaw 项目。​

  * 企业旗舰版：最多 1 个 OpenClaw 项目。​

  
模型 API Key​可选​| 默认使用扣子编程提供的热门模型（豆包 2.0 等），订阅套餐中包含订阅积分，可以用来抵扣 OpenClaw 的 Token 费用，无需额外付费。​如需使用第三方模型（如火山方舟 Coding plan 等），需提前准备对应的 API Key，并自行支付模型费用。​  
  
​

部署 OpenClaw 飞书助理​

参考以下流程，在扣子编程中创建你的 OpenClaw AI 助理，并打通飞书渠道。操作完成后，你可以在飞书中和 OpenClaw AI 助理对话。​

视频教程​

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

步骤一：一键部署 OpenClaw​

扣子编程提供了一键部署 OpenClaw 的极简方案，在扣子编程首页单击立刻领取按钮，后台将自动完成项目的创建和部署。只需三分钟，即可获得一个 7×24 小时在线智能助手。​

详细操作步骤如下：​

1.

登录[扣子编程](<https://code.coze.cn/>)。​

2.

在一键部署 OpenClaw 区域单击立刻领取。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27455%27%20height=%27328%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU1IiBoZWlnaHQ9IjMyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择你的 OpenClaw 配置，并单击确定。​

  * ​

配置​| 说明​  
---|---  
模型选择​| 为你的 OpenClaw 助理选择模型。默认为自动模式，你也可以选择豆包 2.0 等热门模型。部署后也可以随时切换模型。​  
版本选择​| 扣子编程提供以下两种部署版本：​
    * 满血版（默认）：OpenClaw 原版默认配置，无差异的性能体验。Token 消耗相对较多，适合需要极致性能的用户。​
    * 省流版：在满血版的基础上调整了上下文压缩和心跳配置，Token 消耗相对较低，但部分场景下可能会有一些性能损失。省流版适合需要控制 Token 成本的用户。​  
渠道配置​| 你和 OpenClaw 个人助理对话的渠道，OpenClaw 将作为该渠道的机器人应用和你展开对话。​
    * 若无需发布到渠道，则直接单击确定来跳过渠道配置。若未配置渠道，你只能在 Web UI 界面上和 OpenClaw 个人助理对话。​
    * 如需配置飞书渠道，参考后续流程完成配置。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272626%27%20height=%271635.1712962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYyNiIgaGVpZ2h0PSIxNjM1LjE3MTI5NjI5NjI5NjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

步骤二：配置飞书渠道​

扣子编程现已支持一键配置飞书渠道，在 OpenClaw 配置页面确认你的飞书机器人名称，单击创建按钮，即可和你的 OpenClaw 助手在飞书对话。​

详细操作步骤如下：​

1.

打开 OpenClaw 配置页面。​

  * 你可以在 OpenClaw 页面右上角单击配置图标，进入 OpenClaw 配置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27520%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIwIiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在渠道配置区域找到飞书渠道，单击去配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27343%27%20height=%27198%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQzIiBoZWlnaHQ9IjE5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

（可选）确认飞书机器人的名称，并单击开始配置。​

  * 机器人名称默认为 XX 的助手，如果你不喜欢这个机器人的名字，可以重新设置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27241%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUwIiBoZWlnaHQ9IjI0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

确认飞书账号，并单击授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27362%27%20height=%27400%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYyIiBoZWlnaHQ9IjQwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

等待后台配置完成。​

  * 如果看到以下页面，表示扣子编程仍在后台帮你配置飞书群渠道，请耐心等待。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27365%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY1IiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

成功连接到飞书。​

  * 扣子编程会在后台为你创建飞书机器人、开启长连接，并配置相关权限、事件与回调、配对。如果看到以下页面，表示你的 OpenClaw 助手已经成功连接到飞书，可以根据页面提示去飞书和 OpenClaw 助手对话。​

  * 去后台管理：前往飞书开放平台，查看你的飞书机器人应用的相关配置，包括 App ID、权限等信息。​

  * 去飞书对话：前往飞书客户端，和你的 OpenClaw 助手对话。如果你有多个飞书账号，请注意登录上述步骤中完成授权的账号，否则可能跳转对话失败。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27616%27%20height=%27388%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE2IiBoZWlnaHQ9IjM4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：体验效果​

扣子编程为你的 OpenClaw 项目预安装了一系列技能与工具，并开通了相关的飞书权限，无需任何额外配置，直接和 OpenClaw 个人助理对话即可完成以下常见任务。​

基础问答​

示例 Query：​

​

Plain Text

复制

介绍一下你自己​

​

​

效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27216%27%20height=%27234%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE2IiBoZWlnaHQ9IjIzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

联网搜索​

示例 Query：​

​

Plain Text

复制

查询一下今天的黄金价格​

​

​

效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27223%27%20height=%27150%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzIiBoZWlnaHQ9IjE1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

生成图片​

示例 Query：​

​

Plain Text

复制

帮我生成一个马年春节绘本，卡通风格，包含灯笼、春联等春节常见元素，连续 4 张​

​

效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27242%27%20height=%27215%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQyIiBoZWlnaHQ9IjIxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

创建飞书文档​

示例 Query：​

​

Plain Text

复制

帮我检索关于 OpenClaw 的新闻，整理成一篇日报之后，写到飞书文档里​

​

​

效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27232%27%20height=%27185%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMyIiBoZWlnaHQ9IjE4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

增强 OpenClaw 能力​

扣子编程已为 OpenClaw 项目预先安装了联网搜索、图片生成等常用技能（Skills），你也可以将自己开发的技能、扣子技能商店的开源技能、Github 开源社区的热门技能安装到自己的 OpenClaw 项目中，增强其在垂直领域的能力。​

关于扣子技能的详细说明，可参考​技能概述；关于如何创建一个技能，可参考​开发技能。​

参考以下流程，将你已有的技能，导入到 OpenClaw 项目中使用。​

1.

获取技能包：从技能项目的文件树中下载技能的 .zip 压缩包。​

2.

上传安装：在扣子编程 OpenClaw 项目的左下角对话框中，上传 该压缩包，AI 会自动为你安装。​

3.

测试技能：在预览窗口中用自然语言调用该技能，验证效果。​

获取技能包：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27387%27%20height=%27207%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg3IiBoZWlnaHQ9IjIwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上传安装：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27353%27%20height=%27506%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUzIiBoZWlnaHQ9IjUwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

测试技能：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27280%27%20height=%27248%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgwIiBoZWlnaHQ9IjI0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

相关配置​

飞书快捷指令​

你的 OpenClaw 绑定飞书之后，可以通过飞书快捷指令，一键执行 OpenClaw 的部分斜杠命令，灵活管理对话状态。​

  * /new：开始一个新会话。此命令会清空当前对话的上下文、开启一段全新对话，不会影响历史对话和记忆，一般在切换新话题的时候时候。​

  * /restart：重启 OpenClaw。此命令会重置 OpenClaw 运行状态，彻底重启服务。常用于助手响应异常、逻辑混乱或功能卡顿时恢复正常。​

  * /stop：中止当前会话。此命令立即停止当前正在生成的内容或执行中的任务，保留现有上下文，仅终止本次输出。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27371%27%20height=%27341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzcxIiBoZWlnaHQ9IjM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

切换模型​

扣子编程默认为你的 OpenClaw 项目安装了内置的大模型、图片生成、联网搜索集成，如果你希望 OpenClaw 使用其他模型完成任务，可以通过自然语言对话方式，在页面左侧的输入框中下达你的指令。​

  * 使用扣子编程内置集成的模型。​

  * 在 OpenClaw 配置页面，直接使用扣子编程提供的豆包 2.0 等热门模型，无需额外开通其他厂商的模型服务。​

a.

在 OpenClaw 页面右上角单击配置图标，进入 OpenClaw 配置页面。​

b.

在模型选择框中，选择你想使用的模型。​

c.

单击确定。​

  * 打开 OpenClaw 配置页面：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272634%27%20height=%271652.8349999999998%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYzNCIgaGVpZ2h0PSIxNjUyLjgzNDk5OTk5OTk5OTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

选择模型：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27366%27%20height=%27249%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY2IiBoZWlnaHQ9IjI0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * 使用火山方舟等厂商的模型服务 API。​

  * 如果内置集成中没有你想使用的模型，或者你已经开通了火山方舟等厂商的模型服务，可以直接使用模型 API。建议提供模型 ID、API Key 和完整的 Base URL，便于扣子 AI 帮你快速、正确配置模型。​

​

Plain Text

复制

帮我把模型换成火山方舟的 Doubao 1.8，模型详细信息如下​

模型 ID：ep-20260204215010-*****​

API Key：e9da865c-3050-4ed8-b49d-bc6a********​

Base URL：https://ark.cn-beijing.volces.com/api/v3​

​

你可以在火山方舟控制台的“模型广场”页面找到不同模型的 ID，并在“密钥管理”页面创建和获取 API Key。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27262%27%20height=%27319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYyIiBoZWlnaHQ9IjMxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * 使用 Coding Plan。​

  * 如果你开通了火山方舟 Coding Plan，也可以让扣子 AI 帮你切换成支持 Coding Plan 的模型。注意 Coding Plan 的 Base URL 和普通 API 调用不同，建议在对话中提供完整的 Base URL。​

  * 例如：​

​

Plain Text

复制

帮我切换成火山方舟 coding plan 的 GLM 4.7 模型，模型详细信息如下​

model name：glm-4.7​

Base URL：https://ark.cn-beijing.volces.com/api/coding/v3​

API Key：e9da865c-3050-4ed8-b49d-bc6a********​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271240%27%20height=%271706%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI0MCIgaGVpZ2h0PSIxNzA2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

安装和更新飞书官方插件​

说明

如果你已安装飞书官方插件，希望使用最新的插件版本，可以在终端区域执行以下命令查看并更新插件版本。 ​

  * 查看当前版本：npx @larksuite/openclaw-lark-tools info ​

  * 更新插件版本：npx -y @larksuite/openclaw-lark-tools update​

你也可以要求你的 OpenClaw 个人助理设置定时任务，帮你定期更新飞书插件版本，例如“每天早上十点帮我更新飞书插件，更新命令是 npx -y @larksuite/openclaw-lark-tools update”。​

​

在 3 月 5 日及之前创建的 OpenClaw 项目，默认使用 OpenClaw 内置的飞书插件来配置飞书渠道，如果你希望使用飞书官方发布的 OpenClaw 飞书插件，体验更强大的飞书集成能力，可以参考以下步骤更新插件。 ​

关于飞书官方插件的详细说明，可参考 [OpenClaw飞书官方插件使用指南（公开版）](<https://bytedance.larkoffice.com/docx/MFK7dDFLFoVlOGxWCv5cTXKmnMh>)。​

安装插件时，你可以选择创建一个新的机器人，或者使用原有的机器人：​

  * ​使用新建的机器人：（推荐）使用飞书扫码创建一个新的机器人，此插件将自动帮你完成机器人的创建、事件和回调配置、添加权限等等操作，并自动关联到 OpenClaw 项目。​

  * ​使用 OpenClaw 已关联的机器人：如果你已经有一个关联过 OpenClaw 的飞书机器人，也可以直接使用。但为了体验飞书官方插件的完整能力，你还需要为机器人手动开启一系列配置。​

使用新建的机器人​

1.

在扣子编程的 OpenClaw 项目中，打开终端窗口。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27499%27%20height=%27239%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk5IiBoZWlnaHQ9IjIzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

执行以下命令，安装飞书官方插件。 ​

  * 安装新插件的同时，扣子编程会自动移除原飞书插件。 ​

  * ​

Shell

复制

npx -y @larksuite/openclaw-lark-tools install​

​

3.

根据页面提示，选择 Create a new bot，并敲击回车。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27530%27%20height=%27222%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMwIiBoZWlnaHQ9IjIyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

打开飞书客户端，扫描终端输出的二维码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27534%27%20height=%27283%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM0IiBoZWlnaHQ9IjI4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

根据飞书客户端的提示，创建飞书机器人。​

a.

设置机器人名称，并单击​

​

​

​

6.

在飞书向机器人发送一条消息，验证机器人是否正常工作。​

  * ​

使用 OpenClaw 已关联的机器人​

1.

在扣子编程的 OpenClaw 项目中，打开终端窗口。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27499%27%20height=%27239%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk5IiBoZWlnaHQ9IjIzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

执行以下命令，安装飞书官方插件。 ​

  * 安装新插件的同时，扣子编程会自动移除原飞书插件。 ​

  * ​

Shell

复制

npx -y @larksuite/openclaw-lark-tools install​

​

3.

根据页面提示，选择 Use an existing bot linked to OpenClaw (使用 OpenClaw 已关联的机器人)，并敲击回车。​

  * 看到以下提示，表示已成功安装官方插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273110%27%20height=%271069.0625%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzExMCIgaGVpZ2h0PSIxMDY5LjA2MjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

4.

完成配对。​

a.

打开飞书客户端，找到你已关联 OpenClaw 的飞书机器人，输入任意一条消息。​

b.

飞书机器人会回复你一条包含配对码的消息，复制配对码。​

c.

回到扣子编程，将配对码发送给扣子 AI。​

  * 扣子 AI 会自动完成机器人配对。​

  * 获取配对码：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27260%27%20height=%27118%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYwIiBoZWlnaHQ9IjExOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

发送给扣子 AI：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27235%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM1IiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

5.

在飞书向机器人发送一条消息，验证机器人是否正常工作。​

  * 例如，发送 /feishu start，如果机器人回复了飞书 OpenClaw 的插件版本，表示已完成机器人配对。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27417%27%20height=%27182%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE3IiBoZWlnaHQ9IjE4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

（可选）为飞书机器人添加权限和配置。​

  * 完成配对后，飞书机器人可以正常对话、回复你的问题，但是但为了体验飞书官方插件的完整能力，你还需要为机器人手动开启一系列配置。​

a.

登录[飞书开放平台](<https://open.feishu.cn/app?lang=zh-CN>)，找到你的飞书机器人应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27412%27%20height=%27257%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEyIiBoZWlnaHQ9IjI1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为飞书机器人添加必要的权限。​

i.

在左侧目录树选择安全配置，开启刷新 user_access_token 开关。 ​

  * 说明

安全配置页面若无此配置，说明企业默认开启了刷新 user_access_token 开关，可跳过此步骤。 ​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27542%27%20height=%27271%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQyIiBoZWlnaHQ9IjI3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

ii.

在左侧目录中选择开发配置 > 权限管理，单击批量导入/导出权限。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27537%27%20height=%27240%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM3IiBoZWlnaHQ9IjI0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

iii.

在导入页签中，将如下权限替换原有示例，单击下一步，确认新增权限按钮。​

  * 说明

建议导入以下完整权限。缺失部分权限会影响你的飞书机器人能力与表现。​

​

  * ​

JSON

复制

{​

"scopes": {​

"tenant": [​

"contact:contact.base:readonly",​

"docx:document:readonly",​

"im:chat:read",​

"im:chat:update",​

"im:message.group_at_msg:readonly",​

"im:message.p2p_msg:readonly",​

"im:message.pins:read",​

"im:message.pins:write_only",​

"im:message.reactions:read",​

"im:message.reactions:write_only",​

"im:message:readonly",​

"im:message:recall",​

"im:message:send_as_bot",​

"im:message:send_multi_users",​

"im:message:send_sys_msg",​

"im:message:update",​

"im:resource",​

"application:application:self_manage",​

"cardkit:card:write",​

"cardkit:card:read"​

],​

"user": [​

"contact:user.employee_id:readonly",​

"offline_access","base:app:copy",​

"base:field:create",​

"base:field:delete",​

"base:field:read",​

"base:field:update",​

"base:record:create",​

"base:record:delete",​

"base:record:retrieve",​

"base:record:update",​

"base:table:create",​

"base:table:delete",​

"base:table:read",​

"base:table:update",​

"base:view:read",​

"base:view:write_only",​

"base:app:create",​

"base:app:update",​

"base:app:read",​

"sheets:spreadsheet.meta:read",​

"sheets:spreadsheet:read",​

"sheets:spreadsheet:create",​

"sheets:spreadsheet:write_only",​

"docs:document:export",​

"docs:document.media:upload",​

"board:whiteboard:node:create",​

"board:whiteboard:node:read",​

"calendar:calendar:read",​

"calendar:calendar.event:create",​

"calendar:calendar.event:delete",​

"calendar:calendar.event:read",​

"calendar:calendar.event:reply",​

"calendar:calendar.event:update",​

"calendar:calendar.free_busy:read",​

"contact:contact.base:readonly",​

"contact:user.base:readonly",​

"contact:user:search",​

"docs:document.comment:create",​

"docs:document.comment:read",​

"docs:document.comment:update",​

"docs:document.media:download",​

"docs:document:copy",​

"docx:document:create",​

"docx:document:readonly",​

"docx:document:write_only",​

"drive:drive.metadata:readonly",​

"drive:file:download",​

"drive:file:upload",​

"im:chat.members:read",​

"im:chat:read",​

"im:message",​

"im:message.group_msg:get_as_user",​

"im:message.p2p_msg:get_as_user",​

"im:message:readonly",​

"search:docs:read",​

"search:message",​

"space:document:delete",​

"space:document:move",​

"space:document:retrieve",​

"task:comment:read",​

"task:comment:write",​

"task:task:read",​

"task:task:write",​

"task:task:writeonly",​

"task:tasklist:read",​

"task:tasklist:write",​

"wiki:node:copy",​

"wiki:node:create",​

"wiki:node:move",​

"wiki:node:read",​

"wiki:node:retrieve",​

"wiki:space:read",​

"wiki:space:retrieve",​

"wiki:space:write_only"​

]​

}​

}​

​

iv.

在弹窗中确认权限无误后，单击申请开通按钮，完成操作。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27546%27%20height=%27293%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ2IiBoZWlnaHQ9IjI5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

为飞书机器人配置事件和回调。​

  * 飞书官方插件内置了一些技能，便于你更好地和机器人交流，如果未配置相关事件和回调，可能影响部分技能的使用体验和效果。​

i.

在左侧目录树选择开发配置 > 事件与回调。​

ii.

选择事件配置页签，在已添加事件区域，单击添加事件按钮。​

iii.

输入 “action”，选择消息被reaction、消息被取消reaction两个权限，并单击添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27566%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY2IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 通过 reaction 权限，你可以在对话中实现以下效果：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27398%27%20height=%27213%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk4IiBoZWlnaHQ9IjIxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

选择回调配置页签，单击订阅方式旁的编辑按钮。​

iv.

选择使用 长连接 接收回调，并单击保存按钮。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27438%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM4IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

v.

在已添加事件区域，单击添加事件按钮，选择卡片回传交互，并单击添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27512%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEyIiBoZWlnaHQ9IjI1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

新建机器人版本并发布。 ​

i.

单击顶部的创建版本按钮。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27506%27%20height=%27152%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA2IiBoZWlnaHQ9IjE1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

ii.

按需配置应用版本号、默认能力及更新说明等信息，并在页面底部的保存按钮，创建版本。 ​

iii.

根据页面提示发布应用。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27575%27%20height=%27262%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc1IiBoZWlnaHQ9IjI2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 待管理员通过发布审核后，即可正式在飞书中使用全新的飞书官方插件，体验新版效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27574%27%20height=%27176%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc0IiBoZWlnaHQ9IjE3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

  * ​如何切换授权的飞书账号？​

  * ​OpenClaw 项目里，扣子 AI 能做什么？​

  * ​如何取消部署？​

  * ​OpenClaw 对话中断或无响应？​

  * ​为什么我的飞书机器人和 OpenClaw 的连接总是中断​

上一篇

趣味玩法

下一篇

OpenClaw 集成企业微信