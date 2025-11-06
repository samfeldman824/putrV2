# PUTR Poker Tracker v2

A FastAPI-based poker session tracking application with Firebase backend.

## Quick Start

### 1. Install Dependencies

```bash
make dev
```

This will install the project and all development dependencies, and set up pre-commit hooks.

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your Firebase credentials
```

### 3. Run the Development Server

```bash
make run
```

Visit http://localhost:8000 to see the API running.
Visit http://localhost:8000/docs for interactive API documentation.

### 4. Run Tests

```bash
make test
```

## Development Commands

Run `make help` to see all available commands:

- **Setup**: `make install`, `make dev`
- **Run**: `make run`
- **Test**: `make test`, `make coverage`
- **Code Quality**: `make lint`, `make format`, `make type-check`
- **Multi-version**: `make nox` (test across Python 3.10, 3.11, 3.12)

## Project Structure

```
backend/
  ├── api/v1/        # API endpoints (versioned)
  ├── models/        # Pydantic models
  ├── services/      # Business logic
  ├── middleware/    # Custom middleware
  ├── utils/         # Shared utilities
  └── main.py        # FastAPI app entry point

tests/
  ├── unit/          # Unit tests
  ├── integration/   # Integration tests
  ├── e2e/           # End-to-end tests
  └── fixtures/      # Test fixtures
```

## Tech Stack

See [docs/TECH_STACK.md](docs/TECH_STACK.md) for details.

## Next Steps for Development

1. **Set up Firebase**: Configure Firestore and add credentials
2. **Create Models**: Define Pydantic models for poker sessions
3. **Add Services**: Implement business logic for session management
4. **Build API Routes**: Create endpoints in `backend/api/v1/`
5. **Write Tests**: Add tests as you build features