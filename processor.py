import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles input data processing with robust error checks."""

    def process_payload(self, data: Optional[dict]) -> dict:
        try:
            if not isinstance(data, dict):
                raise ValueError(f"Invalid input type: {type(data).__name__}")
            
            if "id" not in data:
                raise KeyError("Missing mandatory key: id")

            # Simulate processing logic
            result = {
                "status": "success",
                "processed_id": data["id"],
                "value": data.get("value", 0)
            }
            return result

        except ValueError as ve:
            logger.error(f"Validation failure: {ve}")
            return {"status": "error", "message": str(ve)}
        except KeyError as ke:
            logger.error(f"Schema constraint failure: {ke}")
            return {"status": "error", "message": f"Schema violation: {ke}"}
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}", exc_info=True)
            return {"status": "error", "message": "internal system failure"}

    def batch_process(self, items: list) -> list:
        if not isinstance(items, list):
            return []
        
        results = []
        for item in items:
            results.append(self.process_payload(item))
        return results