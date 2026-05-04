---
source_url: https://docs.coze.cn/guides/knowledge_delete_node
title: '知识库删除节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:24Z
---

# 知识库删除节点 - 文档 - 扣子

知识库删除节点

低代码工作流中的知识库删除节点用于删除指定知识库中的文件。​

节点说明​

在低代码工作流中，你可以添加知识库删除节点，用于动态删除指定的知识库文件。知识库文件的动态删除操作，常用于知识库文件更新场景，例如当需要更新知识库内容时，可以先通过知识库删除节点删除旧文件，再通过知识库写入节点写入新文件，避免手动操作的繁琐。​

知识库删除节点需要指定待操作的知识库和文档 ID，每次执行此节点时将删除符合条件的文件。​

注意

  * 删除某个知识库文件后，引用了对应知识库的低代码智能体或工作流将无法召回该内容。​

  * 删除操作不可撤回，请谨慎操作。​

​

添加节点​

在工作流画布中，单击 \+ 添加节点，在知识库&数据区域选择知识库删除节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27496%27%20height=%27272%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/41b8296f6c9a4e9685f5bd71759ba05f~tplv-goo7wpa0wc-quality:q75.image)​

​

配置节点​

输入​

知识库删除节点的输入参数固定为 documentID，数据类型为 String，表示需要配置待删除的文档 ID。具体配置如下：​

  * 引用上游节点的输出参数：将知识库写入节点或知识库检索节点作为知识库删除节点的上游节点，在知识库删除节点的输入变量 documentID 中，引用知识库写入节点或知识库检索节点的输出参数 documentId。​

  * 如果上游节点的输出参数中存在多个 documentId，默认选择第一个 documentId。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27455%27%20height=%27167%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU1IiBoZWlnaHQ9IjE2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 输入固定值：如果是火山知识库，可以在[火山知识库控制台](<https://console.volcengine.com/vikingdb/knowledge/region:vdb-knowledge+cn-beijing/collection/list>)的目标知识库中，找到文档 ID，例如 _sys_auto_gen_doc_id-1362****84360926。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272824%27%20height=%27711.1532846715329%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgyNCIgaGVpZ2h0PSI3MTEuMTUzMjg0NjcxNTMyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 然后在知识库删除节点中，引用开始节点的输入参数 input，并输入固定的文档 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27395%27%20height=%27166%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk1IiBoZWlnaHQ9IjE2NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

知识库​

在知识库区域，选择待删除的知识库。​

  * 知识库来源：选择扣子知识库或火山知识库。​

  * 添加知识库：选择具体的知识库。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27394%27%20height=%27199%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk0IiBoZWlnaHQ9IjE5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

输出​

知识库删除节点中的输出参数是执行知识库删除操作后的输出内容，固定为 isSuccess，值为 true 或者 false，表示是否删除成功。​

示例​

例如在工作流中，通过知识库检索节点检索到标题为产品手册V1.0的旧文档，通过知识库删除节点将其删除，然后通过知识库写入节点将产品手册V2.0文档写入知识库，从而完成文档内容的更新操作，整个过程高效且减少繁琐的手动操作。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272036%27%20height=%271001.5046296296296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAzNiIgaGVpZ2h0PSIxMDAxLjUwNDYyOTYyOTYyOTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

上一篇

知识库检索节点

下一篇

长期记忆节点