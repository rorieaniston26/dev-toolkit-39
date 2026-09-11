import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

class DataProcessor:
    """Handles data cleaning and transformation for toolkit pipelines."""

    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        self.is_active = True

    def clean_records(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Removes empty values and filters invalid entries."""
        if not self.is_active:
            logger.warning("Processor is inactive, returning empty list.")
            return []

        cleaned = []
        for record in data:
            # filter entries with missing keys
            if all(record.values()):
                cleaned.append({k: v.strip() if isinstance(v, str) else v for k, v in record.items()})
        
        logger.info(f"Processed {len(cleaned)} records.")
        return cleaned

    def reorganize_structure(self, data: List[Dict[str, Any]], key_field: str) -> Dict[str, Any]:
        """Reorganizes list of dicts into a keyed dictionary mapping."""
        result = {}
        for item in data:
            key = item.get(key_field)
            if key:
                result[key] = item
        return result

if __name__ == '__main__':
    proc = DataProcessor({"mode": "strict"})
    sample = [{"id": "1", "name": " dev "}, {"id": "2", "name": ""}]
    print(proc.clean_records(sample))