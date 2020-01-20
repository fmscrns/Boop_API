"""empty message

Revision ID: 9838abea1d76
Revises: d9926beecff0
Create Date: 2020-01-19 21:11:06.323492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9838abea1d76'
down_revision = 'd9926beecff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet_profPhoto_rel')
    op.drop_table('user_profPhoto_rel')
    op.drop_table('user_coverPhoto_rel')
    op.drop_table('pet_coverPhoto_rel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet_coverPhoto_rel',
    sa.Column('public_id', sa.INTEGER(), server_default=sa.text('nextval(\'"pet_coverPhoto_rel_public_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('pet_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.public_id'], name='pet_coverPhoto_rel_pet_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.public_id'], name='pet_coverPhoto_rel_photo_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('public_id', name='pet_coverPhoto_rel_pkey')
    )
    op.create_table('user_coverPhoto_rel',
    sa.Column('public_id', sa.INTEGER(), server_default=sa.text('nextval(\'"user_coverPhoto_rel_public_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.public_id'], name='user_coverPhoto_rel_photo_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], name='user_coverPhoto_rel_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('public_id', name='user_coverPhoto_rel_pkey')
    )
    op.create_table('user_profPhoto_rel',
    sa.Column('public_id', sa.INTEGER(), server_default=sa.text('nextval(\'"user_profPhoto_rel_public_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.public_id'], name='user_profPhoto_rel_photo_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], name='user_profPhoto_rel_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('public_id', name='user_profPhoto_rel_pkey')
    )
    op.create_table('pet_profPhoto_rel',
    sa.Column('public_id', sa.INTEGER(), server_default=sa.text('nextval(\'"pet_profPhoto_rel_public_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('pet_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.public_id'], name='pet_profPhoto_rel_pet_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.public_id'], name='pet_profPhoto_rel_photo_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('public_id', name='pet_profPhoto_rel_pkey')
    )
    # ### end Alembic commands ###