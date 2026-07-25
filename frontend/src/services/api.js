import axios from "axios";

const api = axios.create({
  baseURL: "/api/v1/decisions",
  headers: {
    "Content-Type": "application/json",
  },
});

export const createReplenishmentDecision = (payload) => {
  return api.post("/replenishment", payload);
};

export default api;