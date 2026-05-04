---
source_url: https://docs.coze.cn/tutorial/openclaw_functions_in_practice
title: '功能实操 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:50:17Z
---

# 功能实操 - 文档 - 扣子

功能实操

主动干活​

OpenClaw 不止会给你出主意，更能直接动手帮你完成任务。从定时自动执行重复工作、操控浏览器获取信息，到记住你的习惯偏好、用语音高效交互，让 AI 成为你身边随叫随到的「全能助理」，真正解放你的双手与时间。​

定时任务​

什么是定时任务​

OpenClaw 可以按照你指定的时间/周期，自动执行预设好的任务，不需要你每次手动触发。比如定时查消息、定时推菜单、定时发提醒、定时总结待办等等。​

定时任务是如何实现的​

OpenClaw 使用内置的 Cron 调度器，和标准 Linux Cron 语法完全兼容：​

  * 支持三种调度模式：一次性定时（"明天下午3点提醒我"）、固定间隔（"每半小时检查一次消息"）、Cron 表达式（精确到分钟的复杂时间规则）。​

  * 所有定时任务都在独立隔离的会话中运行，不会干扰当前对话。​

  * 任务执行完成后会自动把结果/通知推送给你，不需要手动查询。​

  * 支持任务开关、运行历史查看、出错自动重试等能力。​

如何设置定时任务​

你只需要用自然语言告诉 OpenClaw 你的需求就可以，格式：[时间规则] + [要做的任务]。例如：​

​

喝水提醒​| 检查飞书消息​| 每日工作总结​  
---|---|---  
​Plain Text复制工作日 11 点、15 点、17 点提醒我喝水​​| ​Plain Text复制每小时整点、半点执行，检查所有未读私信和群聊中@我的消息。按🔴紧急 / 🟡关注 / 🟢其他三级分类推送给我​​| ​Plain Text复制每天下午六点，总结你今天完成的工作，并推送给我​​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271500%27%20height=%271120%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwMCIgaGVpZ2h0PSIxMTIwIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27228%27%20height=%27400%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjI4IiBoZWlnaHQ9IjQwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27612%27%20height=%27860%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjEyIiBoZWlnaHQ9Ijg2MCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

浏览器工具​

扣子编程 OpenClaw 配备了 Agent 专用的浏览器，可以帮你完成多种网页相关的操作。例如：​

  * 浏览网页：自动打开任意网页，阅读网页中的文本、表格等内容。​

  * 抓取信息：提取网页中的数据和信息，例如商品规格、新闻内容、搜索结果等。​

  * UI 自动化操作：模拟用户点击按钮、填写表单、提交信息、滚动页面等操作，可用于网页自动化测试等场景。​

  * 截图、导出 PDF 等：支持完整页面截图、指定区域截图、将网页内容导出为 PDF 文件等。​

使用方法：​

无需复杂的指令，用自然语言告诉 OpenClaw 你的需求即可，例如：​

​

访问网页​| 提取Markdown​| 网页截图​  
---|---|---  
​Plain Text复制帮我访问GitHub查看OpenClaw的最新Release版本​​| ​Plain Text复制把这个网页（https://docs.coze.cn/guides/long_memory）的内容完整保存成Markdown格式​​| ​Plain Text复制帮我打开扣子编程的首页，截个图看看​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27264%27%20height=%27315%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY0IiBoZWlnaHQ9IjMxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27310%27%20height=%27317%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEwIiBoZWlnaHQ9IjMxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271402%27%20height=%271388%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQwMiIgaGVpZ2h0PSIxMzg4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

记忆能力​

OpenClaw 的记忆分为短期会话记忆和长期持久记忆两层，所有记忆都存储在你本地的工作区中，不会上传到任何第三方，完全私密安全。重要的信息、规则、偏好会永久存在云端文件里，即使重启、会话结束也不会丢失。​

你可以这样感受到 OpenClaw 的记忆能力：​

  * 定时任务永久生效：你设置的定时会一直按规则执行，无需每次提醒​

  * 偏好自动适配：你表达过的偏好（喜欢的风格、格式、禁忌）等，OpenClaw 会永久记住，每次回复都自动适配。​

  * 帮你回忆对话：你和 OpenClaw 聊过的内容都会记录在短期记忆里，可以随时续上之前中断的话题。​

直接说记住：xxxx，让它主动记录：​

  * 记住：我的常用地址是杭州市余杭区仓前街道xxx​

  * 记住：我喜欢简洁的回复，语气专业但不失俏皮​

​

强调记忆​| 唤起回忆​| 总结对话​  
---|---|---  
​Plain Text复制记住：我的常用地址是杭州市余杭区仓前街道仓南广场​​| ​Plain Text复制还记得我的地址在哪里吗​​| ​Plain Text复制我们今天都聊了啥，总结一下​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27745%27%20height=%27643%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzQ1IiBoZWlnaHQ9IjY0MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27678%27%20height=%27303%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjc4IiBoZWlnaHQ9IjMwMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27731%27%20height=%27727%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzMxIiBoZWlnaHQ9IjcyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​  
  
​

全能工具​

从文档改写、信息检索，到创意文案、日程管理，OpenClaw 内置的实用工具覆盖你日常工作与生活的方方面面。不管是需要快速处理文字、搜集资料，还是辅助内容创作、规划时间，都能通过一次对话搞定。​

文本创作​

支持工作汇报、演讲稿、通知公告、邮件往来、自媒体文案、随笔感悟等多场景文本一键生成。还能按需调整语气风格、篇幅长短与内容侧重点，从初稿搭建到细节优化全程辅助，省去大量构思与撰写时间，高质量内容快速落地，轻松应对各类文字输出任务。​

​

小红书种草文案​| 小学生日记范文​| 深度分析​  
---|---|---  
​Plain Text复制帮我写个小红书种草文案，介绍下我们的新品：扣子牌的薯片。主要卖点和特色是清新的口味、低油低糖的健康配方、时尚的包装设计，适合各个年龄段，尤其是青少年聚会场景。​​| ​Plain Text复制我在辅导小孩写作业，帮我写个小学生日记给他作参考，主题是春天来了。写三篇不同风格的​​| ​Plain Text复制帮我做个 OpenClaw 的深度分析，加上一些你的个人观点​​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271195%27%20height=%27890%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTE5NSIgaGVpZ2h0PSI4OTAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271622%27%20height=%271558%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYyMiIgaGVpZ2h0PSIxNTU4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271496%27%20height=%271584%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ5NiIgaGVpZ2h0PSIxNTg0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
  
​

信息检索​

通过扣子编程 OpenClaw 内置的联网搜索技能，你输入关键词即可快速获取全网核心有效信息，涵盖行业资讯、专业知识、数据资料、热点内容、常识科普等各类信息。同时 OpenClaw 自动梳理信息脉络、提炼核心要点，过滤冗余无效内容，帮你快速锁定关键内容，节省海量搜索与整理时间，精准获取所需资料。​

​

检索热点新闻​| 查询天气​| 事实查证​  
---|---|---  
​Plain Text复制听说香港要禁烟了，查查相关的新闻资讯​​| ​Plain Text复制下周三杭州天气怎么样​​| ​Plain Text复制劳动法规定的年假怎么计算？​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271602%27%20height=%271544%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYwMiIgaGVpZ2h0PSIxNTQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271444%27%20height=%27950%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ0NCIgaGVpZ2h0PSI5NTAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271504%27%20height=%271152%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwNCIgaGVpZ2h0PSIxMTUyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
  
​

语音能力​

扣子编程的 OpenClaw 内置了语音能力，包括基于字节跳动豆包大模型的语音合成（TTS）和语音识别（ASR）能力：​

  * 语音合成（回复你）：OpenClaw 要回复的文本内容会自动通过TTS接口转换成自然流畅的中文语音，直接发送到飞书会话，单击即可播放。​

  * 语音识别（接收你的消息）：向 OpenClaw 发语音消息的时候，它会自动把语音转成文字理解内容，不需要你手动转文字。​

你只需要在提问的时候说明想要语音回复，或者直接说把XX内容用语音读出来，OpenClaw 就会自动把回复内容转换成语音发送给你。例如：​

​

语音讲故事​| 语音播报新闻​| 语音识别​  
---|---|---  
​Plain Text复制用语音给我讲个童话故事​​| ​Plain Text复制制作一个 AI 新闻日报，然后用语音读给我听​​| ​Plain Text复制帮我总结一下 A 项目进展群里的消息​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27754%27%20height=%27601%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzU0IiBoZWlnaHQ9IjYwMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27687%27%20height=%27634%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjg3IiBoZWlnaHQ9IjYzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271428%27%20height=%271184%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQyOCIgaGVpZ2h0PSIxMTg0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
  
​

创意制作​

除了文本内容的生成以外，扣子编程 OpenClaw 还安装了图片制作和视频生成技能，辅助各类创意内容落地。只要你有灵感，无论是营销海报，还是图文排版、广告视频、AI 漫剧、AI 短剧，都能都能提供多元灵感方案零基础也能轻松做出优质创意内容，让创作不再受限，随心打造专属创意作品。​

​

制作手抄报​| 制作节气海报​| 制作商品宣传视频​  
---|---|---  
​Plain Text复制帮我制作一个「清明节」主题的手抄报​​| ​Plain Text复制做一个「谷雨」节气海报​​| ​Plain Text复制做一个1分钟左右的，小狗带逛卢浮宫的视频，9:16比例。从平静地带逛开始，但是在看完蒙娜丽莎之后，卢浮宫现场被黑衣人打劫了。​​  
​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27264%27%20height=%27352%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY0IiBoZWlnaHQ9IjM1MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27254%27%20height=%27339%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU0IiBoZWlnaHQ9IjMzOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​| ​​ __ Replay Play 00:00 / 00:58 Live 00:00 Fullscreen  Cssfullscreen  1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag  ​​  
  
​

多渠道对话​

不用再频繁切换软件，在你最熟悉的飞书、微信等聊天工具里，就能直接召唤 OpenClaw。无论是收发消息、整理会议纪要，还是安排日程、撰写周报，一句话就能让 AI 帮你高效处理，让办公沟通更流畅、更省心。​

此外，所有渠道的数据、记忆是完全同步的，不会因为换了渠道就"失忆"。​

飞书渠道​

飞书渠道是工作场景的首选，支持交互式卡片、文件上传下载、日程/任务/文档等飞书生态深度集成。​

为了能在飞书和你的 OpenClaw 龙虾对话，参考以下步骤完成飞书渠道的配置。​

1.

在[扣子编程](<https://code.coze.cn/home>)中找到你的 OpenClaw 项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27501%27%20height=%27282%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAxIiBoZWlnaHQ9IjI4MiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在页面右上角单击设置图标，打开 OpenClaw 配置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27468%27%20height=%27256%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDY4IiBoZWlnaHQ9IjI1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

（可选）找到飞书渠道，为你的 OpenClaw 龙虾助手设置名称。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27238%27%20height=%27274%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjM4IiBoZWlnaHQ9IjI3NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击授权并创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27257%27%20height=%27291%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjU3IiBoZWlnaHQ9IjI5MSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

根据页面提示完成授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27293%27%20height=%27312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkzIiBoZWlnaHQ9IjMxMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

创建成功，单击去飞书对话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27274%27%20height=%27287%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjc0IiBoZWlnaHQ9IjI4NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

页面会自动跳转到飞书客户端，你可以直接发送消息和你的 OpenClaw 助手对话。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27292%27%20height=%27257%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkyIiBoZWlnaHQ9IjI1NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

微信渠道​

微信是当前热门且普遍使用的 IM 聊天工具，为你的 OpenClaw 配置微信渠道，在微信里和它对话，操作更编辑。​

参考以下步骤完成微信渠道的配置。​

1.

在[扣子编程](<https://code.coze.cn/home>)中找到你的 OpenClaw 项目。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27375%27%20height=%27211%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzc1IiBoZWlnaHQ9IjIxMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

页面右上角单击设置图标，打开 OpenClaw 配置页面。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27409%27%20height=%27224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA5IiBoZWlnaHQ9IjIyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

找到微信渠道，单击去创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27490%27%20height=%27253%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDkwIiBoZWlnaHQ9IjI1MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

打开微信客户端，扫描屏幕显示的二维码。根据微信客户端提示，单击连接。​

5.

后台会自动完成渠道连接，并自动打开一个名为微信 ClawBot 的对话页面。​

  * 输入任意一条消息，测试微信机器人是否能正常回复。 ​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27193%27%20height=%27418%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkzIiBoZWlnaHQ9IjQxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27192%27%20height=%27415%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyIiBoZWlnaHQ9IjQxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

其他渠道​

此外，扣子编程 OpenClaw 还支持绑定钉钉、企业微信等渠道，参考以下使用指南完成配置：​

  * ​OpenClaw 集成钉钉​

  * ​OpenClaw 集成企业微信​

上一篇

OpenClaw 新手入门

下一篇

持续养虾