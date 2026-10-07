import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dev-toolkit-39")

class DataProcessor:
    """Processes batches of incoming data with strict input validation."""

    def __init__(self):
        self.processed_count = 0
        self.failed_count = 0

    def validate_payload(self, payload: dict) -> bool:
        """Validates the input payload schema and values."""
        if not isinstance(payload, dict):
            return False

        required_keys = {"id", "metric", "value"}
        if not required_keys.issubset(payload.keys()):
            return False

        if not isinstance(payload["id"], int) or payload["id"] <= 0:
            return False

        if not isinstance(payload["metric"], str) or not payload["metric"].strip():
            return False

        if not isinstance(payload["value"], (int, float)) or payload["value"] < 0:
            return False

        return True

    def process_batch(self, batch: list) -> dict:
        """Processes a batch of payloads, validating each item first."""
        results = []
        self.processed_count = 0
        self.failed_count = 0

        if not isinstance(batch, list):
            raise ValueError("Batch must be a list of items")

        for index, item in enumerate(batch):
            if not self.validate_payload(item):
                logger.warning(f"Invalid payload at index {index}: {item}")
                self.failed_count += 1
                continue

            # Process the valid item (e.g., standardizing data)
            processed_item = {
                "id": item["id"],
                "metric": item["metric"].strip().lower(),
                "value": float(item["value"]),
                "status": "processed"
            }
            results.append(processed_item)
            self.processed_count += 1

        return {
            "success": True,
            "processed": self.processed_count,
            "failed": self.failed_count,
            "data": results
        }
