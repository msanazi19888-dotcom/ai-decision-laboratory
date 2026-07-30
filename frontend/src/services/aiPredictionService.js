import axios from "axios";

const API = "http://127.0.0.1:8001/api/v2";
export async function predictDemand(data) {
    const response = await axios.post(
        `${API}/predict-demand`,
        data
    );

    return response.data;
}