from app.domain.decision_context import DecisionContext
from app.domain.decision_knowledge import DecisionKnowledge


class KnowledgeEngine:
    def collect(self, context: DecisionContext) -> DecisionKnowledge:
        data = context.business_data

        return DecisionKnowledge(
            product_id=context.product_id,
            business_objective=context.business_objective,
            priority=context.priority,
            time_horizon=context.time_horizon,
            current_stock=data["current_stock"],
            daily_sales=data["daily_sales"],
            supplier_lead_time=data["supplier_lead_time"],
            safety_stock=data["safety_stock"],
            warehouse_capacity=data["warehouse_capacity"],
            budget=data["budget"],
            unit_cost=data["unit_cost"],
            constraints=context.constraints,
            policies=context.policies,
            external_events=context.external_events,
        )