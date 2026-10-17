import functools
import time
from typing import Callable, Any

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results with a size limit."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            if len(cache) >= 1024:
                cache.pop(next(iter(cache)))
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator to yield chunks for efficient memory usage."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator to log execution time for performance tuning."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper