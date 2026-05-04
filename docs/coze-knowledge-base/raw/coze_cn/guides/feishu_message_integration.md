---
source_url: https://docs.coze.cn/guides/feishu_message_integration
title: '飞书消息 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:35Z
---

# 飞书消息 - 文档 - 扣子

飞书消息

扣子编程支持集成飞书消息能力，以实现通过飞书自定义机器人 Webhook 发送文本、富文本或卡片消息。​

支持的能力​

  * 发送文本、富文本或卡片消息。​

  * @指定的群成员，@所有群成员。​

配置方式​

步骤一：获取飞书机器人 URL​

在集成飞书消息能力前，需要先在飞书侧创建一个自定义机器人，并获取其对应的 Webhook URL。具体操作，请参考[在群组中添加自定义机器人](<https://open.larkoffice.com/document/client-docs/bot-v3/add-custom-bot?lang=zh-CN#399d949c>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27394%27%20height=%27263%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/39668200e43c45e9be660d3471e3a137~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：为工作空间启用外部集成（企业旗舰版管控操作）​

企业旗舰版由组织管理员统一管控工作空间内外部集成的可用性。即组织管理员可以为工作空间设置空间内可用的外部集成。默认情况下，企业旗舰版所有工作空间内均不可使用外部集成。具体操作，请参考​步骤一：为工作空间启用外部集成。​

说明

企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

​

步骤三：配置飞书消息集成​

在集成管理页面，单击飞书消息对应的配置，然后输入你已获取的飞书机器人 Webhook URL。配置后，当前空间下所有集成了飞书消息能力的项目，均通过该飞书机器人发送消息。​

说明

配置外部集成后，系统会自动将开发项目所需的官方技能添加到技能列表中，不同项目对应的技能有所不同。请勿随意移除，以免开发时报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27591%27%20height=%27326%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTkxIiBoZWlnaHQ9IjMyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：为项目接入飞书消息集成​

配置飞书消息集成后，你可以在开发 AI 编程项目时，输入添加飞书消息集成的相关需求，让扣子 AI 自动识别并加载飞书消息技能来接入飞书消息外部集成。运行工作流，可以通过飞书自定义机器人 Webhook 发送文本、富文本或卡片消息，并支持@功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27518%27%20height=%27288%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE4IiBoZWlnaHQ9IjI4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

演示效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271636%27%20height=%27839.2718676122931%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYzNiIgaGVpZ2h0PSI4MzkuMjcxODY3NjEyMjkzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27816%27%20height=%27650.0992907801419%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODE2IiBoZWlnaHQ9IjY1MC4wOTkyOTA3ODAxNDE5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

​

  * ​

​

上一篇

内置集成

下一篇

飞书多维表格