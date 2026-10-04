import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively strips whitespace from string values in dicts or lists."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def safe_json_load(content: str) -> Optional[Dict[str, Any]]:
    """Safely parses JSON strings with basic error recovery."""
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return None

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)