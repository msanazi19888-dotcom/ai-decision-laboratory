from fastapi import FastAPI

from app.api.analytics import router as analytics_router
from app.api.replenishment import router as replenishment_router

app = FastAPI(
    title="AI Decision Laboratory",
    description="AI-powered strategic decision support platform",
    version="0.1.0",
)

app.include_router(replenishment_router)
app.include_router(analytics_router)


@app.get("/")
def root():
    return {"message": "Welcome to AI Decision Laboratory"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Decision Laboratory",
        "version": "0.1.0",
    }