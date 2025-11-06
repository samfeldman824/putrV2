"""Nox sessions for testing and code quality checks."""

import nox

# Python versions to test against
PYTHON_VERSIONS = ["3.10", "3.11", "3.12"]

# Default sessions to run when just typing 'nox'
nox.options.sessions = ["lint", "type_check", "test"]


@nox.session(python=PYTHON_VERSIONS)
def test(session: nox.Session) -> None:
    """Run the test suite with pytest."""
    session.install(".[dev]")
    session.run(
        "pytest",
        "-v",
        "--cov=backend",
        "--cov-report=term-missing",
        *session.posargs,
    )


@nox.session(python="3.11")
def lint(session: nox.Session) -> None:
    """Run ruff linter and formatter checks."""
    session.install("ruff")
    session.run("ruff", "check", "backend", "tests", "noxfile.py")
    session.run("ruff", "format", "--check", "backend", "tests", "noxfile.py")


@nox.session(python="3.11")
def format(session: nox.Session) -> None:
    """Format code with ruff."""
    session.install("ruff")
    session.run("ruff", "check", "--fix", "backend", "tests", "noxfile.py")
    session.run("ruff", "format", "backend", "tests", "noxfile.py")


@nox.session(python="3.11")
def type_check(session: nox.Session) -> None:
    """Run mypy type checker."""
    session.install(".[dev]")
    session.run("mypy", "backend")


@nox.session(python="3.11")
def security(session: nox.Session) -> None:
    """Run security checks with bandit."""
    session.install("bandit")
    session.run("bandit", "-r", "backend", "-ll")


@nox.session(python="3.11")
def coverage(session: nox.Session) -> None:
    """Generate test coverage report."""
    session.install(".[dev]")
    session.run(
        "pytest",
        "--cov=backend",
        "--cov-report=html",
        "--cov-report=term-missing",
    )
    session.notify("View coverage report at: htmlcov/index.html")
