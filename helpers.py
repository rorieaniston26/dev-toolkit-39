import json
from typing import Any, Callable, Dict, List, Optional

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file into a dictionary.
    This function reads the specified file and parses its content as JSON.
    Args:
        filepath: The path to the JSON file to load.
    Returns:
        A dictionary containing the parsed JSON data.
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Save a dictionary as a JSON file.
    Args:
        filepath: Path where to save the JSON file.
        data: Dictionary to serialize and save.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries where override takes precedence.
    Performs a shallow merge of the dictionaries.
    Args:
        base: The base dictionary.
        override: The dictionary with values to override.
    Returns:
        A new dictionary with merged contents.
    """
    result = base.copy()
    result.update(override)
    return result

def filter_items(items: List[Any], predicate: Callable[[Any], bool]) -> List[Any]:
    """Filter a list of items using a predicate function.
    Args:
        items: The list of items to filter.
        predicate: A function that takes an item and returns True to keep it.
    Returns:
        A new list containing only items where predicate returned True.
    """
    return [item for item in items if predicate(item)]

def safe_dict_get(data: Dict[str, Any], key: str, default: Optional[Any] = None) -> Any:
    """Get a value from a dictionary safely, returning default if missing.
    Args:
        data: The dictionary to retrieve from.
        key: The key to look up.
        default: The value to return if the key is not present.
    Returns:
        The value associated with the key or the default.
    """
    return data.get(key, default)

def group_by(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    """Group a list of dictionaries by a specified key.
    Args:
        data: List of dictionaries to group.
        key: The key to group the dictionaries by.
    Returns:
        A dictionary mapping group keys to lists of matching dictionaries.
    """
    # Initialize the groups dictionary
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for item in data:
        # Get the group key, default to 'unknown' if missing
        group_key: str = str(item.get(key, 'unknown'))
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(item)
    return groups