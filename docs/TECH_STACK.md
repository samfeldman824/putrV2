# PUTR Poker Tracker - Tech Stack Summary

## Backend
- **Framework**: FastAPI
- **Language**: Python 3.9, 3.10, 3.11
- **Data Validation**: Pydantic
- **Database**: Firebase (Firestore)
- **Hosting**: Railway.app
- **CSV Processing**: Pandas

## Code Quality
- **Linting & Formatting**: Ruff
- **Type Checking**: MyPy
- **Security Scanning**: Bandit
- **Pre-commit Hooks**: Yes
- **Testing**: Pytest
- **Multi-Python Testing**: Nox
- **Logging**: Python built-in (structured JSON)

## Development Commands
- **Make**: High-level shortcuts (`make test`, `make lint`)
- **Nox**: Testing across Python versions (`nox -s test -p 3.11`)

## Deployment & DevOps
- **Hosting Platform**: Railway.app
- **CI/CD**: GitHub Actions (tests on 3.9, 3.10, 3.11)
- **Version Control**: Git/GitHub

## Infrastructure & Configuration
- **Environment**: Dev container (Ubuntu 24.04.2 LTS)
- **Configuration Management**: Pydantic Settings
- **Dependency Injection**: FastAPI Depends()
- **Rate Limiting**: slowapi

## API Strategy
- **Documentation**: FastAPI auto-generated Swagger UI
- **Versioning**: URL-based (/api/v1/)
- **Error Handling**: Custom exception hierarchy
- **Async**: Full async for I/O
