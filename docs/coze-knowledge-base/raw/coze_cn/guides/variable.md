---
source_url: https://docs.coze.cn/guides/variable
title: '变量 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:32:45Z
---

# 变量 - 文档 - 扣子

变量

变量用来存储动态变化的信息，使低代码智能体能够根据不同情况灵活调整，满足用户的特定需求和偏好。扣子编程的低代码智能体支持使用系统变量和用户变量。你可以在工作流、插件中引用预设的系统变量；也可以创建用户变量来保存用户个人信息，例如语言偏好等。​

变量类型​

使用扣子编程开发低代码智能体时，可以通过系统变量和用户变量来满足不同的业务需求和场景。每种变量类型都有其特定的用途和优势，以下是对这些变量类型的介绍说明。​

系统变量​

系统默认创建了用户信息、飞书、音视频等类别的系统变量，你可以根据实际业务需求选择开启所需的系统变量。开启后，系统将在用户请求时自动存储变量数据，这些数据为只读状态，用户或开发者均无法修改。你可以通过工作流节点例如问答、结束等节点获取系统变量值。​

每个系统变量获取的数据不同，支持使用的渠道也不同，具体说明如下：​

​

变量分类​| 变量名称​| 变量描述​| 数据类型​| 支持渠道​  
---|---|---|---|---  
用户信息​| sys_uuid​| 扣子账号 UID、发布渠道 ID 与智能体 ID 组合后的编码值，用于识别和追踪用户行为。​sys_uuid并非扣子账号的 UID。​| String​| 全部渠道​  
​| sys_longitude​| 扣子用户实时位置的经度信息。​使用此变量会触发用户授权。​| String​| 

  * 扣子商店​

  * 扣子模板​

  
​| sys_latitude​| 扣子用户实时位置的纬度信息。​使用此变量会触发用户授权。​| String​| 

  * 扣子商店​

  * 扣子模板​

  
​| sys_lat_lon​| 扣子用户实时位置的经纬度信息，纬度在前，经度在后。​使用此变量会触发用户授权。​| String​| 

  * 扣子商店​

  * 扣子模板​

  
​| sys_lon_lat​​| 扣子用户实时位置的经纬度信息，经度在前，纬度在后。使用此变量会触发用户授权。​| String​| 

  * 扣子商店​

  * 扣子模板​

  
飞书​| sys_lark_chat_id​| 飞书群的群 ID。详细说明，请参考[群 ID 说明](<https://open.larkoffice.com/document/server-docs/group/chat/chat-id-description#394516c9>)。​例如搭建用于总结飞书群消息的智能体时，可以在工作流中添加[飞书消息](<https://www.coze.cn/store/plugin/7395041302766944275?from=add_plugin_menu>)插件中的get_chat_messages工具，并设置工具中的 container_id 参数引用 sys_lark_chat_id 变量，当智能体被添加到不同的飞书群时，它能够自动识别并获取当前群的 ID，并对该群内的聊天消息进行高效总结。​| String​| 飞书​  
​| sys_lark_chat_mode​| 飞书群的群模式，包括普通对话群组、话题群组和单聊。详细说明，请参考[群组管理概述](<https://open.larkoffice.com/document/server-docs/group/chat/intro>)。​例如在搭建一个飞书消息相关的智能体时，可以引用 sys_lark_chat_mode 变量获取群模式。当智能体被发布到飞书后，可以根据群模式动态调整消息的处理逻辑。​| String​| 飞书​  
​| sys_lark_open_id​| 飞书用户在应用内的身份 ID。详细说明，请参考[用户身份](<https://open.larkoffice.com/document/home/user-identity-introduction/introduction>)。​例如在搭建智能客服智能体时，可以引用系统变量 sys_lark_open_id，当智能体被发布到飞书后，可以识别并验证用户身份，根据用户的历史咨询记录和偏好，提供定制化的服务建议，提高客服效率和用户满意度。​| String​| 飞书​  
​| sys_lark_thread_id​| 飞书的话题 ID。详细说明，请参考[话题概述](<https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/thread-introduction>)。​例如搭建基于话题的知识管理智能体时，可以在工作流中添加[飞书消息](<https://www.coze.cn/store/plugin/7395041302766944275?from=add_plugin_menu>)插件中的 get_thread_messages 工具，并设置工具中的 container_id 参数引用 sys_lark_thread_id 变量。当智能体被添加到飞书群时，它能够自动获取历史话题的 ID，并根据话题 ID 对信息进行分类和整理。​| String​| 飞书​  
音视频​| sys_voiceprint_name​| 声纹名称，用于标识对话人的身份，例如爸爸、妈妈等。例如你在智能体中开启声纹识别功能后，可以通过 sys_voiceprint_name 变量，以实现用户在与智能体语音通话时，智能体能够从声纹组中匹配说话人的身份，并根据匹配到的身份信息，提供针对性的回复。详细说明，请参考​声纹识别。​

  * 打开声纹识别功能后，sys_voiceprint_name 变量自动为启用状态。​

  * 关闭声纹识别功能后，sys_voiceprint_name 变量自动为关闭状态。​

| String​| API​  
​| sys_voiceprint_info​| 声纹的描述信息，由用户自己定义，例如你可以添加用户信息 爸爸是四十岁男性，关注科技类新闻，喜欢打球。​在智能体声纹识别功能中，你还可以通过 sys_voiceprint_info 变量来补充用户信息，使用智能体能够根据该信息提供更贴切、更个性化的回复。详细说明，请参考​声纹识别。​

  * 打开声纹识别功能后，sys_voiceprint_info 变量自动为启用状态。​

  * 关闭声纹识别功能后，sys_voiceprint_info 变量自动为关闭状态。​

| String​| API​  
​| sys_images​| 视频通话抽帧图片列表。开启视频通话功能后，系统会自动进行视频画面抽帧，并将抽帧图片以 URL 形式存储到 sys_images 变量中。你可以通过 sys_images 变量使用这些图片。​

  * 打开视频通话功能后，sys_images 变量自动为启用状态。​

  * 关闭视频通话功能后，sys_images 变量自动为关闭状态。​

| array<image>​| API​  
  
​

用户变量​

用户变量以 Key-Value 形式存储每个用户在使用智能体过程中，需要持久化存储和读取的数据，例如用户的个性化设置、语言偏好、历史交互记录等。开发者可以在扣子编程中配置用户变量，并在用户与智能体交互时存储和检索这些变量，用户变量的值在用户会话之间持久化存储，支持可读可写。​

使用限制​

  * 用户变量仅支持 String 类型。​

  * 在智能体中，最多可创建 30 个用户变量。​

  * 系统变量不支持修改、删除，不支持开启提示词访问。​

创建及使用用户变量​

你可以根据业务场景的需求，为智能体创建用户变量。创建后，你可以在提示词中为智能体声明用户变量的具体使用场景，或在工作流、插件的配置参数中引用用户变量。​

说明

  * 如果用户更新了数据（例如，用户在会话内提供了新的用户名），则智能体会自动修改变量为最新值。​

  * 如果变量被删除，则变量内保存的用户数据也会被删除。​

​

1.

创建用户变量。​

  * 在智能体的编排页面，单击变量对应的 +，然后在编辑变量对话框中，新增用户变量。重要参数说明如下表所示：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjI1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27310%27%20height=%27407%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEwIiBoZWlnaHQ9IjQwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

  * ​

配置​| 说明​  
---|---  
名称​| 用户变量的名称。​说明必须确保每个变量名在智能体内唯一，不能与智能体内的其他变量重名。​​  
描述​| 描述变量的额外信息，包括变量的用途以及任何其他重要的使用说明。​建议填写准确的变量名称与描述，以提高智能体命中用户数据的准确性。​  
默认值​| 为变量指定一个初始值。​  
开启提示词访问​| 打开启用变量开关且勾选操作列后，表示启用变量并开启提示词访问功能，即你可以在智能体的人设与提示词中使用用户变量。​仅打开启用变量开关，未勾选操作列时，表示仅支持在工作流、插件中使用该变量。​  
启用变量​| 打开启用变量开关后，你才能在工作流、插件中使用该变量。​  
  
​

2.

使用用户变量。​

  * 当你创建并启用变量后，与智能体对话时，系统会自动识别与变量匹配的内容，并将其存储至变量中。​

  * 例如在提示词中添加 称呼你的用户为{{name}}。当你在与智能体对话时，告诉智能体你的名字，系统会将你的名字记录到变量 {{name}} 中，后续智能体将根据你的名字称呼你。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27675%27%20height=%27259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc1IiBoZWlnaHQ9IjI1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

开启并使用系统变量​

系统变量默认为关闭状态，你需要先启用目标系统变量，然后可以在工作流、插件的配置参数中引用系统变量。​

1.

启用系统变量。​

  * 在智能体的编排页面，单击变量对应的 +，然后在编辑变量对话框中，找到待启用的目标系统变量，打开启用变量开关。​

  * 说明

sys_voiceprint_name、sys_voiceprint_info 和 sys_images 变量不支持手动开启。当相关功能被启用时，这些变量将自动启动并生效，无需用户手动操作。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27390%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkwIiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27337%27%20height=%27445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzM3IiBoZWlnaHQ9IjQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

使用系统变量。​

  * 启用系统变量后，你可以在插件或工作流中使用系统变量。例如在工作流中添加[飞书消息](<https://www.coze.cn/store/plugin/7395041302766944275?from=add_plugin_menu>)插件中的 get_chat_messages 工具，并设置其中的 container_id 参数引用系统变量 sys_lark_chat_id。当智能体被发布到飞书并添加到不同的飞书群后，它能够自动识别并获取当前群的 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27482%27%20height=%27385%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgyIiBoZWlnaHQ9IjM4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

用户变量示例​

以翻译大师智能体为例，定义一个用户变量 name，当用户首次使用 AI 翻译智能体时，工作流会引导用户输入他们希望被称呼的昵称，这个昵称会被赋值给用户变量 name。随后，每次用户请求翻译服务时，智能体会先亲切地使用这个昵称来称呼用户，然后再提供翻译结果。这样的个性化互动不仅增强了用户体验，也使得翻译服务更加友好和贴心。​

工作流的流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272258%27%20height=%27355.4259259259259%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI1OCIgaGVpZ2h0PSIzNTUuNDI1OTI1OTI1OTI1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

​

3.

在低代码模式区域，单击智能体开发。​

4.

根据页面提示，创建一个新智能体。​

5.

创建变量。​

a.

在智能体的编排页面，单击变量对应的 +。​

b.

在用户变量区域，设置变量的名称、描述和默认值，然后单击保存。​

  * 本示例变量名称设置为name。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27465%27%20height=%27157%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY1IiBoZWlnaHQ9IjE1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

创建工作流。​

a.

单击工作流对应的添加图标 +，然后单击创建工作流->创建工作流。​

b.

输入工作流的名称和描述，然后单击确认。​

c.

在工作流画布中编排工作流，然后试运行并发布工作流。工作流中的各个节点配置如下：​

  * ​

节点类型​| 说明​| 示例​  
---|---|---  
开始节点​| 工作流的起始节点，本示例无需配置任何输入参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27164%27%20height=%2779%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY0IiBoZWlnaHQ9Ijc5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
问答节点（询问称呼）​| 用于询问用户希望被称呼的昵称，需要设置：​
    * 提问内容：设置为你希望我称呼你为什么？​
    * 回答类型：选择直接回答。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27163%27%20height=%27302%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYzIiBoZWlnaHQ9IjMwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
变量赋值节点​| 用于为变量 name 赋值，引用问答节点（询问称呼）的输出参数。​说明如果工作流中无变量，请先前往试运行，关联有变量配置的智能体后再选择变量。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27163%27%20height=%27133%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYzIiBoZWlnaHQ9IjEzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
问答节点（询问翻译内容）​| 用于询问用户希望翻译的内容，需要设置：​
    * 提问内容：设置为你想翻译什么？​
    * 回答类型：选择直接回答。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27164%27%20height=%27296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY0IiBoZWlnaHQ9IjI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
大模型节点​| 用于翻译用户的输入内容，需要设置：​
    * 输入：引用问答节点（询问翻译内容）的输出参数。​
    * 系统提示词：设置翻译大师的人设，可以通过 AI 自动生成。​
    * 用户提示词：设置为翻译{{input}}为英文。​
    * 输出：变量名设置为 output。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27163%27%20height=%27624%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYzIiBoZWlnaHQ9IjYyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 选择返回文本模式，并设置输出变量和回答内容。​
    * 输出变量：​
    * 定义 output 参数，引用大模型节点的输出参数 output。​
    * 定义 name 参数，引用用户变量 name。​
    * 回答内容：设置为亲爱的{{name}}，你查询的译文为{{output}}。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27162%27%20height=%27191%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYyIiBoZWlnaHQ9IjE5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

d.

将工作流添加到智能体。​

7.

配置人设与回复逻辑。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27505%27%20height=%27264%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA1IiBoZWlnaHQ9IjI2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

测试智能体效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27510%27%20height=%27253%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEwIiBoZWlnaHQ9IjI1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

系统变量示例​

以搭建飞书聊天总结智能体为例，你可以在工作流中添加[飞书消息](<https://www.coze.cn/store/plugin/7395041302766944275?from=add_plugin_menu>)插件中的 get_chat_messages 工具， 以获取飞书群内的聊天消息。同时，添加大模型节点，借助其强大的语言处理能力对聊天记录进行智能总结。在设置过程中，设置 get_chat_messages 工具中的 container_id 参数引用系统变量 sys_lark_chat_id，从而动态获取目标群的 ID。当智能体被添加到不同的飞书群时，它能够自动识别并获取当前群的 ID，并对该群内的聊天消息进行高效总结。​

工作流如下所示：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271809%27%20height=%27275.55697674418604%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgwOSIgaGVpZ2h0PSIyNzUuNTU2OTc2NzQ0MTg2MDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

​

3.

在低代码模式区域，单击智能体开发。​

4.

根据页面提示，创建一个新智能体。​

5.

发布智能体到飞书。​

a.

单击右上角的发布。​

b.

勾选飞书，然后单击发布。​

  * 首次发布时需要进行授权，根据引导完成授权。​

5.

记录飞书应用的 ID 和 Secret。​

  * 发布到飞书后，系统将默认在[飞书开发者后台](<https://open.larkoffice.com/app?lang=zh-CN>)创建一个与智能体同名的飞书应用。记录该应用的 ID 和 Secret，在搭建工作流时，需输入该信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27542%27%20height=%2792%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQyIiBoZWlnaHQ9IjkyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

6.

开启系统变量 sys_lark_chat_id。​

  * 返回到智能体，单击变量对应的 +，然后启用系统变量 sys_lark_chat_id。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27382%27%20height=%27140%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgyIiBoZWlnaHQ9IjE0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

创建工作流。​

a.

单击工作流对应的 +，然后选择创建工作流->创建工作流。​

b.

输入工作流的名称和描述，然后单击确认。​

c.

在工作流画布中编排工作流。​

  * 工作流中的各个节点配置如下：​

  * ​

节点类型​| 说明​| 示例​  
---|---|---  
开始节点​| 工作流的起始节点，本示例无需配置任何输入参数。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27568%27%20height=%27314.95734597156394%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY4IiBoZWlnaHQ9IjMxNC45NTczNDU5NzE1NjM5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
插件节点​| 添加飞书消息插件中的 get_chat_messages 工具，用于获取指定单聊或群聊的消息记录，需要设置：​
    * container_id：引用系统变量 sys_lark_chat_id。当智能体被添加到飞书群后，将获取到该群的 ID，并总结该群的消息。​
    * appid：输入智能体所在飞书开放平台应用的 ID，即你在上述步骤 5 中获取的应用的 ID。​
    * appsecret：输入智能体所在飞书开放平台应用的 Secret，即你在上述步骤 5 中获取的应用的 Secret。​
​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27362%27%20height=%27521.5545023696683%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYyIiBoZWlnaHQ9IjUyMS41NTQ1MDIzNjk2NjgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
大模型节点​| 用于总结飞书聊天记录，需要设置：​
    * 输入：引用 get_chat_messages 节点的 data 参数。​
    * 系统提示词：设置聊天总结的人设，可以通过 AI 自动生成。​
    * 用户提示词：设置为总结{{input}}。​
    * 输出：变量名设置为 output。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27368%27%20height=%271156.3222748815165%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY4IiBoZWlnaHQ9IjExNTYuMzIyMjc0ODgxNTE2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 选择返回文本模式，并设置输出变量和回答内容。​
    * 输出变量：定义 output 参数，引用大模型节点的输出参数 output。​
    * 回答内容：设置为{{output}}。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27384%27%20height=%27418.5781990521327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg0IiBoZWlnaHQ9IjQxOC41NzgxOTkwNTIxMzI3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

d.

发布工作流。​

e.

将工作流添加到智能体。​

8.

配置人设与回复逻辑。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27305%27%20height=%27194%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA1IiBoZWlnaHQ9IjE5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

9.

重新发布智能体到飞书。​

10.

测试智能体效果。​

  * 在飞书群里，通过添加机器人方式，将智能体添加到飞书群中，并测试智能体效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27315%27%20height=%27439%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE1IiBoZWlnaHQ9IjQzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

相关操作​

查看变量值​

你可以在智能体编排页面的右上角，选择记忆 > 变量，查看变量值。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27715%27%20height=%27134%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzE1IiBoZWlnaHQ9IjEzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271244%27%20height=%27265.3080568720379%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI0NCIgaGVpZ2h0PSIyNjUuMzA4MDU2ODcyMDM3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

​

上一篇

为低代码智能体添加知识

下一篇

数据库