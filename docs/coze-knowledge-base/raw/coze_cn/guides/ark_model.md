---
source_url: https://docs.coze.cn/guides/ark_model
title: '接入火山方舟模型 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:43:46Z
---

# 接入火山方舟模型 - 文档 - 扣子

接入火山方舟模型

订阅企业标准版、企业旗舰版后，你可以在方舟平台中添加更多模型推理接入点，扩大智能体可选择的模型范围。此后，在扣子编程中创建低代码智能体并为其设置模型时，便可在模型列表中选择对应的模型推理接入点。​

使用限制​

​

限制​| 说明​  
---|---  
付费版本​| 

  * 企业标准版、企业旗舰版支持接入火山方舟模型。​

  * 如果你之前是扣子专业版用户，升级到个人付费版后，历史已创建的智能体和应用可以继续使用原有的方舟模型。未使用方舟模型的智能体和应用，后续将无法在模型下拉列表中查看或选择方舟模型。​

  
操作权限​| 仅企业超级管理员、被授予火山方舟权限的成员可以在方舟平台开通模型，给成员设置权限的操作请参见​为成员设置火山引擎 IAM 权限。​  
更新模型版本​| 接入火山方舟模型之后，如果需要更新模型版本，应重新创建模型接入点。直接在方舟平台为接入点切换模型版本不会在扣子编程中生效。​  
使用模型​| 接入火山方舟视频生成模型后，只支持在工作流的视频生成节点中使用。关于视频生成节点的更多信息，请参考​视频生成节点。​  
  
​

步骤一：在方舟平台开通模型​

在方舟平台中开通模型的详细说明可参考[方舟平台官方文档](<https://www.volcengine.com/docs/82379/1099522#模型推理使用入口>)。开通模型后，如果不再使用某个模型，需要先在方舟平台中停止此模型的推理接入点，再删除接入点。​

1.

登录[火山方舟控制台](<https://console.volcengine.com/ark>)。​

2.

在左侧导航栏中选择模型推理 > 在线推理。​

3.

在自定义推理接入点页签中，单击创建推理接入点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27279.53757225433526%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjI3OS41Mzc1NzIyNTQzMzUyNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

根据页面提示，设置接入点名称，并选择模型。​

  * ​

参数名称​| 参数说明​  
---|---  
接入点名称​| 接入点名称。​  
接入点描述​| 描述接入模型的业务需求，如接入场景、用途（如测试、线上业务）等。​  
模型选择​| 单击添加模型，在选择模型页面，你可以通过模型广场或模型仓库页签筛选对应的模型。​
    * 选择模型广场中的模型后，需进一步选择模型版本。​
    * 选择模型仓库中的模型后，需进一步选择模型版本和 Checkpoint。当前仅支持基于豆包系列模型进行精调的模型。模型仓库的详细说明，可参考[模型仓库](<https://www.volcengine.com/docs/82379/1217587>)。​  
购买方式​| 支持按Token付费、按模型单元付费。​  
接入点限流​| 设置限流后，使用此模型的智能体回复频率均受限于此设置。​建议不设置接入点限流。​  
  
​

5.

单击开通模型并接入。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27373.6416184971098%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjM3My42NDE2MTg0OTcxMDk4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

6.

在模型推理页面可查看已接入的模型列表。​

  * 模型状态为健康时，表示该模型可以在扣子编程中使用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27253.41040462427748%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjI1My40MTA0MDQ2MjQyNzc0OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 开通模型后，企业中所有工作空间将默认允许使用该模型。空间所有者和管理员也可以禁止本空间成员使用该模型，具体步骤请参见​为空间配置模型。​

步骤二：在扣子编程中为低代码智能体选择模型​

在智能体的编排页面，开发者可以在模型列表的方舟接入点区域，选择已开通的方舟模型。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27272.5694444444444%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI3Mi41Njk0NDQ0NDQ0NDQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

上一篇

模型服务

下一篇

接入自定义模型