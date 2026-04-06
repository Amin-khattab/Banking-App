"""add balance to users

Revision ID: 765059adc609
Revises: f774fedccec2
Create Date: 2026-04-07 01:18:41.838622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '765059adc609'
down_revision: Union[str, Sequence[str], None] = 'f774fedccec2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",
                  sa.Column("balance",
                            sa.Numeric(precision=10,scale=2),
                            server_default=sa.text("10000.00"),
                            nullable=False)
                            )


def downgrade() -> None:
    op.drop_column("users","balance")
