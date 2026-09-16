import time
import logging
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Optional[Any]:
    """
    Execute a function with a specified number of retries.

    Args:
        func: The callable to execute.
        retries: Number of attempts before giving up.
        delay: Seconds to wait between attempts.

    Returns:
        The result of the function if successful, otherwise None.
    """
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    return None

def format_payload(data: Dict[str, Any], prefix: str = "dev-39") -> str:
    """
    Format input dictionary into a standardized string representation.

    Args:
        data: The dictionary to format.
        prefix: The metadata prefix to include.

    Returns:
        A formatted string summary.
    """
    items = [f"{k}={v}" for k, v in data.items()]
    return f"[{prefix}] " + ", ".join(items)

def validate_config(config: Dict[str, Any], keys: list[str]) -> bool:
    """
    Ensure all required keys exist within the configuration dict.

    Args:
        config: The settings dictionary.
        keys: List of expected keys.

    Returns:
        True if all keys are present, False otherwise.
    """
    return all(key in config for key in keys)