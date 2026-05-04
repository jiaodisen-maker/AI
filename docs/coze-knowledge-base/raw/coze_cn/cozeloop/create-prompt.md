---
source_url: https://docs.coze.cn/cozeloop/create-prompt
title: '开发提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:56Z
---

# 开发提示词 - 文档 - 扣子

开发提示词

在开发 AI 应用过程中，编写高质量的提示词（Prompt）是重要任务之一。合理的提示词设计和模型配置，可以充分发挥模型的潜力，实现更智能、更灵活的应用场景。扣子罗盘提供了系统化能力帮助你快速编写并调试提示词，以满足业务需求。​

  * 本文中的模型指代大语言模型。​

  * 本文中使用的输出示例由豆包模型返回，仅供参考。​

流程介绍​

扣子罗盘提供了完整的提示词开发流程：​

1.

创建提示词：首先，你需要在指定空间下创建一个提示词。​

2.

设计和编写提示词：接下来，使用 Prompt 模板来构建适用于不同应用场景（例如分类、总结、问答等）的提示词。​

3.

调试和优化：在完成 Prompt 模板搭建后，通过调整模型参数、插入函数和变量等方式进行模拟调用，检查输出是否符合预期。同时，支持比较多个模型的表现，以选择最适合的模型。​

4.

发布提示词：最后，提交调试后的提示词，保存版本记录。后续，可针对不同版本的提示词进行评测或通过 SDK 获取提示词配置。​

步骤一：创建 Prompt​

首先，你需要创建一个 Prompt。 你可以选择自定义创建，也可以基于扣子罗盘提供的提示词模板创建，两种方式都能帮助你快速开启提示词的开发工作。 ​

自定义创建​

如果你希望创建一个空的 Prompt，从零开始编写自己的 Prompt，可以在创建 Prompt 时选择自定义创建。操作步骤如下：​

1.

登录[扣子罗盘](<https://loop.coze.cn/console>)，然后在左侧导航栏，选择 Prompt 工程 > Prompt 开发。​

2.

在打开的 Prompt 开发页面，单击 \+ 创建Prompt > 自定义创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272884%27%20height=%27527.4774346793349%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/12719ff0195e41c4a12ddda90776ba37~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

在 创建 Prompt 对话框，输入 Prompt 的 Key、名称和描述，然后单击确认。​

  * 注意

    * Prompt Key 是提示词的唯一标识符，同一空间内的 Prompt Key 不能相同。​

    * Prompt 创建后，Prompt Key 无法修改。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27383%27%20height=%27194%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgzIiBoZWlnaHQ9IjE5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

基于模板创建​

为便于开发者快速创建常见场景的 Prompt，扣子罗盘提供了 Prompt 模板，涵盖数据分析、营销文案等多种行业和应用场景，你可以根据实际需求选择合适的模板来创建 Prompt。 ​

参考以下步骤，基于模板创建 Prompt。​

1.

登录[扣子罗盘](<https://loop.coze.cn/console>)，然后在左侧导航栏，选择 Prompt 工程 > Prompt 开发。​

2.

在打开的 Prompt 开发页面，单击 \+ 创建Prompt > 基于模板创建。​

3.

在 Prompt 模板列表中选择一个 Prompt，单击使用。​

  * 扣子罗盘将使用该模板为你创建一个新的 Prompt，并引导你填写基础信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27460%27%20height=%27319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYwIiBoZWlnaHQ9IjMxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 如果发现感兴趣的模板，单击预览即可快速查看 Prompt 模板内容、并且快速调试 Prompt 效果。如果模板符合你的需求，在调试区域右上角单击快捷创建，即可使用这个模板创建一个新的 Prompt。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27423%27%20height=%27220%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIzIiBoZWlnaHQ9IjIyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：设计和编写 Prompt​

完成 Prompt 创建后，你将进入到 Prompt 开发页面。在这里，你需要设计和编写 Prompt。你可以在 Prompt 模板区域，编写 Prompt内容。​

Prompt 模板默认为 Normal 模式的系统提示词（System Prompt），你也可以切换模板模式。系统提示词定义模型的全局规则，用于指导模型的整体行为。例如，角色设定、任务边界、输出的格式要求等。你也可以输入一段简短的 Prompt，由 AI 帮你优化。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27837%27%20height=%27384%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODM3IiBoZWlnaHQ9IjM4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

此外，扣子罗盘还提供多种 Prompt 编排能力，帮助你快速完成高质量的 Prompt 编写，例如：​

  * Prompt 模板： Prompt 模板是一种格式化结构，用于组织提示词。它通过固定指令格式、动态变量占位符和上下文规则，确保模型在不同任务中生成一致且可控的输出。​

  * 模型配置：扣子罗盘提供业内领先的多种模型供你选择，支持调整模型配置以控制输出风格和内容长度。​

  * 函数调用：对于支持使用工具的模型，扣子罗盘支持配置函数，模拟函数调用过程，方便更好地评估提示词效果。​

详细说明，可参考​编写提示词。​

步骤三：调试 Prompt 效果​

编写提示词之后，你可以在预览与调试区域输入用户问题，进行 Prompt 调试，验证输出效果是否符合预期。调试过程中，你可以随时修改 Prompt 来测试模型输出的效果。​

为了更好地演示调试操作，本文以一个旅行助手为例。在这个示例中，我们使用了一个天气函数，并开启了单步调试。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27809%27%20height=%27371%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODA5IiBoZWlnaHQ9IjM3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

以普通调试模式为例，你可以在 Prompt 开发页面的预览与调试区域，直接输入一个指令，然后单击运行；或者在 Prompt 变量中输入指令信息，然后直接单击运行。​

方式一：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272732%27%20height=%271540.7962085308059%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjczMiIgaGVpZ2h0PSIxNTQwLjc5NjIwODUzMDgwNTkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

方式二：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272736%27%20height=%271543.052132701422%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjczNiIgaGVpZ2h0PSIxNTQzLjA1MjEzMjcwMTQyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

因为开启了单步调试模式，所以可以在调试过程中，手动修改函数的模拟返回值。这里，我们将上海的天气改为Rainy。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27289%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg5IiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

以下是模型的回复内容，我们可以看到模型有关注到天气对出行的影响，并给了带雨具的建议，是符合预期的。​

以下内容由 AI 生成，仅供参考。​

​

Markdown

复制

好的，以下是我为你提供的一份周日在上海的游玩计划：​

上午：​

- 早餐：去生煎店品尝特色小吃生煎包，或者逛逛周边的特色早餐店。​

- 游览上海博物馆：这是一座大型的中国古代艺术博物馆，收藏了大量的珍贵文物和艺术品，可以感受历史文化的魅力。​

- 前往南京路步行街：在这里可以逛街购物、感受上海的繁华，并品尝各种美食。​

...​

请注意，由于天气原因，在游玩过程中请携带雨具，并根据实际情况调整行程。希望你在上海度过一个愉快的周日！​

​

关于 Prompt 调试模式的详细说明，可参考​调试提示词。​

步骤四：提交并管理 Prompt ​

当完成 Prompt 调试与优化，模型可以输出预期结果后，可提交当前的 Prompt 配置，并生成一个版本号。后续，可以选择指定的 Prompt 版本进行效果评测和链路追踪。发布版本后如何管理提示词版本，可参考​管理提示词版本。​

1.

在 Prompt 开发页面，单击提交新版本。​

2.

在弹出的对话框中，确认版本号，设置版本标识和版本说明，然后单击提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27397%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk3IiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 当后续对 Prompt 进行修改、调试后，你可以继续提交新版本。在提交新版本时，系统会展示最新版本与上一个版本的差异。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27260%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI0IiBoZWlnaHQ9IjI2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

后续操作​

至此，你已经完成 Prompt 的开发。接下来你可以：​

  * 对 Prompt 效果进行评估，参考​评测入门教程。​

  * 实时观测 Prompt 消息链路，参考​查看 Trace 数据。​

  * 接入扣子罗盘 SDK，获取 Prompt 配置。参考​SDK 概述。​

上一篇

什么是提示词？

下一篇

编写提示词