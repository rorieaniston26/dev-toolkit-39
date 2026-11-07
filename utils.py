import time
import functools
import logging

# Configure basic logger for network ops
logger = logging.getLogger('dev-toolkit-39')

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    """
    Decorator for retrying functions on exception.
    
    Args:
        max_retries: Total retry attempts
        delay: Initial wait time in seconds
        backoff: Multiplier for delay after each fail
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        logger.error(f"Failed after {max_retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator