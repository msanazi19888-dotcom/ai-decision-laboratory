import { useState } from "react";
import "./App.css";

import Header from "./components/Header";
import InputCard from "./components/InputCard";
import RecommendationCard from "./components/RecommendationCard";

function App() {
  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  return (
    <div className="app">
      <Header />

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
    </div>
  );
}

export default App;