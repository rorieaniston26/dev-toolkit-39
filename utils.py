import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry_on_failure(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0
) -> Callable:
    """
    Decorator that retries a network-related or fragile operation
    using exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_attempts:
                        logger.error(
                            f"Function '{func.__name__}' failed "
                            f"permanently after {max_attempts} attempts."
                        )
                        raise err
                    
                    logger.warning(
                        f"Attempt {attempt}/{max_attempts} failed: {err}. "
                        f"Retrying in {delay:.2f} seconds..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
            return func(*args, **kwargs)
        return wrapper
    return decorator
