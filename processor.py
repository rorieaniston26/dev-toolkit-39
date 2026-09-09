import functools
import time
from typing import Callable, Any, Dict

# global cache for memoization of expensive computations
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

class DataProcessor:
    """Core processor for heavy data transformations."""
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    @memoize
    def compute_heavy_metric(self, value: int) -> int:
        """Simulate complex CPU-bound calculation."""
        time.sleep(0.1)
        return value * value

    def process_batch(self, data: list[int]) -> list[int]:
        """Execute batch processing with generator expression."""
        return [self.compute_heavy_metric(x) for x in data]

    def clear_cache(self) -> None:
        """Manual cache invalidation for memory management."""
        _CACHE.clear()