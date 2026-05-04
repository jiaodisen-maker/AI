---
source_url: https://docs.coze.cn/coze_pro/resource_expansion_fee
title: '资源扩容费用 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:59:19Z
---

# 资源扩容费用 - 文档 - 扣子

资源扩容费用

扣子为部分付费资源提供扩容服务，支持同一时间叠加购买，你可以按需提升资源使用上限以应对高并发需求。购买扩容服务后，将根据扩容并发数和时长产生额外的费用。​

注意事项​

进行资源扩容时，请先阅读如下注意事项。​

  * 仅支持企业旗舰版、原企业版的超级管理员或管理员购买扩容服务。​

  * 仅企业旗舰版、原企业版支持使用三方付费插件并进行扩容操作。​

  * 主账号及其所有子账号共享并发数。​

  * 语音识别的扩容并发数仅适用于流式语音识别的相关调用，不包括录音文件识别的相关调用。​

  * 智能绘图_文生图插件的并发扩容费用为每个并发数每小时 20800 积分。建议你在扩容操作前，仔细评估实际需求，谨慎操作。​

支持扩容的资源​

目前，扣子支持如下付费资源的并发限制扩容。​

​

功能模块​| 扩容计费项​| 资源说明​| 默认并发数​| 每次可扩容的最大并发数​  
---|---|---|---|---  
插件​| 并发扩容-智能绘图（扣子官方插件）​| [智能绘图_文生图插件](<https://docs.coze.cn/guides/gen_image_pay_plugin>)支持扩容并发数。​| 7​| 5​  
​| XXX 插件（三方付费插件）​| 针对已开通且支持扩容的三方付费插件，企业超级管理员或管理员可以申请扩容并发数。提交申请后，由插件开发者进行审批。​| 由插件开发者定义​| 由插件开发者定义​  
语音​| 并发扩容-大模型-语音转文字​| 使用大模型进行流式语音识别时，支持扩容并发数。​

  * 相关的 API、插件及工作流节点调用会共用并发数。​

  * 对应的语音计费项为大模型流式语音识别时长，详情请参考​音视频费用。​

| 10​| 10​  
​| 并发扩容-小模型-语音转文字​| 使用小模型进行流式语音识别时，支持扩容并发数。​

  * 相关的 API、插件及工作流节点调用会共用并发数。​

  * 对应的语音计费项为小模型流式语音识别时长 ，详情请参考​音视频费用。​

| 10​| 10​  
​| 并发扩容-大模型-系统音色文字转语音​| 使用大模型 1.0 系统音色进行语音合成时，支持扩容并发数。​

  * 相关的 API、插件及工作流节点调用会共用并发数。​

  * 对应的语音计费项为系统音色文字转语音字数，详情请参考​音视频费用。​

| 10​| 10​  
​| 并发扩容-大模型-复刻音色文字转语音​| 使用大模型复刻音色进行语音合成时，支持扩容并发数。​

  * 相关的 API、插件及工作流节点调用会共用并发数。​

  * 对应的语音计费项为复刻音色文字转语音字数，详情请参考​音视频费用。​

| 10​| 10​  
​| 并发扩容-豆包语音合成2.0-系统音色文字转语音​| 使用大模型 2.0 系统音色进行语音合成时，支持扩容并发数。​

  * 相关的 API 调用会共用并发数。​

  * 对应的语音计费项为豆包语音合成2.0-系统音色文字转语音字数，详情请参考​音视频费用。​

| 10​| 10​  
​| 并发扩容-小模型-文字转语音​| 使用小模型系统音色进行语音合成时，支持扩容并发数。​

  * 相关的 API、插件及工作流节点调用会共用并发数。​

  * 对应的语音计费项为小模型合成次数，详情请参考​音视频费用。​

| 10​| 10​  
API​| 限时免费​| 如下对话相关的 API 支持扩容 QPS。​

  * [发起对话](<https://docs.coze.cn/developer_guides/chat_v3>)​

  * [查看对话详情](<https://docs.coze.cn/developer_guides/retrieve_chat>)​

  * [查看对话消息详情](<https://docs.coze.cn/developer_guides/list_chat_messages>)​

| 500​| 500​  
​| ​| 如下工作流相关的 API 支持扩容 QPS。​

  * [执行工作流](<https://docs.coze.cn/developer_guides/workflow_run>) ​

  * [执行工作流（流式响应）](<https://docs.coze.cn/developer_guides/workflow_stream_run>) ​

  * [执行对话流](<https://docs.coze.cn/developer_guides/workflow_chat>) ​

  * [查询工作流异步执行结果](<https://docs.coze.cn/developer_guides/workflow_history>) ​

  * [查询输出节点的执行结果](<https://docs.coze.cn/developer_guides/get_node_execute_history_response>) ​

| 500​| 500​  
​| ​| 如下插件相关的 API 支持扩容 QPS。​

  * [调用插件工具](<https://docs.coze.cn/developer_guides/call_plugin_tool>)​

  * [查询插件详情](<https://docs.coze.cn/developer_guides/get_plugin>)​

| 100​| 100​  
  
​

单价​

扩容服务计费项的价格如下表所示：​

​

功能模块​| 计费项​| 单价​| ​  
---|---|---|---  
​| ​| 积分结算（积分/并发/小时）​| 现金结算（元/并发/小时）​  
插件​| 并发扩容-智能绘图（扣子官方插件）​| 20,800​| 20.8​  
​| XXX 插件（三方付费插件）​| 不支持积分抵扣​| 由插件开发者定义​  
语音​| 并发扩容-大模型-语音转文字​| 140​| 0.14​  
​| 并发扩容-大模型-系统音色文字转语音​| 140​| 0.14​  
​| 并发扩容-大模型-复刻音色文字转语音​| 140​| 0.14​  
​| 并发扩容-豆包语音合成2.0-系统音色文字转语音​| 140​| 0.14​  
​| 并发扩容-小模型-语音转文字​| 140​| 0.14​  
​| 并发扩容-小模型-文字转语音​| 140​| 0.14​  
API​| 限时免费​| ​| ​  
  
​

计算公式​

扩容服务的计费公式如下：​

扩容费用 = 扩容的并发数 ✖️ 使用小时（整点） ✖️ 单价​

说明

扩容服务以每个自然小时（如 15:00～16:00）为计费单位，不足 1 小时按 1 小时计算。例如 15:12～16:12 期间生效的扩容服务，那么将按照两小时计算。​

​

例如你购买了智能绘图_文生图插件的扩容服务，指定扩容 4 个并发，生效时间为 10:00~20:00，那么这 10 小时的插件扩容费用为 4 个 ✖️ 10 小时 ✖️ 20,800 积分/人/小时 = 832,000 积分。​

相关操作​

购买扩容服务​

1.

企业超级管理员或管理员登录[扣子编程](<https://code.coze.cn/home>)。​

2.

在页面左下角，单击积分卡片，然后单击扩容管理。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27495%27%20height=%27300%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk1IiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在扩容管理页面，找到需扩容的资源，单击扩容。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27499%27%20height=%27118%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDk5IiBoZWlnaHQ9IjExOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

设置并发数及生效时间，然后单击开通。​

  * 说明

如果界面上提示扩容额度超额，表示并发数已达到总上限值。​

​

  * 并发：新增的并发数。​

  * 生效时间：资源扩容生效时间。​

取消扩容服务​

你可以在扩容管理页面，找到已扩容的资源，单击扩容生效中或扩容待生效，找到需要取消的扩容服务，单击取消扩容。​

注意

  * 取消后，已生效的时间区间正常计费（按自然小时），未生效的时间区间不计费。​

  * 例如扩容服务的生效期间为 15:12～16:12，将按照两小时计费。如果你在 15:20 取消扩容服务，那么将收取 15:00～16:00 期间的费用，16:00～17:00 期间不再计费。​

  * 取消扩容服务，将下调对应的并发数，可能会对线上服务造成影响。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27570%27%20height=%27219%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcwIiBoZWlnaHQ9IjIxOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看扩容记录​

你可以在扩容管理页面，找到已扩容的资源，单击扩容生效中、扩容已过期或扩容待生效等字样，查看已购买的扩容服务，包括已过期的、生效中的、待生效的、已取消的。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27505%27%20height=%27199%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA1IiBoZWlnaHQ9IjE5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

查看扩容审核状态​

针对三方付费插件，提交扩容申请后，需等待插件开发者审核通过，才能完成扩容。你可以在扩容记录中查看审核状态。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27570%27%20height=%27113%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTcwIiBoZWlnaHQ9IjExMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

上一篇

知识库空间费用

下一篇

席位费用（已下架）