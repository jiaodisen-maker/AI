---
source_url: https://docs.coze.cn/tutorial/openclaw_dingding
title: 'OpenClaw 集成钉钉 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:43Z
---

# OpenClaw 集成钉钉 - 文档 - 扣子

OpenClaw 集成钉钉

如果你想通过钉钉和你的 OpenClaw AI 助理对话，可以在部署 OpenClaw 部署之后，创建一个钉钉机器人，通过扣子 AI 配置 OpenClaw 的钉钉渠道。​

关于 OpenClaw 的详细说明，可参考​一键部署 OpenClaw 并集成飞书。​

准备工作​

​

项目​| 说明​  
---|---  
订阅套餐及配额​| [购买以下任一一款订阅套餐](<https://code.coze.cn/subscription-paywall>)：​

  * 个人高阶版：最多 1 个 OpenClaw 项目。​

  * 个人旗舰版：最多 3 个 OpenClaw 项目。​

  * 企业标准版：最多 1 个 OpenClaw 项目。​

  * 企业旗舰版：最多 1 个 OpenClaw 项目。​

  
使用限制​| 如果取消部署，对话随时可能因沙箱回收而中断。​  
费用说明​| 

  * 使用 OpenClaw 会消耗你的扣子编程积分（包括对话、大模型调用、图片生成等）。​

  * OpenClaw 的 Token 消耗较高，你可以选择省流版以节省 Token 成本。​

  
  
​

操作步骤​

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
渠道配置​| 如果无需配置飞书渠道，则跳过此步骤，直接单击确定。​如果后续希望再配置飞书渠道，可参考​步骤二：配置飞书渠道。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27488%27%20height=%27260%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg4IiBoZWlnaHQ9IjI2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：创建钉钉应用并完成配置​

1.

创建钉钉应用。​

a.

登录[钉钉开放平台](<https://open-dev.dingtalk.com/>)，单击创建按钮。​

  * 要创建钉钉应用，您的钉钉账号需要有开发者权限。您可以联系您的组织管理员获取钉钉开放平台的开发权限。​

b.

在左侧目录树中选择企业内部应用 > 钉钉应用，在页面右上角单击创建应用按钮。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27464%27%20height=%27163%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY0IiBoZWlnaHQ9IjE2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

配置应用名称、图标等信息后，单击保存。​

2.

为钉钉应用添加权限。​

  * 钉钉应用需要申请的权限如下：​

  * ​

Plain Text

复制

Card.Instance.Write​

Card.Streaming.Write​

qyapi_robot_sendmsg​

​

  * 申请权限的操作步骤如下：​

a.

登录[钉钉应用控制台](<https://open-dev.dingtalk.com/fe/app>)，单击前文创建的应用名称进入其详情页。​

b.

在左侧目录树选择开发配置 > 权限管理。​

c.

在搜索框中输入Card，勾选互动卡片实例写权限与AI卡片流式更新权限，单击批量申请按钮完成操作。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27388%27%20height=%27187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg4IiBoZWlnaHQ9IjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

在搜索框中输入qyapi_robot_sendmsg，单击企业内机器人发送消息权限右侧操作列的立即开通按钮完成操作。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27410%27%20height=%27194%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEwIiBoZWlnaHQ9IjE5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

配置钉钉机器人。​

a.

在左侧目录树选择应用能力 > 添加应用能力，单击机器人卡片的添加按钮。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27408%27%20height=%27161%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA4IiBoZWlnaHQ9IjE2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

在机器人配置页面，打开机器人配置开关。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27416%27%20height=%27240%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE2IiBoZWlnaHQ9IjI0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

将消息接收模式调整为 Stream 模式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27490%27%20height=%27118%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkwIiBoZWlnaHQ9IjExOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

单击发布按钮，保存配置。​

4.

发布应用版本。​

a.

在左侧目录树选择应用发布 > 版本管理与发布，并单击创建新版本按钮。​

b.

按需配置应用版本号、可见范围等信息后，单击保存按钮。​

c.

在弹窗中单击确认发布按钮，发布应用版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27586%27%20height=%27336%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg2IiBoZWlnaHQ9IjMzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

获取应用信息。​

  * 在左侧目录树选择基础信息 > 凭证与基础信息，找到并复制 AppKey、AppSecret、App ID 和 CorpId。这些密钥信息将被用于后续的渠道配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27614%27%20height=%27220%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE0IiBoZWlnaHQ9IjIyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：配置 OpenClaw 钉钉渠道​

扣子已经为你的 OpenClaw 项目安装了钉钉插件，创建钉钉应用并完成配置后，只要通过对话向扣子 AI 提供密钥信息即可。​

1.

登录扣子编程，找到你的 OpenClaw 项目。​

2.

在左下角输入框中，输入你的指令，请扣子 AI 安装钉钉插件，并配置相关密钥。​

​

Plain Text

复制

请帮我配置钉钉机器人​

1\. AppKey：<your_appkey>​

2\. AppSecret：<your_appsecret>​

3\. App ID：<your_appId>​

4\. CorpId：<your_CorpId>​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27938%27%20height=%271436%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTM4IiBoZWlnaHQ9IjE0MzYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

步骤四：体验效果​

当你的钉钉应用通过企业管理员审核之后，你可以打开钉钉 App，找到 OpenClaw AI 助理，体验对话效果。​

找到 OpenClaw AI 助理：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272042%27%20height=%271272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA0MiIgaGVpZ2h0PSIxMjcyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

对话效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271274%27%20height=%271180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI3NCIgaGVpZ2h0PSIxMTgwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

常见问题​

  * ​切换模型​

  * ​OpenClaw 项目里，扣子 AI 能做什么？​

  * ​如何取消部署？​

  * ​OpenClaw 对话中断或无响应？​

上一篇

OpenClaw 集成微信

下一篇

Openclaw 常见问题