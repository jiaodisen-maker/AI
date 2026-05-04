---
source_url: https://docs.coze.cn/developer_guides/query_database_list
title: '查询数据库列表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:23:29Z
---

# 查询数据库列表 - 文档 - 扣子

查询数据库列表

查询指定工作空间下的扣子数据库列表，支持分页查询。​

基础信息​

​

请求方式​| GET​  
---|---  
请求地址​| ​Plain Text复制https://api.coze.cn/v1/databases​​  
权限​| Workspace.listDatabase​确保调用该接口使用的访问令牌开通了Workspace.listDatabase权限，详细信息参考[鉴权方式](<https://docs.coze.cn/developer_guides/authentication>)。​  
接口说明​| 查询指定工作空间下的扣子数据库列表。​  
  
​

请求参数​

Header​

​

参数​| 取值​| 说明​  
---|---|---  
Authorization​| Bearer $Access_Token​| 用于验证客户端身份的访问令牌。你可以在扣子平台中生成访问令牌，详细信息，参考[准备工作](<https://www.coze.cn/docs/developer_guides/preparation>)。​  
Content-Type​| application/json​| 请求正文的方式。​  
  
​

Query​

​

参数​| 类型​| 是否必选​| 示例​| 说明​  
---|---|---|---|---  
workspace_id​| String​| 必选​| 753232939603****​| 数据库所在的工作空间 ID。​  
page_num​| Integer​| 可选​| 1​| 用于指定返回数据的页数，默认值为 1。​  
page_size​| Integer​| 可选​| 20​| 每页返回的记录数量，默认值为 20，最大支持 1000条记录。​  
  
​

​

返回参数​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
data​| Object of [OpenDatabaseInfoList](<https://docs.coze.cn/developer_guides/query_database_list#opendatabaseinfolist>)​| {"items":[...],"has_more":false,"total_count":5}​| 已创建的扣子数据库列表。​  
code​| Long​| 0​| 调用状态码。​

  * 0 表示调用成功。​

  * 其他值表示调用失败。你可以通过 msg 字段判断详细的错误原因。​

  
msg​| String​| ""​| 状态信息。API 调用失败时可通过此字段查看详细错误信息。​状态码为 0 时，msg 默认为空。​  
detail​| Object of [ResponseDetail](<https://docs.coze.cn/developer_guides/query_database_list#responsedetail>)​| {"logid":"20241210152726467C48D89D6DB2****"}​| 包含请求的详细信息的对象，主要用于记录请求的日志 ID 以便于排查问题。​  
  
​

OpenDatabaseInfoList​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
has_more​| Boolean​| false​| 标识当前返回的数据是否为完整数据集。枚举值包括：​

  * true ：表示未返回所有数据。​

  * false，表示已返回所有数据。​

  
total_count​| Integer​| 10​| 符合当前查询条件的数据库总数。​  
items​| Array of [OpenDatabaseInfo](<https://docs.coze.cn/developer_guides/query_database_list#opendatabaseinfo>)​| [{"id":"761070127115408****","table_name":"user_info",...}]​| 数据库列表，包含多个数据库的详细信息。每个数据库项包括数据库 ID、表名、字段信息、索引列表等。​  
  
​

OpenDatabaseInfo​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
id​| String​| 761070127115408****​| 数据库 ID。​  
app_id​| String​| 760615362298825****​| 数据库所在的低代码应用 ID。​  
create_time​| String​| 1704067200​| 数据库创建时间。Unixtime 时间戳格式，精确到秒（s）。​  
icon_url​| String​| https://lf3-appstore-sign.oceancloudapi.com/ocean-cloud-tos/database/icon/default.png?x-expires=177****&x-signature=IuE****​| 数据库头像 URL。​​  
table_name​| String​| user_info​| 数据表名称。​  
database_type​| String​| coze_database​| 数据库类型。枚举值如下：​

  * coze_database：扣子数据库​

  * volcano_database：火山数据库​

  
rw_mode​| String​| unlimited_read_write​| 数据表的读写模式。枚举值包括：​

  * limited_read_write：单用户模式，开发者和用户只能对自己创建的数据进行读写操作。​

  * read_only：只读模式。开发者和用户只能对自己创建的数据进行读操作。​

  * unlimited_read_write：多用户模式，开发者和用户能对所有人创建的数据进行读写操作，该模式仅在工作流节点中有效。​

  
workspace_id​| String​| 753232939603****​| 数据库所在的工作空间 ID。​  
creator_id​| String​| 852741963085274****​| 数据库创建者 ID。​  
update_time​| String​| 1704153600​| 数据库更新时间。Unixtime 时间戳格式，精确到秒（s）。​  
table_desc​| String​| 存储用户基本信息​| 数据表描述。​  
fields​| Array of [OpenFieldItem](<https://docs.coze.cn/developer_guides/query_database_list#openfielditem>)​| [{"name":"id","type":"integer",...}]​| 数据表的字段信息列表，包含字段名称、类型、是否必填、是否主键等属性。每个字段项详细描述了字段的元数据信息，用于定义表结构。​  
indexs​| Array of [OpenIndexItem](<https://docs.coze.cn/developer_guides/query_database_list#openindexitem>)​| [{"index_name":"idx_name","field_names":["name"]}]​| 数据表的索引列表，包含索引名称、字段名列表和索引描述等信息。每个索引项详细描述了索引的元数据信息，用于优化查询性能。​  
  
​

OpenFieldItem​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
type​| String​| string​| 存储字段的数据类型，大语言模型会按照选择的数据类型对用户输入的内容进行处理和保存。目前支持的数据类型包括 String、Integer、Time、Number、Boolean。​  
is_required​| Boolean​| true​| 存储字段是否为必要字段。枚举值如下：​

  * true：必要字段。​

  * false：非必要字段。​

  
is_system_field​| Boolean​| false​| 标识字段是否为系统字段。系统默认字段为 true，用户自定义字段均为 false。​  
is_primary_key​| Boolean​| false​| 标识字段是否为表主键。仅系统生成的 id 字段为 true，用户自定义字段均为 false。​  
name​| String​| name​| 存储字段名称，只能包含小写字母、数字、下划线（_）、必须以英文字母开头，最多 64 字符，不支持使用数据库关键词或保留字作为字段名称。​扣子编程关键词和保留字列表，请参考[扣子数据库关键词和保留字有哪些？](<https://docs.coze.cn/guides/database_faq#22ad0019>)。​  
desc​| String​| 用户姓名​| 存储字段的补充说明，可以是对存储字段的自然语言描述、示例数据，也可以是格式说明等。​  
  
​

OpenIndexItem​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
index_name​| String​| idx_level​| 索引的名称，需确保唯一性。如果未传入该字段，服务端将按照一定规则自动生成。​  
field_names​| Array of String​| ["level"]​| 当前仅支持单字段索引，即数组中只能包含一个字段名。​  
comment​| String​| 等级​| 索引描述。​  
  
​

ResponseDetail​

​

参数​| 类型​| 示例​| 说明​  
---|---|---|---  
logid​| String​| 20241210152726467C48D89D6DB2****​| 本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此logid及错误码联系扣子团队获取帮助。详细说明可参考[获取帮助和技术支持](<https://docs.coze.cn/guides/help_and_support>)。​  
  
​

示例​

请求示例​

​

JSON

复制

curl --location --request GET 'https://api.coze.cn/v1/databases?workspace_id=753232939603****&page_num=1&page_size=20' \​

\--header 'Authorization : Bearer pat_O****' \​

\--header 'Content-Type: application/json'​

​

返回示例​

​

JSON

复制

{​

"data": {​

"has_more": false,​

"total_count": 2,​

"items": [​

{​

"id": "761070127115408****", ​

"table_desc": "存储单词",​

"fields": [​

{​

"type": "string",​

"is_required": false,​

"is_system_field": false,​

"name": "word",​

"desc": "单词"​

},​

{​

"is_required": false,​

"is_system_field": false,​

"name": "phonetic_alphabet",​

"desc": "音标",​

"type": "string"​

},​

{​

"is_required": false,​

"is_system_field": false,​

"name": "meaning",​

"desc": "含义",​

"type": "string"​

},​

{​

"is_required": true,​

"is_system_field": false,​

"name": "status",​

"desc": "是否已学习",​

"type": "boolean"​

}​

],​

"rw_mode": "unlimited_read_write",​

"indexs": [],​

"database_type": "coze_database",​

"workspace_id": "753232939603****",​

"app_id": "0",​

"creator_id": "852741963085274****",​

"create_time": "1760568791",​

"update_time": "1761033382",​

"icon_url": "https://lf3-appstore-sign.oceancloudapi.com/ocean-cloud-tos/database/icon/default.png?x-expires=177****&x-signature=IuE****",​

"table_name": "word"​

},​

{​

"indexs": [​

{​

"field_names": [​

"level"​

],​

"comment": "等级",​

"index_name": "idx_level"​

}​

],​

"app_id": "0",​

"create_time": "1772517749", ​

"icon_url": "https://lf3-appstore-sign.oceancloudapi.com/ocean-cloud-tos/database/icon/default.png?x-expires=177****&x-signature=IuE****",​

"table_name": "user_info",​

"database_type": "coze_database",​

"rw_mode": "unlimited_read_write",​

"id": "761290326253828****",​

"workspace_id": "749820488328041****",​

"creator_id": "23903235371****",​

"update_time": "1772517749",​

"table_desc": "存储用户基本信息的数据库",​

"fields": [​

{​

"is_system_field": false,​

"name": "user_id",​

"desc": "姓名",​

"type": "string",​

"is_required": true​

},​

{​

"type": "integer",​

"is_required": true,​

"is_system_field": false,​

"name": "level",​

"desc": "等级"​

}​

]​

}​

]​

},​

"code": 0,​

"msg": "",​

"detail": {​

"logid": "20241210152726467C48D89D6DB2****"​

} ​

}​

​

错误码​

如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考[错误码](<https://docs.coze.cn/developer_guides/coze_error_codes>)文档查看对应的解决方法。​

​

上一篇

删除数据

下一篇

查询异步执行结果