---
source_url: https://docs.coze.cn/tutorial/llm_response_time
title: '优化大模型响应时间 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:51:06Z
---

# 优化大模型响应时间 - 文档 - 扣子

优化大模型响应时间

本文介绍如何通过压缩方法名、自定义编码、避免嵌套结构以及使用中文数字替代阿拉伯数字等方式，减少输出的 Token 数量，从而有效降低大模型的响应时间。你可以根据实际应用场景选择合适的优化策略，提升大模型的性能和用户体验。​

大模型响应时间计算公式​

大模型响应时间计算公式如下：​

​

Bash

复制

latency = ttft + output_token_num * tpot​

​

其中：​

  * ttft（Time To First Token）：第一个 Token 响应的时间，即模型生成第一个输出 Token 所需的时间。该值主要由大模型的架构和部署环境决定，通常难以直接优化。​

  * output_token_num：大模型输出的 Token 数量。减少输出的 Token 数量可以直接降低响应时间。​

  * tpot（Time Per Output Token）：大模型在首个 Token 输出后，后续输出每个 Token 所需的时间。该值同样取决于大模型的性能和部署环境。​

因此，你可以通过优化大模型输出的 Token 数量，来降低大模型的响应时间。​

优化手段​

​

优化手段​| 详细说明​| 举例​| Token 对比​  
---|---|---|---  
压缩方法名和参数​| 压缩工作流或插件工具的方法名和参数。​| 将工具的方法名 getCountry 压缩为 gc，getWeather 压缩为 gw。​| Token 数量从 3 个减少到 1 个。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2784.29752066115702%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/615719a3161942e6ad87a97f7075b59d~tplv-goo7wpa0wc-quality:q75.image)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2780.57851239669421%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/43ceaf40b136436d973d0a34e34589d0~tplv-goo7wpa0wc-quality:q75.image)​​  
自定义编码​| 将意图识别结果编码为简化的数字或符号。​| 你是一个意图识别专家，如果用户需要联网搜索，返回 1，如果用户需要英语陪聊，返回 2。​| Token 数量从 2 个减少到 1 个。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2789.25619834710744%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9Ijg5LjI1NjE5ODM0NzEwNzQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2790.49586776859503%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjkwLjQ5NTg2Nzc2ODU5NTAzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
不使用 JSON、XML 等嵌套结构​​| 使用自定义的格式来代替 JSON、XML 的嵌套结构，例如使用管道符、CSV 格式等。​​| 将以下 JSON 格式转换为管道符格式：​​JSON复制{​ "func": "getWeather",​ "args": {​ "city": "shenzhen",​ "date": "2024-12-12"​ }​}​​管道符 | 的格式：​​Bash复制getWeather|shenzhen|2024-12-12​​| Token 数量从 48 个减少到 17 个。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27111.57024793388429%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjExMS41NzAyNDc5MzM4ODQyOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2791.73553719008264%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjkxLjczNTUzNzE5MDA4MjY0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
使用中文替代阿拉伯数字​| 使用中文数字替代阿拉伯数字。​| 将 2025-03-20 转换为二五年三月二十日。​| Token 数量从 10 个减少到 5 个。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2789.25619834710744%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9Ijg5LjI1NjE5ODM0NzEwNzQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2790.49586776859503%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjkwLjQ5NTg2Nzc2ODU5NTAzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

说明

你可以通过[方舟 Token 计算器](<https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM={}&OpenTokenDrawer=true&current=1&pageSize=20>)预估输入的内容需要消耗的 Token。​

​

实战案例​

以下是天气参数提取案例的对比情况。通过优化系统提示词，将阿拉伯数字改为中文，并把 JSON 嵌套结构换成管道符格式后，大模型的输出效果、消耗的 Token 数量和响应时间都发生了变化。​

​

类别​| 优化前​| 优化后​  
---|---|---  
系统提示词​| ​Markdown复制# 技能​你是一个信息提取大师，你需要从用户的输入中提取用户的城市，以及要查询的天气的日期。​​# 注意​日期需要结合“当前时间”来输出 end_time 和 start_time，如果只是查询某一天的天气，则 end_time 和 start_time 为同一日期​现在真实时间：2025-03-20​​## 输出​输出 json：​{​ "city": "",​ "start_time": "",​ "end_time": ""​}​​| ​Markdown复制# 技能​你是一个信息提取大师，你需要从用户的输入中提取用户的城市，以及要查询的天气的日期。​​# 注意​日期需要结合“当前时间”来输出 end_time 和 start_time，如果只是查询某一天的天气，则 end_time 和 start_time 为同一日期​现在真实时间：二五年三月二十日​​## 输出​将结果使用 | 按照如下顺序拼接：城市、开始日期、结束日期​### 示例 1 ​输入：深圳天气​输出：深圳|二五年三月二十日|二五年三月二十日​### 示例 2​输入：河南郑州昨天的天气​输出：郑州|二五年三月十九日|二五年三月十九日​​  
大模型的输出​| ​JSON复制{​ "city": "深圳",​ "start_time": "2025-03-20",​ "end_time": "2025-03-20"​}​​| ​Bash复制深圳|二五年三月二十日|二五年三月二十日​​​  
消耗的 Token​| 消耗的 Token 数量为 47。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%27102.39999999999999%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjEwMi4zOTk5OTk5OTk5OTk5OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| 消耗的 Token 数量为 13。​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27300%27%20height=%2785.55758683729432%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9Ijg1LjU1NzU4NjgzNzI5NDMyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
响应时间​| 1,175 ms （按 TPOT 25ms 计算）​| 325 ms（按 TPOT 25ms 计算）​  
  
​

扣子编程大模型节点的配置和运行示例如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27800%27%20height=%27501.6759776536313%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMS42NzU5Nzc2NTM2MzEzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

上一篇

为自定义参数赋值

下一篇

通过飞书进行 SAML SSO 登录