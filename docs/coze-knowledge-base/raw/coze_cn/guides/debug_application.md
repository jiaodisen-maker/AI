---
source_url: https://docs.coze.cn/guides/debug_application
title: '调试低代码应用 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:17Z
---

# 调试低代码应用 - 文档 - 扣子

调试低代码应用

扣子编程提供了低代码应用搭建调试台，助力开发者快速定位及修复低代码应用搭建中的问题。在搭建低代码应用过程中，开发者能够实时对页面组件的属性配置及交互事件配置进行调试，验证各个组件功能与交互逻辑符合预期。例如当属性配置错误时，调试台会即时展示错误信息；当执行页面操作失败时，调试台将精准定位到该操作所绑定的事件及失败原因。​

功能入口​

你可以在低代码应用的用户界面页签中，单击调试，展开调试台。调试台包含如下两个核心部分：​

  * 时间线：提供组件交互事件的实时运行视图，便于开发者追溯事件执行过程。​

  * 错误：集中展示组件属性配置的错误或警告信息，便于开发者及时发现并修改属性配置。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272217%27%20height=%271201.8473684210526%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/429aa62ca9344b77ab3185ebac4453bc~tplv-goo7wpa0wc-quality:q75.image)​

​

时间线​

触发组件的事件时，时间线页签中会实时展示具体事件的详细信息，包括触发事件的组件、事件类型、触发动作、事件执行的时间点、事件耗时、事件执行状态、事件执行顺序、事件详情等信息，便于开发者快速追溯操作顺序并精准定位问题。​

以[拍照解题](<https://www.coze.cn/template/project/7475734454254895131?>)应用为例，使用者通过拍照功能上传题目图片后，单击开始解题，应用随机自动解答题目。其中，开始解题按钮已绑定交互事件，即单击时调用解题工作流并进行页面跳转。因此当你单击开始解题时，时间线中会记录并展示对应的事件信息。如果未上传题目，直接单击开始解题，工作流调用将失败，并展示失败原因。当上传题目后并再次单击开始解题，时间线中会继续记录事件的运行过程，此时显示工作流正常运行直到运行成功，并展示具体的输入值、输出值。​

执行失败​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271899%27%20height=%271137.2542372881358%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5OSIgaGVpZ2h0PSIxMTM3LjI1NDIzNzI4ODEzNTgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

执行中​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271905%27%20height=%271140.8474576271187%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkwNSIgaGVpZ2h0PSIxMTQwLjg0NzQ1NzYyNzExODciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

执行成功​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271892%27%20height=%271133.0621468926554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg5MiIgaGVpZ2h0PSIxMTMzLjA2MjE0Njg5MjY1NTQiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

你还可以单击成功、错误、加载中，筛选对应类型的事件。当你不再需要查看当前时间线内容时，可以单击清除图标，清除内容。​

注意

清除时间线内容后，不可恢复。​

​

错误​

当你配置的组件属性不符合平台规范时，调试台的错误页签中将实时展示对应的错误或警告信息。例如可见性属性仅允许设置为 false、true 或变量，如果输入非预期的值，错误页签中将立刻提示错误信息。当你将值修改正确后，错误信息自动清除。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272211%27%20height=%27550.1790697674419%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIxMSIgaGVpZ2h0PSI1NTAuMTc5MDY5NzY3NDQxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

上一篇

配置应用跳转外部链接的域名

下一篇

管理低代码应用