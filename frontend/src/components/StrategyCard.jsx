function StrategyCard({ strategy, rank }) {
  return (
    <div className="strategy-card">
      <div className="strategy-card-header">
        <span className="strategy-rank">#{rank}</span>
        <span className="strategy-score">{strategy.score.toFixed(2)}</span>
      </div>

      <h4 className="strategy-title">{strategy.name}</h4>

      <p className="strategy-description">{strategy.description}</p>
    </div>
  );
}

export default StrategyCard;