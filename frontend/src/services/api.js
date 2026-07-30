import axios from "axios";

const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8001";

const api = axios.create({
  baseURL: `${API_URL}/api/v1/decisions`,
  headers: {
    "Content-Type": "application/json",
  },
});

export const createReplenishmentDecision = async (payload) => {
  return await api.post("/replenishment", payload);
};

export const getDecisions = async () => {
  return await api.get("/");
};

export const getDecision = async (decisionId) => {
  return await api.get(`/${decisionId}`);
};

export default api;