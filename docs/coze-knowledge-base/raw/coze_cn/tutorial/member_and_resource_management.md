---
source_url: https://docs.coze.cn/tutorial/member_and_resource_management
title: 'AI 教学场景的成员与资源管理 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:35Z
---

# AI 教学场景的成员与资源管理 - 文档 - 扣子

AI 教学场景的成员与资源管理

本文以 AI 教学场景为例，介绍教育机构如何通过 API 将内部系统与扣子编程集成，实现单点登录（SSO）、师生账号全生命周期管理、课程工作空间划分及教学智能体资源管控，助力教育机构高效、安全地实现扣子用户权限管理与教学场景化开发。​

场景描述​

在中大型教育机构开展 AI 教学实践时，管理员常面临以下痛点：​

  * 账号初始化低效：大量师生账号需手动注册与分班，耗时耗力。​

  * 权限更新不同步：离职老师或毕业学员权限回收，需在教务系统和扣子编程分别操作，流程繁琐易遗漏。​

扣子编程提供一套完整的 API 集成方案，支持将成员管理、工作空间配置、教学资源协作等核心能力无缝对接至学校自有系统（如教务管理平台、智慧教学系统），助力教育机构实现 “一站式教学管控”，兼顾效率与安全。具体能力包括：​

  * 单点登录（SSO）：师生无需额外注册或记忆多套密码，直接使用校园卡账号、教务系统账号等内部现有账号登录扣子编程，简化师生登录流程。​

  * 师生账号全生命周期管理：支持通过 API 批量完成扣子编程师生用户的创建、教学权限授权、账号注销，降低人工操作成本。​

  * 精细化课程空间权限控制：支持按班级、课程等维度划分独立工作空间，每个空间内可通过文件夹有序管理不同课时的教学内容。通过 API 邀请师生加入指定空间，并针对平台管理员、授课教师、学员分别设置不同权限点，全方位满足教学管理、授课开展、学习实践等多场景需求。​

  * 协同开发：覆盖 AI 教学中的智能体创建、师生多人协作开发、成果发布全流程。​

权限控制​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27322.91666666666663%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e5f2d65b236641d482d036aae31bd2ff~tplv-goo7wpa0wc-quality:q75.image)​

​

协同开发​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27295.13888888888886%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/408c6139c4c341538ab6816e47afce07~tplv-goo7wpa0wc-quality:q75.image)​

​

​

API 调用时序图​

课程开班​

课程开班，添加师生及资源管理的操作流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27443.287037037037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQ0My4yODcwMzcwMzcwMzciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

课程结束​

课程结束，移除用户的操作流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%2794.32870370370372%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9Ijk0LjMyODcwMzcwMzcwMzcyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

准备工作​

​

操作​| 用途​| 参考文档​  
---|---|---  
获取火山账号的 AccessKey 和 SecretKey​| 调用火山引擎的创建成员等 API 时需要身份认证与鉴权。​说明为了账号安全，建议使用子用户密钥，为应用程序创建独立的 IAM 用户，并为 IAM 用户分配 CozeFullAccess 和 CloudIdentityFullAccess 权限。​​| [获取AccessKey、SecretKey](<https://www.volcengine.com/docs/6291/65568>)​  
创建企业特权应用​| 调用企业成员管理 API 时需要身份认证与鉴权，仅该 OAuth 能授权企业管理、组织管理相关权限。​| ​OAuth JWT 授权（企业特权应用）​  
创建普通 OAuth 应用​| 调用扣子编程的创建工作空间、资源管理等 API 时需要身份认证与鉴权。​| ​鉴权方式概述​  
  
​

场景一：配置 SSO 登录​

对于已对接 SAML 2.0 协议或 OAuth 2.0 协议的 IdP（Identity Provider，身份提供商）的教育机构，通过配置 SSO 登录，可实现师生直接使用校园卡账号、教务系统账号等内部现有账号登录扣子编程，无需额外注册或记忆多套密码，简化师生登录流程。​

1.

企业管理员分别在企业 IdP 后台和扣子编程分别配置 SAML 单点登录相关参数，详细步骤请参见​配置单点登录（SSO），配置示例请参见​通过飞书进行 SAML SSO 登录。​

2.

配置 SSO 登录后跳转的扣子编程页面，默认跳转至火山引擎云身份中心的登录门户。具体配置方法请参见​配置 SSO 登录后跳转至扣子编程指定页面。​

场景二：AI 创意编程课开班​

某教育平台新开设"AI 创意编程"班级 1，该课程聚焦人工智能生成内容与少儿编程的融合教学。平台管理员小李需为 1 名老师（A）和 4 名学员（B、C、D、E）开通扣子编程权限，以便师生能顺利开展工作。为避免手动操作繁琐及确保账号规范，管理员通过调用 API 完成相关操作。​

步骤一：创建成员并激活​

管理员小李需要调用火山引擎的 API 分别为师生（A、B、C、D、E）创建火山子用户，并授权其访问扣子，详细说明请参见​成员管理（火山 API）。​

说明

你也可以使用火山引擎提供的 Volcengine SDK 实现成员管理，该 SDK 已内置 AK/SK 签名逻辑，无需自行实现，SDK 接入方法请参见 [Volcengine SDK 接入指南](<https://api.volcengine.com/api-sdk/view?serviceCode=coze&version=2025-06-01&language=Java>)。​

​

1.

创建扣子编程成员。​

  * 管理员小李依次调用火山引擎的 [CreateUser-新建成员](<https://api.volcengine.com/api-docs/view?action=CreateUser&serviceCode=coze&version=2025-06-01>) API，逐一创建 5 名师生的火山子用户，并获取火山 UserID。请求示例如下：​

  * ​

JSON

复制

POST /?Action=CreateUser&Version=2025-06-01 HTTP/1.1​

Host: open.volcengineapi.com​

Content-Type: application/json; charset=UTF-8​

X-Date: 20250605T145232Z​

X-Content-Sha256: 287e874e******d653b44d21e​

Authorization: HMAC-SHA256 Credential=Adfks******wekfwe/20250605/cn-beijing/coze/request, SignedHeaders=host;x-content-sha256;x-date, Signature=47a7d934ff7b37c03938******cd7b8278a40a1057690c401e92246a0e41085f​

​

{​

"UserName": "susu",​

"SecurePhone": "+861112225***5",​

"SecureEmail": "test@email.com"​

}​

​

  * 说明

    * 每次请求只能新增一位成员。如需添加多位，请依次发送请求。​

    * 该 API 不支持并发请求，且单个 API 的流控限制为 5 QPS。​

​

2.

授权成员访问扣子编程并激活账号。​

  * 管理员小李调用火山引擎的 [AuthorizeCozeToUser-授权成员访问扣子](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=AuthorizeCozeToUser>) API，给 5 名师生授权访问扣子编程。授权成功后，该成员即被激活，可以访问扣子编程。请求示例如下：​

  * ​

JSON

复制

POST /?Action=AuthorizeCozeToUser&Version=2025-06-01 HTTP/1.1​

Host: open.volcengineapi.com​

Content-Type: application/json; charset=UTF-8​

X-Date: 20250604T100255Z​

X-Content-Sha256: 287e874e******d653b44d21e​

Authorization: HMAC-SHA256 Credential=Adfks******wekfwe/20250604/cn-beijing/coze/request, SignedHeaders=host;x-content-sha256;x-date, Signature=47a7d934ff7b37c03938******cd7b8278a40a1057690c401e92246a0e41085f​

​

{​

"UserId": "21357147977***" //填写上一步获取的火山用户 ID​

}​

​

3.

查看成员列表。​

  * 管理员小李调用火山引擎的 [ListCozeUser-成员列表](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=ListCozeUser>) API，查看 5 名师生的扣子用户 ID，后续添加企业成员时需要使用对应的扣子用户 ID。请求示例如下：​

  * ​

JSON

复制

POST /?Action=ListCozeUser&Version=2025-06-01 HTTP/1.1​

Host: open.volcengineapi.com​

Content-Type: application/json; charset=UTF-8​

X-Date: 20250605T145044Z​

X-Content-Sha256: 287e874e******d653b44d21e​

Authorization: HMAC-SHA256 Credential=Adfks******wekfwe/20250605/cn-beijing/coze/request, SignedHeaders=host;x-content-sha256;x-date, Signature=47a7d934ff7b37c03938******cd7b8278a40a1057690c401e92246a0e41085f​

​

{​

"QueryString": "user",​

"PageNumber": 1,​

"PageSize": 10,​

"UserName": "username"​

}​

​

4.

（可选）授权访问火山引擎控制台。​

  * 仅当成员需要访问火山引擎控制台时，你可以调用火山引擎的 [AuthorizeVolcToUser-授权访问火山引擎控制台](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=AuthorizeVolcToUser>) API，给该成员授权，否则该成员只能使用扣子编程，无法访问火山引擎控制台。请求示例如下：​

  * ​

JSON

复制

POST /?Action=AuthorizeVolcToUser&Version=2025-06-01 HTTP/1.1​

Host: open.volcengineapi.com​

Content-Type: application/json; charset=UTF-8​

X-Date: 20250605T145209Z​

X-Content-Sha256: 287e874e******d653b44d21e​

Authorization: HMAC-SHA256 Credential=Adfks******wekfwe/20250605/cn-beijing/coze/request, SignedHeaders=host;x-content-sha256;x-date, Signature=47a7d934ff7b37c03938******cd7b8278a40a1057690c401e92246a0e41085f​

​

{​

"UserId": "5123****4"​

}​

​

步骤二：添加企业成员​

管理员小李需要将 5 名师生（A、B、C、D、E）添加到企业中，A 作为老师，设置其为企业管理员（enterprise_admin），其余学员设置为企业成员（enterprise_member）。​

管理员小李依次调用扣子编程的​添加企业成员 API ，逐一将师生添加至企业中，并设置对应的角色。请求示例如下：​

添加学员

添加老师并设为管理员

​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/enterprises/736163827687053****/members' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type : application/json' \​

\--data-raw '{​

"users": [​

{​

"user_id": "21357147977***", // 扣子用户 ID，对应[ListCozeUser-成员列表](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=ListCozeUser>) API返回的 CozeUserId 的值，不是火山 UserId。​

"role": "enterprise_member" //设置学员在企业中的角色为普通成员。​

}​

]​

}'​

​

​

说明

  * 每次请求只能添加一位成员。如需添加多位，请依次发送请求。​

  * user_id 需使用扣子用户 ID（CozeUserId），非火山引擎 UserID，你可以调用火山引擎的 [ListCozeUser-成员列表](<https://api.volcengine.com/api-docs/view?serviceCode=coze&version=2025-06-01&action=ListCozeUser>) API 查看。​

​

步骤三：工作空间管理​

建议按班级划分工作空间，每个空间内可创建文件夹，用于管理不同课时的教学内容。邀请师生加入空间并设置其角色，实现资源隔离与分级权限管理。​

1.

创建工作空间。​

  * 管理员小李调用​创建工作空间 API 创建工作空间，并设置该工作空间所属的组织。请求示例如下：​

  * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/workspaces' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"name": "AIGC创意编程班级1",​

"description": "AIGC创意编程班级1使用的工作空间。",​

"icon_file_id": "73694959811****",​

"coze_account_id": "749088814445***", //组织 ID，用于标识工作空间所属的组织。你可以在组织设置页面查看对应的组织 ID。​

}'​

​

2.

批量邀请用户加入空间。​

  * 创建工作空间后，管理员小李调用​批量邀请用户加入空间 API 将 5 名师生（A、B、C、D、E）添加至工作空间中，并指定老师 A 为工作空间管理员（admin），其余 4 个学员为工作空间成员（member）。​

  * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/workspaces/7515267805***/members' \​

\--header 'Content-Type: application/json' \​

\--header 'Authorization: Bearer pat_O******' \​

\--data-raw '{​

"users": [​

{​

"role_type": "admin", // A 作为工作空间管理员​

"user_id": "55242585801***" // A 的扣子用户 ID，即CozeUserId​

},​

{​

"role_type": "member", // B 作为工作空间成员​

"user_id": "21357147977***" // B 的扣子用户 ID，即CozeUserId​

},​

{​

"role_type": "member", // C 作为工作空间成员​

"user_id": "21357147978***" // C 的扣子用户 ID，即CozeUserId​

},​

{​

"role_type": "member", // D 作为工作空间成员​

"user_id": "21357147979***" // D 的扣子用户 ID，即CozeUserId​

},​

{​

"role_type": "member", // E 作为工作空间成员​

"user_id": "21357147980***" // E 的扣子用户 ID，即CozeUserId​

}​

]​

}'​

​

3.

在工作空间内创建文件夹。​

  * 老师 A 在扣子编程的工作空间 > 项目管理页面，单击右上角的新增文件夹，为每个课时创建文件夹，用于管理不同课时的教学内容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27111.1111111111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjExMS4xMTExMTExMTExMTExIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤四：资源管理​

1.

老师 A 调用​创建智能体 API 创建教学示范智能体。​

  * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/bot/create' \​

\--header 'Authorization : Bearer pat_Osa******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"space_id": "7515267805***", // 绑定"AIGC创意编程班级1"的课程空间ID​

"name": "童话编程故事生成器",​

"description": "帮助小学生构思童话故事框架，并生成可用于编程动画的情节脚本",​

"icon_file_id": "73694959811****", // 选用童话书风格的图标​

"prompt_info": {​

"prompt": "你是少儿故事创作导师，能根据学员提供的角色（如小猫、机器人）和场景（如森林、太空），生成3-5段适合编程动画的童话故事片段。每段包含角色动作描述（便于转化为动画指令）和简单对话，语言要生动有趣，词汇难度适合8-10岁儿童"​

},​

"onboarding_info": {​

"prologue": "你好呀！我是故事创作小助手～ 告诉我你想写什么角色的故事，发生在什么地方，我来帮你构思情节哦！",​

"suggested_questions": [​

"帮我写一个太空探险的故事，主角是机器人小铁",​

"森林里的小兔子和狐狸能成为朋友吗？编个故事吧",​

"请用小猫、月亮、雨伞创作一段童话"​

]​

},​

"workflow_id_list": {​

"ids": [​

{​

"id": "746049108611037****" // 绑定故事段落拆分工作流​

}​

]​

},​

"model_info_config": {​

"model_id": "1706077826" ​

}​

}'​

​

2.

学员根据自己的创意新建智能体，或复制老师 A 创建的智能体，在其基础上修改。本文以通过 API 复制智能体为例。​

a.

调用​复制资源 API，将老师 A 创建的智能体模板复制到学员课程的工作空间，例如 "AIGC创意编程班级1"的课程空间。​

b.

调用​查询资源复制的结果，根据​复制资源 API 返回的 task_id 查询复制结果。如果是本空间内复制智能体，则无需执行该步骤，跨空间复制智能体、扣子应用和工作流需要执行该步骤。​

  * 复制资源​

​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/entities/copy_tasks' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"entity_id": "73428668*****", //老师 A 创建的智能体模板的 ID​

"entity_type": "bot",​

"to_workspace_id": "7515267805***" //"AIGC创意编程班级1"的课程空间ID​

}'​

​

查询资源复制的结果​

​

JSON

复制

curl --location --request GET 'https://api.coze.cn/v1/entities/copy_tasks/567456700***' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type: application/json' \​

​

​

3.

配置多人协作。​

  * 为便于教学指导，为学员创建的智能体添加老师 A 为协作者，以便老师查看学员的智能体搭建进度，并提供针对性指导。​

  * 智能体​

1.

调用​开启或关闭智能体多人协作 API 开启多人协作模式。​

    * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/bots/73428668*****/collaboration_mode' \​

\--header 'Authorization : Bearer pat_Osa******' \​

\--header 'Content-Type : application/json' \​

\--data-raw '{​

"collaboration_mode": "collaboration"​

}'​

​

2.

调用​添加智能体的协作者和​删除智能体的协作者 API 对智能体的协作者进行管理。​

    * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/bots/737946218936519****/collaborators' \​

\--header 'Authorization : Bearer pat_Osa******' \​

\--header 'Content-Type : application/json' \​

\--data-raw '{​

"collaborators": [​

{​

"user_id": "55242585801***" // A 的扣子用户 ID，即CozeUserId​

}​

]​

}'​

​

工作流​

1.

调用​开启或关闭工作流多人协作 API 开启多人协作模式。​

    * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/workflows/746049108611037****/collaboration_mode' \​

\--header 'Authorization : Bearer pat_Osa******' \​

\--header 'Content-Type : application/json' \​

\--data-raw '{​

"collaboration_mode": "collaboration"​

}'​

​

2.

调用​添加工作流协作者和​删除工作流协作者 API 对工作流的协作者进行管理。​

    * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/workflows/73505836754923***/collaborators' \​

\--header 'Authorization: Bearer pat_hfwkehfncaf****' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"collaborators": [​

{​

"user_id": "55242585801***" // A 的扣子用户 ID，即CozeUserId​

}​

]​

}'​

​

​

  * 说明

每次请求只能添加一位协作者。如需添加多位，请依次发送请求。​

​

4.

调用​发布智能体 API 发布智能体。​

  * ​

JSON

复制

curl --location --request POST 'https://api.coze.cn/v1/bot/publish' \​

\--header 'Authorization: Bearer pat_x*******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"bot_id": "73428668*****",​

"connector_ids": [​

"1024"​

]​

}'​

​

  * 说明

学员和老师均能发布智能体。​

​

场景三：课程结束后，移除成员​

学员账号存续期间产生的费用由企业承担，并计入企业权益中的成员费用。另外，学员发布的智能体或应用在运行时所产生的 token 消耗也将由企业承担。因此，课程结束后建议及时清理冗余学员账号，或在清理前通过权限管控限制学员的发布权限，避免不必要的成本支出。​

课程结束后，请按以下顺序将学员移除：​

1.

（可选）移除工作空间成员。​

  * 调用​批量移除空间中的用户API 将其移出工作空间，扣子编程默认会将其拥有的资源转移给工作空间所有者。​

  * 你也可以跳过本步骤，在移出组织时会自动将其移出工作空间，但资源会转交给组织超级管理员。为避免资源过度集中到组织超级管理员，确保资源仍归属原项目团队，减少后续资源交接成本，建议执行本步骤。​

  * ​

JSON

复制

curl --location --request DELETE 'https://api.coze.cn/v1/workspaces/751526780526****/members' \​

\--header 'Content-Type: application/json' \​

\--header 'Authorization: Bearer pat_FFTwA******' \​

{​

"user_ids": ["21357147977***","21357147978***", "21357147979***", "21357147980***"] // 学员的扣子用户 ID，即CozeUserId​

​

2.

移除组织成员。​

  * 调用​移除组织成员 API 依次将这个班级中的学员移出对应的组织，并将其资源转交给组织超级管理员，从而有效保护企业数据安全，避免资源泄露。​

  * ​

JSON

复制

curl --location --request DELETE 'https://api.coze.cn/v1/organizations/74908881444562***/members/41147914833****' \​

\--header 'Authorization : Bearer pat_O******' \​

\--header 'Content-Type : application/json' \​

\--data-raw '{​

"receiver_user_id": "21357147977***" // B 的扣子用户 ID，即CozeUserId​

}'​

​

  * 说明

每次请求只能移除一位成员。如需移除多位，请依次发送请求。​

​

3.

移除企业成员。​

  * 调用​移除企业成员 API 将学员移出企业。移除后，该学员将不再占用扣子套餐内的成员席位。​

  * ​

JSON

复制

curl --location --request DELETE 'https://api.coze.cn/v1/enterprises/736163827687053****/members/41147914833****' \​

\--header 'Authorization: Bearer pat_O******' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"receiver_user_id": "21357147977***" // B 的扣子用户 ID，即CozeUserId​

}'​

​

4.

删除子用户。​

  * 在火山引擎控制台将毕业学员绑定的子用户删除，彻底回收账号权限，详细操作请参见​删除成员。​

常见问题​

移出组织成员之前需要将其移出工作空间吗？​

移出组织成员时，扣子编程会自动将其移出工作空间，并将其拥有的资源转移给指定的组织超级管理员。​

为避免资源过度集中到组织超级管理员，确保资源仍归属原项目团队，减少后续资源交接成本，建议调用​批量移除空间中的用户API 先将离职成员移出工作空间。移出工作空间时，扣子编程会自动将其拥有的资源转移给工作空间所有者，而不是转移给组织超级管理员。​

​

上一篇

查询股票价格

下一篇

入驻公共渠道