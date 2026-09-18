import time
import functools
import logging
from typing import Callable, Any

# Configure logger for toolkit operations
logger = logging.getLogger('dev-toolkit-39')

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            local_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}, retrying in {local_delay}s")
                    time.sleep(local_delay)
                    local_delay *= backoff
        return wrapper
    return decorator

@with_retry(retries=3, delay=2.0)
def fetch_network_resource(url: str):
    """Example usage of network operation retry logic."""
    import requests
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()