import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(max_retries: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)): 
    """Decorator for retrying network-based operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            current_delay = delay
            
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(f"Max retries reached for {func.__name__}")
                        raise
                    
                    logger.warning(f"Retry {retries}/{max_retries} for {func.__name__} after {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= 2
            return None
        return wrapper
    return decorator