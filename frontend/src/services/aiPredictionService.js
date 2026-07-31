import axios from "axios";

const API = import.meta.env.VITE_API_URL || "http://127.0.0.1:8001";

export async function predictDemand(data) {
  const response = await axios.post(`${API}/api/v2/predict-demand`, data);
  return response.data;
}