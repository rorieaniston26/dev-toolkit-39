import concurrent.futures
from functools import lru_cache
from typing import Callable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class PerformanceOptimizer:
    """Provides optimized execution patterns for CPU and I/O bound tasks."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    @staticmethod
    @lru_cache(maxsize=1024)
    def cached_computation(key: str, computational_heavy_func: Callable[[], R]) -> R:
        """Caches results of heavy operations using a unique lookup key."""
        return computational_heavy_func()

    def parallel_map(self, func: Callable[[T], R], items: List[T]) -> List[R]:
        """Executes a function over a list of items in parallel using a thread pool."""
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            return list(executor.map(func, items))

    def batch_process(
        self, func: Callable[[List[T]], List[R]], items: List[T], batch_size: int
    ) -> List[R]:
        """Processes items in optimized batches to reduce overhead."""
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i : i + batch_size]
            results.extend(func(batch))
        return results
