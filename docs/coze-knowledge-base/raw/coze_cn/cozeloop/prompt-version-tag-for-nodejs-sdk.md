---
source_url: https://docs.coze.cn/cozeloop/prompt-version-tag-for-nodejs-sdk
title: '通过版本标识拉取 Prompt 版本 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:29Z
---

# 通过版本标识拉取 Prompt 版本 - 文档 - 扣子

通过版本标识拉取 Prompt 版本

扣子罗盘 SDK 支持通过版本标识拉取指定 Prompt 版本。​

使用方式​

在扣子罗盘中提交 Prompt 版本时，如果设置了版本标识，即可在 SDK 中通过 getPrompt 方法指定 prompt_key 和 label 来获取该版本的 Prompt 详细信息。​

说明

  * getPrompt 方法中version参数优先级高于label。 例如 Prompt 提交了两个版本（0.0.1 和 0.0.2），其中 0.0.2 版本添加了production标识，以下代码最终会获取 0.0.1 版本 Prompt，而不是production标识对应的 0.0.2 版本。​

  * ​

TypeScript

复制

const prompt = await hub.getPrompt('prompt_hub_test', '0.0.1', 'production');​

​

  * Version和Label参数均为空时，会获取最新提交版本的 prompt。​

​

通过版本标识获取指定 Prompt 的示例代码如下：​

​

TypeScript

复制

import { PromptHub } from '@cozeloop/ai';​

​

const hub = new PromptHub({​

/** workspace id, use process.env.COZELOOP_WORKSPACE_ID when unprovided */​

// workspaceId: 'your_workspace_id',​

apiClient: {​

// baseURL: 'api_base_url',​

// token: 'your_api_token',​

},​

});​

​

// get prompt with `beta` label​

// - prompt_key: xxx​

// - version: undefined​

// - label: beta​

const prompt = await hub.getPrompt('xxx', undefined, 'beta');​

​

// format prompt with variables​

const messages = hub.formatPrompt(prompt, {​

var1: 'value_of_var1',​

var2: 'value_of_var2',​

var3: 'value_of_var3',​

placeholder1: { role: 'assistant', content: 'user' },​

});​

​

上一篇

最佳实践

下一篇

调用 Prompt