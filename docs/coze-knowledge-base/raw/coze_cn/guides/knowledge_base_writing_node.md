---
source_url: https://docs.coze.cn/guides/knowledge_base_writing_node
title: '知识库写入节点 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:34:19Z
---

# 知识库写入节点 - 文档 - 扣子

知识库写入节点

低代码工作流中的知识库写入节点用于向指定的扣子知识库或火山知识库中添加内容。​

使用限制​

使用火山知识库时，节点的请求频率限制遵循火山知识库自身的 QPS 配额限制。更多信息，请参考[接口限流说明](<https://www.volcengine.com/docs/84313/1339026#接口限流说明-2>)。​

  * 写入文本到火山知识库文档时，将调用 [/api/knowledge/point/add](<https://www.volcengine.com/docs/84313/1386607>) 接口，该接口的 QPS 为 10。​

  * 上传新文档到火山知识库时，将调用 [/api/knowledge/doc/add](<https://www.volcengine.com/docs/84313/1254624>) 接口，该接口的 QPS 为 300。​

  * 检索火山知识库中的文档时，将调用 [/api/knowledge/service/chat](<https://www.volcengine.com/docs/84313/1544072>) 接口，该接口与部分火山知识库接口共享 QPS，其值为 50。​

节点说明​

在低代码工作流执行过程中，用户不仅可以从已上传的知识库里检索信息，还可以通过知识库写入节点来主动更新知识库，上传新的文档内容。知识库写入节点是智能体或应用的用户上传知识库的唯一途径，它的本质是向一个已创建的知识库中上传文件或内容，内容的切片策略沿用知识库的分段策略。​

说明

  * 每次运行知识库写入节点只能上传一个文件到知识库，但是你可以通过批处理或循环节点多次执行写入操作。​

  * 知识库写入节点为异步节点，工作流执行时无需等待文档上传完成。​

​

添加节点​

在工作流画布中，单击 \+ 添加节点，在知识库&数据区域选择知识库写入节点，即可将节点添加到画布中。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27538%27%20height=%27297%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/280445517aba42b79cc8ad1097ce173f~tplv-goo7wpa0wc-quality:q75.image)​

​

配置火山知识库​

选择知识库来源为火山知识库时，参考如下配置。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27306%27%20height=%27303%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA2IiBoZWlnaHQ9IjMwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27323%27%20height=%27309%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIzIiBoZWlnaHQ9IjMwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

写入方式​

当选择知识库来源为火山知识库时，支持设置写入方式，具体包括以下两种方式：​

  * 写入知识库：将文件写入到指定的知识库中。​

  * 写入文档：将文本内容上传到知识库的指定文档中。​

输入​

知识库写入节点的输入参数固定为 knowledge，表示用户需要上传到知识库中的文件或内容。​

  * 如果要上传文本内容到知识库文档中，可设置 knowledge 的数据类型为 String 或 Array<object> 。上传的内容需引用上游节点的输出参数，在上游节点获取内容后写入。​

  * 如果知识库是结构化类型，需上传结构一致的文本内容，建议设置数据类型为 Array<object>。​

  * 如果知识库是非结构化类型，可设置数据类型为 String。​

  * 如果要上传新文件到知识库，可设置 knowledge 的数据类型为 File<Doc>。上传的文件可以固定为某个文件，由知识库的搭建者在搭建时上传；也可以引用上游节点的输出参数，在上游节点获取文件后上传。​

  * 如果知识库是结构化类型，支持上传 csv，xlsx，jsonl，faq.xlsx 格式的文件。​

  * 如果知识库是非结构化类型，支持上传 pdf， ppt，txt，markdown，doc，xlsx，csv，jsonl，faq 格式的文件。​

知识库​

在知识库区域，选择待写入内容的知识库。​

  * 知识库来源：选择火山知识库。​

  * 添加知识库：选择具体的知识库。​

  * 目标写入文档：设置写入方式为写入文档时，需选择具体的知识库文档。​

标签​

说明

仅火山知识库旗舰版支持标签功能。更多信息，请参考[创建知识库](<https://www.volcengine.com/docs/84313/1254457>)。​

​

火山知识库的标签功能用于对知识库文档进行分类与过滤，提升知识库的检索效率。添加标签后，后续在知识库检索时，将先在标签范围内检索文档，然后结合召回策略返回结果。​

标签区域将展示你在创建火山知识库时所创建的标签。标签值中将罗列你在创建标签时设置的标签值，你也可以在搜索框中输入标签值，单击创建，创建新的标签值。设置完成后，系统会在上传文档时，同步为文档添加标签。​

选择标签值​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27281%27%20height=%27194%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgxIiBoZWlnaHQ9IjE5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

创建标签值​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27404%27%20height=%27184.7751937984496%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA0IiBoZWlnaHQ9IjE4NC43NzUxOTM3OTg0NDk2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

数据写入设置​

火山知识库的解析与分离策略，需单击前往火山配置，在[火山知识库控制台](<https://console.volcengine.com/vikingdb/knowledge/region:vdb-knowledge+cn-beijing/collection/list>)进行配置，包括文本向量化模型、向量维度、切片方式等。具体操作，请参考[创建知识库](<https://www.volcengine.com/docs/84313/1254463>)。​

输出​

输出参数固定为以下参数：​

说明

上传文本内容到知识库文档时，fileName 和 fileUrl 参数值为空。​

​

  * documentId：知识库文档的 ID。格式为 String。​

  * fileName：知识库文档的名称。格式为 String。​

  * fileUrl：知识库文档的访问地址。格式为 String。​

配置扣子知识库​

选择知识库来源为扣子知识库时，参考如下配置。​

输入​

知识库写入节点的输入参数固定为 knowledge，数据类型为 File<Doc>，表示用户需要上传到知识库中的文件。此文件可以固定为某个文件，由知识库的搭建者在搭建时上传；也可以引用上游节点的输出参数，在上游节点获取文件后上传。​

知识库​

在知识库区域，选择待写入内容的知识库。​

  * 知识库来源：选择扣子知识库。​

  * 添加知识库：选择具体的知识库。​

数据写入设置​

扣子知识库的文档解析策略和分段策略说明如下：​

​

参数​| 说明​  
---|---  
文档解析策略​| 文档解析策略用于定义系统如何解析文档中的文本、图片或表格内容。支持设置为：​

  * 快速解析：不提取文档中的图像、表格元素，适用于纯文本格式的内容，该模式下解析速度更快。​

  * 精准解析：提取文档中的图片、表格元素，支持选择提取的元素类型，默认包含图片元素、图片元素（OCR）、表格元素。该模式需要耗费更长的时间来解析并处理数据，如果工作流下游还有知识库检索节点，精准解析模式下上传的文档可能会未完成解析而无法被立即检索。​

  
分段策略​| 每次上传文档时都可以设置新文档的分段策略，合理的切片策略可以提高检索效率、提升检索结果的准确性。支持选择自动分段或自定义分段，详细说明可参考​知识库概述。​  
  
​

输出​

输出参数固定为以下参数：​

  * documentId：知识库文档的 ID。格式为 String。​

  * fileName：知识库文档的名称。格式为 String。​

  * fileUrl：知识库文档的访问地址。格式为 String。​

常见问题​

用户上传的文档和开发者上传的文档有什么区别？​

用户上传的文档和开发者上传的文档本身没有任何区别，都是知识库中的公开内容，可以被其他用户检索。但上传方式有区别，用户只能通过工作流的知识库写入节点上传文档，开发者则是在知识库管理页面或通过知识库 API 上传文档。​

知识库写入节点是异步节点吗？​

知识库写入节点为异步节点，工作流执行时无需等待文档上传完成。​

​

​

​

​

上一篇

变量赋值节点

下一篇

知识库检索节点