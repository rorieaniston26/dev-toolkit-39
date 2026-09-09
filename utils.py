import time
import functools
import random
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, backoff_factor=1.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise
                    
                    wait_time = backoff_factor * (2 ** (attempts - 1)) + random.uniform(0, 1)
                    logger.warning(f"Retry {attempts}/{max_attempts} after {wait_time:.2f}s due to: {e}")
                    time.sleep(wait_time)
            return None
        return wrapper
    return decorator