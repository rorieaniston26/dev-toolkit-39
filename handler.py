from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class DataHandler:
    """Handles incoming data payloads and routes them to processors."""

    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings = settings
        self.is_active = True

    def process_payload(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Validate and sanitize incoming dictionary data.

        Args:
            data: The raw input dictionary to be processed.

        Returns:
            A processed dictionary or None if validation fails.
        """
        if not isinstance(data, dict):
            logger.error("Invalid payload format: expected dict")
            return None

        try:
            sanitized = {k: str(v).strip() for k, v in data.items() if v is not None}
            return sanitized
        except Exception as e:
            logger.exception(f"Processing error: {e}")
            return None

    def shutdown(self) -> None:
        """Graceful shutdown of the handler instance."""
        self.is_active = False
        logger.info("Handler shut down successfully")