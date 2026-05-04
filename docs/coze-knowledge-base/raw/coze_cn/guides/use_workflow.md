---
source_url: https://docs.coze.cn/guides/use_workflow
title: '使用低代码工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:16Z
---

# 使用低代码工作流 - 文档 - 扣子

使用低代码工作流

低代码工作流是一系列可执行指令的集合，用于实现业务逻辑或完成特定任务。你可以在低代码智能体和应用搭建中通过低代码工作流实现特定的任务或指令。​

搭建低代码工作流​

无论是在智能体还是应用中使用工作流，都需要先创建一个可运行的工作流。​

步骤一：创建低代码工作流​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在资源库页面右上角，选择 +资源 > 工作流。​

4.

设置工作流的名称与描述，并单击确认。​

  * 说明

清晰明确的工作流名称和描述，有助于大语言模型更好地理解工作流的功能。​

​

  * 创建后页面会自动跳转至工作流的编辑页面，初始状态下工作流包含开始节点和结束节点。​

  * 开始节点用于启动工作流。​

  * 结束节点用于返回工作流的运行结果。​

步骤二：编排低代码工作流​

创建工作流后，你在画布中添加节点，并按照任务执行顺序连接节点。​

工作流内置了多种基础节点供你使用，同时你还可以添加插件节点来执行特定任务。如果你在[插件商店](<https://www.coze.cn/store/plugin?cate_type=recommend&cate_value=recommend>)中收藏了某些插件，则添加节点面板中将自动展示你所收藏的插件，便于你直接调用。​

1.

在底部面板中选择要使用的节点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27258%27%20height=%27323%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b0e85ae375f541bf83698bb78e6e1e16~tplv-goo7wpa0wc-quality:q75.image)​

​

2.

将各个节点相连接。​

3.

配置节点的输入和输出参数。​

步骤三：测试并发布低代码工作流​

要想在智能体内使用该工作流，则需要发布工作流。​

1.

单击试运行。​

  * 如果输入参数包含图片、视频等文件类型，试运行时可以上传文件或输入文件 URL。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27421.09090909090907%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjQyMS4wOTA5MDkwOTA5MDkwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 运行成功的节点边框会显示绿色，在各节点的右上角可查看节点的输入和输出。​

2.

单击发布。​

  * 发布时你可以选择之前试运行阶段已保存的测试集作为默认测试集，发布后，该空间内的其他用户使用该工作流时，可以使用该测试集进行试运行和测试。​

在低代码智能体中添加低代码工作流​

添加低代码工作流​

1.

前往当前工作空间的智能体页面，选择进入指定智能体。​

2.

在智能体编排页面的工作流区域，单击右侧的加号图标。​

3.

在添加工作流对话框，在我创建的页面选择自建的工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27413%27%20height=%27180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDEzIiBoZWlnaHQ9IjE4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在智能体的人设与回复逻辑区域，引用工作流的名称来调用工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27418%27%20height=%27105%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE4IiBoZWlnaHQ9IjEwNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置低代码工作流异步运行​

注意

功能升级中，暂不支持新建的低代码智能体设置异步运行。​

​

工作流默认为同步运行，即智能体必须在工作流运行完毕后才会将工作流的输出传递给智能体用户。如果工作流复杂，或包含一些运行耗时长的节点，可能会导致工作流整体运行耗时超过 10 分钟，智能体判断为工作流运行超时，在其运行完毕前就结束对话。例如包含图像流节点、多个大模型节点，或编排逻辑复杂的工作流节点。​

在这种场景下，你可以设置工作流为异步运行，设置后，智能体对话不依赖工作流的运行结果，工作流超时时间延长至 24 小时。工作流异步运行时会默认返回一条预设的回复内容，用户可以继续与智能体对话，工作流运行完毕后智能体会针对触发工作流的指令做出最终回复。​

说明

  * 如果工作流或节点运行超时，智能体可能无法提供符合预期的回复。各场景的超时时间可参考​低代码工作流使用限制。​

  * 工作流异步运行，仅在调试智能体或与商店中的智能体对话时生效，飞书、豆包等渠道暂不支持工作流异步运行。 ​

  * 工作流开启异步运行后，模型节点无法查看对话历史。​

​

开启异步运行：​

1.

在指定工作流右侧单击设置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27398%27%20height=%2790%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk4IiBoZWlnaHQ9IjkwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

开启异步运行，并设置回复内容。​

  * 回复内容是工作流在异步运行时，智能体回复用户的默认文案。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27398%27%20height=%27129%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk4IiBoZWlnaHQ9IjEyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

异步运行效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27424%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI0IiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在低代码应用中添加低代码工作流​

扣子编程支持在项目中创建一个新的工作流或复制一个已有的工作流使用。​

在资源列表中，找到工作流，然后选择一种添加方式。​

  * 新建工作流：在该项目中创建一个新的工作流。​

  * 新创建的工作流只能在项目中使用，无法共享给其他项目使用。​

  * 引入资源库文件：复制一个项目所属的工作空间内已发布的工作流到该项目中使用。​

  * 复制后，你可以对这个工作流进行修改。在项目中对工作流的修改不影响资源库中的工作流。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27470%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDcwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

添加工作流后，你可以根据实际需求修改节点配置，或新增新的节点。​

查看引用资源​

工作流提供资源引用页面，帮助你快速查看应用中已添加的工作流、插件、数据库等资源，以便理解应用中各项资源的引用关系，从而更高效地管理资源、定位问题。​

在工作流编排页面右上角单击引用关系图标，页面将自动跳转到资源引用页面。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27607%27%20height=%27194%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjA3IiBoZWlnaHQ9IjE5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

资源引用页面展示工作流引用的子工作流、插件、数据库、知识库等资源，箭头从 A 指向 B 表示 A 引用了 B。例如在下图中，gen_zhuzhu_image 工作流直接引用了 test 知识库、头条搜索插件和 search 工作流。你还可以单击资源卡片，在新标签页中查看资源详情。​

说明

资源库中的工作流支持查看引用的资源版本，例如子工作流的版本、插件版本等。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271356%27%20height=%27441.01388888888886%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM1NiIgaGVpZ2h0PSI0NDEuMDEzODg4ODg4ODg4ODYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

复制低代码工作流​

  * 在某一工作流的编辑页面，单击右上角的创建副本图标，可以将该工作流复制到你的工作流列表中。​

  * 支持跨画布复制节点。​

  * 在画布中选择并复制已配置好的节点，然后切换到目标画布，直接粘贴即可。​

说明

跨空间复制工作流时，暂不支持同时复制节点绑定的火山知识库。​

​

  * 

删除低代码工作流​

对于不再需要使用的工作流，你可以在工作流列表内找到该工作流，并在操作列单击删除图标。​

注意

如果工作流已添加至智能体，在删除时会同步删除智能体中的工作流。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272326%27%20height=%27284.7463126843658%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjMyNiIgaGVpZ2h0PSIyODQuNzQ2MzEyNjg0MzY1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

低代码工作流使用限制

下一篇

导入与导出低代码工作流