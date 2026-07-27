def get_dashboard_metrics(self) -> dict:
    decisions = self.repository.list_all()

    total_decisions = len(decisions)

    if total_decisions == 0:
        return {
            "kpis": {
                "total_decisions": 0,
                "average_score": 0,
                "recommendation_success_rate": 0,
                "average_estimated_cost": 0,
                "most_recommended_strategy": "N/A",
            },
            "trend": [],
            "strategy_distribution": [],
            "status_distribution": [],
            "recent_decisions": [],
        }

    selected = [
        d.selected_strategy
        for d in decisions
        if d.selected_strategy is not None
    ]

    average_score = (
        sum(s.score for s in selected) / len(selected)
        if selected else 0
    )

    average_cost = (
        sum(s.expected_cost for s in selected) / len(selected)
        if selected else 0
    )

    strategy_frequency = {}
    status_frequency = {}
    trend = []

    for index, decision in enumerate(reversed(decisions), start=1):

        trend.append({
            "label": f"D{index}",
            "value": 1,
        })

        status = decision.status.value
        status_frequency[status] = status_frequency.get(status, 0) + 1

        if decision.selected_strategy:
            name = decision.selected_strategy.name
            strategy_frequency[name] = (
                strategy_frequency.get(name, 0) + 1
            )

    strategy_distribution = [
        {"name": k, "value": v}
        for k, v in strategy_frequency.items()
    ]

    status_distribution = [
        {"name": k, "value": v}
        for k, v in status_frequency.items()
    ]

    recent = [
        {
            "decision_id": d.id,
            "decision_type": d.decision_type.value,
            "status": d.status.value,
            "strategy": (
                d.selected_strategy.name
                if d.selected_strategy
                else "-"
            ),
            "score": (
                round(d.selected_strategy.score, 2)
                if d.selected_strategy
                else 0
            ),
        }
        for d in decisions[:5]
    ]

    return {

        "kpis": {
            "total_decisions": total_decisions,
            "average_score": round(average_score, 2),
            "recommendation_success_rate": 100,
            "average_estimated_cost": round(average_cost, 2),
            "most_recommended_strategy": max(
                strategy_frequency,
                key=strategy_frequency.get,
            ),
        },

        "trend": trend,

        "strategy_distribution": strategy_distribution,

        "status_distribution": status_distribution,

        "recent_decisions": recent,
    }