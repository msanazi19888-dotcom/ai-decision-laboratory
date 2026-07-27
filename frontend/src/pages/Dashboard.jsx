import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import "./Dashboard.css";

import Navigation from "../components/Navigation";
import Header from "../components/Header";
import InputCard from "../components/InputCard";
import RecommendationCard from "../components/RecommendationCard";

import DashboardKPICards from "../components/DashboardKPICards";
import ExecutiveSummary from "../components/ExecutiveSummary";
import DecisionTrendChart from "../components/DecisionTrendChart";
import StrategyDistributionChart from "../components/StrategyDistributionChart";
import DecisionStatusChart from "../components/DecisionStatusChart";


const EMPTY_ANALYTICS = {
  kpis: {
    total_decisions: 0,
    average_score: 0,
    recommendation_success_rate: 0,
    average_estimated_cost: 0,
    most_recommended_strategy: "N/A",
  },
  trend: [],
  strategy_distribution: [],
  status_distribution: [],
  recent_decisions: [],
};

function Dashboard() {
  const navigate = useNavigate();

  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [analytics, setAnalytics] = useState(EMPTY_ANALYTICS);
  const [analyticsLoading, setAnalyticsLoading] = useState(true);
  const [analyticsError, setAnalyticsError] = useState("");

  useEffect(() => {
    const controller = new AbortController();

    const loadAnalytics = async () => {
      try {
        const response = await fetch("/api/v1/analytics/");

        if (!response.ok) {
          throw new Error();
        }

        const data = await response.json();

        setAnalytics({
          ...EMPTY_ANALYTICS,
          ...data,
        });
      } catch {
        setAnalyticsError("Failed to load analytics.");
      } finally {
        setAnalyticsLoading(false);
      }
    };

    loadAnalytics();

    return () => controller.abort();
  }, []);

  return (
    <>
      <Navigation />
      <Header />

      <div className="card">
        <h2>Executive Analytics</h2>

        {analyticsLoading && <p>Loading...</p>}

        {analyticsError && <p>{analyticsError}</p>}

        {!analyticsLoading && !analyticsError && (
          <>
            <DashboardKPICards kpis={analytics.kpis} />

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "1fr 1fr",
                gap: "20px",
                marginTop: "25px",
              }}
            >
              <DecisionTrendChart
                data={analytics.trend}
              />

              <StrategyDistributionChart
                data={analytics.strategy_distribution}
              />
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "1fr 1fr",
                gap: "20px",
                marginTop: "25px",
              }}
            >
              <DecisionStatusChart
                data={analytics.status_distribution}
              />

              <ExecutiveSummary
                kpis={analytics.kpis}
              />
            </div>

            <div
              className="card"
              style={{ marginTop: "25px" }}
            >
              <h3>Recent Decisions</h3>

              <table className="history-table">
                <thead>
                  <tr className="history-header">
                    <th>ID</th>
                    <th>Strategy</th>
                    <th>Score</th>
                    <th>Status</th>
                  </tr>
                </thead>

                <tbody>
                  {analytics.recent_decisions.map((d) => (
                    <tr
                      key={d.decision_id}
                      style={{ cursor: "pointer" }}
                      onClick={() =>
                        navigate(`/decision/${d.decision_id}`)
                      }
                    >
                      <td>{d.decision_id}</td>
                      <td>{d.strategy}</td>
                      <td>{d.score}</td>
                      <td>{d.status}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </>
        )}
      </div>

      <main className="grid">
        <InputCard
          onRecommendation={setRecommendation}
          onLoadingChange={setLoading}
          onError={setError}
        />

        <RecommendationCard
          recommendation={recommendation}
          loading={loading}
          error={error}
        />
      </main>
    </>
  );
}

export default Dashboard;