from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class BatchProcessor:
    """A flexible processor for executing batch operations on structured data."""

    def __init__(self, batch_size: int = 100) -> None:
        """Initialize the batch processor with a specified batch size.

        Args:
            batch_size: Number of items to process in each chunk.
        """
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size

    def chunk_data(self, items: List[T]) -> List[List[T]]:
        """Split a list of items into smaller chunks of configured size.

        Args:
            items: The list of elements to be partitioned.

        Returns:
            A list of lists, where each inner list has at most batch_size items.
        """
        return [
            items[i : i + self.batch_size]
            for i in range(0, len(items), self.batch_size)
        ]

    def transform_and_filter(
        self,
        items: List[T],
        transform_fn: Callable[[T], R],
        predicate_fn: Optional[Callable[[R], bool]] = None,
    ) -> List[R]:
        """Transform elements and optionally filter the resulting items.

        Args:
            items: Source items to process.
            transform_fn: Function to map each input item to output type.
            predicate_fn: Optional filter condition evaluated on transformed item.

        Returns:
            A list of transformed and filtered items.
        """
        results: List[R] = []
        for item in items:
            transformed = transform_fn(item)
            if predicate_fn is None or predicate_fn(transformed):
                results.append(transformed)
        return results

    def process_records(
        self, records: List[Dict[str, Any]], key_mapping: Dict[str, str]
    ) -> List[Dict[str, Any]]:
        """Remap keys in a list of dictionary records using a key map.

        Args:
            records: List of raw input dictionaries.
            key_mapping: Map specifying old key names to new key names.

        Returns:
            List of processed dictionaries with updated keys.
        """
        processed: List[Dict[str, Any]] = []
        for record in records:
            new_record = {
                key_mapping.get(k, k): v for k, v in record.items()
            }
            processed.append(new_record)
        return processed
