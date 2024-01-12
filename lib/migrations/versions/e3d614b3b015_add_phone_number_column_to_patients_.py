"""Add phone_number column to patients table

Revision ID: e3d614b3b015
Revises: 5c0b648fe075
Create Date: 2024-01-11 10:37:16.972888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3d614b3b015'
down_revision: Union[str, None] = '5c0b648fe075'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'phone_number')
    # ### end Alembic commands ###