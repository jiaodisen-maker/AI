"""pytest 配置 - 让测试能 import services/agent-router/app"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "services" / "agent-router"))
