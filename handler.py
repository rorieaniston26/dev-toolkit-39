import functools
from typing import Callable, Any, Dict

# global cache for intensive computation results
_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """decorator for performance boost via result caching"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

class DataHandler:
    def __init__(self, data_stream: list):
        self.data = data_stream

    @memoize
    def process_heavy_batch(self, factor: int) -> list:
        """simulates expensive calculation with batch processing"""
        return [x * factor for x in self.data if x % 2 == 0]

    def clear_cache(self) -> None:
        """manual memory cleanup for cached objects"""
        _cache.clear()

if __name__ == '__main__':
    handler = DataHandler(list(range(1000)))
    result = handler.process_heavy_batch(2)
    print(f'Processed {len(result)} items successfully')