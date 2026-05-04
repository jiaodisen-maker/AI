---
source_url: https://docs.coze.cn/developer_guides/nodejs_getting_started
title: '快速开始 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:25:28Z
---

# 快速开始 - 文档 - 扣子

快速开始

本文介绍如何使用 Node.js SDK 完成扣子编程的常用操作。例如初始化 Node.js SDK、创建一个智能体草稿、发布智能体为 API 服务、和智能体对话等。​

准备工作​

  * 已安装 Node.js SDK。更多信息，可参见​安装 Node.js SDK。​

  * 已实现授权流程，并通过环境变量方式配置了访问密钥。详细说明可参考​配置访问密钥。​

初始化 Node.js SDK​

初始化 Coze client 之后，才可以向扣子编程服务端发送 OpenAPI 请求。初始化时推荐通过环境变量动态获取访问密钥，以免硬编码引发数据安全风险。​

初始化代码如下：​

​

JavaScript

复制

import { CozeAPI, COZE_CN_BASE_URL } from '@coze/api';​

​

// Import token using the environment variable​

const token = process.env.COZE_API_TOKEN || "input your coze api token"​

​

// Instantiate Coze API client​

const client = new CozeAPI({​

baseURL: COZE_CN_BASE_URL,​

token: token,​

});​

​

创建并发布智能体为 API 服务​

通过 API 方式和智能体对话之前，需要先创建一个智能体，并将其发布为 API 服务。可以在扣子编程中创建智能体并发布，也可以通过调用相关的 API 实现。调用 API 创建智能体时，部分配置对应的 API 参数暂未开放，只能为智能体添加知识库等有限的配置。创建智能体的操作步骤可参考​搭建一个 AI 助手智能体，将智能体发布为 API 服务的操作步骤可参考​发布智能体为 API 服务。​

  * 创建智能体的完整示例代码，参见 [GitHub 示例](<https://github.com/coze-dev/coze-js/blob/main/examples/coze-js-node/src/bot.ts>)。​

  * 相关 API 接口描述，请参见：​

  * ​创建智能体。​

  * ​发布智能体。​

示例代码如下：​

​

JavaScript

复制

import { CozeAPI, ChatEventType, ChatStatus, COZE_CN_BASE_URL } from '@coze/api';​

​

const token = process.env.COZE_API_TOKEN;​

const spaceId = process.env.COZE_SPACE_ID;​

const baseURL = COZE_CN_BASE_URL;​

​

const client = new CozeAPI({​

baseURL,​

token,​

});​

​

// Invoke the create API to create a bot in the draft status.​

const bot = await client.bots.create({​

space_id: spaceId,​

name: '翻译专家',​

description:​

'能帮你进行中英互译的专业翻译人员',​

prompt_info: {​

prompt:​

'你是一名翻译人员，请将以下文本从英语翻译成汉语',​

},​

});​

​

​

// Call the publish API to publish the bot on the API channel.​

const publishedBot = await client.bots.publish({​

bot_id: bot.bot_id,​

connector_ids: ['API'],​

});​

​

发起对话 ​

​发起对话接口用于向指定智能体发起一次对话。支持在对话时添加对话的上下文消息，以便智能体基于历史消息做出合理的回复。开发者可以按需选择响应方式，即流式或非流式响应。响应方式决定了开发者获取智能体回复的方式。​

  * 流式响应：智能体在生成回复的同时，将回复消息以数据流的形式逐条发送给客户端。处理结束后，服务端会返回拼接后完整的智能体回复。详细说明可参考​流式响应。 ​

  * 非流式响应：无论对话是否处理完毕，立即发送响应消息。开发者可以通过接口​查看对话详情口确认本次对话处理结束后，再调用​查看对话消息详情接口查看模型回复等完整响应内容。详细说明可参考​非流式响应。​

本文档以流式响应为例，演示通过 API 方式和智能体对话相关实例代码。可以查看 Node.js SDK [示例代码目录](<https://github.com/coze-dev/coze-js/tree/main/examples>)，查看 chat 接口的其他实现方式。例如，非流式响应、对话中发送多模态内容等。​

示例代码如下：​

​

JavaScript

复制

import { CozeAPI, ChatEventType, ChatStatus, COZE_CN_BASE_URL, RoleType } from '@coze/api';​

​

const token = process.env.COZE_API_TOKEN;​

const botId = process.env.COZE_BOT_ID;​

const baseURL = COZE_CN_BASE_URL;​

​

const client = new CozeAPI({​

baseURL,​

token,​

});​

​

​

const stream = await client.chat.stream({​

bot_id: botId,​

additional_messages: [​

{​

role: RoleType.User,​

content: '你好',​

content_type: 'text',​

},​

],​

});​

​

for await (const part of stream) {​

if (part.event === ChatEventType.CONVERSATION_MESSAGE_DELTA) {​

process.stdout.write(part.data.content); // Real-time response​

}​

}​

​

​

上一篇

配置访问密钥

下一篇

Java SDK 概述