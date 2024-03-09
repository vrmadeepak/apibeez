"""create otp table

Revision ID: 5e329510db0b
Revises: 
Create Date: 2024-03-09 18:39:56.241787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e329510db0b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('otps',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('otp', sa.String(), nullable=False),
    sa.Column('otp_status', sa.Enum('FAIL', 'SENT', 'SUCCESS', name='otpstatusenum'), nullable=False),
    sa.Column('resend_attempts', sa.Integer(), nullable=True),
    sa.Column('verification_attempts', sa.Integer(), nullable=True),
    sa.Column('account_status', sa.Enum('LOCKED', 'ACTIVE', 'RETRY', name='accountstatusenum'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_otps_email'), 'otps', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_otps_email'), table_name='otps')
    op.drop_table('otps')
    # ### end Alembic commands ###