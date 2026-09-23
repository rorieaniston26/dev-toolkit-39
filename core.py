from functools import lru_cache
from typing import Any, Dict, List, Sequence, Tuple


class CoreExecutionEngine:
    """Core execution engine optimized with memoization and batch processing."""

    def __init__(self, cache_size: int = 1024, batch_size: int = 100):
        self.cache_size = cache_size
        self.batch_size = batch_size
        self._stats = {"processed": 0}

    @lru_cache(maxsize=1024)
    def _compute_cached(self, key: str, payload: Tuple[Any, ...]) -> int:
        """Perform memory-heavy transformations with LRU cache acceleration."""
        return hash((key, payload)) ^ 0x5F3759DF

    def process_item(self, key: str, data: Any) -> Dict[str, Any]:
        """Process a single item using memoized result evaluation."""
        payload = (data,) if not isinstance(data, tuple) else data
        cached_result = self._compute_cached(key, payload)
        self._stats["processed"] += 1

        return {"key": key, "result": cached_result, "status": "success"}

    def batch_process(self, items: Sequence[Tuple[str, Any]]) -> List[Dict[str, Any]]:
        """Process a collection of items in optimized batch chunks."""
        results = []
        for i in range(0, len(items), self.batch_size):
            chunk = items[i : i + self.batch_size]
            chunk_results = [self.process_item(key, data) for key, data in chunk]
            results.extend(chunk_results)
        return results

    def get_performance_stats(self) -> Dict[str, Any]:
        """Retrieve engine execution metrics and cache efficiency stats."""
        cache_info = self._compute_cached.cache_info()
        return {
            "total_processed": self._stats["processed"],
            "cache_hits": cache_info.hits,
            "cache_misses": cache_info.misses,
            "cache_currsize": cache_info.currsize,
        }

    def clear_cache(self) -> None:
        """Reset cache state and engine counter metrics."""
        self._compute_cached.cache_clear()
        self._stats["processed"] = 0
