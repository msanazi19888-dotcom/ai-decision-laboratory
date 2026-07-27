import { useState } from "react";
import { createReplenishmentDecision } from "../services/api";

function InputCard({ onRecommendation, onLoadingChange, onError }) {
  const [formData, setFormData] = useState({
    product_id: "P1001",
    business_objective: "Maintain stock availability",
    priority: "medium",
    time_horizon: "30_days",
    current_stock: 40,
    daily_sales: 18,
    supplier_lead_time: 7,
    safety_stock: 50,
    warehouse_capacity: 500,
    budget: 10000,
    unit_cost: 10,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]:
        name === "product_id" ||
        name === "business_objective" ||
        name === "priority" ||
        name === "time_horizon"
          ? value
          : value === ""
            ? ""
            : Number(value),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      onLoadingChange(true);
      onError("");

      const response = await createReplenishmentDecision(formData);

      onRecommendation(response.data);
    } catch (error) {
      console.error(error);
      onError(
        error?.response?.data?.detail ||
          error?.message ||
          "Failed to generate recommendation."
      );
    } finally {
      onLoadingChange(false);
    }
  };

  return (
    <section className="card">
      <h2>Decision Input</h2>

      <form className="form" onSubmit={handleSubmit}>
        <label>
          Product ID
          <input
            type="text"
            name="product_id"
            value={formData.product_id}
            onChange={handleChange}
          />
        </label>

        <label>
          Business Objective
          <input
            type="text"
            name="business_objective"
            value={formData.business_objective}
            onChange={handleChange}
          />
        </label>

        <label>
          Priority
          <input
            type="text"
            name="priority"
            value={formData.priority}
            onChange={handleChange}
          />
        </label>

        <label>
          Time Horizon
          <input
            type="text"
            name="time_horizon"
            value={formData.time_horizon}
            onChange={handleChange}
          />
        </label>

        <label>
          Current Stock
          <input
            type="number"
            name="current_stock"
            value={formData.current_stock}
            onChange={handleChange}
          />
        </label>

        <label>
          Daily Sales
          <input
            type="number"
            name="daily_sales"
            value={formData.daily_sales}
            onChange={handleChange}
          />
        </label>

        <label>
          Supplier Lead Time
          <input
            type="number"
            name="supplier_lead_time"
            value={formData.supplier_lead_time}
            onChange={handleChange}
          />
        </label>

        <label>
          Safety Stock
          <input
            type="number"
            name="safety_stock"
            value={formData.safety_stock}
            onChange={handleChange}
          />
        </label>

        <label>
          Warehouse Capacity
          <input
            type="number"
            name="warehouse_capacity"
            value={formData.warehouse_capacity}
            onChange={handleChange}
          />
        </label>

        <label>
          Budget
          <input
            type="number"
            name="budget"
            value={formData.budget}
            onChange={handleChange}
          />
        </label>

        <label>
          Unit Cost
          <input
            type="number"
            name="unit_cost"
            value={formData.unit_cost}
            onChange={handleChange}
          />
        </label>

        <button type="submit">Generate Recommendation</button>
      </form>
    </section>
  );
}

export default InputCard;