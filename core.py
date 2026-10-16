import json
import os
from typing import Any, Dict, Optional

def load_json(path: str) -> Dict[str, Any]:
    """Reads and parses a json file from disk."""
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path: str, data: Dict[str, Any]) -> None:
    """Serializes data to a formatted json file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback default."""
    return os.environ.get(key, default) or ''

def chunk_list(data: list, size: int):
    """Generator for splitting lists into smaller segments."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_path(path: str) -> str:
    """Removes potential traversal characters from string paths."""
    return path.replace('..', '').lstrip('/\\')