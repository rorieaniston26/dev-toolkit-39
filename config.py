import json
import os
from typing import Any, Dict, Optional

# Configuration loader with defaults support using JSON files
class ConfigLoader:
    """A practical configuration loader that starts with defaults and merges from JSON file."""

    def __init__(self, defaults: Dict[str, Any], config_path: Optional[str] = None) -> None:
        """Initialize the loader with defaults and load overrides if file exists."""
        self._config: Dict[str, Any] = defaults.copy()
        if config_path and os.path.isfile(config_path):
            self._load_from_file(config_path)

    def _load_from_file(self, config_path: str) -> None:
        """Attempt to load and merge JSON config from the given path."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                file_config = json.load(f)
            if isinstance(file_config, dict):
                self._merge(self._config, file_config)
        except (json.JSONDecodeError, IOError, OSError) as e:
            print(f"Warning: Could not load config from {config_path}: {e}")

    def _merge(self, base: Dict[str, Any], updates: Dict[str, Any]) -> None:
        """Recursively merge updates into base, handling nested dicts."""
        for key, value in updates.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get value for key, supporting dot notation for nested access."""
        keys = key.split('.')
        current = self._config
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        return current

    def get_all(self) -> Dict[str, Any]:
        """Return a shallow copy of the entire config dictionary."""
        return self._config.copy()

    def update(self, updates: Dict[str, Any]) -> None:
        """Merge additional updates into the current configuration."""
        self._merge(self._config, updates)

    def save(self, path: str) -> bool:
        """Write the current config to a JSON file, return success status."""
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2)
            return True
        except (IOError, OSError) as e:
            print(f"Warning: Failed to save config to {path}: {e}")
            return False
