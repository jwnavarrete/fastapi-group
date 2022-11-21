"""add_group_table

Revision ID: c95db72f987a
Revises: 7b1f464b34ce
Create Date: 2022-11-21 04:14:19.217456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c95db72f987a'
down_revision = '7b1f464b34ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('privacy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_creator', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('detail', sa.String(), nullable=False),
    sa.Column('privacy_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['privacy_id'], ['privacy.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_creator'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group')
    op.drop_table('privacy')
    op.drop_table('category')
    # ### end Alembic commands ###