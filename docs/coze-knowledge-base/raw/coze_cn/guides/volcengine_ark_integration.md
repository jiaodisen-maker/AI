---
source_url: https://docs.coze.cn/guides/volcengine_ark_integration
title: '火山方舟 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:30:47Z
---

# 火山方舟 - 文档 - 扣子

火山方舟

扣子编程支持集成火山方舟大模型服务，用于调用方舟丰富的模型资源，以扩展 AI 编程项目的能力边界。你可以在方舟平台中添加模型推理接入点，然后为 AI 编程项目集成火山方舟模型服务，扩大其可选择的模型范围。​

费用说明​

通过火山方舟集成服务接入的方舟模型，其产生的 token 费用，由火山方舟平台收取。 ​

步骤一：获取火山方舟 API Key​

在集成火山方舟大模型能力前，需要先在火山方舟平台获取方舟模型的 API Key，该密钥将作为模型调用时的鉴权凭证。具体操作，请参考[API Key 管理](<https://www.volcengine.com/docs/82379/1361424>)。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27509%27%20height=%27112%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/65c9e560211e4ddd85644eabcece15b2~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤二：在方舟平台开通模型​

1.

登录[火山方舟控制台](<https://console.volcengine.com/ark>)。​

2.

在左侧导航栏中选择模型推理 > 在线推理。​

3.

在自定义推理接入点页签中，单击创建推理接入点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27617%27%20height=%27287%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/03ca38a364ed45ec932409c76106932b~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

根据页面提示，设置接入点名称，并选择模型。​

  * 在方舟平台中开通模型的详细说明可参考[方舟平台官方文档](<https://www.volcengine.com/docs/82379/1099522#模型推理使用入口>)。​

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

步骤三：为工作空间启用外部集成（企业旗舰版管控操作）​

企业旗舰版由组织管理员统一管控工作空间内外部集成的可用性。即组织管理员可以为工作空间设置空间内可用的外部集成。默认情况下，企业旗舰版所有工作空间内均不可使用外部集成。具体操作，请参考​步骤一：为工作空间启用外部集成。​

说明

企业旗舰版支持管控工作空间内外部集成的可用性，其他版本请跳过此步骤。​

​

步骤四：配置火山方舟集成​

在集成管理页面，单击火山方舟对应的配置，然后输入你已获取的 API Key。​

说明

配置外部集成后，系统会根据项目类型自动添加对应的官方技能到技能列表中。请勿随意移除官方技能，以免扣子 AI 在开发过程中因无法加载所需技能而报错。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27532%27%20height=%27291%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMyIiBoZWlnaHQ9IjI5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271051%27%20height=%27827.3829787234043%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA1MSIgaGVpZ2h0PSI4MjcuMzgyOTc4NzIzNDA0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤五：为项目接入火山方舟集成​

配置火山方舟集成后，你可以在开发 AI 编程项目时，输入添加火山方舟集成的相关需求，让扣子 AI 自动识别并加火山方舟技能来接入火山方舟集成。​

你可以在项目开发过程中，指定要接入你已创建的火山方舟大模型的接入点。例如调用火山方舟 ep-2025**** 模型提供新闻总结服务。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27615%27%20height=%27395%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjE1IiBoZWlnaHQ9IjM5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

企业微信机器人

下一篇

管理外部集成服务