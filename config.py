import os
from pathlib import Path
from typing import Dict, Any

class Config:
    """Centralized application configuration management."""
    BASE_DIR = Path(__file__).resolve().parent
    ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True") == "True"

    DEFAULT_SETTINGS = {
        "log_level": "INFO",
        "timeout": 30,
        "retries": 3
    }

    def __init__(self, overrides: Dict[str, Any] = None):
        self.settings = self.DEFAULT_SETTINGS.copy()
        if overrides:
            self.settings.update(overrides)

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    @classmethod
    def from_env(cls) -> 'Config':
        """Initialize configuration from environment variables."""
        env_overrides = {
            "log_level": os.getenv("LOG_LEVEL", "INFO"),
            "timeout": int(os.getenv("TIMEOUT", 30)),
            "retries": int(os.getenv("RETRIES", 3))
        }
        return cls(overrides=env_overrides)

# Instantiate singleton for global use
app_config = Config.from_env()