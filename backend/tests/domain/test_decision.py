import pytest

from app.domain.decision import Decision, DecisionStatus, DecisionType
from app.domain.decision_context import DecisionContext
from app.domain.strategy import Strategy


def create_context():
    return DecisionContext(
        product_id="P1001",
        business_objective="Maintain Stock",
        priority="high",
        time_horizon="30_days",
    )


def test_create_decision():
    context = create_context()

    decision = Decision.create(
        decision_id="DEC-001",
        decision_type=DecisionType.INVENTORY_REPLENISHMENT,
        context=context,
    )

    assert decision.id == "DEC-001"
    assert decision.status == DecisionStatus.CREATED
    assert decision.context == context


def test_add_strategy():
    context = create_context()

    decision = Decision.create(
        decision_id="DEC-001",
        decision_type=DecisionType.INVENTORY_REPLENISHMENT,
        context=context,
    )

    strategy = Strategy(
        id="S1",
        name="Order Now",
        description="Place replenishment order immediately.",
        score=0.95,
    )

    decision.add_strategy(strategy)

    assert len(decision.strategies) == 1


def test_select_strategy():
    context = create_context()

    decision = Decision.create(
        decision_id="DEC-001",
        decision_type=DecisionType.INVENTORY_REPLENISHMENT,
        context=context,
    )

    strategy = Strategy(
        id="S1",
        name="Order Now",
        description="Place replenishment order immediately.",
        score=0.95,
    )

    decision.add_strategy(strategy)
    decision.select_strategy("S1")

    assert decision.selected_strategy == strategy


def test_complete_decision():
    context = create_context()

    decision = Decision.create(
        decision_id="DEC-001",
        decision_type=DecisionType.INVENTORY_REPLENISHMENT,
        context=context,
    )

    strategy = Strategy(
        id="S1",
        name="Order Now",
        description="Place replenishment order immediately.",
        score=0.95,
    )

    decision.add_strategy(strategy)
    decision.select_strategy("S1")
    decision.complete()

    assert decision.status == DecisionStatus.COMPLETED


def test_cancel_decision():
    context = create_context()

    decision = Decision.create(
        decision_id="DEC-001",
        decision_type=DecisionType.INVENTORY_REPLENISHMENT,
        context=context,
    )

    decision.cancel()

    assert decision.status == DecisionStatus.CANCELLED


def test_cannot_complete_without_strategy():
    context = create_context()

    decision = Decision.create(
        decision_id="DEC-001",
        decision_type=DecisionType.INVENTORY_REPLENISHMENT,
        context=context,
    )

    with pytest.raises(ValueError):
        decision.complete()