---
source_url: https://docs.coze.cn/tutorial/f6h9bsps
title: '查询股票价格 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:21Z
---

# 查询股票价格 - 文档 - 扣子

查询股票价格

本文以开发一个查询股票价格的插件为例，介绍如何通过插件集成的 IDE 工具创建自定义插件。​

步骤一：构建低代码工作流​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，单击 +资源 > 插件。​

4.

在新建插件对话框内完成配置，并单击确认。​

  * 插件名称：示例值 查询股票价格。​

  * 插件描述：示例值 接收股票名称，查询并返回对应价格信息。​

  * 插件工具创建方式：选择在 Coze IDE 中创建。​

  * IDE 运行时：选择 Node.js。​

5.

待页面自动跳转后，单击在IDE中创建工具。​

6.

在弹出的创建工具对话框，设置工具名称与介绍，并单击确定。​

  * 工具名称：示例值 search_stock_prices。​

  * 工具介绍：示例值 根据股票名称查询股票价格。​

步骤二：配置并发布插件​

1.

在 IDE 工具中，单击元数据页签。​

2.

在元数据的输入参数区域，单击编辑，并新增 code 参数，描述为股票名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27442%27%20height=%27341%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fc4abfe559b24ca3ac12f85252b604c7~tplv-goo7wpa0wc-quality:q75.image)​

​

3.

单击代码页签，在代码编辑器中通过快捷键唤起 AI 助手（macOS 为 Command + I、Windows 为 Ctrl + I）。​

4.

向 AI 助手输入代码编辑需求，由 AI 生成代码。​

  * 例如输入：根据 input.code，到 alpha vantage 查询股票价格。​

5.

AI 生成代码后，可自行调整代码内容。​

  * 完整示例代码如下，你可以选择直接复制使用该示例代码。​

  * ​

JavaScript

复制

import { Args } from '@/runtime';​

import { Input, Output } from "@/typings/search_stock_prices/search_stock_prices";​

import axios from 'axios';​

export async function handler({ input, logger }: Args<Input>): Promise<Output> {​

const code = input.code;​

const apiKey = 'YOUR_ALPHA_VANTAGE_API_KEY';​

const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${code}&apikey=${apiKey}`;​

​

try {​

const response = await axios.get(url);​

const data = response.data['Global Quote'];​

return {​

code: code,​

price: data['05. price'],​

};​

} catch (error) {​

logger.error(`Error fetching stock price for ${code}: ${error}`);​

return {​

code: code,​

price: null,​

};​

}​

}​

​

6.

在页面左下角，添加 axios@1.6.8 依赖包。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27557%27%20height=%27143%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU3IiBoZWlnaHQ9IjE0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

7.

在页面右上角单击测试代码图标，并在输入区域单击自动生成图标。​

8.

将自动生成的测试数据改为 AAPL，并单击运行。​

9.

在输出区域查看测试结果，并单击更新输出参数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27514%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjUxNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

10.

在页面中间单击元数据页签，在输出参数区域单击编辑，完善输出参数的描述。​

  * code 描述为股票名称。​

  * price 描述为价格。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27561%27%20height=%27151%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYxIiBoZWlnaHQ9IjE1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

11.

在页面右侧单击运行，重新进行测试。测试无问题后，在页面右上角单击发布。​

12.

在发布对话框，单击下一步。​

13.

在个人信息收集声明对话框，选择否，并单击发布。​

步骤三：在低代码智能体内使用插件​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击新建项目。​

​

3.

在项目开发页面，选择创建智能体或者进入指定智能体。​

4.

在智能体编排页面，找到插件区域，并单击右侧的 + 图标。​

5.

在添加插件页面，单击团队工具，并选择添加 search_stock_prices 工具。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27555%27%20height=%27308%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTU1IiBoZWlnaHQ9IjMwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在智能体的人设与回复逻辑中，设置调用插件的规则。​

7.

在智能体的预览与调试中，测试智能体功能。​

  * 如下图所示，智能体调用查询股票价格插件的 search_stock_prices 工具处理用户咨询的 AAPL 股票价格。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27340%27%20height=%27455%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzQwIiBoZWlnaHQ9IjQ1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

上一篇

雅思陪练

下一篇

AI 教学场景的成员与资源管理