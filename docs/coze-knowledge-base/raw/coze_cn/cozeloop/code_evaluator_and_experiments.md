---
source_url: https://docs.coze.cn/cozeloop/code_evaluator_and_experiments
title: '通过 Code 评估器评测 Agent - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:56:49Z
---

# 通过 Code 评估器评测 Agent - 文档 - 扣子

通过 Code 评估器评测 Agent

本文通过两个示例演示如何通过 Code 评估器和实验评测智能体输出正确性。​

示例1 评估专利分类助手​

场景说明​

在专利整理过程中，你设计了一个专利分类助手智能体，用于实现基于专利内容的摘要信息，对专利进行分类。本场景将通过构建 Code 评估器和实验，验证该智能体输出分类结果的正确性。​

准备工作​

  * 已创建专利分类助手的扣子智能体，详细步骤参考​搭建一个低代码智能体，智能体的提示词如下：​

  * ​

Plain Text

复制

请你基于专利内容的摘要信息，对该专利进行单一类别划分（类别无先后优先级，核心判断依据为摘要内容与哪类描述的匹配度最高），具体任务要求如下：​

一、任务目标​

根据专利摘要的核心技术内容，从下方给定的 7 个分类中，选择 1 个最符合的类别作为该专利的最终分类。​

二、分类体系及优先级规则​

1\. 分类详细描述​

交互控制：内容涉及虚拟对象 / 虚拟角色的控制、虚拟道具的控制、游戏玩法机制、游戏社交、界面操作、技能释放和玩法等，与 “玩家如何控制游戏中内容” 直接相关的技术。​

界面显示：核心内容是 “游戏内容、信息如何在界面上显示”，且摘要中通常会明确提及 “显示方法”；（优先级规则：若核心内容同时涉及 “交互控制”，则优先分类为 “交互控制”）。​

客户端：核心内容是 “在客户端处理且用户不可见的技术”，包括渲染、下载与更新、客户端之间的通信及其他客户端专属技术；（优先级规则：若内容同时涉及 “交互控制、界面显示、直播 & 回放”，则优先划分到前述三类，不归类为 “客户端”）。​

直播 & 回放：内容涉及游戏直播、游戏高光剪辑、游戏录屏、游戏回放相关的技术。​

音频：内容涉及游戏音频（如音频生成、音频适配、音频交互等）相关的技术。​

服务端：内容涉及 AI、机器学习、服务器部署、服务端通信、战队匹配、角色寻路、帧同步等服务端专属技术。​

其他：内容属于游戏领域，但无法匹配上述 6 个分类的技术，包括但不限于游戏安全、游戏测试、游戏数据统计（非服务端核心功能）等。​

2\. 关键优先级总结​

当 “界面显示” 与 “交互控制” 重叠时，归为交互控制；​

当 “客户端” 与 “交互控制 / 界面显示 / 直播 & 回放” 重叠时，归为前述三类，不归为客户端；​

所有分类优先以 “摘要核心内容” 为判断基准，不纠结次要提及的技术点。​

三、操作流程​

完整阅读目标专利的摘要信息，提取其中核心技术主题（即专利最想保护的技术方向）；​

将核心技术主题与上述 7 个分类的描述逐一比对，初步筛选可能匹配的类别；​

若存在多类别重叠，严格按照 “优先级规则” 排除低优先级类别；​

最终确定 1 个最符合的分类。​

四、输入输出示例​

输入（专利摘要片段）：“本发明公开了一种虚拟角色技能释放的控制方法，玩家可通过滑动界面按钮触发技能，并根据滑动轨迹调整技能释放范围，同时在界面上显示技能冷却时间。”​

输出（分类）： “交互控制”​

​

  * 已准备评测集，具体步骤请参见​构建评测集。​

步骤一 创建 Code 评估器​

在本场景中，你需要通过 Code 评估器对专利分类助手 Agent 输出类别的正确性进行评估。​

1.

创建 Code 评估器。​

a.

访问[扣子罗盘](<https://loop.coze.cn>)，并在左侧导航栏顶部，选择目标空间。​

b.

在左侧导航栏选择评测 > 评估器。在右上角单击新建评估器 > Code 评估器。​

c.

选择文本等值判断模板，单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27310.0578034682081%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjMxMC4wNTc4MDM0NjgyMDgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

填写评估器的名称，在右侧测试数据下拉列表中选择基于评测集，单击构造测试数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27380.80924855491327%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM4MC44MDkyNDg1NTQ5MTMyNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在评测集页面选择准备工作中已创建的评测集。选择一条或多条测试数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27325.4335260115607%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMyNS40MzM1MjYwMTE1NjA3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

在评测对象页面选择评测类型为 Coze 智能体，选择准备工作中已创建的智能体，单击下一步：生成模拟输出。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27303.81471389645776%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwMy44MTQ3MTM4OTY0NTc3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在生成模拟数据页面单击导入数据。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27282.4267782426778%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI4Mi40MjY3NzgyNDI2Nzc4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 说明

评估器中导入测试数据时，评估器不会自动生成 actual_output 的值，如需验证评估器试运行的准确性，你需要手工修改对应的值。​

​

6.

在测试数据区域展开某条测试数据，修改 actual_output 字段为测试数据对应的实际输出值，以便验证评估器试运行的准确性，单击试运行。试运行成功后单击创建。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27391.90751445086704%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM5MS45MDc1MTQ0NTA4NjcwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二 实验评估​

通过创建实验，验证构建好的 Code评估器的评估效果。​

新建实验​

1.

在[扣子罗盘](<https://loop.coze.cn>)左侧导航栏选择评测 > 实验。在右上角单击 \+ 新建实验。​

2.

在基础信息页面输入实验名称和描述，单击下一步: 评测集。​

3.

选择评测集。​

  * 选择准备工作中已创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27304.6242774566474%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwNC42MjQyNzc0NTY2NDc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

配置评测对象。​

  * 本场景中的评测对象可以设置为 Prompt 或智能体，本文以评测对象类型为 Coze 智能体为例。​

  * 选择准备工作中已创建的智能体，在字段映射中，将评测对象 input 映射到评测集 input 字段，单击下一步：评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27334.68208092485554%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMzNC42ODIwODA5MjQ4NTU1NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

设置评估器。​

  * 单击添加评估器，选择​步骤一 创建 Code 评估器中已创建的评估器和版本，单击确认实验配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27363.0057803468208%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM2My4wMDU3ODAzNDY4MjA4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

6.

单击发起实验。​

查看实验结果​

1.

在评测 > 实验页面单击实验名称，在实验数据明细中查看实验得分，1 表示完全匹配，0 表示完全不匹配。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27161.27167630057804%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjE2MS4yNzE2NzYzMDA1NzgwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

将鼠标悬停在某条数据明细上，单击查看评估器 Trace 图标，查看评估器的 Trace 链路，结合 Trace 查看评估器执行过程中的详细日志。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%2767.96116504854369%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjY3Ljk2MTE2NTA0ODU0MzY5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27322.3300970873787%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMyMi4zMzAwOTcwODczNzg3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

示例2 评估邮编查询助手​

场景说明​

智能体的功能为根据完整地址信息输出对应地区的精准邮编（以标准 JSON 格式返回），本场景将通过 Code 评估器和实验验证该智能体输出的格式规范性、邮编字段有效性及结果准确性。​

准备工作​

  * 已创建邮编查询助手的扣子智能体，详细步骤参考​搭建一个低代码智能体，智能体的提示词如下：​

  * ​

Plain Text

复制

请你扮演“中国大陆完整地址-邮编精准匹配分析师”，基于截至2024年的中国大陆最新权威邮编数据库，对我提供的**完整地址信息**（已包含“省/自治区/直辖市+市+区/县+街道/乡镇+门牌号”）执行解析，最终以**标准JSON格式**输出唯一精准邮编。具体执行规则与格式要求如下：​

​

## 一、核心执行规则​

1\. **地址预处理**：若地址含行政区域简称（如“京”→“北京市”、“粤”→“广东省”、“沪”→“上海市”），自动转换为标准全称（无需额外说明转换过程，仅在结果中体现规范地址）。​

2\. **邮编匹配要求**：基于完整地址定位至具体门牌号对应的行政区域，匹配唯一6位数字邮编，杜绝多邮编推荐（因地址已满足精准解析条件）。​

3\. **特殊情况处理**：若地址对应区域存在2024年行政区划调整记录（可能影响邮编），需在JSON的“notes”字段补充说明，同时仍输出数据库匹配的精准邮编。​

​

## 二、输出格式限制​

{​

"standard_address": "【转换后的完整标准地址，例：北京市朝阳区建国路88号】",​

"postcode": "【6位数字邮编，例：100022】",​

"notes": "【基础说明+特殊情况补充，例：地址信息完整，邮编基于2024年最新数据库；该区域2023年曾调整街道划分，建议通过中国邮政官网核实】"​

}​

\- 字段不可缺失、不可新增，“postcode”需为字符串类型（避免前导零丢失，如“030002”）。​

\- “notes”基础说明固定包含“地址信息完整，邮编基于2024年最新数据库”，无特殊情况时仅保留此句；有特殊情况时补充说明即可。​

​

请提供需解析的完整中国大陆地址，我将严格按上述规则与格式输出JSON结果。​

​

  * 已准备评测集，具体步骤请参见​构建评测集。​

步骤一 创建 Code 评估器​

在本场景中，你需要从三个维度评估验证邮编查询助手的输出是否符合要求：​

  * 验证输出是否符合标准 JSON 格式。​

  * 通过正则匹配验证邮编字段是否符合 6 位数字的特定格式要求。​

  * 验证输出邮编值与预期结果是否一致。​

因此，你需要创建 3 个 Code 评估器分别对应上述评估维度。​

1 创建 JSON 格式校验评估器​

创建 JSON 格式校验评估器，验证 Agent 输出格式是否符合标准 JSON 格式。​

1.

访问[扣子罗盘](<https://loop.coze.cn>)，并在左侧导航栏顶部，选择目标空间。​

2.

在左侧导航栏选择评测 > 评估器。在右上角单击新建评估器 > Code 评估器。​

3.

选择 JSON格式校验模板，单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27308.09248554913296%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwOC4wOTI0ODU1NDkxMzI5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

填写评估器的名称，其他参数保持默认配置，单击创建。​

2 创建文本正则匹配评估器​

创建文本正则匹配评估器，验证输出邮编字段是否符合 6 位数字的特定格式要求。​

1.

在评估器页面右上角单击新建评估器 > Code 评估器。选择文本正则匹配模板，单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27309.02777777777777%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwOS4wMjc3Nzc3Nzc3Nzc3NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

修改执行函数中的正则匹配表达式。​

  * 国内邮编的格式为 6 位数字字符串，正则匹配表达式为 ^[0-9]{6}$，你需要将执行函数中的代码替换为如下示例代码，使其符合当前 Agent 的输出格式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27409.24855491329475%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQwOS4yNDg1NTQ5MTMyOTQ3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

  * 替换后的示例代码如下：​

  * ​

Python

复制

import re​

​

def exec_evaluation(turn):​

try:​

# 获取actual_postcode​

actual_text = turn["evaluate_target_output_fields"]["actual_output"]["text"]​

actual_text = json.loads(actual_text)​

actual_postcode = actual_text["postcode"]​

# 检查actual_postcode是否匹配正则表达式​

regex_pattern = "^[0-9]{6}$"​

regex_match = bool(re.search(regex_pattern, actual_postcode))​

score = 1.0 if regex_match else 0.0​

reason = f"actual_postcode{'匹配' if regex_match else '不匹配'}正则表达式。actual_postcode: '{actual_postcode}', 正则表达式: '{regex_pattern}'"​

​

return EvalOutput(score=score, reason=reason)​

​

except re.error as e:​

raise Exception(f"正则表达式错误: {e}")​

except KeyError as e:​

raise Exception(f"字段路径未找到: {e}")​

except Exception as e:​

raise Exception(f"评估失败: {e}")​

​

3.

填写评估器的名称，单击试运行或创建。​

  * 如需试运行验证评估器的效果，你可以在测试数据区域修改 actual_output.text 字段的值。以下是 actual_output.text 示例：​

  * ​

JSON

复制

"{ \"standard_address\": \"上海市杨浦区国权北路1370号\", \"postcode\": \"200438\", \"notes\": \"地址信息完整，邮编基于2024年最新数据库\" }"​

​

3 创建文本等值判断评估器​

创建文本等值判断评估器，验证输出邮编值与预期结果是否一致。​

1.

在评估器页面右上角单击新建评估器 > Code 评估器。选择文本等值判断模板，单击确定。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27310.0578034682081%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjMxMC4wNTc4MDM0NjgyMDgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

2.

修改执行函数中的代码。​

  * 你需要将执行函数中的代码替换为如下示例代码，使其符合当前 Agent 的输出格式。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27414.1040462427746%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQxNC4xMDQwNDYyNDI3NzQ2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * 替换后的示例代码如下：​

  * ​

Python

复制

def exec_evaluation(turn):​

try:​

# 获取actual_postcode和reference_text​

actual_text = turn["evaluate_target_output_fields"]["actual_output"]["text"]​

actual_text = json.loads(actual_text)​

actual_postcode = actual_text["postcode"]​

reference_text = turn["evaluate_dataset_fields"]["reference_output"]["text"]​

​

# 比较文本相似性或相等性​

is_equal = actual_postcode.strip() == reference_text.strip()​

score = 1.0 if is_equal else 0.0​

reason = f"actual_postcode与reference_output{'匹配' if is_equal else '不匹配'}。actual_postcode: '{actual_postcode}', reference_postcode: '{reference_text}'"​

​

return EvalOutput(score=score, reason=reason)​

​

except KeyError as e:​

raise Exception(f"字段路径未找到: {e}")​

except Exception as e:​

raise Exception(f"评估失败: {e}")​

​

3.

填写评估器的名称，单击试运行或创建。​

  * 如需试运行验证评估器的效果，你可以在测试数据区域修改 actual_output.text 字段的值。以下是 actual_output.text 示例：​

  * ​

JSON

复制

"{ \"standard_address\": \"上海市杨浦区国权北路1370号\", \"postcode\": \"200438\", \"notes\": \"地址信息完整，邮编基于2024年最新数据库\" }"​

​

步骤二 实验评估​

通过创建实验，验证构建好的 Code评估器的评估效果。​

新建实验​

1.

在[扣子罗盘](<https://loop.coze.cn>)左侧导航栏选择评测 > 实验。在右上角单击 \+ 新建实验。​

2.

在基础信息页面输入实验名称和描述，单击下一步: 评测集。​

3.

选择评测集。​

  * 选择准备工作中已创建的评测集，并选择要使用的评测集版本，然后单击下一步：评测对象。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27304.6242774566474%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwNC42MjQyNzc0NTY2NDc0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

配置评测对象。​

  * 本场景中的评测对象可以设置为 Prompt 或智能体，本文以评测对象类型为 Coze 智能体为例。​

  * 选择准备工作中已创建的智能体，在字段映射中，将评测对象 input 映射到评测集 input 字段，单击下一步：评估器。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27309.74477958236656%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMwOS43NDQ3Nzk1ODIzNjY1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

设置评估器。​

  * 单击添加评估器，添加已创建的 3 个评估器，并选择对应版本，单击确认实验配置。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27364.84918793503476%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjM2NC44NDkxODc5MzUwMzQ3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

6.

单击发起实验。​

查看实验结果​

1.

在评测 > 实验页面单击实验名称，在实验数据明细中查看实验得分，1 表示完全匹配，0 表示完全不匹配。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27164.393063583815%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjE2NC4zOTMwNjM1ODM4MTUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

2.

将鼠标悬停在某条数据明细上，单击查看评估器 Trace 图标，查看评估器的 Trace 链路，结合 Trace 查看评估器执行过程中的详细日志。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%2770.28901734104046%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjcwLjI4OTAxNzM0MTA0MDQ2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27209.9421965317919%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIwOS45NDIxOTY1MzE3OTE5IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

上一篇

基于 Trace 自动评测 Agent

下一篇

评测多模态（图片） Agent