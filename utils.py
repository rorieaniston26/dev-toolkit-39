import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=1, exceptions=(Exception,)):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation failed after {retries} attempts")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2)
def fetch_data(url):
    """Mock network call for demonstration purposes."""
    # Example implementation of network operation
    return {"status": "success", "url": url}