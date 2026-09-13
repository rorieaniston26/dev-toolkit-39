import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> None:
    """Writes data to a JSON file with standard formatting."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def get_timestamp() -> str:
    """Returns an ISO formatted current timestamp string."""
    return datetime.utcnow().isoformat()

def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Accesses nested dictionary keys safely without exceptions."""
    return data.get(key, default)

def ensure_directory(path: str) -> None:
    """Creates a directory structure if it missing."""
    if not os.path.exists(path):
        os.makedirs(path)

class DataFormatter:
    """Static utility class for common string manipulations."""
    @staticmethod
    def clean_string(value: str) -> str:
        return str(value).strip().lower()