# Getting Started with PUTR Poker Tracker

Welcome! This guide will walk you through building your first FastAPI application step-by-step.

## What You Have Now

You have a complete development environment set up with:
- ✅ FastAPI application with basic endpoints
- ✅ Testing framework (pytest) 
- ✅ Code quality tools (ruff, mypy, bandit)
- ✅ Multi-version testing (nox)
- ✅ Pre-configured Makefile for common tasks

## Your First Steps

### 1. Start the Development Server

```bash
make run
```

Visit:
- http://localhost:8000 - API root
- http://localhost:8000/docs - Interactive API documentation (Swagger UI)
- http://localhost:8000/health - Health check endpoint

### 2. Run the Tests

```bash
make test
```

You should see 2 passing tests. These test the basic endpoints.

### 3. Check Code Quality

```bash
make lint          # Check for issues
make format        # Auto-fix formatting
make type-check    # Run mypy type checking
```

## Next Steps: Building Your First Feature

Let's build a simple poker session tracker. Here's the recommended order:

### Step 1: Create a Pydantic Model

Create `backend/models/session.py`:

```python
from datetime import datetime
from pydantic import BaseModel, Field


class SessionCreate(BaseModel):
    """Data needed to create a poker session."""
    date: datetime
    location: str
    game_type: str
    stakes: str
    buy_in: float = Field(gt=0)
    cash_out: float = Field(ge=0)
    duration_hours: float = Field(gt=0)


class Session(SessionCreate):
    """Complete poker session with ID."""
    id: str
    profit: float  # Calculated: cash_out - buy_in
```

### Step 2: Create a Service

Create `backend/services/session_service.py`:

```python
from typing import List


class SessionService:
    """Business logic for poker sessions."""
    
    def __init__(self):
        # TODO: Add Firebase client
        self.sessions = {}  # Temporary in-memory storage
    
    async def create_session(self, session_data: dict) -> dict:
        """Create a new poker session."""
        # TODO: Save to Firebase
        pass
    
    async def get_session(self, session_id: str) -> dict:
        """Get a single session by ID."""
        # TODO: Fetch from Firebase
        pass
    
    async def list_sessions(self) -> List[dict]:
        """List all sessions."""
        # TODO: Query Firebase
        pass
```

### Step 3: Create API Endpoints

Create `backend/api/v1/sessions.py`:

```python
from fastapi import APIRouter, Depends, HTTPException

from backend.models.session import Session, SessionCreate
from backend.services.session_service import SessionService

router = APIRouter(prefix="/sessions", tags=["sessions"])


def get_session_service() -> SessionService:
    """Dependency injection for session service."""
    return SessionService()


@router.post("/", response_model=Session, status_code=201)
async def create_session(
    session: SessionCreate,
    service: SessionService = Depends(get_session_service)
):
    """Create a new poker session."""
    # TODO: Implement
    pass


@router.get("/{session_id}", response_model=Session)
async def get_session(
    session_id: str,
    service: SessionService = Depends(get_session_service)
):
    """Get a specific session by ID."""
    # TODO: Implement
    pass
```

### Step 4: Register the Router

In `backend/main.py`, add:

```python
from backend.api.v1 import sessions

app.include_router(sessions.router, prefix="/api/v1")
```

### Step 5: Write Tests

Create `tests/unit/test_sessions.py`:

```python
def test_create_session():
    # Test session creation
    pass
```

## Development Workflow

1. **Write a test** that defines what you want to build
2. **Run the test** and watch it fail: `make test`
3. **Write code** to make the test pass
4. **Run lint/format**: `make format && make lint`
5. **Run tests again**: `make test`
6. **Check the API docs**: Visit `/docs` to see your new endpoints

## Common Make Commands

```bash
make help          # See all available commands
make run           # Start development server
make test          # Run tests
make test-watch    # Run tests in watch mode (when available)
make coverage      # Generate coverage report
make lint          # Check code quality
make format        # Auto-fix formatting issues
make type-check    # Run mypy type checker
make nox           # Test across Python versions
```

## Tips for Learning FastAPI

1. **Start with endpoints** - Build simple GET/POST endpoints first
2. **Use the docs** - The auto-generated `/docs` page is invaluable
3. **Test as you go** - Write tests for each new feature
4. **Async by default** - Use `async def` for all routes and I/O operations
5. **Dependency injection** - Use `Depends()` to inject services
6. **Type hints everywhere** - FastAPI uses them for validation and docs

## When You're Ready for Firebase

1. Create a Firebase project
2. Download service account credentials
3. Add to `.env`:
   ```
   FIREBASE_PROJECT_ID=your-project-id
   FIREBASE_CREDENTIALS_PATH=path/to/credentials.json
   ```
4. Initialize Firebase in `backend/utils/firebase.py`
5. Update services to use Firestore

## Need Help?

- Check the FastAPI docs: https://fastapi.tiangolo.com
- Refer to `.github/copilot-instructions.md` for project conventions
- Run `make help` to see available commands
