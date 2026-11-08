import functools
from typing import Callable, Any, Dict
import time

# Cache to store expensive function computations
_performance_cache: Dict[str, Any] = {}

def memoize_compute(func: Callable) -> Callable:
    """Decorator for caching results of heavy operations"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _performance_cache:
            _performance_cache[key] = func(*args, **kwargs)
        return _performance_cache[key]
    return wrapper

class DataProcessor:
    """Core processor with optimized lookup capabilities"""
    def __init__(self, data_stream: list):
        self._stream = data_stream

    @memoize_compute
    def calculate_heavy_metric(self, threshold: int) -> float:
        """Simulates complex calculation with caching"""
        time.sleep(0.1)
        return sum(x for x in self._stream if x > threshold) / len(self._stream)

    def batch_process(self, thresholds: list) -> list:
        """Efficient iteration over metric thresholds"""
        results = []
        for t in thresholds:
            results.append(self.calculate_heavy_metric(t))
        return results