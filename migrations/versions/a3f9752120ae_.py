"""empty message

Revision ID: a3f9752120ae
Revises: 
Create Date: 2020-01-19 11:32:36.169702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3f9752120ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('business',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('business_name', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('contact_no', sa.String(length=20), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('circle',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('circle_name', sa.String(length=100), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('specie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('specie_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('specie_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('contact_no', sa.String(length=20), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('breed',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('breed_name', sa.String(length=100), nullable=True),
    sa.Column('specie_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['specie_id'], ['specie.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('breed_name'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('deal',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('posted_on', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Numeric(precision=100, scale=2), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.Column('deal_owner', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['deal_owner'], ['user.username'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('pet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('pet_name', sa.String(length=100), nullable=False),
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('sex', sa.String(length=100), nullable=False),
    sa.Column('profPic_filename', sa.String(length=50), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('pet_owner', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pet_owner'], ['user.username'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=300), nullable=False),
    sa.Column('posted_on', sa.DateTime(), nullable=False),
    sa.Column('post_author', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['post_author'], ['user.username'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('user_business_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('business_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ondelete='cascade')
    )
    op.create_table('user_circle_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('circle_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['circle_id'], ['circle.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ondelete='cascade')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('comment', sa.String(length=300), nullable=False),
    sa.Column('posted_on', sa.DateTime(), nullable=False),
    sa.Column('posted_by', sa.String(), nullable=True),
    sa.Column('post_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['posted_by'], ['user.username'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('pet_kind_rel',
    sa.Column('pet_id', sa.String(), nullable=True),
    sa.Column('specie_id', sa.String(), nullable=True),
    sa.Column('breed_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['breed_id'], ['breed.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['specie_id'], ['specie.public_id'], ondelete='cascade')
    )
    op.create_table('pet_price_rel',
    sa.Column('pet_id', sa.String(), nullable=True),
    sa.Column('deal_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['deal_id'], ['deal.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.public_id'], ondelete='cascade')
    )
    op.create_table('pet_sale_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('deal_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['deal_id'], ['deal.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ondelete='cascade')
    )
    op.create_table('user_pet_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('pet_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ondelete='cascade')
    )
    op.create_table('user_post_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('public_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['public_id'], ['post.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ondelete='cascade')
    )
    op.create_table('comment_post_rel',
    sa.Column('post_id', sa.String(), nullable=True),
    sa.Column('comm_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['comm_id'], ['comment.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['post_id'], ['post.public_id'], ondelete='cascade')
    )
    op.create_table('user_comment_rel',
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('comm_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['comm_id'], ['comment.public_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ondelete='cascade')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_comment_rel')
    op.drop_table('comment_post_rel')
    op.drop_table('user_post_rel')
    op.drop_table('user_pet_rel')
    op.drop_table('pet_sale_rel')
    op.drop_table('pet_price_rel')
    op.drop_table('pet_kind_rel')
    op.drop_table('comment')
    op.drop_table('user_circle_rel')
    op.drop_table('user_business_rel')
    op.drop_table('post')
    op.drop_table('pet')
    op.drop_table('deal')
    op.drop_table('breed')
    op.drop_table('user')
    op.drop_table('specie')
    op.drop_table('circle')
    op.drop_table('business')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###