import { Routes, Route } from "react-router-dom";

import "./App.css";
import Dashboard from "./pages/Dashboard";
import DecisionHistory from "./pages/DecisionHistory";
import DecisionDetails from "./pages/DecisionDetails";

function App() {
  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/history" element={<DecisionHistory />} />
        <Route path="/decision/:id" element={<DecisionDetails />} />
      </Routes>
    </div>
  );
}

export default App;