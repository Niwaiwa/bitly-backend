"""create urls and keys table

Revision ID: ea90ed65cdf8
Revises: 07638cc019da
Create Date: 2023-03-12 02:38:22.089518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea90ed65cdf8'
down_revision = '07638cc019da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('urls',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('hash', sa.String(length=64), nullable=False, index=True, unique=True),
    sa.Column('origin_url', sa.Text(length=65535), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()),
    sa.Column('expired_time', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    )
    op.create_table('keys',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('hash', sa.String(length=64), nullable=False, index=True, unique=True),
    sa.Column('is_used', sa.Boolean(), nullable=False, server_default=sa.text('TRUE')),
    )


def downgrade() -> None:
    op.drop_table('keys')
    op.drop_table('urls')

