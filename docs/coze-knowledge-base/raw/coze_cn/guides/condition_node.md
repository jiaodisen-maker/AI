---
source_url: https://docs.coze.cn/guides/condition_node
title: '选择器节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:41Z
---

# 选择器节点 - 文档 - 扣子

选择器节点

选择器节点是一个 if-else 节点，用于设计低代码工作流内的分支流程。​

条件分支​

当向该节点输入参数时，节点会判断是否符合如果区域的条件，符合则执行如果对应的工作流分支，否则执行否则对应的工作流分支。​

每个分支条件支持添加多个判断条件（且/或），同时支持添加多个条件分支，可通过拖拽分支条件配置面板来设定分支条件的优先级。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27711%27%20height=%27268%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/26801110f735455eb42598a147500add~tplv-goo7wpa0wc-quality:q75.image)​

​

优先级​

当存在多个条件分支时，将根据优先级排序逐个判断条件是否成立，若均不成立则只运行“否则”分支。​

例如以下示例中，如果开始节点的 input 既不等于 true，也不等于 false，则执行“否则”分支。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27791%27%20height=%27240%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/978132f2d8644c9b80c50fa8d5ad92fa~tplv-goo7wpa0wc-quality:q75.image)​

​

​

上一篇

代码节点

下一篇

意图识别节点