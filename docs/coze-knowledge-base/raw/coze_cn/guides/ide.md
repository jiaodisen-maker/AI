---
source_url: https://docs.coze.cn/guides/ide
title: '使用 IDE 创建插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:39:39Z
---

# 使用 IDE 创建插件 - 文档 - 扣子

使用 IDE 创建插件

扣子编程 IDE 是扣子编程提供的在线编码和运行环境，允许你在多种技术栈中创建插件。创建插件后，必须发布插件才可以被低代码智能体使用。插件发布后，IDE 会帮助你托管运行代码，你无需关心环境配置、服务部署等步骤。​

说明

  * 个人工作空间中的插件，仅能被个人调用；企业工作空间中插件，能被任意企业成员调用。​

  * 插件发布了新版本后，使用了这个插件的低代码智能体会自动使用已发布的最新版本。​

​

服务升级说明​

为提供更优质的 IDE 插件开发环境，我们将从2025年12月3日开始逐步对 IDE 插件的后台开发工具进行升级。本次升级仅优化后台服务，不会对插件代码造成影响，请放心操作。​

在插件列表中，存量的 IDE 插件会提示服务升级。你只需单击服务升级，以及迁移，系统会自动完成迁移操作。​

说明

  * 如果不迁移，你将无法编辑 IDE 插件。​

  * 为确保升级后插件的正常运行，建议你在迁移完成后，重新试运行插件进行验证。​

  * 迁移完成后，请通过插件页面重新打开插件编辑页面，原插件编辑页面链接将失效。​

  * IDE 服务升级后，不支持 AI 助手功能。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272286%27%20height=%27533.8404624277457%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/65ab4df379fc4048b0e4fd6de6e80d60~tplv-goo7wpa0wc-quality:q75.image)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272306%27%20height=%27523.3475177304964%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d6f471628bd4099832ddb497a43810b~tplv-goo7wpa0wc-quality:q75.image)​

​

​

创建插件​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，选择 +资源 > 插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27504%27%20height=%27170%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA0IiBoZWlnaHQ9IjE3MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在新建插件对话框，根据以下信息完成配置并单击确认。​

  * ​

参数​| 说明​  
---|---  
插件图标​| 单击默认图标后，你可以上传本地图片文件作为新的图标。​  
插件名称​| 自定义插件名称，用于标识当前插件。建议输入清晰易理解的名称，便于大语言模型搜索与使用插件。​  
插件描述​| 插件的描述信息，一般用于记录当前插件的用途。​  
插件工具创建方式​| 选择云侧插件-在扣子 IDE中创建。​  
IDE 运行时​| 选择 Node.js 或者 Python3。​  
  
​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27301%27%20height=%27407%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAxIiBoZWlnaHQ9IjQwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

5.

创建工具。​

a.

在插件详情页，单击在IDE中创建工具。​

b.

单击添加工具，然后在弹出的创建工具对话框，设置工具名称和介绍，以明确工具的用途，并单击确定。​

  * 工具名称和介绍越清晰，大语言模型就越能理解并使用它。创建后，你将跳转到扣子编程 IDE 页面进行编码。​

  * 如果你需要添加多个工具，可以在 IDE 左上角工具列表区域，单击 + 图标。你还可以通过单击列表内某一工具的设置图标，来编辑、删除或重置代码。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27209%27%20height=%27162%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA5IiBoZWlnaHQ9IjE2MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

（可选）在 IDE 左下角依赖包区域，管理依赖包，所有工具共用该依赖列表。​

  * 你可以单击 + 或者单击添加依赖，输入依赖包名称并选择版本（可通过依赖名@版本号的格式进行搜索），然后安装依赖包。安装日志显示在控制台 Console 区域。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27486%27%20height=%27143%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg2IiBoZWlnaHQ9IjE0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

在页面中间代码区域，根据所选的 IDE 运行时，默认内置了代码模板。​

  * 注意

    * 请勿删除或修改模板内的 handler 方法，否则将导致函数运行失败。​

    * 返回内容必须为 JSON 对象。​

​

  * 以下提供了不同 IDE 运行时的代码模板，你可以参考模板内的方式获取输入参数、打印日志。​

  * Node.js​

  * ​

JavaScript

复制

/**​

* Each file needs to export a function named `handler`. This function is the entrance to the Tool.​

* @param {Object} args.input - input parameters, you can get test input value by input.xxx.​

* @param {Object} args.logger - logger instance used to print logs, injected by runtime​

* @returns {*} The return data of the function, which should match the declared output parameters.​

* ​

* Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.​

*/​

export async function handler({ input, logger }: Args<Input>): Promise<Output> {​

const name = input.name || "world";​

​

logger.info(name);​

​

return {​

message: `Hello, ${name}!`,​

};​

};​

​

  * Python3​

  * ​

Python

复制

# Python code example​

"""​

Each file needs to export a function named `handler`. This function is the entrance to the Tool.​

​

Parameters:​

args: parameters of the entry function.​

args.input - input parameters, you can get test input value by args.input.xxx.​

args.logger - logger instance used to print logs, injected by runtime.​

​

Remember to fill in input/output in Metadata , it helps LLM to recognize and use tool.​

​

Return:​

The return data of the function, which should match the declared output parameters.​

"""​

def handler(args: Args[Input])->Output:​

# get name from input ​

name=args.input.name​

​

# print name​

args.logger.info(name)​

​

return {"content": "Hello,"\+ name }​

​

8.

单击元数据，配置工具的元数据。​

  * 元数据的作用是让大语言模型理解每个工具输入或输出参数有哪些、各个参数有何含义。当用户在使用该工具的智能体时，模型会根据工具的元数据信息，从用户问答中解析、提取出对应的输入参数，并选择调用该工具，流程图如下所示。因此，在工具的元数据内提供详细的参数说明，可以让大语言模型更准确的使用工具。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27663%27%20height=%27350%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjYzIiBoZWlnaHQ9IjM1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 以下是一个网页搜索工具的元数据，当智能体内添加了该工具后，模型会根据工具的元数据信息，在收到匹配的用户查询语句时，调用工具处理用户任务。例如，如果用户发送消息查询上海天气，智能体将会使用该工具响应用户。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27560%27%20height=%27327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYwIiBoZWlnaHQ9IjMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 元数据配置说明：​

  * ​

配置项​| 描述​  
---|---  
名称​| 工具名称。建议输入清晰易理解的名称，便于后续大语言模型搜索与使用工具。​  
描述​| 工具的描述信息，一般用于记录当前工具的用途。​  
启用​| 是否启用当前工具。使用说明：​
    * 如果工具未开发测试完成，建议先禁用该工具，只启用并发布已通过测试的工具。​
    * 如果需要下线某一工具，可将该工具设置为禁用，并再次发布插件。​
    * 如果插件中只有一个工具，则不支持禁用该工具。如需下线该工具，你可以选择直接删除该插件，或者创建另一个工具并完成开发测试后，再禁用该工具，最后发布插件。​  
输入参数​| 当前工具对应接口的输入参数信息。准确、清晰易理解的参数名称、描述等信息，可以让大语言模型更准确的使用工具。​  
输出参数​| 当前工具对应接口的输出参数信息。准确、清晰易理解的参数名称、描述等信息，可以让大语言模型更准确的使用工具。​  
  
​

9.

在页面右侧单击测试代码图标并输入所需的参数，然后单击运行，测试工具。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27207%27%20height=%27174%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA3IiBoZWlnaHQ9IjE3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 你可以在控制台 Console 区域查看运行日志、在输出区域查看运行结果，单击更新输出参数，将输出结果中的参数更新到元数据的输出参数中，以确保输出参数的一致性和准确性。​

  * 说明

如果插件试运行正常，但是在智能体或工作流中运行不符合预期时，建议你检查插件的输出参数是否存在以下情况：​

    * 参数定义不完整：未定义所有必要的输出参数和数据类型，可能导致数据处理不全。如果输出参数是数组类型，则必须要明确定义数组元素的数据类型。​

    * 数据类型不一致：实际返回参数的数据类型与自定义输出参数的数据类型不匹配时，在智能体中调用插件可能导致输出参数的值为空，而在工作流中调用插件可能会导致运行失败。​

    * 未启用的输出参数：已定义输出参数但是未开启，可能导致该参数不被输出。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27468%27%20height=%27135%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY4IiBoZWlnaHQ9IjEzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

10.

测试完成后，在页面右上角单击发布。​

11.

在弹出的发布对话框，核对工具信息，并设置是否启用工具，然后单击下一步。​

12.

在个人信息收集声明 Privacy Collection Statement 对话框，如果该工具会收集、传输用户个人信息，则需要选择是，并根据实际情况选择具体收集的个人信息，否则选择否，最后单击。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27294%27%20height=%27325%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjk0IiBoZWlnaHQ9IjMyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上架到商店​

你可以将插件上架到扣子插件商店或企业插件商店。不能同时上架扣子插件商店和企业插件商店，仅支持选择其中一个渠道。​

  * 上架扣子插件商店​

  * 对于通用功能、不涉及敏感数据且具有广泛适用性的公开插件，你可以将其上架到扣子商店，以便更多扣子用户发现、使用。详情请参考​将插件上架到插件市场。​

  * 上架企业插件商店​

  * 仅企业旗舰版支持。​

  * 对于企业自主开发的涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的插件，你可以将其上架到企业插件商店，供企业成员使用。详情请参考​管理企业插件。​

上一篇

通过 JSON 或 YAML 文件导入插件

下一篇

使用代码注册插件