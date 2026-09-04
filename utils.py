import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(max_retries: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)): 
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {retries} failed, retrying in {current_delay}s: {e}")
                    time.sleep(current_delay)
                    current_delay *= 2
            return None
        return wrapper
    return decorator