---
source_url: https://docs.coze.cn/tutorial/variable
title: '为自定义参数赋值 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:01Z
---

# 为自定义参数赋值 - 文档 - 扣子

为自定义参数赋值

本文介绍如何在对话流中添加自定义参数，并在对话中为自定义参数赋值。​

功能简介​

在低代码智能体对话流中添加自定义参数，常用于在对话中灵活存储和使用关键信息，以便提供个性化服务、传递上下文信息。例如，你可以在自定义参数中设置用户偏好、用户信息、地理位置、订单信息等，当用户与低代码智能体对话时，可以传入对应的自定义参数的值，以便低代码智能体根据这些参数提供更精准的服务，如根据用户偏好推荐内容、根据订单信息查询物流状态等，从而提升用户体验和对话效率。​

步骤一：在对话流中设置自定义参数​

1.

在对话流编排页面，在开始节点的输入参数中创建自定义参数，并在输出节点中引用该自定义参数。本文以 user_name为例，你可以根据实际业务场景设置其他参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27218.24817518248176%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/33bf6439c7c942dba99707e72094a5e2~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27321.1678832116788%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1f260d677d784b38b6c79666fdb05941~tplv-goo7wpa0wc-quality:q75.image)​

​

​

  * 说明

自定义参数的类型可以是 String 、Array 等多种类型。​

​

2.

将智能体设置为单 Agent（对话流模式），在智能体中添加对话流，发布智能体。​

步骤二：给自定义参数赋值​

你可以根据实际的业务场景，在用户与智能体对话时动态更新和读取自定义参数的值，支持通过如下方式给自定义参数赋值。​

WebSocket 语音通话​

说明

仅支持给发布为 API 的单 Agent（对话流模式）的智能体设置自定义参数。​

​

1.

建立 WebSocket 连接，详细示例代码请参见​双向流式语音对话。​

2.

发送 chat.update 事件，在事件的 chat_config.parameters 参数中指定自定义参数的名称和值，数据类型为 Map[String, Any] 格式的键值对集合。WebSocket 会将该自定义参数的值传给对话流。parameters 中的参数名称为对话流中设置的自定义参数，本示例中为user_name。​

​

JSON

复制

{ ​

"id": "event_id", ​

"event_type": "chat.update", ​

"data": { ​

"chat_config": {​

"parameters": {​

"user_name": "John"​

}​

}​

}​

}​

​

RTC 音视频通话​

说明

仅支持给发布为 API 的单 Agent（对话流模式）的智能体设置自定义参数。​

​

进入 RTC 房间后，发送​更新房间配置上行事件，在事件的 data.chat_config.parameters 参数中指定自定义参数的名称和值，数据类型为 Map[String, Any] 格式的键值对集合。在后续对话中，Realtime SDK 会将该自定义参数的值传给对话流。​

parameters 中的参数名称为对话流中设置的自定义参数，本示例中为user_name。​

​

JSON

复制

{ ​

"id": "7446668538246561828", ​

"event_type": "session.update", ​

"data": { ​

"chat_config": { ​

"parameters": { ​

"user_name": "John"​

} ​

}​

} ​

} ​

​

发起对话 OpenAPI ​

说明

仅支持给发布为 API 的单 Agent（对话流模式）的智能体设置自定义参数。​

​

在调用​发起对话 OpenAPI 时，在 parameters 参数中指定自定义参数的名称和值，数据类型为 Map[String, Any] 格式的键值对集合。智能体会将自定义参数的值传递给对话流。​

parameters 中的参数名称为对话流中设置的自定义参数，本示例中为user_name。​

​

Shell

复制

curl --location --request POST 'https://api.coze.cn/v3/chat?conversation_id=7374752000116113452' \​

\--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \​

\--header 'Content-Type: application/json' \​

\--data-raw '{​

"bot_id": "734829333445931****",​

"user_id": "123456789",​

"stream": true,​

"auto_save_history": true,​

"parameters": {​

"user_name": "John"​

},​

"additional_messages": [​

{​

"role": "user",​

"content": "2024年10月1日是星期几",​

"content_type": "text"​

}​

]​

}'​

​

执行对话流​

说明

仅支持给发布为 API 的单 Agent（对话流模式）的智能体设置自定义参数。​

​

在调用​执行对话流 OpenAPI 时，在 parameters 参数中指定自定义参数的名称和值，数据类型为 Map[String, Any] 格式的键值对集合。parameters 中的参数名称为对话流中设置的自定义参数，本示例中为user_name。​

​

JavaScript

复制

curl -X POST 'https://api.coze.cn/v1/workflows/chat' \​

-H "Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****" \​

-H "Content-Type: application/json" \​

-d '{​

"parameters": {​

"user_name": "John"​

},​

"workflow_id": "你的 workflow id",​

"bot_id": "734829333445931****",​

"additional_messages": [​

{​

"content": "2024年10月1日是星期几",​

"content_type": "text",​

"role": "user",​

"type": "question"​

}​

]​

}'​

​

ChatSDK​

说明

仅支持给发布为 ChatSDK 的低代码应用或单 Agent（对话流模式）的智能体设置自定义参数。​

​

当低代码应用或智能体中绑定了对话流后，调用 ChatSDK 中的 CozeWebSDK.WebChatClient 创建聊天对话框时，在 config 中指定自定义参数的名称和值，数据类型为 Map[String, Any] 格式的键值对集合。ChatSDK 会将自定义参数的值传递给对话流。ChatSDK 的具体使用方法可参考​安装并使用 Chat SDK。​

parameters 中的参数名称为对话流中设置的自定义参数，本示例中为 user_name。​

  * 低代码应用：​

  * ​

JavaScript

复制

new CozeWebSDK.WebChatClient({​

config: {​

type: 'app',​

appInfo: {​

appId: '744189632066042****',​

workflowId: '744229754050396****',​

parameters: {​

user_name: 'John'​

}​

}​

},​

auth: {​

type: 'token', ​

token: 'pat_zxzSAzxawer234zASNElEglZxcmWJ5ouCcq12gsAAsqJGALlq7hcOqMcPFV3wEVDiqjrg****',​

onRefreshToken: () => 'pat_zxzSAzxawer234zASNElEglZxcmWJ5ouCcq12gsAAsqJGALlq7hcOqMcPFV3wEVDiqjrg****',​

}​

});​

​

  * 低代码智能体：​

  * ​

TypeScript

复制

const cozeWebSDK = new CozeWebSDK.WebChatClient({​

config: {​

// 智能体 ID​

botId: '740849137970326****',​

isIframe: false,​

// 给自定义参数赋值并传给对话流​

botInfo: {​

parameters: {​

user_name: 'John'​

}​

}​

},​

auth: {​

// Authentication methods, the default type is 'unauth', which means no authentication is required; it is recommended to set it to 'token', indicating authentication through PAT (Personal Access Token) or OAuth​

type: 'token', ​

// When the type is set to 'token', it is necessary to configure a PAT (Personal Access Token) or OAuth access token for authentication.​

token: 'pat_zxzSAzxawer234zASNElEglZxcmWJ5ouCcq12gsAAsqJGALlq7hcOqMcPFV3wEVDiqjrg****',​

// When the access token expires, use a new token and set it as needed.​

onRefreshToken: () => 'pat_zxzSAzxawer234zASNElEglZxcmWJ5ouCcq12gsAAsqJGALlq7hcOqMcPFV3wEVDiqjrg****',​

}​

});​

​

上一篇

快速搭建智能体列表查询插件

下一篇

优化大模型响应时间