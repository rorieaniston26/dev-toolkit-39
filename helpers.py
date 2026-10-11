"""General utility helper functions for common operations."""

import time
from typing import Any, Callable, List, TypeVar

T = TypeVar("T")


def chunk_list(data: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]


def deep_merge(dict1: dict, dict2: dict) -> dict:
    """Recursively merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def safe_cast(val: Any, to_type: type, default: Any = None) -> Any:
    """Safely cast a value to a target type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry a function if it raises an exception."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(delay)

        return wrapper

    return decorator
