---
source_url: https://docs.coze.cn/guides/set_pro_subusers
title: '为成员设置火山引擎 IAM 权限 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:46:46Z
---

# 为成员设置火山引擎 IAM 权限 - 文档 - 扣子

为成员设置火山引擎 IAM 权限

购买了企业版套餐后，超级管理员或管理员可以在企业中添加成员，共享企业中的高级权益与海量资源。如果同时希望成员具备火山引擎的操作权限（如操作火山扣子控制台、火山方舟控制台等），可在创建成员时开启允许访问火山引擎的功能，系统将为该成员创建同名的 IAM 用户，用于登录及操作火山引擎控制台。该用户默认拥有火山扣子控制台的只读权限（CozeReadOnlyAccess）。本文介绍如何为成员添加 IAM 权限，以操作火山引擎控制台。​

权限策略​

策略是访问控制 IAM 描述能力的一种方式，IAM 用户可以关联以下两种权限策略：​

  * 系统预设策略：统一由火山引擎创建，你只能使用不能修改，策略的版本更新由火山引擎维护。​

  * 用户自定义策略：如果系统预设策略无法满足你的授权需求，你可以新建自定义策略，策略的版本更新由你自己维护。详情请参考[新建自定义策略](<https://www.volcengine.com/docs/6257/1158323>)。​

下表为你提供扣子和火山方舟的系统预设策略，你可以直接为 IAM 用户授权。​

​

策略类别​| 策略名​| 描述​  
---|---|---  
扣子​| CozeReadOnlyAccess​| 扣子控制台的只读访问权限。​  
​| CozeFullAccess​| 扣子控制台的全部管理权限。​  
火山方舟​| ArkFullAccess​| 火山方舟（Ark）管理员用户，拥有所有 Ark 服务的权限，适合算法、研发等角色，可查看和配置方舟内全部资源。​  
​| ArkReadOnlyAccess​​| 火山方舟（Ark）只读用户，拥有 Ark 服务的只读权限，适合产品、运营等角色，可查看方舟内全部资源。​  
​| ArkLabelAccess​| 火山方舟（Ark）标注用户，拥有标准模块的所有权限，适合运营、标注等角色，可查看和配置方舟内标注资源，配置模型接入和模型仓库资源。​  
​| ArkStandardGlobalAccess​| 火山方舟（Ark）标准全局权限，拥有读接口权限、火山方舟自动创建的TOS桶读权限、公开基础模型的读权限和创建各类关联资源的权限，适合只有项目权限的用户。​  
​| ArkExperienceAccess​| 火山方舟（Ark）体验权限用户，拥有体验中心的所有权限，适合运营、测试等角色，可查看和体验方舟在模型广场的模型。​  
  
​

前提条件​

开始前，请确保完成以下操作：​

  * 已创建成员，并开启允许访问火山引擎。详情请参考​步骤一：创建成员。​

  * 已获取与扣成员关联的 IAM 用户的用户名。​

  * 你可以在扣子控制台的成员列表区域，将鼠标悬停在成员对应的允许上，查看与其关联的 IAM 用户的用户名。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272424%27%20height=%27454.1384248210024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQyNCIgaGVpZ2h0PSI0NTQuMTM4NDI0ODIxMDAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

操作步骤​

你可以直接为 IAM 用户授权，或将 IAM 用户添加进用户组，用户组中的成员将继承用户组的权限。​

直接为成员授权​

你可以直接为单个扣成员授权。操作步骤如下：​

1.

主账号登录[访问控制控制台](<https://console.volcengine.com/iam/identitymanage/user>)。​

2.

在左侧导航栏，选择用户管理 > 用户。​

3.

在用户页面，找到目标 IAM 用户，单击其用户名。​

4.

在用户详情页面的权限页签下，单击添加权限。​

5.

在添加授权页面，搜素并选择目标权限。​

  * 扣子和火山方舟的常用权限可参考​权限策略。​

6.

单击确定。​

完成授权后，权限立即生效，你可以使用授权的成员登录火山引擎控制台，进行相关的操作。​

通过加入用户组为成员授权​

你可以创建用户组并向用户组授权，再将成员添加进用户组，用户组中的成员将继承用户组的权限。​

操作步骤如下：​

1.

登录[访问控制控制台](<https://console.volcengine.com/iam/identitymanage/user>)。​

2.

创建用户组并授权。​

a.

在左侧导航栏，选择用户管理 > 用户组。​

b.

在用户组页面，单击新建用户组。​

c.

输入用户组名、显示名和备注，然后单击提交。​

d.

单击立即授权，根据业务需求授权。​

  * 扣子和火山方舟的常用权限可参考​权限策略。​

e.

单击确定。​

3.

将成员添加进用户组。​

a.

在左侧导航栏，选择用户管理 > 用户。​

b.

在用户页面，找到目标 IAM 用户，单击其用户名。​

  * 你可以在扣子控制台的成员管理页面查看 IAM 用户的用户名为 { 成员的用户名 } + @CloudIdentitySaas 组成。例如，成员的用户名为 test_name，则关联的 IAM 用户的用户名为test_name@CloudIdentitySaas。​

c.

在用户详情页面，单击用户组页签。​

d.

单击添加至组，选择目标用户组。​

e.

单击确定。​

授权完成后，权限立即生效。你可以使用授权的成员登录火山引擎控制台，进行相关的操作。​

授权示例：为成员添加火山方舟只读权限​

本示例介绍如何为成员添加火山方舟只读权限ArkReadOnlyAccess，添加完成后，扣子成员即可在火山方舟控制台查看全部资源。​

操作步骤如下：​

1.

登录[访问控制控制台](<https://console.volcengine.com/iam/identitymanage/user>)。​

2.

在左侧导航栏，选择用户管理 > 用户。​

3.

在用户页面，找到目标 IAM 用户，单击其用户名。​

4.

在用户详情页面，单击权限页签。​

5.

在全局权限下，单击添加权限。​

6.

搜索并勾选ArkReadOnlyAccess，然后单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27563%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYzIiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

授权完成后，成员即可查看火山方舟控制台的全部资源，例如查看方舟模型调用量统计。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27583%27%20height=%27281%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgzIiBoZWlnaHQ9IjI4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

上一篇

设置成员角色

下一篇

获取登录信息