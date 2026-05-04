---
source_url: https://docs.coze.cn/developer_guides/web_sdk
title: '（历史版本）Chat SDK - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:25:08Z
---

# （历史版本）Chat SDK - 文档 - 扣子

（历史版本）Chat SDK

扣子 Chat SDK是一个 JavaScript 库，您可以使用它将智能体集成到您的 Web 应用程序中。集成后，用户可从网页与智能体对话。 ​

注意

1.0.0-beta.4 版本之前的 Chat SDK 为历史版本，开发者无需鉴权即可集成 SDK。历史版本 Chat SDK 仅提供基础的对话能力，安全性及扩展性较低，后续将不再维护和更新。推荐你使用最新版本的 Chat SDK ​安装并使用 Chat SDK，体验更安全、更友好的智能对话服务。​

​

前提条件​

已经在扣子平台创建了智能体。 ​

安装 SDK ​

按照以下步骤通过将 JavaScript 库添加到您的 Web 应用程序来安装 SDK。 ​

1.

登录[扣子](<https://www.coze.com/>)平台。 ​

2.

查找要部署为 Web 服务的目标智能体。 ​

3.

在编排页面，复制并保存当前页面 URL 的最后一个字符串。​

  * 这个是智能体id，将在以后的配置中使用。​

4.

点击发布。 ​

5.

在发布页面，选择 Chat SDK 选择并单击发布。​

  * 发布 SDK 后才能在新的发布页面选择安装 SDK。​

6.

回到智能体的编排页面，再次点击发布，进入发布页面。​

7.

在发布页面，点击安装。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27808%27%20height=%27147%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/610af1078b9549199dbd04aa40ac949e~tplv-goo7wpa0wc-quality:q75.image)​

​

  * 页面将展示智能体的安装代码。直接将代码粘贴到网页的 <body> 区域中即可。你也可以按需添加各种属性配置，支持属性可参考​初始化 SDK 。​

  * 说明

{{version}} 部分为 Chat SDK 的版本号，例如 0.1.0-beta.5。​

​

  * 安装代码示例如下：​

  * ​

HTML

复制

<script src="https://lf-cdn.coze.cn/obj/unpkg/flow-platform/chat-app-sdk/{{version}}/libs/cn/index.js"></script>​

<script>​

new CozeWebSDK.WebChatClient({​

config: {​

bot_id: '738176858****',​

},​

componentProps: {​

title: 'Coze',​

},​

});​

</script>​

​

初始化 SDK ​

安装 Chat SDK 后，您现在可以初始化智能体客户端。将以下代码添加到您要初始化智能体客户端的页面中。 ​

​

HTML

复制

<script>​

new CozeWebSDK.WebChatClient(options);​

</script>​

​

options 参数包含 config 和 componentProps 两个属性，详细说明可参见下表。 ​

​

属性​| 参数​| 是否必选​| 数据类型​| 描述​  
---|---|---|---|---  
config ​| bot_id ​| 必选​| string ​| 智能体ID。 ​进入智能体的 开发页面，开发页面 URL 中 bot 参数后的数字就是智能体ID。例如https://www.coze.cn/space/341****/bot/73428668*****，智能体ID 为73428668*****。​说明确保该智能体已经发布为 Chat SDK。 ​​  
componentProps ​| title ​| 可选​| string ​| 智能体名字，如果没有配置，使用默认名：扣子 Bot。 ​  
​| icon ​| 可选​| string ​| 智能体的显示图标，如果不设置，则使用默认扣子图标。 ​  
​| lang ​| 可选​| string ​​| 智能体的系统语言，例如智能体的工具提示。 ​

  * en：（默认）英语 ​

  * zh-CN：中文 ​

​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271014%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAxNCIgaGVpZ2h0PSIyMzgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
​| layout ​​| 可选​| string​| 智能体窗口的布局风格，支持设置为：​

  * mobile：移动端风格。​

  * pc：PC 端风格。​

未设置此参数时，系统会自动识别设备，设置相应的布局风格。​  
​| width​| 可选​| number​| PC 端智能体窗口的宽度，单位为 px，默认为 460。​建议综合考虑各种尺寸的屏幕，设置一个合适的宽度。​仅在 layout = pc 时生效。​  
  
​

销毁 SDK 客户端 ​

您可以添加一个 destroy 方法销毁智能体客户端。 ​

​

HTML

复制

<script>​

const client = new CozeWebSDK.WebChatClient(options);​

client.destroy();​

</script>​

​

解绑智能体​

如果你不需要智能体继续以 web 服务方式使用，在发布页面，点击解绑按钮。 ​

说明

一旦解绑，智能体就无法通过集成的 Web 应用程序使用。 如果您想恢复 Web 应用程序的访问，需要再次将智能体发布为 Chat SDK。 ​

​

示例​

以下是一段完整的 Chat SDK 的代码示例。 ​

​

HTML

复制

<!doctype html>​

<html lang="en">​

<head>​

<style>​

/* 自定义悬浮入口的位置 */​

#position_demo {​

position: absolute;​

right: 10px;​

bottom: 20px;​

}​

</style>​

</head>​

<body>​

<h1>Hello Bot</h1>​

<div id="position_demo"></div>​

//{{version}} 为 Chat SDK 的版本号，例如 0.1.0-beta.5。你可以在发布页面的安装代码中查看最新版本的version ​

<script src="https://lf-cdn.coze.cn/obj/unpkg/flow-platform/chat-app-sdk/{{version}}/libs/cn/index.js"></script>​

<script>​

const bot_id = '7330182852614******';​

// 自定义智能体名称和icon​

const title = 'AI翻译助手';​

const icon = 'https://lf-bot-studio-plugin-resource.coze.cn/obj/bot-studio-platform-plugin-tos/artist/image/7e813aa2c7e14ebb9e2d1a989acfb128.png';​

const lang = 'zh-CN';​

const layout = 'pc';​

const width = 800;​

​

new CozeWebSDK.WebChatClient({​

config: {​

bot_id,​

},​

componentProps: {​

title,​

icon,​

width,​

},​

el: document.getElementById('position_demo'),​

});​

</script>​

</body>​

</html>​

​

在本地创建一个HTML文件，将上述代码复制进文件后，本地运行的效果如下所示。 ​

说明

注意将 bot_id 替换为已经发布为 Chat SDK 的智能体的 ID，{{version}} 替换为发布页面安装代码中的版本号。​

​

其中： ​

  * 图标 1 是 icon 参数值。 ​

  * 图标 2 是 title 参数值。 ​

  * 图标 3 是 lang 参数控制的语言配置。 ​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27290%27%20height=%27408%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjQwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271816%27%20height=%271364.1516587677727%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgxNiIgaGVpZ2h0PSIxMzY0LjE1MTY1ODc2Nzc3MjciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

​

​

​

​

​

​

​

上一篇

Chat SDK 发布历史

下一篇

Chat SDK 常见问题