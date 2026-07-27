from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base


class DecisionModel(Base):
    __tablename__ = "decisions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    decision_type: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, index=True)

    selected_strategy_id: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    context: Mapped["DecisionContextModel"] = relationship(
        back_populates="decision",
        cascade="all, delete-orphan",
        uselist=False,
    )

    strategies: Mapped[list["StrategyModel"]] = relationship(
        back_populates="decision",
        cascade="all, delete-orphan",
    )

    outcome: Mapped["DecisionOutcomeModel"] = relationship(
        back_populates="decision",
        cascade="all, delete-orphan",
        uselist=False,
    )


class DecisionContextModel(Base):
    __tablename__ = "decision_contexts"

    decision_id: Mapped[str] = mapped_column(
        ForeignKey("decisions.id", ondelete="CASCADE"),
        primary_key=True,
    )

    product_id: Mapped[str] = mapped_column(String(64), nullable=False)
    business_objective: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[str] = mapped_column(String(32), nullable=False)
    time_horizon: Mapped[str] = mapped_column(String(32), nullable=False)

    business_data: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
    constraints: Mapped[list[str]] = mapped_column(JSONB, default=list, nullable=False)
    policies: Mapped[list[str]] = mapped_column(JSONB, default=list, nullable=False)
    external_events: Mapped[list[str]] = mapped_column(JSONB, default=list, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    decision: Mapped["DecisionModel"] = relationship(back_populates="context")


class StrategyModel(Base):
    __tablename__ = "strategies"

    id: Mapped[str] = mapped_column(String(128), primary_key=True)

    decision_id: Mapped[str] = mapped_column(
        ForeignKey("decisions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, default="", nullable=False)

    order_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    supplier: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    expected_cost: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    lead_time: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    expected_stock_level: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    assumptions: Mapped[list[str]] = mapped_column(JSONB, default=list, nullable=False)
    risks: Mapped[list[str]] = mapped_column(JSONB, default=list, nullable=False)
    benefits: Mapped[list[str]] = mapped_column(JSONB, default=list, nullable=False)
    expected_impact: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)

    score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="evaluated", nullable=False)

    selected: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    decision: Mapped["DecisionModel"] = relationship(back_populates="strategies")


class DecisionOutcomeModel(Base):
    __tablename__ = "decision_outcomes"

    decision_id: Mapped[str] = mapped_column(
        ForeignKey("decisions.id", ondelete="CASCADE"),
        primary_key=True,
    )

    implemented: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    actual_sales: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    remaining_inventory: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    stockout_occurred: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    recommendation_successful: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    notes: Mapped[str] = mapped_column(Text, default="", nullable=False)

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    decision: Mapped["DecisionModel"] = relationship(back_populates="outcome")