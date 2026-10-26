import os
import json
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigManager:
    """Manages application configuration loading and environment overrides."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None) -> None:
        """Initialize config manager with an optional default configuration dictionary."""
        self._config: Dict[str, Any] = default_config or {}

    def load_from_json(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration settings from a JSON file into the manager."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")

        with open(path, "r", encoding="utf-8") as file:
            data: Dict[str, Any] = json.load(file)

        self._config.update(data)
        return self._config

    def apply_env_overrides(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Override configuration values with matching environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = self._parse_env_value(value)
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key with an optional fallback."""
        return self._config.get(key, default)

    @staticmethod
    def _parse_env_value(value: str) -> Union[int, float, bool, str]:
        """Parse string environment values into appropriate Python types."""
        val_lower = value.lower()
        if val_lower in ("true", "1", "yes"):
            return True
        if val_lower in ("false", "0", "no"):
            return False

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            pass

        return value
