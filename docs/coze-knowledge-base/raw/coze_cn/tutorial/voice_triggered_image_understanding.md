---
source_url: https://docs.coze.cn/tutorial/voice_triggered_image_understanding
title: '实现语音和图片的多模态交互 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:52:04Z
---

# 实现语音和图片的多模态交互 - 文档 - 扣子

实现语音和图片的多模态交互

在智能眼镜等终端场景中，用户常常需要通过语音指令触发智能体，并上传图片以实现图片理解功能。这种多模态交互方式能够显著提升用户体验，尤其是在需要快速获取信息或进行复杂任务处理时。你可以选择基于对话 OpenAPI 或音视频通话来实现这一功能。​

方式一：基于对话 OpenAPI 实现​

步骤一：创建并发布智能体​

创建单 Agent（自主规划模式）类型的智能体，选择豆包·视觉理解·Pro 模型或其他支持视觉理解的模型。调试后将智能体发布为 API。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27378.7037037037037%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b57d5a1d68a94a159e3f4ec11f388559~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：调用发起对话 API 实现多模态交互​

实现方法​

1.

调用​上传文件 API，将图片和语音文件上传到扣子编程，并获取对应的 file_id。​

2.

调用​发起对话 API，在 messages 中同时传入图片和语音文件的 file_id。智能体将结合语音内容和图片内容进行联合理解，并返回对图片的理解结果。​

示例代码​

示例代码如下，完整的示例代码请参见 [audio_chat_with_vision_image](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/audio_chat_with_vision_image/http_chat.py>) 示例项目源码。​

​

Python

复制

# 将语音和图片上传到 coze​

audio_file = coze.files.upload(file=audio_path)​

image_file = coze.files.upload(file=image_path)​

​

# 调用 /v3/chat 发起对话, 传入语音和图片的 file id​

stream = coze.chat.stream(​

bot_id=bot_id,​

user_id=secrets.token_urlsafe(),​

additional_messages=[​

Message.build_user_question_objects(​

[​

MessageObjectString.build_image(file_id=image_file.id),​

MessageObjectString.build_audio(file_id=audio_file.id),​

]​

)​

],​

)​

print(f"对话开始 logid: {stream.response.logid}")​

​

成功调用后，智能体将返回图片的理解结果，返回示例如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27204.62962962962962%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjIwNC42Mjk2Mjk2Mjk2Mjk2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

方式二：基于语音通话 SDK​

步骤一：搭建对话流​

1.

创建一个对话流，对话流的节点概览如下图所示，在对话流中添加大模型节点用于理解图片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27182.40740740740742%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjE4Mi40MDc0MDc0MDc0MDc0MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 对话流中各节点的配置和参数如下表所示。​

  * ​

节点​| 参数配置​| 示例图​  
---|---|---  
开始​| 开始节点添加一个类型为 image 的输入参数，参数名称可以自定义，但需与代码中一致，本文以 image 为例。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27223.0769230769231%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIyMy4wNzY5MjMwNzY5MjMxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
大模型​| 
    * 模型选择豆包·视觉理解·Pro 模型或其他支持视觉理解的模型。​
    * 输入参数：输入中添加 input 和 image变量，变量的值分别引用开始节点的 USER_INPUT 和 image。​
    * 系统提示词：使用以下示例 Markdown 信息，表示将用户输入的数据传入 LLM 进行处理。​
    * ​Markdown复制用户输入：{{input}}​图片：{{image}}​​
​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27640.506329113924%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjY0MC41MDYzMjkxMTM5MjQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
结束​| 新增 output 输出参数，并在参数值区域选择引用大模型节点的 output 参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27330.3797468354431%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjMzMC4zNzk3NDY4MzU0NDMxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

2.

创建智能体并将智能体设置为单 Agent（对话流模式），在智能体中添加对话流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27288.19444444444446%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjI4OC4xOTQ0NDQ0NDQ0NDQ0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

将智能体发布为 API。​

步骤二：对话中发送音频和图片​

通过 WebSocket 或 RTC 进行音视频通话时，通过上行事件中的 parameters 参数，将图片发送给对话流。本文以 WebSocket 为例介绍具体实现方法。​

实现方法​

1.

建立 WebSocket 连接时，在 URL 路径的 Query 参数中设置 bot_id。​

2.

建立 WebSocket 连接后，发送 chat.update 上行事件，在 data.chat_config.parameters 参数中传入 image 输入参数的值，并传递给对话流，事件的详细说明请参见 ​双向流式对话上行事件。​

3.

通过 WebSocket 与智能体进行实时语音交互时，通过 input_audio_buffer.append 上行事件，流式上传音频数据，事件的详细说明请参见​流式上传音频片段。​

示例代码​

示例代码如下，完整的示例代码请参见 [websocket_chat.py](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/audio_chat_with_vision_image/websocket_chat.py>)[ ](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/audio_chat_with_vision_image/websocket_chat.py>)示例项目源码。​

​

Python

复制

chat = coze.websockets.chat.create(​

bot_id=bot_id,​

on_event=WebsocketsChatEventHandler(),​

)​

​

# 建立 websocket 链接​

async with chat() as client:​

print("建立 websocket 链接成功")​

# 发送 chat_flow 参数​

await client.chat_update(​

ChatUpdateEvent.Data.model_validate(​

{​

"chat_config": ChatUpdateEvent.ChatConfig.model_validate(​

{​

"parameters": {​

"image": json.dumps(​

{​

"file_id": image_file.id,​

}​

),​

}​

}​

)​

}​

)​

)​

# 发送语音数据​

for delta in split_bytes_by_length(audio_data, 1024):​

await client.input_audio_buffer_append(​

InputAudioBufferAppendEvent.Data.model_validate(​

{​

"delta": delta,​

}​

)​

)​

await asyncio.sleep(len(delta) * 1.0 / 24000 / 2) # 模拟真实说话间隔​

await client.input_audio_buffer_complete()​

await client.wait()​

​

​

成功建立连接并发送数据后，智能体将根据语音和图片内容返回相应的对话结果，返回示例如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271280%27%20height=%27272.5925925925926%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4MCIgaGVpZ2h0PSIyNzIuNTkyNTkyNTkyNTkyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

搭建漫画视频工作流

下一篇

搭建低延时语音助手