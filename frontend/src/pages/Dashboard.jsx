import { useEffect, useState } from "react";

import "./Dashboard.css";

import Navigation from "../components/Navigation";
import Header from "../components/Header";
import QuickActions from "../components/QuickActions";
import ExecutiveAnalytics from "../components/ExecutiveAnalytics";
import RecommendationWorkspace from "../components/RecommendationWorkspace";
import AIForecast from "../components/AIForecast";

const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8001";

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
        setAnalyticsLoading(true);
        setAnalyticsError("");

        const response = await fetch(
          `${API_URL}/api/v1/analytics/`,
          {
            signal: controller.signal,
          }
        );

        if (!response.ok) {
          throw new Error(`Failed to load analytics: ${response.status}`);
        }

        const data = await response.json();

        setAnalytics({
          ...EMPTY_ANALYTICS,
          ...data,
          kpis: {
            ...EMPTY_ANALYTICS.kpis,
            ...(data.kpis || {}),
          },
        });
      } catch (err) {
        if (err.name !== "AbortError") {
          console.error(err);
          setAnalyticsError("Failed to load dashboard analytics.");
        }
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
      <QuickActions />

      <ExecutiveAnalytics
        analytics={analytics}
        loading={analyticsLoading}
        error={analyticsError}
      />

      <AIForecast />

      <RecommendationWorkspace
        recommendation={recommendation}
        loading={loading}
        error={error}
        onRecommendation={setRecommendation}
        onLoadingChange={setLoading}
        onError={setError}
      />
    </>
  );
}

export default Dashboard;