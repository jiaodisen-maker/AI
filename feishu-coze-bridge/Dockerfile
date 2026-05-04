FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bridge/ ./bridge/

ENV PYTHONUNBUFFERED=1
EXPOSE 8810 9100

# default: webhook server. Override in docker-compose for worker / refresher.
CMD ["python", "-m", "bridge.server"]
