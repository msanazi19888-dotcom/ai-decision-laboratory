import {
  ResponsiveContainer,
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Bar,
} from "recharts";

function DecisionStatusChart({ data }) {
  if (!data || data.length === 0) {
    return (
      <div className="card">
        <p className="section-title">DECISION STATUS</p>
        <p>No status data available.</p>
      </div>
    );
  }

  return (
    <div className="card">
      <p className="section-title">DECISION STATUS</p>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="name" />

          <YAxis allowDecimals={false} />

          <Tooltip />

          <Bar
            dataKey="value"
            fill="#16a34a"
            radius={[6, 6, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default DecisionStatusChart;