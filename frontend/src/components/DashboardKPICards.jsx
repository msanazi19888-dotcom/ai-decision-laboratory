const currencyFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  maximumFractionDigits: 2,
});

function DashboardKPICards({ kpis }) {
  if (!kpis) return null;

  return (
    <div className="kpi-grid">

      <div className="kpi-card">
        <span className="kpi-label">📋 Total Decisions</span>
        <span className="kpi-value">
          {kpis.total_decisions}
        </span>
      </div>

      <div className="kpi-card">
        <span className="kpi-label">⭐ Average Score</span>
        <span className="kpi-value">
          {Number(kpis.average_score).toFixed(2)}
        </span>
      </div>

      <div className="kpi-card">
        <span className="kpi-label">✅ Success Rate</span>
        <span className="kpi-value">
          {kpis.recommendation_success_rate}%
        </span>
      </div>

      <div className="kpi-card">
        <span className="kpi-label">💰 Average Cost</span>
        <span className="kpi-value">
          {currencyFormatter.format(
            kpis.average_estimated_cost
          )}
        </span>
      </div>

    </div>
  );
}

export default DashboardKPICards;