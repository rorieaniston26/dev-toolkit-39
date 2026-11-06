import json
import logging
from typing import Any, Dict, Optional

def load_json_file(filepath: str) -> Optional[Dict[str, Any]]:
    """safely load and parse a json file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"failed to load {filepath}: {e}")
        return None

def slugify(text: str) -> str:
    """convert string to url-friendly slug"""
    return "-".join(text.lower().split()).replace(" ", "-")

def chunk_list(data: list, size: int):
    """yield successive n-sized chunks from list"""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_get_nested(data: Dict, path: str, delimiter: str = ".") -> Any:
    """retrieve value from nested dict using dot notation"""
    keys = path.split(delimiter)
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return None