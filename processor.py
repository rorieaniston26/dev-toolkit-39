import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """
    Recursively sanitize dictionaries to remove null values
    and normalize key formats for downstream consumption.
    """
    if isinstance(data, dict):
        return {
            str(k).lower().replace(' ', '_'): clean_data(v)
            for k, v in data.items()
            if v is not None
        }
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    return data

def safe_json_load(json_string: str) -> Optional[Dict[str, Any]]:
    """
    Attempt to parse string into dictionary,
    returning None if parsing fails.
    """
    try:
        parsed = json.loads(json_string)
        return clean_data(parsed) if isinstance(parsed, dict) else None
    except (json.JSONDecodeError, TypeError):
        return None

def batch_process(items: list, processor_func: callable) -> list:
    """
    Utility to apply a function over a list
    with basic error suppression for robustness.
    """
    results = []
    for item in items:
        try:
            results.append(processor_func(item))
        except Exception:
            continue
    return results