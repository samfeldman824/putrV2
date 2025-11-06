.PHONY: help install dev test lint format type-check security clean run coverage

# Default target - show available commands
help:
	@echo "PUTR Poker Tracker - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install        Install project dependencies"
	@echo "  make dev            Install dev dependencies and pre-commit hooks"
	@echo ""
	@echo "Development:"
	@echo "  make run            Run the FastAPI development server"
	@echo "  make test           Run tests with pytest"
	@echo "  make test-watch     Run tests in watch mode"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint           Check code with ruff"
	@echo "  make format         Format code with ruff"
	@echo "  make type-check     Run mypy type checker"
	@echo "  make security       Run bandit security checks"
	@echo "  make coverage       Generate test coverage report"
	@echo ""
	@echo "Multi-version Testing:"
	@echo "  make nox            Run all nox sessions"
	@echo "  make nox-test       Run tests across Python versions"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean          Remove build artifacts and caches"

# Installation
install:
	pip install -e .

dev:
	pip install -e ".[dev]"
	pre-commit install

# Development server
run:
	uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Testing
test:
	pytest -v

test-watch:
	pytest-watch

coverage:
	pytest --cov=backend --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated at htmlcov/index.html"

# Code quality
lint:
	ruff check backend tests noxfile.py

format:
	ruff check --fix backend tests noxfile.py
	ruff format backend tests noxfile.py

type-check:
	mypy backend

security:
	bandit -r backend -ll

# Nox multi-version testing
nox:
	nox

nox-test:
	nox -s test

# Cleanup
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
