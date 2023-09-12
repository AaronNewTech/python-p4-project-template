"""message

Revision ID: a59e6217b0f4
Revises: 937cab77bb05
Create Date: 2023-09-08 17:33:10.537956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a59e6217b0f4'
down_revision = '937cab77bb05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('age')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###