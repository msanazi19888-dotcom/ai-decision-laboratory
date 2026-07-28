import { useNavigate } from "react-router-dom";
import { FaRobot, FaHistory, FaChartLine } from "react-icons/fa";

function QuickActions() {
  const navigate = useNavigate();

  const scrollToRecommendation = () => {
    window.scrollTo({
      top: document.body.scrollHeight,
      behavior: "smooth",
    });
  };

  const scrollToAnalytics = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  return (
    <div className="dashboard-section">
      <h2 className="analytics-title">QUICK ACTIONS</h2>

      <div className="analytics-grid">
        <div
          className="analytics-card clickable-row"
          onClick={scrollToRecommendation}
          role="button"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              scrollToRecommendation();
            }
          }}
        >
          <div className="quick-action-icon">
            <FaRobot />
          </div>

          <h3 className="quick-action-title">
            Generate Recommendation
          </h3>

          <p className="quick-action-description">
            Create a new AI-powered inventory replenishment
            recommendation.
          </p>

          <span className="quick-action-link">
            Start →
          </span>
        </div>

        <div
          className="analytics-card clickable-row"
          onClick={() => navigate("/history")}
          role="button"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              navigate("/history");
            }
          }}
        >
          <div className="quick-action-icon">
            <FaHistory />
          </div>

          <h3 className="quick-action-title">
            Decision History
          </h3>

          <p className="quick-action-description">
            Browse previous AI decisions and their business
            explanations.
          </p>

          <span className="quick-action-link">
            Open →
          </span>
        </div>

        <div
          className="analytics-card clickable-row"
          onClick={scrollToAnalytics}
          role="button"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              scrollToAnalytics();
            }
          }}
        >
          <div className="quick-action-icon">
            <FaChartLine />
          </div>

          <h3 className="quick-action-title">
            Executive Analytics
          </h3>

          <p className="quick-action-description">
            Review KPIs, analytics, trends, and executive
            business insights.
          </p>

          <span className="quick-action-link">
            Explore →
          </span>
        </div>
      </div>
    </div>
  );
}

export default QuickActions;