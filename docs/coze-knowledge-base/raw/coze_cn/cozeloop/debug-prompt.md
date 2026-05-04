---
source_url: https://docs.coze.cn/cozeloop/debug-prompt
title: '调试提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:01Z
---

# 调试提示词 - 文档 - 扣子

调试提示词

扣子罗盘提供两种调试模式：普通模式和自由对比模式，默认为普通模式。在以下场景中，推荐进入自由对比模式进行 Prompt 调试：​

  * 当需要快速对比同一 Prompt 在不同模型上的表现差异时​

  * 当需要快速对比不同 Prompt 在同一模型上的表现差异时​

普通调试​

你可以在 Prompt 开发页面的预览与调试区域，直接输入一个指令，然后单击运行；或者在 Prompt 变量中输入指令信息，然后直接单击运行。​

方式一：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272418%27%20height=%271111.5924170616113%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3f89c34ee22d43899beb6ede33f55436~tplv-goo7wpa0wc-quality:q75.image)​

​

方式二：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272456%27%20height=%271111.6018957345973%27/%3e)![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c6cd5e4094714fb69b49fa9f18fe8525~tplv-goo7wpa0wc-quality:q75.image)​

​

​

因为开启了单步调试模式，所以可以在调试过程中，手动修改函数的模拟返回值。这里，我们将上海的天气改为Rainy。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27291%27%20height=%27212%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d53a77b7e4ea438d95495eff5828a922~tplv-goo7wpa0wc-quality:q75.image)​

​

以下是模型的回复内容，我们可以看到模型有关注到天气对出行的影响，并给了带雨具的建议，是符合预期的。​

以下内容由 AI 生成，仅供参考。​

​

Markdown

复制

好的，以下是我为你提供的一份周日在上海的游玩计划：​

上午：​

- 早餐：去生煎店品尝特色小吃生煎包，或者逛逛周边的特色早餐店。​

- 游览上海博物馆：这是一座大型的中国古代艺术博物馆，收藏了大量的珍贵文物和艺术品，可以感受历史文化的魅力。​

- 前往南京路步行街：在这里可以逛街购物、感受上海的繁华，并品尝各种美食。​

...​

请注意，由于天气原因，在游玩过程中请携带雨具，并根据实际情况调整行程。希望你在上海度过一个愉快的周日！​

​

设置运行模式​

普通调试时，可以在调试区域设置运行模式。默认为单次运行。​

​

运行模式​| 说明​| 示例​  
---|---|---  
单次运行​| 针对指定 User Prompt，模型仅执行一次，并输出一条回复。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272464%27%20height=%271154.3937007874015%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ2NCIgaGVpZ2h0PSIxMTU0LjM5MzcwMDc4NzQwMTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​  
多次运行​| 针对指定 User Prompt，模型同时执行 n 次，并横向并排展示每一次的运行结果，以便有效测试模型回复的稳定性。每个运行结果均记录 Trace，你也可以通过观测功能查看每一次请求的调用链。​多次运行模式可设置运行组数，即模型运行的次数，默认 2 组，最多可设置为 10 组。​多次运行模式下，无法发送新消息，你可以采纳更好的一条回复，继续进行调试。​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27876%27%20height=%27424.2047244094488%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODc2IiBoZWlnaHQ9IjQyNC4yMDQ3MjQ0MDk0NDg4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

自由对比模式​

自由对比模式适用于需要比较不同模型或系统提示词的表现的场景。​

参考以下步骤，开启自由对比调试：​

1.

在 Prompt 开发页面，单击进入自由对比模式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27415%27%20height=%27235%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDE1IiBoZWlnaHQ9IjIzNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

根据需要调整对照组的配置。​

  * 例如保持其他配置不变的情况下，使用不同的模型，查看不同模型的表现。​

  * 系统默认添加一个与基准组配置相同的对照组，可单击 \+ 增加对照组复制基准组配置来添加更多的对照组。​

  * 说明

    * 在需要调整 Prompt 或模型配置以进行对比时，建议对基准组进行调整。这样可以避免在切换到自由对比模式后，无法保存调整后的配置。​

    * 最多可添加 3 个对照组。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27483%27%20height=%27272%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgzIiBoZWlnaHQ9IjI3MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 选择右侧的同步勾选框，你可以将草稿部分的编辑内容（包含 Prompt 模版、变量信息、函数信息等）一键同步至对照组。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27422%27%20height=%27263%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIyIiBoZWlnaHQ9IjI2MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在预览与调试区域，输入一个指令，然后单击运行。​

4.

查看三个对照组的输出结果进行比较。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27621%27%20height=%27350%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjIxIiBoZWlnaHQ9IjM1MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

编写提示词

下一篇

智能优化提示词