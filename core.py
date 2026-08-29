import functools
from typing import List

class CoreModule:
    """Core processing module with performance optimizations applied."""

    @functools.lru_cache(maxsize=256)
    def heavy_calculation(self, value: int) -> int:
        """Perform expensive calculation with automatic caching.
        Caching avoids recomputation for repeated values.
        """

        if value < 0:
            return 0
        result = 0
        for i in range(value + 1):
            result += i ** 2
        return result

    def batch_process(self, items: List[int]) -> List[int]:
        """Process list of items using cached heavy calculation."""

        processed = []
        for item in items:
            processed.append(self.heavy_calculation(item))
        return processed

    def aggregate_data(self, datasets: List[List[int]]) -> int:
        """Aggregate multiple datasets using generator expression.
        Generator provides memory efficiency for large datasets.
        """

        return sum(
            self.heavy_calculation(sum(dataset)) for dataset in datasets
        )

if __name__ == "__main__":
    core = CoreModule()
    test_data = [10, 20, 30, 10, 20]
    print(core.batch_process(test_data))
    multi_data = [[1, 2], [3, 4, 5], [100]]
    print(core.aggregate_data(multi_data))