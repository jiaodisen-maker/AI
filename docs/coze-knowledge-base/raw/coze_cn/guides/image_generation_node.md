---
source_url: https://docs.coze.cn/guides/image_generation_node
title: '图像生成节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:38Z
---

# 图像生成节点 - 文档 - 扣子

图像生成节点

低代码工作流中的图像生成节点用于生成图片。通过图像生成节点，你可以将一段文字转为图片，也可以根据参考图生成图片。​

节点说明​

在 AI 智能处理场景下，我们通常使用文生图的方式调用大模型节点来生成图像，如果模型生成效果不符合预期，则通过一系列关键词和参数调整细节。但对话方式处理图像通常存在以下问题：​

  * 过程繁琐、保密性低，不适合批量的图像生成和处理。​

  * 普通开发者也可能不熟悉图像处理的模型参数及其效果，反复调试非常耗时。​

为了更高效地生成图像，建议你使用图像生成节点来生成图像。它不仅能生成单张图片，还可以配合​循环节点进行批量处理。目前，扣子编程提供了丰富的生图模型，例如能够灵活应对复杂的多模态生成任务的 Seedream 4.0、 Seedream 4.5、Seedream 5.0 Lite 模型、专用于动漫场景的动漫模型、面部处理更加细致自然的人像模型等，你可以选择不同的模型，分别试运行体验模型效果。​

注意

  * 在扣子账号（主账号+子账号）维度下，图像生成节点的并发限制为 4，建议合理控制调用频率。​

  * 图像处理插件输出的图片为链接格式，有效期为 1 年，建议在到期前及时保存。​

​

说明

前往[图像生成器模板](<https://www.coze.cn/template/project/7442540084944994344>)可直接体验图像模型的生图效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%27347%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/000cb37085d34f1593f15eb347d5de17~tplv-goo7wpa0wc-quality:q75.image)​

​

​

费用说明​

使用图像生成节点时，选择不同的模型将对应不同的计费项。具体的价格及免费额度说明，请参考​插件费用。​

​

模型​| 计费项​  
---|---  
Seedream 5.0 Lite​| 

  * 文生图-Seedream 5.0​

  * 图生图-Seedream 5.0​

  
Seedream 4.5​| 

  * 文生图-Seedream 4.5​

  * 图生图-Seedream 4.5​

  
Seedream 4.0​| 

  * 文生图-Seedream 4.0​

  * 图生图-Seedream 4.0​

  
Seedream 3.0​| 文生图-Seedream 3.0​  
其他生图模型​| 图像生成​  
  
​

配置图像生成节点​

模型设置​

选择用于生成图片的模型，并设置图像比例等参数。不同模型对应的配置参数不同，以实际界面为准，重要参数说明如下：​

Seedream 系列生图模型

其他生图模型

  * 模型：Seedream 5.0 Lite、Seedream 4.5、Seedream 4.0、Seedream 3.0​

  * 关于 Seedream 5.0 Lite、Seedream 4.5、Seedream 4.0 模型的更多使用案例，请参考​Seedream 模型生图教程。​

  * 联网搜索：Seedream 5.0 Lite 模型支持联网搜索能力。​

  * 开启联网搜索后，模型会根据提示词自主判断是否搜索互联网内容（如商品、天气等），提升生成图片的时效性，但也会增加一定的时延。​

  * 比例：设置生成的图像尺寸。你可以选择预设的常用尺寸或进行自定义。​

  * Seedream 5.0 Lite 模型：支持通过宽高或分辨率指定尺寸，两者不支持同时生效。​

  * 宽高：设置自定义宽高时，需满足宽高比在 1/16～16 之间，且宽高总像素值在 3686400～10404496 范围内。例如你可以指定高为 2048，宽为 2048。​

  * 分辨率：支持 2K 或 3K。​

  * Seedream 4.5 模型：支持通过宽高或分辨率指定尺寸，两者不支持同时生效。​

  * 宽高：设置自定义宽高时，需满足宽高比在 1/16～16 之间，且宽高总像素值在 3686400～16777216 范围内。例如你可以指定高为 2048，宽为 2048。​

  * 分辨率：支持 1K、2K 或 4K。​

  * Seedream 4.0 模型：支持通过宽高或分辨率指定尺寸，两者不支持同时生效。​

  * 宽高：设置自定义宽高时，需满足宽高比在 1/16～16 之间，且宽高总像素值在 921600～16777216 范围内。例如你可以指定高为 2048，宽为 2048。​

  * 分辨率：支持 2K 或 4K。​

  * Seedream 3.0 模型支持的宽高范围为 512～2048 像素。​

  * 图片水印：打开开关，系统将在生成的图片上添加AI生成字样的水印。​

  * 最多生成图片数量：用于控制 Seedream 4.0、Seedream 4.5、Seedream 5.0 Lite 模型单次生成的图片数量，最大值为 15。参考图数量和生成的图片数量总和需在 15 张以内。如果需要生成多张图片，则需在提示词中指定图片数量。​

​

参考图​

生成图像的参考图，支持设置多个参考图。不同模型对应的配置参数不同，以实际界面为准，重要参数说明如下：​

Seedream 系列生图模型

其他生图模型

参考图：为模型提供参考图，可以上传本地图片，也可以引用上游节点输出的图片。​

​

输入​

提示词中可使用的输入参数，用于动态传入内容。输入参数可以指定为一个固定值，也可以引用上游节点的输出。​

提示词​

图像模型的提示词，用于下达图像生成相关的指令，也就是你对画面的描述。提示词中只需要输出正向和负向的关键词即可。支持引用输入中定义的变量，引用方式为{{变量名}}。​

  * 正向提示词：即 positive prompt，必选。用于描述你想要出现在画面中的内容，例如 1girl,necklace, jewelry,best quality,。​

  * 负向提示词：即 negative Prompt，可选。用于描述你的画面中不想生成的内容，例如 watermark, long neck, missing fingers, extra arms,worst quality, low quality, normal quality,。同时扣子也预设了一系列负向提示词，包括 nsfw,nude,blurry,watermark,identifying mark, low resolution,mutated,lack of hierarchy。​

输出​

节点的输出参数固定为以下参数：​

  * data：Image 格式的图像，即模型生成的图像。通常是一个公开可访问的 URL 链接。​

  * msg：节点执行状态，success 表示执行成功。​

  * errorBody：节点执行失败时的详细信息，包括 errorMessage 和 errorCode。​

  * isSuccess：节点执行状态，true 表示执行成功，false 表示执行失败。​

其中isSuccess、errorBody 仅在节点的异常处理方式设置为返回设定内容或执行异常流程时返回，用于节点执行异常时传递详细信息。​

异常设置​

默认情况下，节点运行超时、运行异常时，工作流会中断，工作流调试界面或 API 中会返回错误信息。你也可以手动设置节点运行超时等异常情况下的处理方式，例如整体执行超时、是否重试、是否跳转异常分支等。​

​

异常处理设置​| 说明​  
---|---  
整体执行超时​| 整体执行超时是指节点运行的最大耗时，如果超过此时长，则判断为该节点运行超时。​默认情况下，节点的超时时间为 600s，即 10 分钟。你也可以将其改为 0.1s~600s，灵活控制超时时间。​  
重试次数​| 节点运行超时或异常时，默认不重试，你也可以设置为重试 1 次。​  
异常处理方式​| 节点运行超时或异常时，默认中断工作流。你也可以手动修改此节点的异常处理方式：​

  * 中断流程：工作流执行中断，不再运行后续节点。​

  * 返回设定内容：发生异常后，工作流运行不会中断。开发者可自定义设置需要返回的输出字段内容，必须是输出中已定义的字段，且格式为合法的 JSON 格式。另外，节点还会返回输出参数 isSuccess、errorBody，传递节点异常的详细信息。​

  * 执行异常流程：发生异常后，工作流运行不会中断，转而执行异常流程分析，开发者需要为新增的异常分支配置处理流程。异常信息会通过节点的输出参数 isSuccess、errorBody 返回。​

  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27384%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg0IiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例​

文生图​

通过文字描述生成一张动漫风格的图片。模型选择动漫，引用开始节点的用户原始输入作为正向提示词，并添加一系列正向的关键词作为提示词。负向提示词为 low quality，表示避免低质量图像。节点配置及试运行结果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27476%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc2IiBoZWlnaHQ9IjI1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

图生图​

通过参考图片生成一张相同人物造型和姿势的动漫图片。模型选择动漫，参考图上传一张想要的人物造型与动作图片。引用开始节点的用户原始输入作为正向提示词。负向提示词为 low quality，表示避免低质量图像。节点配置及试运行结果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27460%27%20height=%27253%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYwIiBoZWlnaHQ9IjI1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

Seedream 4.0 ​

例如，搭建一个图像生成智能体，该智能体绑定了对应的图像生成工作流。当用户输入详细的生图提示词、参考图后，智能体会自动调用工作流生成图像。请参考​Seedream 模型生图教程。​

​

上一篇

长期记忆检索节点

下一篇

画板节点