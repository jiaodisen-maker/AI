---
source_url: https://docs.coze.cn/guides/publish_to_feishu
title: '发布到飞书 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:44:13Z
---

# 发布到飞书 - 文档 - 扣子

发布到飞书

飞书是一站式协同办公平台，为企业提供各种数字化办公解决方案。你可以将搭建的低代码智能体发布到飞书中，让飞书中的用户与智能体对话。​

如何发布到飞书​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。​

3.

在项目开发页面，选择低代码智能体。在页面右上角，单击发布。​

​

4.

首次发布时需要进行授权，根据引导完成授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2734.21965317919075%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a826fb79d2d14b7086ad55b443bb34cf~tplv-goo7wpa0wc-quality:q75.image)​

​

5.

勾选飞书渠道，然后单击发布。​

  * 说明

如果这是你的飞书租户第一次发布扣子智能体应用，你会收到飞书消息提醒。如果提醒应用审核通过，则你可以直接使用智能体。否则你需要等待企业管理员审核完成之后，才可以使用智能体。​

​

在飞书中分享你的智能体​

注意

目前只支持在同一飞书租户内分享智能体，不支持跨飞书租户分享智能体。​

​

你可以通过以下两种方式分享智能体：​

  * 方式一：分享智能体链接。​

a.

打开飞书客户端，单击智能体头像，然后再单击分享按钮将智能体分享给飞书好友。​

b.

被分享人需要点击链接申请使用权限，待智能体开发者通过权限申请后，被分享人即可使用智能体。​

  * 方式二：在开发者后台，修改智能体的可见范围。​

a.

登录[飞书开发者后台](<https://open.feishu.cn/>)。​

b.

单击已发布的智能体应用，进入应用详情页。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27531%27%20height=%27188%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMxIiBoZWlnaHQ9IjE4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

在左侧菜单栏，单击版本管理与发布，然后再单击创建版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27531%27%20height=%27159%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMxIiBoZWlnaHQ9IjE1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

d.

输入版本信息和更新版本说明，然后单击可用范围配置下的编辑链接，添加可使用该智能体的人员。最后单击保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27529%27%20height=%27261%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI5IiBoZWlnaHQ9IjI2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

e.

单击申请上线发布完成应用发布。​

  * 发布后，添加的用户就可以在飞书中搜到这个智能体，并与其对话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27532%27%20height=%27179%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMyIiBoZWlnaHQ9IjE3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

下架智能体​

如果不再需要在该渠道中展示智能体，你可以选择将其下架。下架的操作步骤请参见​下架智能体。​

你也可以登录[飞书开放平台](<https://open.larkoffice.com/app?from=devbotmenu>)，单击已发布的智能体，进入应用详情页，按照页面提示删除对应的智能体应用，即可完成智能体下架。​

常见问题​

发布到飞书后，无法生成回复，显示“正在回复”​

在飞书中和对话，如果智能体持续显示“正在回复”，但智能体分析页面中可查看到这条消息记录，且记录中显示智能体已正常回复，可能原因是智能体的回复中包含邮箱地址、电话号码等可能涉及个人隐私的信息，飞书屏蔽了这条消息。你可以在智能体分析页面的消息记录页签中查看智能体回复，确认回复中是否存在敏感信息。如果有，建议通过模型的提示词添加约束，例如“你的回复中不能包含任何的邮件地址、电话、姓名等可能涉及个人隐私的信息”。​

如何在飞书中清除消息记录？​

在飞书对话框中输入/clear，即可清除你和智能体对话的消息记录。​

飞书中的智能体回复和扣子平台中不一致​

如果飞书中智能体回复和扣子平台中不一致，可能原因如下：​

  * 智能体回复会受历史对话记录的影响，建议在飞书对话框中输入/clear，清除消息记录后重试。​

  * 模型回复具有随机性，对于同一个问题，每一次回复不一定完全相同。如果希望降低随机性，可以调整模型设置，调整方式可参考​设置模型。​

将智能体发布到飞书后，能否生成一个分享的微信二维码或者链接？​

目前，将智能体发布到飞书不支持生成微信二维码分享，如果需要分享链接给朋友或同事，可以分享智能体链接到飞书，具体操作请参见​在飞书中分享你的智能体。​

​

​

上一篇

发布到豆包

下一篇

发布到抖音小程序