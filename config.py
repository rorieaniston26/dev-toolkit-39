import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self._defaults = default_config
        self.settings = default_config.copy()

    def load(self, filepath: str) -> None:
        """Loads config from disk, merging over defaults."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self._merge(self.settings, user_config)
        except (json.JSONDecodeError, IOError):
            pass

    def _merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Recursively update dictionary settings."""
        for key, value in update.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._merge(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a specific configuration value."""
        return self.settings.get(key, default)