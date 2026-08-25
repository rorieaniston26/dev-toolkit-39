import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """A simple configuration loader that supports defaults, file loading, and env vars."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with default configuration values."""
        self.defaults: Dict[str, Any] = defaults or {}
        self.config: Dict[str, Any] = self.defaults.copy()

    def load(self, config_path: Optional[str] = None, env_prefix: str = "") -> Dict[str, Any]:
        """Load configuration merging file and environment over defaults."""
        if config_path:
            self._load_from_json(config_path)
        if env_prefix:
            self._load_from_environment(env_prefix)
        return self.config.copy()

    def _load_from_json(self, path: str) -> None:
        """Load and merge configuration from a JSON file if it exists."""
        if not os.path.isfile(path):
            return
        try:
            with open(path, "r", encoding="utf-8") as file:
                file_config: Dict[str, Any] = json.load(file)
            if isinstance(file_config, dict):
                self.config.update(file_config)
        except (IOError, json.JSONDecodeError) as error:
            print(f"Config load warning for {path}: {error}")

    def _load_from_environment(self, prefix: str) -> None:
        """Override config with environment variables matching the prefix."""
        for env_key, env_value in os.environ.items():
            if env_key.startswith(prefix):
                config_key = env_key[len(prefix):].lower()
                if env_value.lower() in ("true", "false"):
                    self.config[config_key] = env_value.lower() == "true"
                else:
                    try:
                        self.config[config_key] = int(env_value)
                    except ValueError:
                        self.config[config_key] = env_value

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieve a config value or fallback."""
        return self.config.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        """Allow dict-like access to config."""
        return self.config[key]

if __name__ == "__main__":
    default_settings = {
        "app_name": "MyApp",
        "port": 3000,
        "debug": False,
        "host": "127.0.0.1"
    }
    loader = ConfigLoader(default_settings)
    loaded_config = loader.load()
    print("Loaded config:", loaded_config)
    print("Port value:", loader.get("port"))
