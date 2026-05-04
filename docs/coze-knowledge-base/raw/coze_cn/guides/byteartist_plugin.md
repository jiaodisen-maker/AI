---
source_url: https://docs.coze.cn/guides/byteartist_plugin
title: 'ByteArtist 插件 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:40:35Z
---

# ByteArtist 插件 - 文档 - 扣子

ByteArtist 插件

[ByteArtist 插件](<https://www.coze.cn/store/plugin/7328315861222031410>)用于根据文本描述生成图像，支持指定图像数量和大小。​

ByteArtist 插件包含 text2image 工具、image2image 工具、ImageToolPro 工具。不同工具的配置项不同，生成结果也不同。​

使用限制​

扣子主账号内所有子账号共享 ByteArtist 插件的并发限制 ，其值为 4。​

计费说明​

ByteArtist 插件根据插件调用次数计费，对应的计费项及单价请参考​插件费用。​

说明

ByteArtist 插件内包含多个工具，调用这些工具的次数将共同计入该插件的免费额度。​

​

text2image 工具​

text2image 工具支持通过提示词生成图片，一次只能生成一张图片。​

配置说明​

使用 text2image 工具时，你需要输入提示词。同时，你也可以根据业务需求，指定图片风格、尺寸、宽高比例等参数，以满足个性化的图像生成需求。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
prompt​| 设置用于生成图片的提示词，必填参数。​  
ddm_steps​| 设置用于生成图像的步数。值越大，生成的图片越精细，但花费时间也越长。​

  * 取值范围：[1-50]。​

  * 默认值：20。​

  
height​| 设置待生成图片的高度。​

  * 卡通风格​

  * 取值范围：[128,768]。​

  * 默认值：512。​

  * 动漫风格​

  * 取值范围：[576,1728]。​

  * 默认值：1088。​

  * 说明动漫风格的宽*高不可以超过 1088*1088 个像素点。​​

  
model_type​| 设置待生成图片的风格。​

  * 0（默认值）：通用风格。​

  * 1：动漫风格。​

  
negative_prompt​| 设置负面提示词，用于排除不希望生成的图像效果或元素。默认为 worst quality, low quality, normal quality, nsfw, glitch, deformed, mutated, disfigured, bad hands, signature, watermark, text, error, jpeg artifacts, blurry, overexposed, high-contrast, bad-contrast, pattern, duplicate, bad hand, missing fingers。​  
ratio​| 设置待生成图像的宽高比例。​

  * 1（默认值）：1:1​

  * 2：4:3​

  * 3：16:9​

  * 4：3:4​

  * 5：9:16​

  
scale​| 设置文本描述对生成图像的影响程度。​

  * 取值范围：[1, 30]。​

  * 默认值：7。​

  
seed​| 设置随机种子，输入 -1 或正整数。​

  * -1（默认值）：系统将随机生成图片，每次生成结果不同。​

  * 任意正整数：系统将基于该种子值生成相似的图片，确保结果可复现。​

  
width​| 设置待生成图片的宽度。​

  * 卡通风格​

  * 取值范围：[128,768]。​

  * 默认值：512。​

  * 动漫风格​

  * 取值范围：[576,1728]。​

  * 默认值：1088。​

  * 说明动漫风格的宽*高不可以超过 1088*1088 个像素点。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
log_id​| 日志 ID。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
code​| 错误码。​  
data.images.image_url​| 图片生成后的图片 URL。URL 有效期为 30 天，请及时转存。​  
  
​

示例​

调用 text2image 工具生成一张女孩图片。其中，设置提示词为一个中国年轻女孩,白色背景,黑色头发,长波​

波头,正面脸,特写,工作室灯光,工作室,侧光,化妆肖像,穿白色衣服。图片生成后，你可以通过输出结果中的图片链接查看图片。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27750%27%20height=%27675.6505576208178%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUwIiBoZWlnaHQ9IjY3NS42NTA1NTc2MjA4MTc4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

效果图如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

image2image 工具​

image2image 工具支持根据你所提供的原始图片和提示词生成新的图片，一次只能生成一张图片。​

配置说明​

在使用 image2image 工具时，你需要上传原始图片及输入提示词。同时，你也可以根据业务需求，指定原图的修改强度、负面提示词等参数，以满足个性化的图像生成需求。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
prompt​| 设置用于生成图像的提示词，必填参数。​  
url​| 设置原始图片来源，必填参数。​支持输入图片链接或引用上游节点的输出参数。​说明在调试节点效果时，建议输入一个图片链接，用于调整参数配置，并仅测试该节点，快速查看效果。​  
ddm_steps​| 设置用于生成图像的步数。值越大，生成的图片越精细，但花费时间也越长。​

  * 取值范围：[1-50]。​

  * 默认值：20。​

  
model_type​| 设置模型版本名称。目前仅支持设置为 1，表示使用 anime_v1.3 模型。​  
negative_prompt​| 设置负面提示词，用于排除不希望生成的图像效果或元素。默认为"worst quality, low quality, normal quality, nsfw, glitch, deformed, mutated, disfigured, bad hands, signature, watermark, text, error, jpeg artifacts, blurry, overexposed, high-contrast, bad-contrast, pattern, duplicate, bad hand, missing fingers"。​  
scale​| 设置文本描述对生成图像的影响程度。值越大，影响程度越大。​

  * 取值范围：[1, 30]。​

  * 默认值：7。​

  
seed​| 设置随机种子，输入 -1 或正整数。​

  * -1（默认值）：系统将随机生成图片，每次生成结果不同。​

  * 任意正整数：系统将基于该种子值生成相似的图片，确保结果可复现。​

  
strength​| 设置对原图的修改强度。值越大，生成的图片与原图差别越大。​

  * 取值范围：[0.0, 1.0]。​

  * 默认值：0.7。​

  
  
​

输出参数​

​

参数​| 说明​  
---|---  
log_id​| 日志 ID。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
code​| 错误码。​  
data.images.image_url​| 图片生成后的图片 URL。URL 有效期为 30 天，请及时转存。​  
  
​

ImageToolPro 工具​

text2image 工具支持通过提示词生成多种风格的图片。​

配置说明​

在使用 image2image 工具时，你需要输入提示词和图片风格。​

输入参数​

输入参数说明如下表所示：​

​

参数​| 说明​  
---|---  
prompt​| 设置用于生成图片的提示词。必填参数。​  
model_type​| 设置待生成图片的风格。必填参数。​

  * 0：通用风格。​

  * 1：卡通风格。​

  * 2：根据用户输入的图片生成。​

  * 3：像素贴纸风格。​

  
image_url​| 设置原始图片来源。支持输入图片链接或引用上游节点的输出参数。​说明

  * 设置 model_type 为 2 时，必须设置图片链接。​

  * 在调试节点效果时，建议输入一个图片链接，用于调整参数配置，并仅测试该节点，快速查看效果。

​  
  
​

输出参数​

​

参数​| 说明​  
---|---  
log_id​| 日志 ID。​  
msg​| 执行插件时的状态描述或错误提示信息。​  
code​| 错误码。​  
data.prompt​| 生成图片的提示词。​  
data.image_url​| 图片生成后的图片 URL。URL 有效期为 30 天，请及时转存。​  
  
​

示例​

调用 ImageToolPro 工具生成一张小狗图片。其中，设置 prompt 为两只黄色的小狗，设置 model_type 为 1，即卡通风格。图片生成后，你可以通过输出结果中的图片链接查看图片。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27750%27%20height=%27457.14285714285717%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUwIiBoZWlnaHQ9IjQ1Ny4xNDI4NTcxNDI4NTcxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

效果图如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

* ByteArtist插件 ID：7348853341922983946​

上一篇

图像调整插件

下一篇

背景替换插件