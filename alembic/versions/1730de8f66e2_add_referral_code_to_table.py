"""add referral_code to table

Revision ID: 1730de8f66e2
Revises: f1387f457423
Create Date: 2024-03-11 01:33:52.417156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1730de8f66e2'
down_revision: Union[str, None] = 'f1387f457423'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('referral_code', sa.String(), nullable=False))
    op.create_index(op.f('ix_users_referral_code'), 'users', ['referral_code'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_referral_code'), table_name='users')
    op.drop_column('users', 'referral_code')
    # ### end Alembic commands ###
