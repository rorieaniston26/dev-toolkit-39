import json
from typing import Any, Dict, Optional

def clean_data(data: Any, strip_strings: bool = True) -> Any:
    """
    Recursively cleans data structures by stripping strings
    and converting empty values to None.
    """
    if isinstance(data, dict):
        return {k: clean_data(v, strip_strings) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [clean_data(item, strip_strings) for item in data]
    elif isinstance(data, str) and strip_strings:
        cleaned = data.strip()
        return cleaned if cleaned else None
    return data

def safe_load_json(file_path: str) -> Optional[Dict]:
    """
    Safely attempts to load and parse a JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return None

def format_byte_size(size_bytes: int) -> str:
    """
    Human readable byte formatting utility.
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"