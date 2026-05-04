---
source_url: https://docs.coze.cn/guides/email_integration
title: 'Email - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:40Z
---

# Email - 文档 - 扣子

Email

扣子编程支持集成电子邮件能力，可让你的 AI 编程项目便捷实现邮件的发送与接收功能，满足办公协同、通知推送等需求。​

支持的能力​

  * 接收邮件​

  * 向指定的邮箱发送邮件​

  * 管理邮件等主流的邮箱服务​

配置方式​

步骤一：获取邮箱配置信息​

根据你所使用的邮箱，获取对应的授权码、SMTP 端口、SMTP 服务器地址、IMAP 服务器地址、IMAP 端口等关键配置信息。不同邮箱服务商的配置信息不同，请以对应邮箱官方文档或设置页面提供的标准配置为准。​

步骤二：为工作空间启用外部集成（企业版管控操作）​

企业旗舰版由组织管理员统一管控工作空间内外部集成的可用性。即组织管理员可以为工作空间设置空间内可用的外部集成。默认情况下，企业旗舰版所有工作空间内均不可使用外部集成。具体操作，请参考​步骤一：为工作空间启用外部集成。​

说明

企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

​

步骤三：配置 Email 集成​

在集成管理页面，单击 Email 集成对应的配置，然后完成如下参数配置。配置完成后，当前空间下所有集成了 Email 能力的项目，均通过该邮箱账号发送邮件，或读取该邮箱账号内的邮件。​

说明

配置外部集成后，系统会根据项目类型自动添加对应的官方技能到技能列表中。请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

参数​| 说明​  
---|---  
Account​| 邮箱登录账号。​  
Auth Code​| 邮箱服务商提供的授权码，用于第三方客户端登录验证。不是邮箱密码。​  
SMTP Server​| SMTP 邮件服务器的地址。SMTP 协议用于发送邮件。​  
SMTP Port​| SMTP 邮件服务器的端口号。​  
IMAP Server​| IMAP 邮件服务器的地址。IMAP 协议用于接收和管理邮件。​  
IMAP Port​| IMAP 邮件服务器的端口号。​  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27548%27%20height=%27343%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ4IiBoZWlnaHQ9IjM0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271044%27%20height=%27814.468085106383%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA0NCIgaGVpZ2h0PSI4MTQuNDY4MDg1MTA2MzgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

步骤四：为项目接入 Email 集成​

配置 Email 集成后，你可以在开发 AI 编程项目时，输入添加 Email 集成的相关需求，让扣子 AI 自动识别并加载邮件技能来接入入 Email 集成。​

发送邮件时，系统是将 Email 集成中已配置的邮箱账号作为发件方，向指定的目标账户投递邮件，而非向该配置邮箱账号本身发送邮件。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27586%27%20height=%27375%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg2IiBoZWlnaHQ9IjM3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果演示​

例如创建一个邮件助手，集成数据库与 Email 能力后，该助手可自动撰写邮件，并调取数据库中存储的目标邮箱地址，完成邮件的自动发送。​

与智能体对话​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271616%27%20height=%271119.3569739952718%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYxNiIgaGVpZ2h0PSIxMTE5LjM1Njk3Mzk5NTI3MTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

收到邮件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271784%27%20height=%271265.919191919192%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc4NCIgaGVpZ2h0PSIxMjY1LjkxOTE5MTkxOTE5MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

飞书多维表格

下一篇

微信公众号