---
source_url: https://docs.coze.cn/cozeloop/evaluation-quick-start
title: '评测入门教程 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:16Z
---

# 评测入门教程 - 文档 - 扣子

评测入门教程

本教程以一个扣子中搭建的翻译智能体为例，指导你使用扣子罗盘的评测功能来评估智能体的翻译的正确性。​

教程概览​

在本教程中，你将学习使用扣子罗盘的评测功能来评估翻译智能体的表现。该智能体的任务是将用户提供的中文技术内容翻译成英文。​

我们的主要目标是确保翻译的准确性，无事实性错误。要完成这个评测，需要按照以下步骤操作：​

1.

构建评测集：首先，准备用于评测的测试数据。下表是我们将使用的测试数据。​

  * ​

中文​| 参考翻译​| 检测目标​  
---|---|---  
使用docker pull命令从镜像仓库下载最新版本的应用容器。​| Use the docker pull command to download the latest version of the application container from the image registry.​| 术语一致性 + 简洁性​  
当HTTP响应状态码为503时，表示服务暂时不可用。​| An HTTP 503 status code indicates that the service is temporarily unavailable.​| 被动语态 + 句式简化​  
此配置项用于控制缓存过期时间，默认值为300秒。设置过小可能导致频繁缓存穿透，过大则可能引发内存溢出。​| This configuration item controls the cache expiration time. The default value is 300 seconds. A value too low may cause cache penetration, while a value too high may lead to memory overflow.​| 正确性 + 术语准确性​  
警告：修改此参数可能导致系统不稳定，建议先在测试环境验证。​| Warning: Modifying this parameter may cause system instability. Verify changes in a test environment first.​| 正确性 + 简洁性优化​  
该方案通过“削峰填谷”策略优化资源利用率。​| The solution optimizes resource utilization through a "peak shaving and valley filling" strategy.​| 正确性​  
使用Redis的SETNX命令实现分布式锁时，需注意处理锁过期和羊群效应问题。​| When using Redis's SETNX command to implement a distributed lock, it is important to address issues related to lock expiration and the thundering herd problem.​| 术语一致性 + 简洁性​  
  
​

2.

创建评估器：接下来，创建一个包含准确性检测规则的评估器，用于评估翻译智能体的输出结果。​

3.

发起评测实验：将评测数据输入智能体，并使用评估器对智能体的输出结果进行打分。​

4.

分析实验结果：最后，根据实验结果判断智能体的翻译准确性，并进行必要的调整和优化。​

步骤一：创建评测集​

评测集是用于系统化评测 AI Agent 性能的标准化测试数据集。评测集通常包含输入样本与参考输出，作为衡量 AI Agent 表现的基准。评测集是创建评测任务的第一步。​

参考以下步骤，创建评测集。​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，然后单击右上角的立即体验。​

2.

使用扣子账号登录。​

  * 如果你尚未注册扣子账号，参考[账号注册](<https://www.coze.cn/open/docs/guides/sign_up>)注册一个扣子账号并完成登录。​

3.

在左侧导航栏顶部，选择一个空间。​

4.

在左侧导航栏，选择评测 > 评测集，然后单击 \+ 新建评测集。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27585%27%20height=%27217%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg1IiBoZWlnaHQ9IjIxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在新建评测集页面，参考以下信息配置评测集的输入数据列和输出列信息，然后单击创建。​

  * ​

配置项​| 说明​  
---|---  
名称​| 输入一个评测集名称。​  
描述（可选）​| 提供一个评测集描述。​  
配置列-input​| 指定输入样本列配置：​
    * 名称：输入列名称。必须以英文字母开头，支持添加字母、数字和下划线。​
    * 数据类型：选择一种数据类型。通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量。​
    * 查看格式：选择一种渲染评测数据的格式，提高数据的可读性和维护性。​
    * 描述信息：提供描述信息，便于帮助开发者后续理解与维护数据。​  
配置列-reference_output（可选）​| 指定数据集中期望输出列配置：​
    * 名称：输入列名称。必须以英文字母开头，支持添加字母、数字和下划线。​
    * 数据类型：选择一种数据类型。通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。​
    * 查看格式：选择一种渲染评测数据的格式，提高数据的可读性和维护性。​
    * 描述：提供预期输出的补充信息，可作为评估时的参考标准。​
说明预期输出主要作为参考答案提供给评估器评分使用。开发者可根据选择的评估器是否需要该输入，按需选择是否提供该字段。​​  
其他列​| 单击 +添加列补充其他信息，供评测对象与评估器执行评估时消费使用。​评测对象通常需要多个输入字段。例如，当前请求的查询、历史聊天的上下文等。此外，像name这样的字段可能需要维护额外的列，以确保完整的信息记录和分析。​  
  
​

  * 本教程中的评测集的列配置如下图所示。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27562%27%20height=%27425%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYyIiBoZWlnaHQ9IjQyNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

在评测集详情页面，选择添加数据 > 手动添加来添加测试数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27602%27%20height=%27247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAyIiBoZWlnaHQ9IjI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 扣子罗盘评测集支持手动添加和本地导入两种方式来添加数据。本教程中选择手动添加方式。更多关于评测集的操作说明，参考​管理评测集。​

  * 说明

    * 最多可添加 5000 条测试数据。​

    * 本地上传的 CSV 文件仅支持 UTF-8 编码格式。​

​

7.

在添加数据页面，输入第一组测试数据，然后单击 \+ 添加数据项添加更多测试数据。最后，单击添加完成数据添加。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27529%27%20height=%27434%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTI5IiBoZWlnaHQ9IjQzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

8.

添加数据后，单击提交新版本提交评测集。​

  * 说明

在创建评测实验时，只能使用已提交的评测集，不支持使用草稿状态的评测集。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27603%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAzIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：创建评估器​

提交评测集后，接下来要创建一个评估器，设置评估规则。​

参考以下步骤，创建评估器。​

1.

在左侧导航栏，选择评测 > 评估器，然后单击 \+ 新建评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27669%27%20height=%27247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjY5IiBoZWlnaHQ9IjI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在新建评估器页面，参考以下信息配置评估器。​

  * ​

配置​| 说明​  
---|---  
名称​| 输入评估器名称。​  
描述 ​| 提供一个评估器的说明信息。​  
模型选择​| 使用豆包模型。​目前，评估器仅支持豆包模型。​  
Prompt​| 输入评估器的提示词，指示评估器如何进行评估，可以使用内置的评估 Prompt 模板或二次修改模板后使用。​单击选择模板链接，选择正确性模板，最后单击确认。​
    * ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27432%27%20height=%27238%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDMyIiBoZWlnaHQ9IjIzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
\+ 添加 User Prompt​| （可选）单击 + 添加 User Prompt 输入你希望强调的评估规则。​本教程中，在正确性的评估中更关注无错误翻译和漏译这个规则。所以可以输入以下内容：​确保没有错误翻译和漏译。​  
  
​

3.

在完成评估器配置后，单击调试，测试一下评估器效果。​

  * 说明

在调试评估器时，会产生 Token 消耗。​

​

  * 在弹出的预览与调试页面，输入一组测试数据，然后单击运行查看评估效果是否符合预期。​

  * 以下图中的评估器为例，它对构造的output内容评估完全准确。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27658%27%20height=%27290%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU4IiBoZWlnaHQ9IjI5MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

在调试后，单击创建完成评估器创建并提交评估器版本。​

  * 说明

在创建评测实验时，只能使用已提交的评估器。​

​

步骤三：发起实验​

在准备好评测集和评估器后，就可以发起实验来测试翻译助手智能体的翻译准确性了。​

参考以下步骤，发起实验。​

1.

在左侧导航栏，选择评测 > 实验，然后单击 \+ 新建实验。​

2.

输入一个实验名称，然后单击下一步: 评测集。​

3.

选择已创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27591%27%20height=%27334%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTkxIiBoZWlnaHQ9IjMzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

评测对象选择 Coze 智能体，然后选择要评测的智能体和版本，再通过字段映射的方式选择评测集中的哪列数据作为智能体的输入传递给智能体，最后单击下一步：评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27643%27%20height=%27455%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQzIiBoZWlnaHQ9IjQ1NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

选择已创建的评估器和版本，然后将评测集的字段、评测对象的实际输出与评估器的参数关联，确保评估器准确获取数据并执行评估，最后单击确认实验配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27623%27%20height=%27407%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjIzIiBoZWlnaHQ9IjQwNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

检查实验配置，确认无误后，单击发起实验。​

  * 发起实验后，你可以刷新实验页面，查看评估进度。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272374%27%20height=%271265.894259818731%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM3NCIgaGVpZ2h0PSIxMjY1Ljg5NDI1OTgxODczMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤四：分析实验结果​

在评估器执行完所有评估任务后，你可以在实验页面查看实验报告。通过实验报告来判断评估对象是否符合预期。​

查看评测结果​

在实验详情页面，你可以查看评估器对每个测试数据的执行结果的评分，以及评分的具体原因。​

如果某个测试数据的评估器自动打分不准确，你可以将鼠标悬浮至评分上，然后点击出现的人工校准图标。在弹出的页面中输入修正的分数和原因。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272410%27%20height=%271263.5285714285712%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQxMCIgaGVpZ2h0PSIxMjYzLjUyODU3MTQyODU3MTIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

查看实验报告​

在实验详情页面，单击指标统计查看实验数据报告。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272374%27%20height=%271051.3428571428572%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM3NCIgaGVpZ2h0PSIxMDUxLjM0Mjg1NzE0Mjg1NzIiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

至此，我们已经完成了翻译智能体的正确性评估。从实验报告上来看，翻译准确性还是比较高的，没有出现事实性错误。​

​

上一篇

什么是评测

下一篇

管理评测集