"""add column language_code

Revision ID: feaaa21a8352
Revises: 747915ac580c
Create Date: 2019-07-22 10:37:52.508253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feaaa21a8352'
down_revision = '747915ac580c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('language', sa.Column('language_code',
                                        sa.String, nullable=False, server_default="Unknown"))


def downgrade():
    pass
