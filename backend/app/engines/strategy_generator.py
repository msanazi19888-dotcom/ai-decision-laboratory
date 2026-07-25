from __future__ import annotations

from app.domain.decision_knowledge import DecisionKnowledge
from app.domain.strategy import Strategy


class StrategyGenerator:
    """
    Generates candidate replenishment strategies
    based on structured decision knowledge.
    """

    def generate(self, knowledge: DecisionKnowledge) -> list[Strategy]:
        current_stock = knowledge.current_stock
        daily_sales = knowledge.daily_sales
        safety_stock = knowledge.safety_stock
        lead_time = knowledge.supplier_lead_time
        unit_cost = knowledge.unit_cost

        demand_during_lead_time = daily_sales * lead_time

        reorder_quantity = max(
            safety_stock + demand_during_lead_time - current_stock,
            0,
        )

        immediate_quantity = reorder_quantity
        partial_quantity = max(reorder_quantity // 2, 1)
        delay_quantity = 0

        immediate_cost = immediate_quantity * unit_cost
        partial_cost = partial_quantity * unit_cost
        delay_cost = 0.0

        immediate_expected_stock = max(
            current_stock + immediate_quantity - demand_during_lead_time,
            0,
        )
        partial_expected_stock = max(
            current_stock + partial_quantity - demand_during_lead_time,
            0,
        )
        delay_expected_stock = max(
            current_stock - demand_during_lead_time,
            0,
        )

        strategies = [
            Strategy(
                id="STR-001",
                name="Order Immediately",
                description=f"Order {immediate_quantity} units immediately.",
                order_quantity=immediate_quantity,
                supplier="Preferred Supplier",
                expected_cost=immediate_cost,
                lead_time=lead_time,
                expected_stock_level=immediate_expected_stock,
                assumptions=[
                    "Supplier lead time remains stable",
                    "Demand stays near current average",
                ],
                risks=[
                    "Higher immediate cash outflow",
                    "Possible overstock if demand drops",
                ],
                benefits=[
                    "Lowest stockout risk",
                    "Fast response to demand pressure",
                ],
                expected_impact={
                    "quantity": immediate_quantity,
                    "estimated_cost": immediate_cost,
                    "stock_risk": "low",
                },
                score=0.0,
            ),
            Strategy(
                id="STR-002",
                name="Partial Order",
                description=f"Order {partial_quantity} units now and review later.",
                order_quantity=partial_quantity,
                supplier="Preferred Supplier",
                expected_cost=partial_cost,
                lead_time=lead_time,
                expected_stock_level=partial_expected_stock,
                assumptions=[
                    "Demand can be monitored before the second order",
                    "Supplier availability remains stable",
                ],
                risks=[
                    "May still leave some stockout exposure",
                    "May require a second procurement action",
                ],
                benefits=[
                    "Reduces immediate budget pressure",
                    "Keeps some flexibility",
                ],
                expected_impact={
                    "quantity": partial_quantity,
                    "estimated_cost": partial_cost,
                    "stock_risk": "medium",
                },
                score=0.0,
            ),
            Strategy(
                id="STR-003",
                name="Delay Order",
                description="Delay replenishment and continue monitoring demand.",
                order_quantity=delay_quantity,
                supplier="Preferred Supplier",
                expected_cost=delay_cost,
                lead_time=lead_time,
                expected_stock_level=delay_expected_stock,
                assumptions=[
                    "Demand may slow down",
                    "Stockout risk is acceptable for now",
                ],
                risks=[
                    "Higher chance of stockout",
                    "May hurt service level",
                ],
                benefits=[
                    "Preserves budget in the short term",
                    "Avoids unnecessary purchase",
                ],
                expected_impact={
                    "quantity": delay_quantity,
                    "estimated_cost": delay_cost,
                    "stock_risk": "high",
                },
                score=0.0,
            ),
        ]

        return strategies