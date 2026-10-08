import json
from datetime import datetime
from typing import Any, Dict, List, Optional

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def format_timestamp(ts: float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Converts epoch time to readable string."""
    return datetime.fromtimestamp(ts).strftime(fmt)

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller sub-lists."""
    return [items[i:i + size] for i in range(0, len(items), size)]

def safe_json_load(content: str) -> Dict[str, Any]:
    """Safely parses JSON string with fallback."""
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return {}

def flatten_keys(data: Dict[str, Any], prefix: str = "") -> Dict[str, Any]:
    """Flattens nested dictionary keys with underscores."""
    items = {}
    for k, v in data.items():
        new_key = f"{prefix}_{k}" if prefix else k
        if isinstance(v, dict):
            items.update(flatten_keys(v, new_key))
        else:
            items[new_key] = v
    return items