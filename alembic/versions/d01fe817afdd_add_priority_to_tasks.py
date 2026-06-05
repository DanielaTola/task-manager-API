"""add priority to tasks

Revision ID: d01fe817afdd
Revises: 80b97694d5ae
Create Date: 2026-06-04 15:26:05.988847

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d01fe817afdd"
down_revision: Union[str, Sequence[str], None] = "80b97694d5ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "tasks",
        sa.Column(
            "priority",
            sa.String(length=50),
            nullable=False,
            server_default="medium",
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("tasks", "priority")
