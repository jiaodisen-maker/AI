---
source_url: https://docs.coze.cn/guides/canvas_node
title: '画板节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:39Z
---

# 画板节点 - 文档 - 扣子

画板节点

低代码工作流中的画板节点是一个支持自定义绘制的图形创作节点。画板节点通常用于图文排版和设计场景，例如电商海报、营销 banner、社交媒体博文配图等。​

你可以在画板节点中插入各种元素，例如上传指定图片、添加文本、添加矩形等各种线性图形、画笔自由绘制等，还可以添加变量元素，引用上游节点的输出。除此之外，你还可以设置元素图层、画板尺寸、画板颜色、画板透明度等。​

在画板编辑区域双击预览图即可编辑画板，你也可以在画板编辑右上角单击图标来进入编辑状态。​

注意

  * 画板节点暂不支持展示 emoji 表情。​

  * 画板节点输出的图片为链接格式，有效期为 1 年，建议在到期前及时保存。​

  * 在扣子账号（主账号+子账号）维度下，画板节点的并发限制为 4。​

​

变量元素​

画板节点中添加的变量可以作为一个画板元素展示在画面中，这种画板元素被称为变量元素。​

如果需要引用上游节点的输出参数，作为画板节点的元素之一，可以在画板节点的配置页面元素设置区域单击加号（+）来增加一个元素，元素值引用上游节点的输出参数。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27358%27%20height=%27193%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/64f5f6a396e14a7d8dd01b42c871fb8c~tplv-goo7wpa0wc-quality:q75.image)​

​

添加变量元素后，此元素不会默认展示在画布中，你需要在画布手动添加这个元素。目前支持通过以下方式在画布中添加变量元素：​

​

添加方式​| 操作说明​| 示例​  
---|---|---  
直接插入变量元素​| 在画布中单击引用变量图标，添加一个变量元素。默认插入与变量类型相同的元素对象，即 String 类型对应文本对象，image类型对应图片对象。​​​| 例如根据指定输入文案生成小红书笔记配图。我们可以在开始节点中添加输出参数 title，并在画板节点中引用这个参数 title，title 参数的值会自动添加到画板节点中。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271159%27%20height=%27461.75298804780874%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE1OSIgaGVpZ2h0PSI0NjEuNzUyOTg4MDQ3ODA4NzQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
在固定元素中设置引用变量​| 如需为固定元素设置引用，选中文本对象或图片对象，并在配置框中选择要引用的变量即可。​固定元素中，仅文本对象和图片对象可以引用变量，且均可引用 image 和 String 类型的变量。​

  * 如果文本对象引用了 image 变量，最终生成的图片中，本文框内会展示变量对应图片的 URL。​

  * 如果 String 变量的值是一个公开可访问的图片 URL，那么图片对象可以引用这个 String 变量，最终生成的图片中，自动将 URL 渲染为图片。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271198%27%20height=%27666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE5OCIgaGVpZ2h0PSI2NjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

固定元素​

固定元素指添加到画板中的非变量元素，包括本地上传的图片、固定文本、画板中绘制的线性图形、画笔自由绘制等。对于固定元素的常见操作如下：​

​

操作​| 说明​| 示例​  
---|---|---  
添加图片​| 在画板中单击对应图标，上传一张本地图片到画板节点中。​添加图片后，可以设置填充样式和描边样式。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271896%27%20height=%27732.7171314741036%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5NiIgaGVpZ2h0PSI3MzIuNzE3MTMxNDc0MTAzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
添加文字​| 在画板中单击对应图标，添加一段文本内容到画板节点中。支持添加单行文本或区块文本，其中区块文本指固定大小的文本框。​添加文本框后，双击文本框可以设置文字内容，单击文本框可以调整文字的大小、位置等展示效果。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271202%27%20height=%27440.57370517928285%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMiIgaGVpZ2h0PSI0NDAuNTczNzA1MTc5MjgyODUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
添加图形​| 在画板中单击对应图标，添加一个线性图形到画板节点中。​添加图形后，可以设置填充样式和描边样式。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271011%27%20height=%27628.3505976095618%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAxMSIgaGVpZ2h0PSI2MjguMzUwNTk3NjA5NTYxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
画笔模式​| 在画板中单击对应图标，进入画笔模式。​在画笔模式下，你可以自由操控鼠标或触控板，在画板中自由绘制。​如需删除画笔轨迹，可以单击画笔图标退出画笔模式，再按下键盘上的 Delete 键。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271012%27%20height=%27665.2589641434263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAxMiIgaGVpZ2h0PSI2NjUuMjU4OTY0MTQzNDI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

元素样式​

添加变量元素和固定元素之后，可以随时调整元素的样式、展示效果、通过快捷键复制或删除元素。​

​

操作​| 说明​| 示例​  
---|---|---  
调整元素样式​| 选中变量元素，可以快速调整变量元素的位置、元素大小等。选中变量元素后，界面会浮现出用于编辑图形的工具栏，你还可以在浮现的工具栏中点击相应图标，调整变量元素的外观样式，例如调整字体大小、颜色、字体类型等。​此外，你还可以在画板中修改变量元素，直接预览显示效果，例如编辑文字预览效果、更换图片预览效果。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27868%27%20height=%27560.2231075697212%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODY4IiBoZWlnaHQ9IjU2MC4yMjMxMDc1Njk3MjEyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
调整元素位置​| 在画布中直接鼠标拖拽元素即可移动元素位置。移动时页面会显示坐标辅助线，帮助你判断元素之间的相对位置。​选中多个元素之后，还可以批量设置对齐方式。​| 

  * 移动：​

​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271194%27%20height=%27666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE5NCIgaGVpZ2h0PSI2NjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​

  * 对齐：​

​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27773%27%20height=%27631.3346613545817%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzczIiBoZWlnaHQ9IjYzMS4zMzQ2NjEzNTQ1ODE3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
快捷键操作​| 画布中支持通过以下快捷键复制操作：​

  * Command/Ctrl+C：拷贝​

  * Command/Ctrl+V：粘贴​

  * Command/Ctrl+D：拷贝并粘贴​

  * Alt+鼠标拖拽：自定义坐标快速复制​

  * Backspace/Delete：删除​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271198%27%20height=%27666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE5OCIgaGVpZ2h0PSI2NjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
删除元素​| 支持快捷键（Backspace/Delete）删除变量元素在内的所有元素。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271194%27%20height=%27666%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE5NCIgaGVpZ2h0PSI2NjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

画板设置​

画板节点的基础设置包括尺寸、颜色、透明度等画板设置、元素图层、预览比例等。​

​

操作​| 说明​| 示例​  
---|---|---  
调整画板设置​| 在画板中单击对应图标，调整画板设置。支持调整画板尺寸、颜色和透明度。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271116%27%20height=%27626.9163346613545%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTExNiIgaGVpZ2h0PSI2MjYuOTE2MzM0NjYxMzU0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
重置视图​| 调整预览比例后，单击重置视图图标，恢复到 100% 预览比例。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271094%27%20height=%27732.2390438247012%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA5NCIgaGVpZ2h0PSI3MzIuMjM5MDQzODI0NzAxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27922%27%20height=%27782.4143426294821%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTIyIiBoZWlnaHQ9Ijc4Mi40MTQzNDI2Mjk0ODIxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
调整预览比例​| 在画板中单击加号或减号，调整预览比例。预览的最小比例为 100%。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27760%27%20height=%27399.68127490039836%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzYwIiBoZWlnaHQ9IjM5OS42ODEyNzQ5MDAzOTgzNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
调整元素图层​| 选中元素后，在画板中单击对应图标，将指定元素置底或置顶。适用于元素重叠展示的场景下调整元素所在图层，例如在某个图形上叠加文字。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27816%27%20height=%27390.1195219123506%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODE2IiBoZWlnaHQ9IjM5MC4xMTk1MjE5MTIzNTA2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

输出​

画板节点的输出参数固定为：​

  * data：Image 格式的图像，即排版后的最终图像。通常是一个公开可访问的 URL 链接。​

  * msg：节点执行状态，success 表示处理成功。​

  * errorBody：节点执行失败时的详细信息，包括 errorMessage 和 errorCode。​

  * isSuccess：节点执行状态，true 表示执行成功，false 表示执行失败。​

其中isSuccess、errorBody 仅在节点的异常处理方式设置为返回设定内容或执行异常流程时返回，用于节点执行异常时传递详细信息。​

异常设置​

默认情况下，节点运行超时、运行异常时，工作流会中断，工作流调试界面或 API 中会返回错误信息。你也可以手动设置节点运行超时等异常情况下的处理方式，例如整体执行超时、是否重试、是否跳转异常分支等。​

​

异常处理设置​| 说明​  
---|---  
整体执行超时​| 整体执行超时是指节点运行的最大耗时，如果超过此时长，则判断为该节点运行超时。​默认情况下，节点的超时时间为 60s，即 1 分钟。你也可以将其改为 0.1s~60s，灵活控制超时时间。​  
重试次数​| 节点运行超时或异常时，默认不重试，你也可以设置为重试 1 次。​  
异常处理方式​| 节点运行超时或异常时，默认中断工作流。你也可以手动修改此节点的异常处理方式：​

  * 中断流程：工作流执行中断，不再运行后续节点。​

  * 返回设定内容：发生异常后，工作流运行不会中断。开发者可自定义设置需要返回的输出字段内容，必须是输出中已定义的字段，且格式为合法的 JSON 格式。另外，节点还会返回输出参数 isSuccess、errorBody，传递节点异常的详细信息。​

  * 执行异常流程：发生异常后，工作流运行不会中断，转而执行异常流程分析，开发者需要为新增的异常分支配置处理流程。异常信息会通过节点的输出参数 isSuccess、errorBody 返回。​

  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27384%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzg0IiBoZWlnaHQ9IjIwMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

示例​

例如通过画板节点搭建一个生成小红书配图的图像流。其中：​

  * 添加变量元素 mbti 和 title，引用开始节点的输入参数，作为画板中动态调整的 MBTI 部分、主题部分。​

  * 添加变量元素 image，引用开始节点的图片输入，作为画板中的配图。​

  * 最后为图片设置一个底色、调整尺寸即可。​

画板节点配置：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271877%27%20height=%27840.6469194312797%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg3NyIgaGVpZ2h0PSI4NDAuNjQ2OTE5NDMxMjc5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

生成效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27250%27%20height=%27269%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjI2OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

图像生成节点

下一篇

图像处理插件节点