# AI Pipeline

## Overview

The AI module generates synthetic business data, engineers predictive features, trains a machine learning model, and exposes demand forecasting through a REST API.

## Pipeline

```text
Synthetic Data Generation
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Serialization (.pkl)
        │
        ▼
FastAPI Prediction Endpoint
        │
        ▼
React Dashboard
```

## Synthetic Data

The platform generates:

- Products
- Suppliers
- Inventory
- Sales History

## Feature Engineering

Features include:

- Day of week
- Month
- Year
- Weekend flag
- 7-day rolling average
- 30-day rolling average

Target:

- Next-day demand (`future_quantity`)

## Machine Learning

Algorithm:

- Random Forest Regressor

Output:

- `demand_model.pkl`

## Inference

The trained model is loaded by the backend and used through:

`POST /api/v2/predict-demand`