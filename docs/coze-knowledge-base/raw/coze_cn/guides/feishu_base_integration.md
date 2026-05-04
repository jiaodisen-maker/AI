---
source_url: https://docs.coze.cn/guides/feishu_base_integration
title: '飞书多维表格 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:38Z
---

# 飞书多维表格 - 文档 - 扣子

飞书多维表格

扣子编程支持集成飞书多维表格能力，可在获得授权的飞书账号内，对目标飞书多维表格及其表记录、表字段，进行创建、查询、修改、删除等操作。​

支持的能力​

  * 创建多维表格​

  * 搜索多维表格​

  * 获取多维表格元数据​

  * 创建多维表格数据表​

  * 删除多维表格数据表​

  * 查询多维表格下的全部数据表​

  * 在数据表中新增字段​

  * 在数据表中更新字段​

  * 在数据表中删除字段​

  * 查询单个数据表的全部字段​

  * 在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录​

  * 批量更新多维表格数据表中的记录，单次调用最多更新 500 条记录​

  * 查询多维表格数据表中的现有记录，单次最多查询 500 行记录​

  * 批量删除多维表格数据表中的记录​

配置方式​

步骤一：为工作空间启用外部集成（企业旗舰版管控操作）​

企业旗舰版由组织管理员统一管控工作空间内外部集成的可用性。即组织管理员可以为工作空间设置空间内可用的外部集成。默认情况下，企业旗舰版所有工作空间内均不可使用外部集成。具体操作，请参考​步骤一：为工作空间启用外部集成。​

说明

企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

​

步骤二：配置飞书多维表格集成​

在集成管理页面，单击飞书多维表格对应的配置，然后在弹出的授权框中，完成授权。​

在授权时，默认选择当前登录飞书的账号，你可以切换为其他飞书账号。配置完成后，当前工作空间中，所有集成了飞书多维表格服务的项目，均只能操作本次授权的飞书账号下的飞书多维表格。不能访问其他飞书账号。​

说明

配置外部集成后，系统会根据项目类型自动添加对应的官方技能到技能列表中。请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27404%27%20height=%27223%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA0IiBoZWlnaHQ9IjIyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27325%27%20height=%27340%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI1IiBoZWlnaHQ9IjM0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271047%27%20height=%27833.7927272727273%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA0NyIgaGVpZ2h0PSI4MzMuNzkyNzI3MjcyNzI3MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤三：为项目接入飞书多维表格集成​

配置飞书多维表格集成后，你可以在开发 AI 编程项目时，输入添加飞书多维表格集成服务的相关需求，让扣子 AI 自动识别并加载飞多维表格技能来接入飞书多维表格集成。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27491%27%20height=%27318%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkxIiBoZWlnaHQ9IjMxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

配置示例​

例如搭建一个识别发票的工作流，将识别结果写入到飞书多维表格进行存储和管理。​

1.

搭建工作流，让扣子 AI 自动识别并加载飞多维表格技能来接入飞书多维表格集成。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27326%27%20height=%27338%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzI2IiBoZWlnaHQ9IjMzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在飞书侧创建一个多维表格，并根据工作流输出字段设置数据表的表头和数据类型。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27750%27%20height=%2781%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUwIiBoZWlnaHQ9IjgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

3.

获取多维表格 ID 和数据表 ID。​

  * 你可以在多维表格的 URL 中获取多维表格ID 和数据表 ID，在运行工作流时，需要输入该 ID，用于指定向目标数据表写入数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271128%27%20height=%27124.44128113879005%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEyOCIgaGVpZ2h0PSIxMjQuNDQxMjgxMTM4NzkwMDUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

4.

试运行工作流。​

  * 试运行工作流，上传发票 PDF 以及输入多维表格 ID 和数据表 ID，试运行成功后，提取到的发票信息将发送到多维表格中。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271413%27%20height=%27948.0774193548388%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQxMyIgaGVpZ2h0PSI5NDguMDc3NDE5MzU0ODM4OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27752%27%20height=%27116%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUyIiBoZWlnaHQ9IjExNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

常见问题​

​向飞书多维表格推送数据时，提示 [1254045]: FieldNameNotFound错误，如何处理？​

上一篇

飞书消息

下一篇

Email