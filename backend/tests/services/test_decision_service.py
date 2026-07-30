from app.domain.decision import Decision


class InMemoryDecisionRepository:
    def __init__(self):
        self._items = []

    def save(self, decision: Decision) -> Decision:
        self._items.append(decision)
        return decision

    def get_by_id(self, decision_id: str) -> Decision | None:
        for decision in self._items:
            if decision.id == decision_id:
                return decision
        return None

    def list_all(self) -> list[Decision]:
        return list(self._items)


from app.services.decision_service import DecisionService


def build_service():
    return DecisionService(repository=InMemoryDecisionRepository())


def test_create_replenishment_decision_returns_decision():
    service = build_service()

    decision = service.create_replenishment_decision(
        product_id="P1001",
        business_objective="AvoidStockout",
        priority="high",
        time_horizon="30_days",
    )

    assert decision.id.startswith("DEC-")
    assert decision.decision_type.value == "inventory_replenishment"
    assert decision.context is not None
    assert decision.context.product_id == "P1001"
    assert decision.context.business_objective == "AvoidStockout"


def test_get_decision_returns_saved_decision():
    service = build_service()

    created = service.create_replenishment_decision(
        product_id="P1001",
        business_objective="AvoidStockout",
        priority="high",
        time_horizon="30_days",
    )

    fetched = service.get_decision(created.id)

    assert fetched is not None
    assert fetched.id == created.id


def test_list_decisions_returns_all_saved_decisions():
    service = build_service()

    service.create_replenishment_decision(
        product_id="P1001",
        business_objective="AvoidStockout",
        priority="high",
        time_horizon="30_days",
    )
    service.create_replenishment_decision(
        product_id="P1002",
        business_objective="MaintainServiceLevel",
        priority="medium",
        time_horizon="30_days",
    )

    decisions = service.list_decisions()

    assert len(decisions) == 2