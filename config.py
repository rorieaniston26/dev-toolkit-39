import os
from pathlib import Path
from typing import Dict, Any

# Project constants
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_LOG_LEVEL = "INFO"

def get_environment_config() -> Dict[str, Any]:
    """Extract configuration from environment variables."""
    return {
        "env": os.getenv("APP_ENV", "development"),
        "debug": os.getenv("DEBUG", "false").lower() == "true",
        "port": int(os.getenv("PORT", 8080)),
        "db_url": os.getenv("DATABASE_URL", "sqlite:///default.db")
    }

class Settings:
    """Application configuration container."""
    def __init__(self):
        self.data = get_environment_config()
        self.log_level = os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL)

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

# Global settings instance
settings = Settings()