"""oauth_tokens table for Douyin / Qianchuan token persistence + auto-refresh.

Revision ID: 002
Revises: 001
"""
from typing import Sequence, Union

from alembic import op

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE oauth_tokens (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            provider TEXT NOT NULL CHECK (provider IN ('douyin','qianchuan')),
            account_id TEXT NOT NULL,
            access_token TEXT NOT NULL,
            refresh_token TEXT,
            expires_at TIMESTAMPTZ,
            scope TEXT,
            advertiser_id TEXT,
            updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            UNIQUE (provider, account_id)
        )
        """
    )
    op.execute("CREATE INDEX idx_oauth_tokens_expires_at ON oauth_tokens (expires_at)")


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS oauth_tokens")
