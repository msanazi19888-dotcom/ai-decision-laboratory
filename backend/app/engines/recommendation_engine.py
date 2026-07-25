from __future__ import annotations

from app.domain.recommendation import Recommendation
from app.domain.strategy import Strategy


class RecommendationEngine:
    """
    Creates the final recommendation based on
    the evaluated strategies.
    """

    def recommend(
        self,
        strategies: list[Strategy],
    ) -> Recommendation:

        if not strategies:
            raise ValueError(
                "No strategies available for recommendation."
            )

        best_strategy = max(
            strategies,
            key=lambda strategy: strategy.score,
        )

        recommendation = Recommendation(
            strategy=best_strategy,
            confidence=0.90,
            evaluation_score=best_strategy.score,
        )

        recommendation.add_explanation(
            f"The strategy '{best_strategy.name}' achieved the highest evaluation score."
        )

        return recommendation