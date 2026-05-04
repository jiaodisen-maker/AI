---
source_url: https://docs.coze.cn/guides/chatflow_in_app
title: '为低代码应用编排对话流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:22Z
---

# 为低代码应用编排对话流 - 文档 - 扣子

为低代码应用编排对话流

什么是对话流​

对话流是基于对话场景的特殊工作流，专门用于处理对话类请求。对话流通过对话的方式和用户交互，并完成复杂的业务逻辑。在低代码应用中添加对话流，将对话中的用户指令拆分为一个个步骤节点，并为其设计用户界面，你可以搭建出适用于移动端或网页端的对话式低代码应用，实现自动化、智能化的对话流程。​

相较于工作流而言，对话流更适合处理对话场景下的交互逻辑。每个对话流都绑定了一个会话，运行时可以从此会话中读取历史消息，同时将本次运行对话流产生的消息记录在这个会话中，相当于一个拥有了记忆的工作流。对话流适用于 Chatbot 等需要在响应请求时进行复杂逻辑处理的对话式应用程序，例如智能客服、虚拟伴侣等。​

关于工作流与对话流的区别，可参考​工作流与对话流。​

对话流与会话​

会话指的是用户与模型之间基于同一主题的一系列连续的对话交互，会话中存储用户输入的消息和模型回复的消息。包括：​

  * 用户的输入：用户通过开始节点和输入节点传入的内容。​

  * 对话流的输出：对话流通过输出节点和结束节点输出的内容。​

和低代码智能体对话，或者调用​发起对话 API 时，扣子编程会自动创建会话，并将用户输入和模型输出的消息保存到会话中。在扣子编程搭建对话类的低代码应用时，你需要自行创建一个对话流和会话，编排对话的后端处理流程。你可以在低代码应用中创建空会话，并绑定对话流，对话流执行时用户输入和对话流输出会作为消息保存在此会话中，再次执行对话流时，这些已保存的消息可以作为上下文传递给大模型节点，以便模型生成更符合对话语境的回复。​

在低代码应用中搭建对话流​

创建对话流和会话​

参考以下步骤在低代码应用中创建一个对话流，并为其绑定同名会话。指定对话流时产生的用户输入和对话流输出会以消息形式保存在会话中。你也可以预先创建一个会话，详细说明可参考​管理低代码应用会话。​

1.

在项目管理页面，找到你已经创建的低代码应用。​

2.

在业务逻辑页面资源面板的工作流区域单击 + > 新建对话流。​

3.

填写对话流的基本信息，并选择是否创建会话。​

  * 对话流名称：对话流的名称，在同一低代码应用中不可重复。​

  * 创建并绑定同名会话：是否创建一个同名的会话，并绑定这个对话流。绑定后，对话流输入参数的 CONVERSATION_NAME 默认为这个同名对话，表示对话流运行时可以从此会话中读取历史消息，同时将本次运行对话流产生的消息记录在这个会话中。​

  * 对话流描述：对话流的描述信息。​

4.

单击确认。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272716%27%20height=%271266.837962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcxNiIgaGVpZ2h0PSIxMjY2LjgzNzk2Mjk2Mjk2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

编排对话流​

对话流中有两个默认节点，即开始节点和结束节点。将对话中需要处理的复杂逻辑拆分为一个个的步骤，每个步骤对应对话中的一个节点，在对话流画布中添加这些节点并将其连接起来。​

例如添加一个大模型节点，用于接收用户的提问，并由模型生成回复。​

1.

在工作流画布下方单击添加节点，并选择大模型节点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27425%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI1IiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

将开始节点、大模型节点和结束节点按顺序连接起来。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272238%27%20height=%27481.0902612826603%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzOCIgaGVpZ2h0PSI0ODEuMDkwMjYxMjgyNjYwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

配置对话流开始节点。​

  * 对话流的开始节点包含两个默认输入参数，你也可以按需定义其他输入参数。​

  * USER_INPUT：用户在对话流的本轮对话中输入的内容。String 类型，无默认值。你可以按需设置一个默认值，设置后，如果用户没有在对话中输入任何信息，系统会将这个默认值作为用户输入。​

  * CONVERSATION_NAME：对话流绑定的会话。String 类型，如果创建对话流时设置了同名会话，则默认值为同名会话；若未设置，则默认为 Default 会话。运行对话流中会向 CONVERSATION_NAME 指定的会话写入消息、可以从此对话中读取历史消息。​

4.

配置大模型节点。​

  * 为大模型设置输入参数和用户提示词，并开启对话历史。大模型节点的配置说明可参考​大模型节点。​

  * 输入参数：大模型节点有默认参数 input，你可以为其指定一个值，便于在系统提示词和用户提示中设置动态的内容。例如指定 input 参数引用开始节点的 USER_INPUT 参数。​

  * 开启对话历史：开启对话历史功能后，扣子编程会将会话中已存的近期消息作为对话历史传递给大模型，供大模型生成回复时作为参考，生成更符合语境的回复。​

  * 用户提示词：对话中的用户问题。你可以直接引用输入参数中定义的变量 {{input}}，表示使用开始节点的 USER_INPUT 参数作为用户提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcyIiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

配置结束节点。​

  * 对话流的结束节点与工作流完全相同，你可以选择返回文本，并直接引用大模型的输出参数作为回答内容。​

  * 输出变量：为默认的输出变量 output 设置参数值，引用大模型节点的输出参数 output。​

  * 回答内容：直接引用结束节点定义的输出变量 {{output}}。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27474%27%20height=%27271%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc0IiBoZWlnaHQ9IjI3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

试运行对话流​

完成对话流的编排之后，你可以在低代码应用的对话流画布中试运行对话流，查看对话流的运行效果。​

试运行流程​

1.

在对话流画布下方单击试运行。​

2.

填写对话流入参配置。​

  * 根据页面提示选择一个会话。此处默认展示对话流开始节点 CONVERSATION_NAME 中指定的默认会话，你也可以从列表中选择其他会话。试运行时可以选择开发者手动创建的静态会话，也可以选择创建会话节点创建的动态会话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27165%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTY1IiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

单击保存并开始对话调试。​

4.

在输入框中输入一段内容，并按回车键发送。​

  * 如果你在对话流的开始节点设置了 USER_INPUT 参数的默认值，那么这个默认值会自动填写在输入框，作为你的输入参考。​

5.

扣子编程会自动运行对话流，并在试运行面板中展示你的输入和对话流执行的返回结果。​

  * 对话流的试运行面板默认为对话式，类似智能体的调试区域，展示每一次试运行此工作流时用户和模型的对话交互过程。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27161%27%20height=%27246%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYxIiBoZWlnaHQ9IjI0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看试运行结果​

试运行对话流时可以查看对话中各个节点的运行流程、调试数据及已存对话。​

​

操作​| 说明​| 示例​  
---|---|---  
查看各个节点的输入输出​| 在对话流画布各个节点下方单击展开结果，查看每个节点的输入与输出、运行状态，判断每个节点的运行过程与结果是否符合预期。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271802%27%20height=%27665.3538461538462%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgwMiIgaGVpZ2h0PSI2NjUuMzUzODQ2MTUzODQ2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
查看调试流程​| 单击试运行左侧的调试图标，页面会自动展示调试区域。调试区域中包含三个页面，你可以在调试页面中查看对话流的详细执行过程，包括树状图、火焰图或列表形式的调用流程。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272300%27%20height=%271315.438596491228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMwMCIgaGVpZ2h0PSIxMzE1LjQzODU5NjQ5MTIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
查看已存会话​| 会话管理页签展示低代码应用中所有已创建的会话及其消息内容，包括静态会话和动态会话。此处展示的会话中，消息内容是草稿态的调试数据，和线上数据互相隔离。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272830%27%20height=%271330.5964912280701%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgzMCIgaGVpZ2h0PSIxMzMwLjU5NjQ5MTIyODA3MDEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
  
​

​

上一篇

编排业务逻辑

下一篇

管理低代码应用会话