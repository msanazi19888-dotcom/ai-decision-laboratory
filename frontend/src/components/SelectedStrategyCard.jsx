function SelectedStrategyCard({ strategy, status = "Completed" }) {
  if (!strategy) {
    return (
      <div className="result-block">
        <p className="section-title">RECOMMENDED STRATEGY</p>
        <h2 className="strategy-name">No Recommendation</h2>
        <p>No strategy has been generated yet.</p>
      </div>
    );
  }

  return (
    <div className="result-block">
      <p className="section-title">🏆 RECOMMENDED STRATEGY</p>

      <h2 className="strategy-name">{strategy.name}</h2>

      <div className="info-row">
        <span className="label">Evaluation Score</span>
        <span className="score">{strategy.score.toFixed(2)}</span>
      </div>

      <div className="info-row">
        <span className="label">Status</span>
        <span className="status completed">
          {status.toUpperCase()}
        </span>
      </div>

      <div className="description-box">
        <h4>Business Description</h4>
        <p>{strategy.description}</p>
      </div>
    </div>
  );
}

export default SelectedStrategyCard;