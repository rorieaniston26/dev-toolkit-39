import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries=3, delay=1.0, backoff=2):
    """Decorator to retry a function if an exception occurs during execution."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_operation(max_retries=3)
def fetch_data(url):
    """Example network operation function."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Temporary server timeout")
    return {"status": "success", "data": "sample payload"}