---
source_url: https://docs.coze.cn/coze_pro/bills_and_usage
title: '账单与用量 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:58:56Z
---

# 账单与用量 - 文档 - 扣子

账单与用量

本文介绍如何查看企业版账单、分账账单、账号积分用量、成员积分用量等信息，以及如何为成员设置积分额度等相关操作。​

查询账单​

查看总账单​

说明

当前企业版出账存在小时级的延时，例如 16:00～17:00 期间产生的费用，可能在 17:30:00 才出账并扣款。​

​

购买企业版后，你可以在火山引擎费用中心的[账单详情](<https://console.volcengine.com/finance/bill/detail>)页面，筛选产品为扣子、扣子-三方插件，查看扣子账单。其中，iSlide 、悠船、飞常准、天眼查等付费插件在账单中的产品名为扣子-三方插件。​

账单详情说明，请参考[账单管理](<https://www.volcengine.com/docs/6269/94010>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27571%27%20height=%27286%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7704ccd52bd54d95bf6b64c29286816d~tplv-goo7wpa0wc-quality:q75.image)​

​

查看分账账单​

说明

首次使用时，需要先开通分账账单功能。开通后，新生成的账单明细将生成对应的分账账单明细，开通前的存量账单明细无对应分账数据，数据最晚存在 2 天延迟。​

​

购买企业版后，你可以通过分账账单功能，以组织和工作空间维度查看各个工作空间内资源用量和对应的分拆费用。​

  * 支持按组织和工作空间维度分账的费用：任务编程费用、内置集成费用、模型费用、插件费用、语音通话费用、视频通话费用、声纹识别费用、语音合成费用和语音识别费用支持按照空间维度分账，但由于使用场景的多样性，不保证这些费用在所有场景下都能实现按组织和工作空间维度的分账。​

  * 不支持按组织和工作空间维度分账的费用：购买套餐、购买积分、购买增购项（增购声音复刻-音色数量等）、扣子费用、知识库空间费用、购买商店模板费用等仅支持按账号维度查看。​

支持按组织和工作空间维度分账的计费项，其拆分项标识为[org:****]-[ws:****] 或 [org:****]；不支持按组织和工作空间维度分账的计费项，其拆分项标识为 [acc:2***]。​

说明

如果要在分账账单中查看当前账号下的所有扣子账单，则需将分拆项名称或 ID 筛选项留空。​

​

  * [org:****]：组织名称或组织 ID​

  * [ws:****]：工作空间名称或工作空间 ID​

  * [acc:2***]：火山账户 ID​

你可以在火山引擎费用中心的[分账账单](<https://console.volcengine.com/finance/bill/split-bill>)页面，根据分拆项名称或 ID 筛选分账账单。筛选时，输入的值必须与分拆项的 ID 或名称完全匹配。常见的筛选格式为 [org:组织名称]-[ws:工作空间名称]、[org:组织ID]-[ws:工作空间ID]、[org:组织名称]、[org:组织ID]、[acc:2***]。​

分账账单中的各个字段说明，请参考[分账账单](<https://www.volcengine.com/docs/6269/177196>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272305%27%20height=%27442.42890995260666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMwNSIgaGVpZ2h0PSI0NDIuNDI4OTA5OTUyNjA2NjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看积分余额​

说明

企业版出账存在小时级的延时，因此抵扣积分也存在小时级的延时。例如 16:00～17:00 期间产生的费用，可能在 17:30:00 才抵扣。​

​

购买企业版后，企业超级管理员、管理员可以通过如下方式查看已购买的扣子积分列表及余量。 ​

1.

在[扣子编程](<https://code.coze.cn/home>)的左下角，单击积分卡片。​

2.

在订阅管理页面的积分区域，查看积分余额。​

  * 单击积分明细，可查看已购买的积分列表。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27493%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkzIiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

积分用量统计与明细​

查看计费项维度的用量明细​

购买企业版后，你可以在[火山引擎扣子控制台](<https://console.volcengine.com/coze-pro/overview>)的用量统计页面，查看各个计费项的用量。​

  * 编程项目：查看指定时段内，大语言模型、生图模型、语音模型、联网搜索等各个内置集成服务的使用量。 ​

  * 低代码项目：查看指定时段内，低代码项目相关的大模型用量、智能语音用量、实时音视频用量、插件用量、知识库用量、大模型 TPM 保障额度、成员用量、记忆库用量。​

  * 扣子罗盘：查看指定时段内，扣子罗盘智能调优功能消耗的积分。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272543%27%20height=%271078.9375722543352%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU0MyIgaGVpZ2h0PSIxMDc4LjkzNzU3MjI1NDMzNTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看账号维度的用量明细​

企业超级管理员、管理员可以在[扣子编程](<https://code.coze.cn/home>)的积分消耗页面中，切换到企业总用量视图，查看整个企业版账户维度的积分消耗情况。包括：​

  * 该账户的月度积分总消耗的预估值。​

  * 该账户下各扣子任务、扣子编程任务的积分消耗预估值及明细。​

  * 该账户下各扣子编程付费资源的积分消耗预估值及明细。​

详细说明，请参考​查看积分消耗明细。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27524%27%20height=%27301%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI0IiBoZWlnaHQ9IjMwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

你也跳转至火山引擎费用中心的[资源包管理](<https://console.volcengine.com/finance/resource-package>)页面，查看积分消耗情况。积分抵扣明细的各个字段说明，请参考[抵扣明细](<https://www.volcengine.com/docs/6269/165227>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27697%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjk3IiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看组织维度的用量明细​

在企业旗舰版中，企业超级管理员、管理员可以在[扣子编程](<https://code.coze.cn/home>)中，单击积分卡片，然后在限额管理>组织总限额页签下，查看各个组织消耗的积分总用量以及在对应组织内每日按功能模块分类的积分消耗明细。​

说明

用量列表中暂时仅展示有历史累计积分用量的组织。​

​

组织用量概览​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27707%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzA3IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

组织用量明细​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27985%27%20height=%27835.9692671394799%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTg1IiBoZWlnaHQ9IjgzNS45NjkyNjcxMzk0Nzk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

查看空间维度的用量明细​

在企业旗舰版中，企业超级管理员、管理员可以在[扣子编程](<https://code.coze.cn/home>)中，单击积分卡片，然后在限额管理>编程空间页签下，查看各个空间消耗的积分总用量以及在对应空间内每日按功能模块分类的积分消耗明细。​

说明

用量列表中暂时仅展示有历史累计积分用量的空间。​

​

空间用量概览​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27712%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzEyIiBoZWlnaHQ9IjI1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

空间用量明细​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27980%27%20height=%27822.4586288416076%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTgwIiBoZWlnaHQ9IjgyMi40NTg2Mjg4NDE2MDc2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

查看成员维度的用量明细​

企业成员可以查看自己个人的用量明细，企业旗舰版的超级管理员、管理员可以查看各个企业成员的积分用量明细。​

查看个人用量

查看全体成员用量

企业成员可以在[扣子编程](<https://code.coze.cn/home>)中，单击积分卡片，然后在积分消耗页面，查看自己的积分消耗情况。包括：​

  * 当前企业成员的月度积分总消耗的预估值。​

  * 当前企业成员在各扣子任务、扣子编程任务中的积分消耗预估值以及明细。​

  * 当前企业成员使用各扣子编程付费资源的积分消耗预估值以及明细。​

详细说明，请参考​查看积分消耗明细。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27530%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMwIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

设置积分额度限制​

在企业旗舰版中，企业超级管理员、管理员可以设置组织、空间、成员维度的积分额度限制。​

额度限制规则​

企业超级管理员、管理员可以为组织、空间或成员开启累计额度限制和每月额度限制。​

说明

系统会同时执行你所设置的所有额度限制，其中任一额度达到上限时，其对应范围内的成员均将无法继续使用需要消耗积分的扣子功能。​

​

​

额度限制类型​| 配置说明​| 重置机制​  
---|---|---  
累计额度限制​| 开启额度限制后，当该组织、空间或成员的积分使用量达到额度上限值时，将无法继续使用需要抵扣积分的扣子功能。​| 无自动重置，需超级管理员手动调整额度。​  
每月额度限制​| 开启额度限制后，当该组织、空间或成员在当月的积分使用量达到额度上限值时，当月将无法继续使用需要抵扣积分的扣子功能。​| 每月 1 号自动重置当月额度。​  
  
​

设置组织积分额度限制​

在企业旗舰版中，企业超级管理员、管理员可以在[扣子编程](<https://code.coze.cn/home>)中，单击积分卡片，然后在限额管理>组织总限额页签下，单击目标组织对应的编辑，设置积分额度限制。​

说明

用量列表中暂时仅展示有历史累计用量的组织。若需要对没有历史消耗的组织设置限额，可直接搜索该组织名称。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272082%27%20height=%27959.7872340425532%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA4MiIgaGVpZ2h0PSI5NTkuNzg3MjM0MDQyNTUzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27936%27%20height=%27796.5957446808511%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTM2IiBoZWlnaHQ9Ijc5Ni41OTU3NDQ2ODA4NTExIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

设置空间积分额度限制​

在企业旗舰版中，企业超级管理员、管理员可以在[扣子编程](<https://code.coze.cn/home>)中，单击积分卡片，然后在限额管理>编程空间页签下，单击目标空间对应的编辑，设置积分额度限制。​

说明

用量列表中暂时仅展示有历史累计用量的空间。若需要对没有历史消耗的空间设置限额，可直接搜索该空间名称。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271492%27%20height=%27606.676122931442%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ5MiIgaGVpZ2h0PSI2MDYuNjc2MTIyOTMxNDQyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27936%27%20height=%27809.8723404255319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTM2IiBoZWlnaHQ9IjgwOS44NzIzNDA0MjU1MzE5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

设置成员积分额度限制​

在企业旗舰版中，企业超级管理员、管理员可以为企业成员（管理员、员工、访客）设置积分额度限制，来管理企业成员的积分用量，避免成员过度消耗积分。​

说明

  * 不支持为超级管理员配置积分额度限制。​

  * 用量列表中暂时仅展示有历史累计用量的成员。若需要对没有历史消耗的成员设置限额，可直接搜索该成员对应的用户名或昵称。​

​

企业超级管理员、管理员可以在[扣子编程](<https://code.coze.cn/home>)中，单击积分卡片，然后在限额管理>成员限额页签下，通过如下方式为成员配置积分额度限制。​

  * 成员维度：为单个成员或批量为多个成员设置积分额度限制。​

  * 角色维度：为各个角色设置设置积分额度限制。如果同时设置了成员积分限额和角色积分限额，那么将以成员维度的积分限额为准。​

配置角色资源点额度

配置单个成员资源点额度

批量配置成员资源点额度

在角色限额配置区域中，单击目标角色对应的编辑图标，为各个角色设置积分额度限制。例如为管理员角色设置积分额度限制后，那么所有管理员将统一遵循该限额。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27575%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc1IiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

查看单次调用的积分消耗明细（低代码项目）​

在[扣子编程](<https://code.coze.cn/home>)的低代码项目中，使用模型、插件、工作流、智能语音、知识库、记忆库等扣子付费资源，均会产生相应的费用。扣子支持统计并展示单次智能体对话、工作流试运行所涉及的扣子付费资源、计费项、消耗的积分等信息。该积分统计存在一定的延时，详情请参考​出账延迟说明。​

说明

此处展示的积分预估值，实际扣减以火山账单为准。如何查看账单，请参考​查看总账单。​

​

查看入口​

你可以在如下页面查看单次智能体对话、工作流试运行所消耗的积分。​

​

查看入口​| 说明​| 示例​  
---|---|---  
低代码智能体调试区​​| 在智能体编排页面与智能体对话后，可以查看单次对话涉及的扣子付费资源、计费项、单价、用量及消耗的积分。​

1.单击调试图标。​

2.选择目标对话。​

  * 筛选对话名称，可以查看历史对话的积分消耗情况。​

3.单击积分。​

4.查看此次对话的积分消耗情况。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272549%27%20height=%27691.1467661691541%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU0OSIgaGVpZ2h0PSI2OTEuMTQ2NzY2MTY5MTU0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
低代码工作流调试区​| 在工作流编排页面，可以查看单次试运行涉及的扣子付费资源、计费项、单价、用量及消耗的积分。​

1.单击调试图标。​

2.选择目标试运行时间。​

  * 筛选试运行时间，可以查看历史试运行的积分消耗情况。​

3.选择积分。​

4.查看此次试运行的积分消耗情况。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272544%27%20height=%27810.0298507462686%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU0NCIgaGVpZ2h0PSI4MTAuMDI5ODUwNzQ2MjY4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
  
​

出账延迟说明​

单次智能体对话、工作流试运行所展示的积分消耗明细存在一定延迟，并且不同付费资源的延迟时间不同。​

  * 智能语音相关功能的积分用量展示存在小时级别延迟。​

  * 智能语音涉及声纹识别、语音合成、语音识别、音频通话、视频通话等计费场景，详细的计费项说明，请参考​音视频费用。​

  * 插件、模型、知识库、记忆库等功能消耗的积分展示存在秒级延迟。​

​

上一篇

欠费与关停

下一篇

扣子任务费用