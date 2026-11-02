import json
import os
import time
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: Dict[str, Any], file_path: str) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def retry_operation(func, retries: int = 3, delay: int = 1):
    """Retries a function call upon failure."""
    last_exception = None
    for _ in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            time.sleep(delay)
    raise last_exception

def format_timestamp(ts: Optional[float] = None) -> str:
    """Returns human-readable time string."""
    import datetime
    dt = datetime.datetime.fromtimestamp(ts or time.time())
    return dt.strftime('%Y-%m-%d %H:%M:%S')