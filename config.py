import os
from pathlib import Path
from typing import Dict, Any

class Config:
    """Centralized application configuration management."""
    
    def __init__(self) -> None:
        self.base_dir = Path(__file__).resolve().parent
        self.env = os.getenv("APP_ENV", "development")
        self.debug = os.getenv("DEBUG", "True") == "True"
        self.settings = self._load_settings()

    def _load_settings(self) -> Dict[str, Any]:
        """Mock method for loading environment specific settings."""
        return {
            "timeout": int(os.getenv("TIMEOUT", "30")),
            "max_retries": int(os.getenv("MAX_RETRIES", "3")),
            "log_level": "DEBUG" if self.debug else "INFO"
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value with fallback."""
        return self.settings.get(key, default)

def get_config() -> Config:
    """Factory function for global config instance."""
    return Config()