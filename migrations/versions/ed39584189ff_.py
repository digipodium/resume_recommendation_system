"""empty message

Revision ID: ed39584189ff
Revises: 881adb1b3ee7
Create Date: 2020-03-25 10:46:03.443851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed39584189ff'
down_revision = '881adb1b3ee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_upload', sa.Column('imgtype', sa.String(length=4), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('my_upload', 'imgtype')
    # ### end Alembic commands ###