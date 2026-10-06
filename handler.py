import json
import os
import time
from typing import Any, Optional

def read_json_file(file_path: str) -> dict:
    """Reads and parses a JSON file with basic error handling."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json_file(data: dict, file_path: str) -> bool:
    """Writes dictionary to a JSON file safely."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env_variable(key: str, default: Optional[Any] = None) -> Any:
    """Retrieves environment variable with fallback default."""
    return os.getenv(key, default)

def timestamped_log(message: str) -> str:
    """Generates a standard string with current timestamp."""
    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return f"[{ts}] {message}"

def batch_process(items: list, chunk_size: int = 10):
    """Generator for processing large lists in chunks."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]