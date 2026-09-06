import time
from typing import Generator, Iterable, Any, TypeVar

T = TypeVar('T')

def batch_processor(iterable: Iterable[T], batch_size: int) -> Generator[list[T], None, None]:
    """
    Yields successive batches of the specified size from the iterable.
    Optimized to minimize memory footprint and handle lazy generators efficiently.
    """
    if batch_size <= 0:
        raise ValueError("Batch size must be greater than zero.")
    
    iterator = iter(iterable)
    while True:
        batch = []
        try:
            for _ in range(batch_size):
                batch.append(next(iterator))
            yield batch
        except StopIteration:
            if batch:
                yield batch
            break

class MemoizeWithTimeout:
    """
    Decorator to cache function results with a time-to-live (TTL).
    Optimizes performance by avoiding redundant database or API calls.
    """
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self.cache: dict[tuple[Any, ...], tuple[float, Any]] = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in self.cache:
                timestamp, val = self.cache[key]
                if now - timestamp < self.ttl:
                    return val
            
            result = func(*args, **kwargs)
            self.cache[key] = (now, result)
            return result
        return wrapper