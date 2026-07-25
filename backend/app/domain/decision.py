from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .decision_context import DecisionContext
    from .decision_outcome import DecisionOutcome
    from .strategy import Strategy


class DecisionType(str, Enum):
    INVENTORY_REPLENISHMENT = "inventory_replenishment"


class DecisionStatus(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Decision:
    id: str
    decision_type: DecisionType
    context: Optional["DecisionContext"] = None
    status: DecisionStatus = DecisionStatus.CREATED
    strategies: List["Strategy"] = field(default_factory=list)
    selected_strategy: Optional["Strategy"] = None
    outcome: Optional["DecisionOutcome"] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

    @classmethod
    def create(
        cls,
        decision_id: str,
        decision_type: DecisionType,
        context: Optional["DecisionContext"] = None,
    ) -> "Decision":
        return cls(
            id=decision_id,
            decision_type=decision_type,
            context=context,
        )

    def start(self) -> None:
        self._ensure_not_finalized()
        if self.status != DecisionStatus.CREATED:
            raise ValueError(f"Decision cannot be started from status '{self.status.value}'.")
        self.status = DecisionStatus.IN_PROGRESS

    def add_strategy(self, strategy: "Strategy") -> None:
        self._ensure_not_finalized()
        if self.has_strategy(strategy.id):
            raise ValueError(f"Strategy '{strategy.id}' already exists for this decision.")
        self.strategies.append(strategy)
        if self.status == DecisionStatus.CREATED:
            self.status = DecisionStatus.IN_PROGRESS

    def remove_strategy(self, strategy_id: str) -> None:
        self._ensure_not_finalized()
        if self.selected_strategy is not None and self.selected_strategy.id == strategy_id:
            self.selected_strategy = None

        original_count = len(self.strategies)
        self.strategies = [strategy for strategy in self.strategies if strategy.id != strategy_id]

        if len(self.strategies) == original_count:
            raise ValueError(f"Strategy '{strategy_id}' was not found.")

    def select_strategy(self, strategy_id: str) -> None:
        self._ensure_not_finalized()
        strategy = self._get_strategy(strategy_id)
        self.selected_strategy = strategy
        if self.status == DecisionStatus.CREATED:
            self.status = DecisionStatus.IN_PROGRESS

    def record_outcome(self, outcome: "DecisionOutcome") -> None:
        self._ensure_not_finalized()
        self.outcome = outcome

    def has_outcome(self) -> bool:
        return self.outcome is not None

    def complete(self) -> None:
        self._ensure_not_finalized()
        if self.selected_strategy is None:
            raise ValueError("A decision cannot be completed without a selected strategy.")
        self.status = DecisionStatus.COMPLETED
        self.completed_at = datetime.utcnow()

    def cancel(self) -> None:
        self._ensure_not_finalized()
        self.status = DecisionStatus.CANCELLED
        self.completed_at = datetime.utcnow()

    def has_strategy(self, strategy_id: str) -> bool:
        return any(strategy.id == strategy_id for strategy in self.strategies)

    def is_completed(self) -> bool:
        return self.status == DecisionStatus.COMPLETED

    def is_cancelled(self) -> bool:
        return self.status == DecisionStatus.CANCELLED

    def _get_strategy(self, strategy_id: str) -> "Strategy":
        for strategy in self.strategies:
            if strategy.id == strategy_id:
                return strategy
        raise ValueError(f"Strategy '{strategy_id}' was not found.")

    def _ensure_not_finalized(self) -> None:
        if self.status == DecisionStatus.COMPLETED:
            raise RuntimeError("Completed decisions cannot be modified.")
        if self.status == DecisionStatus.CANCELLED:
            raise RuntimeError("Cancelled decisions cannot be modified.")