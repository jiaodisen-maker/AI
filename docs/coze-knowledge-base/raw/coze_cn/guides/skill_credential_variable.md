---
source_url: https://docs.coze.cn/guides/skill_credential_variable
title: '技能环境变量 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:24Z
---

# 技能环境变量 - 文档 - 扣子

技能环境变量

为避免技能（Skill）在运行过程中泄露 API Key、鉴权秘钥、OAuth Token 等敏感信息，你可以使用环境变量来安全地存储和管理这些凭证。​

根据加载方式，我们将环境变量分为以下类型：​

  * 常规变量：Agent 加载技能时，会直接将这类变量加载到运行环境中。由于使用者在查看智能体的思考和规划过程时可能会看到变量的值，因此常规变量适合存储非敏感信息，例如 API 的 Base URL。​

  * 凭证变量：为了保障凭证安全，当 Agent 加载技能时，系统使用占位符来代替凭证变量。只有在技能实际发起 API 调用时，系统才会通过服务端代理加载真实凭证。​

凭证变量​

认证方式​

凭证变量支持以下两种认证方式：​

  * API Key：适用于通过 API 密钥进行鉴权的场景，例如调用火山方舟模型 API。​

  * OAuth：适用于需要 OAuth 协议授权的场景。授权方式包括：​

  * 平台授权：扣子官方已集成的常用第三方平台（如飞书、Notion 等），开发者无需自行配置 OAuth 参数。​

  * 自建授权：对于扣子未支持的平台，或者开发者希望使用自己的授权参数，可以手动配置 OAuth 授权所需的所有参数。​

赋值方式​

根据由谁提供凭证，凭证变量分为以下两种：​

  * 开发者变量：由技能开发者填写变量值，Agent 调用技能时，使用开发者的秘钥等敏感信息发送请求。开发者变量通常是全局固定参数，不因用户的变化而改变，例如第三方服务的密钥。​

  * 消费者变量：技能安装时将提醒用户填写变量值，使用消费者的秘钥，例如用户自己的公众号 AppID、secret 等。不同用户的变量值相互隔离，互不干扰。​

使用场景​

技能环境变量目前支持以下典型场景：​

  * 存储常规配置：用于存放非敏感、但不希望硬编码在代码中的信息，例如 API 的 Base URL。​

  * API Key 鉴权：在调用需 API Key 作为凭证的接口时使用，例如火山方舟模型 API。​

  * 微信公众号消息鉴权：配置微信公众号凭证后，所有请求将通过固定出口 IP (115.190.189.7) 发送。你可以将此 IP 添加到微信公众号的 IP 白名单中。​

  * OAuth 授权：支持平台授权和自建授权两种方式，用于需要 OAuth 认证的服务集成。​

注意事项​

  * 创建方式：在扣子编程中通过 AI 编程来创建技能时，支持使用凭证变量；在扣子对话中制作的技能不支持此功能。​

  * 安全提醒：关于如何安全开发与使用技能的更多信息，可参考​技能安全指南。​

  * 域名配置：每个凭证变量都会关联一个域名列表。为防止凭证泄漏，当 Agent 使用该凭证调用外部 API 时，扣子平台会强制校验请求的域名是否在该列表中，以防止攻击者将凭证恶意发送到未授权的服务器。​

  * 对于官方托管的凭证（例如火山方舟、微信公众号、OAuth 平台授权），其关联域名由扣子平台维护，不支持修改。​

  * 对于扣子编程提示你自行设置的请求域名，请谨慎配置。​

设置常规变量​

技能常规变量的创建和方式和普通环境变量一致，你可以参考​管理环境变量文档查看详细说明。​

1.

创建环境变量：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271388%27%20height=%27492.6235011990408%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM4OCIgaGVpZ2h0PSI0OTIuNjIzNTAxMTk5MDQwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

请扣子 AI 设置环境变量：​

​

Plain Text

复制

将 baseurl 设置为环境变量​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27191%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxIiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

设置凭证变量​

步骤一：创建凭证变量​

在 AI 编程中，你可以通过以下方式创建凭证变量：​

  * 自动识别：对于需要使用秘钥等敏感信息的 AI 编程任务，扣子 AI 会自动识别并提示你将敏感字段封装为变量。例如要求调用火山方舟模型，扣子 AI 将提示你讲 API Key 配置为凭证变量。​

  * 主动指令：对于已开发完成的技能，你可以直接向 AI 发送指令，例如：“请帮我识别代码中的敏感凭证信息，并进行加密。”​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27437%27%20height=%27257%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM3IiBoZWlnaHQ9IjI1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：设置凭证变量​

扣子 AI 识别到敏感凭证后，会根据凭证方便的类型（API Key 或 OAuth），弹出对应的设置卡片。​

API Key 类型​

对于 API Key 类型的变量，你需要选择配置方式。例如某个技能需要调用火山方舟模型 API，则需要设置：​

  * 开发者变量：直接填写变量值，并单击继续。技能运行时将使用你填写的值发起请求。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27312%27%20height=%27282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEyIiBoZWlnaHQ9IjI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 消费者变量：单击设为消费侧变量，无需填写具体值，技能安装和运行时将由最终消费者自行填写凭证内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27444%27%20height=%27227%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ0IiBoZWlnaHQ9IjIyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

OAuth 类型​

对于 OAuth 类型的变量，你需要选择授权方式，再设置配置方式。以下操作以创建一个“查询飞书云文档”的技能为例，扣子 AI 识别出需要编写脚本调用飞书 API，而飞书平台支持 OAuth 授权，因此提示用户选择授权方式。​

1.

选择授权方式。​

  * 平台授权：扣子官方已集成的常用第三方平台（如飞书、Notion 等），开发者无需自行配置 OAuth 参数。​

  * 自建授权：如果平台未被官方集成，选择此项并手动配置所有 OAuth 参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27365%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY1IiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选择赋值方式，即使用开发者还是消费者的秘钥。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27314%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE0IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 平台授权

自建授权

如果选择平台授权，扣子 AI 会进一步提示选择凭证变量的赋值方式。​

    * 消费者授权：无需填写具体值，技能安装和运行时将由最终消费者自行完成 OAuth 授权。​

    * 开发者授权：根据页面提示，登录你的飞书账号，完成 OAuth 授权。技能运行时将使用你的账号权限发起 API 请求，查阅飞书文档。​

    * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27195%27%20height=%27203%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1IiBoZWlnaHQ9IjIwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * 完成设置之后，扣子 AI 将自动编写代码，完成技能的开发。​

步骤三：调试技能​

技能开发完成后，扣子 AI 会提醒你调试技能，你可以输入简单的问题，查看凭证变量的设置是否符合预期。​

  * 开发者变量：技能运行时将自动使用开发者设置的变量值来发起请求，消费者对此无感知。​

  * 消费者变量：调试技能时，系统会弹出凭证填写窗口，填写完成后将独立保存用户的凭证信息，技能运行时将使用该用户配置的变量值来发起请求。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27491%27%20height=%27409.5545023696682%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkxIiBoZWlnaHQ9IjQwOS41NTQ1MDIzNjk2NjgyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27890%27%20height=%27426.01895734597156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODkwIiBoZWlnaHQ9IjQyNi4wMTg5NTczNDU5NzE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

相关操作​

查看环境变量​

添加环境变量后，你可以新建标签页，打开环境变量标签查看所有已配置的环境变量。​

1.

打开环境变量页面。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271121%27%20height=%27750.0215827338129%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEyMSIgaGVpZ2h0PSI3NTAuMDIxNTgyNzMzODEyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

查看环境变量。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271127%27%20height=%27524.3117505995203%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEyNyIgaGVpZ2h0PSI1MjQuMzExNzUwNTk5NTIwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

修改环境变量​

  * 修改变量类型：直接和扣子 AI 对话，要求修改变量类型。例如：​

  * ​

Plain Text

复制

帮我把 API_KEY 改成消费者变量​

​

  * 修改变量名称或值（开发者变量）：​

a.

打开 环境变量 标签页。​

b.

找到您想修改的变量，在其右侧的折叠菜单中单击 编辑。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27617%27%20height=%27341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE3IiBoZWlnaHQ9IjM0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 修改已配置的凭证（消费者变量）：​

  * 技能的消费者可以按以下步骤修改他们自己配置的凭证：​

a.

前往 [扣子技能商店](<https://www.coze.cn/skills?tab=my>)。​

b.

在 我安装的 或 我创建的 列表中找到对应的技能。​

c.

点击授权/配置按钮，即可重新配置变量值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27480%27%20height=%27224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgwIiBoZWlnaHQ9IjIyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

部署时设置凭证变量​

在开发环境完成凭证变量配置后，所有凭证变量将跟随技能一同部署到生产环境。 你也可以直接在部署页面修改凭证变量的值。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27476%27%20height=%27283%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc2IiBoZWlnaHQ9IjI4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

如果在开发环境修改了环境变量，部署时你将能看到修改前后的差异，以便最终确认。​

部署提醒：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272500%27%20height=%271165.1053864168618%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwMCIgaGVpZ2h0PSIxMTY1LjEwNTM4NjQxNjg2MTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

查看差异：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272596%27%20height=%271375.8177458033574%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU5NiIgaGVpZ2h0PSIxMzc1LjgxNzc0NTgwMzM1NzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

常见问题​

  * ​调用技能时，报错环境变量问题​

  * ​配置开发者变量，但使用技能时智能体要求提供凭证​

  * ​如何将开发者环境变量转换为消费者环境变量​

  * ​模型重新配置环境变量后，部署页面出现重复的变量​

  * ​上架商店时提示「skill内的敏感信息校验未通过，请求域名为空」​

  * ​使用技能时提示授权失败，如何解决？​

上一篇

使用技能

下一篇

技能常见问题