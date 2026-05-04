---
source_url: https://docs.coze.cn/guides/question_node
title: '问答节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:35:08Z
---

# 问答节点 - 文档 - 扣子

问答节点

低代码工作流中的问答节点用于主动收集用户的信息、获取用户意图。​

节点说明​

低代码工作流中的某些节点依赖用户的信息输入或明确意图，问答节点会以自然语言问题或选项的方式收集指定的信息，让对话更加顺畅。在低代码项目中，如果智能体对话中触发了包含问答节点的工作流，智能体会以指定问题向用户提问，并等待用户回答。​

说明

  * 豆包渠道暂不支持问答节点。即使在豆包渠道中触发了问答节点，此节点也不会按照预期运行。​

  * Chat SDK 暂不支持问答节点的卡片效果，用户需要手动复制问答节点的选项，并发送给智能体。​

  * 问答节点等待时长为 24 小时，用户如果未在 24 小时内回复，则此节点运行失败。​

​

问答节点支持以两种方式收集用户的信息或意图：​

​

收集方式​| 说明​| 示例​  
---|---|---  
直接回答​| 节点中指定一个开放式问题，用户直接以自然语言回复问题，智能体会提取用户的整段回复，或提取回复中的关键字段。如果用户的响应和智能体预期提取的信息不匹配，例如缺少必选的字段，或字段数据类型不一致，智能体会主动再次询问，直到获取到关键字段。​​| 例如在查询天气场景下，询问日期和城市，并从用户回复中提取位置字段。如果用户提供的信息不足，智能体将继续询问。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27289%27%20height=%27177%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1ba34f6966754377bfb3503c55935268~tplv-goo7wpa0wc-quality:q75.image)​​  
选项回答​| 问答节点预置固定选项，用户以固定选项回复问题，通常用于聊天式的智能体中，推进对话进度、增强互动性。你可以将用户可以执行的操作设置为选项，帮助用户在指定范围内快速回复，也可以将常见的意图作为选项，作为用户输入的提示信息。每个选项通常对应不同的工作流分支处理，用户在选项之外的回复也需要有分支处理，例如可以引导用户再次选择。​说明在飞书中，选项会展示为普通文字，用户应复制选项文字进行回答。​​| 例如在互动类游戏场景下，收集用户在每个环节的路径选择，推进剧情进展。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271520%27%20height=%271037.9288025889969%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyMCIgaGVpZ2h0PSIxMDM3LjkyODgwMjU4ODk5NjkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
  
​

配置问答节点（直接回答）​

配置步骤​

1.

在工作流画布下方工具栏中，添加问答节点。​

2.

为问答节点添加以下配置。​

  * ​

配置项​| 说明​| 示例​  
---|---|---  
模型​| 选择执行此节点的模型，支持设置模型在此节点中的生成多样性、输入及输出设置等参数配置，使模型效果更符合你的预期。具体配置，请参考​设置模型。​问答节点中的模型仅支持通过 Chat API 调用，不支持 Responses API 调用。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27619.0751445086705%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjYxOS4wNzUxNDQ1MDg2NzA1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​​  
输入​| 设置需要添加到问题中的参数，参数值可以引用前置节点的输出参数，或设置为固定文本内容。​| ​  
回答内容​| 设置智能体在对话中向用户发起的问题内容。​直接回答模式下，问答内容通常是一个无固定答案的开放式的问题，例如游戏场景中，请用户为自己扮演的角色设置一个昵称。​| ​  
回答类型​| 设置用户回答问题的方式，此处应设置为直接回答。​| ​  
输出​| 直接回答模式下，问答节点默认输出以下变量：​
    * USER_RESPONSE： 用户回复的具体内容。​
    * QUESTION_DATA：问答的参数信息，包括提问的内容（content）和参数类型（content_type）。​
你也可以开启从回复中提取字段，由模型从用户回复中自动提取关键信息并保存为变量，便于下游节点引用。​
    * 此时建议设置有意义的变量名称，并添加变量描述，便于模型理解变量定义、正确提取关键信息。​
    * 变量可以设置为必填，如果用户回复中未包含必选的字段信息，工作流将一直追问，直至成功采集信息，或达到指定的回答次数（默认3次）。追问时的具体问题由模型生成，你可以额外添加系统提示词，为模型设置人设和回复逻辑，使追问的语气更加自然。​
| ​  
  
​

3.

将问答节点与其他节点连接，形成完整的调用链路。​

  * 直接回答模式下，问答节点下游无需设置多个分支分别处理用户意图。​

示例​

以一个需求咨询智能体的留资工作流为例，该节点用于收集用户的个人信息，包括企业名称、联系人、联系方式，并将其记录在数据库中，用于后续销售人员联系客户沟通具体需求。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272828%27%20height=%27536.7962962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgyOCIgaGVpZ2h0PSI1MzYuNzk2Mjk2Mjk2Mjk2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

工作流的关键节点如下：​

​

节点名称​| 配置说明​| 示例​  
---|---|---  
问答节点​| 通过问答节点收集用户信息，回答方式指定为直接回答 Reply。开启从回复中提取字段，智能体会自动提取关键字段，各个信息均为必选项，如果用户回复信息不完整，智能体会继续追问。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2791%27%20height=%27185%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTEiIGhlaWdodD0iMTg1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
SQL自定义节点​| 用于保存用户回复中的个人信息，输入参数的值引用问答节点的输出参数，通过 SQL 写入一行新数据，记录用户的个人信息。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2791%27%20height=%27128%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTEiIGhlaWdodD0iMTI4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

配置问答节点（选项回答）​

配置步骤​

1.

在工作流画布下方工具栏中，添加问答节点。​

2.

为问答节点添加以下配置。​

  * ​

配置项​| 说明​  
---|---  
模型​| 选择执行此节点的模型，支持设置模型在此节点中的生成多样性、输入及输出设置等参数配置，使模型效果更符合你的预期。具体配置，请参考​设置模型。​问答节点中的模型仅支持通过 Chat API 调用，不支持 Responses API 调用。​  
输入​| 设置需要添加到问题中的参数，参数值可以引用前置节点的输出参数，或指定内容。​  
回答内容​| 设置智能体在对话中向用户发起的问题内容。​  
回答类型​| 设置用户回答问题的方式，此处应设置为选项回答，并填写选项内容。​此处设置的选项在对话中会展示为按钮形式，用户需要直接点击按钮或回复对应的选项编号来回答问题。​  
选项内容​| 问答节点选项回答模式提供的可选项，支持设置为固定内容或动态内容：​
    * 固定内容：开发者预设固定的选项内容，用户需要从多个选项中任选一个，各个选项会流转至不同的下游分支处理。​
    * 动态内容：引用前置节点的输出变量，变量的格式必须是 String 数组。例如在游戏场景中，可以由模型节点生成多种武器类型，再添加问答节点引导用户选择任意一种武器。​
    * 该模式下各个选项均流转至同一分支处理，与选项不相关的回答会流转至兜底策略。配置示例，请参考​示例2：动态选项内容。​  
输出​| 选项回答模式下，问答节点默认输出以下变量：​
    * optionId：用户选择的选项 ID，即 A~Z，String 类型。​
    * optionContent：用户选择的选项内容，String 类型。​
    * QUESTION_DATA： 问答选项的参数详情，Object 类型。​  
  
​

3.

将问答节点与其他节点连接，形成完整的调用链路。​

  * 问答类型为选项回答时，应为每个分类都设置后续的处理节点。例如在客服类智能体中，为用户提供“售前咨询”、“售后问题”两个选项，分别流转至对应的知识库。​

  * 问答节点应设置兜底策略，若意图未匹配到此处定义的任何分类，则流转到兜底策略处理。例如在客服类智能体中，兜底策略为转人工处理，如果用户回复与任一选项都不相关的内容时，流转到输出节点，指引用户如何联系人工客服。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27454%27%20height=%27291%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU0IiBoZWlnaHQ9IjI5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例1：固定选项内容​

以个人助手智能体为例，助手提供查看热门新闻、查看热门视频的技能，这两项技能均以工作流官方插件节点方式实现。​

工作流的关键节点为问答节点，此节点通过问答方式引导选择意图，即用户期望执行的操作。此处提供两个操作，即“查看热门新闻”和“查看热门视频”。这两个技能均流转至对应的扣子编程官方插件处理。如果用户在问答节点回复了无关内容，则流转至文本节点，并结束工作流。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27715%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzE1IiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

问答节点配置：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27710%27%20height=%271593.0845771144277%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzEwIiBoZWlnaHQ9IjE1OTMuMDg0NTc3MTE0NDI3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

文本处理节点配置：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27714%27%20height=%27823.0472727272728%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzE0IiBoZWlnaHQ9IjgyMy4wNDcyNzI3MjcyNzI4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

示例2：动态选项内容​

以搭建一个生成城市画报的工作流为例，在问答节点中设置问题为你要生成什么城市的画报？，在动态内容中引用开始节点的输入参数 city，city 参数的数据类型需为 Array<String> 。运行工作流时，系统会根据输入的城市数组，生成对应的选项。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27790%27%20height=%27270%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzkwIiBoZWlnaHQ9IjI3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

问答节点配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27548%27%20height=%27611.7672727272728%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ4IiBoZWlnaHQ9IjYxMS43NjcyNzI3MjcyNzI4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

开始节点-输入​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27538%27%20height=%27338.45090909090914%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM4IiBoZWlnaHQ9IjMzOC40NTA5MDkwOTA5MDkxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

问答选项​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27545%27%20height=%27376.54545454545456%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ1IiBoZWlnaHQ9IjM3Ni41NDU0NTQ1NDU0NTQ1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

常见问题​

如果用户回复不相关的内容，会有什么表现​

  * 在直接回答模式下，开发者往往会设置从回答中提取必填字段，例如故障排查场景下，售后客服智能体需要记录用户的 Log ID 便于排查问题。用户回复不相关的内容时，模型无法从回答中提取必填字段，智能体将持续追问，直至成功采集信息，或达到指定的回答次数。​

  * 在选项回答模式下，开发者需要设置兜底策略，如果用户回复不相关的内容，工作流将流转至兜底策略的分支处理。例如在客服类智能体中，兜底策略为转人工处理，如果用户回复与任一选项都不相关的内容时，流转到消息节点，指引用户如何联系人工客服。​

如何设置最多回答次数​

直接回答模式下，如果用户回复不相关的内容，模型无法从用户回答中提取出必填的关键字段，则会继续追问，默认最多追问 2 次，开发者也可以设置用户最多回答的次数，达到次数后工作流会停止运行。最多回答次数默认为 3 次，支持设置为 1~5 次。设置方式如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27397%27%20height=%27320%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk3IiBoZWlnaHQ9IjMyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

HTTP 请求节点

下一篇

文本处理节点