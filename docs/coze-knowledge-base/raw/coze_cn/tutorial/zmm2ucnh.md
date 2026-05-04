---
source_url: https://docs.coze.cn/tutorial/zmm2ucnh
title: '小红书制图工厂 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:10Z
---

# 小红书制图工厂 - 文档 - 扣子

小红书制图工厂

作者：[拔刀刘AI学习](<https://www.coze.cn/user/1748637891168356>)​

作为小红书博主，在运营小红书账号时，发布一篇博文前，需要完成选题、收集素材、编写文案、搜索模板、制作配图等等的繁琐流程。通过小红书制图工厂智能体，确定主题后你就可以一键生成小红书文案及配图，图片自动排版，只需要保存图片发布即可。​

Agent 效果​

选定一个主题后，智能体会自动生成与主题相关的文案，并根据文案自动生成封面图和内容页。图片自动排版，提高运营效率。​

你也可以访问[小红书制图工厂智能体](<https://www.coze.cn/s/ihYTuNUK/>)，直接体验图片生成的效果。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27237%27%20height=%27317%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c49bf472a4e747d4a4ffcbea865966e7~tplv-goo7wpa0wc-quality:q75.image)​

​

应用场景​

小红书制图工厂智能体专用于生成符合小红书风格的图文，只需指定主题即可一键生成封面图和内容页。智能体主要使用工作流中的“画板”功能，对大模型生成的文案内容进行精细排版，例如调整字体、格式等。用户只需要输入一个关键词，就可以自动生成文案与图片，并自动排版，最终输出 1 张封面图、3 张内容页配图的效果，大大提升了小红书运营人员的工作效率。​

低代码智能体设计​

小红书制图工厂智能体的文生图功能依赖一个包含图像节点的工作流。在工作流中，大模型节点根据用户输入的关键词生成封面图和内容页需要的文案，两个工作流分别用于生成封面图和内容页的3张配图。​

整体流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271924%27%20height=%27536%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyNCIgaGVpZ2h0PSI1MzYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

Agent 编排如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273820%27%20height=%271796%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgyMCIgaGVpZ2h0PSIxNzk2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

工作流的编排如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%276656%27%20height=%274554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjY1NiIgaGVpZ2h0PSI0NTU0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

功能实现​

生成封面图​

通过图像节点生成一张封面图。​

封面图的整体逻辑如下：​

1.

根据主题生成一个相关的元素，并根据元素生成一个图标作为主体元素。例如小红书博文主题为“脚气”，主体元素可以设计为一个“泡脚桶”。​

2.

根据主体元素，联想两个辅助元素，再由文生图画出来。例如主体元素是“泡脚桶”，联想的两个辅助元素可以是“艾草”和“盐水”。​

3.

把生成的主体元素和两个辅助元素通过抠图功能抠出来，传给画板来进行排版。​

4.

画板根据传入的元素进行排版，输入参数主要有6项：主标题（分两行）、副标题（分两行）、主图元素、辅助元素​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%274648%27%20height=%272956%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY0OCIgaGVpZ2h0PSIyOTU2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

封面图图像节点设计如下：​

​

节点类型​| 说明​| 示例​  
---|---|---  
开始节点​| 开始节点中设置好所有需要用到的文本，其中：​

  * 主标题拆分成两行显示，即 title1 和 title2。​

  * 副标题也拆分成两行显示，即 sub_title1 和 sub_title2。​

  * 封面配图中需要文生图 3 个与主题相关的插图元素，需要 3 个提示词​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27660%27%20height=%27518%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYwIiBoZWlnaHQ9IjUxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
图像生成节点​| 3 个图像生成节点，分别生成 3 张插图，用于封面图片。​也可以暂不设置提示词，如果文生图效果不佳，再根据具体表现调整提示词。​​JSON复制正向提示词：​1个{{这里改为你的变量名称}}，简单插画，卡通风格，纯白色背景, 儿童简笔画​负向提示词：​其他元素​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27274%27%20height=%27422%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc0IiBoZWlnaHQ9IjQyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
抠图​| 通过抠图节点将插图中的主体元素提取出来。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27374%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc0IiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
画板​| 图文内容排版。此处可以根据实际需求和效果设计，通常需要一个标题行和多个内容行，文字内容引用开始节点的输入参数。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%273492%27%20height=%271482%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQ5MiIgaGVpZ2h0PSIxNDgyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
结束​| 输出节点用于输出最终排版完成的封面图​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27652%27%20height=%27478%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjUyIiBoZWlnaHQ9IjQ3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

效果：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27254%27%20height=%27339%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU0IiBoZWlnaHQ9IjMzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

生成内容页​

通过图像节点生成 3 张内容页配图。​

内容页是纯文字内容，不涉及文生图。内容页图像节点只需要接收输入内容，在统一模板的基础上将工作流中生成的文案进行排版并生成图片。图像节点运行一次即可生成 3 张配图。内容页图像节点编排如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272644%27%20height=%271486%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY0NCIgaGVpZ2h0PSIxNDg2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

节点配置如下：​

开始节点​

输入所有文案字段，包括 1 个主标题、3 个小标题、配套的 3 个介绍文案、小红书账号名称。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27332%27%20height=%27258%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMyIiBoZWlnaHQ9IjI1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

画板节点​

画板节点引用开始节点的输入。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27656%27%20height=%27281%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU2IiBoZWlnaHQ9IjI4MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 画布大小：小红书配图一般是 3:4 的比例，所以我们画布大小设置为 1080*1440。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27215%27%20height=%27144%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE1IiBoZWlnaHQ9IjE0NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 画板设计：根据样例生成排版的模板即可。常用格式包括添加图片、添加文字和图层设置等。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27624%27%20height=%27212%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI0IiBoZWlnaHQ9IjIxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 内容页编排：​

  * 其中边框、矩形文本框均为预先准备的设计素材，由第三方工具制作完成后，上传到画板节点中进行排版。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27276%27%20height=%27364%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc2IiBoZWlnaHQ9IjM2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 1、底图：绿色​

  * 2、底图：白色​

  * 3、标题底图：绿色​

  * 4、标题：单行文本​

  * 5、小标题：单行文本​

  * 6、详细介绍：区块文字​

  * 7、小红书账号名称：单行文本​

结束节点​

结束节点直接输出图片即可。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27302%27%20height=%27226%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAyIiBoZWlnaHQ9IjIyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

编排文生图流程​

图像节点已经准备好了，我们下一步就是制作工作流，通过大模型节点生成图像节点需要的文案，并提供给两个图像节点进行排版。根据用户输入的关键词，通过大模型生成封面图和内容页需要的文案，通过调用图像节点，直接生成 4 张小红书图片，即 1 封面图+3内容页图。​

工作流编排如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%276656%27%20height=%274554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjY1NiIgaGVpZ2h0PSI0NTU0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

大模型节点：生成文案​

添加大模型节点，输入参数为用户输入的关键词，大模型一次生成所有文案，包括 1个主标题，1个副标题，9个小标题，9个详细介绍，3个插图提示词。​

大模型节点的相关配置如下。​

​

配置​| 说明​| 示例​  
---|---|---  
模型设置​| 可以适当调高模型随机度。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272390%27%20height=%27806%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM5MCIgaGVpZ2h0PSI4MDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​  
人设与回复逻辑​| 点击图中标红位置，输入提示词。这里输入的提示词为系统提示词，人设类的内容写在这里，模型生成的内容效果更好。​人设与回复逻辑的示例可参考​相关资源部分。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271250%27%20height=%27760%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1MCIgaGVpZ2h0PSI3NjAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

代码节点：格式化数据​

由于大模型输出的内容，不能保证100%是结构化的数据，所以这里我们使用代码节点处理一下，方便后边流程调用。代码节点的示例可参考​相关资源部分。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27214%27%20height=%27750%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE0IiBoZWlnaHQ9Ijc1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

代码节点：处理主副标题分行​

用代码节点，将主标题和副标题进行分行，后边调用封面图的图像节点中使用。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27203%27%20height=%27357%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAzIiBoZWlnaHQ9IjM1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

代码示例如下：​

​

Python

复制

async def main(args: Args) -> Output:​

params = args.params​

title = params.get('title', '')​

subtitle = params.get('subtitle', '')​

​

# 处理 title​

if len(title) > 7:​

title1 = title[:7]​

title2 = title[7:]​

else:​

title1 = title​

title2 = ''​

​

# 处理 subtitle​

if len(subtitle) > 20:​

subtitle1 = subtitle[:20]​

subtitle2 = subtitle[20:]​

else:​

subtitle1 = subtitle​

subtitle2 = ''​

​

ret: Output = {​

'title1': title1,​

'title2': title2,​

'subtitle1': subtitle1,​

'subtitle2': subtitle2,​

}​

​

return ret​

​

生成图片​

将准备好的图像节点添加至工作流中，调用图像节点生成封面图和内容页配图。此处应关注连线的逻辑关系，将上一步生成的主副标题内容输入给封面图图像节点，将格式化好的数据输入给内容页图像节点，由于我们需要生成3张内容页，所以调用了3次内容页图像节点，注意3次调用配置的输入参数不同。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27491%27%20height=%27823%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkxIiBoZWlnaHQ9IjgyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

代码节点：汇总输出​

通过代码节点汇总4个图像节点输出，将 4 个图像节点中的图片汇总，为之后卡片调用做准备。结束节点一定要包括这个节点生成的pages参数，否则卡片无法调用。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27547%27%20height=%27373%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQ3IiBoZWlnaHQ9IjM3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

示例代码如下：​

​

Python

复制

async def main(args: Args) -> Output:​

params = args.params​

cover_page = params.get("cover_page", "")​

content_page1 = params.get("content_page1", "")​

content_page2 = params.get("content_page2", "")​

content_page3 = params.get("content_page3", "")​

​

# 创建 pages 对象​

pages = [​

{"image": cover_page},​

{"image": content_page1},​

{"image": content_page2},​

{"image": content_page3}​

]​

​

ret: Output = {​

"pages": pages​

}​

​

return ret​

​

完成以上节点配置后，试运行并预发布工作流即可。​

卡片：工作流绑定卡片​

工作流的展示效果依赖卡片格式的输出。你需要创建一个卡片，排版后绑定到工作流。​

组件​

创建一个卡片，并依次添加并设置「标题」「横滑布局」及「文本」组件。点击相应的组件，在右侧还可以调整这个组件的基础属性，比如这里我们不确定要输出几张照片，那我们就选择动态格数。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272382%27%20height=%271060%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM4MiIgaGVpZ2h0PSIxMDYwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

组件配置如下：​

​

组件类型​| 说明​| 示例​  
---|---|---  
标题​| 点击第1行「标题」组件，并且在右侧编辑标题的内容。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272260%27%20height=%27750%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI2MCIgaGVpZ2h0PSI3NTAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
文本​| 编辑下方「文本」的内容，这里我们希望展示文本内容。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272274%27%20height=%271090%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI3NCIgaGVpZ2h0PSIxMDkwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
横滑布局​| 由于我们使用了「布局组件」，需要先把「基础组件」中「图片」拖入到布局中。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272160%27%20height=%27940%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjE2MCIgaGVpZ2h0PSI5NDAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
  
​

变量​

由于这里图片不是固定的内容，所以我们就需要用到变量，来将工作流中的输出结果绑定到这个卡片中。​

1.

在卡片的变量页签中单击新建变量，并选择「变量类型」。​

  * 由于我们这里选择的是「动态格数」，需要绑定的变量类型应该为数组（list）的形式，所以我们选择array，变量名称设置为「图片列表」，默认值设置为array的基本形式，链接就是个示例，可以任意填写。​

  * 示例：​

  * ​

JSON

复制

[​

{​

"image" : "https://www.baidu.com"​

},​

​

{​

"image" : "https://www.baidu.com"​

}​

]​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27333%27%20height=%27235%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMzIiBoZWlnaHQ9IjIzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

点击页面中间的「横滑布局」，在右侧编辑区先绑定数组。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272262%27%20height=%27746%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI2MiIgaGVpZ2h0PSI3NDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

3.

点击「图片」，在右侧编辑区再绑定相应的变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272244%27%20height=%271202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI0NCIgaGVpZ2h0PSIxMjAyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 成功绑定后，显示效果如下：​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27196%27%20height=%27197%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTk2IiBoZWlnaHQ9IjE5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

简单设置一下下边的内容，右上角点击发布即可。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27204%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA0IiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

为工作流绑定卡片。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271836%27%20height=%27310%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgzNiIgaGVpZ2h0PSIzMTAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

相关资源​

模板​

小红书制图工厂在 Agent 商店的 Agent 地址：[小红书制图工厂智能体](<https://www.coze.cn/s/ihYTuNUK/>)​

人设与回复逻辑​

工作流中，用于生成文案的大模型节点人设与回复逻辑如下：​

  * 生成小红书文案：​

  * ​

Markdown

复制

## 角色​

你是一位资深的养生达人，熟悉各种养生知识，擅长通过用户输入的关键词，提供养生建议​

​

## 任务​

根据用户输入的关键词，按照<生成规则>和<输出规则>的要求，为用户提供养生建议，一定要注意<限制要求>中的内容​

​

## 生成规则​

1. 充分理解用户输入关键词的意图​

2. 生成一条养生建议的标题，字数严格要求9-11个字，**标题内容要反认知**，这个非常重要​

3. 围绕这个标题，生成一个副标题，用来解释标题内容，字数严格要求15-20个字​

4. 围绕这个标题，生成9个小标题，以序号开头，如：“1、xxx”，每个小标题字数不超过10个字​

5. 为每一个小标题生成一段介绍内容，字数严格要求90-160个字，**一定要满足字数要求**，这个很重要。​

6. 围绕标题内容，生成一个联想到的名词，比如标题是“假期就多去KTV唱歌”，联想到的名词就是“麦克风”​

7. 围绕这个生成的名词，再生成两个关联的名词，比如生成名词是“麦克风”，关联的名词就是“音符”“音箱”​

​

## 输出规则​

以json格式输出，仅输出如下内容，不要做任何解释。输出格式：​

[{​

"title": "生成的主标题",​

"subtitle": "（生成的副标题）",​

"main_image": "联想到的名词",​

"element_img1": "关联的名词1",​

"element_img2": "关联的名词2",​

"sub_title1": "小标题1",​

"content1": "介绍1",​

"sub_title2": "小标题2",​

"content2": "介绍2",​

"sub_title3": "小标题3",​

"content3": "介绍3",​

"sub_title4": "小标题4",​

"content4": "介绍4"​

"sub_title5": "小标题5",​

"content5": "介绍5"​

"sub_title6": "小标题6",​

"content6": "介绍6"​

"sub_title7": "小标题7",​

"content7": "介绍7"​

"sub_title8": "小标题8",​

"content8": "介绍8"​

"sub_title9": "小标题9",​

"content9": "介绍9"​

}]​

​

## 限制要求​

- 严格按照<输出规则>中的格式输出，不要再输出其他任何内容，也不要使用代码块的方式输出，**不要使用```这类的符号**，这个非常重要！​

​

输出示例：[{​

"title": "建议：假期就多去KTV唱歌",​

"subtitle": "（爱唱歌的人生活得更久，而且还能帮你减肥~​

内附80首KTV必点歌单，假期一起勇闯KTV）",​

"main_image": "麦克风",​

"element_img1": "音符",​

"element_img2": "音箱",​

"sub_title1": "1、爱唱歌的人更长寿",​

"content1": "美国老年学研究中心通过调查发现，歌剧歌唱家的心脏功能和普通人相比更加强活跃。唱歌能使人长寿。研究证实，唱歌是呼吸肌在特定条件下的一种运动，好处不亚于跑步、游泳、划船等，所以说，经常唱歌，能让你活得更久哦～",​

"sub_title2": "2、有节奏的体内按摩",​

"content2": "唱歌时伴随人体横膈膜，这种内部的循环按摩，是任何一项运动都无法替代的。随着歌曲节奏慢慢的变化，唱歌的呼吸时长时短、时快时慢，呼吸系统不断加压、减压的快速变化使得呼吸系统的肌肉得到锻炼，帮助按摩内脏，激活肺腑潜能，促进脏腑健康。",​

"sub_title3": "3、唱歌能帮助减肥",​

"content3": "唱歌是一项全身运动，可以锻炼全身肌肉，间接帮助你达到减肥的效果。调研显示，60公斤体重的人唱歌时热量消耗率2.0千卡/分钟，唱2小时消耗240千卡左右，唱一首歌相当于跑100米，对于想要减肥又喜欢运动的人来说，不妨试试多唱歌～",​

"sub_title4": "4、提升心理健康",​

"content4": "唱歌能够释放内心的压力和焦虑，研究表明，唱歌可以促进体内内啡肽的分泌，带来愉悦感，帮助改善情绪，提升心理健康。",​

"sub_title5": "5、增强社交能力",​

"content5": "在KTV等场合唱歌可以促进人与人之间的互动，增强社交能力。共同唱歌、分享歌曲能够拉近彼此的距离，增进友谊。",​

"sub_title6": "6、提高记忆力",​

"content6": "唱歌需要记忆歌词和旋律，这对大脑是一种锻炼。研究发现，常唱歌的人在记忆和学习新事物方面表现更佳，能够有效提高记忆力。",​

"sub_title7": "7、改善呼吸系统",​

"content7": "唱歌能够增强肺活量，改善呼吸系统功能。通过唱歌时的深呼吸，有助于增加氧气摄入，促进身体健康。",​

"sub_title8": "8、提升自信心",​

"content8": "在众人面前唱歌能够锻炼个人的表现能力，逐渐提升自信心。无论是独唱还是合唱，都会让你在舞台上更加自信。",​

"sub_title9": "9、丰富文化知识",​

"content9": "通过唱歌可以接触到不同的音乐风格和文化背景，丰富个人的文化知识，增加对音乐的理解和欣赏能力。"​

}]​

​

格式化代码示例​

工作流中，用于格式化数据的代码示例如下。你可以在代码节点中单击在IDE中编辑，选择 Python 语言，并输入代码。​

​

Python

复制

import re​

import json​

​

async def main(args: Args) -> Output:​

params = args.params​

​

# 使用正则表达式提取键值对​

pattern = r'"(title|subtitle|sub_title\d|content\d|main_image|element_img\d+)":\s*"([^"]*)"'​

matches = re.findall(pattern, params['input'])​

​

# 构建输出字典​

extracted_values = {}​

for key, value in matches:​

extracted_values[key] = value​

​

# 包装成输出格式​

ret: Output = {​

"extracted_values": [extracted_values]​

}​

return ret​

​

上一篇

抖音电商同款智能客服

下一篇

Seedream 模型生图教程