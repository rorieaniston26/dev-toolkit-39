import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "DevToolkit",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "max_workers": 4,
    "cache": {
        "enabled": True,
        "ttl": 3600,
        "directory": ".cache"
    }
}


class ConfigLoader:
    """Loads and merges configuration settings from JSON files and environment variables."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = (default_config or DEFAULT_CONFIG).copy()

    def load_from_file(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration options from a JSON file and merge with defaults."""
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with path.open("r", encoding="utf-8") as file:
            file_config = json.load(file)

        self._deep_update(self._config, file_config)
        return self._config

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Override configuration settings using environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                if value.lower() in ("true", "false"):
                    parsed_val: Any = value.lower() == "true"
                elif value.isdigit():
                    parsed_val = int(value)
                else:
                    parsed_val = value
                self._config[config_key] = parsed_val
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value using dot notation for nested keys."""
        parts = key.split(".")
        current = self._config
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
        return current

    def _deep_update(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Recursively update nested dictionaries."""
        for key, val in source.items():
            if isinstance(val, dict) and key in target and isinstance(target[key], dict):
                self._deep_update(target[key], val)
            else:
                target[key] = val
