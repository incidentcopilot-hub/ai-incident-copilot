from fastapi import FastAPI

from api.routes.health import router as health_router


def create_app() -> FastAPI:
    """Create FastAPI application with all routes."""
    app = FastAPI(title="AI Incident Copilot API")
    app.include_router(health_router)
    return app


app = create_app()
