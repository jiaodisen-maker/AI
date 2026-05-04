---
source_url: https://docs.coze.cn/guides/radio_button_mini_program
title: '单选按钮 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:38:00Z
---

# 单选按钮 - 文档 - 扣子

单选按钮

单选按钮组件用于从多个选项中选择一个，确保用户只能选择一个选项。​

属性设置​

单选按钮组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考​设置组件属性和事件。​

绑定静态数据​

你可以输入选项名称和选项值，为单选按钮组件绑定静态数据。​

  * 选项名称：设置选项的显示名称，能够清晰展示每个选项的含义。​

  * 选项值：选项对应的具体值，用于数据处理或与接口的数据对齐。​

例如通过单选按钮组件设置满意度选项，其中选项名称为非常满意、一般、不满意，选项值为 3、2、1。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27627%27%20height=%27350%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/544d6a8060d24ea2994ffd2ee9ab1782~tplv-goo7wpa0wc-quality:q75.image)​

​

绑定动态数据​

通过绑定工作流为单选按钮获取动态数据。​

1.

为单选按钮绑定一个 Array 类型的数据源。​

  * 例如将工作流的输出变量（例如 output）作为单选按钮的数据源，该输出变量必须为 Array 类型。绑定工作流后，需要配置事件以触发工作流的调用，确保数据能够动态加载。​

  *     * 工作流输出变量​

    * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27523%27%20height=%27681.0708955223881%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTIzIiBoZWlnaHQ9IjY4MS4wNzA4OTU1MjIzODgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

绑定数据源​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27269%27%20height=%27264.98507462686564%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY5IiBoZWlnaHQ9IjI2NC45ODUwNzQ2MjY4NjU2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

配置事件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27383%27%20height=%27528.7686567164179%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzgzIiBoZWlnaHQ9IjUyOC43Njg2NTY3MTY0MTc5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

2.

为单选按钮组件中的绑定具体的数据字段。​

  * 绑定数据源后，你可以通过 item 变量遍历和访问 Array 类型数据源中的每个元素。即你可以为单选按钮组件中的选项名称和选项值绑定具体的数据字段。例如为选项名称绑定数据字段 {{item.show_name}}，为选项值绑定数据字段 {{item.show_id}}。具体示例，请参考​配置示例。​

  * 说明

为图片组件绑定数据字段时，字段值需为图片地址，支持上传 jpg、png格式，暂不支持svg。​

​

  * item 变量 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27204%27%20height=%27468%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA0IiBoZWlnaHQ9IjQ2OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

绑定数据字段​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27269%27%20height=%27322%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY5IiBoZWlnaHQ9IjMyMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

可见性设置​

单选按钮组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。​

  * 表达式方式​

  * 设置为 false：显示组件。​

  * 设置为 true：隐藏组件。​

  * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考​隐藏组件。​

  * 常用条件方式​

  * 支持通过可视化界面设置条件，以控制组件的可见性。​

例如通过下拉选择组件 Picker2 的值动态控制两个单选按钮组件 Radio3、Radio4 的可见性，其中 Picker2 的选项为男生（值为 0）、女生（值为 1）。​

  * 设置单选按钮组件 Radio3 的隐藏条件为 Picker2.value = 1，即在 Picker2 组件中选择女生时，隐藏组件 Radio3，展示组件 Radio4。​

  * 设置单选按钮组件 Radio4 的隐藏条件为 Picker2.value = 0 ，即在 Picker2 组件中选择男生时，隐藏组件 Radio4，展示组件 Radio3。​

Radio3 组件可见性配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27535%27%20height=%27547.1590909090909%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM1IiBoZWlnaHQ9IjU0Ny4xNTkwOTA5MDkwOTA5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

Radio4 组件可见性配置​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27562%27%20height=%27544.969696969697%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYyIiBoZWlnaHQ9IjU0NC45Njk2OTY5Njk2OTciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

效果​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27476%27%20height=%27323.68%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDc2IiBoZWlnaHQ9IjMyMy42OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

事件设置​

通过配置单选按钮组件的事件，可以为单选按钮组件添加丰富的交互功能，以增强用户体验和界面的互动性。​

​

事件项​| 说明​  
---|---  
事件类型​| 数据改变时：当单选按钮组件的数据发生变化时，触发预定义的事件。​  
组件方法​| 支持以下方法：​

  * 设置数据：为组件设置或更新数据。​

  * 设置禁用：使组件变为禁用状态，用户无法与之交互。​

  * 设置隐藏：隐藏组件，使其不可见。​

  
  
​

配置示例​

例如某企业想组织员工观影，可通过创建工作流查询正在上映的电影，并设计表单让员工通过单选按钮选择感兴趣的影片，从而高效完成调查。具体操作如下：​

1.

创建工作流（test2）。​

  * 使用淘票票插件（GetMovieAndShow）搜索正在上映或即将上映的电影。其中，在结束节点中，设置输出变量 output 的值为淘票票插件输出结果中的 return_value ，其为 Array 类型，包括影片名称、ID、类型、描述等信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271864%27%20height=%27719.4774346793349%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg2NCIgaGVpZ2h0PSI3MTkuNDc3NDM0Njc5MzM0OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

搭建表单页面。​

  * 搭建一个小程序表单页面，包括姓名、选择的影片等。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27212%27%20height=%27391%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEyIiBoZWlnaHQ9IjM5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

为单行输入组件（Input1）配置事件。​

  * 输入员工名字后，将调用工作流（test2）搜索正在上映或即将上映的电影。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27403%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkzIiBoZWlnaHQ9IjQwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

绑定数据。​

a.

将工作流的输出变量 output 绑定到单选按钮组件上。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcyIiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

为单选按钮组件中的选项名称和选项值绑定数据字段。​

  * show_name 字段值为影片名称。 ​

  * show_id 字段值为影片 ID。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27262%27%20height=%27318%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjYyIiBoZWlnaHQ9IjMxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

预览效果。​

  * 你还可以为提交按钮添加事件，将提交结果写入飞书多维表格进行统计。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27265%27%20height=%27562%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY1IiBoZWlnaHQ9IjU2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

图片上传

下一篇

标签栏