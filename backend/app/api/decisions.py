from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.services.decision_service import DecisionService

router = APIRouter(prefix="/api/v1/decisions", tags=["decisions"])
service = DecisionService()


def serialize_decision_summary(decision):
    return {
        "decision_id": decision.id,
        "decision_type": decision.decision_type.value if hasattr(decision.decision_type, "value") else str(decision.decision_type),
        "status": decision.status.value if hasattr(decision.status, "value") else str(decision.status),
        "strategy": decision.selected_strategy.name if decision.selected_strategy else "-",
        "score": round(decision.selected_strategy.score, 2) if decision.selected_strategy else 0,
        "created_at": decision.created_at.isoformat() if decision.created_at else None,
    }


def serialize_decision_detail(decision):
    return {
        "decision_id": decision.id,
        "decision_type": decision.decision_type.value if hasattr(decision.decision_type, "value") else str(decision.decision_type),
        "status": decision.status.value if hasattr(decision.status, "value") else str(decision.status),
        "created_at": decision.created_at.isoformat() if decision.created_at else None,
        "completed_at": decision.completed_at.isoformat() if decision.completed_at else None,
        "context": decision.context,
        "strategies": decision.strategies,
        "selected_strategy": decision.selected_strategy,
        "outcome": decision.outcome,
    }


@router.get("/")
def get_decisions():
    decisions = service.list_decisions()
    decisions = sorted(decisions, key=lambda d: d.created_at, reverse=True)
    return jsonable_encoder([serialize_decision_summary(d) for d in decisions])


@router.get("/{decision_id}")
def get_decision(decision_id: str):
    decision = service.get_decision(decision_id)
    if decision is None:
        raise HTTPException(status_code=404, detail="Decision not found")
    return jsonable_encoder(serialize_decision_detail(decision))