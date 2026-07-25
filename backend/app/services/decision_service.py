from __future__ import annotations

from uuid import uuid4

from app.domain.decision import Decision, DecisionType
from app.domain.decision_context import DecisionContext

from app.engines.knowledge_engine import KnowledgeEngine
from app.engines.strategy_generator import StrategyGenerator
from app.engines.strategy_evaluator import StrategyEvaluator
from app.engines.recommendation_engine import RecommendationEngine
from app.engines.explanation_engine import ExplanationEngine

from app.repositories.in_memory_decision_repository import InMemoryDecisionRepository


class DecisionService:
    def __init__(self) -> None:
        self.repository = InMemoryDecisionRepository()
        self.knowledge_engine = KnowledgeEngine()
        self.strategy_generator = StrategyGenerator()
        self.strategy_evaluator = StrategyEvaluator()
        self.recommendation_engine = RecommendationEngine()
        self.explanation_engine = ExplanationEngine()

    def create_replenishment_decision(
        self,
        *,
        product_id: str,
        business_objective: str,
        priority: str,
        time_horizon: str,
        current_stock: int = 120,
        daily_sales: int = 18,
        supplier_lead_time: int = 7,
        safety_stock: int = 50,
        warehouse_capacity: int = 500,
        budget: float = 10000.0,
        unit_cost: float = 10.0,
    ) -> Decision:
        context = DecisionContext(
            product_id=product_id,
            business_objective=business_objective,
            priority=priority,
            time_horizon=time_horizon,
        )

        context.add_business_data("current_stock", current_stock)
        context.add_business_data("daily_sales", daily_sales)
        context.add_business_data("supplier_lead_time", supplier_lead_time)
        context.add_business_data("safety_stock", safety_stock)
        context.add_business_data("warehouse_capacity", warehouse_capacity)
        context.add_business_data("budget", budget)
        context.add_business_data("unit_cost", unit_cost)

        context.add_constraint("Budget Limit")
        context.add_constraint("Warehouse Capacity")
        context.add_policy("Preferred Supplier")
        context.add_external_event("Seasonal Demand")

        knowledge = self.knowledge_engine.collect(context)

        decision = Decision.create(
            decision_id=f"DEC-{uuid4().hex[:8].upper()}",
            decision_type=DecisionType.INVENTORY_REPLENISHMENT,
            context=context,
        )

        strategies = self.strategy_generator.generate(knowledge)
        evaluated_strategies = self.strategy_evaluator.evaluate(strategies, knowledge)

        recommendation = self.recommendation_engine.recommend(evaluated_strategies)
        recommendation = self.explanation_engine.explain(knowledge, recommendation)

        for strategy in evaluated_strategies:
            decision.add_strategy(strategy)

        decision.select_strategy(recommendation.strategy.id)
        decision.complete()

        return self.repository.save(decision)

    def get_decision(self, decision_id: str) -> Decision | None:
        return self.repository.get_by_id(decision_id)

    def list_decisions(self) -> list[Decision]:
        return self.repository.list_all()