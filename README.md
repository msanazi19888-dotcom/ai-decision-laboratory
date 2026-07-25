# AI Decision Laboratory

An AI-powered Decision Intelligence platform that assists organizations in making explainable business decisions.

---

## Project Overview

AI Decision Laboratory is a graduation project that combines:

- Decision Support Systems (DSS)
- Decision Intelligence (DI)
- Explainable AI (XAI)
- Domain-Driven Design (DDD)
- Clean Architecture

The first implemented business use case is **Inventory Replenishment**, where the system generates, evaluates, and recommends replenishment strategies based on business knowledge.

---

## Objectives

The system aims to:

- Model organizational decision-making.
- Generate multiple decision alternatives.
- Evaluate strategies using business criteria.
- Produce explainable recommendations.
- Support future AI modules such as demand forecasting and scenario simulation.

---

## Architecture

```
Frontend
    │
    ▼
FastAPI API
    │
    ▼
Decision Service
    │
    ▼
Decision Intelligence Pipeline

Context Validation
        │
Knowledge Extraction
        │
Strategy Generation
        │
Strategy Evaluation
        │
Recommendation
        │
Explanation

    ▼

Domain Layer

Decision
DecisionContext
DecisionKnowledge
Strategy
Recommendation

    ▼

Repository Layer

InMemory Repository
PostgreSQL Repository (planned)
```

---

## Technology Stack

### Backend

- Python 3
- FastAPI
- Pydantic
- Pytest

### Architecture

- Clean Architecture
- Domain-Driven Design
- Repository Pattern

### Database

- PostgreSQL *(planned)*
- SQLAlchemy *(planned)*
- Alembic *(planned)*

### Frontend

- React *(planned)*
- Next.js *(planned)*

### AI

- Demand Forecasting *(planned)*
- Scenario Simulation *(planned)*
- Explainable AI *(planned)*

---

## Current Features

- FastAPI REST API
- Swagger Documentation
- Decision Domain Model
- Decision Context
- Decision Knowledge
- Strategy Model
- Knowledge Engine
- Strategy Generator
- Strategy Evaluator
- Recommendation Engine
- In-Memory Repository
- Unit Tests

---

## Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── domain/
│   ├── engines/
│   ├── repositories/
│   ├── services/
│   └── main.py
│
├── tests/
│
└── requirements.txt
```

---

## Running the Project

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python -m uvicorn app.main:app --reload
```

### Run Tests

```bash
python -m pytest
```

---

## Roadmap

### Phase 1

- ✅ Backend Foundation

### Phase 2

- 🚧 Decision Intelligence

### Phase 3

- PostgreSQL

### Phase 4

- React Dashboard

### Phase 5

- AI Integration

### Phase 6

- Evaluation

---

## Author

Graduation Project

AI Decision Laboratory

2026