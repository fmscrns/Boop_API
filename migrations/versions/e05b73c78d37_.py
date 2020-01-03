"""empty message

Revision ID: e05b73c78d37
Revises: 2150529f906a
Create Date: 2020-01-03 19:40:37.895067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e05b73c78d37'
down_revision = '2150529f906a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=300), nullable=False),
    sa.Column('posted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('post_id')
    )
    op.create_table('user_post_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('post_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_post_rel')
    op.drop_table('post')
    # ### end Alembic commands ###
