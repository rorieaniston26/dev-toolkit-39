import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Manages application configuration with default fallbacks and env overrides."""

    DEFAULT_CONFIG: Dict[str, Any] = {
        "app_name": "DevToolkit",
        "environment": "development",
        "debug": True,
        "port": 8080,
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "dev_db",
        },
    }

    def __init__(self, config_path: Optional[str] = None):
        self._config: Dict[str, Any] = json.loads(json.dumps(self.DEFAULT_CONFIG))
        if config_path and os.path.exists(config_path):
            self.load_from_file(config_path)

    def load_from_file(self, file_path: str) -> None:
        """Loads and merges configuration settings from a JSON file."""
        with open(file_path, "r", encoding="utf-8") as file:
            user_config = json.load(file)
        self._merge_dicts(self._config, user_config)

    def _merge_dicts(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Recursively merges source dictionary values into target."""
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._merge_dicts(target[key], value)
            else:
                target[key] = value

    def get(self, key_path: str, default: Any = None) -> Any:
        """Retrieves nested configuration value using dot notation."""
        keys = key_path.split(".")
        current = self._config
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        return current

    def override_from_env(self, prefix: str = "APP_") -> None:
        """Overrides matching configuration keys from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix) :].lower()
                if clean_key in self._config:
                    if value.lower() in ("true", "false"):
                        self._config[clean_key] = value.lower() == "true"
                    elif value.isdigit():
                        self._config[clean_key] = int(value)
                    else:
                        self._config[clean_key] = value
