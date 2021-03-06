"""added User model

Revision ID: 39a48987c28c
Revises: 14d53c2e4304
Create Date: 2021-09-15 10:23:47.400000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39a48987c28c'
down_revision = '14d53c2e4304'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('post', 'first_name')
    op.drop_column('post', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_table('user')
    # ### end Alembic commands ###
