---
name: memory-write
description: 写入一条记忆，自动路由到 GBrain（长期/语义）或 Hindsight（情景/工作）
trigger:
  - 记一下 / 帮我记 / 备忘
  - save / store / remember
inputs:
  content: 要记的内容（必填）
  hints:
    source: 来源（gmail / feishu / chat / docs / patrol / ...）
    type: 类型（fact / preference / experience / belief / person_profile / ...）
    subject_ref: 关联的实体（可选，例如 brain/people/zhangsan.md）
---

# Skill: memory-write

## 目标
把一条信息写进合适的记忆系统，**绝不直接写底层**，必须经过 MemoryRouter。

## 步骤

1. **判断输入完整性**
   - 没有 `content` → 拒绝，要求补充
   - 没有 `hints` → 走 LLM 兜底分类

2. **调 MCP 工具 `memory_write`**
   ```
   memory_write(
     content="<原文>",
     hints={"source": "feishu_dm", "type": "preference",
            "subject_ref": "brain/people/zhangsan.md"}
   )
   ```

3. **接收返回**
   - 返回 `{"target": "hindsight" | "gbrain" | "both", "id": "...", "path": "..."}`
   - 若 `target = both`，结果会有 `gbrain_path` + `hindsight_id` 两个字段，自动建立双向引用（不用你管）

4. **告诉用户**
   - GBrain：`已记入档案 brain/people/zhangsan.md`
   - Hindsight：`已记入工作记忆（id=m_8273），autoDream 凝固后会同步进档案`
   - both：两个位置都报

## 边界 / 不要做的事

- ❌ 不要绕过 router 直接编辑 brain repo 的 markdown
- ❌ 不要在这里调 `memory_reflect`（凝固是守护进程的活）
- ❌ 检测到 PII / 密钥 → 拒绝写入，提示用户走加密渠道

## 例子

> 用户："记一下，张三不喜欢周一早会"
>
> Skill 调用：
> ```
> memory_write(
>   content="张三不喜欢周一早会",
>   hints={"source":"chat","type":"preference","subject_ref":"brain/people/zhangsan.md"}
> )
> ```
>
> 返回：`{"target":"hindsight","id":"m_8273"}`
>
> 回复用户："已记入工作记忆。如果之后这个偏好被多次印证，会自动凝固进张三的档案。"
