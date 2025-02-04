"""empty message

Revision ID: 66a35500024d
Revises: 19708a672da1
Create Date: 2018-05-19 10:53:26.197454

"""

# revision identifiers, used by Alembic.
revision = '66a35500024d'
down_revision = '19708a672da1'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pre_pedido', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pre_pedido', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('pre_pedido', 'keywords',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('pre_pedido', 'orgao_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('pre_pedido', 'state',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('pre_pedido', 'text',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pre_pedido', 'text',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('pre_pedido', 'state',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('pre_pedido', 'orgao_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('pre_pedido', 'keywords',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('pre_pedido', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('pre_pedido', 'author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
