import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively removes null values from nested dictionaries."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    return data

def safe_json_parse(json_str: str, default: Optional[Dict] = None) -> Any:
    """Parses json string with fallback to default dictionary."""
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default if default is not None else {}

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)