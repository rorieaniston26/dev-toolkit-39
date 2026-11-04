import json
import os
from typing import Any, Optional

def load_json(filepath: str) -> dict:
    """Reads and parses a json configuration file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: dict) -> None:
    """Writes a dictionary to a json file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_directory(path: str) -> None:
    """Creates directory structure if missing."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieves environment variable with default fallback."""
    return os.getenv(key, default)

def format_byte_size(size_bytes: int) -> str:
    """Converts bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"