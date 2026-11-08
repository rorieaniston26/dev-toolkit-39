import os
from typing import Dict, Any

class Config:
    """Centralized configuration management for dev-toolkit-39."""
    
    def __init__(self) -> None:
        self.env: str = os.getenv("APP_ENV", "development")
        self.debug: bool = os.getenv("DEBUG", "True") == "True"
        self.settings: Dict[str, Any] = {
            "timeout": 30,
            "max_retries": 3,
            "base_path": os.getcwd()
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve settings with fallback support."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Dynamic update of configuration values."""
        self.settings[key] = value

def load_config() -> Config:
    """Factory function for configuration instantiation."""
    config = Config()
    if config.env == "production":
        config.update("debug", False)
    return config