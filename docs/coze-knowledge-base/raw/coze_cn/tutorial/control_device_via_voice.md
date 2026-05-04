---
source_url: https://docs.coze.cn/tutorial/control_device_via_voice
title: '通过语音控制设备 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:52:41Z
---

# 通过语音控制设备 - 文档 - 扣子

通过语音控制设备

本文介绍如何通过输出节点、端插件或云侧插件实现语音控制设备，例如调节音量、拍照识别等。​

实现方案对比​

​

方案​| 通过输出节点传递语音指令​| 端插件​| 云侧插件​  
---|---|---|---  
适用场景​| 适用于仅需下发指令而无需设备返回数据的单向控制场景，如调节音量、控制设备移动、转人工等。​| 需要从设备端获取数据（如摄像头图像、传感器数据），并根据数据执行后续处理的场景，如拍照识别、获取手机日历等。​| 需要跨设备控制的场景。​  
  
​

方案一：通过输出节点传递语音指令​

通过对话流中的输出节点，可将意图识别后的语音指令传递至设备。适用于简单的、单向的设备控制，例如调节音量或转人工等。具体实现流程如下：​

在对话流中分别配置意图识别和输出节点，当意图识别到需要调节音量等设备控制时，扣子编程向设备发送conversation.message.completed 事件，例如 type= "answer", content_type="text", content = {"action": "volume_up"} ，设备根据 content 字段获取控制指令并执行相应的设备操作。事件详情请参见​消息完成事件。​

时序图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27458.4971098265895%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c0900486eb2541608dca35d64242f5c2~tplv-goo7wpa0wc-quality:q75.image)​

​

1 搭建对话流​

以智能家居场景下，实现语音调节音量与语音闲聊功能为例。对话流的编排详情如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%275593%27%20height=%271500.0878612716763%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU5MyIgaGVpZ2h0PSIxNTAwLjA4Nzg2MTI3MTY3NjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

各节点的详细配置如下。​

​

节点​| 说明​| 示例​  
---|---|---  
开始节点 ​| 开始节点的输入参数保持默认值即可。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27124.61059190031152%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjEyNC42MTA1OTE5MDAzMTE1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
意图识别（大模型节点）​| 通过开始节点中的用户输入进行意图识别。​

  * 模型：选择 doubao 1.5-lite-32k 或豆包·角色扮演·Pro 等支持复杂多轮对话的模型。​

  * 输入：引用开始节点的 USER_INPUT。建议开启会话历史，确保模型结合上下文判断意图。​

  * 系统提示词：根据实际场景调整系统提示词中的意图，本文的系统提示词样例请参见​提示词样例。​

说明

  * 为了降低大模型的响应时间，建议参考本文通过大模型节点实现意图识别，而不是使用对话流自带的意图识别节点，因为自带的意图识别节点采用直接输出内容的方式，会导致输出的 Token 数量过多，从而增加响应时间。​

  * 意图识别的输出结果用序号（例如1、2、3）来标识意图，避免让大模型直接返回完整回答，否则，会导致输出的 Token 数量过多，从而显著增加响应时间。具体原理请参见​优化大模型响应时间。​

​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27487.2274143302181%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ny4yMjc0MTQzMzAyMTgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
选择器​| 智能体根据意图识别返回的值，判断进入设备控制节点或闲聊节点。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27163.2398753894081%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE2My4yMzk4NzUzODk0MDgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
输出节点-设备控制（输出节点） ​| 用于下发设备控制指令。​

  * 输出内容：根据实际场景调整输出内容中的设备控制指令。例如：{"action": "volume_up"}。​

  * 通话中转语音：配置音视频通话时是否朗读输出节点的消息内容。若不希望设备控制指令通过TTS 朗读，可关闭此功能。​

  * 会话历史写入：设置为不写入。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27222.42990654205607%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIyMi40Mjk5MDY1NDIwNTYwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
闲聊（大模型节点） ​| 实现语音闲聊功能。​

  * 输入参数：input 参数的值引用开始节点的 USER_INPUT。​

  * 系统提示词：根据实际情况调整闲聊的回复逻辑和风格。本文的系统提示词请参见​提示词样例。​

  * 用户提示词：引用输入参数中的 input 参数。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27428.03738317757006%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQyOC4wMzczODMxNzc1NzAwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
输出节点​| 用于输出闲聊节点的结果，输出变量的值引用闲聊节点的输出参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27115.88785046728971%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjExNS44ODc4NTA0NjcyODk3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 因为已通过前面的输出节点输出工作流的结果，所以结束节点无需返回变量或文本。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27147.0404984423676%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE0Ny4wNDA0OTg0NDIzNjc2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

2 测试并发布智能体​

1.

试运行并发布对话流。​

2.

创建单 Agent（对话流模式）的智能体，在智能体中添加对话流，开启语音通话并设置音色。​

3.

在智能体右侧的调试页面单击通话图标，语音输入调大音量，智能体将返回设备控制指令 {"action": "volume_up"}。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27371.0982658959537%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM3MS4wOTgyNjU4OTU5NTM3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

将智能体发布到 API 渠道或其他目标渠道。​

方案二：端插件​

本文以 AI 眼镜为例，介绍用户通过语音输入指令后，智能体如何调用端侧插件实现拍照与物体识别。​

时序图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27440.46242774566474%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQ0MC40NjI0Mjc3NDU2NjQ3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

搭建智能体​

1 复制智能体模板​

1.

打开[AI 眼镜小助手](<https://docs.coze.cn/tutorial/coze.cn/template/agent/7527496694058139686>)智能体，然后单击复制。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27250.83612040133778%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI1MC44MzYxMjA0MDEzMzc3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选择智能体的所属空间并输入一个智能体名称，然后单击确定。​

3.

（可选）在复制的智能体编排页面，单击智能体名称旁的修改图标，修改智能体名称。​

4.

根据实际需求，修改开场白文案和预置问题。​

2 调整对话流​

对话流的编排详情如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%278266%27%20height=%273373.2924855491333%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODI2NiIgaGVpZ2h0PSIzMzczLjI5MjQ4NTU0OTEzMzMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

根据实际场景，在对话流中调整相应的节点和子工作流。本文重点介绍设备拍照分支的实现逻辑，其他子工作流的实现逻辑请参见​搭建低延时语音助手。各节点配置要求如下：​

​

节点​| 说明​| 示例​  
---|---|---  
意图识别（大模型节点）​| 通过开始节点中的用户输入进行意图识别，判断是否需要调用端插件。每种意图分别对应一个子工作流。​

  * 模型：选择 doubao 1.5-lite-32k 或豆包·角色扮演·Pro 等支持复杂多轮对话的模型。​

  * 输入：需要开启会话历史，确保模型结合上下文判断意图。​

  * 系统提示词：根据实际场景调整系统提示词中的意图。​

说明

  * 为了降低大模型的响应时间，建议参考本文通过大模型节点实现意图识别，而不是使用对话流自带的意图识别节点，因为自带的意图识别节点采用直接输出内容的方式，会导致输出的 Token 数量过多，从而显著增加响应时间。​

  * 意图识别的输出结果用序号（例如1、2、3）来标识意图，避免让大模型直接返回完整回答，否则，会导致输出的 Token 数量过多，从而显著增加响应时间。具体原理请参见​优化大模型响应时间。

​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27683.4890965732086%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjY4My40ODkwOTY1NzMyMDg2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
获取当前时间（代码节点）​| 通过代码获取实时日期和时间，添加输出参数current_time 和 current_date，作为后续大模型的输入参数，用于生成当前时间相关的回答。​| ​Python复制from datetime import datetime​​​async def main(args: Args) -> Output:​ current_time = datetime.now()​ formatted_date = current_time.strftime("%Y-%m-%d")​ formatted_time = current_time.strftime("%H:%M")​ ret: Output = {​ "current_date": formatted_date,​ "current_time": formatted_time ​ }​ return ret​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27298.44236760124613%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI5OC40NDIzNjc2MDEyNDYxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
选择器​| 智能体根据意图识别返回的值，进入对应的子工作流，例如设备拍照分支。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27433.64485981308405%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQzMy42NDQ4NTk4MTMwODQwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
photograph（端插件） ​| 通过[设备控制端插件](<https://www.coze.cn/store/plugin/7527323690468393014>)实现设备拍照，并将图片上传到服务端。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27198.13084112149534%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE5OC4xMzA4NDExMjE0OTUzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
视觉理解（大模型节点）​| 接收端插件上传的图片信息，并结合用户原始问题进行多模态理解。​

  * 输入参数：​

  * input ：参数的值引用开始节点的USER_INPUT。​

  * image ：参数的值引用 photograph 端插件输出的 image。​

  * current_date 和 current_time ：参数的值引用获取当前时间节点的输出。​

  * 系统提示词：根据实际场景，修改系统提示词中的技能。​

  * 用户提示词：引用输入参数中的 input 和image参数。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27440.4984423676012%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ0MC40OTg0NDIzNjc2MDEyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
输出​| 将视觉理解节点的分析结果返回给用户。建议开启流式输出，以提升用户体验。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27272.2741433021807%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI3Mi4yNzQxNDMzMDIxODA3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

发布并验证效果​

1.

试运行并发布对话流。​

2.

将智能体发布到 API 渠道。​

3.

验证效果。​

a.

访问 [Realtime 智能音视频 Demo](<https://www.coze.cn/open-platform/realtime/playground>)，单击 Settings，设置 Token 和对应的智能体。单击 Connect。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27410.63583815028903%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQxMC42MzU4MzgxNTAyODkwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

语音输入指令，例如这是什么东西，验证智能体是否能正确触发端插件。例如 Demo 弹出 Function Call 事件对话框表示已触发端插件。​

c.

通过​上传文件API 获取图片 ID，并将图片 ID 填入提交端插件执行结果的 output 中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27325.3179190751445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjMyNS4zMTc5MTkwNzUxNDQ1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

端插件实现流程​

设备端需要实现完整的事件监听、执行和上报闭环，具体步骤如下：​

1\. 接收required_action事件​

当对话流触发端插件时，设备会收到 conversation.chat.requires_action 事件，其中包含需要调用的函数信息，如 photograph。​

下行事件示例：​

​

JSON

复制

{​

"id": "event_15",​

"event_type": "conversation.chat.requires_action",​

"data": {​

"id": "7527500166237***",​

"conversation_id": "7527503562080***",​

"required_action": {​

"type": "submit_tool_outputs",​

"submit_tool_outputs": {​

"tool_calls": [​

{​

"id": "5871369658880***",​

"type": "function",​

"function": {​

"name": "photograph",​

"arguments": ""​

}​

}​

]​

}​

}​

}​

}​

​

2\. 执行设备能力并上传文件​

设备根据 function.name 调用本地能力，例如摄像头拍照。调用​上传文件 API，将拍照的图片上传至服务端，并获取图片 ID。​

上传文件 API 示例：​

​

Bash

复制

curl -X POST 'https://api.coze.cn/v1/files/upload' \​

-H "Authorization: Bearer cztei_qTST5l1tkfumssw***" \​

-H "Content-Type: multipart/form-data" \​

\--form 'file=@"ai_glasses_capture.jpeg"'​

​

3\. 提交端插件执行结果​

设备将获取到的 file_id 通过 conversation.chat.submit_tool_outputs 事件提交给扣子编程，以驱动对话流继续执行。​

说明

chat_id、tool_call_id 需要与 conversation.chat.requires_action 事件中的 ID 保持一致。​

​

上行事件示例：​

​

JSON

复制

{​

"id": "1",​

"event_type": "conversation.chat.submit_tool_outputs",​

"data": {​

"chat_id": "7527500166237***",​

"tool_outputs": [​

{​

"tool_call_id": "5871369658880***",​

"output": "{\"image\":\"$file_id\"}"​

}​

]​

}​

}​

​

方案三：云侧插件​

需将设备控制相关服务封装为自定义云侧插件，具体实现方法请参见​基于 API 创建插件。​

在对话流中添加该云侧插件。当意图识别结果为设备控制时，智能体调用该云侧插件。插件对应的服务端接收请求后，根据请求中的通话 ID 信息，执行相应设备操作。​

云侧插件的对话流编排详情如下图所示，各节点的配置和其他方案类似。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%275593%27%20height=%271500.0878612716763%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU5MyIgaGVpZ2h0PSIxNTAwLjA4Nzg2MTI3MTY3NjMiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

时序图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27337.8034682080925%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjMzNy44MDM0NjgyMDgwOTI1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

提示词样例​

意图识别节点​

​

JSON

复制

### 角色​

你是一位杰出的意图识别专家，具备极为敏锐的洞察力，能够迅速且精准地判断用户问题的意图类型。在接收到用户问题时，需紧密结合当前用户输入以及历史消息，全面且深入地剖析问题的核心内涵。​

### 技能​

#### 技能 1：精准识别用户意图​

依据以下意图列表，仅返回与之对应的数字序号。​

| 序号 | 意图 | 描述 | 示例 |​

| :\--: | :\----------- | :\----------------------------------------------------------- | :\----------------------------------------------------------- |​

| 1 | 设备控制 | 涉及需要控制设备的操作 | "调大音量" |​

| 2 | 无需联网 | 属于闲聊范畴，或可单纯依靠基础知识库解答；或是用户明确提出不联网需求；亦或是涉及通用概念、原理性的问题、用户的主观感受 | “三角形内角和是多少”“给我讲个笑话”“我不想联网，给我说说历史故事”“你觉得/你认为/你有没有/你平时”|​

### 回复格式​

\- 仅回复意图对应的序号：1、2​

​

### 示例​

#### 示例 1​

当前用户输入：我感觉好无聊呀​

2​

#### 示例 2​

当前用户输入：调大音量​

1​

### 限制​

\- 若遇到难以理解或把握不准的问题，统一归类到 2。​

\- 用户输入中可能涵盖一个或多个上述意图，需根据输入内容输出最为贴近的一个意图序号，仅回复一个数字，无需阐述原因。 ​

​

闲聊节点​

​

JSON

复制

# 角色​

你是一个高效且知识渊博的生活小助理，能陪伴用户​

​

## 技能​

### 技能 1: 闲聊陪伴​

1. 积极与用户互动，倾听用户的心声，给予温暖的回应，回复100字左右​

2. 结合历史消息和用户当前输入，根据用户的话题展开有趣的讨论，让用户感受到陪伴。​

​

​

## 回答格式​

\- 直接输出文本，不要输出json​

​

## 限制:​

\- 只回答与生活相关或百科知识范围内的问题，拒绝回答无关话题。​

\- 所输出的内容必须按照给定的格式进行组织，不能偏离框架要求。​

\- 请确保信息来源准确可靠，必要时注明引用来源。​

​

​

​

上一篇

基于 RTC 实现按键说话/语义判停

下一篇

语音降噪