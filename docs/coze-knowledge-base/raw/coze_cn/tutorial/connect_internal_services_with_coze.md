---
source_url: https://docs.coze.cn/tutorial/connect_internal_services_with_coze
title: '企业内部服务如何与扣子安全连接 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:41Z
---

# 企业内部服务如何与扣子安全连接 - 文档 - 扣子

企业内部服务如何与扣子安全连接

扣子编程提供了多种安全连接方式，确保企业内部服务在与扣子编程对接时的数据安全与合规性。你可以根据不同的业务场景和安全需求，选择合适的扣子安全连接方案。本文介绍企业内部服务与扣子编程建立安全连接的五种方式。​

安全连接方式概览​

​

项目​| 企业安全访问扣子 API​| ​| 扣子安全访问企业服务​| ​| 企业审核插件使用者​  
---|---|---|---|---|---  
​| 固定 IP 访问扣子 API​| 私网连接访问扣子 API​| 固定 IP 访问插件​| 私网连接访问私网插件​| 插件 Header 透传用户 ID​  
适用版本​| 企业旗舰版​| 企业旗舰版​| 企业旗舰版（白名单功能）​| 企业旗舰版​| 所有套餐版本​  
适用场景​| 通过固定 IP 限制访问源，满足企业安全合规要求。​| 企业服务部署在火山引擎 VPC 内，希望避免任何公网数据传输风险。​| 插件化的内部服务需要被扣子编程调用，且企业管控访问内网服务的公网 IP。​| 将部署在火山引擎 VPC 内的内部服务封装为扣子私网插件，内部服务无需暴露公网。​| 在插件调用时传递用户身份信息，用于内部服务的权限校验或审计。​  
核心优势​| 适配企业防火墙白名单策略，满足外网访问的合规性要求。​| 数据仅在 VPC 内传输，避免公网数据传输风险。​| 适配企业防火墙白名单策略，实现对公网访问内网服务的源 IP 管控。​| 

  * 私网调用，确保了数据传输的安全性和隐私性。​

  * 通过白名单管控和自主断开连接机制，进一步提升数据安全性。​

| 轻量级实现用户身份的传递。​  
架构示意图​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27194.87179487179486%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f58743f73d54446f901f12a40e37296d~tplv-goo7wpa0wc-quality:q75.image)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27139.83739837398375%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1d94f7b418a94145b756ee43e8c0872d~tplv-goo7wpa0wc-quality:q75.image)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27202.66666666666669%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cf3a875537b14e74a00ec66e80fb1fc8~tplv-goo7wpa0wc-quality:q75.image)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27184.1726618705036%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b5d74b50170b4fac823d16b05bf11030~tplv-goo7wpa0wc-quality:q75.image)​​| -​  
配置复杂度​| 低​| 中​| 低​| 高​| 低​  
参考文档​| ​通过固定 IP 访问扣子 API​| ​通过私网连接访问扣子 API​| ​通过固定 IP 访问插件​| ​管理私网连接​​创建私网模式插件​| -​  
  
​

企业安全访问扣子 API​

方式一：通过固定 IP 访问扣子 API​

适用场景​

对于需要严格管控访问外部服务的企业，此方案允许你将扣子 API 的固定 IP 地址加入防火墙白名单，确保连接的合规性。​

配置步骤​

1.

配置防火墙白名单。​

  * 将如下扣子域名对应的 IP 列表添加到企业 IDC 防火墙的出口 IP 白名单中。​

  *     * 36.110.186.29​

    * 36.110.186.35​

    * 101.126.58.176​

    * 101.126.58.175​

    * 101.126.58.177​

    * 110.249.198.5​

    * 110.249.198.6​

    * 111.62.49.199​

    * 111.62.49.200​

    * 111.63.62.233​

    * 111.63.62.234​

    * 111.225.144.30​

    * 111.225.144.31​

    * 113.24.210.25​

    * 113.24.210.26​

    * 121.30.176.142​

    * 121.30.176.143​

    * 122.14.229.7​

    * 122.14.229.103​

    * 122.14.229.102​

    * 183.201.125.143​

    * 183.201.125.144​

    * 221.194.131.78​

    * 221.194.131.81​

​

2.

使用固定 IP 域名访问扣子 API。​

  * 将扣子 API 请求的 Endpoint 替换为扣子的固定 IP 专用域名： https://static-api.coze.cn。​

  * API 请求示例：​

  * ​

JSON

复制

curl --location 'https://static-api.coze.cn/v3/chat' \​

\--header 'Authorization: Bearer pat_Qm47PKJR5dvMOP53v6DyzwT3iSYlTdScJ8xWg****' \​

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

方式二：通过私网连接访问扣子 API​

适用场景​

企业服务部署在火山引擎 VPC 内，需通过私有网络安全调用扣子 Open API，避免公网数据传输风险。​

配置步骤​

1.

创建 VPC 与终端节点。​

a.

在 [VPC 控制台](<https://console.volcengine.com/vpc/vpc>) 华北 2 地域可用区 A 创建与扣子服务同地域的 VPC，具体请参见[创建私有网络](<https://www.volcengine.com/docs/6401/69467>)。​

b.

在私网连接 ＞ 终端节点页面创建终端节点，终端节点服务填写扣子的服务名称（固定为 com.volces.privatelink.cn-beijing.epsvc-mjadtc7ir3sw5smt1a2gtwun）。​

  * 创建 VPC​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27492.75362318840575%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ5Mi43NTM2MjMxODg0MDU3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

创建终端节点​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27321.73913043478257%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMyMS43MzkxMzA0MzQ3ODI1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

获取终端节点域名​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2784.05797101449275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9Ijg0LjA1Nzk3MTAxNDQ5Mjc1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

2.

通过私网访问扣子 API。​

  * 将扣子 API 请求的 Endpoint 替换为上一步创建的终端节点的终端节点域名。​

  * API 请求示例：​

  * ​

JSON

复制

curl --location '你的终端节点域名/v3/chat' \​

\--header 'Authorization: Bearer pat_Qm47PKJR5dvMOP53v6Deg9v1T3iSYlTdScJ8xWg****' \​

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

扣子安全访问企业服务​

方式一：通过固定 IP 访问插件​

适用场景​

当企业内部服务被封装为扣子插件，并且企业安全策略要求对所有访问内网服务的公网 IP 进行管控时，你可以通过固定的 IP 地址来调用插件。​

配置步骤​

说明

仅基于已有服务创建的云侧插件支持该功能，扣子 IDE 中创建的云侧插件和端侧插件不支持。​

​

1.

申请开通白名单。​

  * 该功能目前仅对扣子企业旗舰版的白名单用户开放。如果需要使用此功能，请联系商务经理，提供插件所在的空间 ID，申请加入白名单。申请通过后，扣子编程会提供具体的 IP 地址列表。​

2.

配置防火墙白名单。​

  * 将扣子编程提供的固定 IP 地址列表添加到企业防火墙白名单中。​

3.

开启插件的固定 IP 调用。​

  * 在资源库页面，单击需要使用固定 IP 访问的插件。单击插件名称后面的修改图标，在编辑插件配置页面，开启固定 IP 调用。开启后，扣子将通过固定 IP 地址列表中的 IP 访问插件对应的服务。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27130.49645390070924%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEzMC40OTY0NTM5MDA3MDkyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27568.0659670164919%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjU2OC4wNjU5NjcwMTY0OTE5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​

方式二：通过私网连接访问私网插件​

适用场景​

将部署在火山引擎 VPC 内的内部服务封装为扣子私网插件，并通过私网进行安全调用，避免内部服务地址暴露公网。​

配置步骤​

1.

创建终端节点服务。​

  * 在[终端节点服务控制台](<https://console.volcengine.com/pl/endpointServices>)创建华北 2 地域的终端节点服务，具体操作步骤参见[创建终端节点服务](<https://www.volcengine.com/docs/6980/155798>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27406.35838150289015%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQwNi4zNTgzODE1MDI4OTAxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

添加白名单。​

  * 单击对应的终端节点服务，在服务白名单页面，将扣子编程的火山引擎账号 ID（固定为：2105685532）添加至服务白名单中，授权扣子编程访问。具体的操作步骤参见[管理服务白名单](<https://www.volcengine.com/docs/6980/155795>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27436%27%20height=%27296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM2IiBoZWlnaHQ9IjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在扣子编程创建私网连接。​

  * 在扣子编程的组织管理 > 私有网络管理页面。单击 \+ 私网连接，配置终端节点服务 ID 为上一步创建的终端节点服务的 ID。详细的参数说明请参见​步骤四：创建私网连接。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27457.8034682080924%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQ1Ny44MDM0NjgyMDgwOTI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

接受终端节点连接。​

a.

在火山引擎控制台，单击对应的终端节点服务，在终端节点连接页面，接受所属账号为 2105685532 的终端节点连接。​

b.

返回扣子编程，查看对应的私网连接状态变为连接成功。​

  * 火山控制台接受终端节点连接​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2787.39884393063583%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9Ijg3LjM5ODg0MzkzMDYzNTgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

扣子编程查看私网连接状态​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27116.53179190751446%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjExNi41MzE3OTE5MDc1MTQ0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

5.

创建并使用私网插件。​

  * 创建插件时，在私网连接中选择上一步已建立的私网连接，具体操作请参见​创建私网模式插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27553.5911602209944%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjU1My41OTExNjAyMjA5OTQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

企业审核插件使用者​

插件 Header 参数透传用户 ID​

适用场景​

在插件调用时传递用户身份信息（如企业员工 ID），用于内部服务的权限校验或审计。​

配置步骤​

1.

绑定用户变量。​

  * 通过​发起对话 API 调用插件时，在 user_id 参数中填写企业员工的用户 ID。​

  * 扣子编程调用插件时，会自动在插件请求的 Header 中注入通用字段 X-Aiplugin-Connector-Identifier，用于标识用户 ID。​

2.

内部服务接收 Header。​

  * 内部服务在接收插件请求时，从请求 Header 中解析 X-Aiplugin-Connector-Identifier字段的值，进行身份验证或日志记录。​

上一篇

企业内部权限管理