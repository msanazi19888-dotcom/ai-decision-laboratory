from __future__ import annotations

from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.domain.decision import Decision, DecisionStatus, DecisionType
from app.domain.decision_context import DecisionContext
from app.domain.decision_outcome import DecisionOutcome
from app.domain.strategy import Strategy
from app.infrastructure.database import SessionLocal
from app.infrastructure.models import (
    DecisionContextModel,
    DecisionModel,
    DecisionOutcomeModel,
    StrategyModel,
)
from app.repositories.decision_repository import DecisionRepository


class PostgreSQLDecisionRepository(DecisionRepository):
    def save(self, decision: Decision) -> Decision:
        with SessionLocal() as session:
            session.query(DecisionOutcomeModel).filter_by(
                decision_id=decision.id
            ).delete(synchronize_session=False)
            session.query(StrategyModel).filter_by(
                decision_id=decision.id
            ).delete(synchronize_session=False)
            session.query(DecisionContextModel).filter_by(
                decision_id=decision.id
            ).delete(synchronize_session=False)
            session.query(DecisionModel).filter_by(
                id=decision.id
            ).delete(synchronize_session=False)

            model = self._to_model(decision)
            session.add(model)
            session.commit()

            stmt = (
                select(DecisionModel)
                .options(
                    selectinload(DecisionModel.context),
                    selectinload(DecisionModel.strategies),
                    selectinload(DecisionModel.outcome),
                )
                .where(DecisionModel.id == decision.id)
            )
            saved_model = session.scalars(stmt).first()
            if saved_model is None:
                return decision

            return self._to_domain(saved_model)

    def get_by_id(self, decision_id: str) -> Optional[Decision]:
        with SessionLocal() as session:
            stmt = (
                select(DecisionModel)
                .options(
                    selectinload(DecisionModel.context),
                    selectinload(DecisionModel.strategies),
                    selectinload(DecisionModel.outcome),
                )
                .where(DecisionModel.id == decision_id)
            )
            model = session.scalars(stmt).first()
            if model is None:
                return None
            return self._to_domain(model)

    def list_all(self) -> List[Decision]:
        with SessionLocal() as session:
            stmt = (
                select(DecisionModel)
                .options(
                    selectinload(DecisionModel.context),
                    selectinload(DecisionModel.strategies),
                    selectinload(DecisionModel.outcome),
                )
                .order_by(DecisionModel.created_at.desc())
            )
            models = session.scalars(stmt).all()
            return [self._to_domain(model) for model in models]

    def _strategy_db_id(self, decision_id: str, strategy_id: str) -> str:
        return f"{decision_id}-{strategy_id}"

    def _to_model(self, decision: Decision) -> DecisionModel:
        model = DecisionModel(
            id=decision.id,
            decision_type=decision.decision_type.value,
            status=decision.status.value,
            selected_strategy_id=(
                self._strategy_db_id(decision.id, decision.selected_strategy.id)
                if decision.selected_strategy
                else None
            ),
            created_at=decision.created_at,
            completed_at=decision.completed_at,
        )

        if decision.context is not None:
            model.context = DecisionContextModel(
                decision_id=decision.id,
                product_id=decision.context.product_id,
                business_objective=decision.context.business_objective,
                priority=decision.context.priority,
                time_horizon=decision.context.time_horizon,
                business_data=decision.context.business_data,
                constraints=decision.context.constraints,
                policies=decision.context.policies,
                external_events=decision.context.external_events,
                created_at=decision.context.created_at,
            )

        model.strategies = [
            self._strategy_to_model(
                decision.id,
                strategy,
                decision.selected_strategy,
            )
            for strategy in decision.strategies
        ]

        if decision.outcome is not None:
            model.outcome = DecisionOutcomeModel(
                decision_id=decision.id,
                implemented=decision.outcome.implemented,
                actual_sales=decision.outcome.actual_sales,
                remaining_inventory=decision.outcome.remaining_inventory,
                stockout_occurred=decision.outcome.stockout_occurred,
                recommendation_successful=decision.outcome.recommendation_successful,
                notes=decision.outcome.notes,
                recorded_at=decision.outcome.recorded_at,
            )

        return model

    def _strategy_to_model(
        self,
        decision_id: str,
        strategy: Strategy,
        selected_strategy: Strategy | None,
    ) -> StrategyModel:
        return StrategyModel(
            id=self._strategy_db_id(decision_id, strategy.id),
            decision_id=decision_id,
            name=strategy.name,
            description=strategy.description,
            order_quantity=strategy.order_quantity,
            supplier=strategy.supplier,
            expected_cost=strategy.expected_cost,
            lead_time=strategy.lead_time,
            expected_stock_level=strategy.expected_stock_level,
            assumptions=strategy.assumptions,
            risks=strategy.risks,
            benefits=strategy.benefits,
            expected_impact=strategy.expected_impact,
            score=strategy.score,
            status=strategy.status,
            selected=bool(selected_strategy and selected_strategy.id == strategy.id),
        )

    def _to_domain(self, model: DecisionModel) -> Decision:
        context = None
        if model.context is not None:
            context = DecisionContext(
                product_id=model.context.product_id,
                business_objective=model.context.business_objective,
                priority=model.context.priority,
                time_horizon=model.context.time_horizon,
            )
            context.business_data = dict(model.context.business_data or {})
            context.constraints = list(model.context.constraints or [])
            context.policies = list(model.context.policies or [])
            context.external_events = list(model.context.external_events or [])
            context.created_at = model.context.created_at

        decision = Decision.create(
            decision_id=model.id,
            decision_type=DecisionType(model.decision_type),
            context=context,
        )
        decision.status = DecisionStatus(model.status)
        decision.created_at = model.created_at
        decision.completed_at = model.completed_at

        strategies: list[Strategy] = []
        for strategy_model in model.strategies:
            strategy = Strategy(
                id=strategy_model.id,
                name=strategy_model.name,
                description=strategy_model.description,
            )
            strategy.order_quantity = strategy_model.order_quantity
            strategy.supplier = strategy_model.supplier
            strategy.expected_cost = strategy_model.expected_cost
            strategy.lead_time = strategy_model.lead_time
            strategy.expected_stock_level = strategy_model.expected_stock_level
            strategy.assumptions = list(strategy_model.assumptions or [])
            strategy.risks = list(strategy_model.risks or [])
            strategy.benefits = list(strategy_model.benefits or [])
            strategy.expected_impact = dict(strategy_model.expected_impact or {})
            strategy.score = strategy_model.score
            strategy.status = strategy_model.status
            strategies.append(strategy)

        decision.strategies = strategies

        if model.selected_strategy_id:
            decision.selected_strategy = next(
                (s for s in strategies if s.id == model.selected_strategy_id),
                None,
            )

        if model.outcome is not None:
            decision.outcome = DecisionOutcome(
                implemented=model.outcome.implemented,
                actual_sales=model.outcome.actual_sales,
                remaining_inventory=model.outcome.remaining_inventory,
                stockout_occurred=model.outcome.stockout_occurred,
                recommendation_successful=model.outcome.recommendation_successful,
                notes=model.outcome.notes,
                recorded_at=model.outcome.recorded_at,
            )

        return decision