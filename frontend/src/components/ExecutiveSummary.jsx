function ExecutiveSummary({ kpis }) {
  if (!kpis) return null;

  return (
    <div className="card">
      <p className="section-title">EXECUTIVE SUMMARY</p>

      <div className="history-table">

        <div className="history-row">
          <div>Total Decisions</div>
          <div>{kpis.total_decisions}</div>
        </div>

        <div className="history-row">
          <div>Average Score</div>
          <div>{Number(kpis.average_score).toFixed(2)}</div>
        </div>

        <div className="history-row">
          <div>Success Rate</div>
          <div>{kpis.recommendation_success_rate}%</div>
        </div>

        <div className="history-row">
          <div>Average Cost</div>
          <div>
            ${Number(kpis.average_estimated_cost).toLocaleString(undefined, {
              minimumFractionDigits: 2,
              maximumFractionDigits: 2,
            })}
          </div>
        </div>

        <div className="history-row">
          <div>Top Strategy</div>
          <div>{kpis.most_recommended_strategy}</div>
        </div>

      </div>
    </div>
  );
}

export default ExecutiveSummary;