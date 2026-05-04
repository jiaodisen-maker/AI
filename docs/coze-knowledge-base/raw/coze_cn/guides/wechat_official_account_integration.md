---
source_url: https://docs.coze.cn/guides/wechat_official_account_integration
title: '微信公众号 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:43Z
---

# 微信公众号 - 文档 - 扣子

微信公众号

扣子编程支持集成微信公众号能力，以实现公众号文章内容的生成与文章数据查询。​

支持的能力​

  * 发布草稿到微信公众号​

  * 发布微信公众号文章​

  * 查询文章数据​

配置方式​

步骤一：获取微信公众号配置信息​

在使用微信公众号集成服务前，你需要先在微信开发者平台的公众号管理页面，获取对应的开发者 ID（AppID）和密钥（AppSecret），具体操作，请参考[获取 AppID 和 AppSecret](<https://developers.weixin.qq.com/doc/subscription/guide/dev/api/#获取-AppID-和-AppSecret>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27583%27%20height=%27295%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7f10c780171a4d2eb0168ec7ecdcdbed~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：配置 IP 白名单​

为确保接口调用安全，微信公众号仅允许白名单内的 IP 地址调用公众号的服务端接口。即你需要在微信开发者平台的公众号管理页面，配置 API IP 白名单为 115.190.189.7。具体操作，请参考[公众号与服务号 IP 白名单](<https://developers.weixin.qq.com/doc/oplatform/developers/basic_func/ip_whitelist.html#_2、公众号与服务号-IP-白名单>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27584%27%20height=%27374%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg0IiBoZWlnaHQ9IjM3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：为工作空间启用外部集成（企业旗舰版管控操作）​

企业旗舰版由组织管理员统一管控工作空间内外部集成的可用性。即组织管理员可以为工作空间设置空间内可用的外部集成。默认情况下，企业旗舰版所有工作空间内均不可使用外部集成。具体操作，请参考​步骤一：为工作空间启用外部集成。​

说明

企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

​

步骤四：配置微信公众号集成​

在集成管理页面，单击微信公众号对应的配置，然后输入你已获取的开发者 ID（AppID）和密钥（AppSecret）。​

说明

配置外部集成后，系统会根据项目类型自动添加对应的官方技能到技能列表中。请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27536%27%20height=%27355%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM2IiBoZWlnaHQ9IjM1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271053%27%20height=%27821.4893617021277%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA1MyIgaGVpZ2h0PSI4MjEuNDg5MzYxNzAyMTI3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤五：为项目接入微信公众号集成​

完成微信公众号集成配置后，你可以在开发 AI 编程项目时，输入添加微信公众号集成服务的相关需求，让扣子 AI 自动识别并加载微信公众号技能来添加集成服务。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27476%27%20height=%27305%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc2IiBoZWlnaHQ9IjMwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

Email

下一篇

企业微信机器人