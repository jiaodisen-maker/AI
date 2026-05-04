---
source_url: https://docs.coze.cn/guides/chatflow_api_request_parameter_verification
title: '对话流 API 请求参数校验调整的公告 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:28:23Z
---

# 对话流 API 请求参数校验调整的公告 - 文档 - 扣子

对话流 API 请求参数校验调整的公告

为进一步提升扣子对话流 API 的服务稳定性、降低异常请求导致的业务中断风险，我们将对执行对话流 API 的additional_messages 请求参数启动标准化规则校验。​

调整时间​

自 2025 年 9 月 5 日起，扣子将正式对​执行对话流 API 的以下请求参数进行强规则校验：​

  * additional_messages.content​

  * additional_messages.role​

  * additional_messages.content_type​

调整内容​

若​执行对话流 API 的 additional_messages 请求参数不符合传参规则，在执行时将返回失败。为避免对你的线上业务造成影响，请根据本文中的检查清单仔细检查代码中对应的传参是否符合规范。若发现不符合的情况，请尽快进行修复。​

检查清单​

请对照以下规则，逐一对代码中的请求参数进行核查。​

​

校验字段​| 规则说明​| 错误示例​| 正确示例​  
---|---|---|---  
additional_messages.content​| 必填项，且其值不能为空字符串。用于输入对话的具体内容。如果该字段缺失或其值为空字符串，API 将拒绝处理该请求。​| "content": ""（空字符串）​| "content": "请推荐一款智能家居产品"​  
additional_messages.role​| 必填项，用于标识消息的发送者身份。其值仅支持 user、assistant 或 system 。且当​additional_messages.type为 question 时，role 字段的值必须为 user。​| 

  * "type": "user"（参数名不正确）​

  * "role": "admin"（无效值）​

| "role": "user"​  
additional_messages.content_type​| 必填项，用于定义 content 内容的格式。其值仅支持 text、object_string 或 card。​| 

  * 没有填写 content_type​

  * "content_type": "image"（无效值）​

| "content_type": "text"​  
  
​

正确请求示例​

​

JSON

复制

curl --location 'https://api.coze.cn/v1/workflows/chat' \​

\--header 'Authorization: Bearer pat_*****' \​

\--header 'Content-Type: application/json' \​

\--data '{​

"workflow_id": "749608044709****",​

"bot_id": "7496082951****",​

"parameters": {​

"volume": "100",​

"speed": "2",​

"name": "张三",​

"call_name": "宝贝xx",​

"ability": "",​

"personality": "",​

"custom_ability": "",​

"user_info": "",​

"birthday": "",​

"word_list": ""​

},​

"conversation_id": "7542845997404***",​

"additional_messages": [​

{​

"role": "assistant",​

"content": "宝贝成长路，金小葵守护。我是小葵，快来跟我聊天吧！",​

"content_type": "text"​

},​

{​

"role": "user",​

"content": "你刚刚说的题目正确答案是不是气球？",​

"content_type": "text"​

}​

],​

"ext": {​

"user_id": "e5e742c3-45a0-4984-bcd6-e6***"​

}​

}​

​

如有任何疑问或需要帮助，请联系扣子技术支持团队，我们将竭诚为你服务，协助你顺利完成参数校验的适配工作。​

​

​

上一篇

关于图像生成节点调整的公告

下一篇

扣子专业版更名公告