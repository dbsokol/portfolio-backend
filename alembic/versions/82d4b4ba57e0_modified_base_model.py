"""modified base model

Revision ID: 82d4b4ba57e0
Revises: 1fe633e19aab
Create Date: 2023-02-20 07:05:54.189794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "82d4b4ba57e0"
down_revision = "1fe633e19aab"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("skills") as batch_op:
        batch_op.alter_column("last_updated_at", new_column_name="updated_at")


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###