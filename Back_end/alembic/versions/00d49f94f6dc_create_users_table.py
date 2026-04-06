"""create users table

Revision ID: 00d49f94f6dc
Revises: 
Create Date: 2026-04-04 13:57:09.611578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00d49f94f6dc'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None :
    op.create_table("users",
    sa.Column("id",sa.Integer(),nullable = False,primary_key=True),
    sa.Column("email",sa.String(length=255),nullable=False,unique=True),
    sa.Column("hashed_password",sa.String(length=255),nullable=False),
    sa.Column("created_at",sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))


def downgrade() -> None:
    op.drop_table("users")
