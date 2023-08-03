"""add user table

Revision ID: 7e7e753430a4
Revises: ae180c928a53
Create Date: 2023-08-03 19:04:01.509496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e7e753430a4'
down_revision = 'ae180c928a53'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False), 
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


    pass


def downgrade():
    op.drop_table('users')


    pass