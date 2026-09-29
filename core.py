import time
import functools
import logging

# Configure logging for network operations
logger = logging.getLogger('dev-toolkit-39')

def retry_operation(max_attempts=3, backoff_factor=1.0):
    """
    Decorator for retrying network operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            delay = backoff_factor
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {delay}s...")
                    time.sleep(delay)
                    delay *= 2
            return None
        return wrapper
    return decorator

# Example network operation usage
@retry_operation(max_attempts=3, backoff_factor=2)
def fetch_data(url):
    # Simulate network instability
    logger.info(f"Requesting data from {url}")
    raise ConnectionError("Server unreachable")