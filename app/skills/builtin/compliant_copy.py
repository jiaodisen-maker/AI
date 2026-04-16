"""合规文案生成 Skill — 第一个核心 Skill.

保健品行业文案生成，三层合规校验：
1. 禁词库（正则匹配 300+ 违规词）
2. 规则引擎（结构化合规规则）
3. LLM 审核（模型二次校验）

支持多平台适配：小红书、抖音、公众号、京东详情页。
"""

from __future__ import annotations

import re
from typing import Any

from app.llm.models import ChatMessage, ChatRequest, Role
from app.llm.router import ModelRouter
from app.skills.base import BaseSkill
from app.skills.models import (
    ModelPreference,
    SkillCategory,
    SkillInput,
    SkillMeta,
    SkillOutput,
)

# ============================================================
# 保健品广告法禁词库
# 优先从本体 YAML 加载，fallback 到硬编码列表
# ============================================================
_FALLBACK_PROHIBITED_WORDS: list[str] = [
    "最好", "最佳", "最优", "第一", "唯一",
    "治疗", "治愈", "根治", "疗效", "消炎",
    "特效", "立竿见影", "纯天然", "无副作用",
]


def _load_prohibited_words() -> list[str]:
    """Load prohibited words from ontology YAML, fallback to hardcoded."""
    try:
        from app.ontology.loader import OntologyLoader
        loader = OntologyLoader()
        loader.load_all()
        data = loader.get("prohibited_words")
        if data:
            words = []
            for category in [
                "absolute_terms", "disease_treatment", "efficacy_guarantee",
                "false_claims", "authority_misleading", "urgency_inducing",
            ]:
                words.extend(data.get(category, []))
            if words:
                return words
    except Exception:
        pass
    return _FALLBACK_PROHIBITED_WORDS


def _load_safe_replacements() -> dict[str, str]:
    """Load safe word replacements from ontology YAML."""
    try:
        from app.ontology.loader import OntologyLoader
        loader = OntologyLoader()
        loader.load_all()
        data = loader.get("prohibited_words")
        if data and "safe_replacements" in data:
            return data["safe_replacements"]
    except Exception:
        pass
    return {
        "最好": "优质", "治疗": "调理", "特效": "优质",
        "纯天然": "天然来源", "无副作用": "温和配方",
    }


PROHIBITED_WORDS: list[str] = _load_prohibited_words()

# Compile regex patterns for efficient matching
PROHIBITED_PATTERNS: list[re.Pattern] = [
    re.compile(re.escape(word)) for word in PROHIBITED_WORDS
]

# ============================================================
# 合规规则引擎
# ============================================================
COMPLIANCE_RULES: list[dict[str, str]] = [
    {
        "id": "R001",
        "rule": "保健食品广告不得含有表示功效、安全性的断言或保证",
        "check": "不能出现'保证''肯定''一定'等断言性表述",
    },
    {
        "id": "R002",
        "rule": "不得含有利用代言人作推荐、证明的内容",
        "check": "不能出现'XX明星推荐''专家推荐''医生建议'等代言表述",
    },
    {
        "id": "R003",
        "rule": "保健食品广告应当显著标明'本品不能代替药物'",
        "check": "输出必须包含合规声明提示",
    },
    {
        "id": "R004",
        "rule": "不得涉及疾病预防、治疗功能",
        "check": "不能暗示产品可以预防或治疗任何疾病",
    },
    {
        "id": "R005",
        "rule": "功效宣称不得超出注册/备案的保健功能范围",
        "check": "功效描述需在允许范围内",
    },
]

# ============================================================
# 平台风格指南
# ============================================================
PLATFORM_STYLES: dict[str, str] = {
    "xiaohongshu": """小红书风格要求：
- 标题用吸引人的口语化表达，可用 emoji
- 分享体验而非硬广，用第一人称
- 加入使用场景和真实感受
- 字数 300-500 字
- 结尾加话题标签 3-5 个""",
    "douyin": """抖音短视频脚本风格：
- 开头 3 秒抓住注意力（提问/痛点/反转）
- 口语化、节奏感强
- 字数 150-300 字
- 强调视觉画面描述
- 结尾引导互动（点赞/评论/关注）""",
    "wechat": """公众号文章风格：
- 标题引发好奇或共鸣
- 开头讲故事或场景带入
- 分段清晰，小标题引导
- 字数 800-1500 字
- 专业但不生硬，有温度""",
    "jd": """京东详情页风格：
- 产品核心卖点前置（3 个以内）
- 成分/原料特色说明
- 适用人群明确
- 使用方法/规格/参数清晰
- 品质背书（生产资质/检测报告）""",
}

# ============================================================
# 生成 Prompt
# ============================================================
COPYWRITING_SYSTEM_PROMPT = """\
你是一个专业的保健品文案专家。你需要为保健品生成合规、有吸引力的文案。

严格遵守以下规则：
1. 绝不使用违反《广告法》的禁用词
2. 不得暗示疾病治疗、预防功能
3. 功效描述需温和、客观，使用"有助于""辅助"等措辞
4. 不得使用绝对化用语
5. 不得虚假宣传

{platform_style}

{experience_prompt}

在文案末尾添加提示：[温馨提示：保健食品不是药物，不能代替药物治疗疾病]"""

COMPLIANCE_REVIEW_PROMPT = """你是保健品广告合规审核专家。请审核以下文案的合规性。

审核标准：
1. 是否含有禁用词或绝对化用语
2. 是否暗示疾病治疗、预防功能
3. 是否有虚假宣传内容
4. 是否缺少必要的合规声明
5. 功效宣称是否过度

待审核文案：
{copy_text}

以 JSON 格式返回：
{{"passed": true/false, "issues": ["问题1", "问题2"], "suggestions": ["建议1"]}}"""


class CompliantCopySkill(BaseSkill):
    """保健品合规文案生成技能。

    三层合规保障：
    1. 生成时：prompt 约束 + 经验注入
    2. 生成后：禁词库正则扫描 + 规则引擎检查
    3. 终审：LLM 二次合规审核
    """

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="compliant-copy",
            name="合规文案生成",
            description="为保健品生成符合广告法的营销文案，支持小红书/抖音/公众号/京东等多平台",
            category=SkillCategory.CONTENT,
            version="1.0.0",
            author="AI中台",
            triggers=[
                "写文案", "生成文案", "合规文案", "写一篇", "帮我写",
                "小红书文案", "抖音文案", "公众号文案", "京东详情",
                "产品文案", "营销文案", "种草文案",
            ],
            parameters={
                "type": "object",
                "properties": {
                    "product_name": {"type": "string", "description": "产品名称"},
                    "platform": {
                        "type": "string",
                        "enum": ["xiaohongshu", "douyin", "wechat", "jd"],
                        "description": "目标平台",
                    },
                    "key_ingredients": {"type": "string", "description": "核心成分"},
                    "target_audience": {"type": "string", "description": "目标人群"},
                    "tone": {"type": "string", "description": "文案风格/调性"},
                },
            },
            # Creative writing benefits from stronger models
            model_preference=ModelPreference.OVERSEAS,
        )

    def validate(self, skill_input: SkillInput) -> str | None:
        if not skill_input.user_message.strip():
            return "请描述您需要生成的文案内容"
        return None

    def ontology_needs(self) -> list[str]:
        """This skill needs product domain knowledge and compliance rules."""
        return ["health_supplements"]

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        """Generate compliant copywriting."""
        # Determine platform
        platform = self._detect_platform(skill_input)
        platform_style = PLATFORM_STYLES.get(platform, "")

        # Get experience prompt
        experience_prompt = skill_input.context.get("experience_prompt", "")

        # Build generation prompt
        system_prompt = COPYWRITING_SYSTEM_PROMPT.format(
            platform_style=platform_style,
            experience_prompt=experience_prompt,
        )

        request = ChatRequest(
            messages=[
                ChatMessage(role=Role.SYSTEM, content=system_prompt),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference=self.meta().model_preference.value,
            temperature=0.8,
            max_tokens=2048,
            skill_id=self.meta().id,
        )

        response = await self.model_router.chat(request)

        return SkillOutput(
            success=True,
            content=response.content,
            metadata={
                "platform": platform,
                "model_used": response.model_used,
                "tokens": response.input_tokens + response.output_tokens,
            },
        )

    async def post_execute(self, skill_input: SkillInput, output: SkillOutput) -> SkillOutput:
        """Post-processing: run 3-layer compliance check."""
        if not output.success:
            return output

        # P0 修复：保存原始文案，Layer 3 审核必须看原始版本
        original_content = output.content

        # Layer 1: Prohibited word scan
        violations = self._check_prohibited_words(output.content)
        if violations:
            # Auto-fix: replace prohibited words with safe alternatives
            fixed_content = self._auto_fix_prohibited(output.content, violations)
            output.content = fixed_content
            output.metadata["compliance_fixes"] = violations

        # Layer 2: Rule engine check
        rule_issues = self._check_rules(output.content)
        if rule_issues:
            output.metadata["rule_warnings"] = rule_issues

        # Layer 3: LLM compliance review — 审核原始文案，不是修复后的版本
        review = await self._llm_compliance_review(original_content)
        output.metadata["compliance_review"] = review

        # 如果 LLM 审核不通过，标记输出
        if not review.get("passed", False):
            output.metadata["compliance_warning"] = "LLM 合规审核未通过，建议人工复核"

        return output

    def _detect_platform(self, skill_input: SkillInput) -> str:
        """Detect target platform from user message or parameters."""
        platform = skill_input.parameters.get("platform", "")
        if platform:
            return platform

        message = skill_input.user_message.lower()
        if "小红书" in message:
            return "xiaohongshu"
        elif "抖音" in message:
            return "douyin"
        elif "公众号" in message or "微信" in message:
            return "wechat"
        elif "京东" in message or "详情页" in message:
            return "jd"

        return "xiaohongshu"  # default

    def _check_prohibited_words(self, text: str) -> list[str]:
        """Layer 1: Scan for prohibited words."""
        found = []
        for word, pattern in zip(PROHIBITED_WORDS, PROHIBITED_PATTERNS):
            if pattern.search(text):
                found.append(word)
        return found

    def _auto_fix_prohibited(self, text: str, violations: list[str]) -> str:
        """Attempt to replace prohibited words with safe alternatives."""
        safe_replacements = _load_safe_replacements()

        for word in violations:
            replacement = safe_replacements.get(word, "***")
            text = text.replace(word, replacement)

        return text

    def _check_rules(self, text: str) -> list[dict[str, str]]:
        """Layer 2: Check structural compliance rules."""
        issues = []

        # R001: Check for absolute assertions
        assertion_words = ["保证", "肯定", "一定", "必定", "绝对"]
        for word in assertion_words:
            if word in text:
                issues.append({
                    "rule_id": "R001",
                    "issue": f"发现断言性表述：'{word}'",
                })

        # R002: Check for endorsement claims
        endorsement_words = ["明星推荐", "专家推荐", "医生建议", "名人代言"]
        for word in endorsement_words:
            if word in text:
                issues.append({
                    "rule_id": "R002",
                    "issue": f"发现代言表述：'{word}'",
                })

        # R003: Check for compliance disclaimer
        if "保健食品不是药物" not in text and "不能代替药物" not in text:
            issues.append({
                "rule_id": "R003",
                "issue": "缺少合规声明：'保健食品不是药物，不能代替药物治疗疾病'",
            })

        return issues

    async def _llm_compliance_review(self, text: str) -> dict[str, Any]:
        """Layer 3: LLM-based compliance review."""
        import json

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=COMPLIANCE_REVIEW_PROMPT.format(copy_text=text[:2000]),
                ),
            ],
            model_preference="local",  # Review uses local model for speed
            temperature=0.1,
            max_tokens=512,
        )

        try:
            response = await self.model_router.chat(request)
            content = response.content.strip()
            if content.startswith("```"):
                content = content.split("\n", 1)[-1]
            if content.endswith("```"):
                content = content.rsplit("```", 1)[0]
            return json.loads(content.strip())
        except Exception as e:
            # P0 修复：合规审核失败时必须返回不通过，不能默认放行
            return {
                "passed": False,
                "issues": [f"合规审核系统异常，请人工复核: {e}"],
                "suggestions": [],
            }
