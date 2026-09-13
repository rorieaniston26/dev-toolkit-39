import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Operation failed after {max_attempts} attempts: {e}")
                        raise
                    
                    sleep_time = delay * (2 ** (attempts - 1))
                    logger.warning(f"Attempt {attempts} failed, retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=2.0)
def fetch_data(url: str) -> dict:
    """Example function for fetching remote network resources."""
    # Simulation of a network call logic
    import random
    if random.random() < 0.7:
        raise ConnectionError("Service unavailable")
    return {"status": "success", "data": "sample payload"}