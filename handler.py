from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class DataHandler:
    """Handles incoming raw data processing and validation."""

    def __init__(self, target_schema: Dict[str, Any]) -> None:
        self.schema = target_schema

    def validate_payload(self, payload: Dict[str, Any]) -> bool:
        """Validates payload against predefined schema keys."""
        for key in self.schema.keys():
            if key not in payload:
                logger.warning(f"Missing required key: {key}")
                return False
        return True

    def process(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Processes valid data packets into a sanitized dictionary."""
        if not self.validate_payload(data):
            return None

        try:
            sanitized = {k: str(v).strip() for k, v in data.items()}
            logger.info("Data processed successfully")
            return sanitized
        except Exception as e:
            logger.error(f"Processing error: {e}")
            return None

def create_handler(config: Dict[str, Any]) -> DataHandler:
    """Factory function for initializing DataHandler instances."""
    schema = config.get("schema", {})
    return DataHandler(target_schema=schema)