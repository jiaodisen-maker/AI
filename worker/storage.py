"""MinIO storage helper for case media (videos, ASR, OCR intermediates)."""
import os
from io import BytesIO

from minio import Minio


def get_minio_client() -> Minio:
    return Minio(
        os.getenv("MINIO_ENDPOINT", "localhost:9000"),
        access_key=os.getenv("MINIO_ROOT_USER", "minio"),
        secret_key=os.getenv("MINIO_ROOT_PASSWORD", "minio12345"),
        secure=False,
    )


def ensure_bucket(client: Minio, bucket: str) -> None:
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)


def put_bytes(bucket: str, key: str, data: bytes, content_type: str = "application/octet-stream") -> str:
    client = get_minio_client()
    ensure_bucket(client, bucket)
    client.put_object(bucket, key, BytesIO(data), length=len(data), content_type=content_type)
    return f"s3://{bucket}/{key}"
