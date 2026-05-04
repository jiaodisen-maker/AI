---
source_url: https://docs.coze.cn/tutorial/workflow_random_number
title: '生成随机数 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:40Z
---

# 生成随机数 - 文档 - 扣子

生成随机数

扣子编程低代码工作流中的代码节点通常用于实现一些特定的逻辑或算法，或数据进行特定格式转换或处理，本教程演示如何通过代码节点生成随机数。​

效果示例​

搭建一个生成随机数的低代码工作流，并将其绑定智能体之后，在调试区域发送生成随机数的指令，智能体会自动调用该工作流，并生成一个随机数。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27341%27%20height=%27370%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b790d2f751f24ffa87a0c32ff9b5d61e~tplv-goo7wpa0wc-quality:q75.image)​

​

低代码工作流设计​

本文构建的示例工作流节点概览如下图所示。在该工作流中：​

1.

开始节点接收用户指定随机数长度。​

2.

代码节点根据指定的长度生成随机数。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271358%27%20height=%27326.9259259259259%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8ae4a09c8ea04663a92bb52938fa6875~tplv-goo7wpa0wc-quality:q75.image)​

​

步骤一：构建低代码工作流​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，单击 +资源 > 工作流。​

  * 本文示例配置如下：​

  * 工作流名称：输入 random_number​

  * 工作流描述：输入 生成随机数​

4.

在工作流的编辑页面，从左侧选择节点列表，选用代码节点。​

5.

连接各节点，并依次配置输入输出参数。​

  * 节点连接顺序：开始 → 代码 → 结束，各节点参数配置说明如下表。​

  * ​

节点​| 参数配置​  
---|---  
开始​| 新增输入变量 input_length，并选择 String 数据类型。​  
代码​| 
    * 新增输入变量 length，并在参数值区域选择引用 Start > input_length。​
    * 新增输出变量 random，数据类型选择 String。​
    * 在代码节点打开 IDE，清空默认内容并添加以下代码，该代码用于生成随机数。​
    * ​JavaScript复制async function main({ params }: Args): Promise<Output> {​ var IDX = 36, HEX = ''; ​ while (IDX--) HEX += IDX.toString(36); ​ ​ // @see https://github.com/lukeed/uid/blob/master/src/single.js ​ function uid(len) { ​ var str = '', num = len || 11; ​ while (num--) str += HEX[Math.random() * 36 | 0]; ​ return str; ​ } ​ ​ const ret = { ​ "random": uid(params.length), ​ } ​ return ret ​}​​  
结束​| 新增 output 输入参数，并在参数值区域选择引用 代码 > random。​  
  
​

6.

配置完成后，单击页面右上角的试运行，测试工作流。​

  * 例如，输入 8 进行测试，待所有节点都运行成功（节点会展示绿色边框）后，查看指定节点的运行结果。​

7.

测试工作流无问题后，单击页面右上角的发布。​

  * 成功发布后，在工作流列表中可以查看到该工作流。​

步骤二：在智能体添加工作流并测试​

1.

前往当前工作空间的项目开发页面，创建或进入指定智能体。​

2.

在智能体内，找到技能区域的工作流，在右侧单击加号图标。​

3.

在对话框左侧单击资源库工作流，找到自建的 random_number 工作流，并在右侧单击添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27631%27%20height=%27240%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMxIiBoZWlnaHQ9IjI0MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在智能体的人设与回复逻辑内，声明智能体使用 random_number 工作流处理任务。​

  * 编写后，你可以单击优化，让 AI 帮助你生成结构化的回复逻辑。​

5.

在智能体的右侧预览与调试区域，输入内容预览智能体实现的效果。​

  * 例如输入 生成一个8位随机数。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27330%27%20height=%27358%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzMwIiBoZWlnaHQ9IjM1OCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

解析文件

下一篇

批量生成和处理图片