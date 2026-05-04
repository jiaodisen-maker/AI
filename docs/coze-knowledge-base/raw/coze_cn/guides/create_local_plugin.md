---
source_url: https://docs.coze.cn/guides/create_local_plugin
title: '创建端插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:03Z
---

# 创建端插件 - 文档 - 扣子

创建端插件

通过端插件，低代码智能体能够直接与硬件设备进行交互，实现对硬件设备的控制和信息获取。本文介绍创建端插件的步骤，你可以通过页面创建端插件、或通过 JSON 和 YAML 导入插件。​

场景描述​

以“控制电脑完成简单任务”为例，端插件需要实现以下两个功能：​

  * 获取电脑电量：通过截图和图片理解技术，获取当前电脑的电量状态。​

  * 总结文件内容：读取本地目录中的文件，并提取其主要内容。​

为了实现这些功能，需要创建三个端插件：​

  * 截图工具：该工具没有参数，其功能是直接对电脑屏幕进行全屏截图，并将截图结果作为返回值。​

  * 列出目录下文件工具：该工具的参数是具体的目录地址，其功能是列出指定目录下的所有文件，并将文件列表作为返回值。​

  * 读取文件内容工具：该工具的参数是具体的文件路径，其功能是读取指定文件的内容，并将文件内容作为返回值。​

本文以该场景为例，介绍具体的创建步骤。​

实现原理​

本场景中，三个端插件的实现原理如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27557.4074074074074%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e97349e444f84f2db00d8859f994063a~tplv-goo7wpa0wc-quality:q75.image)​

​

方式一：通过页面创建插件​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，选择 +资源 > 插件。​

4.

填写插件基础信息，插件工具创建方式选择端侧插件，单击确认。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27480.9815950920245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ4MC45ODE1OTUwOTIwMjQ1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

5.

创建工具。​

a.

在本场景中，你需要创建三个工具，分别是截图、列出目录下文件、读取文件内容，具体如下图所示。​

  * 截图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27435.76158940397346%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQzNS43NjE1ODk0MDM5NzM0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

列出目录下文件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27432%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

读取文件内容​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27434.9090909090909%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQzNC45MDkwOTA5MDkwOTA5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

b.

配置工具的输入参数、输出参数。在本场景中，三个工具的参数分别如下：​

  * ​

工具名称 ​|  工具说明 ​|  输入参数 ​|  输出参数 ​  
---|---|---|---  
截图 ​|  直接对电脑屏幕进行全屏截图 ​|  无 ​|  图片 ​  
列出目录下文件 ​|  列出指定目录下的所有文件 ​|  目录地址（字符串）​|  文件列表（数组）​  
读取文件内容​|  读取指定文件的内容并返回 ​|  文件路径（字符串）​|  文件内容（字符串）​  
  
​

  * 截图​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27286.15384615384613%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI4Ni4xNTM4NDYxNTM4NDYxMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

列出目录下文件​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27312.3076923076923%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMxMi4zMDc2OTIzMDc2OTIzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

读取文件内容​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27298.46153846153845%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI5OC40NjE1Mzg0NjE1Mzg0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

6.

单击右上角的发布，发布端插件。​

方式二：通过 JSON 和 YAML 导入插件​

当需要快速部署多个插件，或插件中工具的参数较多且较为复杂时，通过 JSON 和 YAML 文件导入插件的方式更为高效和灵活。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在资源库页面右上角，选择 +资源 > 插件。​

4.

在新建插件页面，单击右上角的命令图标，分别输入JSON 格式和 YAML 格式的命令脚本。​

  * 本场景的 JSON 和 YAML 的完整示例代码请参见 [plugin.json](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/local_plugin/plugin.json>) 和 [plugin.yaml](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/local_plugin/plugin.yaml>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27478.40735068912716%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQ3OC40MDczNTA2ODkxMjcxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27277.08333333333337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjI3Ny4wODMzMzMzMzMzMzMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​

  * 说明

    * plugin.json：以 JSON 格式定义插件的基本信息，包括插件的名称、描述。​

    * plugin.yaml：以 YAML 格式定义插件的配置信息，包括插件中所有工具的名称、描述、函数信息，以及工具的输入参数和输出参数。​

​

5.

检查插件中的参数等相关配置符合预期后，确认无误后，单击右上角的发布，发布端插件。​

​

​

上一篇

端插件概述

下一篇

通过 API 使用端插件