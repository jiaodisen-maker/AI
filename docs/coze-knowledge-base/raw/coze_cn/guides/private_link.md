---
source_url: https://docs.coze.cn/guides/private_link
title: '管理私网连接 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:47:11Z
---

# 管理私网连接 - 文档 - 扣子

管理私网连接

本文介绍如何创建私网连接，以及对私网连接进行断开或删除，以便通过私网模式插件安全地访问插件对应的内部服务。​

功能概述​

扣子编程的 VPC 私网连接功能，为企业用户提供了一种安全访问内部服务的解决方案。企业旗舰版用户可以将火山引擎 VPC 私网部署的内部服务封装为私网插件，扣子编程可以通过终端节点服务安全访问私有插件。私网连接功能同时提供火山引擎私网访问扣子编程 OpenAPI 的能力，创建终端节点之后，即可在火山私网环境下通过终端节点域名访问扣子编程 OpenAPI。​

这种私网连接方式不仅确保了数据传输的安全性和隐私性，还通过白名单管控和自主断开连接等机制，进一步提升了企业场景的数据安全性。​

核心概念​

​

术语​| 说明​  
---|---  
终端节点服务​| 终端节点服务如同智能中转站，可双向转发扣子编程和内部服务请求，以此构建你的私有环境与扣子编程服务的专属通道，实现安全、低延迟的插件和 OpenAPI 调用。​  
终端节点​| 扣子编程 VPC 内创建的接入点，负责将网络请求转发到对应的终端节点服务。​  
私网连接​| 通过终端节点和终端节点服务，能够在你的私有网络 VPC 与扣子编程 VPC 之间构建起一条安全、私密且稳定的连接通道。该通道有效隔绝了公网环境的潜在风险，避免数据在传输过程中遭受网络攻击或泄露，为你提供了安全可靠的访问环境，同时保障数据传输的稳定性和业务运行的流畅性，实现跨 VPC 的资源安全共享。​  
  
​

使用限制​

​

限制项​| 说明​  
---|---  
套餐版本​| 仅扣子企业旗舰版支持私网连接功能。​  
地域要求​| 你的服务需要部署在火山引擎华北 2 地域，其他地域暂不支持与扣子编程进行私网连接。​如果你有其他地域的服务，希望使用私网连接功能，可以联系扣子技术支持，将需求同步给扣子团队评估。​  
跨云/跨地域​| 如果你的业务部署在火山引擎其他地域或其他云厂商，你需要通过 VPN 或专线自行实现 VPC 互通。​  
操作权限​| 仅超级管理员和管理员支持创建和管理私网连接，成员只能查看已创建的私网连接。​  
  
​

通过私网连接访问 OpenAPI​

如果你的业务服务已部署在火山引擎，终端用户往往需要基于 VPC 在私有网络环境中安全访问云服务资源和私网数据。私网访问云服务时，数据在私有网络中传输，不会经过公网，从而避免了数据在公网中被截获或篡改的风险。​

扣子编程现已将 OpenAPI 服务部署在火山引擎，你可按需选择通过公网或是通过火山引擎 VPC 私网连接访问扣子编程 OpenAPI。VPC 私网连接方式确保业务数据在私有网络中传输，可避免公网暴露数据带来的安全风险，适用于对数据和网络安全要求比较高的业务场景。​

详细的配置步骤可参考​通过私网连接访问扣子 API。​

通过私网连接访问私网插件​

在扣子编程使用过程中，常常需要将内部服务封装为插件。然而，这些内部服务通常部署在私有网络（VPC）内，不希望通过公网直接访问。为了确保企业核心数据的安全，避免服务地址暴露至公网，扣子编程提供了一种基于火山引擎私有网络（VPC）的私网连接解决方案。​

通过私网连接，插件可以安全地访问用户部署在私有网络中的内部服务，该方案具备以下优势：​

  * 网络隔离：通过 VPC 间的私网通信，业务资源完全隔绝公网暴露风险，确保数据传输的安全性和隐私性。​

  * 白名单管控：你可以将扣子编程的火山引擎账号 ID 添加到终端节点服务的白名单中，只有白名单中的账号才能通过私网连接访问终端节点服务，有效防止未经授权的访问。​

  * 自主管控连接：你可以在需要时随时断开私网连接，满足安全应急需求。​

私网连接的架构图如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27197.91666666666666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE5Ny45MTY2NjY2NjY2NjY2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置流程​

私网连接的配置流程如下：​

1.

创建终端节点服务：扣子编程在火山引擎的华北 2 地域的 VPC 中部署了服务。你需要在与扣子编程服务相同的华北 2 地域，创建终端节点服务。终端节点服务作为智能中转站，负责接收请求并传递给内部的业务服务。​

2.

添加白名单：在终端节点服务中添加白名单，将扣子编程 VPC 的火山引擎账号 ID 添加到白名单中。只有白名单中的账号才能通过私网连接访问终端节点服务，从而有效防止未经授权的访问。​

3.

创建私网连接：当你在扣子编程创建私网连接时，扣子编程会自动在扣子编程 VPC 中创建终端节点。终端节点作为与扣子编程服务的接入点，会向对应的终端节点服务发起连接请求。​

4.

接受终端连接：你需要在火山引擎控制台接受终端节点连接，私网连接才算连接成功。扣子编程才能通过私网连接访问终端节点服务中的服务资源。​

创建私网连接​

步骤一：创建终端节点服务​

终端节点服务可接收扣子编程请求并准确传递给对应的插件服务，以此构建你的私有环境与扣子编程服务的专属通道。​

在[终端节点服务控制台](<https://console.volcengine.com/pl/endpointServices>)创建华北 2 地域的终端节点服务，具体操作步骤参见[创建终端节点服务](<https://www.volcengine.com/docs/6980/155798>)。​

创建成功后，请复制终端节点服务的 ID，以便后续创建私网连接时填写。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27568.75%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjU2OC43NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：添加白名单​

你需要将扣子编程的火山引擎账号 ID 添加到私网连接的服务白名单中，允许扣子编程 VPC 中的终端节点通过私网连接与你的终端节点服务建立连接。​

单击对应的终端节点服务，在服务白名单页面，将扣子编程的火山引擎账号 ID （固定为：2105685532 ）添加至服务白名单中。具体的操作步骤参见[管理服务白名单](<https://www.volcengine.com/docs/6980/155795>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27436%27%20height=%27296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM2IiBoZWlnaHQ9IjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：（可选）在终端节点服务启用私有 DNS​

大型企业内部通常使用泛域名（例如 *.example.com）管理多个业务服务，此时，通过启用私有 DNS 并指定私有 DNS 名称，可以将企业自身的域名直接映射到私网连接，让内部业务无需适配新域名即可访问后端各业务服务。​

使用场景​

  * 场景一：HTTPS 场景​

  * 使用 HTTPS 协议访问后端服务时，终端节点默认域名与业务证书域名不匹配，可能导致 HTTPS 证书校验失败。通过配置自定义 DNS，使其与 HTTPS 证书域名一致，可规避证书验证失败风险。​

  * 场景二：多服务智能路由​

  * 当终端节点服务背后挂载多个服务，且服务间使用相同主域名时，在 DNS 名称中使用泛域名，即可在同一条私网连接中按子域名（aaa.example.com、bbb.example.com）区分不同后端服务，避免为每个服务创建独立连接，降低资源冗余与运维复杂度。​

操作步骤​

1.

在[终端节点服务控制台](<https://console.volcengine.com/pl/endpointServices>)单击目标终端节点服务的服务 ID 进入终端节点服务的详情页。​

2.

在概览页面的私有DNS名称信息区域，单击启用状态旁边的修改，启用私有 DNS 名称，并配置 DNS 名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27340.97222222222223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM0MC45NzIyMjIyMjIyMjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 在私有 DNS 名称中输入公网域名。推荐配置泛域名形式，例如 *.example.com，则表示该泛域名所覆盖的所有二级子域名均支持解析，例如 abc.example.com 。​

3.

在 DNS 侧为私有 DNS 名称[添加解析记录](<https://www.volcengine.com/docs/6758/109959>)后，单击发起验证，验证私有 DNS 名称，只有验证通过后，才能在扣子编程侧创建私网连接中开启自定义 DNS 解析。详细步骤请参见[修改/验证私有DNS名称](<https://www.volcengine.com/docs/6980/1149794>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27443.9814814814815%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjQ0My45ODE0ODE0ODE0ODE1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤四：创建私网连接​

你需要在扣子编程创建私网连接，填写对应的终端节点服务的 ID，创建成功后，扣子编程会自动在扣子编程 VPC 中创建终端节点。终端节点作为与扣子编程服务的接入点，会向对应的终端节点服务发起连接请求。​

1.

企业超级管理员或管理员登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左下角单击个人头像，选择企业> 团队与企业管理。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27267%27%20height=%27259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY3IiBoZWlnaHQ9IjI1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

3.

在左侧导航栏选择私有网络管理。单击 \+ 私网连接，配置终端节点服务 ID 等相关参数，参数说明如下表所示。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27496.52777777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQ5Ni41Mjc3Nzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

参数​| 说明​  
---|---  
连接名称​| 自定义的连接名称。​  
终端节点服务 ID​| 终端节点服务 ID 为步骤一中创建的终端节点服务对应的 ID。​  
跨账号授权​| 默认只能使用同一个火山引擎主账号下的终端节点服务。如需使用其他火山引擎账号下的私网连接，你需要给扣子编程对应的火山引擎主账号授权终端节点服务的访问权限，具体步骤请参见​跨账号授予私网连接的访问权限。​请填写访问控制中创建的角色的角色 TRN。例如：​trn:iam::21020***:role/CozePrivateLinkEndpointRole。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27157.71812080536913%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE1Ny43MTgxMjA4MDUzNjkxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
自定义 DNS 解析​| 仅当步骤三中启用 DNS 私有名称并验证通过后，方可开启此开关。​开启后，你需要在创建私网模式插件时配置域名前缀，扣子编程即可访问插件对应的服务。具体操作请参见​创建私网模式插件。​  
  
​

4.

创建成功后，私网连接的状态为待连接，需要执行下一步接受终端节点连接。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27714%27%20height=%27208%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzE0IiBoZWlnaHQ9IjIwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：接受终端节点连接​

创建私网连接后，扣子 VPC 中的终端节点会向你的终端节点服务发起建立连接的请求，你需要在火山引擎控制台接受终端节点连接，扣子编程才能通过私网连接访问你的终端节点服务中的服务资源。​

1.

在火山引擎控制台，单击对应的终端节点服务，在终端节点连接页面，接受所属账号为 2105685532 的终端节点连接。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27152.9479768786127%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjE1Mi45NDc5NzY4Nzg2MTI3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

返回扣子编程，查看对应的私网连接状态变为连接成功。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27174.7976878612717%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE3NC43OTc2ODc4NjEyNzE3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤五：创建并使用私网插件​

创建私网连接后，你可以创建并使用私网模式的插件，具体操作请参见​创建私网模式插件。​

管理私网连接​

你可以在私网连接列表中查看各终端节点服务的私网连接状态，并对私网连接进行管理。​

断开私网连接​

如果需要暂停扣子编程通过私网连接访问某个终端节点服务中的服务资源，你可以在火山引擎控制台对应终端节点服务的终端节点连接页面，拒绝扣子编程终端节点的连接。​

断开私网连接后，已绑定该私网连接的插件将无法使用，智能体调用插件会失败。后续可以根据实际需要恢复私网连接。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27158.61271676300578%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjE1OC42MTI3MTY3NjMwMDU3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

删除私网连接​

如果这个私网连接后续不再使用，你可以在扣子编程删除这个私网连接。删除私网连接后，已绑定该私网连接的私网模式插件将无法使用，智能体调用插件会失败。​

注意

删除私网连接后不可恢复，请谨慎操作。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27220.11560693641619%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjIyMC4xMTU2MDY5MzY0MTYxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

跨账号授权​

跨账号授予私网连接的访问权限​

如果扣子编程和私网连接归属不同的火山引擎主账号，此时你需通过跨账号授权功能，将火山账号 A 的私网连接节点授权给火山账号 B 的扣子编程，扣子编程才能访问私网连接中的服务。你可以参考本示例，为账号 B 授予账号 A 私网连接的 PrivateLinkEndpointServiceReadOnlyAccess 权限。​

1.

账号 A 登录[访问控制台](<https://console.volcengine.com/iam/identitymanage/role>)，在角色管理页面单击新建角色，账号 ID 填写扣子编程的火山引擎主账号 ID（本示例中为账号 B），单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27481.5950920245399%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ4MS41OTUwOTIwMjQ1Mzk5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

输入角色名称，角色名称的格式固定为 Coze***Role，例如 CozePrivateLinkEndpointRole。单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27385.67164179104475%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM4NS42NzE2NDE3OTEwNDQ3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在添加权限页面选择 PrivateLinkEndpointServiceReadOnlyAccess，单击提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27449.40476190476187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ0OS40MDQ3NjE5MDQ3NjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击角色名称，在角色详情页，单击信任关系页签，单击编辑信任策略，输入以下信任策略。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27388.88888888888886%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM4OC44ODg4ODg4ODg4ODg4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

JSON

复制

{​

"Statement": [​

{​

"Effect": "Allow",​

"Action": [​

"sts:AssumeRole"​

],​

"Principal": {​

"IAM": [​

"trn:iam::210927***:role/ServiceRoleForCoze" //210927*** 请替换为扣子编程火山引擎主账号 ID。​

]​

}​

}​

]​

}​

​

5.

保存角色 TRN，在扣子编程侧创建私网连接时需要填写该角色 TRN。​

取消授予私网连接的访问权限​

如果需要取消账号 B 的扣子访问账号 A 的私网连接的权限，操作步骤如下：​

1.

账号 A 登录[访问控制台](<https://console.volcengine.com/iam/identitymanage/role>)，撤销对账号 B 的授权。​

  * 单击对应的角色名称，编辑 IAM 角色的信任策略，删除 IAM 中的扣子火山账号 ID。​

  * ​

JSON

复制

{​

"Statement": [​

{​

"Effect": "Allow",​

"Action": [​

"sts:AssumeRole"​

],​

"Principal": {​

"IAM": [​

"trn:iam::210927***:role/ServiceRoleForCoze" //210927*** 请替换为扣子火山引擎主账号 ID。​

]​

}​

}​

]​

}​

​

  * 说明

在访问控制台中删除授权后，之前授权给扣子编程的账号无法再新建私网连接，但是已创建的私网连接仍然保持生效，你需要继续执行下一步。​

​

2.

账号 A 登录[终端节点服务控制台](<https://console.volcengine.com/pl/endpointServices>)断开私网连接。​

  * 在私网连接 > 终端节点连接页面，拒绝扣子终端节点的连接，具体操作请参见​断开私网连接。​

​

​

​

​

​

​

上一篇

配置单点登录（SSO）

下一篇

通过飞书进行 SAML SSO 登录