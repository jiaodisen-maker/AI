---
source_url: https://docs.coze.cn/guides/using_database
title: '使用数据库 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:43:28Z
---

# 使用数据库 - 文档 - 扣子

使用数据库

扣子编程支持在 Prompt 通过 NL2SQL 方式对数据表进行操作，也支持在低代码工作流中添加数据库相关的节点，调用工作流来执行数据库操作。​

为了方便演示和介绍数据功能，本文以一个记录日常开支的智能体为例。这个智能体中使用的数据表结构如下。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27593%27%20height=%27386%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4abdf032a7cb4ef288173be6b81284f3~tplv-goo7wpa0wc-quality:q75.image)​

​

通过自然语言操作数据表​

用户可通过自然语言与智能体进行交互来插入或查询数据库中的数据。智能体会根据用户的输入自动创建一条新的记录并将其存储在数据库中。同样，用户也可以使用自然语言查询数据库中的数据，例如询问某一天的总开支、某一个类别的开支等，智能体会根据用户的查询条件从数据库中检索相应的数据并返回给用户。​

参考以下操作，在 Prompt 中添加并使用数据表：​

1.

在 Prompt 中明确说明要执行的操作和涉及的字段，包括字段的使用说明。这样，大语言模型可以更准确地根据用户输入来执行操作。​

2.

在数据库功能区域添加要操作的数据表。​

  * 默认开启提示词调用功能，表示数据表支持在提示词中访问。若关闭该功能，则数据表仅支持在工作流中访问。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27444%27%20height=%27175%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDQ0IiBoZWlnaHQ9IjE3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在调试区域，进行测试。​

  * 可单击调试区域右上方查看数据表中的数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27508%27%20height=%27219%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA4IiBoZWlnaHQ9IjIxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

通过低代码工作流 SQL 自定义节点操作数据表​

扣子编程支持在工作流中新增 ​SQL 自定义节点、​新增数据节点、​查询数据节点、​更新数据节点和​删除数据节点来操作数据库。此处以 SQL 自定义节点为例。​

下图是工作流中 SQL 自定义节点配置示例。当发布工作流后，在用户与智能体对话时，大语言模型会根据需要调用工作流，按照工作流中数据库节点中配置的 SQL 来执行数据表操作。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27712%27%20height=%27323%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzEyIiBoZWlnaHQ9IjMyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

参考以下说明，在工作流中添加并配置工作流节点。​

注意

低代码工作流中的数据与低代码智能体关联的数据表中的真实数据是隔离的。在工作流中进行 SQL 自定义节点测试时，不会使用智能体数据表中已有数据，因此你需要先插入测试数据再进行查、删、改等操作。​

​

​

参数​| 说明​  
---|---  
输入​| 添加 SQL 执行中需要的参数，可以是一个变量，也可以是一个固定值。​  
数据表​| 添加需要操作的数据表。一个 SQL 自定义节点最多可添加一个数据表。​  
SQL​| 输入要执行的 SQL 语句，支持使用输入参数中的变量，动态生成 SQL 语句，配置示例，请参考​示例。​可单击自动生成使用大模型生成 SQL。在弹出的页面中，选择这个数据库工作流生效的智能体和数据表，然后使用自然语言描述要执行的操作，单击自动生成生成 SQL 语句，最后单击使用Use。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27261%27%20height=%27252%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYxIiBoZWlnaHQ9IjI1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​注意

  * 不支持 Select* 语法。​

  * 不支持多表 Join 操作。​

  * 建议返回数据控制在 100 行以内，避免数据展示不全。​

​  
输出​| SQL 执行后的输出内容。​

  * outputList：输出 SQL 执行后数据表中的字段和数据。变量名需与SQL中定义的字段名一致。​

  * rowNum：输出返回的行数或者受影响的行。​

  
  
​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27653%27%20height=%27297%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjUzIiBoZWlnaHQ9IjI5NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

关联火山数据库

下一篇

管理数据库资源