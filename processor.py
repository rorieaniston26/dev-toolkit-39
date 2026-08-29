import json
from typing import List, Dict, Any

class DataProcessor:
    """A simple processor for cleaning and reorganizing data."""

    def __init__(self, raw_data: List[Dict[str, Any]]) -> None:
        self.raw_data = raw_data
        self.cleaned_data: List[Dict[str, Any]] = []

    def clean_data(self) -> None:
        """Remove entries with missing values and normalize keys."""
        for item in self.raw_data:
            if item.get("value") is not None:
                cleaned = {
                    "id": item.get("id", 0),
                    "value": float(item["value"]),
                    "category": item.get("category", "default")
                }
                self.cleaned_data.append(cleaned)

    def reorganize_data(self) -> None:
        """Sort data by value and group by category."""
        self.cleaned_data.sort(key=lambda x: x["value"], reverse=True)

    def calculate_stats(self) -> Dict[str, float]:
        """Compute basic statistics on cleaned data."""
        if not self.cleaned_data:
            return {"count": 0, "sum": 0.0, "avg": 0.0}
        values = [item["value"] for item in self.cleaned_data]
        total = sum(values)
        count = len(values)
        avg = total / count
        return {"count": count, "sum": total, "avg": avg}

    def filter_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Return subset of data matching category."""
        return [item for item in self.cleaned_data if item["category"] == category]

    def save_to_file(self, filepath: str) -> None:
        """Save processed data to JSON file."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.cleaned_data, f, indent=2)

    def load_from_file(self, filepath: str) -> None:
        """Load data from JSON file (for reorganization)."""
        with open(filepath, "r", encoding="utf-8") as f:
            self.cleaned_data = json.load(f)

# Demonstration
if __name__ == "__main__":
    sample = [
        {"id": 1, "value": 42.5, "category": "A"},
        {"id": 2, "value": 17, "category": "B"},
        {"id": 3, "value": None, "category": "A"},
        {"id": 4, "value": 99.9, "category": "A"},
    ]
    proc = DataProcessor(sample)
    proc.clean_data()
    proc.reorganize_data()
    stats = proc.calculate_stats()
    print("Stats:", stats)
    filtered = proc.filter_by_category("A")
    print("Filtered A:", filtered)
    proc.save_to_file("processed.json")
    print("Data saved to processed.json")