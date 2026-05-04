---
source_url: https://docs.coze.cn/guides/deployment_history
title: '回滚部署版本 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:27Z
---

# 回滚部署版本 - 文档 - 扣子

回滚部署版本

扣子编程会自动保存你的每一次部署记录，方便你随时查看历史版本或在必要时回滚到某个稳定版本。当你执行回滚操作时，扣子编程会基于所选的历史版本创建一个新的部署记录。​

功能简介​

扣子编程支持查看所有部署历史，并支持一键回滚历史版本，其典型应用场景包括：​

  * 快速恢复服务：当线上版本出现故障时，可以迅速回滚到某一个已验证的稳定版本，最大限度地缩短服务中断时间。​

  * 问题追溯与审计：通过完整的部署历史，可以清晰地追溯每一次变更的负责人、时间和具体内容，为故障排查提供可靠依据。​

使用限制​

支持回滚的项目状态、项目可回滚的历史部署版本数量等均存在限制，详情请参见​配额与限制。​

查看部署历史​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的项目，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27212.96296296296296%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cf3f91f97b1e4d9094d25b7627b5ce50~tplv-goo7wpa0wc-quality:q75.image)​

​

​

2.

在 AI 编程开发界面，在右侧单击➕打开新的标签页，在弹出的标签页中选择部署。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27345.0867052023121%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d1704b1c963e4bad9f4b26775415c6da~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

在部署页面的总览页签中，你可以查看曾经部署过的版本，和正在部署的版本。​

回滚部署版本​

当你需要将 AI 编程项目恢复到某个历史状态时，你可以执行回滚操作。回滚后，扣子编程会自动生成一个新的部署版本，原始的历史记录不会被修改或删除。​

说明

回滚时，环境变量也会回退到目标历史版本对应的环境变量设置，以确保项目在回滚后的运行环境与该历史版本一致。你可以在回滚确认对话框中查看变更的环境变量。​

​

1.

在[扣子编程](<https://code.coze.cn/home>)左侧导航栏选择项目管理，筛选带有 New 标签的项目，单击目标项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27212.96296296296296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIxMi45NjI5NjI5NjI5NjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在 AI 编程开发界面，在右侧单击➕打开新的标签页，在弹出的标签页中选择部署。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27345.0867052023121%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM0NS4wODY3MDUyMDIzMTIxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

在部署页面的总览页签中，找到你希望恢复的历史部署记录。​

4.

单击目标部署记录右侧的更多按钮，选择回滚。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27219.90740740740742%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIxOS45MDc0MDc0MDc0MDc0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在回滚确认对话框中核对环境变量差异。单击回滚，可以重新部署该版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27270.2546296296297%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI3MC4yNTQ2Mjk2Mjk2Mjk3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

上一篇

部署工作流

下一篇

查看日志和 Trace