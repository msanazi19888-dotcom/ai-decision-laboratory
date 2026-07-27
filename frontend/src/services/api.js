import axios from "axios";

const api = axios.create({
  baseURL: "/api/v1/decisions",
  headers: {
    "Content-Type": "application/json",
  },
});

// Create a new replenishment decision
export const createReplenishmentDecision = async (payload) => {
  return await api.post("/replenishment", payload);
};

// Get all decisions
export const getDecisions = async () => {
  return await api.get("");
};

// Get a single decision by ID
export const getDecision = async (decisionId) => {
  return await api.get(`/${decisionId}`);
};

export default api;