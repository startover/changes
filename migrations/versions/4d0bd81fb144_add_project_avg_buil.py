"""Add Project.avg_build_time

Revision ID: 4d0bd81fb144
Revises: 52394fd42158
Create Date: 2013-09-26 15:28:00.760579

"""

# revision identifiers, used by Alembic.
revision = '4d0bd81fb144'
down_revision = '52394fd42158'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('avg_build_time', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'avg_build_time')
    ### end Alembic commands ###
