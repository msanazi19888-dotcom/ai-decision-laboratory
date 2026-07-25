function DecisionSummary({ recommendation }) {
  return (
    <div className="result-block">

      <h3>Decision Details</h3>

      <p>
        <strong>Decision ID</strong>
      </p>

      <p>{recommendation.decision_id}</p>

      <hr />

      <p>
        <strong>Status</strong>
      </p>

      <p>{recommendation.status}</p>

      <hr />

      <p>
        <strong>Decision Type</strong>
      </p>

      <p>{recommendation.decision_type}</p>

    </div>
  );
}

export default DecisionSummary;