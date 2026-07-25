from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC

from app.domain.strategy import Strategy


@dataclass
class Recommendation:
    """
    Represents the final recommendation produced
    by the Decision Intelligence Pipeline.
    """

    strategy: Strategy
    confidence: float
    evaluation_score: float
    explanation: list[str] = field(default_factory=list)
    status: str = "recommended"
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def add_explanation(self, text: str) -> None:
        self.explanation.append(text)