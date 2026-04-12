"""Tests for the AgentScope Brain layer — AgentFactory and BrainAgent."""

from app.brain.agent import AgentFactory, BrainAgent


def test_agent_factory_model_config():
    """AgentFactory builds valid model config from settings."""
    factory = AgentFactory()
    config = factory._build_model_config()
    assert config["config_name"] == "default"
    assert config["model_type"] == "litellm_chat"
    assert "model_name" in config


def test_brain_agent_creation():
    """BrainAgent can be created without initialization."""
    brain = BrainAgent()
    assert brain._coordinator is None
    assert brain.role_agent_names == []


def test_brain_agent_register_tool():
    """Tools can be registered before initialization."""
    brain = BrainAgent()

    def dummy_tool(x: str = "") -> str:
        """A test tool."""
        return x

    brain.register_tool(dummy_tool)
    # Tool should be in the toolkit
    schemas = brain.toolkit.get_json_schemas()
    assert len(schemas) > 0
