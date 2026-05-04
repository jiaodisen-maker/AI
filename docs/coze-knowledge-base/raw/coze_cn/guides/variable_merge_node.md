---
source_url: https://docs.coze.cn/guides/variable_merge_node
title: '变量聚合节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:51Z
---

# 变量聚合节点 - 文档 - 扣子

变量聚合节点

低代码工作流的变量聚合节点能够将多路分支的输出变量整合为一个，方便下游节点统一配置。​

节点说明​

如果工作流中设计了多个分支，那么往往需要一个节点来汇总所有分支的输出结果，作为工作流的最终输出。如果有任意一个分支未运行，汇总输出的节点会从该分支读取到一个空值，从而导致工作流运行报错。在这种场景下，你可以使用变量聚合节点聚合多路分支的输出变量，变量聚合节点会读取多路分支中第一个不为空的值，供流程下游的节点使用和操作，不用额外处理未运行分支的输出结果，简化了数据流的管理。​

例如选择器或意图识别节点会将工作流拆分为多路分支，每次执行时，工作流会根据选择器条件或用户意图决定运行其中某一个分支，此时未执行的其他分支输出变量为空。你可以将多路分支都连接到变量聚合节点，并设置一个输出变量。无论哪条分支被执行，其结果都能通过这个变量被引用与访问，避免了下游节点对相同语义输出变量的重复定义。​

变量聚合节点支持分组聚合，每组变量会聚合为一个输出变量，分组组内的数据类型必须相同。​

配置变量聚合节点​

配置变量聚合节点时，需要选择聚合策略和聚合变量，并按需设置聚合分组。​

聚合策略​

通过指定策略对每个分组中的所有变量进行聚合处理，同一组内的变量实施相应聚合策略。​

目前聚合策略仅支持设置为“返回每个分组中第一个非空的值”，你可以拖动变量、调整变量位置。例如组内按顺序设置三个变量 output1、output2 和 output3，将其聚合为一个变量 Group1，如果 output1 不为空，则用 output1 的值为 Group1 赋值；如果 output1 为空，则取 output2 的值，依次类推。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27335%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6c5816e696f3472188b5d5f096e14af3~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27322%27%20height=%27419%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIyIiBoZWlnaHQ9IjQxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

聚合变量​

在 Group 1 中选择需要聚合的变量，分组内变量的数据类型必须相同。​

  * 变量聚合节点支持聚合多种数据类型，包括字符串（String）、数字（Integer、Number）、文件（File）对象（Object）以及数组（Array）等。​

  * 每个分组只能聚合一种数据类型的变量。例如将多个 String 类型的变量聚合为一个 String 变量、将多个 Integer 类型的变量聚合为一个 Integer 变量。​

聚合分组​

默认只有一个分组 Group1，对应一个输出变量 Group1。Group1 分组中所有变量类型和输出的变量类型相同。如果需要输出多个变量，可以添加多个分组。例如每个分支都有两个输出变量 String 和 Integer，可以设置两个分组，分别用于聚合 String 和 Integer。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271132%27%20height=%27594%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEzMiIgaGVpZ2h0PSI1OTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271554%27%20height=%27946.0694444444445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU1NCIgaGVpZ2h0PSI5NDYuMDY5NDQ0NDQ0NDQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

输出​

变量聚合节点的输出变量固定为 Group1，是分组 Group1 聚合的返回结果，具体的值取决于聚合策略。如果有多个分组则根据分组数量递增为 Group2、Group3 等变量。输出变量的数据类型取决于对应分组聚合的变量数据类型。​

示例​

在家教类 AI 应用中，通过 IF 选择器判断用户输入的问题属于哪个学科分类，并将对应的问题流转给对应的分支处理，例如数学问题流转给数学分支的大模型回答问题。三个分支均汇总到变量聚合节点，汇总为两个参数，即学科类型（type）、答案（answer），并传递到结束节点回答用户问题。​

整体流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271913%27%20height=%27508%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkxMyIgaGVpZ2h0PSI1MDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272012%27%20height=%27554.2314814814815%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAxMiIgaGVpZ2h0PSI1NTQuMjMxNDgxNDgxNDgxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

节点配置如下：​

​

节点类型​| 说明​| 示例​  
---|---|---  
开始节点​| 定义两个变量：​

  * BOT_USER_INPUT：用户输入的问题，也就是学生的问题。​

  * type：问题对应的学科。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27151%27%20height=%27147%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUxIiBoZWlnaHQ9IjE0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27154%27%20height=%27113%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU0IiBoZWlnaHQ9IjExMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
选择器节点​| 判断用户输入的 type 属于哪个学科，将问题流转到对应分支处理。这里我们定义语文和数学两个分支，其他学科统一流转到另外一个分支。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27135%27%20height=%27186%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM1IiBoZWlnaHQ9IjE4NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27137%27%20height=%27198%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTM3IiBoZWlnaHQ9IjE5OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
大模型节点​| 用于回答对应学科的问题，需要设置：​

  * 输入：定义 query 变量，引用开始节点收集的用户问题。​

  * 系统提示词：设置学科教师的人设，可以通过 AI 自动生成。​

  * 用户提示词：设置为 {{query}}，直接引用 query 变量即可。​

  * 输出：定义两个变量：​

  * answer：模型生成的答案。​

  * type：学科类型，例如语文节点固定值为“语文”。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27120%27%20height=%27235%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwIiBoZWlnaHQ9IjIzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27125%27%20height=%27239%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjIzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
变量聚合节点​| 聚合大模型节点的两个输出变量 answer 和 type。每个分组只能聚合一个变量，所以我们需要设置两个分组。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27158%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU4IiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27159%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTU5IiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
结束节点​| 选择返回文本模式，并设置输出变量和回答内容，透传大模型节点生成的答案即可。​

  * 输出变量：定义两个变量 answer 和 type，分别引用变量聚合节点的输出参数 Group1 和 Group2。​

  * 回答内容：透传大模型节点生成的答案即可。​

| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27188%27%20height=%27218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg4IiBoZWlnaHQ9IjIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27436%27%20height=%27541.3838862559242%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDM2IiBoZWlnaHQ9IjU0MS4zODM4ODYyNTU5MjQyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

上一篇

批处理节点

下一篇

异步任务节点