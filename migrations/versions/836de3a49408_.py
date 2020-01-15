"""empty message

Revision ID: 836de3a49408
Revises: 6f34ab6f3ede
Create Date: 2020-01-14 10:43:43.712295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836de3a49408'
down_revision = '6f34ab6f3ede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('commented_on', sa.String(), nullable=True))
    op.create_foreign_key(None, 'comment', 'post', ['commented_on'], ['post_id'])
    op.add_column('deal', sa.Column('for_adoption', sa.Boolean(), nullable=False))
    op.alter_column('deal', 'price',
               existing_type=sa.NUMERIC(precision=100, scale=2),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('deal', 'price',
               existing_type=sa.NUMERIC(precision=100, scale=2),
               nullable=True)
    op.drop_column('deal', 'for_adoption')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'commented_on')
    # ### end Alembic commands ###