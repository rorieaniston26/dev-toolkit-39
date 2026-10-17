import functools
from typing import Callable, Any
import time

def memoize_with_ttl(ttl: int = 300):
    """Decorator for function result caching with expiration"""
    def decorator(func: Callable):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 100):
    """Generator to yield chunks for memory efficient iteration"""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def optimized_join(items: list[str]) -> str:
    """High performance string concatenation using join method"""
    return ''.join(items)

class PerformanceTracker:
    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"Execution duration: {elapsed:.4f} seconds")