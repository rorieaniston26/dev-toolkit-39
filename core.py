"""Core processing engine with optimized batch operation capabilities."""

import hashlib
from functools import lru_cache
from typing import Any, Callable, Dict, Iterable, List, Sequence


@lru_cache(maxsize=1024)
def _compute_hash(data_str: str) -> str:
    """Fast memoized hash computation helper for string tokens."""
    return hashlib.sha256(data_str.encode("utf-8")).hexdigest()


class CoreProcessor:
    """High-performance batch processing context with internal cache."""

    def __init__(self, batch_size: int = 500) -> None:
        self.batch_size = batch_size
        self._cache: Dict[str, Any] = {}

    def process_stream(self, items: Iterable[Any], transform: Callable[[Any], Any]) -> List[Any]:
        """Process input stream in memory-efficient batches using cached transforms."""
        results = []
        batch = []

        for item in items:
            batch.append(item)
            if len(batch) >= self.batch_size:
                results.extend(self._process_batch(batch, transform))
                batch.clear()

        if batch:
            results.extend(self._process_batch(batch, transform))

        return results

    def _process_batch(self, batch: Sequence[Any], transform: Callable[[Any], Any]) -> List[Any]:
        """Execute transformation on a single batch using lookups."""
        processed = []
        for item in batch:
            cache_key = _compute_hash(str(item))
            if cache_key not in self._cache:
                self._cache[cache_key] = transform(item)
            processed.append(self._cache[cache_key])
        return processed

    def clear_cache(self) -> None:
        """Purge in-memory processing cache."""
        self._cache.clear()
        _compute_hash.cache_clear()
