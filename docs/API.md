# API Documentation

## Health

GET `/health`

Returns application health status.

---

## Analytics

GET `/api/v1/analytics`

Returns dashboard metrics.

---

## Decisions

GET `/api/v1/decisions`

Returns all decisions.

GET `/api/v1/decisions/{decision_id}`

Returns a single decision.

POST `/api/v1/decisions/replenishment`

Creates a replenishment recommendation.

---

## AI Prediction

POST `/api/v2/predict-demand`

Predicts future product demand using the trained machine learning model.