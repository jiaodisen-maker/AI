---
source_url: https://docs.coze.cn/guides/group_workflow
title: '封装与解散低代码工作流 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:36:01Z
---

# 封装与解散低代码工作流 - 文档 - 扣子

封装与解散低代码工作流

封装低代码工作流是指将复杂工作流中的部分节点及其关系整合为一个独立的子工作流，该子工作流作为原工作流中的一个节点呈现，从而简化工作流结构。封装低代码工作流适用于复杂工作流中存在多个并行分支，且分支中节点、节点关系以及变量高度重复的复杂工作流场景。它能有效减轻画布管理的复杂性，优化工作流编排效率，尤其适合需要频繁修改和优化工作流的场景。​

封装低代码工作流​

使用限制​

选择的工作流节点需要满足如下要求，否则无法完成封装：​

  * 框选范围内不能包含开始节点或结束节点。​

  * 框选范围内不能有未连接的节点。​

  * 框选范围内的节点中，不能存在未定义的变量。​

  * 框选范围内的中间节点不能连到框选范围外的节点，同时框选范围内的多个节点不能连到框选范围外的多个节点。​

  * 框选范围内不能包含继续循环节点或终止循环节点。​

  * 框选范围内包含循环体或批处理体时，关联的循环节点或批处理节点也要被框选。​

操作步骤​

1.

在工作流编排页面，选择需要封装的工作流节点，单击封装工作流或按 ctrl+G / command+G 快捷键。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27187.74566473988438%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8eb930fbcfb64c13a51f9b9487055959~tplv-goo7wpa0wc-quality:q75.image)​

​

  * 若封装工作流按钮为灰色，请根据界面提示检查选择的工作流节点是否满足要求，具体要求请参见​使用限制。​

2.

封装后，将生成一个新的子工作流，它将作为原工作流中的一个节点呈现，且工作流的整体连接方式与封装前保持一致。你可以在资源库中查看该子工作流。扣子编程会自动为子工作流添加开始和结束节点，其中，开始节点会自动接收所有需要的外部变量作为输入参数，而结束节点则会输出当前子工作流中所有被下游引用的变量。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27265.4335260115607%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjI2NS40MzM1MjYwMTE1NjA3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 说明

封装后的子工作流有两种类型：​

    * 子对话流：若框选范围内节点的输入参数同时包含了 USER_INPUT 和 CONVERSATION_NAME，封装后的类型为子对话流。且子对话流开始节点的输入参数默认包含 USER_INPUT 和 CONVERSATION_NAME，命名不变，会自动建立和父工作流的引用关系。​

    * 子工作流：若框选范围内所有节点的输入参数不包含 USER_INPUT 和 CONVERSATION_NAME，或只包含其中一种，封装后的类型为子工作流。​

​

示例​

多个输入节点​

当框选范围内有多个输入节点时，封装后的子工作流中，开始节点会和所有输入节点连线。​

封装前​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27306.3829787234043%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwNi4zODI5Nzg3MjM0MDQzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

封装后的子工作流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27152.24586288416074%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE1Mi4yNDU4NjI4ODQxNjA3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

多个输出节点​

当框选范围内有多个输出节点时，封装后的子工作流中，结束节点会和所有输出节点连线。​

封装前​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27306.3829787234043%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwNi4zODI5Nzg3MjM0MDQzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

封装后的子工作流​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27153.19148936170214%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE1My4xOTE0ODkzNjE3MDIxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

解散低代码工作流​

选中需要被解散的工作流，按 ctrl+shift+G / command+shift+G 快捷键，或单击更多图标，选择解散工作流 。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27165.1821862348178%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjE2NS4xODIxODYyMzQ4MTc4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

解散后，子工作流中的节点会重新添加到当前画布中，被解散的子工作流不会被删除，依然保留在智能体、应用内、资源库中。​

说明

解散循环或批处理中的子工作流时，子工作流中不能包含循环节点或批处理节点。​

​

​

​

上一篇

管理低代码工作流版本

下一篇

低代码工作流常见问题