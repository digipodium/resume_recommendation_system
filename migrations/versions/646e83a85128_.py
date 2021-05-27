"""empty message

Revision ID: 646e83a85128
Revises: 6d4c2bf33617
Create Date: 2021-05-27 16:03:03.117791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '646e83a85128'
down_revision = '6d4c2bf33617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_upload', sa.Column('path', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('my_upload', 'path')
    # ### end Alembic commands ###