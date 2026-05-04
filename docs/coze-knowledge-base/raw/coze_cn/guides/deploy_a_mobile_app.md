---
source_url: https://docs.coze.cn/guides/deploy_a_mobile_app
title: '部署移动应用 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:17Z
---

# 部署移动应用 - 文档 - 扣子

部署移动应用

本文介绍如何将通过扣子编程开发的移动应用 App，快速打包部署为可安装的 Android APK 包，以便将你的创意和原型，转化为能在手机端运行、服务于真实用户的产品。生成的 APK 包需由你自行上架至应用商店进行分发。​

使用限制​

仅应用的所有者有权限执行部署操作，且可创建的项目数量、部署次数等均存在配额限制。详情请参见​配额与限制。​

前提条件​

已通过扣子编程开发移动应用，且测试通过。具体可参考​开发移动应用。​

部署移动应用​

1.

在扣子编程左侧导航栏选择项目管理，单击某个移动应用。​

2.

在 AI 编程开发界面的右上角单击部署。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27604%27%20height=%27154%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/950e55ad6f774d7cb586339448da3fca~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

选择部署版本。​

4.

配置数据库同步。​

  * 生产环境和开发环境的数据隔离。首次部署时，你可以设置是否将开发环境的数据同步至生产环境。后续部署时，扣子编程仅同步开发环境的表结构变更，不同步具体数据。​

  * 关闭：仅同步开发环境中的数据表结构，不同步数据。​

  * 开启：将开发环境中的数据表结构和数据完全同步到生产环境。​

5.

配置生产环境变量。​

  * 在生产环境中为项目配置特定的环境变量，例如 API Key、数据库连接字符串、飞书文档地址等敏感信息，以免将这些信息硬编码在代码中导致安全风险。​

  * 展开环境变量的下拉列表，你可以新建环境变量、查看本次部署新增和变更的环境变量。关于环境变量的具体说明请参考​管理环境变量。​

  * 说明

部署时新建的变量，仅在生产环境生效，不会被添加至开发环境。​

​

6.

如需查看服务器资源、构建指令、端口等高级部署配置，你可以展开更多配置，查看配置详情。​

7.

单击开始部署。​

  * 扣子编程将自动进行部署相关操作。你可以在部署页面查看部署的进展和部署日志。部署过程可能需要几分钟，请耐心等待。部署过程中，你可以随时取消部署。​

获取和分发移动应用​

部署成功后，你可以下载安装包、上架应用市场。​

1.

下载 APK 包​

  * 部署成功后，可直接在 Android 设备上扫码安装应用 APK 包，以完成测试或使用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27597%27%20height=%27195%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTk3IiBoZWlnaHQ9IjE5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

上架应用市场。​

  * 如果你希望将应用公开发布，可将其提交至各大安卓应用市场。应用上架需遵循各应用市场的官方指南，你需要自行准备开发者账号、应用素材，并遵守其审核规则。​

分享移动应用​

在移动应用开发页面右上角单击分享按钮，切换到分享产物页签，即可通过二维码或下载链接，将已部署应用的 APK 安装包分享给他人。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27643%27%20height=%27180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQzIiBoZWlnaHQ9IjE4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

上一篇

部署网页应用

下一篇

部署小程序