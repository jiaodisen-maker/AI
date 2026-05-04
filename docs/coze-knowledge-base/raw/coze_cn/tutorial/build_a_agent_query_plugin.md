---
source_url: https://docs.coze.cn/tutorial/build_a_agent_query_plugin
title: '快速搭建智能体列表查询插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:04Z
---

# 快速搭建智能体列表查询插件 - 文档 - 扣子

快速搭建智能体列表查询插件

本文以搭建智能体列表查询插件为例，介绍将 API 服务转化为实用插件的全流程，包括创建插件、添加工具、发布插件等步骤。​

操作视频​

​

​

__

Replay

Play

00:00 / 03:47 Live

00:00

Fullscreen 

Cssfullscreen 

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag 

​

​

背景信息​

在扣子编程中，一个插件可包含多个工具，每个工具用于完成一个指定的动作。在创建插件时，首先需要将这个 API 服务注册为一个插件，然后再将这个服务下的 API 添加到插件中作为工具使用，最后将插件发布上线。​

本教程以扣子编程的[查看智能体列表](<https://www.coze.cn/open/docs/developer_guides/bots_list_draft_published>) API 为例，展示如何一步步创建插件。插件创建成功后，可以通过该插件查看指定空间发布到 Agent as API 渠道的智能体列表。以下是这个接口的基本信息。​

​

API 信息​| 说明​  
---|---  
请求地址​| https://api.coze.cn/v1/bots​  
Header​| 

  * Authorization：用于验证客户端身份的访问令牌，本教程以个人访问令牌为例，取值：Bearer $Access_Token。​

  * Content-Type：解释请求正文的方式，固定值：application/json。​

  
请求参数和返回参数​| 参考[查看智能体列表](<https://www.coze.cn/open/docs/developer_guides/bots_list_draft_published>)。​  
  
​

准备工作​

确保你已经获取了访问令牌，并开通了 listBot 权限，详细信息参考​鉴权方式概述。​

步骤一：创建插件​

参考以下操作将上述接口创建为一个插件。​

1.

登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面顶部选择目标工作空间，然后在左侧导航栏中单击资源库。​

​

3.

在页面右上角，选择+资源 > 插件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27591%27%20height=%27241%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTkxIiBoZWlnaHQ9IjI0MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

填写插件基础信息。​

a.

输入插件名称和描述。​

b.

设置插件工具创建方式为云侧插件-基于已有服务创建。​

c.

设置私网连接为不使用私网连接。​

d.

设置插件 URL为 API 的服务地址。本教程需输入扣子编程的 API 服务地址 https://api.coze.cn。​

e.

将以下 Header 信息配置到 Header 列表中。​

  * Authorization：用于验证客户端身份的访问令牌，本教程以个人访问令牌为例，取值为 Bearer $Access_Token，例如 Bearer pat_UHNEiqY3tuk0bJbxBwTsTR****。​

  * Content-Type：解释请求正文的方式，固定值为application/json。​

f.

设置授权方式为不需要授权。​

g.

单击确认，完成插件创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27266%27%20height=%27528%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY2IiBoZWlnaHQ9IjUyOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：添加工具​

完成插件创建后，就可以将该服务地址下的 API 添加到插件中了。​

1.

在插件详情页面，单击创建工具。​

2.

配置工具名称和描述信息，然后单击确定。​

3.

在编辑工具页面，完成以下操作。​

a.

单击更多信息区域右上角的编辑，配置工具的路径和请求方法，然后单击保存。​

  * 工具路径：工具路径以/开始，本教程需设置为 /v1/bots。​

  * 请求方法：本教程需设置为 Get 方法。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27702%27%20height=%27171%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAyIiBoZWlnaHQ9IjE3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

单击配置输入参数区域右上角的编辑，单击新增参数，添加[查看智能体列表](<https://www.coze.cn/open/docs/developer_guides/bots_list_draft_published>) API 的请求参数，然后单击保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27702%27%20height=%27151%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAyIiBoZWlnaHQ9IjE1MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

c.

单击配置输出参数区域右上角的编辑，单击自动解析，在弹出的页面输入请求参数 workspace_id 的值，再单击自动解析。接口调用成功后，会将返回参数自动填充到输出参数列表，你可以根据需求进行修改，然后单击保存。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27359%27%20height=%27245%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzU5IiBoZWlnaHQ9IjI0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272101%27%20height=%271135.137440758294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEwMSIgaGVpZ2h0PSIxMTM1LjEzNzQ0MDc1ODI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

4.

单击试运行。​

5.

在试运行页面，设置输入参数，然后单击运行测试接口。测试成功后，单击完成。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27466%27%20height=%27337%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY2IiBoZWlnaHQ9IjMzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：发布插件​

当添加的工具调试成功后，你就可以发布插件了。插件只有发布后，才可以被智能体使用。​

1.

在插件页面，单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27626%27%20height=%27161%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjI2IiBoZWlnaHQ9IjE2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

设置版本号和描述，然后选择是否需要收集个人信息，本教程的接口不涉及个人信息收集，选择插件不会收集、传输用户的个人信息，然后单击发布。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27284%27%20height=%27279%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg0IiBoZWlnaHQ9IjI3OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

上一篇

从零搭建企业组织

下一篇

为自定义参数赋值