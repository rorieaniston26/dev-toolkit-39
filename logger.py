import logging
import functools
import time
from typing import Callable, Any

# Configure global logger for dev-toolkit-39
logger = logging.getLogger('dev-toolkit')
logger.setLevel(logging.INFO)

# Memoization cache for performance
_cache = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def timer(func: Callable) -> Callable:
    """Decorator to measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.info(f"function {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def clear_cache() -> None:
    """Clear memoization storage to prevent memory leaks."""
    _cache.clear()