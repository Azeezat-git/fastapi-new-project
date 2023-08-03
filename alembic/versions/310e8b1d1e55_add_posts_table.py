"""add posts table

Revision ID: 310e8b1d1e55
Revises: 
Create Date: 2023-08-03 19:00:11.978004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310e8b1d1e55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    


def downgrade():
    op.drop_table('posts')
    
