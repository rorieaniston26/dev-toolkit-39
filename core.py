import json
import os
import time
from typing import Any, Dict, Optional

def load_json(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """Serializes data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_timestamp() -> str:
    """Generates a standard ISO formatted timestamp."""
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)