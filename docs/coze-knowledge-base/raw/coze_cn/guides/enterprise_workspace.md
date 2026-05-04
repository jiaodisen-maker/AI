---
source_url: https://docs.coze.cn/guides/enterprise_workspace
title: '迁移空间 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:46:36Z
---

# 迁移空间 - 文档 - 扣子

迁移空间

组织超管或管理员可以将本人拥有的工作空间迁移到企业的组织中，以便继续开发企业级应用。​

功能简介​

购买企业版并创建企业之后，组织超级管理员或管理员可以将扣子个人版或原扣子专业版工作空间中的资源、智能体和应用迁移到企业的工作空间中。迁移空间功能可以高效地完成资源迁移，确保升级过程平滑顺畅。迁移后空间 ID、智能体 ID 保持不变，不影响已发布的智能体或应用正常运行，也无需重新发布。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27348%27%20height=%27448%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7a3b5aa43a58413b8fed23056fca59fe~tplv-goo7wpa0wc-quality:q75.image)​

​

迁移规则​

​

分类​| 说明​  
---|---  
迁移影响​| 

  * 此操作为一次性、不可逆的迁移操作，迁移完成后，该空间及其中的所有资源均为企业的专属资源，无法复制或迁移到企业外的空间中。建议谨慎操作。​

  * 由于智能体等资源属于空间，API 方式创建的会话属于扣子用户，迁移空间之后，智能体无权限访问原个人账号下的会话，建议开发者创建新会话。创建方式可参考​创建会话。​

  * 如需迁移自定义渠道，建议联系扣子技术支持获取支持和帮助。​

  * 迁移后，智能体和应用的 ID 均不变。​

  
迁移范围​| 

  * 工作空间中已创建的智能体、应用、工作流、插件、知识库、数据库、卡片和提示词会同步迁移到企业中。如果某个资源的所有者未同步迁移，该资源的草稿版本不会被迁移；多人协作场景下，协作者未提交的个人草稿版本也不会被迁移。​

  * 空间中指定的内部成员（子用户）和外部用户（访客）会同步迁移到企业中。​

  
权限要求​| 

  * 从扣子个人版迁移到企业版，请确保你是空间的所有者。​

  * 从扣子专业版迁移到企业版，请确保你的账号为火山引擎主账号且为空间所有者。​

  
  
​

创建企业之后，你可以将之前已创建的工作空间迁移到新的企业中，这些工作空间中可享受企业版套餐的全部高级权益，例如企业版安全特性、无限制的空间人数等，工作空间中的成员也可以继续编排原有的智能体、使用已有的知识库等资源。​

操作步骤​

1 选择工作空间​

1.

在[扣子编程](<https://code.coze.cn/home>)左下角单击个人头像，选择企业，然后单击对应组织的设置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27422%27%20height=%27318%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIyIiBoZWlnaHQ9IjMxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

​

2.

在企业组织管理的顶部选择空间管理页签，单击右上角的迁移空间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273467%27%20height=%27669.3514450867052%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ2NyIgaGVpZ2h0PSI2NjkuMzUxNDQ1MDg2NzA1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在选择工作空间页面，选择待迁移的工作空间，单击下一步。​

  * 仅支持迁移你作为空间所有者的工作空间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27480%27%20height=%27304%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgwIiBoZWlnaHQ9IjMwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

（可选）如果选择了个人空间，你需要在弹出的对话框中设置该个人空间迁移后的工作空间的名称，单击确认。​

2 确认非 API 资源​

确认待迁移的非 API 资源，单击下一步。​

非 API 资源的迁移范围包括空间中所有智能体、应用、插件、工作流、知识库、卡片、音色、提示词。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27490%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkwIiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3 迁移 API 资源​

确认空间中待迁移的 API 资源，选择迁移方式。​

  * 如果页面提示没有待迁移的 API 资源，可以直接单击下一步。​

  * 如果待迁移的工作空间中已创建了个人访问令牌、OAuth 应用等 OpenAPI 资源，你需要根据名下的 API 授权选择迁移方式，再根据页面提示完成迁移。​

选择迁移方式​

扣子支持以下两种迁移方式，其对比说明如下：​

​

迁移对比​| 一键授权​| 手动迁移​  
---|---|---  
是否有损​| 

  * 无需任何额外操作，线上服务无损迁移。​

  * 原个人账号下已创建的会话仍会保留。​

| 

  * 原本的 Access Token 失效，需要重新授权 API，以避免影响线上服务。​

  * 智能体无权限访问原个人账号下已创建的会话，建议开发者创建新会话。创建方式可参考​创建会话。​

  
迁移限制​| 

  * 不会移动 API，只是变更了 API 的授权范围，增加企业的访问权限。你仍需在个人账号 > API 管理中查看API 授权。​

  * 仅支持 PAT 和 AuthAPP，不支持 OBO。​

| 将所有授权类型的 API（OBO、PAT、AuthApp）全部剪切迁移，后续可在企业账号 > API 管理处查看和修改。​​  
适用场景​| 适用于无需迁移 OBO 授权的场景，且开发者希望快速完成迁移、仍可访问原个人账号下已创建的会话。​| 需要手动修改代码中的授权逻辑，适用于具备一定开发背景的专业开发者。但该方式会将 API 授权迁移至企业账号下，便于后续的资源管理和维护。​  
  
​

一键授权​

根据页面提示授权，允许企业访问个人版账号 API。Open API 不会迁移，仅增加企业的访问权限。​

  * 注意事项：一键授权迁移方式不会迁移 OBO 授权，如果存在 OBO 类型的 API，请先参考​OBO 授权场景 手动迁移 OBO 授权。​

  * 操作步骤：​

a.

根据页面提示选择一键授权即可。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27270.8994708994709%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI3MC44OTk0NzA4OTk0NzA5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

b.

后续确认待迁移的用户之后，系统会自动完成授权。​

手动迁移​

将空间中的所有 API 授权手动迁移到企业，选择该方式需逐一确认您已知悉风险。可通过提前授权方式降低对线上服务的影响。​

  * 注意事项：​

  * 注意

    * 若未执行更新 API 授权步骤、直接选择手动迁移，会导致原有的 API 授权失效，线上用户调用 API 时会因鉴权失败而无法正常访问。 ​

    * 如果智能体、应用或工作流已发布到生产环境且线上用户量较大，为保障平滑迁移，建议选择服务流量较少的时段（如深夜或凌晨）执行手动迁移。​

​

  * 操作步骤：​

a.

更新 API 授权，将空间中的所有 API 授权手动迁移到企业。​

  * 详细操作步骤可参考文档​升级企业版后更新 API 授权。​

b.

返回迁移空间页面，根据页面提示选择手动迁移。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27323%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIzIiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

选择待迁移的 API 授权，确认已知悉相关风险。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27228.00925925925927%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIyOC4wMDkyNTkyNTkyNTkyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4 迁移用户​

在选择用户页面，从工作空间中已有的成员中选择要同步迁移的用户，并单击确认。​

迁移成功后，被选中的成员将自动加入组织中对应的工作空间，并同步成为组织成员。支持将内部用户（子用户）和外部用户（访客）加入组织。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27371.52777777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM3MS41Mjc3Nzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

说明

如果企业超级管理员和管理员设置了禁止访客加入企业，迁移空间时无法选择外部用户（访客）。迁移空间成功后，外部用户会自动退出此工作空间，其拥有的资源也会自动转让给空间所有者。​

​

​

​

上一篇

添加组织成员

下一篇

删除组织