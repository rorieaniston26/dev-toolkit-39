"""Data processing engine for running sequential transformations."""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class ProcessingContext:
    """Holds metadata and state for a single processing run."""
    run_id: str
    strict_mode: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)


class DataProcessor:
    """Manages ordered pipeline steps and executes data transformations."""

    def __init__(self, context: ProcessingContext) -> None:
        self.context = context
        self._steps: List[Callable[[Any], Any]] = []

    def register_step(self, func: Callable[[Any], Any]) -> None:
        """Add a processing step to the execution pipeline."""
        if not callable(func):
            raise TypeError("Pipeline step must be a callable function")
        self._steps.append(func)

    def process_item(self, item: Any) -> Optional[Any]:
        """Pass an item through all registered processing steps."""
        current_data = item
        for step in self._steps:
            try:
                current_data = step(current_data)
            except Exception as err:
                msg = f"Error in step '{step.__name__}': {err}"
                self.context.errors.append(msg)
                if self.context.strict_mode:
                    raise RuntimeError(msg) from err
                return None
        return current_data

    def process_batch(self, items: List[Any]) -> List[Any]:
        """Process a list of items, returning successful transformations."""
        results = []
        for item in items:
            processed = self.process_item(item)
            if processed is not None:
                results.append(processed)
        return results