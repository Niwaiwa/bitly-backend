"""create users table

Revision ID: 07638cc019da
Revises: 
Create Date: 2023-03-11 22:37:15.153361

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = '07638cc019da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('email', sa.String(length=255), nullable=False, index=True, unique=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('nickname', sa.String(length=30)),
    sa.Column('api_key', sa.String(length=64), unique=True),
    sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('TRUE')),
    sa.Column('is_verified', sa.Boolean(), nullable=False, server_default=sa.text('FALSE')),
    sa.Column('is_admin', sa.Boolean(), nullable=False, server_default=sa.text('FALSE')),
    sa.Column('created_time', sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('users')

