import functools
import time
from typing import Callable, Any, Dict

def memoize(func: Callable) -> Callable:
    """Cache function results based on arguments for performance."""
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Generator for efficient chunking of large datasets."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

class PerformanceTimer:
    """Context manager for tracking execution duration."""
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.duration = self.end - self.start