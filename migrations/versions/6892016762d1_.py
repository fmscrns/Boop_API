"""empty message

Revision ID: 6892016762d1
Revises: 9838abea1d76
Create Date: 2020-01-19 22:43:29.343699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6892016762d1'
down_revision = '9838abea1d76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_posted_by_fkey', 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'user', ['posted_by'], ['public_id'], ondelete='cascade')
    op.drop_constraint('deal_deal_owner_fkey', 'deal', type_='foreignkey')
    op.create_foreign_key(None, 'deal', 'user', ['deal_owner'], ['public_id'], ondelete='cascade')
    op.drop_constraint('pet_pet_owner_fkey', 'pet', type_='foreignkey')
    op.create_foreign_key(None, 'pet', 'user', ['pet_owner'], ['public_id'], ondelete='cascade')
    op.drop_constraint('photo_uploader_fkey', 'photo', type_='foreignkey')
    op.create_foreign_key(None, 'photo', 'user', ['uploader'], ['public_id'], ondelete='cascade')
    op.drop_constraint('post_post_author_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['post_author'], ['public_id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_post_author_fkey', 'post', 'user', ['post_author'], ['username'], ondelete='CASCADE')
    op.drop_constraint(None, 'photo', type_='foreignkey')
    op.create_foreign_key('photo_uploader_fkey', 'photo', 'user', ['uploader'], ['username'], ondelete='CASCADE')
    op.drop_constraint(None, 'pet', type_='foreignkey')
    op.create_foreign_key('pet_pet_owner_fkey', 'pet', 'user', ['pet_owner'], ['username'], ondelete='CASCADE')
    op.drop_constraint(None, 'deal', type_='foreignkey')
    op.create_foreign_key('deal_deal_owner_fkey', 'deal', 'user', ['deal_owner'], ['username'], ondelete='CASCADE')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key('comment_posted_by_fkey', 'comment', 'user', ['posted_by'], ['username'], ondelete='CASCADE')
    # ### end Alembic commands ###