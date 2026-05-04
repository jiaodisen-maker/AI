---
source_url: https://docs.coze.cn/guides/ai_chat_web
title: 'AI 对话 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:09Z
---

# AI 对话 - 文档 - 扣子

AI 对话

AI 对话组件用于搭建对话式的低代码应用，支持绑定对话流、设置开场白和快捷指令。​

属性设置​

AI 对话组件支持丰富的属性设置，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定对话流​

为 AI 对话组件绑定对话流，可以实现对话式的低代码应用开发。​

在低代码应用的业务逻辑页面中创建对话流后，你可以在用户界面中，选中 AI 对话组件，并在其属性的对话流参数中，绑定该对话流。详情请参考​使用对话流搭建低代码应用。​

创建对话流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271270%27%20height=%27355.1184834123223%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/181361979199433d9a7a542b8916ccd6~tplv-goo7wpa0wc-quality:q75.image)​

​

​

绑定对话流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27264%27%20height=%27146%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c44ae3b350b545eca823434f5ffa7737~tplv-goo7wpa0wc-quality:q75.image)​

​

​

在对话流中设置角色信息​

你可以在低代码应用的业务逻辑页面中，单击角色图标，设置角色信息。角色是智能体的人物形象，通过角色相关的配置可以提高智能体的拟人程度。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27827%27%20height=%27480%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f18f6908972a40ed91f4ee1cb2d5ae66~tplv-goo7wpa0wc-quality:q75.image)​

​

​

属性​| 说明​  
---|---  
角色名称​| 设置角色名称。​  
角色描述​| 设置角色的详细信息，帮助用户了解角色的背景和功能。​  
角色头像​| 设置角色头像，支持 AI 生成，也支持上传 .png 或 .jpg  格式的图标。上传的图标最大不超过 5MB。​  
开场白文案​| 设置 AI 对话组件的开场白，开场白是用户进入低代码应用后自动展示的引导信息，它的主要目的是帮助用户理解低代码应用的用途，以及如何与其进行交互。​  
开场白预置问题​| 配置 AI 对话组件的预置问题，用户与低代码应用的对话时，可以直接通过预置问题发起预设的对话。​  
用户问题建议​| 打开用户问题建议开关后，当智能体完成回复时，系统会根据当前的 Prompt，提供最多 3 条与之相关的提问建议。你可以根据这些建议，进一步优化提问的 Prompt，以便获得更精准、更有针对性的回答。​你也可以自定义用于生成提问建议的 Prompt。​  
背景图片​| 设置对话框的背景图片。​  
Agent 声音​| 设置 Agent 的语音音效。​如果打开文本转语音开关，系统将支持使用你所选择的音效播放智能体的回复内容。​  
用户输入方式​| 设置用户与 Agent 交互的输入方式，支持打字输入和语音输入。​  
  
​

为角色信息绑定动态数据​

你可以通过 AI 对话组件的动态角色信息参数，动态设置角色信息。例如设置角色昵称为 {{appInfo.name}}，即表示引用低代码应用的名称，当低代码应用名称发生变化时，角色昵称也会随之改变。​

说明

如果在对话流中设置了角色信息，又在动态角色信息参数中设置了角色信息，那么将以动态角色信息参数中的配置为准。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27319%27%20height=%27334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzE5IiBoZWlnaHQ9IjMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

设置用户信息​

你可以在扣子编程账号个人主页的设置页面中设置用户头像和名称，不支持在 AI 对话组件中设置用户信息。具体操作，请参考​设置个人资料。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27488%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg4IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上传文件​

在 AI 对话组件的属性中，打开文件上传按钮开关，AI 对话中将展示文件上传图标，用于在对话过程中上传文件，支持上传 Image、pdf、docx、excel、csv、audio 类型。例如在图像生成类应用中，可以上传图片文件，低代码应用根据原图片和指定的风格自动生成创意图片。​

属性配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27268%27%20height=%27284%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY4IiBoZWlnaHQ9IjI4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27365%27%20height=%2780%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzY1IiBoZWlnaHQ9IjgwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

清除对话​

在 AI 对话组件的属性中，打开对话清除按钮开关，AI 对话中将展示对话清除图标。单击该图标即可一键清除对话内容。​

属性配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27262%27%20height=%27299%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYyIiBoZWlnaHQ9IjI5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27363%27%20height=%2783%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYzIiBoZWlnaHQ9IjgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

隐藏组件​

AI 对话组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考​隐藏组件。​

事件设置​

通过配置 AI 对话组件的事件，可以为 AI 对话组件添加丰富的交互功能，​

​

事件项​| 说明​  
---|---  
事件类型​| AI 组件不支持配置事件类型。​  
组件方法​| 支持以下方法：​

  * 设置禁用：使组件变为禁用状态，用户无法与之交互。​

  * 设置隐藏：隐藏组件，使其不可见。​

  
  
​

​

上一篇

图片上传

下一篇

快捷键