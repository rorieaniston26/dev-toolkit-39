import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Manages application configuration with fallback defaults."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._defaults = defaults or {}
        self._config: Dict[str, Any] = self._defaults.copy()

    def load_file(self, filepath: Union[str, Path], merge: bool = True) -> Dict[str, Any]:
        """Loads configuration from a JSON file."""
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with open(path, "r", encoding="utf-8") as f:
            file_data = json.load(f)

        if merge:
            self._config.update(file_data)
        else:
            self._config = {**self._defaults, **file_data}

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key with optional default override."""
        return self._config.get(key, self._defaults.get(key, default))

    def get_env(self, key: str, env_var: str, default: Any = None) -> Any:
        """Retrieves config value, falling back to environment variable, then default."""
        if key in self._config:
            return self._config[key]
        return os.getenv(env_var, self._defaults.get(key, default))

    def reset(self) -> None:
        """Resets the configuration back to initial defaults."""
        self._config = self._defaults.copy()
