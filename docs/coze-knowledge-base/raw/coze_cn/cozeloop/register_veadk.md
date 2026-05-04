---
source_url: https://docs.coze.cn/cozeloop/register_veadk
title: '火山智能体注册 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:55:57Z
---

# 火山智能体注册 - 文档 - 扣子

火山智能体注册

在扣子罗盘中注册火山智能体后，你可以在扣子罗盘中观测、调试或评测该火山智能体。​

什么是火山智能体​

火山智能体是通过火山引擎智能体框架（VeADK，Volcengine Agent Development Kit）开发的智能体。关于 VeADK 的详细说明可参考[ VeADK 帮助文档](<https://volcengine.github.io/veadk-python/>)。目前，仅部署到火山引擎函数服务和火山引擎 AgentKit 的火山智能体可以在扣子罗盘中注册。​

  * 参考 [部署到 VeFaaS](<https://volcengine.github.io/veadk-python/deploy/deploy-vefaas/>) 把火山智能体部署到函数服务。​

  * 参考 [部署到 AgentKit](<https://volcengine.github.io/veadk-python/deploy/deploy-agentkit/>) 把火山智能体部署到 AgentKit。​

注意

火山智能体的部署模式必须选择 A2A / MCP Server，才能注册到扣子罗盘进行评测。​

​

火山智能体的 Trace 数据可以直接上报至扣子罗盘，实现调用链路观测；在扣子罗盘中注册的火山智能体，也可以通过观测功能进行 Agent 评测。​

注册火山智能体​

步骤一（可选）：把火山智能体的 Trace 数据上报到扣子罗盘​

如需通过扣子罗盘实现 Trace 观测，在通过 VeADK 开发火山智能体时，你需要通过以下步骤上报 Trace 数据。配置步骤如下：​

1.

在 VeADK 配置文件 config.yaml 的 observability 字段中填写 cozeloop 的属性。关于配置文件的详细说明及示例可参考 [配置文件](<https://volcengine.github.io/veadk-python/configuration/>)。​

  * ​

属性​| 说明​  
---|---  
endpoint​| 固定设置为 https://api.coze.cn/v1/loop/opentelemetry/v1/traces。​  
api_key​| 扣子罗盘访问密钥，支持个人访问令牌、OAuth 访问令牌和服务访问令牌。获取方式可参考​配置个人访问令牌。​  
service_name​| 扣子罗盘工作空间的 ID。你可以在登录扣子罗盘之后，左上角切换到想要存放火山智能体数据的工作空间，并在 URL 的 space 关键词之后获取工作空间 ID，例如 https://loop.coze.cn/console/enterprise/personal/space/73917415734092****/pe/prompts 中，73917415734092****为工作空间 ID。​  
  
​

  * 一个可参考的 config.yaml 示例如下：​

  * ​

YAML

复制

model:​

agent:​

provider: openai​

name: doubao-1-5-pro-256k-250115​

api_base: https://ark.cn-beijing.volces.com/api/v3/​

api_key: 火山方舟模型apikey​

​

# 火山引擎认证信息​

volcengine:​

access_key: 填自己的火山ak​

secret_key: 填自己的火山sk​

​

observability:​

# [optional] for exporting tracing data to Volcengine CozeLoop and APMPlus platform​

opentelemetry:​

cozeloop:​

endpoint: https://api.coze.cn/v1/loop/opentelemetry/v1/traces​

api_key: 填罗盘的apikey​

service_name: 填要上报trace的罗盘的空间ID​

​

2.

设置云端上报器 exporter，添加 CozeLoopExporter 以记录 Agent 执行过程中的关键路径与中间状态。详细说明及示例代码可参考 [VeADK 观测](<https://volcengine.github.io/veadk-python/observation/tracing#火山云观测>)。​

步骤二：获取访问域名和 API Key​

如果你的火山智能体部署到了 AgentKit，你可以直接跳到步骤三。​

如果你的火山智能体部署到了函数服务，你需要在函数服务的 我的应用 列表中找到已部署的火山智能体的访问域名与 API Key。如下图所示:​

  * 访问域名：访问地址 ？前面的部分。​

  * API Key：访问地址中请求参数 Token 的值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272608%27%20height=%27196.2037037037037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYwOCIgaGVpZ2h0PSIxOTYuMjAzNzAzNzAzNzAzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：注册火山智能体​

目前，注册部署到函数服务的火山智能体需要在扣子罗盘操作；注册部署到 AgentKit 的火山智能体需要在 AgentKit 操作。​

注册部署到函数服务的火山智能体​

1.

登录扣子罗盘。​

2.

在左侧导航栏中选择 应用 > 应用注册，并在页面右上角单击 注册新应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273808%27%20height=%271762.962962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgwOCIgaGVpZ2h0PSIxNzYyLjk2Mjk2Mjk2Mjk2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

把火山部署平台设置为 VeFaaS，然后把你在步骤二获取的访问域名和 API Key 分别填入 火山智能体访问域名 和 火山智能体 API Key。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273350%27%20height=%271302.7777777777778%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM1MCIgaGVpZ2h0PSIxMzAyLjc3Nzc3Nzc3Nzc3NzgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

4.

单击获取智能体元信息，测试 Endpoint 是否能正常访问，并获取到对应智能体元信息（ID、名称与描述）。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27659%27%20height=%27498%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU5IiBoZWlnaHQ9IjQ5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

确认无误后，单击确认注册。​

  * 说明

若注册的火山智能体的 Trace 未上报到当前工作空间，不影响注册，且注册后可开展评测实验，但在当前空间查询不到此智能体的 Trace 数据。​

​

注册部署到 AgentKit 的火山智能体​

参考 [接入Cozeloop](<https://www.volcengine.com/docs/86681/1848568?lang=zh>) 在 AgentKit 中把火山智能体注册到扣子罗盘。你暂时无法在扣子罗盘中注册部署到 AgentKit 的火山智能体。​

其他操作​

观测火山智能体​

完成火山智能体的 Trace 数据上报和注册之后，你可以在 应用详情 页面的 观测 页签查看来源为当前火山智能体的 Trace 数据。 关于 Trace 功能的详细说明可参考 ​查看 Trace 数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273336%27%20height=%27976.8611111111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzNiIgaGVpZ2h0PSI5NzYuODYxMTExMTExMTExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

调试火山智能体​

你可以在 应用详情 页面的 调试 页签调试在扣子罗盘中注册的火山智能体。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273354%27%20height=%271890.5069444444446%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM1NCIgaGVpZ2h0PSIxODkwLjUwNjk0NDQ0NDQ0NDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

评测火山智能体​

在扣子罗盘中注册火山智能体后，你在 应用详情 页面的 评测 页签查看当前火山智能体的实验列表，也可以单击 新建实验 为当前火山智能体创建评测实验。关于评测实验的详细操作步骤可参考​评测概述 。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273356%27%20height=%271903.2870370370372%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM1NiIgaGVpZ2h0PSIxOTAzLjI4NzAzNzAzNzAzNzIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

编辑火山智能体​

若火山智能体迭代变更后，如果 API key 有变更，可通过修改应用配置来重新设置 API key；如果智能体名称或描述有变更，可刷新火山智能体信息。操作步骤如下：​

1.

在左侧导航栏中单击应用注册，并在列表中找到要修改的火山智能体。​

2.

在操作列单击编辑。​

3.

在 编辑应用 页面单击 修改配置。​

4.

你可以重新设置 API Key，也可以单击 获取智能体原信息 来刷新火山智能体信息。修改完成后，单击确认。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272594%27%20height=%271197.923611111111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU5NCIgaGVpZ2h0PSIxMTk3LjkyMzYxMTExMTExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

上一篇

Trace 数据回流

下一篇

SDK 概述