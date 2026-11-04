import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "DevToolkit",
    "environment": "development",
    "debug": True,
    "log_level": "INFO",
    "max_workers": 4,
    "timeout": 30.0,
}


class ConfigLoader:
    """Loads and manages application configuration with default fallback values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = (
            defaults.copy() if defaults is not None else DEFAULT_CONFIG.copy()
        )

    def load_from_json(self, filepath: Union[str, Path]) -> bool:
        """Merge configuration settings from a JSON file if it exists."""
        path = Path(filepath)
        if not path.is_file():
            return False

        with open(path, "r", encoding="utf-8") as f:
            file_data = json.load(f)
            if isinstance(file_data, dict):
                self._config.update(file_data)
                return True
        return False

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Override configuration values using environment variables with matching prefix."""
        for key, default_val in list(self._config.items()):
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                if isinstance(default_val, bool):
                    self._config[key] = raw_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    self._config[key] = int(raw_val)
                elif isinstance(default_val, float):
                    self._config[key] = float(raw_val)
                else:
                    self._config[key] = raw_val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Return a dictionary copy of current configuration."""
        return self._config.copy()
