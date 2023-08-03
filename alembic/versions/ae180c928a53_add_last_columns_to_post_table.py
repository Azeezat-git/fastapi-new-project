"""add last columns to post table

Revision ID: ae180c928a53
Revises: 227cf876e51e
Create Date: 2023-08-03 19:03:10.792558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae180c928a53'
down_revision = '227cf876e51e'
branch_labels = None
depends_on = None



def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


    

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')


    pass