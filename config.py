import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """Handles application configuration loading and validation."""

    def __init__(self, env_prefix: str = "DEV_TOOLKIT_") -> None:
        self.env_prefix: str = env_prefix
        self._settings: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        """Reads environment variables starting with the prefix."""
        for key, value in os.environ.items():
            if key.startswith(self.env_prefix):
                clean_key = key[len(self.env_prefix):].lower()
                self._settings[clean_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Sets or updates a configuration value."""
        self._settings[key] = value

    @property
    def all(self) -> Dict[str, Any]:
        """Returns a copy of all current settings."""
        return self._settings.copy()