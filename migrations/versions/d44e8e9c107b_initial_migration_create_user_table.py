"""Initial migration: create User table

Revision ID: d44e8e9c107b
Revises: 
Create Date: 2025-02-19 22:51:17.618966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd44e8e9c107b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('user')
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('display_name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    # ### end Alembic commands ###
