from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Strategy:
    id: str
    name: str
    description: str = ""

    order_quantity: int = 0
    supplier: str = ""
    expected_cost: float = 0.0
    lead_time: int = 0
    expected_stock_level: int = 0

    assumptions: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    benefits: List[str] = field(default_factory=list)

    expected_impact: Dict[str, Any] = field(default_factory=dict)
    score: float = 0.0
    status: str = "evaluated"

    def add_risk(self, risk: str) -> None:
        self.risks.append(risk)

    def add_benefit(self, benefit: str) -> None:
        self.benefits.append(benefit)

    def add_assumption(self, assumption: str) -> None:
        self.assumptions.append(assumption)

    def set_score(self, score: float) -> None:
        self.score = score
        self.status = "evaluated" if score >= 0 else "rejected"