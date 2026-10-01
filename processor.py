from typing import Any, Dict, List, Optional

def sanitize_data(data: Any, keys_to_mask: Optional[List[str]] = None) -> Any:
    """Recursively cleans dictionary data and masks sensitive keys."""
    if not isinstance(data, dict):
        return data

    masked_keys = set(keys_to_mask or ['password', 'secret', 'token'])
    cleaned = {}

    for key, value in data.items():
        if key in masked_keys:
            cleaned[key] = '********'
        elif isinstance(value, dict):
            cleaned[key] = sanitize_data(value, keys_to_mask)
        elif isinstance(value, list):
            cleaned[key] = [sanitize_data(i, keys_to_mask) if isinstance(i, dict) else i for i in value]
        else:
            cleaned[key] = value
            
    return cleaned

def batch_process(items: List[Any], func: callable, batch_size: int = 10) -> List[Any]:
    """Applies a function to a list in defined batch sizes."""
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        results.extend([func(item) for item in batch])
    return results