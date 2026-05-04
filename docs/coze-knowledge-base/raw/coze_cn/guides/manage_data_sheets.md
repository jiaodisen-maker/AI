---
source_url: https://docs.coze.cn/guides/manage_data_sheets
title: '管理数据表 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:43:33Z
---

# 管理数据表 - 文档 - 扣子

管理数据表

数据表创建完成后，你可以管理数据库中的数据表，包括管理表结构和表数据。​

编辑表结构​

编辑表结构是数据库维护和优化的重要部分，合理的表结构可以提高数据管理的效率和效果。​

参考以下操作，编辑表结构。​

1.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

2.

在资源库页面，选择目标数据库。​

3.

在表结构页签下，单击编辑表结构。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27568%27%20height=%27176%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/61857c64957f4e62a3e7e9c6e4058c11~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

在编辑表格页面，你可以执行新增、修改和删除操作，编辑后即生效。​

  * 新增：单击 \+ 新增，新增一个新字段。​

  * 修改：修改已有字段的名称、描述、数据类型、是否设为索引、是否必要。​

  * 删除：单击删除图标，删除一个已有字段。​

  * 注意

    * 修改字段名称，已有数据会存储在新的字段名下。​

    * 修改字段的数据类型，可能会导致已有数据丢失或截断，请谨慎操作。​

    * 删除已有字段，这个字段关联存储的数据也会被删除，请谨慎操作。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27522%27%20height=%27111%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIyIiBoZWlnaHQ9IjExMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看表结构​

数据表创建完成后，你可以查看数据表的表结构，例如字段名称、描述、数据类型以及是否必要等信息。​

1.

在资源库页面，选择目标数据库。​

2.

在表结构页签下，查看数据表结构。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27582%27%20height=%27175%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTgyIiBoZWlnaHQ9IjE3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

添加表记录​

在数据库中支持为测试数据或线上数据添加表记录，这是一种常见的数据操作，其作用因数据类型不同而有所差异。例如为数据库测试数据添加表记录，可以用于验证低代码智能体或应用的功能逻辑是否正确。通过添加多样化的测试数据，可以模拟不同的业务场景，确保智能体或应用在各种情况下都能正常运行。​

添加单条记录​

参考以下操作，为数据表添加一条新记录。​

1.

在资源库页面，选择目标数据库。​

2.

单击测试数据或线上数据页签，然后单击 \+ 新增行。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27552%27%20height=%27113%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTUyIiBoZWlnaHQ9IjExMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

根据字段的名称和数据类型，添加数据记录，然后单击插入。​

  * 添加线上数据记录时，需要为数据记录指定所属的渠道，例如微信小程序、扣子商店、飞书等，而添加测试数据记录时，无需指定渠道，默认为扣子编程渠道。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27304%27%20height=%27319%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzA0IiBoZWlnaHQ9IjMxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

批量导入记录​

你可以先下载数据记录模板文件，按照模板要求填写数据记录，然后上传文件完成批量导入。​

说明

上传的文件格式为 Excel 或 CSV ，文件最大不超过 20MB。​

​

参考以下操作，批量导入数据记录。​

1.

在资源库页面，选择目标数据库。​

2.

单击测试数据或线上数据页签，然后单击批量导入。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27568%27%20height=%27121%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTY4IiBoZWlnaHQ9IjEyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

选择导入渠道。​

  * 批量导入线上数据记录时需要选择导入渠道，导入成功后，每条数据记录的sys_platform的值均为所选的渠道。而批量导入测试数据时无需此操作，默认为扣子编程渠道。​

4.

单击下载模板，按照模板要求填写数据记录，上传文件并单击下一步。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%27211%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYzIiBoZWlnaHQ9IjIxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

完成表结构配置，然后单击下一步。​

  * 数据表：多 sheet 情况下需选择要导入的数据表，单 sheet 情况下选择默认的 sheet1。​

  * 表头：指定表头所在的行，表头指定错误可能导致参数校验不通过，请仔细核对表头信息以确保数据导入的准确性。​

  * 数据起始行：指定从第几行开始导入数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27463%27%20height=%27239%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYzIiBoZWlnaHQ9IjIzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

预览要导入的数据记录，确保符合预期后单击下一步。​

7.

单击确认。​

查看表数据​

在智能体或应用开发与运维过程中，数据库中的测试数据和线上数据发挥着重要作用，扣子数据库中的测试数据和线上数据相互隔离，不可直接转换。你可以查看手动添加表数据，也可以查看调试或运行时产生的数据。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27626%27%20height=%27134%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI2IiBoZWlnaHQ9IjEzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

默认情况下，扣子数据库的测试数据和线上数据按下述规则分类。同时，你也可以调整各个发布渠道的数据读写目标，切换渠道访问的是线上数据还是测试数据，详情请参考​设置渠道读写配置。​

  * 测试数据：是开发者在扣子编程中调试智能体或应用时产生的数据，具有临时性。开发者通过查看测试数据来发现并修复问题，优化智能体和应用的功能与性能。​

  * 线上数据：是智能体或应用在实际运行时产生的真实数据。查看线上数据主要用于业务分析、决策支持和问题排查等场景，以确保智能体或应用的稳定运行。​

  * 线上数据支持按照发布渠道隔离数据，其渠道隔离规则以你创建数据库时选择的渠道模式为准。例如选择渠道隔离，则表示用户在一个渠道（如飞书）中产生的数据无法在另一个渠道（如微信）查看。​

  * 说明

不支持查看豆包渠道数据。​

​

导出表数据​

你可将测试数据或线上数据，分别以 CSV 文件格式导出至本地，用于本地备份或数据分析。​

在资源库页面，选择目标数据库。​

1.

单击测试数据或线上数据页签，然后单击数据导出。​

  * 系统会将全量的测试数据或线上数据导出至本地。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272109%27%20height=%27465.6867052023121%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEwOSIgaGVpZ2h0PSI0NjUuNjg2NzA1MjAyMzEyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

管理数据库资源

下一篇

数据库常见问题