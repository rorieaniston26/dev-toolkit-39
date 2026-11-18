import time
import functools
import logging
from typing import Callable, Any

# Configure basic logger for network events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def retry_operation(retries: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)):
    """
    Decorator to implement exponential backoff retry logic.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=0.5)
def fetch_network_data(url: str):
    """
    Simulated network operation requiring robust connectivity.
    """
    # Actual implementation would use requests or httpx
    logger.info(f"Fetching data from {url}")
    return {"status": 200, "data": "payload"}