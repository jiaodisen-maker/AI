---
source_url: https://docs.coze.cn/tutorial/openclaw_wechat
title: 'OpenClaw 集成微信 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:39Z
---

# OpenClaw 集成微信 - 文档 - 扣子

OpenClaw 集成微信

如果你想通过微信和你的 OpenClaw AI 助理对话，可以在部署 OpenClaw 部署之后，创建一个微信机器人，通过扣子 AI 配置 OpenClaw 的微信渠道。​

关于 OpenClaw 的详细说明，可参考​一键部署 OpenClaw 并集成飞书。​

注意事项​

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

  
微信限制​| 

  * 个人专用：微信ClawBot是你与自己拥有的 OpenClaw 之间的私密消息通道，其他用户无法添加你的微信ClawBot。​

  * 不支持群聊：目前，微信ClawBot不能被加入微信群，仅支持个人单点使用。​

  * 不支持自动化操作：微信ClawBot仅作为消息通道，不会自动化操作你的微信。​

  
  
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

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27642%27%20height=%27334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQyIiBoZWlnaHQ9IjMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：配置微信渠道​

1.

在 OpenClaw 配置页面找到微信渠道，单击去创建。​

  * 如果是刚刚部署的 OpenClaw 项目，页面会自动弹出 OpenClaw 配置页面。​

  * 如果之前已经部署 OpenClaw 并配置了其他渠道，可以在 OpenClaw 项目页面右上角单击配置按钮，打开 OpenClaw 配置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27641%27%20height=%27331%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQxIiBoZWlnaHQ9IjMzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

打开微信客户端，扫描屏幕显示的二维码。​

  * 说明

    * 微信客户端版本要求为 8.0.70 及以上，如果版本号不符合要求，扫码时会提示更新版本。更新版本后需要重启微信、再扫码。​

    * 首次配置微信渠道时，生成二维码预计耗时 3~4 分钟左右，请耐心等待。​

    * 二维码有效期为 5 分钟，如果微信扫码时提示二维码已过期，请手动刷新二维码后再试。​

​

3.

根据微信客户端提示，单击连接。​

4.

后台会自动完成渠道连接，并自动打开一个名为微信 ClawBot 的对话页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27190%27%20height=%27411%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwIiBoZWlnaHQ9IjQxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27185%27%20height=%27401%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg1IiBoZWlnaHQ9IjQwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

5.

输入任意一条消息，测试微信机器人是否能正常回复。 ​

  * 如果机器人及时回复消息，表示微信渠道已配置成功。为了方便后续快速打开机器人对话页面，建议你置顶对话。​

  * 测试回复：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27180%27%20height=%27389%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgwIiBoZWlnaHQ9IjM4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

打开设置页面：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27177%27%20height=%27383%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc3IiBoZWlnaHQ9IjM4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

置顶对话：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27178%27%20height=%27385%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc4IiBoZWlnaHQ9IjM4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

6.

（可选）设置机器人的备注名称。​

  * 由于微信客户端限制，搜索机器人的默认名称 微信 ClawdBot 可能搜索不到你的机器人。建议为机器人设置头像和备注，方便检索。​

  * 在机器人对话页面右上角单击设置图标，并在机器人详情页右上角展开隐藏菜单，单击备注名区域，根据页面提示输入机器人名称即可。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27162%27%20height=%27351%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYyIiBoZWlnaHQ9IjM1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27165%27%20height=%27357%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY1IiBoZWlnaHQ9IjM1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27164%27%20height=%27355%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY0IiBoZWlnaHQ9IjM1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤三：体验效果​

打开微信客户端，在对话列表中找到你的 OpenClaw 助理，体验对话效果。​

对话列表中，有 AI 标识的就是你的 OpenClaw 助理。​

找到 OpenClaw AI 助理：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27198%27%20height=%27428%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk4IiBoZWlnaHQ9IjQyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

对话效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27199%27%20height=%27431%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk5IiBoZWlnaHQ9IjQzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

常见问题​

  * ​已经配置过渠道，还能添加其他渠道吗？​

  * ​为什么微信是最新版本，扫码还是报错？​

  * ​微信中搜索不到机器人？​

  * ​为什么电脑、网页等微信客户端看不到 OpenClaw 对话？​

​

上一篇

OpenClaw 集成企业微信

下一篇

OpenClaw 集成钉钉