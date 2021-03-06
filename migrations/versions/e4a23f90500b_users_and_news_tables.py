"""users and news tables

Revision ID: e4a23f90500b
Revises: 9d155c0bcc1a
Create Date: 2020-11-03 14:00:49.260603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a23f90500b'
down_revision = '9d155c0bcc1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('text', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'event', ['url'])
    op.alter_column('user', 'birthday',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('user', 'birthday',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_constraint(None, 'event', type_='unique')
    op.drop_column('event', 'text')
    # ### end Alembic commands ###
