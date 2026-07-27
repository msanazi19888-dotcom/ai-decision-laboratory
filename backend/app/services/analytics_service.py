from __future__ import annotations

from app.infrastructure.postgres_decision_repository import PostgreSQLDecisionRepository


class AnalyticsService:
    def __init__(self) -> None:
        self.repository = PostgreSQLDecisionRepository()

    def get_dashboard_metrics(self) -> dict:
        decisions = self.repository.list_all()

        total_decisions = len(decisions)

        if total_decisions == 0:
            return {
                "total_decisions": 0,
                "average_score": 0,
                "recommendation_success_rate": 0,
                "average_estimated_cost": 0,
                "most_recommended_strategy": "N/A",
                "recent_decisions": [],
            }

        selected_strategies = [
            d.selected_strategy
            for d in decisions
            if d.selected_strategy is not None
        ]

        average_score = (
            sum(s.score for s in selected_strategies) / len(selected_strategies)
            if selected_strategies
            else 0
        )

        average_cost = (
            sum(s.expected_cost for s in selected_strategies) / len(selected_strategies)
            if selected_strategies
            else 0
        )

        strategy_frequency: dict[str, int] = {}
        for strategy in selected_strategies:
            strategy_frequency[strategy.name] = strategy_frequency.get(strategy.name, 0) + 1

        most_recommended = (
            max(strategy_frequency, key=strategy_frequency.get)
            if strategy_frequency
            else "N/A"
        )

        recent = [
            {
                "decision_id": d.id,
                "decision_type": d.decision_type.value,
                "status": d.status.value,
                "strategy": d.selected_strategy.name if d.selected_strategy else "-",
                "score": round(d.selected_strategy.score, 2) if d.selected_strategy else 0,
            }
            for d in decisions[:5]
        ]

        return {
            "total_decisions": total_decisions,
            "average_score": round(average_score, 2),
            "recommendation_success_rate": 100,
            "average_estimated_cost": round(average_cost, 2),
            "most_recommended_strategy": most_recommended,
            "recent_decisions": recent,
        }