# 🤖 AI Decision Laboratory

># 🤖 AI Decision Laboratory

> **Predict. Explain. Recommend.**

An AI-powered Decision Intelligence Platform built with **React**, **FastAPI**, **PostgreSQL**, and **Machine Learning**.

---

## ✨ Highlights

- 📊 Executive Analytics Dashboard
- 🤖 AI Demand Forecasting
- 📦 Inventory Replenishment Recommendations
- 📈 Interactive Data Visualization
- 📄 PDF & Excel Export
- 🧠 Machine Learning Pipeline

---

## 🚀 Features

### Decision Intelligence
- Executive Analytics Dashboard
- AI Recommendation Workspace
- Decision History
- Decision Details
- PDF Export
- Excel Export

### Artificial Intelligence
- Synthetic Data Generation
- Product Generator
- Supplier Generator
- Inventory Generator
- Sales Generator
- Feature Engineering
- Demand Forecasting
- Random Forest Model
- Prediction REST API
- AI Forecast Dashboard

---

## 🏗 Architecture

```text
                 User
                   │
                   ▼
          React Frontend (Vite)
                   │
             REST API (HTTP)
                   │
                   ▼
            FastAPI Backend
                   │
      ┌────────────┼────────────┐
      │            │            │
      ▼            ▼            ▼
 Decision API  Analytics API  AI Prediction API
      │            │            │
      └────────────┼────────────┘
                   │
            PostgreSQL Database
                   │
                   ▼
               AI Module
      ├── Synthetic Data Generation
      ├── Feature Engineering
      ├── Model Training
      └── Demand Prediction