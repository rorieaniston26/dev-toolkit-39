import json
import os
from typing import Any, Optional

def load_json(path: str) -> dict:
    """load and parse a json file from disk"""
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def save_json(data: dict, path: str) -> bool:
    """serialize dictionary to a json file"""
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env(key: str, default: Optional[Any] = None) -> Any:
    """fetch environment variable with fallback"""
    return os.environ.get(key, default)

def sanitize_path(path: str) -> str:
    """remove potential path traversal sequences"""
    return path.replace('..', '').lstrip('/')

def chunk_list(data: list, size: int):
    """generator for splitting lists into chunks"""
    for i in range(0, len(data), size):
        yield data[i:i + size]