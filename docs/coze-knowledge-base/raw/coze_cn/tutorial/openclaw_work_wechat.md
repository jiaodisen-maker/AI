---
source_url: https://docs.coze.cn/tutorial/openclaw_work_wechat
title: 'OpenClaw 集成企业微信 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:38Z
---

# OpenClaw 集成企业微信 - 文档 - 扣子

OpenClaw 集成企业微信

OpenClaw 是一款开源的主动型 AI Agent。你可以通过 OpenClaw 将多渠道通信能力与大语言模型深度集成，创建拥有持久记忆与主动执行能力的定制化 AI 助理。​

关于 OpenClaw 的详细说明，可参考​什么是 OpenClaw。​

准备工作​

​

项目​| 说明​  
---|---  
订阅套餐及配额​| [购买以下任一一款订阅套餐](<https://code.coze.cn/subscription-paywall>)：​

  * 个人高阶版：最多 1 个 OpenClaw 项目。​

  * 个人旗舰版：最多 3 个 OpenClaw 项目。​

  * 企业标准版：最多 1 个 OpenClaw 项目。​

  * 企业旗舰版：最多 1 个 OpenClaw 项目。​

  
使用限制​| 如果取消部署，对话随时可能因环境回收而中断。​  
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
    * 满血版：OpenClaw 原版默认配置，无差异的性能体验。Token 消耗相对较多，适合需要极致性能的用户。​
    * 省流版（默认）：在满血版的基础上调整了上下文压缩和心跳配置，Token 消耗相对较低，但部分场景下可能会有一些性能损失。省流版适合需要控制 Token 成本的用户。​  
渠道配置​| 你和 OpenClaw 个人助理对话的渠道，OpenClaw 将作为该渠道的机器人应用和你展开对话。​
    * 若无需发布到渠道，则直接单击确定来跳过渠道配置。若未配置渠道，你只能在 Web UI 界面上和 OpenClaw 个人助理对话。​
    * 如需配置企业微信渠道，参考后续流程完成配置。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27637%27%20height=%27397%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM3IiBoZWlnaHQ9IjM5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：配置企业微信渠道​

扣子编程现已支持一键配置飞书渠道，在 OpenClaw 配置页面单击去配置按钮，根据页面提示扫描二维码，即可和你的 OpenClaw 助手在企业微信对话。​

详细操作步骤如下：​

1.

打开 OpenClaw 配置页面。​

  * 你可以在 OpenClaw 页面右上角单击配置图标，进入 OpenClaw 配置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27578%27%20height=%27366%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc4IiBoZWlnaHQ9IjM2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在渠道配置区域，找到企业微信，并单击去配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27583%27%20height=%27364%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgzIiBoZWlnaHQ9IjM2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

使用企业微信 App 扫描二维码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27514%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE0IiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

根据企业微信的页面提示，创建机器人并授权。​

创建机器人：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27160%27%20height=%27347%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYwIiBoZWlnaHQ9IjM0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为机器人授权：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27157%27%20height=%27340%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU3IiBoZWlnaHQ9IjM0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

创建成功：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27155%27%20height=%27336%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1IiBoZWlnaHQ9IjMzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

5.

等待一切就绪。​

  * 在扣子编程中看到以下页面，表示企业微信渠道已配置完成。你可以去企业微信 APP 中和 OpenClaw 助手对话了。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27472%27%20height=%27289%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcyIiBoZWlnaHQ9IjI4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：体验效果​

当你的企业微信机器人通过企业管理员审核之后，你可以打开企业微信，找到 OpenClaw AI 助理，体验对话效果。​

企业微信 OpenClaw 机器人的名称默认为 XX 的机器人，你可以直接在企业微信中搜索名称，找到机器人。​

找到 OpenClaw AI 助理：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27174%27%20height=%27377%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc0IiBoZWlnaHQ9IjM3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

对话效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27170%27%20height=%27368%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcwIiBoZWlnaHQ9IjM2OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

相关操作​

修改企业微信机器人名称和头像​

企业微信 OpenClaw 机器人的名称默认为 XX 的机器人，头像为默认头像。你可以在企业微信的智能机器人应用中修改机器人名称和头像。​

1.

搜索智能机器人，并打开应用。​

2.

找到你的 OpenClaw 机器人，其名称默认为 XX 的机器人。​

3.

打开机器人页面，在右上角单击编辑。​

4.

修改机器人名称和头像，单击保存即可。​

搜索智能机器人应用：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27146%27%20height=%27316%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ2IiBoZWlnaHQ9IjMxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

打开智能机器人应用：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27147%27%20height=%27319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ3IiBoZWlnaHQ9IjMxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

找到机器人，单击编辑：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27147%27%20height=%27319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ3IiBoZWlnaHQ9IjMxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

修改名称和头像：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27144%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ0IiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

更换企业微信账号​

如果你想把 OpenClaw 换绑到另一个企业微信账号，需要重新配置一下企业微信渠道，使用新的企业微信账号扫码授权即可。​

1.

打开 OpenClaw 配置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27466%27%20height=%27295%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY2IiBoZWlnaHQ9IjI5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

找到企业微信，展开折叠菜单，单击重新配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27461%27%20height=%27288%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYxIiBoZWlnaHQ9IjI4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

使用新的企业微信账号扫码授权即可。​

常见问题​

  * ​切换模型​

  * ​OpenClaw 项目里，扣子 AI 能做什么？​

  * ​如何取消部署？​

  * ​OpenClaw 对话中断或无响应？​

上一篇

一键部署 OpenClaw 并集成飞书

下一篇

OpenClaw 集成微信