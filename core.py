from typing import List, Dict, Optional, Any
import time

class TaskProcessor:
    """Handles execution of queued development tasks."""

    def __init__(self, buffer_size: int = 10) -> None:
        self.buffer: List[Dict[str, Any]] = []
        self.buffer_size: int = buffer_size

    def add_task(self, name: str, priority: int = 1) -> bool:
        """Adds a new task to the queue if capacity permits."""
        if len(self.buffer) >= self.buffer_size:
            return False
        
        task = {
            "name": name,
            "priority": priority,
            "timestamp": time.time()
        }
        self.buffer.append(task)
        return True

    def get_pending_tasks(self) -> List[Dict[str, Any]]:
        """Returns the current task queue sorted by priority."""
        return sorted(self.buffer, key=lambda x: x['priority'], reverse=True)

    def clear_completed(self, task_name: Optional[str] = None) -> int:
        """Removes tasks from the queue and returns count of removed items."""
        initial_count = len(self.buffer)
        if task_name:
            self.buffer = [t for t in self.buffer if t['name'] != task_name]
        else:
            self.buffer = []
        
        return initial_count - len(self.buffer)