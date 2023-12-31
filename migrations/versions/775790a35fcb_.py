"""empty message

Revision ID: 775790a35fcb
Revises: f36577cd5f3d
Create Date: 2023-11-22 20:58:48.218032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '775790a35fcb'
down_revision = 'f36577cd5f3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstname', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=250), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')

    # ### end Alembic commands ###
