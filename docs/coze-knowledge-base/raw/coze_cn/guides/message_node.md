---
source_url: https://docs.coze.cn/guides/message_node
title: '输出节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:02Z
---

# 输出节点 - 文档 - 扣子

输出节点

低代码工作流的输出节点用于在低代码工作流执行过程中输出指定的消息内容，例如 "正在执行中"等 Loading 状态展示或安抚语。​

节点说明​

通常情况下，工作流会在执行完毕后通过结束节点输出最终的执行结果。当工作流处理流程较长、运行时间较久时，开发者可以在工作流中添加输出节点，临时输出一段消息，避免用户等待时间过长、放弃对话。例如提示用户任务正在执行中，建议用户耐心等待。​

输出节点支持流式和非流式两种模式，同时支持绑定卡片，展示丰富的交互效果，提升对话过程的用户体验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27254%27%20height=%27350%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1ddc87134863447db6f774691c94c094~tplv-goo7wpa0wc-quality:q75.image)​

​

配置输出节点​

在输出节点中，工作流会在执行的同时输出一条中间消息，消息内容为指定的输出内容，其中可引用已定义的输出变量。输出节点支持流式输出，即打印机效果。​

输出变量​

输出变量用于定义输出内容中可引用的变量，支持添加多个变量。每个变量均需要设置参数名和参数值，其中参数值可指定为某个固定值，或引用上游节点的输出变量。​

输出变量也可以在输出节点绑定的卡片中使用。​

输出内容​

在工作流运行过程中，智能体将直接使用这里指定的内容回复对话。你可以使用{{变量名}}的方式引用输出变量中定义的变量。​

在输出内容右侧单击配置图标，还可以调整流式输出等高级配置。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27318.37944664031625%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjMxOC4zNzk0NDY2NDAzMTYyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

说明

通话中转语音、音色和会话历史写入设置仅对话流可设置，工作流输出节点不支持此配置。​

​

流式输出​

流式输出表示输出节点配置的输出内容会逐字地显示在对话中，类似于打字机的效果。流式输出适用于输出文本较长或需要工作流即时反馈的场景，呈现实时对话的交互效果，用户无需等待一大段文字一次性加载，可显著提高对话过程中的用户体验。​

输出节点默认采用非流式输出，待接收到全部消息内容后，再一次性输出全部消息内容。​

说明

  * 输出节点只有在大模型节点之后才能开启流式响应。​

  * 如果输出节点绑定了消息卡片，即使开启流式输出，输出的卡片也是非流式的，卡片会等待所有回复内容加载完毕后一次性展示在对话中。​

  * 当在一个工作流中配置了多个输出节点并开启了流式返回时，输出节点的执行遵循工作流的执行顺序，先执行的输出节点优先输出消息。​

​

通话中转语音​

仅在视频通话时生效，用于指定通话时是否朗读输出节点配置的消息内容。关闭通话中转语音表示不朗读。输出节点如果展示 Loading 状态、卡片效果、自定义指令等与对话本身无关的内容，通常无需开启通话中转语音。 ​

说明

开启通话中转语音后，音视频通话时朗读输出消息会产生语音转文本的费用，具体资费和朗读时选择的音色类型有关，详细说明可参考​音视频费用。​

​

音色​

为输出节点配置音色，支持配置自定义的复刻音色或系统预设音色。配置后，如果开启了通话中转语音，智能体会在音视频通话中以指定音色朗读输出节点配置的消息内容。未配置音色时，输出节点沿用智能体或对话流角色配置的音色。​

扣子编程的系统预设音色支持多情感音色，即一个音色中包括多种情感，例如开心、悲伤等。你可以指定其中一种情感并设置情绪值，来控制输出节点音色的情绪类型。指定的情感将应用于该输出节点的所有内容，不会根据每句话动态调整。具体配置说明如下表所示。​

注意

试听音色时，扣子编程将根据音色类型（复刻音色/系统音色）及对应规则收取语音合成费用。费用详细说明请参见​音视频费用。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27356.48148148148147%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM1Ni40ODE0ODE0ODE0ODE0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

参数​| 说明​  
---|---  
情感​| 情感参数用于指定输出节点音色的情绪类型，例如开心、悲伤等。你可以从下拉列表中选择该音色对应的情感。不同音色支持的情感范围不同。​  
情绪值​| 情绪值用于量化情感的强度。数值越高，情感表达越强烈，例如： “开心” 的情绪值 5 比 1 更显兴奋。​取值范围：1.0~5.0，默认值：4.0。​  
  
​

会话历史写入​

输出节点配置的消息内容是否自动写入对话流的会话历史。支持设置为：​

  * 写入：（默认）输出消息写入对话流的会话历史。模型会将输出节点的消息内容作为上下文传递给大模型，以便大模型更好地理解用户意图，生成更连贯、自然、准确的回复。同时由于增加了模型输入的 Token，也会一定程度上影响模型响应耗时。​

  * 不写入：输出消息不写入会话历史，仅在执行会话流时展示。例如输出节点配置的 Loading 状态展示、安抚语、自定义指令等和对话本身无关的信息通常无需写入会话历史，否则会影响模型的输出。​

工作流：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27266%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY2IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

对话流：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27242%27%20height=%27335%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQyIiBoZWlnaHQ9IjMzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

示例​

如果工作流的输出内容较长，可以使用输出节点拆分消息内容，一部分通过输出节点输出，一部分通过结束节点输出，同时开启流式输出。​

以好书解析智能体为例，通过大模型节点生成书籍的介绍，指定输出为两个段落，通过文本处理节点将两个段落拆开，一段通过输出节点输出，一段通过结束节点输出。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272840%27%20height=%271159.526627218935%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg0MCIgaGVpZ2h0PSIxMTU5LjUyNjYyNzIxODkzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

核心节点配置说明如下：​

​

节点类型​| 配置说明​| 示例​  
---|---|---  
大模型节点​| 引用开始节点的变量，获取用户需要查询的书籍名称。​用户提示词中需要指定输出格式，例如指定输出为两个段落。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27668.3544303797469%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjY2OC4zNTQ0MzAzNzk3NDY5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
文本处理节点​| 使用字符串分隔模式，通过换行符将大模型节点的输出内容转为数组格式，每个段落是数组的一个元素。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27456.73758865248226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ1Ni43Mzc1ODg2NTI0ODIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
输出节点​| 引用文本处理节点的输出，注意这里只引用数组的第一个元素，也就是书籍简介的第一个段落。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27397.63313609467457%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM5Ny42MzMxMzYwOTQ2NzQ1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 引用文本处理节点的输出，这里只引用第二个段落即可。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27444.9704142011834%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ0NC45NzA0MTQyMDExODM0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

在智能体中的体验效果如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27302%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg1IiBoZWlnaHQ9IjMwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

输入节点

下一篇

SQL 自定义节点