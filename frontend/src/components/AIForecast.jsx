import { useState } from "react";
import { predictDemand } from "../services/aiPredictionService";

export default function AIForecast() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handlePredict() {
    try {
      setLoading(true);
      setError("");
      setPrediction(null);

      const result = await predictDemand({
        day_of_week: 4,
        day: 15,
        month: 7,
        year: 2025,
        week_of_year: 29,
        is_weekend: 0,
        rolling_7_day_avg: 72,
        rolling_30_day_avg: 68,
      });

      setPrediction(result.predicted_demand);
    } catch (err) {
      console.error("Predict Demand failed:", err);
      setError("Failed to get AI prediction. Check backend terminal and browser console.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card" style={{ marginTop: "1rem" }}>
      <h2>🤖 AI Demand Forecast</h2>

      <button onClick={handlePredict} disabled={loading}>
        {loading ? "Predicting..." : "Predict Demand"}
      </button>

      {prediction !== null && (
        <h3 style={{ marginTop: "1rem" }}>
          Predicted Demand: {prediction} Units
        </h3>
      )}

      {error && (
        <p style={{ marginTop: "1rem", color: "red" }}>
          {error}
        </p>
      )}
    </div>
  );
}