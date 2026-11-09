import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    loads json config with fallback to defaults
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

def save_config(filepath: str, data: Dict[str, Any]) -> None:
    """
    persists dict to json file
    """
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)