from typing import List, Dict, Any, Optional
import json
import os

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from the filesystem.

    Args:
        file_path: The absolute or relative path to the json file.

    Returns:
        A dictionary containing the parsed file contents.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file content is not valid JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def format_data_list(items: List[Any], prefix: str = "Item") -> List[str]:
    """Converts a list of items into a formatted string list.

    Args:
        items: A list of objects to format.
        prefix: A string to prepend to each item.

    Returns:
        A list of formatted strings.
    """
    return [f"{prefix}: {str(item)}" for item in items]

def sanitize_input(data: Optional[str]) -> str:
    """Cleans input string by stripping whitespace and empty chars.

    Args:
        data: The raw input string, potentially None.

    Returns:
        A sanitized string, defaulting to an empty string if input is None.
    """
    if data is None:
        return ""
    return data.strip()