"""empty message

Revision ID: 3c2575d14ca1
Revises: 
Create Date: 2020-02-20 12:14:17.504604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c2575d14ca1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('team', sa.String(), nullable=False),
    sa.Column('pos', sa.String(), nullable=False),
    sa.Column('age', sa.Float(), nullable=False),
    sa.Column('gp', sa.Integer(), nullable=False),
    sa.Column('mpg', sa.Float(), nullable=False),
    sa.Column('fta', sa.String(), nullable=False),
    sa.Column('ftp', sa.Float(), nullable=False),
    sa.Column('twpa', sa.String(), nullable=False),
    sa.Column('twpp', sa.Float(), nullable=False),
    sa.Column('thpa', sa.String(), nullable=False),
    sa.Column('thpp', sa.Float(), nullable=False),
    sa.Column('ppg', sa.Float(), nullable=False),
    sa.Column('rpg', sa.Float(), nullable=False),
    sa.Column('apg', sa.Float(), nullable=False),
    sa.Column('bpg', sa.Float(), nullable=False),
    sa.Column('topg', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('record')
    # ### end Alembic commands ###
