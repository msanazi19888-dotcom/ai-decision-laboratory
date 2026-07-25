from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.replenishment import router as replenishment_router

app = FastAPI(
    title="AI Decision Laboratory",
    description="AI-powered strategic decision support platform",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(replenishment_router)


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