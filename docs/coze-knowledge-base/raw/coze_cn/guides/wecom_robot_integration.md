---
source_url: https://docs.coze.cn/guides/wecom_robot_integration
title: '企业微信机器人 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:45Z
---

# 企业微信机器人 - 文档 - 扣子

企业微信机器人

扣子编程支持集成企业微信机器人能力，以实现通过企业微信机器人发送消息。​

配置方式​

步骤一：获取企业微信机器人配置信息​

在集成企业微信机器人能力前，需要先在企业微信侧创建一个群机器人，并获取其对应的 Webhook URL。具体操作，请参考[消息推送 Webhook 地址](<https://open.work.weixin.qq.com/help2/pc/14931#二、「消息推送」添加入口>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27290%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a6de0e306f7d451eb87ac04a6358ca75~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：为工作空间启用外部集成（企业旗舰版管控操作）​

企业旗舰版由组织管理员统一管控工作空间内外部集成的可用性。即组织管理员可以为工作空间设置空间内可用的外部集成。默认情况下，企业旗舰版所有工作空间内均不可使用外部集成。具体操作，请参考​步骤一：为工作空间启用外部集成。​

说明

企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

​

步骤三：配置企业微信机器人集成​

在集成管理页面，单击企业微信机器人对应的配置，然后输入你已获取的 Webhook Key。配置后，当前空间下所有集成了企业微信机器人能力的项目，均通过该企业微信机器人发送消息。​

说明

配置外部集成后，系统会根据项目类型自动添加对应的官方技能到技能列表中。请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27518%27%20height=%27340%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE4IiBoZWlnaHQ9IjM0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271049%27%20height=%27823.3286052009456%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA0OSIgaGVpZ2h0PSI4MjMuMzI4NjA1MjAwOTQ1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤四：为项目接入企业微信机器人集成​

配置企业微信机器人集成后，你可以在开发 AI 编程项目时，输入添加企业微信机器人集成的需求，让扣子 AI 自动识别并加载企业微信机器人技能来接入企业微信机器人集成。集成后，可以通过企业微信机器人 Webhook 发送文本、卡片等形式的消息，并支持@功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27554%27%20height=%27355%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU0IiBoZWlnaHQ9IjM1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果演示​

例如搭建一个搜图工作流，并将搜索到的图片发送到企业微信群中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271677%27%20height=%27860.3049645390071%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY3NyIgaGVpZ2h0PSI4NjAuMzA0OTY0NTM5MDA3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI2IiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

常见问题​

​发送图片到企业微信，出现 SignatureDoesNotMatch 错误，如何处理？​

上一篇

微信公众号

下一篇

火山方舟