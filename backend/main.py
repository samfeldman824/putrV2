"""Main FastAPI application entry point."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from rich.logging import RichHandler

# Configure logging with Rich
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle application startup and shutdown events."""
    # Startup
    logger.info("Starting PUTR Poker Tracker API...")
    # TODO: Initialize Firebase connection
    # TODO: Load configuration
    yield
    # Shutdown
    logger.info("Shutting down PUTR Poker Tracker API...")
    # TODO: Cleanup connections


# Create FastAPI application
app = FastAPI(
    title="PUTR Poker Tracker",
    description="API for tracking poker sessions and statistics",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint - health check."""
    return {"message": "PUTR Poker Tracker API", "status": "running"}


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


# TODO: Include routers
# from backend.api.v1 import sessions, statistics
# app.include_router(sessions.router, prefix="/api/v1")
# app.include_router(statistics.router, prefix="/api/v1")
