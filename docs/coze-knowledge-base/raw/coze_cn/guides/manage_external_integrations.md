---
source_url: https://docs.coze.cn/guides/manage_external_integrations
title: '管理外部集成服务 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:50Z
---

# 管理外部集成服务 - 文档 - 扣子

管理外部集成服务

外部集成是扣子编程提供的第三方服务对接功能，支持连接飞书、企业微信等平台，实现 AI 编程项目与外部服务的交互。本文介绍扣子编程外部集成的相关操作步骤。​

不同套餐对应的操作流程如下：​

  * 企业旗舰版：组织管理员为工作空间启用外部集成 > 空间管理员配置外部集成 > 为项目接入外部集成。​

  * 其他版本：空间管理员配置外部集成 > 为项目接入外部集成。​

企业旗舰版​

企业旗舰版可参考如下步骤配置外部集成。​

步骤一：为工作空间启用外部集成​

企业旗舰版由组织管理员统一管控组织内外部集成的可用性，即组织管理员可以为工作空间启用空间内可用的外部集成。默认情况下，外部集成在企业组织的工作空间内处于禁用状态。​

企业组织管理员为工作空间启用外部集成后，空间管理员才能在工作空间内配置外部集成。​

说明

  * 企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

  * 组织管理员禁用指定工作空间内的某个外部集成后，该工作空间的管理员无法配置该外部集成。​

  * 需要注意的是禁用前已完成配置的外部集成，不受禁用操作影响，仍可正常接入项目。如需禁用该外部集成的可用状态，可在工作空间内删除该外部集成。​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击集成管理，然后在页面右上角单击组织集成管理。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27406%27%20height=%27275%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6fcce07a4d734e8cbaa81618fb920cde~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

在组织集成管理页面，单击目标外部集成对应的配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27414%27%20height=%27414%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE0IiBoZWlnaHQ9IjQxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

选择目标工作空间，单击开启。​

步骤二：在工作空间中配置集成的连接​

空间管理员在空间中配置外部集成，用于建立扣子编程与外部集成的连接。配置完成后，外部集成状态将变为已配置。开发者在该工作空间下开发 AI 编程项目时，扣子 AI 会自动判断并接入该外部集成，无需额外配置。​

说明

外部集成配置在工作空间内生效，所有项目共享。​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击集成管理。​

3.

在外部集成区域，单击添加集成。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27455%27%20height=%27310%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU1IiBoZWlnaHQ9IjMxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击目标外部集成对应的配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27442%27%20height=%27131%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQyIiBoZWlnaHQ9IjEzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

配置外部集成。​

  * 不同外部集成对应的连接配置不同，具体配置说明，请参考配置文档。​

  * ​飞书消息​

  * ​飞书多维表格​

  * ​Email​

  * ​微信公众号​

  * ​企业微信机器人​

  * ​火山方舟​

目前，扣子编程的集成服务均有配套的官方技能。外部集成配置完成后，系统会根据项目类型自动添加对应的官方技能到技能列表中，供扣子 AI 加载。​

说明

请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%27369%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYzIiBoZWlnaHQ9IjM2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：为项目接入外部集成​

完成上述配置后，你在与扣子 AI 协作开发 AI 编程项目时，只需用自然语言清晰描述所需功能，扣子 AI 会自动识别关键词，加载对应的技能来接入外部集成。试运行或正式运行 AI 编程项目时，将自动触发外部集成，使用对应的功能。例如，你可以跟扣子 AI 对话：​

​

Plain Text

复制

让智能体完成任务后，自动向指定飞书群推送结果通知​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27536%27%20height=%27341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM2IiBoZWlnaHQ9IjM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

其他版本​

个人版（免费版、进阶版、高阶版、旗舰版）和企业标准版的工作空间默认可使用外部集成功能，需由空间管理员先在空间内先配置外部集成。具体操作步骤如下：​

步骤一：在工作空间中配置集成的连接​

空间管理员在空间中配置外部集成，用于建立扣子编程与外部集成的连接。配置完成后，外部集成状态将变为已配置。开发者在该工作空间下开发 AI 编程项目时，扣子 AI 会自动判断并接入该外部集成，无需额外配置。​

说明

配置在工作空间内生效，所有项目共享。​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击集成管理。​

3.

单击目标外部集成对应的配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27516%27%20height=%27284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE2IiBoZWlnaHQ9IjI4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

配置外部集成。​

  * 不同外部集成对应的连接配置不同，具体配置说明，请参考配置文档。​

  * ​飞书消息​

  * ​飞书多维表格​

  * ​Email​

  * ​微信公众号​

  * ​企业微信机器人​

  * ​火山方舟​

目前，扣子编程的集成服务均有配套的官方技能。外部集成配置完成后，系统会根据项目类型自动添加对应的官方技能到技能列表中，供扣子 AI 加载。​

说明

请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%27369%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYzIiBoZWlnaHQ9IjM2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：为项目接入外部集成​

完成上述配置后，你在与扣子 AI 协作开发 AI 编程项目时，只需用自然语言清晰描述所需功能，扣子 AI 会自动识别关键词，加载对应的技能来接入外部集成。试运行或正式运行 AI 编程项目时，将自动触发外部集成，使用对应的功能。示例如下：​

​

Plain Text

复制

让智能体完成任务后，自动向指定飞书群推送结果通知​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27536%27%20height=%27341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM2IiBoZWlnaHQ9IjM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

相关操作​

下述表格罗列了外部集成的相关操作。​

​

操作​| 说明​| 图示​  
---|---|---  
禁用外部集成（企业旗舰版）​| 企业组织管理员可以在集成管理页面，禁用工作空间内的外部集成。​

1.在集成管理页面的右上角，单击组织集成管理。​

2.单击目标外部集成对应的配置。​

3.选中目标工作空间，单击关闭。​
禁用后，此前未配置过该外部集成的工作空间，其下所有项目均无法接入该外部集成。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271214%27%20height=%271220%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIxNCIgaGVpZ2h0PSIxMjIwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
删除外部集成配置（企业旗舰版）​| 由于禁用前已完成配置的外部集成，不受禁用操作影响，可正常接入项目。如需禁用该外部集成的可用状态，需在工作空间内删除该外部集成。即在集成管理页面，单击目标集成对应的删除。​如果已在项目中接入该外部集成，需先在项目中通过自然语言对话移除，再在工作空间中删除。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271237%27%20height=%27794.4036697247707%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIzNyIgaGVpZ2h0PSI3OTQuNDAzNjY5NzI0NzcwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
取消外部集成配置（其他版本）​​| 针对个人版（免费版、进阶版、高阶版、旗舰版）和企业标准版，空间管理员可以在工作空间内取消外部集成配置。取消后，该空间下所有的项目均不能接入该集成服务。​

1.在集成管理页面，单击目标集成对应的管理。​

2.在管理外部集成面板中，单击取消配置。​

  * 如果已在项目中接入该外部集成，需先在项目中通过自然语言对话移除，再在工作空间中取消。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271245%27%20height=%27776.6972477064221%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI0NSIgaGVpZ2h0PSI3NzYuNjk3MjQ3NzA2NDIyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看工作空间内的外部集成​| 在集成管理页面，查看该工作空间内可使用的外部集成列表。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271238%27%20height=%271065%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIzOCIgaGVpZ2h0PSIxMDY1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
更新外部集成配置​| 

1.在集成管理页面，单击目标集成对应的管理。​

2.在管理外部集成面板中，修改配置，单击更新。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271242%27%20height=%27780.5229357798165%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI0MiIgaGVpZ2h0PSI3ODAuNTIyOTM1Nzc5ODE2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看外部集成的关联项目​| 

1.在集成管理页面，单击目标集成对应的管理。​

2.在管理外部集成面板中，查看已接入当前外部集成的项目。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271554%27%20height=%27905.3119266055045%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1NCIgaGVpZ2h0PSI5MDUuMzExOTI2NjA1NTA0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

常见问题​

  * ​为什么我的空间无法配置外部集成？​

  * ​组织管理员禁用了某个外部集成后，空间里原已配置的集成是否能继续使用？​

  * ​接入飞书消息集成后，为什么空间内的项目都使用同一个飞书机器人发送消息？​

  * ​支持接入第三方的 API 吗？​

上一篇

火山方舟

下一篇

集成大模型能力