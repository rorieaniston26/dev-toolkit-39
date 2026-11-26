from typing import Dict, Any, Optional, Callable

class DataHandler:
    """Handles incoming data payloads for dev-toolkit-39."""

    def __init__(self, callback: Optional[Callable[[Dict[str, Any]], None]] = None) -> None:
        self.callback = callback
        self.buffer: Dict[str, Any] = {}

    def process_payload(self, data: Dict[str, Any]) -> bool:
        """Validates and stores payload in the internal buffer."""
        if not isinstance(data, dict) or "id" not in data:
            return False

        self.buffer[str(data["id"])] = data

        if self.callback:
            self.callback(data)
            
        return True

    def get_data(self, item_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves an item from the buffer by its ID."""
        return self.buffer.get(item_id)

    def clear_buffer(self) -> None:
        """Clears all stored entries in the buffer."""
        self.buffer.clear()

def default_callback(data: Dict[str, Any]) -> None:
    """Example callback for logging processed data."""
    print(f"Processed item: {data.get('id')}")