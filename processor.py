from typing import Any, List, Dict, Optional
import json

def clean_nested_data(data: Any) -> Any:
    """Recursively removes null values from dictionaries and lists."""
    if isinstance(data, dict):
        return {
            k: clean_nested_data(v) 
            for k, v in data.items() 
            if v is not None
        }
    elif isinstance(data, list):
        return [clean_nested_data(item) for item in data if item is not None]
    return data

def safe_json_load(content: str) -> Optional[Dict[str, Any]]:
    """Parses json string into dictionary with basic error handling."""
    try:
        parsed = json.loads(content)
        return parsed if isinstance(parsed, dict) else None
    except (json.JSONDecodeError, TypeError):
        return None

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks for batch processing."""
    if size <= 0:
        return [data]
    return [data[i:i + size] for i in range(0, len(data), size)]