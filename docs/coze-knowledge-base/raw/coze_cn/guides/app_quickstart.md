---
source_url: https://docs.coze.cn/guides/app_quickstart
title: '开发一个 AI 翻译应用 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:52Z
---

# 开发一个 AI 翻译应用 - 文档 - 扣子

开发一个 AI 翻译应用

​

随着人工智能技术的不断进步，大模型在翻译质量、效率、上下文理解和多语言支持等方面表现出色。因此，越来越多的人开始使用大模型进行文本翻译，以提升效率，降低成本。​

本教程详细指导你如何在扣子编程中完成一个网页端 AI 翻译应用的开发。​

AI 翻译应用介绍​

这个 AI 翻译应用支持用户选择目标翻译语言，在输入文本内容后，点击开始翻译就可以获得到大模型的翻译结果了。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27614%27%20height=%27285%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3fbbfc46746a435aa94ea5b97562f371~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤一：设计你的低代码应用功能​

首先，你需要进行应用设计，规划应用的主体功能和用户界面。​

这个 AI 翻译应用的核心功能是能够满足用户的文本翻译需求，并支持用户选择指定翻译的语言。翻译功能可以通过创建一个包含大模型节点的工作流来实现。​

基于以上功能规划，这个应用的用户界面会包含以下组件：​

  * 一个让用户可以输入翻译内容的区域​

  * 一个让用户选择翻译语言的列表​

  * 一个翻译按钮来触发翻译操作​

  * 一个展示翻译结果的内容区域​

完成主体功能设计和规划后，就可以开始搭建低代码应用了。​

步骤二：创建低代码应用项目​

首先，你需要创建一个低代码应用项目。​

低代码应用项目支持使用工作流来完成复杂的业务逻辑编排，也支持使用数据库、知识库、插件等资源实现与本地数据或线上数据的交互。此外，低代码应用项目支持通过拖拉拽的方式搭建用户界面，并且能够实现与业务逻辑的联动。​

参考以下操作，创建低代码应用项目。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

3.

在低代码模式区域，将鼠标移动到更多，然后单击打开应用开发。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27451%27%20height=%27264%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUxIiBoZWlnaHQ9IjI2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在应用模板页面，单击空白应用。​

5.

输入应用名称，并单击图标旁的 AI 图标使用 AI 自动生成一个图标。然后单击确定。​

  * 应用创建成功后，你会直接进入到应用的集成开发环境 (IDE)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27279%27%20height=%27280%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc5IiBoZWlnaHQ9IjI4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：编排业务逻辑​

创建完低代码应用项目后，你可以开始进行业务逻辑编排了。扣子编程提供了大模型、代码、意图识别、知识库写入与检索等丰富的工作流节点，以满足复杂的业务场景需求。此外，你还可以通过使用变量、插件、知识库等方式与你的本地数据和线上数据进行集成。​

本教程中的 AI 翻译应用，主要是使用大模型实现多语言翻译，所以只需要创建一个包含大模型节点的工作流即可。​

参考以下步骤，创建一个实现翻译功能的工作流。​

1.

在业务逻辑页面，找到工作流，然后单击 \+ > 新建工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27682%27%20height=%27100%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgyIiBoZWlnaHQ9IjEwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

输入工作流名称和描述，然后单击确认。​

  * 说明

工作流名称只支持字母、数字和下划线，且必须以字母开头。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27332%27%20height=%27328%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMyIiBoZWlnaHQ9IjMyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在工作流画布，单击开始节点的连接线或画布下方的添加节点按钮，然后选择大模型节点，并完成连线。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27578%27%20height=%27361%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTc4IiBoZWlnaHQ9IjM2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击开始节点进行配置。开始节点用于设定启动工作流需要的信息。​

  * 本场景中，用户需要提供要翻译的内容和目标语言，所以需要配置两个对应的输入参数。​

i.

在输入区域，单击 \+ 图标，配置第一个变量 (content) 用于传入用户要翻译的内容。​

ii.

再次单击 \+ 图标。输入第二个变量 (lang) 用来指定目标语言。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27348%27%20height=%27217.99999999999997%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ4IiBoZWlnaHQ9IjIxNy45OTk5OTk5OTk5OTk5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击大模型节点进行配置。​

i.

在模型区域，展开模型列表，选择用来执行翻译任务的大模型。例如选择豆包·1.8·深度思考模型。​

  * 如果你想调整模型配置，单击配置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27476%27%20height=%27180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc2IiBoZWlnaHQ9IjE4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

ii.

配置输入参数，这些输入参数可以在模型提示词中使用。​

  * 本教程中需要将用户输入的译文内容和目标语言添加到提示词中，让模型按照用户选择的语言进行翻译。所以需要配置两个输入参数。​

a.

单击输入区域的+图标，然后点击对应的设置图标，选择开始节点中配置的变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27454%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU0IiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

重复上述操作，再添加目标语言的这个变量。​

  * 删除不需要的输入信息，确保输入中只包含下图中的这两个参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27342%27%20height=%27138%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQyIiBoZWlnaHQ9IjEzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

iii.

在系统提示词区域，输入以下内容作为系统提示词。​

  * 系统提示词是一组指示模型行为和功能范围的指令，可以包括如何提问、如何提供信息、如何请求特定功能等。系统提示词也用于设定对话的边界，比如告知用户哪些类型的问题或请求是不被接受的。​

  * ​

Plain Text

复制

# 角色​

你是一个专业的翻译官，能够准确地将用户输入的内容翻译成目标语言，不进行随意扩写。​

​

## 技能​

### 技能 1：翻译文本​

1\. 当用户提供一段文本时，迅速将其翻译成目标语言。​

2\. 确保翻译的准确性和流畅性。​

​

## 限制：​

\- 只进行翻译工作，不回答与翻译无关的问题。​

\- 严格按照用户要求的目标语言进行翻译，不得擅自更改。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27362%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI2IiBoZWlnaHQ9IjM2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

iv.

在用户提示词区域，输入用户提示词。​

  * 用户提示词通常是直接的命令，告诉模型要执行的任务或意图。例如“帮我翻译下这段内容”，指令越清晰，模型的输出也更贴近你的实际需求。​

a.

首先输入以下内容。​

  * ​

Plain Text

复制

将用户输入的内容翻译成目标语言。​

​

  * 因为不同用户提供的翻译内容，选择的目标语言都不同，所以需要将译文内容和目标语言使用输入变量来指代，这样就可以在运行时替换成真实的用户需求。​

b.

在“内容”文字后输入{，然后选择指代翻译内容的变量。​

  * 说明

如果你没有可用的变量，请检查是否按照教程配置了模型节点的输入变量。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27436%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM2IiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

重复上述方法，添加目标语言变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27315%27%20height=%27323%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE1IiBoZWlnaHQ9IjMyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

v.

在输出区域，将输出格式配置为文本，使用默认配置的output变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27379%27%20height=%27111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc5IiBoZWlnaHQ9IjExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

连接大模型节点与结束节点，然后选择结束节点进行配置。​

a.

单击结束节点，然后选择返回文本。​

b.

选择大模型节点的输出结果作为输出变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27532%27%20height=%27327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMyIiBoZWlnaHQ9IjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

在回答内容文本框中输入{{output}}，使用大模型的翻译内容作为最终的回复。​

d.

开启流式输出，实现打字机一样的输出效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27332%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjMzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 至此，你已经完成整个工作流的搭建。​

7.

为了保证业务逻辑实现符合预期，单击试运行测试工作流的执行。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27508%27%20height=%27133%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA4IiBoZWlnaHQ9IjEzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

在试运行页面，输入要翻译的内容和目标语言，然后单击试运行。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27216%27%20height=%27371%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE2IiBoZWlnaHQ9IjM3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

9.

查看运行结果是否符合预期。​

  * 如果不符合预期，你可以逐一检查每个节点的输出结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27229%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI5IiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在完成业务逻辑搭建并通过测试后，你就可以开始用户界面搭建了。​

步骤四：搭建用户界面​

​

扣子编程提供了可视化的用户界面搭建能力，你可以通过拖拉拽的方式搭建一个用户界面，无需写一行代码。​

参考以下操作，搭建网页端翻译应用的用户界面。​

1.

在应用 IDE，单击页面上方的用户界面页签。​

2.

选择桌面网页，然后单击开始搭建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27391%27%20height=%27289%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkxIiBoZWlnaHQ9IjI4OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

添加页面组件，完成页面搭建。​

  * 翻译页面由3个块级组成，具体使用的组件和配置请参考下述步骤。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27499%27%20height=%27225%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk5IiBoZWlnaHQ9IjIyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

1 搭建页面结构​

整体上 AI 翻译应用的用户界面由上下两个部分组成。​

  * 上面是标题区域。​

  * 下面是功能区域。功能区域又分为左右两个区域。​

想要实现这样的页面结构就需要使用容器组件。容器组件是用来进行页面布局的，可以把页面划分成不同的区域和排列顺序。容器组件中可以添加其他各种组件例如文本组件、按钮组件等。​

参考以下操作，完成页面布局：​

1.

确认画布的排列方向为纵向。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27625%27%20height=%27354%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI1IiBoZWlnaHQ9IjM1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在组件面板中，找到布局组件 > 容器组件，然后将容器组件拖入到中间的画布中。​

3.

在画布中，选中拖入的容器组件。组件名称为Div1。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27628%27%20height=%27197%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI4IiBoZWlnaHQ9IjE5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

参考以下配置，修改容器组件Div1的属性。​

  * ​

Div1的属性设置​| 示例​  
---|---  
设置尺寸和布局。​
    * 将宽度设置为填充容器（即100%）。​
    * 将高度设置为60 px。​
    * 将排列方向设置为横向。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272366%27%20height=%27659.3770491803278%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM2NiIgaGVpZ2h0PSI2NTkuMzc3MDQ5MTgwMzI3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
设置样式。​
    * 找到填充属性，然后单击删除图标去掉背景色。​
    * 将边框设置为灰色。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271926%27%20height=%271073.5081967213114%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyNiIgaGVpZ2h0PSIxMDczLjUwODE5NjcyMTMxMTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

5.

再拖入一个容器组件用来组织功能区，并在画布中选中该组件。组件名称为Div2。然后选中该组件，参考下表中的属性配置进行修改。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27674%27%20height=%27210%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc0IiBoZWlnaHQ9IjIxMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

Div2的属性设置​| 示例​  
---|---  
    * 设置尺寸，将宽度和高度都设置为填充容器（即100%）。​
    * 排列方向设置为横向。​
    * 设置样式。找到填充属性，然后单击删除图标去掉背景色。​
​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271958%27%20height=%271000.9179104477612%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1OCIgaGVpZ2h0PSIxMDAwLjkxNzkxMDQ0Nzc2MTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

6.

向画布的容器组件Div2的左侧区域中，拖入一个容器组件Div3，用来组织左侧的内容翻译区域。然后选中该组件，参考下表中的属性配置进行修改。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27228%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg1IiBoZWlnaHQ9IjIyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

Div3的属性设置​| 示例​  
---|---  
    * 将宽度设置为50%。​
    * 将高度设置为固定值550px。​
    * 删除背景色。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271950%27%20height=%27935.7758620689655%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1MCIgaGVpZ2h0PSI5MzUuNzc1ODYyMDY4OTY1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

7.

向画布中容器组件Div2的右侧区域中，拖入一个容器组件Div4，用来组织右侧的翻译结果区域。然后选中该组件，参考下表中的属性配置进行修改。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27630%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMwIiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

Div4的属性设置​| 示例​  
---|---  
    * 将宽度设置为50%。​
    * 将高度设置为固定值550px。​
    * 删除背景色。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271993%27%20height=%27886.9945054945055%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk5MyIgaGVpZ2h0PSI4ODYuOTk0NTA1NDk0NTA1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

至此，我们就完成了这个翻译应用的页面结构搭建。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27444%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ0IiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2 搭建页面标题​

参考以下操作，搭建页面的标题区域。​

1.

在组件面板中，找到推荐组件 > 文本组件，然后将文本组件拖入到顶部的容器组件Div1上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27680%27%20height=%27127%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgwIiBoZWlnaHQ9IjEyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

2.

在画布中，选中拖入的文本组件，然后在右侧的属性面板中设置文本内容，字号大小等。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27287%27%20height=%27214%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg3IiBoZWlnaHQ9IjIxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

至此，你已经完成了标题区域的搭建。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27541%27%20height=%27118%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQxIiBoZWlnaHQ9IjExOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3 搭建左侧翻译内容区​

参考以下操作，搭建翻译内容区域。​

1.

在组件面板中，将表单组件拖入到画布的容器组件Div3中，然后选中不需要的组件并按下 Backspace 键进行删除，只保留文本组件、选择组件和按钮组件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27537%27%20height=%27336%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM3IiBoZWlnaHQ9IjMzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选中表单组件，参考下表修改它的属性。​

  * ​

Form表单组件的属性设置​| 示例​  
---|---  
    * 将宽度和高度都设置为填充容器。​
    * 删除边框。​
| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271950%27%20height=%271189.2857142857144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk1MCIgaGVpZ2h0PSIxMTg5LjI4NTcxNDI4NTcxNDQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

3.

选中表单内的文本输入框，然后将其拉伸它的大小，再修改属性配置。​

  * 标签内容和占位文案都修改为：请输入翻译内容。​

  * 宽度设置百分比 100%。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27606%27%20height=%27306%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA2IiBoZWlnaHQ9IjMwNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

选中表单组件中的选择组件，然后修改它的属性配置。​

  * 标签内容修改为：目标语言。​

  * 选项设置：保留两个选项，分别为英语和日语。确保名称和选项值正确。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27613%27%20height=%27330%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEzIiBoZWlnaHQ9IjMzMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

选中表单组件中的按钮组件，将内容修改为开始翻译。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27521%27%20height=%27262%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIxIiBoZWlnaHQ9IjI2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

至此，我们就完成了左侧的翻译内容区域的页面功能搭建。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27303%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4 搭建右侧翻译结果区​

参考以下操作，搭建翻译结果区域。​

1.

在组件面板中，将 Markdown 组件拖入到画布的容器组件Div4中。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27635%27%20height=%27370%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjM1IiBoZWlnaHQ9IjM3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

选中新拖入的组件，配置以下属性。​

  * 内容：删除已有内容，输入 Markdown 格式内容：###### 翻译结果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27471%27%20height=%27177%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcxIiBoZWlnaHQ9IjE3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 高度和宽度：设置为填充容器。​

  * 圆角：设置为10。​

  * 内边距：设置为20。​

  * 外边距：设置为0。​

  * 边框：设置为灰色。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27266%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjI2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

至此，我们就完成了翻译应用的用户界面搭建，可单击属性面板上方的预览选项进行页面预览。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27682%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgyIiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5 添加事件​

搭建好页面后，就可以通过配置事件和添加数据实现业务逻辑与用户页面的联动了。​

本场景中，预期是希望用户点击开始翻译时，触发翻译工作流，并且将用户输入的译文和目标语言作为输入传入给工作流。所以，需要为开始翻译按钮组件添加一个点击事件。​

1.

在用户页面页签下，单击已添加的开始翻译按钮组件，然后在配置面板中选择事件，最后单击新建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27512%27%20height=%27314%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEyIiBoZWlnaHQ9IjMxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

事件类型选择点击时。​

3.

执行动作选择调用工作流，然后选择已经创建的工作流。选择工作流后，会自动展示所选工作流配置的输入参数。​

4.

将鼠标悬浮至content参数的文本框上，然后单击右侧的配置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27209%27%20height=%27333%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA5IiBoZWlnaHQ9IjMzMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在展开的配置面板中，找到用户输入翻译内容的组件 (Textarea)，选择表单值作为工作流中content参数的值。配置完成后关闭参数配置面板。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27689%27%20height=%27281%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg5IiBoZWlnaHQ9IjI4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

6.

重复上述操作，将目标语言组件的值作为工作流lang参数的值。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27697%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjk3IiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

a.

单击确认完成工作流的调用。​

7.

配置翻译结果数据。​

  * 最后需要将工作流返回的翻译内容展示在用户页面中。​

a.

在画布中，选中最后添加的Markdown组件。​

b.

在右侧的属性面板中，将鼠标悬浮至内容文本框内，然后单击出现的配置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27573%27%20height=%27360%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTczIiBoZWlnaHQ9IjM2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

在展开的面板中，首先在翻译结果下增加一行，然后选择工作流的返回数据作为翻译结果展示给用户。配置完成后，关闭配置面板。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27597%27%20height=%27276%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTk3IiBoZWlnaHQ9IjI3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

步骤五：效果测试​

完成上述所有配置后，单击预览，查看整体功能并进行体验。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27277%27%20height=%27196%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc3IiBoZWlnaHQ9IjE5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

你可以在打开的预览页面中，输入一段文字，然后选择一个翻译语言，单击开始翻译。查看是否在翻译结果区域有出现翻译后的内容。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27614%27%20height=%27285%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE0IiBoZWlnaHQ9IjI4NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤六：发布应用​

完成应用测试后，你就可以将应用发布到商店或模板，或发布成 API 服务与其他应用集成。​

本教程中以商店为例。​

1.

在应用 IDE 中，单击右上角的发布按钮。​

2.

在发布页面，输入版本号和发布描述。​

3.

选择扣子商店，然后选择应用分类。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27479%27%20height=%27349%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc5IiBoZWlnaHQ9IjM0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击页面上的发布按钮，完成应用发布。​

  * 发布完成后，你就可以在扣子商店上使用这个应用了。​

相关文档​

  * ​编排业务逻辑​

  * ​用户界面编辑器概述​

  * ​低代码工作流介绍​

  * ​了解项目发布​

​

上一篇

使用自然语言搭建智能体

下一篇

通过模板搭建智能体