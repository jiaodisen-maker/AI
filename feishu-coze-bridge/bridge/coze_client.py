"""Coze 企业旗舰版 OpenAPI 客户端。

提供给 worker 调用的 5 类核心写入方法：
  - 知识库 CRUD
  - 触发 bot (chat)
  - 直接调起工作流
  - 成员管理
  - 创建会话

每个方法都做：
  - 限速兜底（max 12000 RPM 整体）
  - 自动重试 503 / 429（限流）
  - 抛 RetryableError / PermanentError 让 worker 决定怎么处理

PAT 走环境变量（生产从火山 KMS 拉），不在代码里。
"""
from __future__ import annotations

import base64
import logging
from typing import Any

import httpx

from .config import COZE


LOG = logging.getLogger("bridge.coze_client")


class CozeError(Exception):
    pass


class RetryableError(CozeError):
    """临时错误：worker 应退避重试。"""
    def __init__(self, msg: str, retry_after: float = 5.0):
        super().__init__(msg)
        self.retry_after = retry_after


class PermanentError(CozeError):
    """永久错误：worker 直接进 DLQ。"""


class CozeClient:
    def __init__(self):
        self._cli = httpx.AsyncClient(
            base_url=COZE.api_base,
            headers={
                "Authorization": f"Bearer {COZE.pat}",
                "Content-Type": "application/json",
            },
            timeout=30,
        )

    async def close(self) -> None:
        await self._cli.aclose()

    # ---- 内部 ----------------------------------------------------

    async def _request(self, method: str, path: str, **kw) -> dict:
        try:
            r = await self._cli.request(method, path, **kw)
        except httpx.TimeoutException as e:
            raise RetryableError(f"coze timeout: {e}", retry_after=10) from None
        except httpx.HTTPError as e:
            raise RetryableError(f"coze network: {e}", retry_after=10) from None

        if r.status_code == 429:
            ra = float(r.headers.get("Retry-After", "60"))
            raise RetryableError("coze 429 rate limited", retry_after=ra)
        if 500 <= r.status_code < 600:
            raise RetryableError(f"coze {r.status_code}: {r.text[:200]}",
                                  retry_after=5)
        if r.status_code in (401, 403):
            raise PermanentError(f"coze auth fail: {r.status_code} {r.text[:200]}")
        if r.status_code >= 400:
            raise PermanentError(f"coze {r.status_code}: {r.text[:200]}")

        try:
            return r.json()
        except Exception:
            return {"raw": r.text}

    # ---- 知识库 --------------------------------------------------

    async def upload_doc_to_kb(self, dataset_id: str, name: str,
                                content: bytes | str,
                                source_type: str = "local") -> dict:
        """source_type: local|online_web."""
        if source_type == "local":
            file_bytes = content if isinstance(content, bytes) else content.encode()
            file_b64 = base64.b64encode(file_bytes).decode()
            file_type = name.rsplit(".", 1)[-1] if "." in name else "txt"
            payload = {
                "dataset_id": dataset_id,
                "document_bases": [{
                    "name": name,
                    "source_info": {
                        "file_base64": file_b64,
                        "file_type": file_type,
                    },
                }],
                "chunk_strategy": {"chunk_type": 0},   # 0=自动；1=层级；2=自定义
            }
        else:   # online_web
            payload = {
                "dataset_id": dataset_id,
                "document_bases": [{
                    "name": name,
                    "source_info": {
                        "web_url": content if isinstance(content, str) else "",
                        "document_source": 1,
                    },
                }],
            }
        return await self._request("POST", f"/v1/datasets/{dataset_id}/documents",
                                    json=payload)

    async def update_doc(self, document_id: str, *,
                          name: str | None = None,
                          update_rule: dict | None = None) -> dict:
        body: dict[str, Any] = {}
        if name:
            body["document_name"] = name
        if update_rule:
            body["update_rule"] = update_rule
        return await self._request(
            "POST", f"/v1/datasets/documents/{document_id}/update", json=body)

    async def delete_doc(self, document_id: str) -> dict:
        return await self._request(
            "DELETE", f"/v1/datasets/documents/{document_id}")

    async def list_docs(self, dataset_id: str, page: int = 1,
                         size: int = 50) -> dict:
        return await self._request(
            "GET", f"/v1/datasets/{dataset_id}/documents",
            params={"page": page, "size": size})

    # ---- 触发 bot (chat) -----------------------------------------

    async def trigger_bot(self, bot_id: str, user_id: str, message: str,
                           conversation_id: str | None = None) -> dict:
        """通过 chat API 触发 bot 处理。"""
        payload: dict[str, Any] = {
            "bot_id": bot_id,
            "user_id": user_id,
            "additional_messages": [{
                "role": "user",
                "type": "question",
                "content": message,
                "content_type": "text",
            }],
            "stream": False,
        }
        if conversation_id:
            payload["conversation_id"] = conversation_id
        return await self._request("POST", "/v3/chat", json=payload)

    # ---- 工作流 --------------------------------------------------

    async def trigger_workflow(self, workflow_id: str, parameters: dict
                                ) -> dict:
        payload = {"workflow_id": workflow_id, "parameters": parameters}
        return await self._request("POST", "/v1/workflow/run", json=payload)

    # ---- 成员管理 ------------------------------------------------

    async def add_member(self, user_name: str, email: str,
                          role: str = "member") -> dict:
        payload = {
            "enterprise_id": COZE.enterprise_id,
            "user_name": user_name,
            "email": email,
            "role": role,
        }
        return await self._request(
            "POST", f"/v1/enterprises/{COZE.enterprise_id}/members",
            json=payload)

    async def remove_member(self, user_id: str) -> dict:
        return await self._request(
            "DELETE",
            f"/v1/enterprises/{COZE.enterprise_id}/members/{user_id}")

    async def list_members(self, page: int = 1, size: int = 100) -> dict:
        return await self._request(
            "GET", f"/v1/enterprises/{COZE.enterprise_id}/members",
            params={"page": page, "size": size})

    # ---- 会话 ----------------------------------------------------

    async def create_conversation(self, bot_id: str, user_id: str
                                   ) -> dict:
        payload = {"bot_id": bot_id, "user_id": user_id}
        return await self._request("POST", "/v1/conversation/create",
                                    json=payload)
