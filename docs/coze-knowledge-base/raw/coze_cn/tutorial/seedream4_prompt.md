---
source_url: https://docs.coze.cn/tutorial/seedream4_prompt
title: 'Seedream 模型生图教程 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:12Z
---

# Seedream 模型生图教程 - 文档 - 扣子

Seedream 模型生图教程

Seedream 4.0 及更高版本均支持高达 4K 高清精美图像生成，能够帮助用户高效生成/编辑高质量图像，解决复杂多模态创作需求。本文将介绍该系列模型的生图效果与各版本迭代升级亮点，并提供了详细的教程，指导你搭建生图工作流和智能体。​

模型概览​

为了帮助你根据具体需求快速选择最合适的模型，下表直观展示了 Seedream 4.0、4.5 及 5.0 Lite 的核心特性。​

​

模型名称​| ​| Doubao-Seedream-5.0-lite​| Doubao-Seedream-4.5​| Doubao-Seedream-4.0​  
---|---|---|---|---  
文生图​| ​| ✔️​| ✔️​| ✔️​  
生成组图​| ​| ✔️​| ✔️​| ✔️​  
图像编辑​| ​| ✔️​| ✔️​| ✔️​  
联网搜索​| ​| ✔️​| ➖ ​| ➖ ​  
模型参数​| 分辨率​| 2K, 3K​| 2K, 4K​| 1K, 2K, 4K​  
​| 输出格式​| png, jpeg​| jpeg​| jpeg​  
模型迭代亮点​| ​| 具备联网实时检索、编辑精准可控、智能逻辑推理三大升级亮点。​| 人像场景效果、画面美观度、一致性、编辑准确度等方面均有提升。​| 首次支持多模态生图，支持文生图、图像编辑、生成组图。能够通过自然语言灵活控制画面细节。​  
  
​

说明

输入的参考图数量 + 最终生成的图片数量 ≤ 15张​

​

模型迭代亮点​

Seedream 5.0 Lite​

与 Seedream 4.5 相比，Seedream 5.0 Lite 具备联网实时检索、编辑精准可控、智能逻辑推理三大升级亮点。​

  * 联网实时搜索​

  * 首次支持检索生图功能，能够融合实时网络信息，提升生图时效性。​

  * ​

指令​| 效果图（开启联网）​| 效果图（关闭联网）​  
---|---|---  
​Plain Text复制制作一张杭州未来5日的天气预报图，采用现代扁平化插画风格，清晰展示每日天气、温度和穿搭建议。 整体为横向排版，标题为“杭州未来5日天气预报”，包含5个等宽的垂直卡片，从左到右依次排列。 整体风格为现代、干净、友好的扁平化矢量插画风格，线条清晰，色彩柔和。 人物形象采用年轻男女的卡通插画，表情自然，姿态放松，服装细节清晰。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272048%27%20height=%272048%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA0OCIgaGVpZ2h0PSIyMDQ4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27177%27%20height=%27177%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc3IiBoZWlnaHQ9IjE3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

  * 编辑精准可控​

  * 生成图像与输入文本的契合度提升，能够精准响应复杂指令需求。​

  * ​

  * 智能逻辑推理​

  * 更懂现实规律，支持复杂的逻辑推演与多步推理需求，并且内置了垂直行业专业知识库。​

  * ​

Seedream 4.5​

与 Seedream 4.0 相比，Seedream 4.5 在人像场景效果、画面美观度、一致性、编辑准确度等方面均有提升。​

  * 人像场景效果优化​

  * ​

  * 美观度提升​

  * ​

  * 编辑准确度提升​

  * ​

Seedream 4.0​

首次支持多模态生图，支持文生图、图像编辑、生成组图。​

​

基本能力​

元素增删​

​

改变风格​

​

改变光影&色调​

​

改变材质&背景​

​

改变视角&景别​

​

海报编辑​

​

生成效果​

设计​

​

知识科普​

​

修改图片​

​

生成写真​

​

多图融合​

​

制作插画​

​

画面构图​

​

工作流与智能体应用​

本教程的核心是借助图像生成节点中的 Seedream 4.0 模型，构建了一个定制化的图像生成工作流。在此基础上，进一步搭建了一个生图智能体，该智能体绑定了上述工作流。当用户输入详细的生图提示词和参考图后，智能体会自动调用工作流生成图像，并以卡片形式返回图像。使用该智能体时，用户无需操作复杂的生图流程，仅通过与智能体对话，便能轻松生成符合需求的图像。​

低代码工作流​

工作流说明​

该工作流旨在调用 Seedream 4.0 模型，基于用户提供的生图提示词和参考图，快速生成所需的图像。包括如下节点：​

1.

开始节点：接收用户输入的关键信息，包括图像生成提示词和参考图。本教程定义了最多可以上传 3 张参考图，这些参考图将为 Seedream 4.0 提供具体的视觉参考，帮助生成更贴近需求的图像。​

  * 在提供提示词时，建议尽量详细且准确，以便更好地引导 Seedream 4.0 模型生成符合预期的图像。提示词的描述示例，请参考​生成效果。​

2.

图像生成节点：Seedream 4.0 模型将基于用户提供的生图提示词和参考图，批量生成图像。Seedream 4.0 模型支持生成多张图像，本教程定义了单次最多可生成 15 张图像。生成的图片越多，生成的时间越长。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27767%27%20height=%27396%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzY3IiBoZWlnaHQ9IjM5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

核心节点说明​

各个节点的配置详情如下：​

​

低代码智能体​

搭建好图像生成工作流后，还需要搭建一个生图智能体。首先，在智能体中定义好智能体的角色和技能，确保它能够精准地理解并执行生图工作流。然后在智能体中绑定已创建好的生图工作流，并为工作流添加卡片。当用户输入生图提示词和参考图后，智能体会立即调用工作流生成图像，并以卡片形式返回生成的图像。​

​

搭建完成后，你可以在智能体调试页面，输入生图提示词和参考图，智能体将调用工作流生成新图片并返回。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27639%27%20height=%27306%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM5IiBoZWlnaHQ9IjMwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

小红书制图工厂

下一篇

情感陪聊