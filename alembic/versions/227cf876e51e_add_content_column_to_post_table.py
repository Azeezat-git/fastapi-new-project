"""add content column to post table

Revision ID: 227cf876e51e
Revises: 310e8b1d1e55
Create Date: 2023-08-03 19:02:05.979716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '227cf876e51e'
down_revision = '310e8b1d1e55'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')

    pass