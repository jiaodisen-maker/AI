---
source_url: https://docs.coze.cn/guides/collaborate_agent
title: '协同管理低代码智能体 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:45:58Z
---

# 协同管理低代码智能体 - 文档 - 扣子

协同管理低代码智能体

如果需要多人协同管理低代码低代码智能体，可以为智能体开启协作模式，并将工作空间中的其他成员添加为此智能体的协作者。每个协作者都将拥有独立的智能体草稿，可以提交自己的草稿版本到工作空间，也可以拉取其他协作者的版本到自己的草稿中，最终合并内容后正式发布智能体。​

权限说明​

智能体的协作者无法开启或关闭协作模式、无法删除智能体，仅智能体的所有者才拥有此权限。另外，智能体协作者可以移除本人和所有者以外的协作者。所有者可以移除智能体的所有协作者。除此之外，所有者和协作者关于这个智能体的权限完全相同。​

低代码智能体的协作者和所有者权限详细差异对比如下：​

​

模块​| 操作权限​| 智能体所有者、创建者​| 智能体协作者​  
---|---|---|---  
管理智能体​| 添加协作者​| ✅​| ✅​  
​| 移除协作者​| ✅​​| ✅​智能体协作者可以移除本人和所有者以外的协作者。​  
​| 开启、关闭协作模式​| ✅​| ❌​  
​| 删除智能体​| ✅​| ❌​  
​| 复制智能体​| ✅​| ✅​  
编辑智能体​| 编辑智能体​| ✅​| ✅​  
​| 提交草稿到工作空间​| ✅​| ✅​  
​| 拉取、合并版本​| ✅​| ✅​  
发布智能体​| 发布智能体到豆包和商店​| ✅​| ❌​  
​| 发布智能体到其他渠道​| ✅​| ✅​  
​| 查看提交历史​| ✅​| ✅​  
​| 查看发布历史​| ✅​| ✅​  
​| 还原版本​| ✅​| ✅​  
  
​

开启多人协作​

低代码智能体的创建者可以在智能体编排页面的右上角为这个智能体开启协作模式。开启后需要为智能体添加协作者，协作者可以编排并发布此智能体。​

说明

  * 智能体的协作者必须是工作空间中的成员，暂不支持添加工作空间外的用户作为协作者。​

  * 多 Agent 模式的智能体不支持开启多人协作。​

  * AI 生成的智能体不支持开启多人协作。​

  * 当智能体开启前缀缓存后，将无法开启多人协作，具体请参见​上下文缓存。​

​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部空间列表中选择目标工作空间。​

3.

在左侧导航栏选择项目管理，选择目标低代码智能体或创建一个低代码智能体。​

4.

在页面右上角，单击协作图标，并打开协作开关。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27520%27%20height=%27223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIwIiBoZWlnaHQ9IjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

添加协作者​

低代码智能体的所有者和协作者都可以添加工作空间中的其他成员作为智能体的协作者，但协作者无法从协作名单中移除所有者。​

1.

在页面顶部空间列表中选择目标工作空间。​

2.

在左侧导航栏选择项目管理，选择目标低代码智能体。​

3.

在页面右上角，单击协作图标。​

4.

在协作者区域搜索工作空间内的成员，并单击添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27396%27%20height=%27168%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk2IiBoZWlnaHQ9IjE2OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

协作者添加完成后，你可以在协作图标处查看智能体的协作者数量，单击协作者图标并展开协作者列表，可以查看当前智能体的协作者名单，也可以根据页面提示移除某个协作者。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27421%27%20height=%27178%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIxIiBoZWlnaHQ9IjE3OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

协同编排低代码智能体​

智能体开启多人协作并添加协作者后，智能体的每个协作者都将拥有自己的个人草稿，可以在草稿中进行任何变更，每个协作者的草稿互相不可见。如果某个协作者已完成编排，需要先将自己的草稿提交到工作空间，才能完成发布。​

协作者提交草稿到工作空间后，其他协作者可以拉取此变更，如果此变更和自己的草稿内容不一致，还可以选择合并。​

步骤一：编排低代码智能体​

智能体的协作者完成编排智能体后，需要将自己的草稿版本提交到工作空间中，此智能体版本可以被工作空间中的其他成员查看，无论此成员是否为智能体的协作者。​

1.

在页面顶部空间列表中选择目标工作空间。​

2.

在左侧导航栏选择项目管理，选择目标低代码智能体。​

3.

完成智能体的编排后，在页面右上角单击提交。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27401%27%20height=%27168%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAxIiBoZWlnaHQ9IjE2OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：合并多人的变更​

多人编排同一智能体时，各自的草稿版本往往并不相同，如果某个协作者将自己的草稿提交到工作空间，其他协作者在智能体的编排页面会收到提醒{用户名}已经提交了一个新版本，你可以拉取新版本并合并到你的草稿中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27440%27%20height=%27184%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQwIiBoZWlnaHQ9IjE4NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

协作者在提交自己的草稿前，必须先单击拉取，查看最新版本与你的草稿版本的差异，并就差异的部分选择要保留的结果。​

  * 使用最新提交的版本：选择最新版本，表示放弃自己的草稿，用工作空间中的最新版本覆盖草稿。​

  * 使用自己的草稿版本：选择我的草稿，表示坚持使用自己的草稿版本，准备将自己的草稿版本提交到工作空间中，覆盖最新版本。​

  * 手工合并自己草稿和工作空间中最新提交的版本：选择手工合并，系统自动将你的草稿自动填入合并结果中，可继续编排后单击提交。​

选择保留结果后，就可以单击合入到草稿。​

步骤三：查看差异​

提交草稿到工作空间时，可以单击查看差异，查看当前草稿版本和工作空间中的智能体版本差异，确认每一项差异均为预期中的变更后，再单击提交。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27460%27%20height=%27195%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYwIiBoZWlnaHQ9IjE5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：提交到工作空间​

智能体的协作者完成智能体编排后，需要将自己的草稿版本提交到工作空间中，此智能体版本可以被工作空间中的其他成员查看。​

1.

在页面顶部空间列表中选择目标工作空间。​

2.

在左侧导航栏选择项目管理，选择目标智能体。​

3.

完成智能体的编排后，在页面右上角单击提交。​

发布智能体​

智能体的每个协作者均具有发布权限。成功将智能体提交到工作空间后，就可以发布智能体。发布智能体时也需要确认当前发布版本和线上最新版本的差异，建议确认每一项差异均为预期中的变更，再发布智能体。​

说明

协作者必须先将自己的草稿版本提交到工作空间中，才能发布智能体。​

​

1.

在页面顶部空间列表中选择目标工作空间。​

2.

在左侧导航栏选择项目管理，选择目标智能体。​

3.

在页面右上角单击发布。​

4.

在发布页面，你可以单击发布平台右侧的查看差异图标，查看智能体与目标发布平台的差异。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27445%27%20height=%27180%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ1IiBoZWlnaHQ9IjE4MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

单击发布。​

提交发布后，系统会审核智能体，审核需要一定的时间，请耐心等待，审核结果可以在智能体编排页面右上角的发布历史处查看。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27438%27%20height=%27187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM4IiBoZWlnaHQ9IjE4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

管理历史版本​

每一个协作者提交到工作空间中的草稿版本和正式发布的版本都会记录在智能体的历史版本中，协作者可以查看每个版本，也可以还原指定的版本到自己的草稿中再次编排。​

协作者在智能体编排页面中单击查看历史图标，可以管理智能体的所有历史版本。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27442%27%20height=%27188%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQyIiBoZWlnaHQ9IjE4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

支持的操作如下：​

​

操作​| 说明​| 示例​  
---|---|---  
查看提交历史​| 在提交页签中可以查看每个协作者的提交记录，包括提交版本的协作者名称、提交时间等信息，提交记录按提交时间倒序展示。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2763%27%20height=%27146%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMiIGhlaWdodD0iMTQ2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
查看发布历史​| 在发布页签中可以查看每个协作者的发布记录，包括发布版本的协作者名称、发布时间等信息，发布记录按发布时间倒序展示。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2764%27%20height=%27117%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iMTE3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
调试预览历史版本​| 在提交页签或发布页签中找到指定的历史版本，单击调试预览即可预览此版本的智能体并进行调试。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2771%27%20height=%2789%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzEiIGhlaWdodD0iODkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
还原历史版本到草稿​| 在提交页签或发布页签中找到指定的历史版本，并选择还原为此版本，此智能体版本将会覆盖当前你的草稿版本。​如果你希望将线上版本回退到某个历史版本，需要先还原这个历史版本到草稿，再提交到工作空间并发布。这个新的版本也会作为一条新的提交历史和发布历史记录在版本历史中。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2781%27%20height=%27202%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODEiIGhlaWdodD0iMjAyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

关闭多人协作​

如果智能体的所有者不希望其他用户协同编排智能体，需要先移除所有协作者，并关闭协作模式。关闭协作模式之后，仅智能体的所有者可以编排智能体、发布智能体、管理历史版本。​

说明

  * 仅智能体的所有者可以关闭协作模式，且关闭协作之前需要先移除所有协作者。​

  * 关闭协作模式之后，创建者的草稿版本仍会保留，所有协作者的草稿版本将会被清除且无法恢复，建议谨慎操作。​

​

1.

智能体的创建者在项目管理页面，选择目标智能体。​

2.

在页面右上角单击多人协作图标，并在右侧展开协作者列表，移除所有协作者。​

3.

回到协作页面，关闭协作开关。​

4.

在页面弹出对话框中单击关闭。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27434%27%20height=%27186%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM0IiBoZWlnaHQ9IjE4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

多人协作概述

下一篇

协同管理低代码工作流