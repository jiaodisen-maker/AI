---
source_url: https://docs.coze.cn/guides/pet_image_plugin
title: '宠物风格化插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:40Z
---

# 宠物风格化插件 - 文档 - 扣子

宠物风格化插件

[宠物风格化插件](<https://www.coze.cn/store/plugin/7438922705132421120>)用于对普通宠物图片进行风格化处理，添加宠物照片的创意性和趣味性。​

使用限制​

扣子主账号内所有子账号共享宠物风格化插件的并发限制 ，其值为 4。​

计费说明​

宠物风格化插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

配置说明​

宠物风格化插件包含 spring_pets_image 工具。调用该工具时，你需要上传宠物图片并设置生成图片的风格。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
原图​| 设置原始图片来源，必填参数。​支持上传图片或引用上游节点的输出参数。​说明在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。​  
风格​| 设置图片风格。​

  * 可选值：春游记、花房、复活节彩蛋、打工人​

  * 默认值：春游记。​

  
风格强度​| 设置风格化强度。​

  * 可选值：低、中、高​

  * 默认值：中。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
data.images.image_url​| 宠物照片风格化后的图片 URL。URL 有效期为 30 天，请及时转存。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
  
​

示例​

在工作流中调用宠物风格化插件，风格化宠物图像。其中，指定风格为打工人，风格强度为高。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27804%27%20height=%27799.622504537205%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODA0IiBoZWlnaHQ9Ijc5OS42MjI1MDQ1MzcyMDUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

效果如下：​

原始图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27231.4814814814815%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIzMS40ODE0ODE0ODE0ODE1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

宠物风格化后的图片​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

​

* 宠物风格化插件 ID：7438923179067850767​

​

上一篇

背景替换插件

下一篇

风格滤镜插件