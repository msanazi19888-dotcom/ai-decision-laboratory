import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import Navigation from "../components/Navigation";
import { getDecision } from "../services/api";

function DecisionDetails() {
  const { id } = useParams();

  const [decision, setDecision] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    const loadDecision = async () => {
      try {
        setLoading(true);
        setError("");

        const response = await getDecision(id);

        if (isMounted) {
          setDecision(response.data);
        }
      } catch (err) {
        if (isMounted) {
          setError("Failed to load decision details.");
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    loadDecision();

    return () => {
      isMounted = false;
    };
  }, [id]);

  return (
    <>
      <Navigation />

      <div className="hero">
        <p className="eyebrow">Decision Intelligence</p>
        <h1>Decision Details</h1>
        <p className="subtitle">
          Detailed explanation of the selected business decision.
        </p>
      </div>

      <div className="card">
        {loading && <p>Loading decision details...</p>}

        {error && <p className="error">{error}</p>}

        {!loading && !error && decision && (
          <div className="result">
            <div className="result-block">
              <p className="section-title">DECISION SUMMARY</p>

              <div className="kpi-grid">
                <div className="kpi-card">
                  <span className="kpi-label">Decision ID</span>
                  <span className="kpi-value">{decision.decision_id}</span>
                </div>

                <div className="kpi-card">
                  <span className="kpi-label">Decision Type</span>
                  <span className="kpi-value">{decision.decision_type}</span>
                </div>

                <div className="kpi-card">
                  <span className="kpi-label">Status</span>
                  <span className="status completed">
                    {decision.status.toUpperCase()}
                  </span>
                </div>
              </div>
            </div>

            <div className="result-block">
              <p className="section-title">CONTEXT</p>

              <div className="description-box">
                <h4>Business Objective</h4>
                <p>{decision.context?.business_objective}</p>
              </div>

              <div className="description-box">
                <h4>Product ID</h4>
                <p>{decision.context?.product_id}</p>
              </div>

              <div className="description-box">
                <h4>Priority</h4>
                <p>{decision.context?.priority}</p>
              </div>

              <div className="description-box">
                <h4>Time Horizon</h4>
                <p>{decision.context?.time_horizon}</p>
              </div>
            </div>

            <div className="result-block">
              <p className="section-title">SELECTED STRATEGY</p>

              {decision.selected_strategy ? (
                <>
                  <h2 className="strategy-name">
                    {decision.selected_strategy.name}
                  </h2>

                  <div className="info-row">
                    <span className="label">Evaluation Score</span>
                    <span className="score">
                      {decision.selected_strategy.score.toFixed(2)}
                    </span>
                  </div>

                  <div className="description-box">
                    <h4>Description</h4>
                    <p>{decision.selected_strategy.description}</p>
                  </div>
                </>
              ) : (
                <p>No selected strategy found.</p>
              )}
            </div>

            <div className="result-block">
              <p className="section-title">ALTERNATIVE STRATEGIES</p>

              {decision.strategies && decision.strategies.length > 0 ? (
                <div className="strategy-list">
                  {decision.strategies
                    .filter(
                      (strategy) =>
                        strategy.id !== decision.selected_strategy?.id
                    )
                    .map((strategy) => (
                      <div key={strategy.id} className="strategy-card">
                        <div className="strategy-card-header">
                          <span className="strategy-rank">
                            {strategy.name}
                          </span>
                          <span className="strategy-score">
                            {strategy.score.toFixed(2)}
                          </span>
                        </div>

                        <p className="strategy-description">
                          {strategy.description}
                        </p>
                      </div>
                    ))}
                </div>
              ) : (
                <p>No alternative strategies available.</p>
              )}
            </div>

            <div className="result-block">
              <p className="section-title">BUSINESS DATA</p>

              <div className="history-table">
                {decision.context?.business_data &&
                  Object.entries(decision.context.business_data).map(
                    ([key, value]) => (
                      <div key={key} className="history-row">
                        <div>{key}</div>
                        <div>{String(value)}</div>
                      </div>
                    )
                  )}
              </div>
            </div>
          </div>
        )}
      </div>
    </>
  );
}

export default DecisionDetails;