from __future__ import annotations

from fastapi import APIRouter

from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/api/v1/analytics", tags=["analytics"])
analytics_service = AnalyticsService()


@router.get("/")
def get_dashboard_metrics():
    return analytics_service.get_dashboard_metrics()