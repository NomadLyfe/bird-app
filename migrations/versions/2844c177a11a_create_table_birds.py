"""create table birds

Revision ID: 2844c177a11a
Revises: 
Create Date: 2023-11-03 22:13:58.583900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2844c177a11a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('birds')
    # ### end Alembic commands ###
