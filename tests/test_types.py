"""测试核心数据类型 - 这些类型必须永久稳定"""
from app.adapters.types import (
    AgentFramework,
    AgentMaturity,
    AgentSpec,
    Message,
    Role,
    Skill,
)


def test_skill_creation():
    skill = Skill(
        name="test-skill",
        description="测试用",
        triggers=["测试", "test"],
    )
    assert skill.name == "test-skill"
    assert "测试" in skill.triggers


def test_agent_spec_creation():
    spec = AgentSpec(
        name="test-agent",
        display_name="测试 Agent",
        description="测试用",
        framework=AgentFramework.MOCK,
        endpoint="http://localhost",
        skill=Skill(name="test", description="d"),
    )
    assert spec.framework == AgentFramework.MOCK
    assert spec.maturity == AgentMaturity.POC  # 默认值
    assert spec.created_at > 0  # 自动生成时间戳


def test_message_role_enum():
    msg = Message(role=Role.USER, content="hi")
    assert msg.role == Role.USER
    # 序列化为 string
    assert msg.role.value == "user"


def test_agent_framework_values():
    """确保所有框架名都是稳定的字符串（不能改）"""
    assert AgentFramework.COZE.value == "coze"
    assert AgentFramework.DIFY.value == "dify"
    assert AgentFramework.LANGGRAPH.value == "langgraph"
    assert AgentFramework.AGENTSCOPE_1X.value == "agentscope_1x"
    assert AgentFramework.AGENTSCOPE_2X.value == "agentscope_2x"
    assert AgentFramework.MOCK.value == "mock"
