import json
import os
import time
from typing import Any, Optional

def read_json(filepath: str) -> dict:
    """Load and parse a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(data: dict, filepath: str) -> None:
    """Write a dictionary to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def retry_operation(func, retries: int = 3, delay: float = 1.0) -> Any:
    """Execute a function with simple retry logic."""
    last_exception = None
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            time.sleep(delay * (2 ** i))
    raise last_exception

def format_byte_size(size_bytes: int) -> str:
    """Convert integer bytes into human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"