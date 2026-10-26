import time
import functools
import logging

# Configure basic logger for network events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def retry_operation(max_attempts=3, delay=2, exceptions=(Exception,)):
    """
    Decorator to retry network operations upon failure.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}, retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=1)
def fetch_data(url):
    """
    Example function demonstrating decorated network logic.
    """
    # Simulating a network call that might fail
    import random
    if random.random() < 0.7:
        raise ConnectionError("Service unavailable")
    return {"status": "success", "url": url}