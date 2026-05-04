---
source_url: https://docs.coze.cn/guides/webview
title: '配置应用跳转外部链接的域名 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:14Z
---

# 配置应用跳转外部链接的域名 - 文档 - 扣子

配置应用跳转外部链接的域名

如果低代码应用中配置了页面跳转到外部链接的事件，并且该应用已发布到抖音小程序，那么你需要在抖音开放平台完成外部链接域名的配置，以确保链接可以正常跳转。​

说明

抖音小程序渠道支持开发者配置外部链接域名，实现低代码应用内的外部链接正常跳转。​

​

场景说明​

抖音小程序默认屏蔽外部链接的直接访问，如果你在低代码应用中配置了页面跳转外部链接的事件，并且将低代码应用发布到抖音小程序，那么你需要在抖音开放平台配置外部链接的域名。​

例如为按钮组件配置了跳转到外部链接的事件，那么在发布低代码应用到抖音小程序后，你需要在抖音开放平台添加该外部链接的域名。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27566%27%20height=%27279%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/162c0fcfa44f40d891abadef03e6d3be~tplv-goo7wpa0wc-quality:q75.image)​

​

前提条件​

已发布低代码应用到抖音小程序。具体操作，请参考​发布到抖音小程序。​

操作步骤​

1.

使用抖音开放平台账号登录[抖音开放平台](<https://developer.open-douyin.com/console?type=1>)。 ​

2.

在控制台 > 小程序中，找到需要绑定低代码应用的小程序。​

3.

在左侧导航栏中，选择开发 > 开发配置。​

4.

在域名管理页签下的 web-view 域名区域，完成如下操作。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27536%27%20height=%27174%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM2IiBoZWlnaHQ9IjE3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

a.

单击下载检验文件，下载检验文件。​

b.

配置校验文件。​

  * 假设下载的文件名为 pNWfyB8oLl.txt，外部链接的域名为 example.com，则你需要在域名 example.com 的前端服务器（如 Ngnix）中上传检验文件。然后通过访问校验文件，验证是否可以正常访问，访问地址为 https://example.com/pNWfyB8oLl.txt，访问内容为校验文件内容。​

c.

单击添加，添加外部链接的域名，例如 example.com。​

  * 添加完成后，你在小程序中单击对应的外部链接，链接能够正常跳转。​

上一篇

快捷键

下一篇

调试低代码应用