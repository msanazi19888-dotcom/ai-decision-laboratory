import DashboardKPICards from "./DashboardKPICards";
import DecisionTrendChart from "./DecisionTrendChart";
import StrategyDistributionChart from "./StrategyDistributionChart";
import DecisionStatusChart from "./DecisionStatusChart";
import ExecutiveSummary from "./ExecutiveSummary";
import RecentDecisionTable from "./RecentDecisionTable";

function ExecutiveAnalytics({
  analytics,
  loading,
  error,
}) {
  const recentDecisions = analytics?.recent_decisions || [];

  return (
    <div className="card">
      <p className="section-title">EXECUTIVE ANALYTICS</p>

      {loading && <p>Loading analytics...</p>}

      {error && <p className="error">{error}</p>}

      {!loading && !error && (
        <>
          <DashboardKPICards
            kpis={analytics.kpis}
          />

          <div className="analytics-grid dashboard-section">
            <DecisionTrendChart
              data={analytics.trend}
            />

            <StrategyDistributionChart
              data={analytics.strategy_distribution}
            />
          </div>

          <div className="analytics-grid dashboard-section">
            <DecisionStatusChart
              data={analytics.status_distribution}
            />

            <ExecutiveSummary
              kpis={analytics.kpis}
            />
          </div>

          <RecentDecisionTable
            decisions={recentDecisions}
          />
        </>
      )}
    </div>
  );
}

export default ExecutiveAnalytics; 