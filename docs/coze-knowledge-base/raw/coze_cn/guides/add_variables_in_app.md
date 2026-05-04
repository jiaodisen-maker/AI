---
source_url: https://docs.coze.cn/guides/add_variables_in_app
title: '为低代码应用设置变量 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:28Z
---

# 为低代码应用设置变量 - 文档 - 扣子

为低代码应用设置变量

你可以通过创建变量来保存用户维度的个人信息，并让模型记住这些特征，使回复更加个性化。​

什么是变量​

变量用来存储数据值，可以在低代码应用运行期间保存和修改数据。通过变量，可以存储动态变化的信息，使低代码应用能够根据不同情况灵活调整，满足用户的特定需求和偏好。​

低代码应用支持系统变量、应用变量和用户变量，详细说明如下：​

  * 系统变量：系统为低代码应用自动创建用户信息、飞书等类别的系统变量，默认全部关闭，为不可用状态，你可以根据实际业务需求选择开启需要的系统变量。开启后，系统在用户请求时自动产生变量数据，这些数据是只读的，不可由用户或开发者修改。​

  * 应用变量：应用变量本质是内存变量，每执行一次工作流，应用变量就会自动恢复到最初设定的默认值，就像游戏中的生命值，每次开始新的一局游戏时，生命值都会重置为游戏设定的初始值。​

  * 用户变量：用户变量用于存储每个用户在使用低代码应用过程中，需要持久化存储和读取的数据，例如用户的个性化设置、语言偏好、历史交互记录等。​

关于这三种变量的详细说明，可参考​变量类型。​

开发者为低代码应用定义变量之后，可以通过工作流的变量赋值节点为变量赋值，其他节点可以读取变量值并进行下一步的逻辑判断。例如英语学习场景中，可以为低代码应用设置一个英语水平的数值类型变量，随着学习进度逐渐提高此变量的值，并基于变量值向学员展示对应英语水平的学习内容。​

变量类型​

开发低代码应用时，可以通过系统变量、应用变量和用户变量来满足不同的业务需求和场景。每种变量类型都有其特定的用途和优势，以下是对这些变量类型的介绍说明。​

系统变量​

系统默认创建用户信息、飞书等类别的系统变量，你不可以新增、修改、删除默认的系统变量。这些系统变量默认全部关闭，为不可用状态，你可以根据实际业务需求选择开启需要的系统变量。开启后，系统在用户请求时自动产生变量数据，这些数据是只读的，但不可由用户或开发者修改。通过问答、结束等工作流节点可以获取系统变量值，变量名称必须与低代码应用中设置的变量名称一致。​

扣子默认创建的系统变量如下，每个变量获取的数据不同，支持使用的渠道也不同。​

​

变量分类​| 变量名称​| 变量描述​| 数据类型​| 支持渠道​  
---|---|---|---|---  
用户信息​| sys_uuid​| 扣子账号 UID、发布渠道 ID 与低代码应用 ID 组合后的编码值，用于识别和追踪用户行为。​sys_uuid并非扣子账号的 UID。​| String​| 全部渠道​  
飞书​| sys_lark_chat_id​| 飞书群的群 ID。详细说明可参考[群 ID 说明](<https://open.larkoffice.com/document/server-docs/group/chat/chat-id-description#394516c9>)。​例如搭建用于总结飞书群消息的低代码应用时，可以在工作流中添加[飞书消息](<https://www.coze.cn/store/plugin/7395041302766944275?from=add_plugin_menu>)插件中的get_chat_messages工具，并设置工具中的 container_id 参数引用 sys_lark_chat_id 变量，当低代码应用被添加到不同的飞书群时，它能够自动识别并获取当前群的 ID，并对该群内的聊天消息进行高效总结。​| String​| 飞书​  
​| sys_lark_chat_mode​| 飞书群的群模式，包括普通对话群组、话题群组和单聊。详细说明，请参考[群组管理概述](<https://open.larkoffice.com/document/server-docs/group/chat/intro>)。​在开发团队协作助手应用中，通过获取sys_lark_chat_mode变量，能够根据聊天模式（如群聊或私聊）动态调整低代码应用的功能和界面布局。例如，在群聊模式下，低代码应用可以提供任务分配、项目进度更新等协作功能，促进团队成员之间的信息共享和任务协同。​| String​| 飞书​  
​| sys_lark_open_id​| 飞书用户在低代码应用内的身份 ID。详细说明，请参考[用户身份](<https://open.larkoffice.com/document/home/user-identity-introduction/introduction>)。​例如在搭建智能客服应用时，可以引用系统变量 sys_lark_open_id，当低代码应用被发布到飞书后，可以识别并验证用户身份，根据用户的历史咨询记录和偏好，提供定制化的服务建议，提高客服效率和用户满意度。​| String​| 飞书​  
​| sys_lark_thread_id​| 飞书的话题 ID，详细说明可参考[话题概述](<https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/thread-introduction>)。​例如搭建基于话题的知识管理应用时，可以在工作流中添加[飞书消息](<https://www.coze.cn/store/plugin/7395041302766944275?from=add_plugin_menu>)插件中的 get_thread_messages 工具，并设置工具中的 container_id 参数引用 sys_lark_thread_id 变量。当低代码应用被添加到飞书群时，它能够自动获取历史话题的 ID，并根据话题 ID 对信息进行分类和整理。​| String​| 飞书​  
  
​

使用场景​

  * 用户识别：使用系统变量来识别和区分不同的用户，例如可以通过系统变量 sys_uuid 获取用户唯一 ID，以识别和追踪用户行为。 ​

  * 渠道特定功能：如果低代码应用需要在不同的渠道上运行，系统变量可以用来识别渠道并触发特定功能，目前支持飞书渠道的系统变量。例如可以通过系统变量 sys_lark_open_id 获取飞书用户在应用内的身份 ID，以识别和关联用户在飞书平台上的行为，例如消息发送、文件共享等，从而提供更加个性化的服务和响应。​

示例​

例如，搭建一个家居商品推荐应用，它需要根据每个用户的喜好来推荐家居用品。在这个低代码应用中，系统变量 sys_uuid 作为用户的唯一 ID，用于追踪用户的家居偏好。​

1.

你可以在数据库中定义 sys_uuid 和 favor 字段，分别用于存储用户 ID 和喜好关键字。​

2.

通过问答节点等方式获取用户喜好之后，通过新增数据节点将其添加到数据库中。​

3.

在新增数据节点中，sys_uuid 字段值可以直接引用家居商品推荐应用中已定义的系统变量 sys_uuid。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27696%27%20height=%27302%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjk2IiBoZWlnaHQ9IjMwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

应用变量​

应用变量本质是内存变量，每执行一次工作流，应用变量就会自动恢复到最初设定的默认值，就像游戏中的生命值，每次开始新的一局游戏时，生命值都会重置为游戏设定的初始值。应用变量支持可读可写。​

使用场景​

  * 状态跟踪：应用变量可以用来跟踪用户的状态，例如在一个游戏应用中，可以定义应用变量player_health_points，默认生命值设定为 100，随着游戏进程的推进，玩家会遭遇各种挑战和障碍，生命值逐渐减少。当player_health_points降至 0 时，游戏结束。重新开始游戏时，player_health_points值恢复到 100。 ​

  * 缓存数据：应用变量可以用来存储频繁访问的数据，以减少数据库查询，提高应用性能。例如定义应用变量news，用来存储每天最新的一条 AI 新闻，当用户要查询 AI 新闻时，可以直接通过访问变量news来获取新闻。 ​

示例​

例如，搭建一个猜谜游戏工作流，定义一个应用变量score，默认值设置为 0 。在工作流中添加变量赋值节点，每猜对一个谜语，变量score数值加 1，重新开始新的一局游戏时，score都会重置为游戏设定的初始值 0。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27680%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgwIiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

用户变量​

用户变量用于存储每个用户在使用低代码应用过程中，需要持久化存储和读取的数据，例如用户的个性化设置、语言偏好、历史交互记录等。开发者可以在扣子编程中配置用户变量，并在用户与低代码应用交互时存储和检索这些变量，用户变量的值在用户会话之间持久化存储，支持可读可写。​

使用场景​

  * 个性化体验：用户变量可以存储用户的偏好设置，以提供个性化的用户体验。例如在一个音乐流媒体服务应用中，可以定义用户变量user_music_preferences，用来存储用户最喜欢的音乐类型，以实现根据用户的偏好提供个性化的歌单。 ​

  * 历史数据：用户变量可以用来存储用户的历史行为数据，例如可以定义用户变量purchase_record，用来存储用户的购买记录，根据用户的购买历史向用户推荐同类或关联商品。 ​

示例​

例如，搭建一个 AI 翻译应用，定义一个用户变量name，当用户首次使用 AI 翻译应用时，工作流会引导用户输入他们希望被称呼的昵称，这个昵称会被赋值给用户变量name。随后，每次用户请求翻译服务时，低代码应用会先亲切地使用这个昵称来称呼用户，然后再提供翻译结果。这样的个性化互动不仅增强了用户体验，也使得 AI 翻译服务更加友好和贴心。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27671%27%20height=%27285%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjcxIiBoZWlnaHQ9IjI4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

限制说明​

定义和使用变量时，请了解以下限制：​

  * 定义变量时，必须确保每个变量名在低代码应用内唯一，不能与低代码应用内的其他变量重名。​

  * 系统变量是只读的，不能修改或删除，用户变量和应用变量没有此限制。​

定义变量​

创建低代码应用之后，扣子编程默认为应用添加系统变量。你也可以根据业务场景的需求，为应用添加用户变量或应用变量。​

注意

修改变量，例如修改变量的名称、数据类型，可能会影响使用此变量的工作流的运行。因此，如果要修改变量，请同步更新工作流中的变量配置。​

​

为低代码应用定义变量的操作步骤如下：​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击项目管理。​

3.

在项目管理页面，找到你已经创建的低代码应用。​

4.

在业务逻辑页面的左侧资源区域单击变量。​

5.

展开应用变量或用户变量，然后单击 \+ 新增子项，填写变量信息。​

  * 名称：变量的名称，用于在工作流节点中标识和引用变量的标识符，例如变量赋值节点，必须确保每个变量名在低代码应用内唯一。​

  * 描述：描述提供了变量的额外信息，包括变量的用途以及任何其他重要的使用说明。​

  * 数据类型：数据类型定义了变量可以存储的数据种类，应用变量支持以下全部数据类型，而用户变量仅支持 String 类型。​

  * String：字符串，用于存储文本数据，例如单词、句子或字符序列。 ​

  * Integer：整数，用于存储不带小数部分的整数，例如 -3、0、1024 等。 ​

  * Boolean：布尔值，只有两个值true 和 false，常用于逻辑判断和条件控制。 ​

  * Number：数值，用于存储带小数部分的数值，包括整数和浮点数，例如 3.14、-0.001 等。 ​

  * Object：对象，用于存储键值对集合，可以表示复杂的数据结构，例如 JSON 对象。 ​

  * Array<String>：字符串数组，用于存储一系列字符串，每个元素都是 String 类型。 ​

  * Array<Integer>：整数数组，用于存储一系列整数，每个元素都是 Integer 类型。 ​

  * Array<Boolean>：布尔值数组，用于存储一系列布尔值，每个元素都是 Boolean 类型。 ​

  * Array<Number>：数值数组，用于存储一系列数值，每个元素都是 Number 类型。 ​

  * Array<Object>：对象数组，用于存储一系列对象，每个元素都是 Object 类型。​

  * 默认值：默认值是变量在未赋值时的初始值。​

  * 变量开关：用于控制是否启用变量，对于计划使用的变量，在操作列打开开关按钮。此开关关闭时，低代码应用中所有工作流都无法使用这个变量，例如为这个变量赋值，或读取变量值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27533%27%20height=%27230%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMzIiBoZWlnaHQ9IjIzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

6.

单击保存。​

读取变量值​

你可以通过工作流中的节点来读取系统变量、用户变量和应用变量的值。要读取这些变量，只需在工作流节点中定义一个参数，并将所需变量的值赋给这个参数。这样，你就可以通过访问这个参数来读取变量的值。​

说明

目前，除了开始节点、输入节点、知识库写入节点外，其他所有节点都能读取变量值。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27273%27%20height=%27293%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjczIiBoZWlnaHQ9IjI5MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

例如，搭建一个 AI 翻译应用时，可以设定一个用户变量name。用户首次使用应用时，系统会提示他们输入昵称，该昵称将存储在name变量中。翻译任务通过大模型节点执行，完成后，结束节点会读取name变量的值，并用昵称称呼用户，随后展示翻译结果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27471%27%20height=%27240%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcxIiBoZWlnaHQ9IjI0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

为变量赋值​

在低代码应用中定义变量时，可以为变量设置一个默认值，否则工作流中首次读取变量值时可能会读取到空值，影响后续的逻辑判断。你也可以通过工作流的变量赋值节点为变量赋值，新的变量值对整个应用中所有工作流生效。​

在变量赋值节点中，在输入中添加需要赋值的参数。字段名设置为需要赋值的应用变量名称，变量值可以设置为固定值，也可以引用上游节点的输出参数，详情可参考​变量赋值节点。​

例如添加一个工作流，专门用于为变量name赋值。该工作流可包装为设置用户昵称的功能。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27479%27%20height=%27244%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc5IiBoZWlnaHQ9IjI0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

恢复变量默认值​

应用变量本质是内存变量，每次重新打开低代码应用或发起一个新的请求时，应用变量就会自动恢复到最初设定的默认值。​

例如，搭建一个猜谜游戏工作流，并定义一个应用变量score，默认值设置为 0 。在工作流中添加变量赋值节点，每猜对一个谜语，变量score数值加 1，重新开始新的一局游戏时，score都会重置为游戏设定的初始值 0。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27525%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI1IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看变量值​

你可以在变量页面的测试数据页签下查看系统中存储的变量值。请注意，你只能查看系统变量和用户变量存储的变量值，因为这些变量会被持久化存储。而应用变量仅临时保存，并在会话结束时消失，因此无法查看应用变量的变量值。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27461%27%20height=%27204%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYxIiBoZWlnaHQ9IjIwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

管理低代码应用资源

下一篇

为低代码应用添加知识库