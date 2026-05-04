---
source_url: https://docs.coze.cn/dev_how_to_guides/qeesmmos
title: '通过 API 调用智能体 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:10Z
---

# 通过 API 调用智能体 - 文档 - 扣子

通过 API 调用智能体

将 AI 编程生成的智能体部署为 API 服务后，你可以通过 OpenAPI 方式将智能体的 AI 功能灵活集成到应用中。​

前提条件​

已将 AI 编程生成的智能体部署为 API 服务。具体可参考​部署智能体。​

获取 API 访问信息​

部署成功后，扣子编程会自动生成 API 服务，你可以在部署总览页面获取访问 API 的相关信息。​

查看 API 访问信息​

获取该服务的 API 访问地址、请求Header、请求参数等详细信息。​

1.

在部署的总览页面，单击某条部署记录右侧的更多按钮，选择查看。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27195.37572254335262%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/eef320d3063c4f90a0bd05f32110ba72~tplv-goo7wpa0wc-quality:q75.image)​

​

2.

在API 请求示例及接口说明页面，查看该服务的 API 访问信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27433.52601156069363%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/52d94dd609844ba98b4e7b9a4429f929~tplv-goo7wpa0wc-quality:q75.image)​

​

创建 API Token​

你需要创建 API Token，调用 API 时需要使用 API Token 进行身份验证。你需要将创建的 API Token 包含在请求头的 Authorization 参数中。​

1.

在智能体开发页面，在右侧单击➕打开新的标签页，在弹出的标签页中选择部署。​

2.

在部署的总览页面，单击某条部署记录右侧的更多按钮，选择查看。​

3.

在API 请求示例及接口说明页面，单击管理 API Token，单击创建 API Token 生成新的 API Token。复制并妥善保存 API Token。 ​

  * 说明

    * 生成的令牌仅在此时展示一次，请即刻复制并妥善保存。​

    * 请妥善保存该 API Token，不要在浏览器或其他客户端代码中暴露 API Token。​

    * 每个项目最多能创建 10 个 API Token，API Token 的有效期为永久有效。​

    * 暂时不支持在部署详情页面直接调用和调试 API。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27541.6184971098265%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjU0MS42MTg0OTcxMDk4MjY1IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

（可选）你也可以在 API Token 页面查看已创建的 API Token 列表，删除不再使用的 API Token。​

调用智能体 API​

部署完成后，你可以在你的应用程序或网页中通过 HTTP 请求来调用智能体的 API，以便集成智能体的 AI 能力。​

接口说明​

调用智能体的 API 请求地址的格式为 https://<your_domain>/stream_run，是一个流式响应 API。调用该 API 时，服务端不会一次性发送所有数据，而是以数据流的形式逐条发送数据给客户端，数据流中包含智能体执行过程中触发的各种事件，直至处理完毕或处理中断。​

API 的请求参数由 AI 编程自动生成，具体参数说明可在部署详情页的 API 请求示例及接口说明页面查看。​

说明

AI 编程项目中不兼容低代码 API 文档中的​上传文件等 API 。​

​

调用方法​

1.

复制扣子编程提供的 Curl 请求命令。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27392.60115606936415%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM5Mi42MDExNTYwNjkzNjQxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

将 header 中的 <YOUR_TOKEN> 替换为你在​创建 API Token中获取的 API Token。​

3.

通过 Postman 或相关工具调用对应的 API 。​

  * 以下是某个智能体的 API 请求示例和返回示例。​

  * 请求示例

返回示例

​

JSON

复制

curl --location --request POST "https://m48gym***.coze.site/stream_run" \​

\--header "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwOGU2OTE3LWQwNGYtNDg3Zi1hYjdhLWY0NWIwYWQ4YmM0MCJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbIkgzOVZkS3BwUmVKVXdjMU81VmtraWZkZW9CajZrVlRBIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzY2NTU2NzI4LCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9******" \​

\--header "Content-Type: application/json" \​

\--data '{​

"content": {​

"query": {​

"prompt": [​

{​

"type": "text",​

"content": {​

"text": "今天天气真好，我们去爬山吧"​

}​

}​

]​

}​

},​

"type": "query",​

"project_id": 75872598284063***​

}'​

​

​

上一篇

通过 API 调用工作流