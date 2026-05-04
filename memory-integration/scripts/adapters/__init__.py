"""底层适配层。绝不直接被 OpenClaw 看到——只通过 router/mcp_server 间接调用。"""

from . import gbrain, hindsight, notify  # noqa
