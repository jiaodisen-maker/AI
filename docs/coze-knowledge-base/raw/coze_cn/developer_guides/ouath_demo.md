---
source_url: https://docs.coze.cn/developer_guides/ouath_demo
title: '通过示例文件体验 OAuth 授权流程 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:18:21Z
---

# 通过示例文件体验 OAuth 授权流程 - 文档 - 扣子

通过示例文件体验 OAuth 授权流程

扣子编程提供 OAuth 配置的示例文件，帮助开发者在测试验证阶段快速了解和体验 OAuth Token 的生成与授权流程。示例文件中包括客户端私钥等 OAuth 应用的配置信息，并提供 Python、JavaScript、Go 和 Java 四种语言类型的启动脚本，此外还附上了扣子编程 OpenAPI 的请求示例，开发者运行脚本并获取 OAuth Token 后即可成功发起 OpenAPI 请求。​

扣子编程支持的所有 OAuth 授权方式均提供示例文件以供体验。本文档以 Python 语言、授权码授权方式为例，演示下载示例文件并运行脚本获取 OAuth Token 的完整过程。​

说明

  * 此方式仅用于测试验证阶段快速了解和体验 OAuth 授权流程，为了安全起见，获取的 OAuth Token 不建议应用在线上生产环境。线上环境可使用扣子编程提供的各种语言 SDK，参考各个 SDK 的鉴权示例，详细说明可参考​示例代码。​

  * OAuth Token 存在有效期限制，你可以根据页面提示刷新 Token。​

​

步骤一：下载示例文件​

在扣子编程中找到 OAuth 应用，并下载目标语言的配置示例文件。操作步骤如下：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在左侧导航栏选择 API 管理，在顶部选择授权 > OAuth 应用页面。​

3.

找到目标 OAuth 应用，并在其对应的操作列单击下载图标。 ​

  * 授权码授权方式对应的客户端类型为 Web 后端应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27545%27%20height=%27147%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/03fd242800924b98b1bcab445b95ccae~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

预览配置信息，并选择配置语言。​

  * 预览 client_id 等配置信息，确认无误后选择配置语言。扣子编程提供 Python、JavaScript、Go 和 Java 四种语言类型的示例文件，此处我们选择默认的 Python。​

5.

单击下载。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27451%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcyIiBoZWlnaHQ9IjQ1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：本地运行脚本​

本地运行脚本后，通过浏览器访问本地地址，即可根据页面提示获取 OAuth Token。​

说明

  * 运行脚本之前，应确认本地已安装了对应开发语言的运行环境。各个语言的版本要求如下：​

  * Python：3.7 及后续版本。​

  * JavaScript： Node 14 及后续版本。​

  * Go：1.18 及后续版本。​

  * Java：Java 8、Java 11 或 Java 17。​

  * 请确保本地主机的 8080 端口未被占用。​

​

1.

解压缩示例文件到本地目录。​

2.

在解压缩后的目录下执行命令，运行启动脚本。​

  * Linux 或 macOS：​

  * ​

Bash

复制

bash bootstrap.sh​

​

  * Windows：​

  * ​

Bash

复制

.\bootstrap.ps1​

​

3.

浏览器访问本地主机的 8080 端口 http://127.0.0.1:8080。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27342%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQyIiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

根据页面提示完成授权流程、查看或复制 OAuth Token。​

  * 注意

    * 此示例项目仅用于体验授权流程，生成的 Token 虽然是一个真实有效的 OAuth Token，可以在 API Playground 中在线调试 OpenAPI，但不建议用于线上生产环境。​

    * OAuth Token 存在有效期限制，使用前需要注意过期时间。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27351%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUxIiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：发起 OpenAPI 请求​

授权成功后，后端会根据这个 Token 调用一个显示授权用户基本信息的 API。如果 API 请求成功，授权示例页面会显示 Authorization Successful，顶部会同时显示授权用户的基本信息，包括用户 ID、昵称等。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27366%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjM2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

JWT 授权方式下，授权示例页面不会自动调用这个示例 API，只会展示生成的 Token。如需验证 Token 有效性，你可以复制 OAuth Token 之后，前往 [API Playground](<https://code.coze.cn/playground>)，通过这个 Token 快速发起一个扣子 OpenAPI 请求。​

在 API Playground 中找到要调用的 API，在 Header 区域填写 OAuth Token ，并在右侧的 Shell 区域单击运行，即可发起一个 OpenAPI 请求。​

说明

  * 需要注意的是，这个 OAuth Token 必须已被授予对应 OpenAPI 的权限，否则 Playground 调试时会报错 Token 无权限。你需要在下载示例文件之前在 OAuth 应用中选择正确的权限。​

  * 通过示例项目生成的 Token 均可在 API Playground 中使用。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271381%27%20height=%27484.30902777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM4MSIgaGVpZ2h0PSI0ODQuMzA5MDI3Nzc3Nzc3NzciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

上一篇

OAuth 应用管理

下一篇

OAuth 授权码授权