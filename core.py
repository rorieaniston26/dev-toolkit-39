from typing import List, Dict, Optional, Any
import time

class TaskProcessor:
    """Handles execution of batch processing tasks."""

    def __init__(self, timeout: int = 30) -> None:
        self.timeout: int = timeout
        self.registry: Dict[str, Any] = {}

    def register_task(self, name: str, func: callable) -> None:
        """Registers a task function to the processor."""
        self.registry[name] = func

    def execute_all(self, tasks: List[str]) -> Dict[str, Any]:
        """Runs all registered tasks and returns results mapping."""
        results: Dict[str, Any] = {}
        start_time: float = time.time()

        for task_name in tasks:
            if task_name in self.registry:
                if time.time() - start_time > self.timeout:
                    break
                results[task_name] = self.registry[task_name]()
            else:
                results[task_name] = None
        
        return results

def get_system_status(data: Optional[List[int]] = None) -> str:
    """Calculates basic system status string."""
    if not data:
        return "idle"
    return f"active: {len(data)} items"