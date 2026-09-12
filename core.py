import functools
import time
import logging
from typing import Callable, Any

# Configure performance logger
logger = logging.getLogger('dev-toolkit-39')

CACHE_SIZE = 128

def memoize_with_ttl(ttl_seconds: int = 60) -> Callable:
    """Decorator for caching function results with TTL expiration."""
    def decorator(func: Callable) -> Callable:
        cache = {}

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            now = time.time()

            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            
            # Prevent memory leaks by clearing expired entries
            if len(cache) > CACHE_SIZE:
                expired = [k for k, v in cache.items() if now - v[1] > ttl_seconds]
                for k in expired:
                    del cache[k]
                    
            return result
        return wrapper
    return decorator

@memoize_with_ttl(ttl_seconds=300)
def intensive_computation(data_id: int) -> dict:
    """Simulate resource-heavy data retrieval or processing."""
    time.sleep(1)  # Simulate latency
    return {"id": data_id, "status": "processed", "timestamp": time.time()}