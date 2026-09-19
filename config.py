import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "DevToolkit",
    "version": "1.0.0",
    "debug": False,
    "port": 8080,
    "host": "127.0.0.1",
    "log_level": "INFO",
}


class ConfigLoader:
    """Loads application configurations with default fallback support."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults.copy() if defaults else DEFAULT_CONFIG.copy()

    def load_from_dict(self, overrides: Dict[str, Any]) -> Dict[str, Any]:
        """Merge custom dictionary values over default configurations."""
        config = self.defaults.copy()
        config.update(overrides)
        return config

    def load_from_json(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from a JSON file, filling missing keys with defaults."""
        config = self.defaults.copy()
        path = Path(filepath)

        if path.exists() and path.is_file():
            with open(path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    config.update(user_config)
        return config

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Override configuration options using matching environment variables."""
        config = self.defaults.copy()
        for key in config.keys():
            env_var = f"{prefix}{key.upper()}"
            if env_var in os.environ:
                val = os.environ[env_var]
                if isinstance(config[key], bool):
                    config[key] = val.lower() in ("true", "1", "yes")
                elif isinstance(config[key], int):
                    try:
                        config[key] = int(val)
                    except ValueError:
                        pass
                else:
                    config[key] = val
        return config
