import DecisionSummary from "./DecisionSummary";
import SelectedStrategyCard from "./SelectedStrategyCard";
import StrategyCard from "./StrategyCard";

function RecommendationCard({ recommendation, loading, error }) {
  return (
    <section className="card">
      <h2>Recommendation</h2>

      {loading && <p>Generating recommendation...</p>}

      {error && <p className="error">{error}</p>}

      {!loading && !error && !recommendation && (
        <p>The generated recommendation will appear here.</p>
      )}

      {recommendation && (
        <div className="result">

          {/* Main Recommendation */}
          <SelectedStrategyCard
            strategy={recommendation.selected_strategy}
            status={recommendation.status}
          />

          {/* Decision Information */}
          <DecisionSummary recommendation={recommendation} />

          {/* Alternative Strategies */}
          <div className="result-block">
            <h3>Alternative Strategies</h3>

            {recommendation.strategies &&
            recommendation.strategies.length > 0 ? (
              <div className="strategy-list">
                {recommendation.strategies
                  .filter(
                    (strategy) =>
                      strategy.id !== recommendation.selected_strategy?.id
                  )
                  .map((strategy, index) => (
                    <StrategyCard
                      key={strategy.id}
                      strategy={strategy}
                      rank={index + 2}
                    />
                  ))}
              </div>
            ) : (
              <p>No alternative strategies available.</p>
            )}
          </div>

        </div>
      )}
    </section>
  );
}

export default RecommendationCard;