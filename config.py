import os
import json
from typing import Any, Dict

class ConfigLoader:
    """
    Loads configuration settings with support for default values, 
    JSON file overrides, and environment variable mapping.
    """
    def __init__(self, defaults: Dict[str, Any] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_json(self, filepath: str) -> None:
        """Loads configuration settings from a JSON file."""
        if not os.path.exists(filepath):
            return
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, dict):
                    self._config.update(data)
        except (json.JSONDecodeError, OSError):
            # Fail silently to allow fallbacks to defaults
            pass

    def load_env(self, prefix: str = "APP_") -> None:
        """Updates config values from environment variables if they match existing keys."""
        for key, default_val in list(self._config.items()):
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                self._config[key] = self._cast_type(raw_val, type(default_val))

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._config.get(key, default)

    def _cast_type(self, value: str, target_type: type) -> Any:
        """Attempts to cast string input from environment to the correct type."""
        if target_type is bool:
            return value.lower() in ('true', '1', 'yes', 'on')
        try:
            return target_type(value)
        except (ValueError, TypeError):
            return value
