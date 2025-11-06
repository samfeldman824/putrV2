"""Configuration settings using Pydantic."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "PUTR Poker Tracker"
    debug: bool = False

    # API
    api_v1_prefix: str = "/api/v1"

    # Firebase (to be configured)
    firebase_project_id: str = ""
    firebase_credentials_path: str = ""


# Global settings instance
settings = Settings()
