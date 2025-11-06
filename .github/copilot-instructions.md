# PUTR Poker Tracker - AI Coding Agent Instructions

## Project Overview
PUTR is a FastAPI-based poker session tracking application with Firebase backend. The project uses a clean architecture with clear separation between API routes, business logic, and data access layers.

## Architecture & Project Structure

### Backend Organization (`backend/`)
- `api/v1/` - FastAPI routers with versioned endpoints (use `/api/v1/` prefix)
- `models/` - Pydantic models for request/response validation and Firestore documents
- `services/` - Business logic layer (async methods for I/O operations)
- `middleware/` - Custom middleware (rate limiting via slowapi, logging, error handling)
- `utils/` - Shared utilities (Firebase clients, helpers)
- `cli/` - Command-line tools for management tasks

### Testing Structure (`tests/`)
- `unit/` - Fast, isolated tests for services and utilities
- `integration/` - Tests with real Firebase emulator or test project
- `e2e/` - Full API endpoint tests
- `fixtures/` - Shared test data and pytest fixtures

### Frontend (`frontend/`)
- Future frontend application (structure TBD)

## Development Workflow

### Setup & Dependencies
- Python 3.10, 3.11, 3.12 support required
- Use `make` commands for common tasks (when Makefile is populated)
- Use `nox` for multi-version Python testing: `nox -s test -p 3.11`
- Firebase credentials required for backend services

### Code Quality Standards
- **Linting/Formatting**: Ruff (replaces black, isort, flake8)
- **Type Checking**: MyPy - all functions should have type hints
- **Security**: Bandit for security scanning
- **Pre-commit**: Hooks configured for automatic checks
- **Testing**: Pytest with async support

### Key Conventions
1. **Async by Default**: All I/O operations (Firebase, external APIs) must be async
2. **Dependency Injection**: Use FastAPI's `Depends()` for services and database clients
3. **Error Handling**: Custom exception hierarchy - don't use generic exceptions
4. **Logging**: Use Rich logging handler - `from rich.logging import RichHandler` with Python's `logging` module
5. **Configuration**: Pydantic Settings for environment-based config
6. **CSV Processing**: Use Pandas for poker session CSV imports

## Firebase Integration
- Database: Firestore for all persistent data
- Authentication: Firebase Auth (implementation pending)
- Use Firebase Admin SDK for backend operations
- Keep Firebase client initialization in `backend/utils/`

## API Design Patterns
- **Versioning**: All routes under `/api/v1/` (URL-based)
- **Documentation**: FastAPI auto-generates Swagger UI at `/docs`
- **Rate Limiting**: Apply slowapi decorators to prevent abuse
- **Response Models**: Always define Pydantic response models for type safety
- **Status Codes**: Use appropriate HTTP status codes (201 for creation, 204 for deletion, etc.)

## Testing Approach
- Run tests: `pytest` (unit) or `nox` (multi-version)
- Use pytest fixtures for database setup/teardown
- Mock external dependencies in unit tests
- Use Firebase emulator for integration tests
- Aim for high coverage on service layer

## Deployment
- **Platform**: Railway.app
- **CI/CD**: GitHub Actions runs tests on all supported Python versions
- **Environment**: Dev container (Ubuntu 24.04.2 LTS)
- Railway configuration will auto-detect FastAPI application

## When Adding Features
1. Start with Pydantic models in `models/`
2. Implement business logic in `services/` (async)
3. Create API routes in `api/v1/` with dependency injection
4. Add tests in appropriate test directory
5. Update API documentation if needed (FastAPI auto-docs handles most cases)

## Common Gotchas
- Always use async/await for Firebase operations
- Don't forget rate limiting decorators on public endpoints
- Pydantic models should match Firestore document structure
- Use MyPy type hints for better IDE support and fewer runtime errors
