# 🏗️ System Architecture

## 📖 Overview

AI Decision Laboratory follows a modern multi-layer architecture that separates presentation, business logic, data access, and artificial intelligence into independent modules.

This architecture improves scalability, maintainability, and testability.

---

## 🧩 High-Level Architecture

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
            Business Services
                   │
         Repository Pattern
                   │
            PostgreSQL Database
                   │
                   ▼
               AI Module
```

---

## 🖥️ Frontend

The frontend is developed using React and Vite.

Responsibilities include:

- Dashboard
- Executive Analytics
- Decision History
- AI Forecast
- Recommendation Workspace

---

## ⚙️ Backend

The backend is implemented using FastAPI.

Responsibilities include:

- REST APIs
- Business Logic
- Analytics
- Decision Engine
- AI Prediction API

---

## 🗄️ Database

PostgreSQL stores:

- Decisions
- Recommendations
- Strategies

Database migrations are managed using Alembic.

---

## 🤖 AI Module

The AI subsystem is responsible for:

- Synthetic data generation
- Feature engineering
- Model training
- Demand forecasting
- Prediction inference