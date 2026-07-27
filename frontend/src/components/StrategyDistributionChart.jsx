import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
} from "recharts";

const COLORS = [
  "#2563eb",
  "#16a34a",
  "#f59e0b",
  "#dc2626",
  "#9333ea",
];

function StrategyDistributionChart({ data }) {
  if (!data || data.length === 0) {
    return (
      <div className="card">
        <p className="section-title">STRATEGY DISTRIBUTION</p>
        <p>No strategy data available.</p>
      </div>
    );
  }

  return (
    <div className="card">
      <p className="section-title">STRATEGY DISTRIBUTION</p>

      <ResponsiveContainer width="100%" height={320}>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={110}
            label
          >
            {data.map((entry, index) => (
              <Cell
                key={entry.name}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Pie>

          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default StrategyDistributionChart;