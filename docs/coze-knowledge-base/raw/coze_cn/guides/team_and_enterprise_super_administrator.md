---
source_url: https://docs.coze.cn/guides/team_and_enterprise_super_administrator
title: '设置企业超级管理员 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:46:41Z
---

# 设置企业超级管理员 - 文档 - 扣子

设置企业超级管理员

购买企业版时，系统会自动将主账号（RootUser）设为超级管理员。你还可自行添加或变更超级管理员。​

说明

  * 操作权限：主账号或具备火山引擎扣子控制台操作权限（如 CozeFullAccess 权限）的 IAM 用户，均可添加、变更超级管理员。​

  * 数量限制：支持 20 位企业超级管理员。​

​

配置说明​

扣子编程的超级管理员包括系统默认的超级管理员（RootUser）和手动添加的超级管理员。​

  * 系统默认指定的超级管理员：购买企业版套餐时，系统会自动指定 RootUser 为超级管理员。​

  * 手动添加超级管理员：支持在[扣子控制台](<https://console.volcengine.com/coze-pro/overview>)手动添加超级管理员。如果是火山引擎 IAM 用户，则也可在购买套餐页面添加一位超级管理员，详情请参考​购买订阅套餐。​

  * 超级管理员支持变更操作，分为以下两种情况：​

  * 未创建企业：支持直接变更超级管理员。​

  * 已创建企业：无法直接变更超级管理员。如需调整，需先在扣子火山控制台删除超级管理员用户，然后在扣子编程完成移除及资源转移，才能重新指定其他成员担任超级管理员。​

前提条件​

已创建成员。具体操作，请参考​步骤一：创建成员。​

添加超级管理员​

你可参考如下步骤，指定一个成员为超级管理员。​

1.

登录[火山引擎扣子控制台](<https://console.volcengine.com/coze-pro/overview>)。​

2.

在成员管理页面，单击设置超管。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272448%27%20height=%27639.6199524940617%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d73b19a1517d406fa19f51456e533ba4~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

在设置超级管理员对话框中，单击添加超管，选择目标成员，单击确定。​

4.

使用该超级管理员账号登录[扣子编程](<https://code.coze.cn/home>)，确认其超级管理员身份设置生效。​

变更超级管理员​

所有超级管理员均支持变更，分为以下两种情况：​

  * 在仅完成套餐购买但未创建企业时，可以在扣子火山控制台直接变更超级管理员。​

  * 已创建企业时，需先在扣子火山控制台删除超级管理员用户，然后在扣子编程完成移除及资源转移，才能重新指定其他成员担任超级管理员。​

未创建企业场景​

例如当前账号已购买企业版套餐且创建了 3 名成员 RootUser_xxx（系统生成）、Member_B、Member_C，但未创建企业。其中，RootUser_xxx 为系统默认超级管理员，Member_A 为你手动指定的超级管理员，你可以指定 Member_B 为新的超级管理员。​

1.

登录[火山引擎扣子控制台](<https://console.volcengine.com/coze-pro/overview>)。​

2.

在成员管理页面，单击设置超管。​

3.

在设置超级管理员对话框中，单击添加超管，选择目标成员（如 Member_B），单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27526%27%20height=%27291%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI2IiBoZWlnaHQ9IjI5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

使用新的超级管理员账号登录[扣子编程](<https://code.coze.cn/home>)，确认其超级管理员身份设置生效。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27527%27%20height=%27192%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI3IiBoZWlnaHQ9IjE5MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

已创建企业场景​

例如当前账号已购买企业版套餐且创建了 3 名成员 RootUser_xxx（系统生成）、Member_B、Member_C，并且已创建企业。其中，RootUser_xxx 作为系统默认超级管理员不可更改，Member_A 为你手动指定的超级管理员。如果你要指定 Member_B 为新的超级管理员，那么需要先在扣子火山控制台删除 Member_A 子用户，然后在扣子编程移除该用户，并将该用户的资源转移给超级管理员或管理员，最后再在扣子火山控制台指定 Member_B 为新的超级管理员。​

1.

登录[火山引擎扣子控制台](<https://console.volcengine.com/coze-pro/overview>)。​

2.

在成员管理页面，找到目标成员（如 Member_A），单击删除。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272350%27%20height=%27228.85985748218528%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM1MCIgaGVpZ2h0PSIyMjguODU5ODU3NDgyMTg1MjgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

3.

使用系统超级管理员账号登录[扣子编程](<https://code.coze.cn/home>)，移除超级管理员（如 Member_A），并转移其资源给超级管理员或管理员。具体操作，请参考​移除成员。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27567%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY3IiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

返回到[火山引擎扣子控制台](<https://console.volcengine.com/coze-pro/overview>)，在成员管理页面，单击设置超管。​

5.

在设置超级管理员对话框中，选择目标成员（如 Member_B），单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27561%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYxIiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

使用新的超级管理员账号登录[扣子编程](<https://code.coze.cn/home>)，确认其超级管理员身份设置生效。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27562%27%20height=%27205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYyIiBoZWlnaHQ9IjIwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看超级管理员​

在[扣子编程](<https://code.coze.cn/home>)的企业成员管理页面，查看企业超管。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273810%27%20height=%27634.2658959537572%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgxMCIgaGVpZ2h0PSI2MzQuMjY1ODk1OTUzNzU3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

​

上一篇

删除组织

下一篇

设置成员角色