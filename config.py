import json
import os
from pathlib import Path
from typing import Any, Dict, Optional


class ConfigLoader:
    """Manages application configuration with nested defaults and env overrides."""

    DEFAULT_CONFIG: Dict[str, Any] = {
        "app_name": "DevToolkit",
        "debug": False,
        "log_level": "INFO",
        "server": {
            "host": "127.0.0.1",
            "port": 8080,
            "timeout": 30,
        },
        "features": {
            "auto_reload": True,
            "caching": False,
        },
    }

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = json.loads(json.dumps(self.DEFAULT_CONFIG))
        self.load()

    def _deep_update(self, base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively updates base dictionary with values from updates."""
        for key, value in updates.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._deep_update(base[key], value)
            else:
                base[key] = value
        return base

    def load(self) -> Dict[str, Any]:
        """Loads configuration from JSON file if provided and accessible."""
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self._deep_update(self._config, file_config)
            except (json.JSONDecodeError, IOError) as err:
                print(f"Warning: Failed to load config file ({err}). Using defaults.")

        self._apply_env_overrides()
        return self._config

    def _apply_env_overrides(self) -> None:
        """Applies environment variable overrides using PREFIX_KEY syntax."""
        prefix = "APP_"
        for env_key, value in os.environ.items():
            if env_key.startswith(prefix):
                key = env_key[len(prefix):].lower()
                if key in self._config:
                    if isinstance(self._config[key], bool):
                        self._config[key] = value.lower() in ("true", "1", "yes")
                    elif isinstance(self._config[key], int):
                        self._config[key] = int(value)
                    else:
                        self._config[key] = value

    def get(self, key_path: str, default: Any = None) -> Any:
        """Retrieves a configuration value using dot-notation (e.g., 'server.port')."""
        keys = key_path.split(".")
        val = self._config
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return default
        return val
