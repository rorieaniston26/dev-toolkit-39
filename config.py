import os
from typing import Dict, Any, Optional

class Config:
    """Centralized configuration management for dev-toolkit-39."""

    def __init__(self, env: str = "development") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "debug": True if env == "development" else False,
            "timeout": int(os.getenv("APP_TIMEOUT", "30")),
            "root_path": os.getcwd()
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Update or add a new configuration setting."""
        self.settings[key] = value

    def __repr__(self) -> str:
        """Return string representation of configuration."""
        return f"Config(env={self.env}, settings={list(self.settings.keys())})"

def load_config(env_name: str = "production") -> Config:
    """Factory function to initialize and return a Config instance."""
    config = Config(env=env_name)
    # Apply overrides from environment variables if present
    if os.getenv("DEBUG_MODE") == "true":
        config.update("debug", True)
    return config