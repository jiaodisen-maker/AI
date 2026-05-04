---
source_url: https://docs.coze.cn/guides/coze_pro_upgrade_to_premium
title: '迁移至企业版 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:46:15Z
---

# 迁移至企业版 - 文档 - 扣子

迁移至企业版

本文档以升级到企业旗舰版套餐为例，演示用户购买套餐、创建企业组织、迁移资源的操作流程。​

场景说明​

为了享受企业旗舰版的各种高级权益，例如更大的用户规模、更丰富的安全特性，你可以升级到企业旗舰版，实现中大型 AI 应用的多人协作。购买企业旗舰版之后，操作者默认为企业的超级管理员，需要创建企业、组织，并将之前已搭建、开发的智能体、应用或工作流等资源迁移到企业中。​

例如用户 A 为主账号，其名下已创建一批火山子用户。用户 A 根据企业部门创建了多个工作空间，并分别邀请对应部门的子用户加入。这些子用户在各个工作空间中也创建了一批智能体、扣子应用或工作流等资源，并发布到 API 等各个渠道以供更多用户使用。​

用户 A 可以购买企业旗舰版，创建一个企业组织，将工作空间批量迁移至企业内，并邀请子用户分别加入对应的工作空间以便多人协作开发。工作空间中的智能体等资源也会一起迁移到企业内。​

说明

  * 关于企业的概念，可参考​了解企业组织。​

  * 从原团队版升级至企业旗舰版时，无需迁移资源，也无需重新创建企业，升级套餐后直接可享受企业旗舰版权益。​

​

注意事项​

升级到企业旗舰版之前，需要注意以下事项：​

​

类别​| 说明​  
---|---  
子用户​| 

  * 目前所有的专业版用户无法继续创建子用户，需要购买订阅套餐以继续创建子用户、享受更大的团队规模。​

  * 升级企业旗舰版之后，所有已创建子用户都会变为个人免费版，需要重新添加到企业内，才能享受高级权益。​

  
资源迁移​| 

  * 原有工作空间资源向企业中迁移时，工作空间内其他人创建的资源也会一并迁移。如果资源的创建者未加入企业，其资源会自动转交给操作者。​

  * 开启了多人协作的智能体、应用、工作流中，用户未提交的个人草稿版本不会同步迁移；如果某个资源草稿版本的作者未同步迁移，此草稿版本会被删除，仅迁移资源的最新发布版本。​

  
访问密钥​| 

  * 如果待迁移的工作空间中已创建了个人访问令牌、OAuth 应用等 OpenAPI 资源，迁移空间时你需要选择 API 资源的迁移方式，即一键授权或手动迁移。关于迁移方式的对比，可查看​选择迁移方式。​

  * 升级企业旗舰版之后，如果选择平滑迁移方案，在企业下创建的 JWT 访问密钥无法访问迁移前个人账号下的历史会话。在 Chat SDK 或其他使用已保存的 conversation_id 等场景下，仍然需要需要使用历史会话资源，请勿切换访问密钥，建议继续使用个人访问密钥。​

  
自定义渠道​| 如果空间中已添加自定义渠道，迁移工作空间不会影响已发布的智能体的线上运行。如需迁移自定义渠道，建议联系扣子技术团队获取支持和帮助。​  
  
​

准备工作​

  * 登录火山主账号对应的扣子账号。购买企业旗舰版等操作需要支付订阅套餐的费用，且操作者默认为企业的管理员，建议由火山主账号完成本文档中的升级操作。​

  * 了解企业旗舰版的高级权益与计费规则。你可以在订阅套餐页面查看高级权益，通过文档​计费概述了解计费规则。​

  * 获取工作空间的所有者权限。如果希望将某些工作空间迁移到企业中，享受企业旗舰版的多人协作等高级权益，操作者需要获得工作空间的所有者权限，操作步骤可参考​设置空间成员角色。​

步骤一：购买企业旗舰版​

登录扣子编程后，参考以下步骤购买企业版订阅套餐。​

1.

在[扣子编程](<https://code.coze.cn/home>)的左下角，单击积分。​

2.

在订阅管理页面中，找到企业旗舰版，单击升级。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27349%27%20height=%27231%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ5IiBoZWlnaHQ9IjIzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

根据页面提示完成购买与支付。​

  * 说明

如果你未完成火山引擎实名认证，则需要根据页面提示先完成企业或个人实名认证。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27306%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2IiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：创建企业​

成功购买企业旗舰版之后，系统会引导你创建企业，并为企业设置企业名称和头像。​

1.

根据页面提示，输入企业名称、设置企业头像。​

2.

单击创建企业。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27559%27%20height=%27293%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU5IiBoZWlnaHQ9IjI5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：创建组织​

企业包含默认组织，用户加入时自动加入该默认组织。扣子企业旗舰版支持创建多个组织，企业超管和管理员可按部门或项目创建组织，实现多业务部门的独立运作与统一管理。​

1.

企业超级管理员或管理员登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左下角单击个人头像，选择企业版账号 > 团队与企业管理，进入企业管理页面。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27338%27%20height=%27327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM4IiBoZWlnaHQ9IjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在左侧导航栏选择企业组织管理，单击右上角的+创建组织。输入组织名称和描述，单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27602%27%20height=%27215%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAyIiBoZWlnaHQ9IjIxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：迁移工作空间​

创建企业之后，你可以将之前已创建的工作空间迁移到新的企业中，这些工作空间中可享受企业旗舰版的全部高级权益，例如企业旗舰版安全特性、无限制的空间人数等，工作空间中的成员也可以继续编排原有的智能体、使用已有的知识库等资源。​

迁移工作空间时，自动迁移空间中的所有资源和指定的空间成员。​

说明

迁移影响如下：​

  * 工作空间中已创建的智能体、应用、工作流、插件、知识库、数据库、卡片和提示词会同步迁移到企业中。​

  * 指定的空间成员会同步迁移到企业中。​

  * 空间 ID、智能体 ID 保持不变。​

  * 智能体和应用的发布状态保持不变。如果迁移前已处于发布状态，迁移完成后仍保持发布状态，无需重新发布。​

​

1 选择工作空间​

1.

组织超级管理员或管理员登录[扣子编程](<https://code.coze.cn/home>)。在左下角单击个人头像，单击企业旗舰版账号，单击对应组织右侧的管理图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27451%27%20height=%27340%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUxIiBoZWlnaHQ9IjM0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在企业组织管理页面的顶部选择空间管理页签，在右上角单击迁移空间。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27510%27%20height=%2799%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEwIiBoZWlnaHQ9Ijk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

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

扣子编程支持以下两种迁移方式，其对比说明如下：​

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

  * 不会移动 API，只是变更了 API 的授权范围，增加企业的访问权限。你仍需在个人账号 > API 管理 中查看API 授权。​

  * 仅支持 PAT 和 AuthAPP，不支持 OBO。​

| 将所有授权类型的 API（OBO、PAT、AuthApp）全部剪切迁移，后续可在企业账号 > API 管理 处查看和修改。​​  
适用场景​| 适用于无需迁移 OBO 授权的场景，且开发者希望快速完成迁移、仍可访问原个人账号下已创建的会话。​| 需要手动修改代码中的授权逻辑，适用于具备一定开发背景的专业开发者。但该方式会将 API 授权迁移至企业账号下，便于后续的资源管理和维护。​  
  
​

一键授权​

根据页面提示授权，允许企业访问个人账号 API。Open API 不会迁移，仅增加企业的访问权限。​

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

c.

更新 API 授权，将空间中的所有 API 授权手动迁移到企业。​

  * 详细操作步骤可参考文档​升级企业版后更新 API 授权。​

d.

返回迁移空间页面，根据页面提示选择手动迁移。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27323%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIzIiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

e.

选择待迁移的 API 授权，确认已知悉相关风险。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27347%27%20height=%27158%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ3IiBoZWlnaHQ9IjE1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4 迁移用户​

在选择用户页面，从工作空间中已有的成员中选择要同步迁移的用户，并单击确认。​

迁移成功后，被选中的成员将自动加入组织中对应的工作空间，并同步成为组织成员。支持将内部用户（子用户）和外部用户（访客）加入组织。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27410%27%20height=%27324%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEwIiBoZWlnaHQ9IjMyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

说明

如果企业超级管理员和管理员设置了禁止访客加入企业，迁移空间时无法选择外部用户（访客）。迁移空间成功后，外部用户会自动退出此工作空间，其拥有的资源也会自动转让给空间所有者。​

​

步骤四：添加成员​

如果需要创建新的子用户，并使子用户同样享受企业旗舰版权益，你可以在火山扣子控制台创建新的子用户，然后将其加入企业，共享企业资源。​

说明

如果升级企业旗舰版之前已创建子用户，且迁移工作空间时没有同步迁移这些用户，则需要手动将其加入企业中，子用户才能享受企业旗舰版权益，否则子用户默认为个人免费版。​

​

1 创建成员​

扣子编程支持在火山引擎扣子控制台中通过导入已有 IAM 用户、自定义创建和批量创建三种方式创建成员。本文档以自定义创建为例。​

1.

企业超级管理员进入[企业成员管理](<https://admin.coze.cn/>)页面。​

2.

在左侧导航栏选择企业成员管理，在成员列表页面右上角单击+成员。​

3.

在添加新成员对话框中，单击创建内部成员账号。​

  * 单击后，页面将跳转至火山引擎扣子控制台。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27494%27%20height=%27307%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk0IiBoZWlnaHQ9IjMwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在火山引擎扣子控制台的成员管理页面的01创建成员页签下，单击立即创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27232.77909738717344%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIzMi43NzkwOTczODcxNzM0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在创建成员页面，根据页面提示完成创建。​

  * 创建成员时，可以勾选短信或邮件通知方式，系统将在成员创建成功后自动通过短信或邮件将成员信息发送给对应用户。创建成功后，系统会自动激活成员。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27584%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg0IiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在成员列表中查看该成员是否已自动加入企业。​

  * 创建成员成功后，系统会自动尝试将成员加入企业，当成员状态变更为已加入企业，表示加入成功。​

  * 如果出现特殊情况导致成员未自动加入企业时，可以手动将成员加入到企业中，具体请参考​步骤三：手动加入企业（可选）。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27260.4166666666667%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjI2MC40MTY2NjY2NjY2NjY3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 说明

成员状态说明如下：​

    * 已激活：该成员未加入企业，不计入企业的成员费用。​

    * 已加入企业：该成员已成功加入企业，开始计算成员数量。更多成员计费信息，请参考​席位费用（已下架）。​

​

2 手动加入企业（可选）​

创建成员成功后，系统会自动将成员加入企业，如果出现特殊情况导致成员未自动加入企业时，企业超级管理员或管理员可以参考如下步骤登录扣子编程，手动将成员加入到企业中。​

1.

企业超级管理员进入[企业成员管理](<https://admin.coze.cn/>)页面。​

2.

在左侧导航栏选择企业成员管理，在成员列表页面单击右上角的+成员。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA0IiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选中上述已创建的成员，设置其身份，然后单击确认。​

  * 说明

如果子用户较多，可以搜索用户名、用户昵称或火山成员名来快速定位用户。​

用户可以在账号设置页面查看自己的用户信息。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27475%27%20height=%27219%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc1IiBoZWlnaHQ9IjIxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

3 加入组织​

组织超级管理员和管理员可以邀请员工（子用户）和外部成员（访客）加入对应的组织。成员加入对应组织后，其在默认组织中不会被删除。​

1.

企业超级管理员或管理员登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左下角单击个人头像，选择企业版账号 > 团队与企业管理，进入企业管理页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27336%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM2IiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

1.

在组织管理页面的顶部选择组织成员管理。​

  * 单个添加

分享链接邀请加入

1.

在成员列表页面，单击+成员。​

2.

在搜索框中输入用户名、用户昵称或火山成员名搜索对应的企业员工或访客，选中成员，设置其身份，然后单击确认。​

​

4 加入工作空间​

工作空间所有者和管理员登录扣子编程，邀请组织成员加入到工作空间中。​

3.

在页面左上角展开空间下拉列表，单击目标工作空间右侧的管理图标。​

4.

在顶部单击成员管理页签，在右上角单击 \+ 添加成员。在搜索框中输入用户名搜索对应的企业员工或访客，选中成员，设置其身份，然后单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27640%27%20height=%2795%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQwIiBoZWlnaHQ9Ijk1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

常见问题​

  * ​升级企业版之后，为什么仍然是个人版权益？​

  * ​升级企业版之后，为什么子用户仍然是免费版？​

​

上一篇

从零搭建企业组织

下一篇

创建企业