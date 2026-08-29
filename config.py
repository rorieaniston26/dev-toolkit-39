import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Configuration loader that merges defaults with file and env vars."""
    DEFAULTS: Dict[str, Any] = {
        "app_name": "dev-toolkit-39",
        "debug": False,
        "port": 8080,
        "log_level": "INFO",
        "timeout": 30,
        "max_connections": 100,
    }

    def __init__(self, config_file: Optional[str] = None) -> None:
        self.config: Dict[str, Any] = self.DEFAULTS.copy()
        if config_file:
            self._load_file(config_file)
        self._load_env()

    def _load_file(self, config_file: str) -> None:
        if not os.path.isfile(config_file):
            return
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                user_config = json.load(f)
            if isinstance(user_config, dict):
                self.config.update(user_config)
        except Exception:
            pass

    def _load_env(self) -> None:
        for key, default in self.DEFAULTS.items():
            env_var = key.upper()
            if env_var in os.environ:
                value = os.environ[env_var]
                if isinstance(default, bool):
                    self.config[key] = value.lower() in ("true", "1", "yes")
                elif isinstance(default, int):
                    try:
                        self.config[key] = int(value)
                    except ValueError:
                        self.config[key] = default
                else:
                    self.config[key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def update(self, new_config: Dict[str, Any]) -> None:
        self.config.update(new_config)

    def as_dict(self) -> Dict[str, Any]:
        return self.config.copy()