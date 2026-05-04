---
source_url: https://docs.coze.cn/guides/use_code
title: '使用代码注册插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:42Z
---

# 使用代码注册插件 - 文档 - 扣子

使用代码注册插件

扣子编程提供了代码解析器，支持解析 API 配置文件来创建插件。创建插件后，必须发布插件才可以被低代码智能体使用。​

说明

  * 个人工作空间中的插件，仅能被个人调用；企业工作空间中插件，能被任意企业成员调用。​

  * 插件发布了新版本后，使用了这个插件的低代码智能体会自动使用发布的最新版本。​

​

操作步骤​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，选择 +资源 > 插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27170%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/013e73be30ef4768a3432e8017d9c325~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

在页面右上角单击代码图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27458%27%20height=%27209%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/845b3b548450462aa02fef225fc41c38~tplv-goo7wpa0wc-quality:q75.image)​

​

5.

完成以下配置，然后单击确认。​

a.

在左侧面板中以 JSON 格式填入插件的配置信息。​

b.

在右侧面板中以 YAML 格式填入 API 的配置信息。​

6.

在插件页面，进入插件详情页查看已创建的 API 工具。单击已创建的 API 进行调试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27452%27%20height=%27118%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUyIiBoZWlnaHQ9IjExOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

检查 API 配置，在调试与校验页面，单击编辑工具，输入请求参数，然后单击运行查看 API 是否可以成功调用。​

8.

如果 API 调用成功，单击完成。如果 API 调用失败，根据错误信息修改 API 配置，直至 API 调试成功。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27469%27%20height=%27248%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY5IiBoZWlnaHQ9IjI0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

9.

在插件详情页的右上角，单击发布。​

上架到商店​

你可以将插件上架到扣子插件商店或企业插件商店。不能同时上架扣子插件商店和企业插件商店，仅支持选择其中一个渠道。​

  * 上架扣子插件商店​

  * 对于通用功能、不涉及敏感数据且具有广泛适用性的公开插件，你可以将其上架到扣子商店，以便更多扣子用户发现、使用。详情请参考​将插件上架到插件市场。​

  * 上架企业插件商店​

  * 仅企业旗舰版支持。​

  * 对于企业自主开发的涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的插件，你可以将其上架到企业插件商店，供企业成员使用。详情请参考​管理企业插件。​

上一篇

使用 IDE 创建插件

下一篇

创建私网模式插件