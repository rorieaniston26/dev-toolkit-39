import os
from typing import Dict, Any, Optional

class Config:
    """Application configuration manager for dev-toolkit-39."""

    def __init__(self, env: str = "development") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "debug": env == "development",
            "version": "1.0.0",
            "timeout": 30
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Update existing configuration with a dictionary."""
        self.settings.update(new_settings)

    @property
    def is_production(self) -> bool:
        """Check if current environment is production."""
        return self.env == "production"

def load_config_from_env() -> Config:
    """Factory function to build config from environment variables."""
    env_type: str = os.getenv("APP_ENV", "development")
    config = Config(env=env_type)
    
    # Override with env vars if present
    timeout = os.getenv("APP_TIMEOUT")
    if timeout:
        config.update({"timeout": int(timeout)})
        
    return config