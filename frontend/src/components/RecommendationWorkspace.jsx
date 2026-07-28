import InputCard from "./InputCard";
import RecommendationCard from "./RecommendationCard";

function RecommendationWorkspace({
  recommendation,
  loading,
  error,
  onRecommendation,
  onLoadingChange,
  onError,
}) {
  return (
    <main className="grid dashboard-section">
      <InputCard
        onRecommendation={onRecommendation}
        onLoadingChange={onLoadingChange}
        onError={onError}
      />

      <RecommendationCard
        recommendation={recommendation}
        loading={loading}
        error={error}
      />
    </main>
  );
}

export default RecommendationWorkspace;