"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_session_data() -> dict[str, str | float]:
    """Sample poker session data for testing."""
    return {
        "date": "2025-11-06",
        "location": "Test Casino",
        "game_type": "NL Hold'em",
        "stakes": "1/2",
        "buy_in": 200.0,
        "cash_out": 350.0,
        "duration_hours": 4.5,
    }
