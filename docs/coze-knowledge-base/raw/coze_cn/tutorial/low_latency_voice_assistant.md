---
source_url: https://docs.coze.cn/tutorial/low_latency_voice_assistant
title: '搭建低延时语音助手 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:52:09Z
---

# 搭建低延时语音助手 - 文档 - 扣子

搭建低延时语音助手

语音小伴侣是扣子编程官方推出的低延时语音场景的智能体模板，融合了联网搜索、设备控制、闲聊、低时延等功能，你可以通过复制该模板，创建并定制符合自身业务需求的低延时语音陪伴智能体，尤其适用于对实时性要求较高的场景。​

单击体验[语音小伴侣智能体模板](<https://www.coze.cn/template/agent/7455613304489213989?>)。​

模板介绍​

语音小伴侣智能体是专为实时交互场景打造的低延时语音通话智能体模板，适用于智能家居、智能车载、智能客服等场景。凭借其低延时特性，实现毫秒级响应，让语音交互如面对面交流般自然流畅。例如，在智能家居场景中，用户可语音控制灯光、家电；在车载场景中，智能体可帮用户查询路况、播放音乐；在日常陪伴中，能陪用户闲聊、解答问题，成为用户贴心小帮手。​

模板能力​

语音小伴侣智能体具备以下能力：​

  * 实时信息获取：支持联网搜索功能，可快速获取天气、新闻、知识等实时数据，确保为用户提供最新信息。​

  * 设备控制：能够下发指令控制各类智能设备，实现语音与硬件的联动，让用户的生活更便捷。​

  * 沉浸式闲聊：具备出色的闲聊和角色扮演能力，支持多轮对话关联与追问，使交互更自然流畅，提升用户体验。​

  * 低延时：通过优化对话流的编排逻辑和相关配置，语音小伴侣智能体实现了低延时交互。在联网搜索场景下，平均时延可控制在 2650 毫秒左右；在闲聊场景中，平均时延约为 900 毫秒。显著提升了交互的流畅性，为用户带来更接近实时的对话体验。​

  * 长期记忆：拥有长期记忆功能，可记住用户画像、偏好和关键事件，为用户提供个性化服务。​

  * 贴心服务：在联网响应慢时，能及时安抚用户，减少用户等待的焦虑感。​

方案选型​

扣子编程支持多种方式搭建语音通话的智能体，以下是各方案的优缺点及适用场景：​

​

方案​| 适用场景​  
---|---  
单 Agent（对话流模式）​| 

  * （推荐）灵活高效且时延较低，能够充分保障用户交互的流畅性。本文将以该场景为例介绍搭建思路。​

  * 通过对话流编排，能够清晰地定义不同节点的逻辑，便于搭建复杂的业务场景。​

  
单 Agent（自主规划模式）​| 

  * 配置简单，易于上手。适用于简单的闲聊，对时延要求不高的场景，不适用于复杂的逻辑场景。​

  * 智能体中添加插件和工作流会导致延时增加，故不适用于本场景。​

  
多 Agents​| 

  * 适用于逻辑复杂且对时延要求不高的场景。​

  * 智能体中添加插件和工作流会导致延时增加，故不适用于本场景。​

  
  
​

实现流程​

语音小伴侣模板采用对话流模式编排，主要功能通过对话流实现。对话流的设计思路如下：​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27358.6127167630058%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM1OC42MTI3MTY3NjMwMDU4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

使用模板​

步骤一：复制模板​

1.

打开[语音小伴侣智能体模板](<https://www.coze.cn/template/agent/7455613304489213989?>)，单击复制。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27423.2369942196532%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjQyMy4yMzY5OTQyMTk2NTMyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

选择智能体的所属空间并输入一个智能体名称，然后单击确定。​

3.

（可选）在复制的智能体编排页面，单击智能体名称旁的修改图标，修改智能体名称。​

步骤二：调整智能体配置​

建议沿用智能体的对话流模式，仅调整变量参数、开场白和语音的音色即可。​

在智能体的编排页面，修改智能体的以下编排配置：​

​

配置​| 说明​| 设置方式​  
---|---|---  
变量​| 在记忆 > 变量区域设置变量。本场景中定义了长期记忆所需要的用户画像和用户记忆点变量，在后续对话流中会引用对应的变量。你可以根据需要添加其他变量，具体设置方法请参见​变量。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2784.94208494208493%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9Ijg0Ljk0MjA4NDk0MjA4NDkzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
开场白​| 为智能体重新设计开场白，例如：你好呀！我是你的语音小助手，能帮你查天气、控制家电，还能陪你聊天哦～有什么需要帮忙的吗？具体设置方法请参见​人设与回复逻辑。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27128.1853281853282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEyOC4xODUzMjgxODUzMjgyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
语音的音色​| 智能体默认使用邻家女孩音色，你可以根据需要修改音色。具体设置方法请参见​音色。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2760.23166023166022%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjYwLjIzMTY2MDIzMTY2MDIyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

步骤三：调整对话流​

对话流的编排详情如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27389.5004233700254%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjM4OS41MDA0MjMzNzAwMjU0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

根据实际场景，在对话流中调整相应的节点。以下是关键节点的修改说明：​

​

节点​| 修改说明​| 示例​  
---|---|---  
意图识别（大模型节点）​| 通过开始节点中的用户输入进行意图识别，每一种意图分别对应一个子工作流，通过子工作流进行处理。​

  * 模型：选择 doubao 1.5-lite-32k 或豆包·角色扮演·Pro 等支持复杂多轮对话的模型。​

  * 输入：需要开启会话历史，确保模型结合上下文判断意图。​

  * 系统提示词：根据实际场景调整系统提示词中的意图，例如在智能家居场景中，你可以设置为天气查询、灯光或空调控制、个性化闲聊等。​

说明

  * 为了降低大模型的响应时间，建议参考本文通过大模型节点实现意图识别，而不是使用对话流自带的意图识别节点，因为自带的意图识别节点采用直接输出内容的方式，会导致输出的 Token 数量过多，从而显著增加响应时间。​

  * 意图识别的输出结果用序号（例如1、2、3）来标识意图，避免让大模型直接返回完整回答，否则，会导致输出的 Token 数量过多，从而显著增加响应时间。具体原理请参见​优化大模型响应时间。​

​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27563.0695443645084%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjU2My4wNjk1NDQzNjQ1MDg0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
获取当前时间（代码节点）​| 通过代码获取实时日期，作为后续大模型的输入参数，用于生成当前时间相关的回答。​| ​Python复制from datetime import date​​async def main(args: Args) -> Output:​ today = date.today()​ formatted_date = today.strftime('%Y-%m-%d')​ ret: Output = {​ "date": formatted_date ​ }​ return ret​​  
获取用户画像（文本处理节点）​| 在智能体的变量中设置了 user_profile 变量，用于存储用户画像，在该节点中引用 user_profile 变量并输出。​在闲聊节点的提示词中引用该变量，以便智能体根据用户画像灵活回答用户问题。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27265.8385093167702%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI2NS44Mzg1MDkzMTY3NzAyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
获取用户记忆点（文本处理节点）​| 在智能体的变量中设置了 user_memory_point 变量，用于存储关键记忆点，在该节点中引用 user_memory_point 变量并输出。​在闲聊节点的提示词中引用该变量，以便智能体根据用户历史记忆点回答用户问题。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27265.8385093167702%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI2NS44Mzg1MDkzMTY3NzAyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
闲聊（大模型节点）​| 根据实际需求调整闲聊的回复逻辑和风格。​在闲聊节点后需要增加输出节点输出闲聊结果，否则，扣子编程会等待更新用户画像和用户记忆的子工作流完成输出后才进行响应，这会显著增加响应时间。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27563.0922693266833%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjU2My4wOTIyNjkzMjY2ODMzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

步骤四：设计子工作流​

根据不同的意图，分别设计不同的子工作流，并通过子工作流的调用，实现不同的功能。以下是联网搜索子工作流的设计思路。天气查询、新闻搜索、股票查询等子工作流的实现也类似。​

联网搜索子工作流​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272196%27%20height=%27418.8901734104046%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE5NiIgaGVpZ2h0PSI0MTguODkwMTczNDEwNDA0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

节点​| 修改说明​| 示例​  
---|---|---  
搜索词改写（大模型节点）​| 

  * 模型：选择支持 Function Call 的模型，例如豆包 · 工具调用模型。​

  * 输入：需要开启会话历史，确保模型结合上下文判断意图。​

  * 系统提示词：根据实际场景调整系统提示词中的人设与回复逻辑。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27579.5396419437341%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjU3OS41Mzk2NDE5NDM3MzQxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
插件​| 根据不同的意图，选择合适的插件，例如头条搜索、墨迹天气、新浪财经、头条新闻等。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27244.52830188679243%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI0NC41MjgzMDE4ODY3OTI0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
搜索结果总结（大模型节点）​| 用于对插件的搜索结果进行总结。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27413.19796954314717%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQxMy4xOTc5Njk1NDMxNDcxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
延时安抚（输出节点）​| 联网搜索链路耗时较长，可以在搜索词改写节点前，增加输出节点，流式输出安抚的内容。​当用户发送完消息后，智能体会返回安抚话术，例如 ：正在搜索，请稍后～，提升用户等待体验。​说明安抚内容的结尾需要加标点符号，因为扣子编程语音合成需要识别到断句后才会将文本转换为语音。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27175.75757575757575%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE3NS43NTc1NzU3NTc1NzU3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
输出节点​| 每个子工作流中需要增加输出节点，并开启流式输出。​若未设置输出节点而直接使用结束节点输出最终变量，则需等待所有分支执行完毕后才能输出结果，这将显著增加响应时间。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

设备控制子工作流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%2797.22222222222223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9Ijk3LjIyMjIyMjIyMjIyMjIzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

由于对话流中不能直接在大模型节点调用端插件，因此通过一个大模型节点抽取出设备控制需要的参数，再通过一个代码节点拼接出完整的插件调用参数，触发插件调用。因为本场景中设备控制的参数较为简单，所以直接通过大模型节点抽取参数即可。​

如果设备控制的参数很多，你可以通过 [prompt generator](<https://www.coze.cn/store/agent/7468918778911834164?bid=6gaomspp49012&bot_id=true>) 智能体，将 JSON 格式的参数模板发送给智能体，从而快速生成参数抽取提示词。​

说明

为了减少 Token 数量，优化响应时间，建议：​

  * 返回参数应尽量简短：抽取节点返回的参数需要保持简洁，避免冗余信息。​

  * 使用管道符拼接参数：如果抽取的参数有多个，建议使用管道符（|）将它们拼接在一起，以减少输出的 Token 数量。再通过代码节点解析这些参数，生成多个具体的参数值。示例代码如下：​

  * ​

YAML

复制

例如抽取场景是：抽取出查询天气的城市和日期​

1. 参数提取节点的结果是：深圳|20250101|20250102​

2. 代码节点将字符串处理成json​

{​

"city":"深圳","start_date":"20250101","end_date":"20250102"​

}​

3. 墨迹天气插件，引用代码节点解析出的字段​

​

​

更新用户画像和用户记忆点子工作流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27349.0740740740741%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjM0OS4wNzQwNzQwNzQwNzQxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

本场景通过自定义变量实现更新用户画像和记忆点，而非使用系统自带的长期记忆功能。系统自带的长期记忆功能会在每次查询时触发查询操作，导致响应速度较慢。相比之下，自定义的子工作流采用异步处理方式，不会影响主流程的响应时间。​

在拼接用户记忆点节点中，可自定义存储的记忆点数量，默认为 50 条，用户可根据需求进行调整。​

​

Python

复制

parts = point.split(' | ')​

while point.count(' | ') > 50:​

parts.pop(0)​

point = ' | '.join(parts)​

​

步骤五：测试并发布智能体​

修改对话流并调试发布之后，你就可以测试智能体效果并发布智能体。​

1.

在智能体编排页面的右侧调试区域，输入问题进行测试。​

2.

完成测试后可单击发布，将智能体发布到你需要的任何渠道中使用。​

​

上一篇

实现语音和图片的多模态交互

下一篇

搭建可视化智能体