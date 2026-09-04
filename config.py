import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with provided fallback defaults."""
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def get_env_config(key: str, default: Any) -> Any:
    """Retrieves configuration from environment variables."""
    return os.environ.get(key, default)

if __name__ == '__main__':
    # Example usage for dev-toolkit-39
    base_defaults = {"host": "localhost", "port": 8080, "debug": False}
    final_cfg = load_config("settings.json", base_defaults)
    print(f"Config loaded: {final_cfg}")