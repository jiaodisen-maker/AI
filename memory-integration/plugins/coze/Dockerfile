FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    fastapi==0.115.* uvicorn[standard]==0.32.* \
    httpx==0.27.* pydantic==2.* pyyaml==6.* \
    cryptography==43.* redis==5.*

# 整个 memory-integration（router / scripts / 等）都需要随插件一起跑
COPY ../../ /app/memory-integration/

ENV PYTHONUNBUFFERED=1
EXPOSE 8810

CMD ["python", "-m", "memory_integration.plugins.coze.server"]
