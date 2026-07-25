from __future__ import annotations

from app.domain.decision_knowledge import DecisionKnowledge
from app.domain.evaluation_criteria import EvaluationCriteria
from app.domain.strategy import Strategy


class StrategyEvaluator:
    """
    Evaluates candidate strategies using business criteria.
    """

    def evaluate(
        self,
        strategies: list[Strategy],
        knowledge: DecisionKnowledge,
    ) -> list[Strategy]:
        criteria = EvaluationCriteria()

        current_stock = knowledge.current_stock
        safety_stock = knowledge.safety_stock
        budget = max(knowledge.budget, 1.0)
        warehouse_capacity = knowledge.warehouse_capacity

        for strategy in strategies:
            order_quantity = strategy.order_quantity
            expected_cost = strategy.expected_cost

            inventory_risk_score = 1.0 if current_stock < safety_stock else 0.5

            if strategy.name == "Order Immediately":
                lead_time_score = 1.0
            elif strategy.name == "Partial Order":
                lead_time_score = 0.75
            elif strategy.name == "Delay Order":
                lead_time_score = 0.40
            else:
                lead_time_score = 0.60

            budget_score = 1.0 if expected_cost <= budget else 0.40

            projected_inventory = current_stock + order_quantity
            warehouse_score = 1.0 if projected_inventory <= warehouse_capacity else 0.30

            cost_score = max(0.0, 1.0 - (expected_cost / budget))

            weighted_score = (
                criteria.inventory_risk_weight * inventory_risk_score
                + criteria.budget_weight * budget_score
                + criteria.lead_time_weight * lead_time_score
                + criteria.warehouse_capacity_weight * warehouse_score
                + criteria.cost_weight * cost_score
            )

            normalized_score = (weighted_score / criteria.total_weight()) * 100.0
            strategy.score = round(normalized_score, 2)

        return strategies