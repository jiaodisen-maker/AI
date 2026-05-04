---
source_url: https://docs.coze.cn/guides/manage_channels
title: '管理发布渠道 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:45:48Z
---

# 管理发布渠道 - 文档 - 扣子

管理发布渠道

本文介绍如何对工作空间进行发布渠道管理，包括授权发布渠道、添加公告渠道和自定义渠道，以及移除不再需要的渠道。​

发布渠道概述​

扣子编程提供了多种官方默认发布渠道，例如扣子商店、豆包、API 、SDK 等。你可以手动添加公共渠道和企业自定义渠道，按需拓展 AI 项目的分发渠道。​

扣子企业版（企业标准版、企业旗舰版）中，组织超级管理员或管理员需要为工作空间授权发布渠道，工作空间中的开发者才能将 AI 项目发布到已授权的渠道中。对发布渠道的强管控能避免项目被发布到未经授权的发布渠道，确保项目的发布渠道符合企业的规划和策略。​

扣子订阅套餐中相关角色的操作权限说明如下：​

​

功能​| 个人版​| 企业版 ​| ​| ​| ​| ​| ​  
---|---|---|---|---|---|---|---  
​| ​| 企业超级管理员​| 企业管理员​|  企业成员​| 组织超级管理员​| 组织管理员​|  组织成员​  
给空间开通发布渠道​| ❌​| ❌​| ❌​| ❌​| ✅​| ✅​| ❌​  
发布渠道限制​| ✅​| ✅​| ✅​| ❌​| ❌​| ❌​| ❌​  
添加企业自定义渠道​| ✅​| ✅​| ✅​| ❌​| ✅​| ✅​| ❌​  
移除渠道​| ✅​| ✅​| ✅​| ❌​| ✅​| ✅​| ❌​  
  
​

给工作空间开通发布渠道​

扣子个人版请忽略该操作。扣子企业版中，组织超级管理员或管理员需要给工作空间开通相应的发布渠道，工作空间中的成员才能将智能体或应用发布至对应的发布渠道。​

说明

角色限制：组织超级管理员或管理员。​

​

1.

在[扣子编程](<https://code.coze.cn/home>)左下角单击个人头像，选择企业，然后单击对应组织的设置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27313%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEzIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

2.

在企业组织管理页面的顶部选择发布渠道管理页签。​

3.

在渠道列表中选择目标渠道，在页面底部单击配置，或鼠标悬停在目标渠道的卡片上，单击空间配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27387.15277777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM4Ny4xNTI3Nzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在弹出的对话框中选择目标工作空间，单击开启渠道。​

  * 开通渠道后，企业成员在智能体或应用的发布页面中，发布平台列表中将显示已开通的发布渠道。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27519%27%20height=%27285%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE5IiBoZWlnaHQ9IjI4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

添加公共渠道和自定义渠道​

公共渠道通常包括应用商店、硬件厂商、开发者平台等公开渠道。渠道商完成官方认证与入驻流程后，可申请作为公共渠道向所有扣子用户开放。所有扣子用户均可添加这些公共渠道，并将智能体发布到公共渠道。​

说明

  * 若有公共渠道合作意向，可填写[公共渠道入驻申请](<https://bytedance.sg.larkoffice.com/share/base/form/shrlgcE3ieqZw9kjpWoF5bcllih>)。​

  * 添加公共渠道之前，建议在添加页面单击查看详情，阅读公共渠道的发布指南，了解发布相关的准备工作。​

​

个人版​

说明

角色限制：工作空间所有者、管理员。​

​

1.

在页面左上角展开空间下拉列表，单击目标工作空间右侧的管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27150%27%20height=%27264.9484536082474%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwIiBoZWlnaHQ9IjI2NC45NDg0NTM2MDgyNDc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

在发布管理页面选择发布渠道管理页签，在目标渠道卡片中开启开关。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27396.9194312796209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM5Ni45MTk0MzEyNzk2MjA5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

企业版​

说明

角色限制：企业的超级管理员和管理员。​

​

1.

在左下角单击个人头像，选择企业版账号 > 企业管理。​

  * 你也可以直接访问[扣子编程企业管理页面](<https://docs.coze.cn/guides/admin.coze.cn>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27213.45291479820628%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIxMy40NTI5MTQ3OTgyMDYyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在左侧导航栏选择发布渠道限制，在公共渠道区域开启目标渠道。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27753%27%20height=%27553.1516587677726%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUzIiBoZWlnaHQ9IjU1My4xNTE2NTg3Njc3NzI2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

在左侧导航栏选择企业组织管理，将鼠标悬停至目标组织的卡片，单击当前组织设置。​

4.

在顶部选择发布渠道管理页签，鼠标悬停在目标渠道卡片上，单击空间配置，单击目标工作空间右侧的开关开启渠道。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27387.15277777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM4Ny4xNTI3Nzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 只有给对应工作空间授权目标发布渠道，工作空间成员才能将智能体发布至该渠道。​

​

说明

如需创建自定义渠道，请参见​配置渠道入驻（账号隔离）和​配置渠道入驻（账号互通）。​

​

移除公共渠道和自定义渠道​

你可以移除不再需要的公共渠道和企业自定义渠道，但不支持移除官方默认渠道。​

个人版​

说明

角色限制：工作空间所有者、管理员。​

​

1.

在页面左上角展开空间下拉列表，单击目标工作空间右侧的管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27150%27%20height=%27264.9484536082474%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwIiBoZWlnaHQ9IjI2NC45NDg0NTM2MDgyNDc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

在发布管理页面选择发布渠道管理页签，在目标渠道卡片中关闭开关。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27396.9194312796209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM5Ni45MTk0MzEyNzk2MjA5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

企业版​

说明

角色限制：企业的超级管理员和管理员。​

​

1.

在左下角单击个人头像，选择企业版账号 > 企业管理。​

  * 你也可以直接访问[扣子编程企业管理页面](<https://docs.coze.cn/guides/admin.coze.cn>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27213.45291479820628%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIxMy40NTI5MTQ3OTgyMDYyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在左侧导航栏选择发布渠道限制，在目标渠道卡片中关闭开关。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27151.65876777251182%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE1MS42NTg3Njc3NzI1MTE4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

  * ​

​

​

​

​

​

上一篇

管理发布产物

下一篇

发布渠道能力差异