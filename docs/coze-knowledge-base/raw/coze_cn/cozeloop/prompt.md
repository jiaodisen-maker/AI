---
source_url: https://docs.coze.cn/cozeloop/prompt
title: '编写提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:00Z
---

# 编写提示词 - 文档 - 扣子

编写提示词

扣子罗盘提供了 Prompt 模板、Prompt 变量、AI 优化提示词等功能，帮助你快速生成符合业务需求的 Prompt。本文档介绍如何通过这些能力编写提示词。​

配置 Prompt 模板​

模板类型​

扣子罗盘提供 Normal 和 Jinja2 两种 Prompt 模板类型。默认为 Normal 类型，你也可以设置为 Jinja2 类型，这两种类型的区别如下：​

​

模板类型​| 说明​| 示例​  
---|---|---  
Normal​| 普通模板，支持简单的变量替换，包裹在双大括号 {{}} 中的内容将被自动定义为变量。​​| 

  * Prompt 模板内容：我的问题是“{{question}}”​

  * 变量内容：question=中国是什么类型气候 ​

  * 实际输入给模型的 Prompt：我的问题是“中国是什么类型气候”​

  
Jinja2​|  Jinja2 模板，允许在提示词中嵌入逻辑，使提示词能够根据上下文动态调整，适合在需要动态智能提示的场景（如聊天机器人、客服）下更灵活和高效地编写提示词。​

  * 支持 Jinja2 语法，可实现过滤器、条件判断等复杂的变量逻辑。​

  * 需要先在右侧变量区域添加变量，才能用双大括号 {{}} 引用变量。​

此外， Jinja2 模板还支持多种数据类型的 Prompt 变量，部分数据类型有一定格式要求。详细说明可参考​Jinjia2 模板变量数据类型。​| 

  * Prompt 模板内容：The title is {{title_variable|title}}. Please discuss it.​

  * 变量内容：title_variable为a simple question​

  * 实际输入给模型的 Prompt：The title is A Simple Question. Please discuss it.​

更多示例可参考​模板引擎语法示例。​  
  
​

在 Prompt 开发页面左侧的 Prompt 模板区域，选择模板类型。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27377%27%20height=%27246%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc3IiBoZWlnaHQ9IjI0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

Prompt 变量​

如果你希望在 Prompt 模板中插入动态的内容，可以通过 Prompt 变量实现。​

纯文本变量​

定义并添加 Prompt 变量的方式如下：​

​

模板类型​| 说明​| 示例​  
---|---|---  
Normal​| Normal 模板无需手动定义变量，直接在 Prompt 中输入变量格式即可。​在 Prompt 模板区域，直接输入变量格式和变量名称，例如 {{City}}。系统会自动识别变量格式，并在右侧的 Prompt 变量区域添加对应名称（例如 City）的变量。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271081%27%20height=%27497.74858757062145%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4MSIgaGVpZ2h0PSI0OTcuNzQ4NTg3NTcwNjIxNDUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
Jinja2​|  Jinja2 模板需要手动定义变量，然后才能在 Prompt 中引用这个变量。​

1.在 Prompt 变量区域中，单击新增变量。​

2.设置变量的名称、数据类型和变量值，并单击确认。​

3.在 Prompt 模板区域，输入变量格式和变量名称来引用这个变量，例如 {{Province}}。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271084%27%20height=%27496.06779661016947%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4NCIgaGVpZ2h0PSI0OTYuMDY3Nzk2NjEwMTY5NDciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

定义变量之后，你可以直接输入 {{，系统会提示你可以引用的变量列表。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27582%27%20height=%27257%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgyIiBoZWlnaHQ9IjI1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

说明

不同模板引擎定义变量的方式不一致，切换模板引擎可能导致之前定义的变量渲染失败。例如 Jinja2 模板切换为 Normal 模板之后，通过 Jinja2 语法定义的变量会被视为普通文本。​

​

多模态变量​

对于支持多模态输入的模型，你可以在 User prompt 和 Assistant Prompt 中添加多模态变量，支持图片和文字，可实现图文混排。​

说明

  * 仅 User prompt 和 Assistant Prompt 中添加多模态变量，System Prompt 和 Placeholder 中暂不支持。​

  * 添加多模态变量前，注意需要切换为支持多模态输入的模型，例如豆包视觉理解模型。​

​

添加并调试多模态变量的方式如下：​

1.

单击添加消息，在 User prompt 和 System Prompt 输入框的右上角单击图片图标。​

2.

根据页面提示输入变量名称，并单击确定。​

  * 添加成功后，Prompt 变量区域会展示此变量，可见多模态标识。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27318%27%20height=%27379%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE4IiBoZWlnaHQ9IjM3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在 Prompt 变量区域，找到新增的多模态变量，设置调试时使用的变量值。​

  * 单击添加数据，添加一个变量值，最多可添加 50 条。​

  * 多模态变量支持文本和图片两种类型的输入，其中图片类型支持本地上传图片文件，或者输入在线图片 URL。​

  * 文本：文本格式的内容。​

  * 图片（源文件）：本地上传图片文件，单张图片大小限制需遵循模型要求，例如豆包 VLM-1028 单图大小上限为 10M，支持一次上传多张图片。​

  * 图片（外链）：输入在线图片 URL。上传时扣子罗盘会校验 URL 有效性，开发者需自行保证所提供 URL 长期可用。如果上传的图片链接解析失败，可以检查 URL 是否以 http:// 或 https:// 开头、域名格式是否正确，或尝试更换其他 URL。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27367%27%20height=%27269%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY3IiBoZWlnaHQ9IjI2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在预览与调试区域输入问题，并单击运行，等待大模型回复。​

  * 例如下图中，通过思考内容可以判断出图片已被模型正常识别。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27590%27%20height=%27281%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTkwIiBoZWlnaHQ9IjI4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

自动优化提示词​

选中系统提示词文本框，然后单击右上角的一键优化图标。扣子罗盘会基于底层优化算法自动帮你改进系统提示词。​

说明

系统提示词是基础框架，直接影响模型的输出效果。设计良好的系统提示词能够显著提升模型的表现。建议使用扣子罗盘的一键优化能力，以提升系统提示词的质量和效果。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27688%27%20height=%27248.99999999999997%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg4IiBoZWlnaHQ9IjI0OC45OTk5OTk5OTk5OTk5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

如果你想使用优化后的版本，单击采纳；如果优化后的版本不符合预期，可以单击刷新按钮，重新优化。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27478%27%20height=%27311%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc4IiBoZWlnaHQ9IjMxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

消息列表​

当系统提示词无法满足复杂业务需求时，可以通过消息列表（MessageList）的方式来组织提示词。扣子罗盘支持 MessageList 形态的提示词模版托管。​

参考以下步骤添加更多提示词：​

1.

单击系统提示词区域下的 \+ 添加消息按钮。​

2.

单击文本框左上角的User，然后从下拉列表中选择要添加的提示词，并完成对应配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27222%27%20height=%27271%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIyIiBoZWlnaHQ9IjI3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 下表是扣子罗盘提示词模板支持的提示词消息，你可以根据实际应用场景选择合适的配置。​

  * 说明

下表中的回复均为 AI 生成，仅供参考。​

​

  * 对于内容摘要生成或创意文案撰写等单轮任务，配置系统提示词（System prompt）和用户提示词（User prompt）即可满足需求。​

  * 对于客服咨询或教育辅导等多轮对话任务，可引入助手回复（Assistant prompt）和占位符（Placeholder）以记录历史对话上下文，从而保证对话的连贯性和个性化。​

​

提示词​| 说明​| 示例​  
---|---|---  
系统提示词 (System prompt)​| 作用：定义模型的全局规则，用于指导模型的整体行为，例如角色设定、任务边界、输出格式要求等。​使用场景：系统提示词在所有对话开始时加载，持续影响后续交互。​| System prompt 示例：​​Markdown复制你是一名长沙旅游向导助手，需遵守以下规则： ​1\. 推荐内容需标注价格范围和地理位置（如“五一广场附近”）； ​2\. 若用户需求不明确，主动提问澄清。 ​3\. 使用中文回答用户问题，注意礼貌。​​  
用户提示词 (User prompt)​| 作用：用于接收用户动态请求，通常使用占位符{{query}} 绑定具体内容。​使用场景：当用户与 AI 应用进行交互时，他们提供的输入信息会被系统接收。系统会将提示中的占位符替换为用户的实际输入内容，从而生成完整的提示信息，然后将其发送给模型进行处理。​说明User prompt 的优先级高于 System prompt。​​| 

  * User prompt 示例：​

  * ​Markdown复制用户需求：{{query}} ​请按上述规则回答，并附上费用估算。 ​​

  * 用户提示词：“推荐五一广场附近的平价住宿”​

  * 替换后，发给模型的完整提示如下：​

  * ​Markdown复制用户需求：推荐五一广场附近的平价住宿 ​请按上述规则回答，并附上费用估算。 ​​

  
助手回复 (Assistant prompt)​| 作用：明确指导模型以特定角色、风格、格式或逻辑进行回应的提示内容。​使用场景：通常与用户的问题（User Prompt）配合使用，用于约束或引导模型的输出行为，使其更符合预期的应用场景。​| 以下是一个文案生成助手的 Prompt 模板配置示例。​

  * 系统提示词：​

  * ​Markdown复制你是一个电商客服，可以回答用户的问题。 ​​

  * 用户提示词：​

  * ​Markdown复制我的订单显示发货了，但一周还没收到，怎么办？ ​​

  * 助手回复：​

  * ​Markdown复制你现在是某电商平台的客服助手，需要以友好、专业的语气回应。首先安抚用户情绪，然后分步骤提供解决方案（如查询物流、联系快递、补发订单），最后主动询问是否需要进一步帮助。​​

模型会参考助手回复的内容，生成一个如下的输出：​​Markdown复制非常抱歉给您带来不便！您的包裹可能因物流高峰期有所延迟。建议您先通过订单页面查询物流单号和最新状态；若信息异常，我们可以帮您联系快递确认；若长时间未收到，我们将为您申请补发。请问需要为您转接物流查询服务吗？​​  
占位符 (Placeholder)​| 作用：用于记录历史对话记录，提供模型更多上下文信息。​使用场景：在多轮对话场景中，用户追问时，模型可以根据历史对话记录，准确生成回复内容。​配置说明：当在 Prompt 模板中添加 Placeholder 后，需要在右侧的 Prompt 变量区域，单击编辑 Placeholder 添加作为上下文历史内的对话历史。​​| 以下是一个客服场景的 Prompt 模板配置示例。​

  * 系统提示词：​

  * ​Markdown复制你是一名电信运营商智能客服，需要遵守以下规则：​1\. 准确识别用户问题类型（资费查询/故障报修/套餐变更）​2\. 每次回复需包含当前对话轮次标识​3\. 当用户问题不明确时，要求提供手机号码后四位验证身份​​

  * Placeholder 配置：​

  * ​Markdown复制{{chat_history}}​​

  * Prompt 变量中添加的 Placeholder 的对话历史：​

  * ​Markdown复制User: 我的网络突然不能用了​Assistant: 请问您的手机号码后四位是多少？我们需要先验证身份。​User：1389​Assistant: 1389尾号用户您好，检测到您家宽带处于离线状态，正在为您创建故障工单...​​

当用户提问工单号是多少时，模型回复如下所示：​​Markdown复制1389尾号用户您好，您当前的故障工单号是【CT20231115001】，已安排工程师尽快为您处理，预计2小时内修复。请保持手机畅通，以便工程师联系您。​​当用户进行追问时，通过占位符自动注入完整对话历史，保证了对话的连续性和回复的准确性。​  
  
​

配置模型​

在完成 Prompt 模板搭建后，接下来可以选择合适的模型来接收 Prompt 模板中的指令。​

参考以下步骤，选择并完成模型配置。​

1.

在 Prompt 开发页面，从模型配置下拉列表中选择要使用的模型。​

  * 你可以根据模型的描述信息和功能关键词来选择合适的模型。​

2.

配置模型参数。​

  * 最大回复长度：设置模型最多可以回复的 Token 数量。通常 100 Tokens 约等于 150 个中文汉字。​

  * 生成随机性：设置模型回复的创新性和多样性。取值范围为 0~1。数值越接近 1，表示模型的输出更具多样性和创新性，适用于小说、文案生成等场景；反之，数值降低时，输出内容会更加遵循指令要求，减少多样性，适用于需要精确回答的场景。​

  * Top P：设置模型的累计概率。在生成输出时，模型会从概率最高的词汇开始选择，直到这些词汇的总概率累积达到 Top P 值。这样可以限制模型只选择这些高概率的词汇，从而控制输出内容的多样性。​

  * 说明

    * 不同模型可配置的参数可能不同，请以界面上支持的配置为准。​

    * 不建议同时调整 Top P 和生成随机性，这可能会导致输出结果不稳定或不符合预期。建议根据具体需求选择其中一个进行调整。​

​

配置函数​

选择支持 Function Call 的模型后，可以使用插入函数功能来模拟函数调用。当前，扣子罗盘并不会实际调用定义的函数，而是根据模型的输出模拟调用过程返回预期的函数结果，以便继续执行用户指令。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27443%27%20height=%2760%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQzIiBoZWlnaHQ9IjYwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

参考以下步骤，配置模拟函数调用：​

1.

在 Prompt 开发页面的模型配置区域下，单击 +新增函数。​

2.

在新增函数窗口，完成函数配置。​

a.

在左侧的函数面板中定义函数配置，包括函数的名称（name）、描述（description）以及参数定义（parameters）。可单击使用模板根据模板定义函数。​

b.

在右侧的模拟值面板中输入模拟的返回值。​

  * 由于上一步函数的执行结果会影响下一步模型的决策，为了便于快速验证，可以为函数添加模拟返回值，从而高效测试多步函数调用流程。​

c.

单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27571%27%20height=%27369%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcxIiBoZWlnaHQ9IjM2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

保存函数配置后，系统会自动启用这个函数，并开启单步调用模式。你也可以根据实际需求进行调整：​

  * 启用函数：启用后，调试过程中将模拟函数调用，输出函数返回结构。​

  * 单步调试：​

  * 单步调试模式下会逐步执行模型的函数调用，并支持修改模拟值。通过这种方式，你可以更详细地了解模型的执行过程及其影响。​

  * 非单步模式：在非单步模式下，系统会一次性返回大型模型的函数调用和最终结果，整个过程更为简洁。​

4.

重复上述步骤，添加更多函数。​

至此，你就完成了提示词的设计和编写。接下来，你就可以在扣子罗盘进行 Prompt 调试，验证输出效果是否符合预期。​

相关信息​

模板引擎语法示例​

​

模板引擎​| ​| 变量注入​| 提示词结构​  
---|---|---|---  
Normal 模板引擎​| ​| 支持简单占位符以供静态变量注入。​例如：​

  * 模板：我的问题是：{{question}}​

  * 变量输入 ：question=中国是什么类型气候 ​

  * 传递给模型：我的问题是：中国是什么类型气候​

| 提示结构固定。​

  * 场景：构建一个多轮对话的AI助手，目标是当对话历史较长（比如超过3轮）时，在提示中加入对历史对话的总结。​

  * 解法：普通模板引擎不支持条件判断和复杂逻辑，必须在 Prompt 外部处理逻辑，然后将处理后的字符串传入 Prompt。​

  
Jinja2 模板引擎​| 条件判断​| 支持变量的复杂逻辑/计算，如条件分支/循环/过滤器等。​例如：​

  * 模板：​

{% if include_hint %}温馨提示：{{hint_variable}}​{% endif %}。​我的问题是：{{question}}​

  * 变量输入：include_hint=True，hint_variable=想想中国地理知识，question=中国是什么类型气候​

  * 传递给模型：​

温馨提示：想想中国地理知识。​我的问题是：中国是什么类型气候​| 实时根据上下文调整提示结构。​示例效果如下：​

  * 场景：构建一个多轮对话的AI助手，目标是当对话历史较长（比如超过3轮）时，在提示中加入对历史对话的总结​

  * 解法：在 Prompt 中根据上下文动态生成不同的提示结构​

​Django复制{% if history|length > 3 %} ​ 以下是对话的总结：{{ summarize_history(history) }} ​ 请根据以上总结继续对话。​{% else %} ​ 对话历史： ​ {% for turn in history %} {{ turn.role }}: {{ turn.content }} ​ {% endfor %}​{% endif %}​用户最新输入：{{ new_input }}​​  
​| 循环​| 

  * 模板：​

{% for choice in choices %}选项{{loop.index}}：{{choice}}​{% endfor %}​你认为哪个选项最合适？​

  * 变量输入：choices=['热带', '亚热带', '温带']​

  * 传递给模型：​

选项1：热带​选项2：亚热带​选项3：温带​你认为哪个选项最合适？​| ​  
​| 过滤器​| 

  * 模板：标题是{{title_variable|capitalize}}。请对此展开讨论。​

  * 变量输入：title_variable=brief introduction to chinese culture​

  * 传递给模型：标题是Brief Introduction To Chinese Culture。请对此展开讨论。​

| ​  
  
​

Jinja2 模板变量数据类型​

Jinja2 模板引擎中，Prompt 变量支持以下多种数据类型。​

​

数据类型​| 说明​| 示例​  
---|---|---  
String​| 字符串类型​| "Hello World"​  
Integer​| 整数类型​必须是 Int64 范围​| 42​  
Float​| 浮点数类型​

  * Float64 范围​

  * 最多支持 4 位小数​

| 3.1415​  
Boolean​| 布尔类型​| True / False​  
Object​| 对象类型​

  * 符合 JSON 格式的对象​

  * 最多支持三层嵌套​

  * 不支持自引用​

| {"name": "张三", "age": 30}​  
Array<String>​| 字符串数组​

  * 符合 JSON 格式的数组​

  * 元素数量不超过 100 个​

| ["苹果", "香蕉", "橙子"]​  
Array<Integer>​| 整数数组​

  * 符合 JSON 格式的数组​

  * 元素数量不超过 100 个​

| [1, 2, 3, 4, 5]​  
Array<Float>​| 浮点数数组​

  * 符合 JSON 格式的数组​

  * 元素数量不超过 100 个​

| [1.1, 2.2, 3.3]​  
Array<Boolean>​| 布尔值数组​

  * 符合 JSON 格式的数组​

  * 元素数量不超过 100 个​

| [true, false, true]​  
Array<Object>​| 对象数组​

  * 符合 JSON 格式的数组​

  * 元素数量不超过 100 个​

| [{"id": 1, "name": "张三"}, {"id": 2, "name": "李四"}]​  
  
​

上一篇

开发提示词

下一篇

调试提示词