import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    """
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            config.update(data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

# Example usage:
if __name__ == '__main__':
    default_settings = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    
    # Load config file if it exists, otherwise return defaults
    final_cfg = load_config('settings.json', default_settings)
    print(f"Active configuration: {final_cfg}")