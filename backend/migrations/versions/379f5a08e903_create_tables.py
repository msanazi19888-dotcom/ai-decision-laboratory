"""Create tables

Revision ID: 379f5a08e903
Revises: 6c12ee5257d5
Create Date: 2026-07-26 15:34:34.025149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "379f5a08e903"
down_revision: Union[str, Sequence[str], None] = "6c12ee5257d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "decisions",
        sa.Column("id", sa.String(length=64), primary_key=True),
        sa.Column("decision_type", sa.String(length=64), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("selected_strategy_id", sa.String(length=128), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
    )

    op.create_index(
        op.f("ix_decisions_decision_type"),
        "decisions",
        ["decision_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_decisions_status"),
        "decisions",
        ["status"],
        unique=False,
    )
    op.create_index(
        op.f("ix_decisions_selected_strategy_id"),
        "decisions",
        ["selected_strategy_id"],
        unique=False,
    )

    op.create_table(
        "decision_contexts",
        sa.Column(
            "decision_id",
            sa.String(length=64),
            sa.ForeignKey("decisions.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("product_id", sa.String(length=64), nullable=False),
        sa.Column("business_objective", sa.String(length=255), nullable=False),
        sa.Column("priority", sa.String(length=32), nullable=False),
        sa.Column("time_horizon", sa.String(length=32), nullable=False),
        sa.Column("business_data", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("constraints", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("policies", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("external_events", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        "strategies",
        sa.Column("id", sa.String(length=128), primary_key=True),
        sa.Column(
            "decision_id",
            sa.String(length=64),
            sa.ForeignKey("decisions.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("order_quantity", sa.Integer(), nullable=False),
        sa.Column("supplier", sa.String(length=255), nullable=False),
        sa.Column("expected_cost", sa.Float(), nullable=False),
        sa.Column("lead_time", sa.Integer(), nullable=False),
        sa.Column("expected_stock_level", sa.Integer(), nullable=False),
        sa.Column("assumptions", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("risks", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("benefits", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("expected_impact", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("selected", sa.Boolean(), nullable=False),
    )

    op.create_index(
        op.f("ix_strategies_decision_id"),
        "strategies",
        ["decision_id"],
        unique=False,
    )

    op.create_table(
        "decision_outcomes",
        sa.Column(
            "decision_id",
            sa.String(length=64),
            sa.ForeignKey("decisions.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("implemented", sa.Boolean(), nullable=False),
        sa.Column("actual_sales", sa.Integer(), nullable=False),
        sa.Column("remaining_inventory", sa.Integer(), nullable=False),
        sa.Column("stockout_occurred", sa.Boolean(), nullable=False),
        sa.Column("recommendation_successful", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=False),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("decision_outcomes")
    op.drop_index(op.f("ix_strategies_decision_id"), table_name="strategies")
    op.drop_table("strategies")
    op.drop_table("decision_contexts")
    op.drop_index(op.f("ix_decisions_selected_strategy_id"), table_name="decisions")
    op.drop_index(op.f("ix_decisions_status"), table_name="decisions")
    op.drop_index(op.f("ix_decisions_decision_type"), table_name="decisions")
    op.drop_table("decisions")