import { useNavigate } from "react-router-dom";

function RecentDecisionTable({ decisions }) {
  const navigate = useNavigate();

  return (
    <div className="dashboard-section">
      <p className="section-title">RECENT DECISIONS</p>

      <div className="history-table">
        <div className="history-row history-header">
          <div>Decision ID</div>
          <div>Strategy</div>
          <div>Score</div>
          <div>Status</div>
        </div>

        {decisions.length === 0 ? (
          <div className="history-row">
            <div>No decisions found.</div>
            <div>-</div>
            <div>-</div>
            <div>-</div>
          </div>
        ) : (
          decisions.map((decision) => (
            <div
              key={decision.decision_id}
              className="history-row clickable-row"
              onClick={() =>
                navigate(`/decision/${decision.decision_id}`)
              }
            >
              <div>{decision.decision_id}</div>

              <div>{decision.strategy}</div>

              <div>
                {Number(decision.score || 0).toFixed(2)}
              </div>

              <div>
                <span className="status completed">
                  {decision.status.toUpperCase()}
                </span>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default RecentDecisionTable;