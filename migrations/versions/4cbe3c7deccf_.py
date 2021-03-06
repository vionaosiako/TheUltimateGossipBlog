"""empty message

Revision ID: 4cbe3c7deccf
Revises: 2743c73a5a1f
Create Date: 2022-05-16 13:48:40.273026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cbe3c7deccf'
down_revision = '2743c73a5a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.String(length=1000), nullable=True))
    op.drop_column('comments', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('content', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###
