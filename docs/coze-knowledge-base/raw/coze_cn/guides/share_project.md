---
source_url: https://docs.coze.cn/guides/share_project
title: '分享编程项目 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:31:41Z
---

# 分享编程项目 - 文档 - 扣子

分享编程项目

创建 AI 编程项目之后，你可以将你的项目分享给他人，以便共享项目进展、吸引更多用户。目前支持将你的项目开发页面分享给其他扣子用户，或者将你已部署的成品分享给最终用户或集成方，满足团队协作与对外发布的不同场景需求。​

分享完整项目​

该场景主要面向其他扣子开发者，用于共享 AI 编程项目的开发编辑页面，方便你和其他开发者共享项目进展、搭建方式、代码成果。分享完整项目时，你可以设置分享时长，超期后自动关闭分享。​

被分享者打开 AI 编程项目的分享链接后，将进入项目的只读页面，可进行以下操作：​

  * 查看项目详情与最新状态、对话过程、历史版本​

  * 查看或下载项目代码​

  * 试运行项目​

  * 复制项目（取决于项目所有者的分享配置）​

被分享者无法对项目执行任何编辑类操作，例如：​

  * 与扣子 AI 对话​

  * 修改项目基础设置​

  * 部署项目​

说明

开启分享后，任意获得项目链接的用户，将可能获取到项目开发过程、源码、环境变量等敏感信息。建议谨慎开启项目分享。​

​

分享方式如下：​

1.

在[扣子编程](<https://code.coze.cn/>)的项目管理页面，找到你要分享的 AI 编程项目。​

2.

打开项目，在页面右上角单击分享图标。​

3.

在分享完整项目页签中，单击设为公开可见。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27301%27%20height=%27223%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c476cf1e7a5a4d8199c66173c5527ff9~tplv-goo7wpa0wc-quality:q75.image)​

​

4.

设置分享有效期，支持设置为永久。​

5.

设置是否允许复制，默认不允许。​

  * 说明

开启允许复制后，未包含外部集成的项目可被他人复制。​

​

6.

复制项目链接，并发送给其他扣子用户查看。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27286%27%20height=%27253%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjg2IiBoZWlnaHQ9IjI1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

被分享者看到的项目详情页面大致如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27656%27%20height=%27318%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU2IiBoZWlnaHQ9IjMxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

分享产物​

该场景主要面向 AI 编程项目的最终用户或集成方，用于项目成功部署之后，分享调用方式（例如 API 地址）或页面访问链接。​

分享方式如下：​

​

项目类型​| 分享方式​| 示例​  
---|---|---  
网页应用​| 

1.在[扣子编程](<https://code.coze.cn/>)的项目管理页面，找到你要分享的网页应用。​

2.打开项目，在页面右上角单击分享图标。​

3.在分享产物页签中，复制生产版本 URL。​
说明默认分享最新的生产版本，若需要分享历史版本，可参考​如何查看网页应用的历史部署版本？​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27175%27%20height=%27161%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc1IiBoZWlnaHQ9IjE2MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
智能体​| 

1.在[扣子编程](<https://code.coze.cn/>)的项目管理页面，找到你要分享的智能体项目。​

2.打开项目，在页面右上角单击分享图标。​

3.在分享产物页签中，复制智能体 API 的 curl 调用示例。​
说明curl 调用示例中 API Token 使用占位符 <YOUR_TOKEN> 表示，如果被分享者需要调用 API，应由你提供真实的 API Token。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27460%27%20height=%27516.8727272727273%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDYwIiBoZWlnaHQ9IjUxNi44NzI3MjcyNzI3MjczIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
工作流​| 

1.在[扣子编程](<https://code.coze.cn/>)的项目管理页面，找到你要分享的工作流项目。​

2.打开项目，在页面右上角单击分享图标。​

3.在分享产物页签中，复制工作流 API 的 curl 调用示例。​
说明curl 调用示例中 API Token 使用占位符 <YOUR_TOKEN> 表示，如果被分享者需要调用 API，应由你提供真实的 API Token。​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27872%27%20height=%27703.9418181818181%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODcyIiBoZWlnaHQ9IjcwMy45NDE4MTgxODE4MTgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
  
​

​

上一篇

使用 Git 服务

下一篇

AI 编程常见问题