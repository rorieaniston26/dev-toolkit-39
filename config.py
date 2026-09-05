import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """A practical configuration loader supporting default fallback values."""

    def __init__(self, filepath: str, defaults: Optional[Dict[str, Any]] = None):
        self.filepath = filepath
        self.defaults = defaults or {}
        self.config = self.defaults.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads config from JSON file, merging missing keys from defaults."""
        if not os.path.exists(self.filepath):
            self.save()
            return self.config

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                if isinstance(loaded_data, dict):
                    # Merge defaults with loaded values
                    merged = self.defaults.copy()
                    merged.update(loaded_data)
                    self.config = merged
                else:
                    self.config = self.defaults.copy()
        except (json.JSONDecodeError, IOError):
            # Soft fallback to defaults in case of corruption or read error
            self.config = self.defaults.copy()

        return self.config

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieves a value by key, falling back if not found."""
        return self.config.get(key, fallback)

    def set(self, key: str, value: Any) -> None:
        """Updates a configuration value locally."""
        self.config[key] = value

    def save(self) -> None:
        """Persists the current configuration state to disk."""
        try:
            directory = os.path.dirname(os.path.abspath(self.filepath))
            if directory:
                os.makedirs(directory, exist_ok=True)
            
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write configuration file: {e}")
