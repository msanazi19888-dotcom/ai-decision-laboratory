function SelectedStrategyCard({ strategy, status }) {
  if (!strategy) {
    return (
      <div className="result-block">
        <h3>🏆 Recommended Strategy</h3>
        <p>No strategy selected.</p>
      </div>
    );
  }

  return (
    <div className="result-block">

      <h3>🏆 Recommended Strategy</h3>

      <div className="strategy-name">
        {strategy.name}
      </div>

      <div className="score-box">

        <span className="label">
          Evaluation Score
        </span>

        <span className="score">
          {strategy.score.toFixed(2)}
        </span>

      </div>

      <div className="status-box">

        <span className="label">
          Status
        </span>

        <span className="status completed">
          {status.toUpperCase()}
        </span>

      </div>

      <hr />

      <h4>Description</h4>

      <p>{strategy.description}</p>

    </div>
  );
}

export default SelectedStrategyCard;