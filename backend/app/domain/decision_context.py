from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class DecisionContext:
    """
    Represents all business information required
    to reason about a strategic decision.
    """

    product_id: str
    business_objective: str
    priority: str
    time_horizon: str

    business_data: dict[str, Any] = field(default_factory=dict)
    constraints: list[str] = field(default_factory=list)
    policies: list[str] = field(default_factory=list)
    external_events: list[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.utcnow)

    def add_constraint(self, constraint: str) -> None:
        self.constraints.append(constraint)

    def add_policy(self, policy: str) -> None:
        self.policies.append(policy)

    def add_business_data(self, key: str, value: Any) -> None:
        self.business_data[key] = value

    def add_external_event(self, event: str) -> None:
        self.external_events.append(event)