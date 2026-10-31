import functools
from typing import Any, Callable, Dict, List, Optional


class CoreOptimizer:
    """Core execution engine with caching and batched processing."""

    def __init__(self, cache_size: int = 128) -> None:
        self.cache_size = cache_size
        self._stats: Dict[str, int] = {"hits": 0, "misses": 0}

    def memoize(self, func: Callable) -> Callable:
        """Wrap function with LRU cache and runtime stats tracking."""
        cached_func = functools.lru_cache(maxsize=self.cache_size)(func)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            info = cached_func.cache_info()
            res = cached_func(*args, **kwargs)
            new_info = cached_func.cache_info()

            if new_info.hits > info.hits:
                self._stats["hits"] += 1
            else:
                self._stats["misses"] += 1

            return res

        return wrapper

    def batch_process(
        self, items: List[Any], transform: Callable[[Any], Any], chunk_size: int = 50
    ) -> List[Any]:
        """Process dataset in memory-efficient chunks."""
        if not items:
            return []

        results = []
        for i in range(0, len(items), chunk_size):
            chunk = items[i : i + chunk_size]
            results.extend([transform(item) for item in chunk])

        return results

    def get_performance_stats(self) -> Dict[str, Any]:
        """Return current execution metrics and cache efficiency."""
        total = self._stats["hits"] + self._stats["misses"]
        hit_ratio = (self._stats["hits"] / total) if total > 0 else 0.0
        return {
            "hits": self._stats["hits"],
            "misses": self._stats["misses"],
            "total": total,
            "hit_ratio": round(hit_ratio, 4),
        }
