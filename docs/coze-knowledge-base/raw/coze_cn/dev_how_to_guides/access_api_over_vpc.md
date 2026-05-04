---
source_url: https://docs.coze.cn/dev_how_to_guides/access_api_over_vpc
title: '通过私网连接访问扣子 API - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:49:56Z
---

# 通过私网连接访问扣子 API - 文档 - 扣子

通过私网连接访问扣子 API

本文介绍企业版用户如何通过火山引擎的私有网络服务，创建私网域名，安全、高效的访问扣子编程 OpenAPI。本操作适用于已经在火山引擎上部署业务，需要在私有网络环境下安全、快速地调用扣子编程 OpenAPI 的场景，可保障数据传输安全。​

背景信息​

如果你的业务服务已部署在火山引擎，终端用户往往需要基于 VPC 在私有网络环境中安全访问云服务资源和私网数据。私网访问云服务时，数据在私有网络中传输，不会经过公网，从而避免了数据在公网中被截获或篡改的风险。​

扣子编程现已将 OpenAPI 服务部署在火山引擎，你可按需选择通过公网或是通过火山引擎 VPC 私网连接访问扣子编程 OpenAPI。VPC 私网连接方式确保业务数据在私有网络中传输，可避免公网暴露数据带来的安全风险，适用于对数据和网络安全要求比较高的业务场景。​

说明

仅扣子企业版支持 VPC 私网连接功能，可通过私网连接访问扣子 API。​

​

核心概念​

​

术语​| 说明​  
---|---  
终端节点服务​| 终端节点服务如同智能中转站，可接收请求并准确传递给扣子编程的 OpenAPI 服务，以此构建你的私有环境与扣子 API 服务的专属通道，实现安全、低延迟的 API 调用。​  
终端节点​| 你在自己的 VPC 内创建的接入点，负责将网络请求转发到对应的终端节点服务。​  
私网连接​| 通过终端节点和终端节点服务，能够在你的私有网络 VPC 与扣子 VPC 之间构建起一条安全、私密且稳定的连接通道。该通道有效隔绝了公网环境的潜在风险，避免数据在传输过程中遭受网络攻击或泄露，为你提供了安全可靠的 API 访问环境，同时保障数据传输的稳定性和业务运行的流畅性，实现跨 VPC 的资源安全共享。​  
  
​

功能原理​

通过私有网络访问扣子编程 API 的实现流程如下：​

1.

创建 VPC：你需要在与扣子服务相同的华北 2 地域、可用区 A 下，创建专属的 VPC。​

2.

建立终端节点：在创建的 VPC 内建立终端节点，作为与扣子服务的接入点。​

3.

发起请求：用户在 VPC 内发起访问扣子 API 的请求时，终端节点会将请求转发至扣子终端节点服务。​

4.

安全连接：终端节点服务将请求传递给扣子 OpenAPI 服务，实现安全、私密的连接，避免公网风险。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27208.78612716763004%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjIwOC43ODYxMjcxNjc2MzAwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

费用说明​

通过私网连接访问扣子 API 时，火山引擎私网连接产品会收取终端节点私网连接费用，这些费用按小时计费并结算，并自动从你的火山引擎余额中扣款，具体收费标准可参考[私网连接计费说明](<https://www.volcengine.com/docs/6980/155785>)。​

计费公式如下：私网连接费用 ＝ 终端节点实例费 ＋ 流量处理费。​

操作步骤​

步骤一：创建私有网络 VPC​

扣子的服务部署在火山引擎华北 2 地域的可用区 A 的 VPC 内，你需要在相同地域和可用区中创建 VPC。​

在 [VPC 控制台](<https://console.volcengine.com/vpc/vpc>)中创建私有网络 VPC，地域选择华北 2，可用区选择可用区 A，其他参数请根据实际情况进行设置，具体请参见[创建私有网络](<https://www.volcengine.com/docs/6401/69467>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27363%27%20height=%27447%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYzIiBoZWlnaHQ9IjQ0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：创建终端节点​

终端节点能够在你的私有网络 VPC 和扣子终端节点服务之间建立一条安全、私密的连接。​

1.

在私网连接 ＞ 终端节点页面，创建终端节点，终端节点服务填写扣子编程的服务名称，固定为 com.volces.privatelink.cn-beijing.epsvc-mjadtc7ir3sw5smt1a2gtwun，单击验证。详细的操作步骤请参见[创建接口终端节点](<https://www.volcengine.com/docs/6980/155853>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27402.3121387283237%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQwMi4zMTIxMzg3MjgzMjM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 说明

如果验证失败，请检查创建终端节点的火山账号和扣子的火山账号是否属于同一个主账号。​

​

2.

在终端节点列表中，记录终端节点域名，下一步中需要使用该域名。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27169.2485549132948%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjE2OS4yNDg1NTQ5MTMyOTQ4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤三：通过私网访问扣子 API​

本文以调用扣子编程的​发起对话 API 为例，需要将扣子编程 API 的 Endpoint 替换为你的终端节点域名，验证在私有网络中能正常访问扣子编程 API，并能够成功与智能体进行对话。​

说明

示例代码中的终端节点域名请替换为步骤二中获取的终端节点域名，例如 ep-13g4yfdc768zk3*****.epsvc-mjadtc7ir3sw5sm****.cn-beijing.privatelink.volces.com。​

​

​

JSON

复制

curl --location '你的终端节点域名/v3/chat' \​

\--header 'Authorization: Bearer pat_Qm47PKJR5dvMOP53v6DyzwCbTtvEZHQc2TVINEveg9v1T3iSYlTdScJ8xWg****' \​

\--header 'Content-Type: application/json' \​

\--data '{​

"bot_id": "749122663625236****",​

"user_id": "a",​

"stream": true,​

"auto_save_history":true,​

"additional_messages":[​

{​

"role":"user",​

"content":"你好",​

"content_type":"text"​

}​

]​

}'​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27149.160393746381%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjE0OS4xNjAzOTM3NDYzODEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

上一篇

API 调用方式概述

下一篇

通过固定 IP 访问扣子 API