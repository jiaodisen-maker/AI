---
source_url: https://docs.coze.cn/guides/plugin_faq
title: '插件常见问题 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:42:21Z
---

# 插件常见问题 - 文档 - 扣子

插件常见问题

创建 IDE 插件时，如何读写临时文件？​

创建 IDE 插件时，只支持在/tmp目录下读写临时文件，文件最大为 512MB。​

以插件工具file_writer为例，此工具将当前日期和时间写入一个临时文件，然后读取该文件，并返回读取到的内容。创建 IDE 插件的代码示例如下：​

​

Python

复制

from datetime import datetime​

from pathlib import Path​

from runtime import Args​

from typings.file_writer.file_writer import Input, Output​

​

TMP_DIR = "/tmp"​

​

def handler(args: Args[Input])->Output:​

file_path = TMP_DIR + "/data.txt"​

​

# 写入数据 ​

try:​

with open(file_path, "w") as file_writer:​

file_writer.write(str(datetime.now()))​

except Exception as e:​

return {​

"message": "write file error: " \+ str(e),​

}​

​

# 读取数据​

try:​

with open(file_path, "r") as file_writer:​

text = file_writer.read()​

return {​

"message": f"read file content: {text}"​

}​

except Exception as e:​

return {​

"message": "read file error: " \+ str(e),​

}​

​

如下图所示，代码运行后，返回读取到的日期和时间。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272543%27%20height=%271250.8969907407406%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU0MyIgaGVpZ2h0PSIxMjUwLjg5Njk5MDc0MDc0MDYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

通过自定义插件实现音视频转换，图片和视频怎么输出？​

通过自定义插件转换音视频时，如果要输出图片、视频等多模态内容，你需要先将这类文件上传到云存储等文件服务器，获取文件的公开访问 URL，然后再进行输出。​

通过 IDE 创建插件时，是否可以使用 Python 实现并提交 async 函数？​

支持使用 Python 实现并提交 async 函数。​

插件使用 IP 地址，为什么会调试失败？​

建议在配置插件的 URL 或抓取类插件的参数 URL 时，使用域名而非 IP 地址，这样做可以避免请求被服务端的网络安全设置所拦截。​

如何配置插件参数中的默认值？​

参数的默认值可有效避免大模型运行时因插件参数值缺失而导致的报错。同时，针对一些值较为稳定的参数，设置其默认值且隐藏其可见性可减少大模型的无效判断，从而提高插件调用效率。具体配置，请参考​参数配置。​

链接读取插件如何解析多个 URL？​

通过批处理功能，[链接读取插件](<https://www.coze.cn/store/plugin/7329410795979161663>)可以批量解析多个 URL。​

在工作流中，设置开始节点的 input 变量为 Array<String>类型，在 LinkReaderPlugin 插件节点的批处理页签下，设置 item1 变量引用开始节点的 input 变量，并设置 url 变量引用 item1 变量。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271858%27%20height=%27787.0694444444445%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg1OCIgaGVpZ2h0PSI3ODcuMDY5NDQ0NDQ0NDQ0NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

链接读取插件是否支持设置自定义超时时间？​

[链接读取插件](<https://www.coze.cn/store/plugin/7329410795979161663>)不支持设置自定义超时时间。​

为什么链接读取插件无法读取内容，输出 null？​

使用[链接读取插件](<https://www.coze.cn/store/plugin/7329410795979161663>)时，请检查输入的 URL 是否正确。当 URL 中混杂其他非 URL信息时，系统将无法正常解析，输出结果可能为 null。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271727%27%20height=%27669.5912280701754%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcyNyIgaGVpZ2h0PSI2NjkuNTkxMjI4MDcwMTc1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

链接读取插件读取内容的语言不一致，如何处理？​

直接打开页面时为中文内容，通过[链接读取插件](<https://www.coze.cn/store/plugin/7329410795979161663>)读取的内容为英文内容，此时你可以在 URL 中添加 query 参数  lang=zh-CN。​

为什么插件审核不通过提示"插件素材信息（icon、名称、描述）包含违规内容"？​

该提示表示插件提交的基础信息（图标、名称、描述）中存在不符合平台规范的内容。以下是常见原因及解决建议：​

  * 使用系统默认图标​

  * 问题描述：使用系统默认图标，缺乏个性化，不符合平台对插件独特性的要求。​

  * 解决建议：建议您使用个性化的图标，确保图标清晰、独特且符合插件主题，避免使用系统默认图标。​

  * 名称和描述问题​

  * 问题描述：名称或描述中可能包含敏感词、不当内容或营销信息。​

  * 解决建议：​

  * 检查敏感词：仔细检查名称和描述，确保没有使用任何敏感词汇或不当内容。​

  * 避免营销信息：避免在名称和描述中包含明显的营销信息或广告内容，确保内容真实、客观且符合平台规范。​

已有插件新增工具时如何添加调用示例？​

目前，已有插件新增工具时，不支持调用示例功能。​

使用天眼查插件提示额度用尽该如何处理，如何查看已用额度？​

官方插件免费版存在调用限制。使用天眼查等第三方插件时，如果插件提示额度用尽，则需前往其官网购买 API 额度，购买后按文档配置 token 即可。配置说明，请参考[天眼查插件配置文档](<https://open.tianyancha.com/help/question>)。​

如何提高图片理解插件 QPS？​

目前[图片理解插件](<https://www.coze.cn/store/plugin/7328314686280138803?from=add_plugin_menu>)处于免费阶段，暂不支持提高 QPS。如果遇到 702093018、Pro call plugin qps too high 等问题，建议合理控制调用频率，避免批量使用。​

自定义插件都有哪些通用 Header 参数？​

调用自定义插件时，扣子编程会为插件请求统一添加 Header 公共字段，用于传递低代码智能体 ID 等插件调用的相关信息。开发者可以解析自定义插件请求的 Header 字段，提取关键信息用于后续分析，例如通过 X-Aiplugin-Connector-Identifier 字段提取 API 方式调用插件时指定的 user_id。​

​

参数​| 参数类型​| 说明​  
---|---|---  
X-Tt-Logid ​| String ​| 日志 ID，联系扣子技术支持时可提供给技术支持人员，便于排查问题。​  
X-Aiplugin-Connector-Identifier ​| String ​| 用户标识，即 API 方式（​发起对话）调用插件时传参中指定的 user_id。​  
X-AIPlugin-Bot-ID​| String ​| 调用插件的低代码智能体 ID。 ​  
X-AIPlugin-Conversation-ID​| String ​| 对话的 ID。 ​  
Longitude​| String ​| 插件调用方所在的位置经度。 ​  
Latitude ​| String ​| 插件调用方所在的位置纬度。 ​  
X-AIPlugin-ID​| String ​| 插件 ID。​  
X-AIPlugin-Account-ID​| String ​| 用户扣费的火山引擎账号 ID。​  
X-AIplugin-OpenID​| String ​| 基于扣子用户UID x 插件开发者企业账号 ID 生成。​一个扣子用户在工作流中使用一个企业上架的 N 个插件是同一个 OpenID。​  
X-AIPlugin-UID​| String ​| 扣子用户 UID，仅当使用者和插件开发者归属于一个企业时有值。​  
  
​

插件运行报错“插件已被下架（The plugin has been taken offline）”​

如果插件运行报错“插件已被下架（The plugin has been taken offline）”，错误码为 720711011，这是因为该插件已被作者下架，无法继续使用。你需要替换为其他可用的插件，并重新发布低代码智能体、工作流或应用。操作方式如下：​

1.

定位问题插件。​

  * 你可以在空间配置 > 发布管理中，通过消息日志中查看调用链路，找到问题插件的名称、所在的工作流等相关信息。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27352%27%20height=%27190%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUyIiBoZWlnaHQ9IjE5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

参考以下方式替换插件。​

  * ​

低代码智能体更换插件​| 低代码工作流更换插件​| 低代码应用更换插件​  
---|---|---  
在智能体编排页面的插件区域删掉原插件，再重新添加另一个可用插件：​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27633%27%20height=%27456.412017167382%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjMzIiBoZWlnaHQ9IjQ1Ni40MTIwMTcxNjczODIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​| 在工作流编排页面删掉原插件，再重新添加一个插件节点，另外选择一个可用的插件：​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271862%27%20height=%27920.7692307692308%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg2MiIgaGVpZ2h0PSI5MjAuNzY5MjMwNzY5MjMwOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| 在业务流程页面找到工作流，删掉原插件，再重新添加一个插件节点，另外选择一个可用的插件：​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271846%27%20height=%27791.1428571428571%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTg0NiIgaGVpZ2h0PSI3OTEuMTQyODU3MTQyODU3MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​  
  
​

3.

重新发布智能体、工作流或低代码应用。​

上一篇

管理企业插件

下一篇

知识库概述