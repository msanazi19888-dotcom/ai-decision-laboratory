import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { FaFilePdf } from "react-icons/fa";

import Navigation from "../components/Navigation";
import { getDecision } from "../services/api";
import { exportDecisionReport } from "../services/pdfExport";

import "./DecisionDetails.css";

function DecisionDetails() {
  const { id } = useParams();
  const navigate = useNavigate();

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
          console.error(err);
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

  const selectedStrategy = decision?.selected_strategy;

  const alternativeStrategies =
    decision?.strategies?.filter(
      (strategy) => strategy.id !== selectedStrategy?.id
    ) || [];

  const businessDataEntries = decision?.context?.business_data
    ? Object.entries(decision.context.business_data)
    : [];

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
        <div className="details-toolbar">
          <button
            type="button"
            className="view-button"
            onClick={() => navigate("/history")}
          >
            ← Back to History
          </button>

          {!loading && decision && (
            <button
              type="button"
              className="export-button"
              onClick={() => exportDecisionReport(decision)}
            >
              <FaFilePdf style={{ marginRight: "0.5rem" }} />
              Export PDF
            </button>
          )}
        </div>

        {loading && <p>Loading decision details...</p>}

        {error && <p className="error">{error}</p>}

        {!loading && !error && !decision && (
          <p>No decision details were found.</p>
        )}

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
                    {String(decision.status || "").toUpperCase()}
                  </span>
                </div>
              </div>
            </div>

            <div className="result-block">
              <p className="section-title">CONTEXT</p>

              <div className="kpi-grid">
                <div className="kpi-card">
                  <span className="kpi-label">Business Objective</span>
                  <span className="kpi-value">
                    {decision.context?.business_objective || "-"}
                  </span>
                </div>

                <div className="kpi-card">
                  <span className="kpi-label">Product ID</span>
                  <span className="kpi-value">
                    {decision.context?.product_id || "-"}
                  </span>
                </div>

                <div className="kpi-card">
                  <span className="kpi-label">Priority</span>
                  <span className="kpi-value">
                    {decision.context?.priority || "-"}
                  </span>
                </div>

                <div className="kpi-card">
                  <span className="kpi-label">Time Horizon</span>
                  <span className="kpi-value">
                    {decision.context?.time_horizon || "-"}
                  </span>
                </div>
              </div>
            </div>

            <div className="result-block">
              <p className="section-title">SELECTED STRATEGY</p>

              {selectedStrategy ? (
                <div className="description-box">
                  <h3 className="strategy-name">{selectedStrategy.name}</h3>

                  <div className="info-row">
                    <span className="label">Evaluation Score</span>

                    <span className="score">
                      {Number(selectedStrategy.score || 0).toFixed(2)}
                    </span>
                  </div>

                  <div className="details-section">
                    <h4>Description</h4>

                    <p>{selectedStrategy.description || "-"}</p>
                  </div>

                  {selectedStrategy.expected_impact &&
                    Object.keys(selectedStrategy.expected_impact).length > 0 && (
                      <div className="details-section">
                        <h4>Expected Impact</h4>

                        <div className="history-table">
                          {Object.entries(
                            selectedStrategy.expected_impact
                          ).map(([key, value]) => (
                            <div key={key} className="history-row">
                              <div>{key}</div>
                              <div>{String(value)}</div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                </div>
              ) : (
                <p>No selected strategy found.</p>
              )}
            </div>

            <div className="result-block">
              <p className="section-title">ALTERNATIVE STRATEGIES</p>

              {alternativeStrategies.length > 0 ? (
                <div className="strategy-list">
                  {alternativeStrategies.map((strategy) => (
                    <div key={strategy.id} className="strategy-card">
                      <div className="strategy-card-header">
                        <span className="strategy-rank">{strategy.name}</span>

                        <span className="strategy-score">
                          {Number(strategy.score || 0).toFixed(2)}
                        </span>
                      </div>

                      <p className="strategy-description">
                        {strategy.description || "-"}
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

              {businessDataEntries.length > 0 ? (
                <div className="history-table">
                  {businessDataEntries.map(([key, value]) => (
                    <div key={key} className="history-row">
                      <div>{key}</div>
                      <div>{String(value)}</div>
                    </div>
                  ))}
                </div>
              ) : (
                <p>No business data available.</p>
              )}
            </div>
          </div>
        )}
      </div>
    </>
  );
}

export default DecisionDetails;