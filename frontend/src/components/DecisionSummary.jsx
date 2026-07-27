function DecisionSummary({ recommendation }) {
  return (
    <div className="result-block">
      <p className="section-title">DECISION SUMMARY</p>

      <div className="kpi-grid">
        <div className="kpi-card">
          <span className="kpi-label">Decision ID</span>
          <span className="kpi-value">{recommendation.decision_id}</span>
        </div>

        <div className="kpi-card">
          <span className="kpi-label">Decision Type</span>
          <span className="kpi-value">{recommendation.decision_type}</span>
        </div>

        <div className="kpi-card">
          <span className="kpi-label">Status</span>
          <span className="kpi-value status completed">
            {recommendation.status.toUpperCase()}
          </span>
        </div>
      </div>
    </div>
  );
}

export default DecisionSummary;